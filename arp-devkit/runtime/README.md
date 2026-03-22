# ARP Runtime

`arp-runtime` is the reference runtime inside the grouped `arp-devkit` target.

It demonstrates how to:
- load ARP declarations
- validate them against protocol-owned schemas from `../../arp-spec`
- evaluate scope, authority, escalation, budget, and memory rules
- emit audit events
- build simple operational reports

`arp-runtime` is **not** the protocol itself. Protocol truth remains in `../../arp-spec`.

## Install locally

```bash
pip install -e ./arp-spec
pip install -e ./arp-devkit/runtime
```

## Example CLI run

```bash
arp-runtime \
  --agent ../examples/agents/sales-agent.yaml \
  --task "Customer asks for a discount" \
  --action "reply_inbound_dm" \
  --confidence 0.65 \
  --report
```

## Tests

```bash
python -m unittest discover -s arp-devkit/runtime/tests
```
