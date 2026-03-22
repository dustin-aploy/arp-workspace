import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "arp-devkit" / "runtime" / "src"))
sys.path.insert(0, str(ROOT / "arp-spec" / "src"))

from arp_runtime.runtime import ARPRuntime


class AuditTests(unittest.TestCase):
    def test_audit_ledger_writes_jsonl(self):
        audit_file = Path(tempfile.gettempdir()) / "arp-runtime-audit.jsonl"
        if audit_file.exists():
            audit_file.unlink()
        runtime = ARPRuntime(ROOT / "arp-devkit" / "examples" / "agents" / "support-agent.yaml", audit_path=audit_file)
        runtime.evaluate("Summarize a support ticket", "draft_response", 0.9)
        self.assertTrue(audit_file.exists())
        first_line = audit_file.read_text(encoding="utf-8").strip().splitlines()[0]
        payload = json.loads(first_line)
        self.assertEqual(payload["event_type"], "action-proposed")


if __name__ == "__main__":
    unittest.main()
