import json
import tempfile
import unittest
from pathlib import Path

from potencia_runtime.bootstrap import BootstrapRunner, CommandResult, redact


class FakeRunner:
    def __init__(self, available):
        self.available = set(available)
        self.calls = []
        self.spawned = []

    def which(self, name):
        return f"/fake/{name}" if name in self.available else None

    def run(self, argv, *, cwd=None, timeout=120):
        self.calls.append((list(argv), cwd, timeout))
        stdout = "ok"
        if argv == ["claude", "mcp", "list"]:
            stdout = "codex-subagent stdio"
        if argv == ["codex", "plugin", "list"]:
            stdout = "superpowers"
        return CommandResult(list(argv), 0, stdout=stdout)

    def spawn(self, argv, *, cwd, log_path):
        self.spawned.append((list(argv), cwd, log_path))
        return 4321


def make_workspace(root):
    manifest = {
        "name": "potencia-IA",
        "version": "0.4.0",
        "projects": ["01-superpowers"],
        "plugins": ["omni-route", "headroom"],
    }
    for path, content in (
        ("CLAUDE.md", "fixture"),
        ("AGENTS.md", "fixture"),
        ("MANIFEST.json", json.dumps(manifest)),
        ("bootstrap/BOOTSTRAP.md", "fixture"),
        ("bootstrap/AGENT-POLICY.md", "fixture"),
        ("bootstrap/COMPONENT-MATRIX.md", "fixture"),
    ):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    for path in (".claude/skills", ".claude/agents", ".claude/commands"):
        (root / path).mkdir(parents=True, exist_ok=True)


def make_claude_registry(home):
    registry = home / ".claude" / "plugins"
    registry.mkdir(parents=True)
    entries = {}
    for plugin_key in (
        "superpowers@superpowers-marketplace",
        "vv-harness",
        "security-hooks@atompilot-security-hooks",
        "superharness",
    ):
        install_path = home / "installed" / plugin_key.replace("@", "-")
        install_path.mkdir(parents=True)
        entries[plugin_key] = [{"installPath": str(install_path)}]
    (registry / "installed_plugins.json").write_text(
        json.dumps({"plugins": entries}),
        encoding="utf-8",
    )


class BootstrapTests(unittest.TestCase):
    def test_successful_local_components_still_records_host_plugin_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_workspace(root)
            runner = FakeRunner({"headroom", "omniroute", "rtk", "graphify", "shux"})
            checker = lambda url, **kwargs: (True, {"data": [{"id": "auto"}]})
            state = BootstrapRunner(root, runner=runner, checker=checker, sleep=lambda _: None).bootstrap()

            self.assertEqual(state["components"]["headroom"]["status"], "VERIFIED")
            self.assertEqual(state["components"]["omniroute"]["status"], "VERIFIED")
            self.assertEqual(state["components"]["rtk"]["status"], "VERIFIED")
            self.assertEqual(state["components"]["graphify"]["status"], "VERIFIED")
            self.assertEqual(state["components"]["superharness"]["status"], "VERIFIED")
            self.assertEqual(state["final_gate"]["status"], "BLOCKED")
            self.assertIn("superpowers", state["final_gate"]["blocked_components"])
            self.assertTrue((root / ".potencia/runtime-state.json").is_file())
            commands = [entry["argv"] for entry in state["components"]["headroom"]["commands"]]
            self.assertIn(["headroom", "mcp", "status"], commands)

    def test_claude_host_requires_plugin_registry_and_mcp_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "workspace"
            home = Path(tmp) / "home"
            root.mkdir()
            make_workspace(root)
            make_claude_registry(home)
            runner = FakeRunner({"claude", "uv", "headroom", "omniroute", "rtk", "graphify", "shux"})
            checker = lambda url, **kwargs: (True, {"data": [{"id": "auto"}]})

            state = BootstrapRunner(
                root,
                runner=runner,
                checker=checker,
                sleep=lambda _: None,
                home=home,
            ).bootstrap()

            for name in ("superpowers", "vv-harness", "security-hooks", "superharness", "codex-subagents"):
                self.assertEqual(state["components"][name]["status"], "VERIFIED", name)
            self.assertEqual(state["final_gate"]["status"], "VERIFIED")
            mcp_commands = [entry["argv"] for entry in state["components"]["codex-subagents"]["commands"]]
            self.assertIn(["claude", "mcp", "list"], mcp_commands)

    def test_codex_host_does_not_fake_claude_only_components(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_workspace(root)
            runner = FakeRunner({"codex", "headroom", "omniroute", "rtk", "graphify", "shux"})
            checker = lambda url, **kwargs: (True, {"data": [{"id": "auto"}]})

            state = BootstrapRunner(root, runner=runner, checker=checker, sleep=lambda _: None).bootstrap()

            self.assertEqual(state["components"]["superpowers"]["status"], "VERIFIED")
            for name in ("vv-harness", "security-hooks", "codex-subagents"):
                self.assertEqual(state["components"][name]["status"], "BLOCKED", name)
            self.assertEqual(state["final_gate"]["status"], "BLOCKED")

    def test_missing_installers_are_explicitly_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_workspace(root)
            state = BootstrapRunner(root, runner=FakeRunner(set()), sleep=lambda _: None).bootstrap()

            for name in ("headroom", "omniroute", "rtk", "graphify", "superharness"):
                self.assertEqual(state["components"][name]["status"], "BLOCKED")
            saved = json.loads((root / ".potencia/runtime-state.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["final_gate"]["status"], "BLOCKED")
            self.assertTrue(saved["final_gate"]["blocked_components"])

    def test_sensitive_command_output_is_redacted(self):
        value = "api_key=secret123 bearer abc.def password=hunter2"
        result = redact(value)
        self.assertNotIn("secret123", result)
        self.assertNotIn("abc.def", result)
        self.assertNotIn("hunter2", result)
        self.assertIn("[REDACTED]", result)


if __name__ == "__main__":
    unittest.main()
