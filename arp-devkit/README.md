# ARP Devkit

`arp-devkit` groups the developer-facing implementation and validation tools for the Agent Responsibility Protocol (ARP).

It keeps the runnable pieces of the ARP ecosystem together:
- the reference runtime under `runtime/`
- the conformance and certification tooling under `test-suite/`
- adapter guidance under `adapters/`
- runnable examples under `examples/`
- workspace bootstrap and smoke scripts under `scripts/`

`arp-devkit` is **not** the protocol source of truth. Protocol schemas, versions, normative examples, and governance remain on the `arp-spec/` side.

## Layout

```text
arp-devkit/
  README.md
  LICENSE
  VERSION
  pyproject.toml
  runtime/
  test-suite/
  adapters/
  examples/
  scripts/
```

## Typical local validation flow

```bash
./arp-devkit/scripts/bootstrap.sh
./arp-devkit/scripts/smoke_test.sh
```
