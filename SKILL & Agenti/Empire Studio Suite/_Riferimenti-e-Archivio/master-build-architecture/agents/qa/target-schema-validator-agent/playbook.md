# Target-Schema-Validator Agent — Playbook

## Steps

### Step 1: Memory Bootstrap (P10)
- Create CP for this validation run
- Load previous validation reports

### Step 2: Identify Targets
- Determine what needs validation (all agents? skill structure? memory ecosystem?)
- Load appropriate schema (P06)

### Step 3: Validate Each Target
- Run ValidateTarget() or ValidateAllAgents()
- Compare actual vs schema
- Classify: COMPLIANT / PARTIAL / NON-COMPLIANT

### Step 4: Schema Tightening (PT06)
- If all targets COMPLIANT: tighten schema for next iteration
  - Add new required sections, increase min counts
- If targets PARTIAL: keep schema, fix targets first
- Log schema version in CP

### Step 5: Handoff
- If COMPLIANT: log CP, return to conductor
- If PARTIAL: handoff to agent-spec-builder for completion
- If NON-COMPLIANT: handoff to plan-builder for structural fix

### Step 6: Memory Update (P10)
- Create CP with validation report
- Update shared_state with compliance %
- Append to both INDEX

## Examples

### Example 1 — Agent Validation (PT05)
- 18 agents checked, all have 7 .md files → COMPLIANT
- Schema tightened: add min_fm_entries ≥ 5 for next pass

### Example 2 — Skill Validation
- SKILL.md present, frontmatter valid, ≤500 lines
- agents/ present (18 agents), references/ present, scripts/ present, memory/ present, evals/ present
- Result: COMPLIANT

### Example 3 — Memory Ecosystem Validation
- checkpoints/ ✅, decisions/ ✅, sessions/ ✅, plans/ ✅, architectures/ ✅, MEMORY-INDEX.md ✅
- Result: COMPLIANT

### Example 4 — Partial Agent (Missing Files)
- Agent has 4/7 files (missing playbook.md, evals.md, memory.md)
- Result: PARTIAL → handoff to agent-spec-builder

### Example 5 — Plan Validation
- PLAN-v1 has vision, scope, steps, but missing agents and memory sections
- Result: PARTIAL → handoff to plan-builder for PLAN-v2

## Anti-Patterns Rejected
- AP01: Scaffold as deliverable (validating stubs as complete)
- AP02: Permissive schemas (accepting 3 files as 7)
- AP06: Feature creep (adding non-canonical elements to schema)
