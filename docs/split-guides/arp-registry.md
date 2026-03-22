# Export Guide: `arp-registry`

## 1. Source directories in `arp-workspace`

Copy the current `arp-registry/` subtree:

```text
arp-registry/
```

## 2. Exact target directory structure

The standalone repository root should equal the current contents of
`arp-registry/`:

```text
README.md
LICENSE
VERSION
compatible/
certified/
reports/
schemas/
docs/
```

## 3. Files to copy

Copy all files currently under `arp-registry/`, including:

- root files:
  - `README.md`
  - `LICENSE`
  - `VERSION`
- sample registry listings:
  - `compatible/*.json`
  - `certified/*.json`
- report artifacts:
  - `reports/compliance-report.example.json`
  - `reports/compliance-report.example.sig`
- schemas:
  - `schemas/registry-entry.schema.json`
- docs:
  - `docs/certification-process.md`
  - `docs/recertification-policy.md`
  - `docs/signature-model.md`
  - `docs/trust-model.md`

## 4. Required standalone fixes

Apply these standalone fixes after export:

1. **README path fixes**
   - update `README.md` so references like `../arp-spec` and
     `../arp-devkit/test-suite` no longer assume the grouped workspace
   - replace them with:
     - links to the standalone repositories, or
     - plain textual references to `arp-spec` and `arp-devkit`

2. **Schema reference fixes**
   - `schemas/registry-entry.schema.json` currently references
     `../../arp-spec/schemas/compliance-report.schema.json`
   - replace that with the standalone strategy you choose:
     - an absolute repository URL
     - a published schema URL
     - or a vendored schema copy if the standalone repo intentionally freezes a
       compatible reference artifact

3. **Docs fixes**
   - update registry docs that mention grouped sibling directories so they read
     correctly as standalone documentation
   - preserve the principle that registry references protocol and compliance
     evidence but does not redefine protocol semantics

4. **Sample metadata review**
   - sample project repository URLs currently use `github.com/example/...`
   - keep them if they are intentionally fictional examples, or replace them if
     the standalone registry repository should ship more realistic sample data

## 5. Validation commands

Run lightweight standalone checks from the exported registry root:

```bash
python - <<'PY'
import json
from pathlib import Path

registry_entry = json.loads(Path('certified/sample-certified-project.json').read_text())
report_example = json.loads(Path('reports/compliance-report.example.json').read_text())

assert registry_entry['kind'] == 'ARPRegistryEntry'
assert registry_entry['evidence']['compliance_report']['kind'] == 'ARPComplianceReport'
assert report_example['kind'] == 'ARPComplianceReport'
print('registry samples load successfully')
PY
```

If you also export `arp-spec`, add a follow-up validation that resolves the
registry schema `$ref` against the standalone `arp-spec` schema location you
selected.

## 6. Dependency relationships

- `arp-registry` depends conceptually on `arp-spec` for protocol versions and
  report/schema meaning.
- `arp-registry` depends conceptually on `arp-devkit/test-suite` output for
  compliance evidence formats and certification artifacts.
- `arp-registry` must not become a second source of protocol truth; it should
  reference released protocol and compliance evidence rather than redefine them.
