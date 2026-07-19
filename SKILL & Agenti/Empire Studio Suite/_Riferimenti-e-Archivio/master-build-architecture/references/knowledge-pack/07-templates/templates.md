# Template — File Template per Artefatti

> **Fonte:** Knowledge Pack 07-templates + estrazioni da Content-Forge, Ruflo, Context-Engineering-Advisor.

## Template: Agent Spec (spec.md)

```markdown
# [Agent Name]

**Role:** [1-2 sentence description]
**Category:** [builders | pipeline | domain | qa | optimizers | self-improvement | conductor]
**Level:** [L1 | L2 | L3]

## Mission
[Clear mission statement, 2-3 sentences]

## Invariants (non-negotiable)
1. **[Principle/Pattern]:** [Description]
2. ...

## Activation
- Triggered when: [conditions]
- Input: [expected input]
- Output: [expected output]

## Connections
- Depends on: [other agents]
- Handoff to: [other agents]
```

---

## Template: System Prompt (system-prompt.md)

```markdown
# [Agent Name] — System Prompt

## Identity
You are the [Agent Name], [role description].

## Mission
[Clear mission, 2-3 sentences]

## Invariants (non-negotiable)
1. **[P/PT/CS]:** [Description + enforcement]
2. ...

## Procedure
1. Step 1
2. Step 2
3. ...

## Output Format
[Template for output]

## Anti-Patterns
- NEVER [anti-pattern 1]
- NEVER [anti-pattern 2]
```

---

## Template: Tools (tools.md)

```markdown
# [Agent Name] — Tools

## Tool 1: [Tool Name]
**Purpose:** [What it does]
**Input:** [Parameters]
**Output:** [Return value]
**Implementation:**
```python
def tool_name(params) -> return_type:
    """Docstring."""
    # Implementation
    pass
```

## Tool 2: ...
```

---

## Template: Playbook (playbook.md)

```markdown
# [Agent Name] — Playbook

## Steps
1. **Step 1:** [Description]
2. **Step 2:** [Description]
3. ...

## Examples

### Example 1 — Happy Path
**Prompt:** [User input]
**Expected:** [Expected output]
**Grade:** [X/10]

### Example 2 — Edge Case
**Prompt:** [Edge case input]
**Expected:** [Expected handling]

### Example 3 — Failure Recovery
**Prompt:** [Failure scenario]
**Expected:** [Recovery action]

## Anti-Patterns Rejected
- AP0X: [How this agent avoids it]
```

---

## Template: Evals (evals.md)

```markdown
# [Agent Name] — Evals

## Protocol
Per Skill-Criter evals loop + [relevant principles]:

## Test Cases

### [ID] — [Description]
**Prompt:** [Input]
**Expected:** [Expected output]
**Grade:** [X/10]

### [ID] — ...

## Benchmark
- With [agent]: [metric]
- Without [agent]: [metric]
- Delta: [improvement]

## Iteration
Run 1: [score] → failure-modes logged → Run 2: [improved score]
```

---

## Template: Failure Modes (failure-modes.md)

```markdown
# [Agent Name] — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-[ID] | [Failure description] | [Symptom] | [Prevention] | [Detection] | [Recovery] |
| ... | ... | ... | ... | ... | ... |

## Global Rules
- All failures logged to failure-modes-log/ (P09/P10/PT07)
- Trace: [relevant principles + case studies]
```

---

## Template: Memory (memory.md)

```markdown
# [Agent Name] — Memory

## Memory Mandate (P10)
Every [action] MUST be logged:
1. Create CP in memory/checkpoints/
2. Append to both MEMORY-INDEX.md (top + embedded)
3. Update shared_state
4. Sync between top and embedded memory

## Shared State
```json
{
  "[agent_state]": {
    "last_run": "[date]",
    "status": "[status]",
    "cps": ["[CP list]"]
  }
}
```

## Update Protocol
1. Before: load previous state
2. During: track actions
3. After: create CP, update INDEX, update shared_state

## Research→Plan→Reset→Implement
- Research: [what to research]
- Plan: [what to plan]
- Reset: [what to clear]
- Implement: [what to implement]

## Trace
- [Relevant principles, patterns, case studies]
```

---

## Template: Checkpoint (CP-XXX.md)

```markdown
# CP-[XXX] — [Short Description]

**Date:** [YYYY-MM-DD]
**Phase:** [P0-P7]
**Linked Principles:** [P01-P15, PT01-PT11]

## What Was Done
[Description]

## Output
[Files created/modified]

## Decision Made
[If any, DEC reference]

## Next Step
[What comes next]

## Trace
[Sources, principles, case studies]
```

---

## Template: Decision Record (DEC-XXX.md)

```markdown
# DEC-[XXX] — [Decision Title]

**Date:** [YYYY-MM-DD]
**Context:** [Why this decision was needed]

## Decision
[What was decided]

## Alternatives Considered
1. [Alternative 1] — [Why rejected]
2. [Alternative 2] — [Why rejected]

## Rationale
[Why this decision]

## Consequences
[What happens because of this decision]

## Trace
[Principles, patterns, case studies]
```

---

## Connessioni
- **Principi correlati:** P05 (Markdown+Python), P06 (shapes), PT05 (canonical files)
- **Agenti:** agent-spec-builder usa questi template per costruire agenti
