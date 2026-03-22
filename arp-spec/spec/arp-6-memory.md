# ARP-6: Memory

## Summary

The memory pillar defines what information an ARP agent may retain across interactions, how long it may keep that information, and what sensitivity controls apply.

## Why this must exist

Persistent memory can improve usefulness, but it also creates privacy, security, and governance risk. Organizations need explicit protocol-level declarations for what may be retained and under what controls.

## Normative requirements

- An ARP declaration **MUST** include a `memory` object.
- The declaration **MUST** identify whether persistent memory is enabled in `memory.mode`.
- The declaration **MUST** define allowed `memory.categories` of retained information.
- The declaration **MUST** define `memory.retention` rules.
- The declaration **MUST** identify prohibited memory content.
- The declaration **SHOULD** define deletion, correction, or reset mechanisms.
- The declaration **SHOULD** indicate whether human-approved notes differ from autonomous memory writes.

## Required fields

- `memory.mode`
- `memory.categories`
- `memory.retention.default_days`
- `memory.prohibited_content`

## Recommended fields

- `memory.retention.overrides`
- `memory.review_required_for_write`
- `memory.reset_conditions`
- `memory.subject_access_process`
- `memory.encryption_class`

## Example

```yaml
memory:
  mode: bounded-persistent
  categories:
    - customer-preferences-approved-for-service
    - account-context-from-ticket-history
    - unresolved-issue-follow-up-state
  prohibited_content:
    - payment-card-data
    - government-identifiers
    - raw-authentication-secrets
  retention:
    default_days: 90
    overrides:
      unresolved-issue-follow-up-state: 30
  review_required_for_write: false
  reset_conditions:
    - customer-erasure-request
    - case-closure-plus-retention-expiry
  subject_access_process: privacy-operations-ticket
  encryption_class: managed-service-encrypted
```

## Notes for implementers

Memory declarations should not be used to justify indefinite storage by default. Implementers should model memory categories in ways that support deletion and review, especially when regulated or customer-linked data is involved.
