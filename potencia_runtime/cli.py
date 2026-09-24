from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .bootstrap import BootstrapRunner
from .server import RuntimeServer, load_or_create_token, token_path
from .state import RuntimeState


def _status(workspace: Path) -> int:
    print(json.dumps(RuntimeState(workspace).snapshot(), ensure_ascii=False, indent=2))
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


def _bootstrap(workspace: Path, compact: bool) -> int:
    state = BootstrapRunner(workspace).bootstrap()
    result = {
        "status": state["final_gate"]["status"],
        "blocked_components": state["final_gate"]["blocked_components"],
        "state_file": state["final_gate"]["evidence_file"],
    }
    print(json.dumps(result if compact else state, ensure_ascii=False, indent=0 if compact else 2))
    return 0 if result["status"] == "VERIFIED" else 2


def main() -> None:
    parser = argparse.ArgumentParser(prog="potencia", description="Potencia Runtime")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    serve = sub.add_parser("runtime", help="start the local Potencia Runtime")
    serve.add_argument("--workspace", default=".")
    serve.add_argument("--port", type=int, default=43173)

    status = sub.add_parser("status", help="show local runtime state")
    status.add_argument("--workspace", default=".")

    doctor = sub.add_parser("doctor", help="validate the local Potencia installation")
    doctor.add_argument("--workspace", default=".")

    bootstrap = sub.add_parser("bootstrap", help="install, activate and verify all components")
    bootstrap.add_argument("--workspace", default=".")
    bootstrap.add_argument("--compact", action="store_true")

    args = parser.parse_args()
    workspace = Path(args.workspace).expanduser().resolve()

    if args.command == "status":
        raise SystemExit(_status(workspace))
    if args.command == "doctor":
        raise SystemExit(_doctor(workspace))
    if args.command == "bootstrap":
        raise SystemExit(_bootstrap(workspace, args.compact))

    RuntimeServer(workspace, port=args.port).serve_forever()


if __name__ == "__main__":
    main()
