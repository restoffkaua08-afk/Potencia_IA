import json
import tempfile
import threading
import unittest
from http.client import HTTPConnection
from pathlib import Path
from urllib.request import Request, urlopen

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
                upserts = [
                    ("skill.upsert", "activeSkills", "skill-1", "skill_upsert_changed"),
                    ("plugin.upsert", "activePlugins", "plugin-1", "plugin_upsert_changed"),
                    ("project.upsert", "projects", "project-1", "project_upsert_changed"),
                    ("task.upsert", "tasks", "task-1", "task_upsert_changed"),
                    ("verification.upsert", "verifications", "verification-1", "verification_upsert_changed"),
                    ("tool.upsert", "tools", "tool-1", "tool_upsert_changed"),
                ]
                for command, collection, item_id, event_type in upserts:
                    result = server.execute_command({
                        "command": command,
                        "item": {"id": item_id, "name": item_id, "status": "active"},
                    })
                    self.assertEqual(result["event"]["type"], event_type)
                    self.assertEqual(server.state.snapshot()[collection][0]["id"], item_id)

                server.execute_command({"command": "agent.remove", "id": "agent-1"})
                self.assertEqual(server.state.snapshot()["agents"], [])
                self.assertIsNone(server.execute_command({"command": "shell.exec", "command_text": "dir"}))
                with self.assertRaises(ValueError):
                    server.execute_command([])
                with self.assertRaises(ValueError):
                    server.execute_command({"command": "agent.upsert", "item": {"id": ""}})
                with self.assertRaises(ValueError):
                    server.execute_command({"command": "agent.upsert", "item": {"id": 123}})

            finally:
                server.shutdown()

    def test_http_auth_commands_and_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                port = server.httpd.server_port

                with urlopen(f"http://127.0.0.1:{port}/health", timeout=2) as response:
                    health = json.loads(response.read())
                self.assertTrue(health["ok"])
                self.assertEqual(health["protocol_version"], "1")

                with self.assertRaises(Exception):
                    urlopen(f"http://127.0.0.1:{port}/v1/state", timeout=2)

                headers = {"Authorization": f"Bearer {server.token}"}
                request = Request(f"http://127.0.0.1:{port}/v1/state", headers=headers)
                with urlopen(request, timeout=2) as response:
                    state = json.loads(response.read())
                self.assertEqual(state["protocol_version"], "1")

                payload = json.dumps({
                    "command": "agent.upsert",
                    "item": {"id": "http-agent", "name": "HTTP Executor"},
                }).encode()
                request = Request(
                    f"http://127.0.0.1:{port}/v1/commands",
                    data=payload,
                    headers={**headers, "Content-Type": "application/json"},
                )
                with urlopen(request, timeout=2) as response:
                    result = json.loads(response.read())
                self.assertTrue(result["ok"])
                self.assertEqual(result["event"]["type"], "agent_upsert_changed")

                bad_request = Request(
                    f"http://127.0.0.1:{port}/v1/commands",
                    data=b"[]",
                    headers={**headers, "Content-Type": "application/json"},
                )
                with self.assertRaises(Exception):
                    urlopen(bad_request, timeout=2)

                wrong_type = Request(
                    f"http://127.0.0.1:{port}/v1/commands",
                    data=json.dumps({"command": "ping"}).encode(),
                    headers={**headers, "Content-Type": "text/plain"},
                )
                with self.assertRaises(Exception):
                    urlopen(wrong_type, timeout=2)

                empty_body = Request(
                    f"http://127.0.0.1:{port}/v1/commands",
                    data=b"",
                    headers={**headers, "Content-Type": "application/json"},
                )
                with self.assertRaises(Exception):
                    urlopen(empty_body, timeout=2)

            finally:
                server.shutdown()
                thread.join(timeout=2)

    def test_sse_receives_broadcast_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            connection = HTTPConnection("127.0.0.1", server.httpd.server_port, timeout=2)
            try:
                connection.request("GET", "/v1/events", headers={
                    "Authorization": f"Bearer {server.token}",
                    "Accept": "text/event-stream",
                })
                response = connection.getresponse()
                self.assertEqual(response.status, 200)
                first = response.readline()
                while first and first.strip() != b"event: snapshot":
                    first = response.readline()
                self.assertEqual(first.strip(), b"event: snapshot")
                while response.readline().strip() != b"":
                    pass

                event = server.execute_command({
                    "command": "agent.upsert",
                    "item": {"id": "sse-agent", "name": "SSE Agent"},
                })["event"]

                lines = []
                while True:
                    line = response.readline()
                    if not line:
                        break
                    lines.append(line)
                    if line.strip() == b"" and any(b"event: agent_upsert_changed" in item for item in lines):
                        break

                self.assertTrue(any(b"event: agent_upsert_changed" in item for item in lines))
                self.assertTrue(any(event["id"].encode() in item for item in lines))
            finally:
                connection.close()
                server.shutdown()
                thread.join(timeout=2)

    def test_sse_shutdown_interrupts_heartbeat_wait(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                server.stop_event.set()
                server.shutdown()
                thread.join(timeout=2)
                self.assertFalse(thread.is_alive())
            finally:
                if thread.is_alive():
                    server.shutdown()

    def test_sse_starts_with_snapshot_frame(self):
        with tempfile.TemporaryDirectory() as tmp:
            server = RuntimeServer(Path(tmp), port=0)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            connection = HTTPConnection("127.0.0.1", server.httpd.server_port, timeout=2)
            try:
                connection.request("GET", "/v1/events", headers={
                    "Authorization": f"Bearer {server.token}",
                    "Accept": "text/event-stream",
                })
                response = connection.getresponse()
                self.assertEqual(response.status, 200)
                self.assertEqual(response.getheader("Content-Type"), "text/event-stream; charset=utf-8")
                chunk = response.read(64)
                self.assertIn(b"event: snapshot\n", chunk)
                self.assertIn(b"data: ", chunk)
            finally:
                connection.close()
                server.shutdown()
                thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
