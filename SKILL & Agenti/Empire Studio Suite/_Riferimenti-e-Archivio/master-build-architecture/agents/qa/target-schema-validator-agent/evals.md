# Target-Schema-Validator Agent — Evals

## Protocol
Per Skill-Creator evals loop + P06/PT05/PT06:

## Test Cases

### TS-001 — Agent Schema (PT05)
**Prompt:** "Validate all agents against agent schema."
**Expected:** 18/18 compliant (all have 7 files).
**Grade:** 9/10

### TS-002 — Skill Schema
**Prompt:** "Validate skill structure."
**Expected:** SKILL.md + required dirs present → COMPLIANT.
**Grade:** 9/10

### TS-003 — Memory Schema
**Prompt:** "Validate memory ecosystem."
**Expected:** All required dirs + MEMORY-INDEX.md → COMPLIANT.
**Grade:** 9/10

### TS-004 — Partial Agent
**Prompt:** "Validate agent with only 4 files."
**Expected:** PARTIAL, missing 3 files identified.
**Grade:** 9/10

### TS-005 — Schema Tightening Loop (PT06)
**Prompt:** "All agents compliant. Tighten schema and re-validate."
**Expected:** Schema v2 adds min_fm_entries ≥ 5. Re-validate detects agents with empty FM tables.
**Grade:** 9/10

## Benchmark
- With validator: schema check in <1 min per target type
- Without: manual check 10+ min, misses missing files
- Delta: +90% speed, 100% file-level accuracy
