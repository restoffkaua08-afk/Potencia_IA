from __future__ import annotations

import json
import os
import secrets
import sys
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


class RuntimeServer:
    def __init__(self, workspace: Path, host: str = "127.0.0.1", port: int = 43173):
        self.workspace = workspace.resolve()
        self.token = load_or_create_token()
        self.state = RuntimeState(self.workspace)
        self.clients: list[Any] = []
        self.clients_lock = Lock()
        server = self

        class Handler(BaseHTTPRequestHandler):
            server_version = "PotenciaRuntime/0.3"

            def log_message(self, fmt: str, *args: Any) -> None:
                return

            def _authorized(self) -> bool:
                return self.headers.get(TOKEN_HEADER, "") == f"Bearer {server.token}"

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
                    self.end_headers()
                    with server.clients_lock:
                        server.clients.append(self)
                    try:
                        payload = json.dumps(server.state.snapshot(), ensure_ascii=False)
                        self.wfile.write(f"event: snapshot\\ndata: {payload}\\n\\n".encode("utf-8"))
                        self.wfile.flush()
                        while True:
                            if self.rfile.peek(1):
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
                    length = int(self.headers.get("Content-Length", "0"))
                    body = json.loads(self.rfile.read(length) or b"{}")
                except (ValueError, json.JSONDecodeError):
                    self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid_json"})
                    return
                command = body.get("command")
                if command == "ping":
                    event = server.state.emit("runtime_ping", {"source": "desktop"})
                    server.broadcast(event)
                    self._json(HTTPStatus.OK, {"ok": True, "event": event})
                    return
                if command == "refresh":
                    snapshot = server.state.snapshot()
                    event = server.state.emit("runtime_snapshot_refreshed", {"workspace": str(server.workspace)})
                    server.broadcast(event)
                    self._json(HTTPStatus.OK, {"ok": True, "snapshot": snapshot, "event": event})
                    return
                self._json(HTTPStatus.BAD_REQUEST, {"error": "unsupported_command"})

        self.httpd = ThreadingHTTPServer((host, port), Handler)

    def broadcast(self, event: dict[str, Any]) -> None:
        raw = f"event: {event['type']}\\ndata: {json.dumps(event, ensure_ascii=False)}\\n\\n".encode("utf-8")
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
        self.state.emit("runtime_connected", {"port": self.httpd.server_port})
        self.httpd.serve_forever()

    def shutdown(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()
