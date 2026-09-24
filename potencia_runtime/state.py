from __future__ import annotations

import json
import os
from pathlib import Path
from threading import Lock
from time import time
from typing import Any


def default_state(workspace: Path) -> dict[str, Any]:
    return {
        "potencia_version": "0.3.0",
        "protocol_version": "1",
        "connection": {"status": "active"},
        "workspace": str(workspace.resolve()),
        "agents": [],
        "activeSkills": [],
        "activePlugins": [],
        "projects": [],
        "tools": [],
        "tasks": [],
        "verifications": [],
        "events": [],
        "updated_at": time(),
    }


class RuntimeState:
    def __init__(self, workspace: Path):
        self.workspace = workspace.resolve()
        self.path = self.workspace / ".potencia" / "runtime-state.json"
        self._lock = Lock()
        self._state = self._load()

    def _load(self) -> dict[str, Any]:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("potencia_version", "0.3.0")
                data.setdefault("protocol_version", "1")
                data["workspace"] = str(self.workspace)
                return data
        except (OSError, json.JSONDecodeError):
            pass
        return default_state(self.workspace)

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return json.loads(json.dumps(self._state))

    def update(self, patch: dict[str, Any]) -> dict[str, Any]:
        with self._lock:
            self._state.update(patch)
            self._state["updated_at"] = time()
            self._persist()
            return json.loads(json.dumps(self._state))

    def emit(self, event_type: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        event = {
            "id": f"evt-{int(time() * 1000)}",
            "type": event_type,
            "timestamp": time(),
            "payload": payload or {},
        }
        with self._lock:
            events = self._state.setdefault("events", [])
            events.append(event)
            del events[:-500]
            self._state["updated_at"] = time()
            self._persist()
        return event

    def _persist(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self._state, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, self.path)
