# RFC 0001: ARP Protocol Foundation

## Status
Accepted

## Summary

Establish ARP as a protocol for describing accountable AI agent operation in organizations through normative responsibility pillars, machine-readable schemas, and versioned governance.

## Motivation

Organizations need a way to define what an agent is responsible for without coupling that definition to any particular framework or runtime. ARP provides the interoperable contract layer.

## Design

ARP declarations are structured around eight pillars: identity, scope, authority, escalation, audit, memory, budget, and performance. The protocol repository owns the normative docs, schemas, examples, and version metadata.

## Consequences

- downstream systems gain a stable protocol target;
- the protocol remains distinct from execution infrastructure; and
- future conformance tooling can validate against shared artifacts.
