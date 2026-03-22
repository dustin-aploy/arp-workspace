# RFC 0003: Certification Model Boundaries

## Status
Draft

## Summary

Define the protocol-facing structure for compliance and certification reports without embedding certification execution machinery into the protocol repository.

## Motivation

The protocol needs a stable schema for validation outputs so registries and test systems can exchange evidence, but the execution of certification belongs outside this repository.

## Proposed direction

- define report schemas here;
- allow external test suites to emit evidence aligned to those schemas; and
- keep scoring logic, execution harnesses, and issuance workflows out of the protocol repository.

## Open questions

- what minimum evidence is required for a compliance report?
- how should protocol-version compatibility be represented for partial conformance?
- should certification profiles be standardized or left to external governance bodies?
