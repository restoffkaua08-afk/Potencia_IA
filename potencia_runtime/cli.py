from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .server import RuntimeServer, load_or_create_token, token_path
from .state import RuntimeState


def _status(workspace: Path) -> int:
    state = RuntimeState(workspace).snapshot()
    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 0


def _doctor(workspace: Path) -> int:
    checks = {
        "python": sys.version.split()[0],
        "version": __version__,
        "workspace": str(workspace),
        "workspace_exists": workspace.exists(),
        "token_path": str(token_path()),
        "token_available": bool(load_or_create_token()),
        "state_path": str(workspace / ".potencia" / "runtime-state.json"),
    }
    checks["ok"] = bool(checks["workspace_exists"] and checks["token_available"])
    print(json.dumps(checks, ensure_ascii=False, indent=2))
    return 0 if checks["ok"] else 1


def main() -> None:
    parser = argparse.ArgumentParser(prog="potencia", description="Potencia Runtime")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)
    serve = sub.add_parser("runtime", help="start the local Potencia Runtime")
    serve.add_argument("--workspace", default=".", help="workspace/project root")
    serve.add_argument("--port", type=int, default=43173)
    status = sub.add_parser("status", help="show local runtime state")
    status.add_argument("--workspace", default=".")
    doctor = sub.add_parser("doctor", help="validate the local Potencia installation")
    doctor.add_argument("--workspace", default=".")

    args = parser.parse_args()
    workspace = Path(args.workspace).expanduser().resolve()

    if args.command == "status":
        raise SystemExit(_status(workspace))
    if args.command == "doctor":
        raise SystemExit(_doctor(workspace))

    RuntimeServer(workspace, port=args.port).serve_forever()


if __name__ == "__main__":
    main()
