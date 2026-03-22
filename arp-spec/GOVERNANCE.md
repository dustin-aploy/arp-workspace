# ARP Governance

## Purpose

ARP governance exists to preserve a stable, accountable, and reviewable protocol standard for organizational AI agent responsibility.

## Governance goals

- maintain a clear separation between normative protocol definitions and implementation-specific behavior;
- ensure changes to schemas and semantics are deliberate and reviewable;
- preserve interoperability across downstream runtimes and tools; and
- provide a transparent path for proposing, evaluating, and ratifying changes.

## Governance roles

### Editors
Editors maintain document quality, structure, consistency, and release readiness. Editors may merge editorial changes that do not alter normative semantics.

### Maintainers
Maintainers are responsible for release decisions, schema consistency, RFC adjudication, and compatibility policy.

### Contributors
Contributors may propose improvements, submit RFCs, and provide review input, but normative changes require maintainer approval.

## Decision classes

### Class A: Editorial
- typo fixes;
- formatting;
- explanatory clarifications with no semantic effect; and
- non-normative example improvements that do not alter interpretation.

Approval: editor review is sufficient.

### Class B: Normative, backward compatible
- adding optional fields;
- clarifying required behavior without breaking existing compliant documents;
- adding new examples of compliant usage; and
- strengthening guidance that remains compatible with current schemas.

Approval: maintainer review required; RFC recommended and generally expected.

### Class C: Normative, compatibility affecting
- removing or renaming fields;
- altering required field semantics;
- narrowing accepted values or structures;
- changing version compatibility guarantees; and
- introducing governance changes that affect release authority.

Approval: maintainer consensus required; RFC required.

## RFC process

1. Create an RFC in `rfcs/` using the next available number.
2. Identify motivation, scope, design, compatibility, alternatives, and migration considerations.
3. Link proposed spec and schema changes.
4. Obtain review from maintainers and relevant stakeholders.
5. Merge the RFC before or with the normative implementation change.
6. Release the protocol version that incorporates the accepted change.

## Normative language

ARP uses the key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** in the sense commonly used by standards-oriented specifications. Normative statements should be concrete enough to support schema validation and downstream conformance testing.

## Source-of-truth rule

This repository is the canonical source for ARP field names, structures, and versions. Downstream repositories may extend implementation behavior, but they may not redefine ARP-owned protocol structures independently.

## Release authority

Maintainers approve protocol releases. A release should include:

- updated normative artifacts as needed;
- synchronized schema files;
- updated packaged schema assets;
- version metadata updates; and
- release notes describing compatibility implications.
