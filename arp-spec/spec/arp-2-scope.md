# ARP-2: Scope

## Summary

The scope pillar defines the operational domain, permitted task classes, prohibited actions, and handoff boundaries for an ARP agent.

## Why this must exist

An accountable agent needs an explicit statement of what it is supposed to do and what it must not do. Scope prevents authority creep, clarifies expected use, and creates the baseline for testing and auditing responsibility boundaries.

## Normative requirements

- An ARP declaration **MUST** include a `scope` object.
- The `scope.mission` field **MUST** summarize the agent's authorized purpose.
- The declaration **MUST** list one or more `scope.allowed_tasks`.
- The declaration **MUST** list one or more `scope.prohibited_tasks`.
- The declaration **MUST** define at least one `scope.handoffs` condition for work outside agent scope or confidence boundaries.
- The declaration **SHOULD** include `scope.in_scope_systems` and `scope.out_of_scope_systems` when system boundaries matter operationally.
- The declaration **SHOULD** describe confidence or evidence thresholds when autonomous completion is limited.

## Required fields

- `scope.mission`
- `scope.allowed_tasks`
- `scope.prohibited_tasks`
- `scope.handoffs`

## Recommended fields

- `scope.in_scope_systems`
- `scope.out_of_scope_systems`
- `scope.data_domains`
- `scope.success_criteria`
- `scope.confidence_thresholds`

## Example

```yaml
scope:
  mission: Support first-response triage for customer tickets and route complex cases to humans.
  allowed_tasks:
    - summarize inbound ticket text
    - classify request type using approved taxonomy
    - draft initial troubleshooting steps from approved knowledge sources
    - route tickets to the correct support queue
  prohibited_tasks:
    - promise refunds
    - change billing plans
    - close safety-related incidents without human review
    - access customer data outside ticket context
  handoffs:
    - trigger: user reports financial loss or legal threat
      action: escalate-to-human
      target: support-escalation-manager
    - trigger: confidence below 0.78
      action: request-human-review
      target: tier-2-support
  in_scope_systems:
    - zendesk
    - support-knowledge-base
  out_of_scope_systems:
    - payroll
    - identity-provider-admin
```

## Notes for implementers

Scope should remain concrete enough that a downstream runtime or validator can distinguish compliant from non-compliant work. Avoid vague statements such as "helps with support" unless supported by task-level allowed and prohibited boundaries.
