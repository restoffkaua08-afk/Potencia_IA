from __future__ import annotations

import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable
from urllib.error import URLError
from urllib.request import Request, urlopen

VERSION = "0.4.0"
VERIFIED = "VERIFIED"
BLOCKED = "BLOCKED"

_SECRET_RE = re.compile(r"(?i)(api[_-]?key|token|secret|password)(\s*[:=]\s*)[^\s,;]+")


def redact(value: str) -> str:
    value = _SECRET_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}[REDACTED]", value)
    return re.sub(r"(?i)bearer\s+[A-Za-z0-9._-]+", "Bearer [REDACTED]", value)


@dataclass
class CommandResult:
    argv: list[str]
    returncode: int
    stdout: str = ""
    stderr: str = ""
    duration_ms: int = 0

    @property
    def ok(self) -> bool:
        return self.returncode == 0


class CommandRunner:
    def which(self, name: str) -> str | None:
        return shutil.which(name)

    def run(self, argv: list[str], *, cwd: Path | None = None, timeout: int = 120) -> CommandResult:
        started = time.time()
        try:
            result = subprocess.run(
                argv,
                cwd=str(cwd) if cwd else None,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
                shell=False,
            )
            return CommandResult(
                list(argv),
                result.returncode,
                redact(result.stdout[-4000:]),
                redact(result.stderr[-4000:]),
                int((time.time() - started) * 1000),
            )
        except FileNotFoundError as exc:
            return CommandResult(list(argv), 127, stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            return CommandResult(list(argv), 124, redact(stdout[-4000:]), redact(stderr[-4000:]))

    def spawn(self, argv: list[str], *, cwd: Path, log_path: Path) -> int:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as log:
            process = subprocess.Popen(
                argv,
                cwd=str(cwd),
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=subprocess.STDOUT,
                shell=False,
                start_new_session=True,
            )
        return process.pid


def http_json(
    url: str,
    *,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    timeout: int = 8,
) -> tuple[bool, dict[str, Any]]:
    payload = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Accept": "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    try:
        with urlopen(Request(url, data=payload, headers=headers, method=method), timeout=timeout) as response:
            raw = response.read(1_000_000).decode("utf-8", errors="replace")
            data = json.loads(raw) if raw else {}
            return response.status < 400, data if isinstance(data, dict) else {"raw": raw[:1000]}
    except (OSError, URLError, ValueError, json.JSONDecodeError) as exc:
        return False, {"error": redact(str(exc))}


class BootstrapRunner:
    REQUIRED = (
        "contracts",
        "local-skills",
        "headroom",
        "omniroute",
        "rtk",
        "graphify",
        "superpowers",
        "vv-harness",
        "security-hooks",
        "superharness",
        "codex-subagents",
    )

    def __init__(
        self,
        workspace: Path,
        *,
        runner: CommandRunner | None = None,
        checker: Callable[..., tuple[bool, dict[str, Any]]] = http_json,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.workspace = workspace.resolve()
        self.potencia = self.workspace / ".potencia"
        self.state_path = self.potencia / "runtime-state.json"
        self.runner = runner or CommandRunner()
        self.checker = checker
        self.sleep = sleep
        self.host: dict[str, Any] = {}
        self.components: dict[str, dict[str, Any]] = {}

    def bootstrap(self) -> dict[str, Any]:
        started = time.time()
        self.potencia.mkdir(parents=True, exist_ok=True)
        self.host = self._host()
        self._contracts()
        self._local_skills()
        self._headroom()
        self._omniroute()
        self._rtk()
        self._graphify()
        self._superharness()
        self._host_plugins()
        self._blocked("vv-harness", "VV Harness is a native host plugin; the current host must install and trust it")
        self._blocked("security-hooks", "Security Hooks require host plugin trust or their standalone installer")
        self._blocked("codex-subagents", "Codex Subagents requires host-specific integration verification")
        blocked = [name for name, item in self.components.items() if item["status"] != VERIFIED]
        state = {
            "potencia_version": VERSION,
            "protocol_version": "1",
            "workspace": str(self.workspace),
            "bootstrap": {
                "status": BLOCKED if blocked else VERIFIED,
                "started_at": started,
                "completed_at": time.time(),
                "host": self.host,
                "required_components": list(self.REQUIRED),
                "blocked_components": blocked,
            },
            "components": self.components,
            "final_gate": {
                "status": BLOCKED if blocked else VERIFIED,
                "all_required_components_verified": not blocked,
                "blocked_components": blocked,
                "evidence_file": str(self.state_path),
            },
        }
        self._write(state)
        return state

    def _host(self) -> dict[str, Any]:
        return {
            "os": platform.system(),
            "python": sys.version.split()[0],
            "claude": bool(self.runner.which("claude")),
            "codex": bool(self.runner.which("codex")),
            "npm": bool(self.runner.which("npm")),
            "uv": bool(self.runner.which("uv")),
            "pipx": bool(self.runner.which("pipx")),
            "cargo": bool(self.runner.which("cargo")),
            "brew": bool(self.runner.which("brew")),
            "winget": bool(self.runner.which("winget")),
        }

    def _set(self, name: str, status: str, phase: str, *, evidence: list[Any] | None = None, error: str | None = None, **extra: Any) -> None:
        current = self.components.get(name, {})
        current.update({"id": name, "status": status, "required": True, "phase": phase, "evidence": evidence or []})
        if error:
            current["error"] = redact(error)
        current.update(extra)
        self.components[name] = current

    def _run(self, name: str, argv: list[str], *, cwd: Path | None = None, timeout: int = 120) -> CommandResult:
        result = self.runner.run(argv, cwd=cwd, timeout=timeout)
        self.components.setdefault(name, {}).setdefault("commands", []).append({
            "argv": list(argv),
            "returncode": result.returncode,
            "ok": result.ok,
            "duration_ms": result.duration_ms,
            "stdout": result.stdout,
            "stderr": result.stderr,
        })
        return result

    def _contracts(self) -> None:
        paths = ("CLAUDE.md", "AGENTS.md", "MANIFEST.json", "bootstrap/BOOTSTRAP.md", "bootstrap/AGENT-POLICY.md", "bootstrap/COMPONENT-MATRIX.md")
        missing = [path for path in paths if not (self.workspace / path).is_file()]
        self._set("contracts", VERIFIED if not missing else BLOCKED, "VERIFIED" if not missing else BLOCKED, evidence=[{"path": p, "exists": p not in missing} for p in paths], error="missing: " + ", ".join(missing) if missing else None)

    def _local_skills(self) -> None:
        paths = (self.workspace / ".claude" / "skills", self.workspace / ".claude" / "agents", self.workspace / ".claude" / "commands")
        evidence = [{"path": str(p.relative_to(self.workspace)), "exists": p.is_dir()} for p in paths]
        ok = all(item["exists"] for item in evidence)
        self._set("local-skills", VERIFIED if ok else BLOCKED, "ACTIVE" if ok else BLOCKED, evidence=evidence, error=None if ok else "local skill, agent or command directory is missing")

    def _headroom(self) -> None:
        evidence: list[Any] = []
        if not self.runner.which("headroom") and self.runner.which("uv"):
            self._run("headroom", ["uv", "tool", "install", "--python", "3.13", "headroom-ai[all]"], timeout=300)
        if not self.runner.which("headroom"):
            self._set("headroom", BLOCKED, "BLOCKED", evidence=evidence, error="headroom unavailable after automatic install")
            return
        for argv in (
            ["headroom", "mcp", "install", "--force"],
            ["headroom", "install", "apply", "--preset", "persistent-service", "--providers", "all", "--scope", "user", "--mode", "token"],
            ["headroom", "install", "status"],
            ["headroom", "mcp", "status"],
        ):
            result = self._run("headroom", argv, timeout=180)
            evidence.append({"command": argv, "ok": result.ok})
        ok = all(item["ok"] for item in evidence)
        self._set("headroom", VERIFIED if ok else BLOCKED, "VERIFIED" if ok else BLOCKED, evidence=evidence, endpoint="http://127.0.0.1:8787", error=None if ok else "Headroom install/configuration/health failed")

    def _omniroute(self) -> None:
        evidence: list[Any] = []
        if not self.runner.which("omniroute") and self.runner.which("npm"):
            self._run("omniroute", ["npm", "install", "--global", "omniroute"], timeout=300)
        if not self.runner.which("omniroute"):
            self._set("omniroute", BLOCKED, "BLOCKED", evidence=evidence, error="omniroute unavailable after automatic install")
            return
        endpoint = "http://127.0.0.1:20128"
        healthy, response = self.checker(endpoint + "/v1/models")
        evidence.append({"url": endpoint + "/v1/models", "ok": healthy, "response": response})
        pid = None
        if not healthy:
            try:
                pid = self.runner.spawn(["omniroute"], cwd=self.workspace, log_path=self.potencia / "omniroute.log")
            except (OSError, ValueError) as exc:
                self._set("omniroute", BLOCKED, "BLOCKED", evidence=evidence, error=str(exc))
                return
            evidence.append({"spawned_pid": pid})
            for _ in range(15):
                self.sleep(1)
                healthy, response = self.checker(endpoint + "/v1/models")
                if healthy:
                    break
            evidence.append({"url": endpoint + "/v1/models", "ok": healthy, "response": response})
        data = response.get("data") if isinstance(response, dict) else None
        healthy = healthy and (data is None or isinstance(data, list))
        self._set("omniroute", VERIFIED if healthy else BLOCKED, "VERIFIED" if healthy else BLOCKED, evidence=evidence, endpoint=endpoint, pid=pid, error=None if healthy else "OmniRoute did not expose a healthy local models endpoint")

    def _rtk(self) -> None:
        evidence: list[Any] = []
        if not self.runner.which("rtk"):
            if self.host["os"] == "Windows" and self.runner.which("winget"):
                self._run("rtk", ["winget", "install", "--id", "rtk-ai.rtk", "--exact", "--accept-source-agreements", "--accept-package-agreements"], timeout=300)
            elif self.host["os"] == "Darwin" and self.runner.which("brew"):
                self._run("rtk", ["brew", "install", "rtk"], timeout=300)
            elif self.runner.which("cargo"):
                self._run("rtk", ["cargo", "install", "--git", "https://github.com/rtk-ai/rtk"], timeout=600)
        if not self.runner.which("rtk"):
            self._set("rtk", BLOCKED, "BLOCKED", evidence=evidence, error="rtk unavailable after automatic install")
            return
        for argv in (["rtk", "--version"], ["rtk", "gain"]):
            result = self._run("rtk", argv)
            evidence.append({"command": argv, "ok": result.ok})
        for host, flags in (("claude", []), ("codex", ["--codex"])):
            if self.host[host]:
                argv = ["rtk", "init", "-g", *flags]
                result = self._run("rtk", argv)
                evidence.append({"command": argv, "ok": result.ok, "host": host})
        ok = all(item["ok"] for item in evidence)
        self._set("rtk", VERIFIED if ok else BLOCKED, "VERIFIED" if ok else BLOCKED, evidence=evidence, error=None if ok else "RTK health or host hook activation failed")

    def _graphify(self) -> None:
        evidence: list[Any] = []
        if not self.runner.which("graphify") and self.runner.which("uv"):
            self._run("graphify", ["uv", "tool", "install", "--upgrade", "graphifyy"], timeout=300)
        if not self.runner.which("graphify"):
            self._set("graphify", BLOCKED, "BLOCKED", evidence=evidence, error="graphify unavailable after automatic install")
            return
        result = self._run("graphify", ["graphify", "--help"], timeout=60)
        evidence.append({"command": ["graphify", "--help"], "ok": result.ok})
        self._set("graphify", VERIFIED if result.ok else BLOCKED, "ACTIVE" if result.ok else BLOCKED, evidence=evidence, error=None if result.ok else "graphify health check failed")

    def _superharness(self) -> None:
        evidence: list[Any] = []
        if not self.runner.which("shux"):
            if self.runner.which("pipx"):
                self._run("superharness", ["pipx", "install", "superharness"], timeout=600)
            elif self.runner.which("uv"):
                self._run("superharness", ["uv", "tool", "install", "superharness"], timeout=600)
        if not self.runner.which("shux"):
            self._set("superharness", BLOCKED, "BLOCKED", evidence=evidence, error="superharness unavailable after automatic install")
            return
        for argv in (["shux", "--version"], ["shux", "doctor", "--project", str(self.workspace)]):
            result = self._run("superharness", argv, cwd=self.workspace, timeout=180)
            evidence.append({"command": argv, "ok": result.ok})
        ok = all(item["ok"] for item in evidence)
        self._set("superharness", VERIFIED if ok else BLOCKED, "VERIFIED" if ok else BLOCKED, evidence=evidence, error=None if ok else "superharness installation or doctor failed")

    def _host_plugins(self) -> None:
        if self.host["claude"]:
            commands = [
                "/plugin marketplace add obra/superpowers-marketplace",
                "/plugin install superpowers@superpowers-marketplace",
                "/plugin marketplace add oeftimie/vv-claude-harness",
                "/plugin install vv-harness",
                "/plugin marketplace add artificemachine/superharness",
                "/plugin install superharness",
                "/plugin marketplace add atompilot/claude-code-security-hooks",
                "/plugin install security-hooks@atompilot-security-hooks",
            ]
            self._set("superpowers", BLOCKED, "BLOCKED", evidence=[{"host": "claude", "commands": commands}], error="Claude plugin installation must be completed by the active Claude host")
        else:
            self._set("superpowers", BLOCKED, "BLOCKED", evidence=[{"host": "claude", "detected": False}], error="Claude Code host was not detected; Superpowers cannot be verified")

    def _blocked(self, name: str, reason: str) -> None:
        if name not in self.components:
            self._set(name, BLOCKED, "BLOCKED", error=reason)

    def _write(self, state: dict[str, Any]) -> None:
        temporary = self.state_path.with_suffix(".tmp")
        temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, self.state_path)


def run_bootstrap(workspace: Path) -> dict[str, Any]:
    return BootstrapRunner(workspace).bootstrap()
