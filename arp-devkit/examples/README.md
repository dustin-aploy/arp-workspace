# ARP Runnable Examples

`arp-devkit/examples` contains the runnable developer examples for ARP.

These examples are distinct from the normative protocol examples in `../../arp-spec/examples`:
- `../../arp-spec/examples` shows protocol-valid declarations as normative references
- `../examples` shows runnable developer scenarios, demo tasks, and generated outputs

The examples here are designed to run with `../runtime` and to support smoke-test and validation workflows.

## Typical validation flow

```bash
pip install -e ./arp-spec
pip install -e ./arp-devkit/runtime
python -m arp_runtime.cli       --agent arp-devkit/examples/agents/sales-agent.yaml       --task "Customer asks for a discount"       --action "reply_inbound_dm"       --confidence 0.65       --report
```
