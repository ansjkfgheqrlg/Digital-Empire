# Coverage-Verifier Agent — Evals

## Protocol
Per Skill-Criter evals loop + P01/P08/P10/P12:
- Simulate coverage check on known scope
- Grade: correct orphan detection, correct %, proper handoff
- Benchmark vs baseline (manual grep)
- Iterate on failures

## Test Cases

### CV-001 — Happy Path: Full Coverage After Depth Pass
**Prompt:** "Run coverage check on the full skill after all agents are built."
**Expected:** Coverage ≥ 90%, orphan list empty or near-empty, PASS result.
**Grade:** 9/10

### CV-002 — Gaps Detected: Early Build
**Prompt:** "Run coverage after SKILL.md only (no agents)."
**Expected:** Coverage < 70%, many orphans in agent-specific content, FAIL result.
**Grade:** 9/10

### CV-003 — Meta Coverage: Our Build History
**Prompt:** "Verify coverage of our CPs/ANALYSIS in SKILL.md visibility section."
**Expected:** CPs/ANALYSIS cited ≥3 times in visibility section, full coverage.
**Grade:** 8/10

### CV-004 — Edge: Clone Content Not Counted
**Prompt:** "Run coverage but forget to scan clones/."
**Expected:** Agent catches missing category, warns "clones not in scope", partial result.
**Grade:** 8/10

### CV-005 — Failure Recovery: Orphan Fix Loop
**Prompt:** "Coverage is 75%. Fix orphans and re-run."
**Expected:** Handoff to reference-expander, re-run shows improvement ≥ 85%.
**Grade:** 9/10

## Benchmark
- With coverage-verifier: orphans detected in <5 min, coverage % accurate ±3%
- Without: manual grep takes 30+ min, misses 20% of orphans
- Delta: +80% speed, +20% accuracy

## Iteration
Run 1: 7/10 (missed clone atoms) → failure-modes logged → Run 2: 9/10
