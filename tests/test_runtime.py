import json
import tempfile
import unittest
from pathlib import Path

from potencia_runtime.server import RuntimeServer
from potencia_runtime.state import RuntimeState


class RuntimeStateTests(unittest.TestCase):
    def test_state_persists_and_normalizes_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            state = RuntimeState(workspace)
            state.update({"agents": [{"id": "agent-1", "name": "Executor"}]})
            restored = RuntimeState(workspace).snapshot()
            self.assertEqual(restored["workspace"], str(workspace.resolve()))
            self.assertEqual(restored["agents"][0]["id"], "agent-1")


class RuntimeCommandTests(unittest.TestCase):
    def test_all_entity_upserts_and_removals(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            pairs = {
                "agent": "agents",
                "skill": "activeSkills",
                "plugin": "activePlugins",
                "project": "projects",
                "task": "tasks",
                "verification": "verifications",
                "tool": "tools",
            }
            for kind, collection in pairs.items():
                item = {"id": f"{kind}-1", "name": kind}
                result = server.execute_command({"command": f"{kind}.upsert", "item": item})
                self.assertTrue(result and result["event"]["type"].endswith("_changed"))
                self.assertIn(item, server.state.snapshot()[collection])
                result = server.execute_command({"command": f"{kind}.remove", "id": item["id"]})
                self.assertTrue(result and result["event"]["type"].endswith("_changed"))
                self.assertNotIn(item, server.state.snapshot()[collection])
            server.shutdown()

    def test_invalid_commands_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            with self.assertRaises(ValueError):
                server.execute_command({"command": "agent.upsert", "item": {"name": "missing-id"}})
            with self.assertRaises(ValueError):
                server.execute_command({"command": "tool.remove", "id": ""})
            self.assertIsNone(server.execute_command({"command": "unknown"}))
            server.shutdown()


if __name__ == "__main__":
    unittest.main()
