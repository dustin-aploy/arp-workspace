# ARP-8: Performance

## Summary

The performance pillar defines the service, quality, and review metrics by which an ARP agent is evaluated.

## Why this must exist

A responsible agent must be measured not only for capability but also for fitness within organizational expectations. Performance requirements clarify what outcomes matter and when intervention is required.

## Normative requirements

- An ARP declaration **MUST** include a `performance` object.
- The declaration **MUST** define at least one measurable `performance.objectives` entry.
- The declaration **MUST** identify `performance.review_cycle_days`.
- The declaration **MUST** identify remediation or escalation behavior when objectives are missed.
- The declaration **SHOULD** distinguish quality, speed, safety, and handoff metrics where relevant.
- The declaration **SHOULD** include a source of truth for measurement inputs.

## Required fields

- `performance.objectives`
- `performance.review_cycle_days`
- `performance.failure_action`

## Recommended fields

- `performance.measurement_sources`
- `performance.minimum_sample_size`
- `performance.segmented_targets`
- `performance.human_review_rate`

## Example

```yaml
performance:
  review_cycle_days: 14
  failure_action: increase-human-review-and-reassess-scope
  measurement_sources:
    - crm-reports
    - qa-scorecards
    - escalation-audit-log
  minimum_sample_size: 200
  human_review_rate: 0.10
  objectives:
    - metric: lead-qualification-precision
      target: ">=0.92"
      window: P14D
    - metric: average-response-latency-seconds
      target: "<=45"
      window: P7D
    - metric: improper-autonomous-commitments
      target: "=0"
      window: P30D
```

## Notes for implementers

Performance metrics should be selected to support governance decisions rather than vanity reporting. Metrics that directly reflect scope compliance, escalation quality, and operational safety are usually more useful than generic activity volume counts alone.
