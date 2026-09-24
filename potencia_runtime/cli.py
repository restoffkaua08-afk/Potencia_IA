from __future__ import annotations

import argparse
import json
from pathlib import Path

from .server import RuntimeServer
from .state import RuntimeState


def main() -> None:
    parser = argparse.ArgumentParser(prog="potencia", description="Potencia Runtime")
    sub = parser.add_subparsers(dest="command", required=True)
    serve = sub.add_parser("runtime", help="start the local Potencia Runtime")
    serve.add_argument("--workspace", default=".", help="workspace/project root")
    serve.add_argument("--port", type=int, default=43173)
    status = sub.add_parser("status", help="show local runtime state")
    status.add_argument("--workspace", default=".")
    args = parser.parse_args()
    workspace = Path(args.workspace).expanduser().resolve()
    if args.command == "status":
        print(json.dumps(RuntimeState(workspace).snapshot(), ensure_ascii=False, indent=2))
        return
    RuntimeServer(workspace, port=args.port).serve_forever()
