import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "arp-devkit" / "runtime" / "src"))
sys.path.insert(0, str(ROOT / "arp-spec" / "src"))

from arp_runtime.loader.yaml_loader import load_yaml_file
from arp_runtime.policy_engine.scope_guard import evaluate_scope
from arp_runtime.types import TaskRequest


class ScopeGuardTests(unittest.TestCase):
    def test_prohibited_scope_blocks(self):
        config = load_yaml_file(ROOT / "arp-spec" / "examples" / "sales-agent.yaml")
        decision = evaluate_scope(config, TaskRequest(task="Please negotiate pricing", action="reply", confidence=0.95))
        self.assertEqual(decision.status.value, "blocked")

    def test_low_confidence_escalates(self):
        config = load_yaml_file(ROOT / "arp-spec" / "examples" / "sales-agent.yaml")
        decision = evaluate_scope(config, TaskRequest(task="Summarize lead details", action="draft_note", confidence=0.30))
        self.assertEqual(decision.status.value, "escalated")


if __name__ == "__main__":
    unittest.main()
