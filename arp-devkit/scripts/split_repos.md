# Repo Split Guide

The workspace has already been regrouped into three split-ready targets:

- `arp-spec/`
- `arp-devkit/`
- `arp-registry/`

## Split order

1. Publish `arp-spec` first because it owns protocol truth.
2. Publish `arp-devkit` next because it depends on `arp-spec`.
3. Publish `arp-registry` after or alongside the devkit once registry schemas and evidence references are stable.

## Rules

- `arp-spec` remains the source of truth for schemas, protocol versions, and normative examples.
- `arp-devkit` groups runtime, test-suite, adapters, runnable examples, and scripts.
- `arp-registry` references protocol and compliance artifacts, but does not redefine them.
