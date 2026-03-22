import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "arp-devkit" / "runtime" / "src"))
sys.path.insert(0, str(ROOT / "arp-spec" / "src"))

from arp_runtime.runtime import ARPRuntime


class ReportTests(unittest.TestCase):
    def test_runtime_builds_protocol_shaped_report(self):
        runtime = ARPRuntime(ROOT / "arp-devkit" / "examples" / "agents" / "content-agent.yaml")
        runtime.evaluate("Draft an email headline", "draft_email", 0.95)
        report = runtime.build_report()
        self.assertEqual(report["kind"], "ARPReport")
        self.assertEqual(report["agent_id"], "marketing.content.drafter")


if __name__ == "__main__":
    unittest.main()
