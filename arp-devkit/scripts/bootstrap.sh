#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

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

clean_stale_editable_metadata

echo "[arp-workspace] installing editable grouped packages"
python -m pip install -e ./arp-spec
python -m pip install -e ./arp-devkit

echo "[arp-workspace] bootstrap complete"
echo "Next step: ./arp-devkit/scripts/smoke_test.sh"
