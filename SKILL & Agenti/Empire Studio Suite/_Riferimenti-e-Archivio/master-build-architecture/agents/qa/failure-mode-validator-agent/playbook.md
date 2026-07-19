# Failure-Mode-Validator Agent — Playbook

## Steps

### Step 1: Memory Bootstrap (P10)
- Create CP for this validation run
- Load previous validation reports

### Step 2: Scan All Agents
- Run ScanAgentDirectory()
- Expected: 18+ agents across categories (builders, pipeline, domain, qa, optimizers, self-improvement, conductor)

### Step 3: Validate Each Agent
- For each agent: run ValidateFailureModes()
- Check: file exists, ≥5 table entries, SI cross-refs, memory integration

### Step 4: Synthesize Report
- Aggregate: compliant %, partial %, missing %
- Detail: per-agent issues

### Step 5: Handoff
- If all compliant: log CP, return to conductor
- If any partial/missing: handoff list to agent-spec-builder (PT05) for completion
- If critical gaps: handoff to plan-builder for remediation

### Step 6: Memory Update (P10)
- Create CP with validation report
- Append to both INDEX
- Update shared_state

## Examples

### Example 1 — Happy Path (All Compliant)
- 18 agents scanned, all have failure-modes.md with ≥5 entries + SI + memory
- Result: PASS, 100% compliant

### Example 2 — Partial Coverage
- 18 agents: 14 compliant, 3 partial (<5 entries), 1 missing
- Result: WARN, handoff to agent-spec-builder for 4 agents

### Example 3 — Early Build (Many Missing)
- After initial build, only 5/18 agents have failure-modes.md
- Result: FAIL, handoff to plan-builder for batch completion

### Example 4 — Meta Check (Self-Validation)
- Validate failure-modes of this agent (self-check)
- Verify our own FM table has ≥5 entries + SI + memory refs

### Example 5 — Regression After Update
- Re-run after agent updates: previously compliant agent now missing SI refs
- Result: REGRESSION, flag for review

## Anti-Patterns Rejected
- AP02: Permissive schemas (accepting <5 entries as compliant)
- AP08: No failure-mode doc (the very thing we validate against)
- AP09: Premature optimization (skip validation to go faster)
