from __future__ import annotations

from itertools import count
from pathlib import Path
from typing import Any

from arp_runtime.audit.events import AuditEvent
from arp_runtime.audit.ledger import AuditLedger
from arp_runtime.budget.checker import check_budget
from arp_runtime.budget.state import BudgetState
from arp_runtime.escalation.matcher import match_escalation
from arp_runtime.loader.schema_loader import load_protocol_version
from arp_runtime.loader.yaml_loader import load_yaml_file
from arp_runtime.memory.store import MemoryStore
from arp_runtime.middleware.hooks import HookRegistry
from arp_runtime.performance.report import build_daily_report
from arp_runtime.policy_engine.authority_guard import evaluate_authority
from arp_runtime.policy_engine.decision import merge_decisions
from arp_runtime.policy_engine.scope_guard import evaluate_scope
from arp_runtime.types import DecisionRecord, DecisionStatus, TaskRequest
from arp_runtime.validator.validator import ProtocolValidator, SchemaValidationError


class ARPRuntime:
    def __init__(self, agent_path: str | Path, audit_path: str | Path | None = None) -> None:
        self.agent_path = Path(agent_path)
        self.validator = ProtocolValidator()
        self.agent_config = load_yaml_file(self.agent_path)
        validation = self.validator.validate_agent_config(self.agent_config)
        if not validation.valid:
            raise SchemaValidationError("; ".join(validation.errors))
        self.audit_ledger = AuditLedger(audit_path)
        self.budget_state = BudgetState()
        self.memory_store = MemoryStore(self.agent_config.get("memory", {}).get("mode", "none"))
        self.hooks = HookRegistry()
        self._decision_counter = count(1)
        self._event_counter = count(1)
        self._decisions: list[dict[str, Any]] = []

    def evaluate(self, task: str, action: str, confidence: float, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        request = TaskRequest(task=task, action=action, confidence=confidence, metadata=metadata or {})
        payload = {"task": task, "action": action, "confidence": confidence, "agent_id": self.agent_config["identity"]["id"]}
        self.hooks.run_before(payload)

        scope_decision = evaluate_scope(self.agent_config, request)
        authority_decision = evaluate_authority(self.agent_config, request)
        budget_result = check_budget(self.agent_config, self.budget_state, request)
        escalation_matches = match_escalation(self.agent_config, request)
        escalation_decision = DecisionRecord(
            status=DecisionStatus.ESCALATED if escalation_matches else DecisionStatus.COMPLETED,
            reasons=["matched escalation trigger"] if escalation_matches else ["no escalation triggers matched"],
            matched_rules=escalation_matches,
        )
        budget_decision = DecisionRecord(
            status=DecisionStatus.BLOCKED if budget_result.exhausted else DecisionStatus.COMPLETED,
            reasons=["budget exhaustion policy triggered"] if budget_result.exhausted else ["budget remains within limits"],
            budget_warnings=budget_result.warnings,
        )
        decision = merge_decisions(scope_decision, authority_decision, escalation_decision, budget_decision)
        if decision.status == DecisionStatus.COMPLETED:
            self.memory_store.remember(
                self.agent_config.get("memory", {}).get("categories", ["default"])[0],
                {"task": task, "action": action, "status": decision.status.value},
            )

        decision_id = f"decision-{next(self._decision_counter)}"
        event = AuditEvent.from_decision(
            event_id=f"event-{next(self._event_counter)}",
            decision_id=decision_id,
            agent_id=self.agent_config["identity"]["id"],
            protocol_version=load_protocol_version(),
            outcome=decision.status.value,
            action_name=action,
            policy_references=decision.matched_rules,
            escalated_to=self.agent_config.get("escalation", {}).get("contact_path", {}).get("primary") if decision.status == DecisionStatus.ESCALATED else None,
        )
        self.audit_ledger.append(event)

        result = {
            "agent_id": self.agent_config["identity"]["id"],
            "protocol_version": load_protocol_version(),
            "decision_id": decision_id,
            **decision.to_dict(),
            "budget_consumed": budget_result.consumed,
        }
        self._decisions.append(result)
        self.hooks.run_after(result)
        return result

    def build_report(self) -> dict[str, Any]:
        report = build_daily_report(self.agent_config, self._decisions)
        validation = self.validator.validate_report(report)
        if not validation.valid:
            raise SchemaValidationError("; ".join(validation.errors))
        return report
