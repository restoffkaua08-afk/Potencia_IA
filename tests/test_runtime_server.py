import tempfile
import unittest
from pathlib import Path

from potencia_runtime.server import RuntimeServer


class RuntimeServerTests(unittest.TestCase):
    def test_health_shape_and_safe_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            try:
                health = {
                    "ok": True,
                    "service": "potencia-runtime",
                    "protocol_version": "1",
                    "potencia_version": "0.3.0",
                }
                self.assertTrue(health["ok"])
                self.assertEqual(server.execute_command({"command": "ping"})["event"]["type"], "runtime_ping")

                result = server.execute_command({
                    "command": "agent.upsert",
                    "item": {"id": "agent-1", "name": "Executor", "state": "working"},
                })
                self.assertEqual(result["event"]["type"], "agent_upsert_changed")
                self.assertEqual(server.state.snapshot()["agents"][0]["id"], "agent-1")

                server.execute_command({"command": "agent.remove", "id": "agent-1"})
                self.assertEqual(server.state.snapshot()["agents"], [])
                self.assertIsNone(server.execute_command({"command": "shell.exec", "command_text": "dir"}))
            finally:
                server.shutdown()


if __name__ == "__main__":
    unittest.main()
