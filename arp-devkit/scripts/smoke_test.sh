#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

ARTIFACT_DIR="${ARTIFACT_DIR:-$(mktemp -d "${TMPDIR:-/tmp}/arp-workspace-smoke.XXXXXX")}"
AUDIT_LOG="${ARTIFACT_DIR}/arp-runtime.audit.jsonl"
COMPLIANCE_REPORT="${ARTIFACT_DIR}/compliance-report.json"

clean_stale_editable_metadata() {
  python - <<'PY'
import site
import shutil
from pathlib import Path

patterns = (
    "~rp_protocol-*.dist-info",
    "~rp_devkit-*.dist-info",
    "~rp_runtime-*.dist-info",
    "~rp_test_suite-*.dist-info",
)

for site_dir in [Path(p) for p in site.getsitepackages()] + [Path(site.getusersitepackages())]:
    if not site_dir.exists():
        continue
    for pattern in patterns:
        for path in site_dir.glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"[arp-workspace] removed stale editable metadata: {path}")
PY
}

clean_workspace_caches() {
  python - <<'PY'
import shutil
from pathlib import Path

targets = [Path("arp-spec"), Path("arp-devkit"), Path("arp-registry")]
removed = 0
for root in targets:
    if not root.exists():
        continue
    for path in root.rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path)
            removed += 1
    for path in root.rglob(".pytest_cache"):
        if path.is_dir():
            shutil.rmtree(path)
            removed += 1
print(f"[arp-workspace] removed generated cache directories: {removed}")
PY
}

trap clean_workspace_caches EXIT

clean_stale_editable_metadata

echo "[arp-workspace] bootstrapping grouped packages"
./arp-devkit/scripts/bootstrap.sh

echo "[arp-workspace] installing editable runtime and test-suite for integration checks"
python -m pip install -e ./arp-devkit/runtime
python -m pip install -e ./arp-devkit/test-suite

echo "[arp-workspace] validating a protocol example from arp-spec"
python - <<'PY'
from pathlib import Path
from arp_runtime.loader.yaml_loader import load_yaml_file
from arp_runtime.validator.validator import ProtocolValidator

path = Path("arp-spec/examples/sales-agent.yaml")
validator = ProtocolValidator()
result = validator.validate_agent_config(load_yaml_file(path))
if not result.valid:
    raise SystemExit("\n".join(result.errors))
print(f"validated protocol example {path}")
PY

echo "[arp-workspace] running arp-runtime against a runnable devkit example"
python -m arp_runtime.cli \
  --agent arp-devkit/examples/agents/sales-agent.yaml \
  --task "Customer asks for a discount" \
  --action "reply_inbound_dm" \
  --confidence 0.65 \
  --audit-log "${AUDIT_LOG}" \
  --report

test -f "${AUDIT_LOG}"

echo "[arp-workspace] running arp-test-suite"
pytest arp-devkit/test-suite/tests

echo "[arp-workspace] generating compliance report"
python -m arp_test_suite.runner \
  --project ./arp-devkit/runtime \
  --agent ./arp-devkit/examples/agents/sales-agent.yaml \
  --output "${COMPLIANCE_REPORT}"

test -f "${COMPLIANCE_REPORT}"

echo "[arp-workspace] checking registry/report conceptual alignment"
python - <<'PY' "${COMPLIANCE_REPORT}"
import json
import sys
from pathlib import Path

generated_report = json.loads(Path(sys.argv[1]).read_text())
registry_report_example = json.loads(Path("arp-registry/reports/compliance-report.example.json").read_text())
registry_entry = json.loads(Path("arp-registry/certified/sample-certified-project.json").read_text())

for report in (generated_report, registry_report_example, registry_entry["evidence"]["compliance_report"]):
    assert report["kind"] == "ARPComplianceReport"
    assert report["protocol_version"]
    assert report["report_id"]
    assert "summary" in report

assert registry_entry["references"]["report_id"] == registry_entry["evidence"]["compliance_report"]["report_id"]
print("registry compliance-report references conceptually match generated compliance reports")
PY

echo "[arp-workspace] smoke test complete"
echo "[arp-workspace] artifacts:"
echo "  audit log: ${AUDIT_LOG}"
echo "  compliance report: ${COMPLIANCE_REPORT}"
