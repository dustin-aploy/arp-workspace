# ARP-3: Authority

## Summary

The authority pillar defines what permissions, actions, approvals, and system capabilities an ARP agent is allowed to exercise.

## Why this must exist

An agent may have broad practical capability but narrow legitimate authority. ARP distinguishes what an agent *can* technically do from what it is *authorized* to do on behalf of an organization.

## Normative requirements

- An ARP declaration **MUST** include an `authority` object.
- The declaration **MUST** identify `authority.permission_level`.
- The declaration **MUST** enumerate `authority.allowed_actions`.
- The declaration **MUST** enumerate `authority.restricted_actions`.
- The declaration **MUST** identify `authority.approval_requirements` for actions that need pre-approval, dual approval, or human sign-off.
- The declaration **SHOULD** list `authority.system_permissions` when the agent interacts with operational systems.
- The declaration **SHOULD** identify delegation boundaries and whether the agent may initiate external communication.

## Required fields

- `authority.permission_level`
- `authority.allowed_actions`
- `authority.restricted_actions`
- `authority.approval_requirements`

## Recommended fields

- `authority.system_permissions`
- `authority.external_communication_policy`
- `authority.max_transaction_value`
- `authority.delegation_rules`

## Example

```yaml
authority:
  permission_level: supervised-operational
  allowed_actions:
    - create draft CRM notes
    - update lead status to qualified
    - schedule follow-up tasks
  restricted_actions:
    - modify pricing
    - sign contracts
    - send binding customer commitments
  approval_requirements:
    - action: export-lead-data
      requirement: manager-approval
    - action: outbound-email-send
      requirement: approved-template-only
  system_permissions:
    salesforce:
      - lead.read
      - lead.update
      - task.create
    outreach:
      - sequence.read
  external_communication_policy: draft-only
  max_transaction_value: 0
```

## Notes for implementers

Authority fields should map to organizational approval models rather than low-level product internals wherever possible. When technical permissions are included, they should be presented as evidence of authority boundaries, not a replacement for policy statements.
