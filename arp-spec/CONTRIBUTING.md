# Contributing to ARP

Thank you for contributing to the Agent Responsibility Protocol.

## Scope of contributions

This repository accepts contributions related to:

- protocol specifications;
- machine-readable schemas;
- normative and explanatory documentation;
- examples illustrating protocol usage;
- governance process improvements; and
- packaging metadata required to distribute the protocol artifacts.

This repository does **not** accept runtime orchestration code, adapter implementations, certification execution logic, or vendor-specific integration behavior.

## Contribution principles

Contributors should preserve the following rules:

1. ARP is a protocol, not a framework.
2. Protocol field names and schema structures defined here are authoritative.
3. Non-normative examples must not silently broaden or contradict normative requirements.
4. Changes with compatibility impact must be explicit and versioned.
5. Governance and schema changes should be conservative, reviewable, and well documented.

## Change classes

### Editorial changes
Editorial changes include typo fixes, formatting updates, and clarifications that do not change semantics. These may be proposed directly through pull requests.

### Normative changes
Normative changes affect one or more of the following:

- required fields;
- allowed values;
- compatibility guarantees;
- schema structure;
- versioning semantics;
- governance decision process; or
- interpretation of MUST, SHOULD, or MAY requirements.

Normative changes should be proposed through an RFC under `rfcs/` before or alongside implementation changes.

## Recommended contribution workflow

1. Open an issue describing the problem, ambiguity, or change request.
2. If the change is normative, draft or update an RFC in `rfcs/`.
3. Update the relevant spec documents in `spec/`.
4. Update JSON Schemas in `schemas/` and packaged copies in `src/arp_protocol/schemas/`.
5. Update examples and explanatory docs when necessary.
6. Adjust `VERSION` and packaging metadata if compatibility or release scope changes.
7. Submit a pull request with a clear summary of normative versus non-normative changes.

## Review expectations

Pull requests should clearly state:

- whether the change is editorial or normative;
- whether the change is backward compatible;
- which spec documents are affected;
- which schemas are affected; and
- whether examples or downstream consumers may need updates.

## Schema discipline

Do not redefine protocol fields in downstream repositories and then back-port them informally. If a field needs to exist in ARP, add it here first.

## Release discipline

Version changes should correspond to the scope of change:

- patch releases for editorial fixes or packaging-only corrections;
- minor releases for backward-compatible additions and clarifications; and
- major releases for breaking changes to normative semantics or schema compatibility.
