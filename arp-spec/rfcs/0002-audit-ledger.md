# RFC 0002: Audit Ledger Model

## Status
Draft

## Summary

Define a portable audit event model for ARP-compatible systems so decisions, escalations, approvals, and outputs can be reconstructed consistently.

## Motivation

Auditability is central to ARP, but different runtimes will store events differently. A common event schema improves portability and reviewability.

## Proposed direction

- standardize core audit event fields;
- require correlation identifiers and timestamps;
- allow implementation-specific extensions under namespaced fields; and
- align retention metadata with the audit and memory pillars.

## Open questions

- should prompt content logging be modeled as required, optional, or policy-dependent metadata?
- how should redaction provenance be represented?
- how should multi-system event chains be stitched for forensic review?
