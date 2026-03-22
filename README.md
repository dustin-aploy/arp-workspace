# ARP Workspace

ARP stands for **Agent Responsibility Protocol**. It is an open protocol for accountable AI agents operating inside real organizations. ARP is **not** a full agent framework. Instead, it defines shared contracts, schemas, validation expectations, and interoperability boundaries that implementations can build on.

This repository is the **grouped pre-split workspace** for ARP. The original 6-subproject layout has been regrouped into 3 cleaner targets so the workspace is easier to reason about and easier to split into standalone repositories.

## Why the workspace moved from 6 subprojects to 3 grouped targets

The earlier layout separated protocol, runtime, test-suite, adapters, examples, and registry into many sibling folders. That made ownership visible, but it also made the future repo split noisier than necessary.

The workspace is now grouped into three targets that match the intended long-term repository boundaries more directly:

- `arp-spec/` for the normative protocol layer;
- `arp-devkit/` for runtime, tests, adapters, runnable examples, and developer scripts; and
- `arp-registry/` for publication, discovery, trust, and compliance-listing artifacts.

This regrouping keeps the validated behavior of the workspace while making the split targets explicit.

## Top-level grouped targets

### `arp-spec/`
The protocol/spec target. This is the **source of truth** for ARP schemas, protocol versions, normative examples, RFCs, and governance.

### `arp-devkit/`
The developer toolkit target. It contains the reference runtime, conformance tooling, adapters, runnable examples, and bootstrap/smoke scripts.

### `arp-registry/`
The registry target. It contains compatibility and certification listings, registry schemas, trust/publication docs, and report artifacts.

## Source-of-truth rule

`arp-spec/` is the only place where protocol semantics, schema truth, normative field names, and versioned contracts should originate. Runtime, test-suite, adapters, examples, and registry artifacts must align to `arp-spec/` rather than redefining protocol concepts locally.

## Workspace validation flow

The grouped workspace keeps its end-to-end integration flow under the devkit target:

```bash
./arp-devkit/scripts/bootstrap.sh
./arp-devkit/scripts/smoke_test.sh
```

`./arp-devkit/scripts/bootstrap.sh` installs `arp-spec` and `arp-devkit` in editable mode for grouped-workspace development. `./arp-devkit/scripts/smoke_test.sh` then validates a protocol example from `arp-spec`, runs the devkit runtime on a runnable example, generates an audit log, executes the devkit test-suite, generates a compliance report, and checks registry/report alignment.
