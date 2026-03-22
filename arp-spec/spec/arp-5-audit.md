# ARP-5: Audit

## Summary

The audit pillar defines what evidence an ARP agent must record about its inputs, decisions, actions, outputs, and escalations.

## Why this must exist

Accountability requires more than after-the-fact summaries. Organizations need a record of what happened, why it happened, what evidence was used, what constraints were applied, and whether escalation or review occurred.

## Normative requirements

- An ARP declaration **MUST** include an `audit` object.
- The declaration **MUST** define `audit.level`.
- The declaration **MUST** identify which event types are recorded in `audit.required_events`.
- The declaration **MUST** specify `audit.retention_period_days`.
- The declaration **MUST** define whether prompts, tool calls, outputs, escalations, approvals, and policy references are logged.
- The declaration **SHOULD** identify redaction rules for sensitive data.
- The declaration **SHOULD** define trace or correlation identifiers for cross-system reconstruction.

## Required fields

- `audit.level`
- `audit.required_events`
- `audit.retention_period_days`
- `audit.redaction_policy`

## Recommended fields

- `audit.correlation_id_strategy`
- `audit.log_prompt_inputs`
- `audit.log_tool_calls`
- `audit.log_policy_references`
- `audit.storage_classification`

## Example

```yaml
audit:
  level: full
  required_events:
    - input-received
    - policy-evaluated
    - action-proposed
    - human-review-requested
    - output-issued
  retention_period_days: 365
  redaction_policy: redact-secrets-and-regulated-identifiers
  correlation_id_strategy: request-id-and-decision-id
  log_prompt_inputs: true
  log_tool_calls: true
  log_policy_references: true
  storage_classification: confidential-operational
```

## Notes for implementers

Audit requirements should strike a balance between accountability and data minimization. The protocol should specify what must be reconstructable while leaving storage technology choices to downstream systems.
