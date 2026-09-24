import json
import tempfile
import unittest
from pathlib import Path

from potencia_runtime.state import RuntimeState


class RuntimeStateTests(unittest.TestCase):
    def test_default_snapshot_has_protocol(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = RuntimeState(Path(tmp))
            snapshot = state.snapshot()
            self.assertEqual(snapshot["protocol_version"], "1")
            self.assertEqual(snapshot["workspace"], str(Path(tmp).resolve()))

    def test_update_persists_without_deadlock(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = RuntimeState(Path(tmp))
            snapshot = state.update({"connection": {"status": "connected"}})
            self.assertEqual(snapshot["connection"]["status"], "connected")
            saved = json.loads((Path(tmp) / ".potencia" / "runtime-state.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["connection"]["status"], "connected")

    def test_emit_keeps_bounded_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = RuntimeState(Path(tmp))
            for index in range(510):
                state.emit("test_event", {"index": index})
            snapshot = state.snapshot()
            self.assertEqual(len(snapshot["events"]), 500)
            self.assertEqual(snapshot["events"][0]["payload"]["index"], 10)


if __name__ == "__main__":
    unittest.main()
