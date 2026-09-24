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
        return CommandResult(list(argv), 0, stdout="ok")

    def spawn(self, argv, *, cwd, log_path):
        self.spawned.append((list(argv), cwd, log_path))
        return 4321


def make_workspace(root):
    for path in (
        "CLAUDE.md",
        "AGENTS.md",
        "MANIFEST.json",
        "bootstrap/BOOTSTRAP.md",
        "bootstrap/AGENT-POLICY.md",
        "bootstrap/COMPONENT-MATRIX.md",
    ):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("fixture", encoding="utf-8")
    for path in (".claude/skills", ".claude/agents", ".claude/commands"):
        (root / path).mkdir(parents=True, exist_ok=True)


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
