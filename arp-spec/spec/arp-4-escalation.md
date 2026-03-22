# ARP-4: Escalation

## Summary

The escalation pillar defines when an ARP agent must defer, pause, seek review, or transfer responsibility to another actor.

## Why this must exist

Even a well-scoped agent will encounter ambiguity, risk, conflict, low confidence, or restricted situations. Escalation rules make those boundaries actionable and auditable.

## Normative requirements

- An ARP declaration **MUST** include an `escalation` object.
- The declaration **MUST** define one or more `escalation.triggers`.
- Each trigger **MUST** specify a `condition`, `action`, and `target`.
- The declaration **MUST** define behavior for policy conflicts, insufficient authority, and low-confidence operation.
- The declaration **SHOULD** define time-based escalation expectations for unacknowledged or unresolved items.
- The declaration **SHOULD** state whether the agent may continue in a limited mode while escalation is pending.

## Required fields

- `escalation.triggers`
- `escalation.default_action`
- `escalation.contact_path`

## Recommended fields

- `escalation.severity_levels`
- `escalation.response_slos`
- `escalation.pause_on_trigger`
- `escalation.notification_channels`

## Example

```yaml
escalation:
  default_action: pause-and-escalate
  contact_path:
    primary: finance-ops-oncall
    secondary: controller-office
  pause_on_trigger: true
  response_slos:
    high: PT15M
    medium: PT2H
  triggers:
    - condition: request exceeds authority.max_transaction_value
      action: escalate-to-human
      target: finance-approver
      severity: high
    - condition: contradictory policy sources detected
      action: halt-and-request-review
      target: compliance-operations
      severity: high
    - condition: confidence below 0.80 for final recommendation
      action: request-human-review
      target: finance-analyst
      severity: medium
```

## Notes for implementers

Escalation must be defined in operational terms rather than as a vague aspiration to "ask for help." The protocol should make it possible for validators and auditors to understand what specific triggers require a handoff and to whom that handoff should go.
