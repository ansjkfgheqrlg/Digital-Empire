# Coverage-Verifier Agent — Playbook

## Steps

### Step 1: Memory Bootstrap (P10)
- Create CP for this coverage run
- Load previous coverage reports from memory/
- Load current state of knowledge-pack and outputs

### Step 2: Research — Enumerate Sources (P12/PT09)
- Run EnumerateSourceAtoms(scope="all")
- Categories: P01-P15, PT01-PT11, AP01-AP09, CS01-CS04, glossary, clone-sections, advisor-patterns, skill-creator-rules, user-inputs
- Expected: 80-120+ atoms depending on scope

### Step 3: Research — Enumerate Outputs
- Run EnumerateOutputAtoms()
- Scan: SKILL.md, agents/**/*.md, references/knowledge-pack/**/*.md, scripts/*.py, memory/*.md
- Extract traceability headers (P01, PT05, CS03, etc.)

### Step 4: Synthesize — Build Coverage Map
- For each source atom, find all output references
- Classify: full (≥3), partial (1-2), orphan (0)
- Generate orphan list

### Step 5: Plan — Coverage Report
- If coverage ≥ 90%: report PASS
- If coverage 70-89%: report WARN with gaps
- If coverage < 70%: report FAIL with critical gaps

### Step 6: Handoff
- If PASS: log CP, update INDEX, return to conductor
- If WARN: handoff to reference-expander-agent (O3) to fill gaps
- If FAIL: handoff to plan-builder (P01) for remediation plan

### Step 7: Memory Update (P10)
- Create CP with coverage report
- Append to both INDEX (top + embedded)
- Log to failure-modes if gaps found

## Examples

### Example 1 — Happy Path (Full Coverage)
- Source atoms: 95 (15P + 11PT + 9AP + 4CS + glossary + clones)
- Full coverage: 88 (92.6%)
- Partial: 7 (7.4%)
- Orphan: 0
- Result: PASS → CP-0XX logged

### Example 2 — Gaps Found (Partial Coverage)
- Source atoms: 95
- Full: 60, Partial: 20, Orphan: 15
- Orphans: AP03-AP09 not cited in any agent, CS02 not referenced
- Result: WARN → handoff to reference-expander

### Example 3 — Failure (Low Coverage)
- After first SKILL.md build (before depth pass)
- Coverage: 45% — most P/PT/AP not referenced in agents
- Result: FAIL → handoff to plan-builder for P5 depth pass

### Example 4 — Meta Coverage (Self-Check)
- Source atoms include our own build history (CPs, ANALYSIS)
- Verify these are referenced in SKILL.md visibility section
- Meta-traceability check

## Anti-Patterns Rejected
- AP01: Claiming coverage without running scan
- AP02: Counting metadata (CATALOG) as content coverage
- AP08: Skipping failure-mode reporting for gaps
