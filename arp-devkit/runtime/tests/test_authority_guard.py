import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "arp-devkit" / "runtime" / "src"))
sys.path.insert(0, str(ROOT / "arp-spec" / "src"))

from arp_runtime.loader.yaml_loader import load_yaml_file
from arp_runtime.policy_engine.authority_guard import evaluate_authority
from arp_runtime.types import TaskRequest


class AuthorityGuardTests(unittest.TestCase):
    def test_restricted_action_blocks(self):
        config = load_yaml_file(ROOT / "arp-spec" / "examples" / "sales-agent.yaml")
        decision = evaluate_authority(config, TaskRequest(task="Offer a discount", action="modify legal terms", confidence=0.9))
        self.assertEqual(decision.status.value, "blocked")

    def test_reply_requires_escalation_for_draft_only(self):
        config = load_yaml_file(ROOT / "arp-spec" / "examples" / "sales-agent.yaml")
        decision = evaluate_authority(config, TaskRequest(task="Reply to lead", action="reply_inbound_dm", confidence=0.9))
        self.assertEqual(decision.status.value, "escalated")


if __name__ == "__main__":
    unittest.main()
