# Complete Quality Checklist — Agent Quality Sentinel

## Section 1: Frontmatter Validation

### name field
- [ ] Present
- [ ] Lowercase only (no uppercase letters)
- [ ] Only letters, numbers, hyphens (no underscores, spaces, dots)
- [ ] 3-50 characters
- [ ] Starts with letter or number
- [ ] Ends with letter or number
- [ ] Unique within the plugin (no two agents with same name)

**Scoring:** Pass/Fail — any failure is a Critical Issue

### description field
- [ ] Present
- [ ] Starts with "Use this agent when..."
- [ ] Contains at least 2 `<example>` blocks
- [ ] Length: 200-2000 characters (under 200 = too vague, over 2000 = unwieldy)
- [ ] Each example has: Context, user, assistant, commentary tags
- [ ] User messages in examples are realistic and specific (not generic like "help me")
- [ ] Commentary explains WHY this agent was triggered (not just "this is relevant")
- [ ] Covers at least 2 different phrasings of the trigger scenario
- [ ] Does NOT overlap completely with another agent's description

**Scoring:**
- All checks pass: 9-10/10
- 1-2 minor issues: 7-8/10
- Missing examples or too vague: 4-6/10
- Starts wrong or no examples: 1-3/10

### model field
- [ ] Present
- [ ] Value is one of: inherit, opus, sonnet, haiku
- [ ] Assignment is justified by task complexity

**Correct assignments:**
- `opus`: complex reasoning, multi-step judgment, strategic decisions, orchestration with full context
- `sonnet`: writing, coding, research, balanced analysis
- `haiku`: classification, routing, formatting, JSON parsing, simple decisions
- `inherit`: default choice when no specific need

**Scoring:** Pass/Fail for validity; score -1 for each unjustified assignment

### color field
- [ ] Present
- [ ] Value is one of: blue, cyan, green, yellow, magenta, red
- [ ] Distinct color from other agents in the same plugin (recommended, not required)

**Scoring:** Pass/Fail

### tools field
- [ ] If present: valid array
- [ ] Each tool name is valid: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, Agent, TodoWrite, Task
- [ ] No unnecessary tools (least-privilege principle applied)

**Least-privilege check:**
- Research-only agent: should NOT have Write, Edit, Bash
- Read-only analyzer: should NOT have Write
- Orchestrator: acceptable to have all tools or omit field

**Scoring:** Critical Issue if invalid tool names; Major Issue if over-privileged

---

## Section 2: System Prompt Quality

### Identity & Persona (0-10)
- [ ] Starts with "You are..." in second person, present tense
- [ ] Role is specific (not just "a helpful assistant")
- [ ] Domain is narrow and precise
- [ ] Implies expertise level (years, methodology, school of thought)
- [ ] Does NOT start with "I am..." (first person = wrong)

**Score 9-10:** Expert identity with methodology and standards
**Score 7-8:** Clear role and domain, missing methodology
**Score 5-6:** Vague role, no domain specificity
**Score 1-4:** Generic ("helpful assistant") or first-person

### Mission Statement (0-10)
- [ ] Present (even if just one sentence)
- [ ] Specific to this agent's actual task
- [ ] Output-focused ("produce X" not "help with X")
- [ ] Measurable or concrete

**Score 9-10:** "Transform [input] into [precise output] that achieves [specific goal]"
**Score 7-8:** Clear goal but missing precision
**Score 5-6:** Generic goal
**Score 1-4:** No mission statement

### Core Responsibilities (0-10)
- [ ] Present
- [ ] 3-6 items (fewer = too vague, more = unfocused)
- [ ] Each item is specific to this agent's role
- [ ] No overlaps with other agents' responsibilities
- [ ] Uses active verbs

**Score 9-10:** 4-5 specific, actionable responsibilities
**Score 7-8:** 3-4 responsibilities, minor vagueness
**Score 5-6:** Too few or too generic
**Score 1-4:** Missing or "assist the user with things"

### Operating Process (0-10)
- [ ] Present
- [ ] Numbered steps (not bullet soup)
- [ ] Each step is specific (not "do X well")
- [ ] Steps include reasoning ("do X because Y")
- [ ] Covers the full workflow from input to output
- [ ] Accounts for validation/checking steps

**Score 9-10:** 4-8 steps with reasoning, covers full workflow including edge checks
**Score 7-8:** Clear steps, missing reasoning or 1-2 gaps
**Score 5-6:** Generic steps ("research the topic, write the output")
**Score 1-4:** No process section

### Output Contract (0-10)
- [ ] Present
- [ ] Specifies exact format (not "a good analysis")
- [ ] Shows template with field names if structured output
- [ ] States what format (JSON, markdown, plain text, etc.)
- [ ] States what NOT to include

**Score 9-10:** Exact template shown, format specified, exclusions noted
**Score 7-8:** Format specified, no template
**Score 5-6:** Vague ("produce a detailed report")
**Score 1-4:** No output contract

### Hard Constraints (0-10)
- [ ] Present
- [ ] "Never" list: specific prohibitions with brief reasons
- [ ] "Always" list: non-negotiable behaviors
- [ ] Includes safety/quality constraints
- [ ] Not trivially obvious ("never be rude" = useless constraint)

**Score 9-10:** 3-5 specific Never/Always with reasons
**Score 7-8:** Some constraints, missing reasons
**Score 5-6:** Only obvious constraints
**Score 1-4:** No constraints section

### Edge Case Handling (0-10)
- [ ] Present
- [ ] Covers the most likely failure scenarios for this agent
- [ ] Provides specific behavior for each case (not "handle gracefully")
- [ ] Covers empty/null input case
- [ ] Covers malformed input case

**Score 9-10:** 3-5 specific scenarios with exact behavior
**Score 7-8:** Some scenarios covered
**Score 5-6:** Generic ("handle errors appropriately")
**Score 1-4:** No edge cases

---

## Section 3: Architecture Coherence

For the complete agent system:

### Responsibility Clarity
- [ ] Each agent has ONE primary responsibility
- [ ] No two agents share the same primary responsibility
- [ ] Every responsibility in the workflow is owned by exactly one agent

### Hierarchy Integrity
- [ ] Orchestrator(s) identified and their role is coordination-only
- [ ] Specialists do not orchestrate (no specialist spawning other agents)
- [ ] Data flow is documented and logical

### Coverage
- [ ] No workflow steps are missing an agent to handle them
- [ ] No orphan agents (agents with no clear input source)
- [ ] Start and end of workflow are clearly defined

### Model Efficiency
- [ ] Expensive models (opus) used only where reasoning complexity warrants
- [ ] Cheap models (haiku) used for simple/fast tasks
- [ ] Mix of models = lower cost and appropriate quality per task

---

## Section 4: Overall Scoring Formula

```
Agent Score = (TQS × 0.25) + (SPDS_avg × 0.5) + (ACC × 0.25)

TQS = Triggering Quality Score (description quality)
SPDS_avg = average of 7 system prompt dimension scores
ACC = Architecture Coherence (10 if all pass, -1 per failure)
```

| Overall Score | Verdict |
|---|---|
| 9-10 | Production-ready. Install immediately. |
| 7-8 | Good. Minor improvements recommended before production. |
| 5-6 | Needs work. Major issues will cause inconsistent behavior. |
| 3-4 | Significant rework needed. Do not install yet. |
| 1-2 | Start over with agent-architect. |
