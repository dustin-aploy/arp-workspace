# ARP Repo Split Plan

## Goal

Regroup the validated ARP workspace so it can split cleanly into three standalone repositories:
- `arp-spec`
- `arp-devkit`
- `arp-registry`

## Current grouped layout

```text
arp-spec/
arp-devkit/
arp-registry/
docs/
AGENTS.md
README.md
```

## Mapping summary

### `arp-spec`
Built primarily from the former protocol-side project:
- docs
- examples
- rfcs
- schemas
- spec
- src/arp_protocol
- protocol governance and packaging metadata

### `arp-devkit`
Built from the former implementation-side projects:
- runtime
- test-suite
- adapters
- runnable examples
- workspace scripts
- developer/integration guidance

### `arp-registry`
Built from the former registry project:
- certified
- compatible
- reports
- schemas
- docs

## Split principles

1. Keep protocol truth only on the `arp-spec` side.
2. Keep runtime, test-suite, adapters, and runnable examples together in `arp-devkit`.
3. Keep registry publication and listing concepts in `arp-registry`.
4. Prefer clean ownership boundaries over preserving old folder names.
5. Update docs and smoke paths whenever structure changes.
