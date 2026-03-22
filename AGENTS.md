# AGENTS.md

## Purpose
This repository is the **ARP grouped workspace**: a pre-split repository that organizes the Agent Responsibility Protocol ecosystem into three clean targets ready for standalone repository extraction.

ARP is a **protocol for accountable agents**, not a full agent framework. Every coding agent must preserve that distinction in code, docs, tests, examples, and restructuring work.

The current grouped workspace contains these major areas:
- `arp-spec`
- `arp-devkit`
- `arp-registry`

These map to the intended standalone repositories of the same names.

---

## Non-negotiable ARP guardrails

### 1) ARP is a protocol, not a full agent framework
- Do **not** evolve ARP into a monolithic orchestration framework.
- Keep normative protocol concerns separate from runtime or integration concerns.

### 2) Protocol truth lives on the spec side only
- Normative definitions of ARP fields, schema structure, report shape, audit shape, protocol versions, and compatibility expectations must originate from `arp-spec/`.
- Runtime, test-suite, adapters, examples, and registry must not become alternate sources of protocol truth.

### 3) Downstream components must not invent alternate field names
- No downstream component may rename, fork, or redefine ARP field names for convenience.
- If a new field or concept is needed, add it on the spec side first and then propagate it outward.

### 4) Runtime, test-suite, adapters, and examples must align to `arp-spec`
- `arp-devkit/runtime`, `arp-devkit/test-suite`, `arp-devkit/adapters`, and `arp-devkit/examples` must consume or validate against the protocol source of truth.
- Fix drift by reconciling with `arp-spec`, not by local redefinition.

### 5) Registry must reference protocol/test concepts, not redefine them
- `arp-registry` should reference protocol versions, compliance reports, certification evidence, and compatibility artifacts.
- Registry data must not redefine protocol semantics or create registry-only substitute schema vocabularies.

### 6) Do not create monoliths
- Keep spec, devkit, and registry boundaries clean.
- Prefer explicit ownership and small targeted changes over convenience-driven consolidation.

### 7) Prioritize usability and consistency over old folder names
- The grouped 3-part structure is the current architectural truth.
- Do not preserve outdated names when doing so makes the future split less clean.

---

## Required workflow for substantial tasks

1. **Inspect current structure first**
   - Review the relevant grouped target (`arp-spec`, `arp-devkit`, or `arp-registry`) and the files affected.

2. **Make a short plan**
   - State a concise plan before making substantial edits.

3. **Implement minimally and cleanly**
   - Make the smallest coherent change set that solves the task while preserving clear future split boundaries.

4. **Run validation and tests**
   - Run the narrowest useful validation first, then broader checks as needed.
   - Keep the grouped smoke flow working.

5. **Commit changes**
   - Commit verified work on the current branch with a meaningful message.

---

## Grouped target responsibilities

### `arp-spec`
Owns:
- protocol schemas
- protocol versions
- normative examples
- RFCs and protocol docs
- governance and contribution rules
- packaged protocol artifacts under `src/arp_protocol`

### `arp-devkit`
Owns:
- the reference runtime
- the conformance/certification test-suite
- adapters and integration guidance
- runnable developer examples
- developer-oriented scripts and integration docs

### `arp-registry`
Owns:
- registry entry schemas
- compatibility/certification listing artifacts
- publication and trust docs
- references to protocol versions and compliance evidence

---

## Example split rule
Examples must stay conceptually split:

1. **Normative protocol examples** live under `arp-spec/examples`.
2. **Runnable developer examples** live under `arp-devkit/examples`.

Do not collapse these into one mixed examples area.

---

## Documentation expectations
- Update docs when structure, pathing, ownership, or workflow changes.
- Keep the root README aligned with the grouped 3-part structure.
- Keep `docs/repo-split-plan.md` and `docs/post-split-dependency-model.md` current as regrouping decisions evolve.

## Smoke-test expectations
- Keep `./arp-devkit/scripts/bootstrap.sh` and `./arp-devkit/scripts/smoke_test.sh` working as the documented workspace entry points unless they are explicitly replaced with a documented better flow.
- Do not leave the grouped workspace in a silently broken state.
