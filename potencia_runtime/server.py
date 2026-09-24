from __future__ import annotations

import hmac
import json
import os
import secrets
import sys
import time
from threading import Event
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from typing import Any

from .state import RuntimeState

TOKEN_HEADER = "Authorization"


def token_path() -> Path:
    if sys.platform == "win32":
        root = Path(os.environ.get("APPDATA", Path.home() / "AppData/Roaming"))
    elif sys.platform == "darwin":
        root = Path.home() / "Library/Application Support"
    else:
        root = Path.home() / ".config"
    return root / "Potencia" / "runtime.token"


def load_or_create_token() -> str:
    path = token_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        token = path.read_text(encoding="utf-8").strip()
        if token:
            return token
    except OSError:
        pass
    token = secrets.token_urlsafe(32)
    path.write_text(token, encoding="utf-8")
    try:
        path.chmod(0o600)
    except OSError:
        pass
    return token


def _merge_item(items: list[dict[str, Any]], item: dict[str, Any]) -> list[dict[str, Any]]:
    item_id = item.get("id")
    if not isinstance(item_id, str) or not item_id:
        raise ValueError("item.id must be a non-empty string")
    updated = [existing for existing in items if existing.get("id") != item_id]
    updated.append(item)
    return updated


class RuntimeServer:
    def __init__(self, workspace: Path, host: str = "127.0.0.1", port: int = 43173):
        self.workspace = workspace.resolve()
        self.token = load_or_create_token()
        self.state = RuntimeState(self.workspace)
        self.clients: list[Any] = []
        self.clients_lock = Lock()
        self.stop_event = Event()
        server = self

        class Handler(BaseHTTPRequestHandler):
            server_version = "PotenciaRuntime/0.3"

            def log_message(self, fmt: str, *args: Any) -> None:
                return

            def _authorized(self) -> bool:
                return hmac.compare_digest(self.headers.get(TOKEN_HEADER, ""), f"Bearer {server.token}")

            def _json(self, status: int, body: dict[str, Any]) -> None:
                raw = json.dumps(body, ensure_ascii=False).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(raw)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(raw)

            def do_GET(self) -> None:
                if self.path == "/health":
                    self._json(HTTPStatus.OK, {
                        "ok": True,
                        "service": "potencia-runtime",
                        "protocol_version": "1",
                        "potencia_version": "0.3.0",
                        "workspace": str(server.workspace),
                    })
                    return
                if not self._authorized():
                    self._json(HTTPStatus.UNAUTHORIZED, {"error": "unauthorized"})
                    return
                if self.path == "/v1/state":
                    self._json(HTTPStatus.OK, server.state.snapshot())
                    return
                if self.path == "/v1/events":
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                    self.send_header("Cache-Control", "no-cache")
                    self.send_header("Connection", "keep-alive")
                    self.send_header("X-Accel-Buffering", "no")
                    self.end_headers()
                    with server.clients_lock:
                        server.clients.append(self)
                    try:
                        payload = json.dumps(server.state.snapshot(), ensure_ascii=False)
                        self.wfile.write(f"event: snapshot\ndata: {payload}\n\n".encode("utf-8"))
                        self.wfile.flush()
                        while not server.stop_event.wait(15):
                            try:
                                self.wfile.write(b": heartbeat\n\n")
                                self.wfile.flush()
                            except (BrokenPipeError, ConnectionResetError, OSError):
                                break
                    except (BrokenPipeError, ConnectionResetError, OSError):
                        pass
                    finally:
                        with server.clients_lock:
                            if self in server.clients:
                                server.clients.remove(self)
                    return
                self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

            def do_POST(self) -> None:
                if not self._authorized():
                    self._json(HTTPStatus.UNAUTHORIZED, {"error": "unauthorized"})
                    return
                if self.path != "/v1/commands":
                    self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})
                    return
                try:
                    if self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower() != "application/json":
                        raise ValueError("content type must be application/json")
                    length = int(self.headers.get("Content-Length", "0"))
                    if length <= 0 or length > 1_000_000:
                        raise ValueError("invalid content length")
                    body = json.loads(self.rfile.read(length) or b"{}")
                    if not isinstance(body, dict):
                        raise ValueError("request body must be an object")
                except (ValueError, json.JSONDecodeError):
                    self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid_json"})
                    return

                try:
                    result = server.execute_command(body)
                except ValueError as exc:
                    self._json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
                    return

                if result is None:
                    self._json(HTTPStatus.BAD_REQUEST, {"error": "unsupported_command"})
                    return
                self._json(HTTPStatus.OK, {"ok": True, **result})

        self.httpd = ThreadingHTTPServer((host, port), Handler)
        self.httpd.daemon_threads = True
        self.httpd._BaseServer__is_shut_down.set()

    def execute_command(self, body: dict[str, Any]) -> dict[str, Any] | None:
        if not isinstance(body, dict):
            raise ValueError("command must be an object")
        command = body.get("command")
        if command == "ping":
            event = self.state.emit("runtime_ping", {"source": "desktop"})
            self.broadcast(event)
            return {"event": event}

        if command == "refresh":
            snapshot = self.state.snapshot()
            event = self.state.emit("runtime_snapshot_refreshed", {"workspace": str(self.workspace)})
            self.broadcast(event)
            return {"snapshot": snapshot, "event": event}

        collection_by_command = {
            "agent.upsert": "agents",
            "skill.upsert": "activeSkills",
            "plugin.upsert": "activePlugins",
            "project.upsert": "projects",
            "task.upsert": "tasks",
            "verification.upsert": "verifications",
            "tool.upsert": "tools",
        }
        collection = collection_by_command.get(command)
        if collection:
            item = body.get("item")
            if not isinstance(item, dict):
                raise ValueError("item must be an object")
            current = self.state.snapshot().get(collection, [])
            if not isinstance(current, list):
                raise ValueError(f"state collection {collection} is invalid")
            updated = _merge_item([x for x in current if isinstance(x, dict)], item)
            self.state.update({collection: updated})
            event = self.state.emit(f"{command.replace('.', '_')}_changed", {"item": item})
            self.broadcast(event)
            return {"event": event}

        remove_collections = {
            "agent.remove": "agents",
            "skill.remove": "activeSkills",
            "plugin.remove": "activePlugins",
            "project.remove": "projects",
            "task.remove": "tasks",
            "verification.remove": "verifications",
            "tool.remove": "tools",
        }
        collection = remove_collections.get(command)
        if collection:
            item_id = body.get("id")
            if not isinstance(item_id, str) or not item_id:
                raise ValueError("id must be a non-empty string")
            current = self.state.snapshot().get(collection, [])
            if not isinstance(current, list):
                raise ValueError(f"state collection {collection} is invalid")
            updated = [x for x in current if isinstance(x, dict) and x.get("id") != item_id]
            self.state.update({collection: updated})
            event = self.state.emit(f"{command.replace('.', '_')}_changed", {"id": item_id})
            self.broadcast(event)
            return {"event": event}

        return None

    def broadcast(self, event: dict[str, Any]) -> None:
        raw = f"event: {event['type']}\ndata: {json.dumps(event, ensure_ascii=False)}\n\n".encode("utf-8")
        with self.clients_lock:
            clients = list(self.clients)
        dead = []
        for client in clients:
            try:
                client.wfile.write(raw)
                client.wfile.flush()
            except (BrokenPipeError, ConnectionResetError, OSError):
                dead.append(client)
        if dead:
            with self.clients_lock:
                self.clients[:] = [c for c in self.clients if c not in dead]

    def serve_forever(self) -> None:
        if self.stop_event.is_set():
            return
        self.state.emit("runtime_connected", {"port": self.httpd.server_port})
        try:
            self.httpd.serve_forever()
        except (OSError, ValueError):
            if not self.stop_event.is_set():
                raise

    def shutdown(self) -> None:
        self.stop_event.set()
        if not self.httpd._BaseServer__is_shut_down.is_set():
            self.httpd.shutdown()
        self.httpd.server_close()
