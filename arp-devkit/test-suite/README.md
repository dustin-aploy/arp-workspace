# ARP Test Suite

`arp-test-suite` is the conformance and certification foundation inside the grouped `arp-devkit` target.

It depends on:
- `../../arp-spec` for protocol schemas and version truth
- `../runtime` for a reference execution path used in local validation flows

It is responsible for building protocol-shaped `ARPComplianceReport` artifacts and validating behavior, audit, and reporting expectations.

## Install locally

```bash
pip install -e ./arp-spec
pip install -e ./arp-devkit/runtime
pip install -e ./arp-devkit/test-suite
```

## Run tests

```bash
pytest arp-devkit/test-suite/tests
```
