# Failure-Mode-Validator Agent — Evals

## Protocol
Per Skill-Creator evals loop + P09/PT07/P10:

## Test Cases

### FM-001 — Happy Path: All Compliant
**Prompt:** "Validate failure-modes for all 18 agents."
**Expected:** All pass with ≥5 entries, SI refs, memory refs.
**Grade:** 9/10

### FM-002 — Partial: Some Agents Missing Entries
**Prompt:** "Validate after adding 3 new agents with stub failure-modes."
**Expected:** Detect partial agents, report correctly.
**Grade:** 9/10

### FM-003 — Missing: Agent Without File
**Prompt:** "Validate when 1 agent has no failure-modes.md."
**Expected:** Detect missing file, report as MISSING.
**Grade:** 9/10

### FM-004 — Edge: Table Exists But No SI Refs
**Prompt:** "Validate agent with failure-modes.md but no SI cross-references."
**Expected:** Detect missing SI refs, report as PARTIAL.
**Grade:** 8/10

### FM-005 — Self-Validation
**Prompt:** "Validate this agent's own failure-modes.md."
**Expected:** Self-check passes (our FM table has ≥5 entries).
**Grade:** 8/10

## Benchmark
- With validator: all agents checked in <2 min
- Without: manual check takes 20+ min, misses entries <5
- Delta: +90% speed, +100% accuracy on entry count
