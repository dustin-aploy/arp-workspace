# ARP-7: Budget

## Summary

The budget pillar defines the operational resource limits under which an ARP agent may run, including cost, throughput, invocation, and tool usage constraints.

## Why this must exist

Responsible operation is not only about policy and authority. Agents also need explicit limits on resource consumption so organizations can manage cost, reliability, and abuse exposure.

## Normative requirements

- An ARP declaration **MUST** include a `budget` object.
- The declaration **MUST** define at least one concrete limit under `budget.limits`.
- The declaration **MUST** identify the measurement period associated with each limit.
- The declaration **MUST** define what happens when a limit is reached.
- The declaration **SHOULD** distinguish between soft limits and hard limits.
- The declaration **SHOULD** identify whether escalation or throttling occurs before termination.

## Required fields

- `budget.limits`
- `budget.exhaustion_action`

## Recommended fields

- `budget.warning_thresholds`
- `budget.override_process`
- `budget.priority_tier`
- `budget.cost_center`

## Example

```yaml
budget:
  exhaustion_action: throttle-and-escalate
  priority_tier: business-critical
  cost_center: customer-support-ops
  warning_thresholds:
    - limit: monthly-usd
      percent: 80
  limits:
    - name: monthly-usd
      amount: 3500
      unit: usd
      period: P1M
      enforcement: hard
    - name: tickets-per-hour
      amount: 600
      unit: count
      period: PT1H
      enforcement: soft
    - name: tool-calls-per-ticket
      amount: 12
      unit: count
      period: per-interaction
      enforcement: hard
  override_process: director-approval-required
```

## Notes for implementers

Budget is intentionally protocol-visible because uncontrolled agent use can become an organizational risk. Downstream systems may implement enforcement in different ways, but the declared limits and exhaustion behavior should remain interpretable and testable.
