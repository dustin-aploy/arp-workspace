# Post-Split Dependency Model

## Dependency direction

The intended dependency flow after splitting is:

```text
arp-spec
  ├──> arp-devkit
  └──> arp-registry

arp-devkit
  └──> arp-registry (via generated compliance/report artifacts, not schema ownership)
```

## Rules

- `arp-spec` owns schemas, protocol versions, normative examples, and protocol semantics.
- `arp-devkit` depends on `arp-spec` for protocol truth.
- `arp-registry` references protocol versions and compliance artifacts, but does not redefine protocol structure.
- Runtime, test-suite, adapters, and runnable examples stay together so developer workflows remain coherent.

## Example ownership split

- Normative declaration/report examples belong in `arp-spec`.
- Runnable examples and demo outputs belong in `arp-devkit`.

## Validation expectation

The grouped smoke flow should continue to prove:
- protocol package installs
- grouped devkit package installs
- runtime package installs
- test-suite package installs
- runnable examples validate and execute
- registry/report alignment still holds

Use the workspace entry points:

```bash
./arp-devkit/scripts/bootstrap.sh
./arp-devkit/scripts/smoke_test.sh
```
