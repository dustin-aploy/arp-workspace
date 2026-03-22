# ARP-1: Identity

## Summary

The identity pillar defines how an ARP agent is named, owned, versioned, and classified so that the organization can determine what the agent is, who is responsible for it, and which protocol version governs its declaration.

## Why this must exist

Without a canonical identity block, organizations cannot reliably distinguish one agent from another, track accountability across versions, or determine which owner and stewardship chain applies during audits, incidents, and reviews.

## Normative requirements

- An ARP declaration **MUST** include an `identity` object.
- The `identity.id` field **MUST** be stable within the declaring organization.
- The `identity.name` field **MUST** be human-readable.
- The `identity.role` field **MUST** describe the organizational function the agent serves.
- The `identity.owner` object **MUST** identify the accountable business or technical owner.
- The `identity.protocol_version` field **MUST** reference the ARP version against which the declaration is authored.
- The `identity.lifecycle_state` field **MUST** indicate whether the declaration is proposed, active, suspended, retired, or another protocol-approved lifecycle state.
- The declaration **SHOULD** include `identity.review_cycle_days` to indicate planned review cadence.
- The declaration **SHOULD** include `identity.classification` when the organization uses risk or sensitivity tiers.

## Required fields

- `identity.id`
- `identity.name`
- `identity.role`
- `identity.owner.name`
- `identity.owner.email`
- `identity.protocol_version`
- `identity.lifecycle_state`

## Recommended fields

- `identity.summary`
- `identity.owner.team`
- `identity.owner.manager`
- `identity.classification`
- `identity.review_cycle_days`
- `identity.tags`

## Example

```yaml
identity:
  id: sales.pipeline.qualifier
  name: Sales Pipeline Qualifier
  role: inbound-sales-qualification
  summary: Qualifies inbound leads and prepares CRM-ready opportunity notes.
  protocol_version: 0.1.0
  lifecycle_state: active
  classification: internal-moderate
  review_cycle_days: 30
  tags:
    - sales
    - crm
    - qualification
  owner:
    name: Maya Chen
    email: revenue-ops@example.com
    team: Revenue Operations
    manager: VP Revenue Operations
```

## Notes for implementers

Identity data should be treated as canonical reference information. Downstream systems may index on `identity.id`, but they should not alter the semantics of identity fields. Where organizations have internal registry identifiers, those may be represented as additional metadata, provided the ARP identity fields remain intact.
