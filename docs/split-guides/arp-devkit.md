# Export Guide: `arp-devkit`

## 1. Source directories in `arp-workspace`

Copy the current `arp-devkit/` subtree:

```text
arp-devkit/
```

## 2. Exact target directory structure

The standalone repository root should equal the current contents of
`arp-devkit/`:

```text
README.md
LICENSE
VERSION
pyproject.toml
build_backend.py
runtime/
  src/
  tests/
test-suite/
  docs/
  fixtures/
  schemas/
  src/
  tests/
adapters/
examples/
  agents/
  demo_outputs/
  demo_tasks/
  docs/
docs/
scripts/
```

## 3. Files to copy

Copy all files currently under `arp-devkit/`, especially:

- repo root:
  - `README.md`
  - `LICENSE`
  - `VERSION`
  - `pyproject.toml`
  - `build_backend.py`
- runtime package:
  - `runtime/README.md`
  - `runtime/VERSION`
  - `runtime/pyproject.toml`
  - `runtime/build_backend.py`
  - `runtime/src/arp_runtime/**/*.py`
  - `runtime/tests/*.py`
- test-suite package:
  - `test-suite/README.md`
  - `test-suite/VERSION`
  - `test-suite/pyproject.toml`
  - `test-suite/build_backend.py`
  - `test-suite/docs/*.md`
  - `test-suite/fixtures/*`
  - `test-suite/schemas/*.json`
  - `test-suite/src/arp_test_suite/**/*.py`
  - `test-suite/tests/**/*.py`
- adapters:
  - `adapters/**`
- examples:
  - `examples/README.md`
  - `examples/agents/*.yaml`
  - `examples/demo_outputs/*`
  - `examples/demo_tasks/*`
  - `examples/docs/*.md`
- developer docs/scripts:
  - `docs/README.md`
  - `scripts/bootstrap.sh`
  - `scripts/smoke_test.sh`
  - `scripts/split_repos.md`

## 4. Required standalone fixes

Apply these standalone fixes after export:

### 4.1 Packaging and dependency paths

Update workspace-specific file URIs and relative references:

- `runtime/pyproject.toml`
  - replace `arp-protocol @ file:///workspace/arp-workspace/arp-spec` with the
    chosen standalone dependency strategy:
    - a published version constraint, or
    - a local file URI rooted in the standalone export environment
- `runtime/build_backend.py`
  - replace the hard-coded `ROOT.parents[1] / "arp-spec"` dependency URI logic
    with standalone-compatible dependency resolution
- `test-suite/pyproject.toml`
  - replace:
    - `arp-protocol @ file:///workspace/arp-workspace/arp-spec`
    - `arp-runtime @ file:///workspace/arp-workspace/arp-devkit/runtime`
- `test-suite/build_backend.py`
  - replace the hard-coded workspace dependency URIs with standalone-compatible
    resolution

### 4.2 README and docs fixes

Update any docs that assume sibling folders in the grouped workspace:

- `README.md`
- `runtime/README.md`
- `examples/README.md`
- `test-suite/README.md`
- adapter docs that point to `../../arp-spec` or `../runtime`

Typical fixes:

- change `pip install -e ./arp-spec` / `pip install -e ./arp-devkit/runtime`
  instructions to standalone equivalents
- change `../../arp-spec` references to the published or cloned standalone
  `arp-spec` repository
- update example CLI paths so they work from the standalone devkit root

### 4.3 Script fixes

`scripts/bootstrap.sh` and `scripts/smoke_test.sh` currently assume the grouped
workspace exists with sibling `arp-spec/` and `arp-registry/`.

For a standalone `arp-devkit` repo, decide one of these strategies and update
the scripts consistently:

1. **Clone-based local integration strategy**
   - require sibling clones of standalone `arp-spec` and `arp-registry`
   - update README to document the required checkout layout

2. **Published-dependency strategy**
   - install `arp-spec` from a package index or VCS URL
   - keep registry alignment checks against checked-in sample artifacts that no
     longer assume a sibling `arp-registry`

At minimum, fix these workspace-specific assumptions in the scripts:

- `ROOT_DIR` logic that expects the grouped repository root
- direct references to:
  - `./arp-devkit/runtime`
  - `./arp-devkit/test-suite`
  - `arp-spec/examples/...`
  - `arp-registry/...`
  - `/tmp/arp-workspace-smoke...` log prefixes

### 4.4 Test fixes

Many tests currently assume the grouped workspace root exists. Update:

- `runtime/tests/*.py`
- `test-suite/tests/**/*.py`

Common changes:

- remove `sys.path.insert(... / "arp-spec" / "src")` assumptions
- point example loading either at:
  - exported standalone examples within `arp-devkit`, or
  - an installed/published `arp-spec` package

## 5. Validation commands

After export and standalone fixes, run from the standalone devkit root:

```bash
python -m pip install -e .
python -m pip install -e ./runtime
python -m pip install -e ./test-suite
pytest runtime/tests
pytest test-suite/tests
./scripts/bootstrap.sh
./scripts/smoke_test.sh
```

If bootstrap/smoke are rewritten to depend on separately cloned standalone repos,
document and run the exact clone/setup commands in the exported README.

## 6. Dependency relationships

- `arp-devkit` depends on `arp-spec` for protocol truth.
- `arp-devkit/runtime` should consume packaged schemas/version metadata from
  `arp-spec`.
- `arp-devkit/test-suite` depends on:
  - `arp-spec` for protocol truth
  - `arp-runtime` for reference execution behavior
- `arp-devkit` may generate artifacts later consumed by `arp-registry`, but it
  should not own registry schema definitions.
