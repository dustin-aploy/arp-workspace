import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "arp-devkit" / "runtime" / "src"))
sys.path.insert(0, str(ROOT / "arp-spec" / "src"))

from arp_runtime.runtime import ARPRuntime


class RuntimeSmokeTests(unittest.TestCase):
    def test_runtime_loads_protocol_example_and_evaluates(self):
        audit_file = Path(tempfile.gettempdir()) / "arp-runtime-smoke.jsonl"
        if audit_file.exists():
            audit_file.unlink()
        runtime = ARPRuntime(ROOT / "arp-devkit" / "examples" / "agents" / "sales-agent.yaml", audit_path=audit_file)
        result = runtime.evaluate("Customer asks for a discount", "reply_inbound_dm", 0.65)
        self.assertEqual(result["status"], "escalated")
        self.assertTrue(audit_file.exists())


if __name__ == "__main__":
    unittest.main()
