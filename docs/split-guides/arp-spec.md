# Export Guide: `arp-spec`

## 1. Source directories in `arp-workspace`

Copy the current `arp-spec/` subtree exactly as the source of truth:

```text
arp-spec/
```

## 2. Exact target directory structure

The standalone repository root should equal the current contents of
`arp-spec/`:

```text
README.md
LICENSE
VERSION
CONTRIBUTING.md
GOVERNANCE.md
pyproject.toml
build_backend.py
spec/
schemas/
examples/
rfcs/
docs/
src/arp_protocol/
```

## 3. Files to copy

Copy all files currently under `arp-spec/`, including:

- root files:
  - `README.md`
  - `LICENSE`
  - `VERSION`
  - `CONTRIBUTING.md`
  - `GOVERNANCE.md`
  - `pyproject.toml`
  - `build_backend.py`
- protocol docs:
  - `spec/*.md`
  - `rfcs/*.md`
  - `docs/*.md`
- schemas:
  - `schemas/*.json`
  - `src/arp_protocol/schemas/*.json`
- packaged protocol code:
  - `src/arp_protocol/__init__.py`
  - `src/arp_protocol/version.py`
- normative examples:
  - `examples/*.yaml`

## 4. Required standalone fixes

Apply only these standalone hardening fixes:

1. **README path fixes**
   - change any install command like `pip install -e ./arp-spec` to
     `pip install -e .`
   - change any tree diagram that shows `arp-spec/` as a nested directory so it
     reflects the standalone repository root

2. **Repository metadata fixes**
   - update `pyproject.toml` `[project.urls]` so `Homepage`, `Repository`, and
     `Issues` point to the real standalone repository

3. **Doc wording fixes**
   - remove wording that assumes this package lives inside the grouped workspace
   - keep wording that says `arp-spec` is the normative source of truth

4. **Do not change**
   - `schemas/*.json`
   - `src/arp_protocol/schemas/*.json`
   - RFCs, spec documents, examples, and governance docs except for clearly
     workspace-only path references

## 5. Validation commands

Run these inside the exported standalone repository root:

```bash
python -m pip install -e .
python -c "import json; from importlib import resources; from arp_protocol import PROTOCOL_VERSION; schema=json.loads((resources.files('arp_protocol') / 'schemas' / 'arp.schema.json').read_text()); print(PROTOCOL_VERSION, schema['title'])"
```

Optional additional checks:

```bash
python -c "from importlib import resources; print((resources.files('arp_protocol') / 'schemas' / 'report.schema.json').is_file())"
python -c "from pathlib import Path; print(sorted(p.name for p in Path('examples').glob('*.yaml')))"
```

## 6. Dependency relationships

- `arp-spec` has **no required runtime dependency** on `arp-devkit` or
  `arp-registry`.
- `arp-devkit` should consume protocol assets from `arp-spec`.
- `arp-registry` should reference protocol versions and protocol-shaped evidence
  from `arp-spec`, but must not redefine protocol structure.
