# SKILL
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > agent-factory > skills > system-prompt-forge]]

## Content

---
name: system-prompt-forge
description: This skill should be used when the user needs to "write a system prompt for an agent", "create the instructions for an agent", "forge a system prompt", "write agent instructions", "make the prompt for my agent", "turn a blueprint into system prompts", or after the agent-architect skill has produced an Architecture Blueprint. Trigger this skill as the SECOND step in agent creation, after architecture is defined. Also trigger it when the user says an agent is not behaving correctly and the system prompt needs to be rewritten. This skill transforms architectural blueprints into elite, production-grade system prompts that define precise agent behavior, constraints, persona, and output format.
version: 1.0.0
---

# System Prompt Forge

This is the second skill in the agent-factory pipeline. Its input is the Architecture Blueprint from `agent-architect`. Its output is a complete, production-grade system prompt for every agent defined in the blueprint.

A system prompt is not a description. It is the agent's entire identity, cognitive framework, and behavioral ruleset. A weak system prompt produces an inconsistent, generic agent. An elite system prompt produces an agent that is sharp, reliable, and domain-expert-level.

## Core Principle

Write system prompts in second person, present tense. The agent IS the role — it does not pretend to be it.

**Wrong:** "You should act as a marketing expert when the user asks for copy."
**Right:** "You are a senior direct-response copywriter with 15 years of CRO expertise. Every word you write is optimized for conversion."

The second version creates identity. The first creates a cosplay.

## The Forge Process

### Step 1: Read the Blueprint

Before writing a single word, read the Architecture Blueprint from agent-architect. Extract for each agent:
- Name and role
- Inputs it receives
- Outputs it must produce
- Tools it has access to
- Model assigned to it
- Edge cases it must handle

### Step 2: Build Each System Prompt

Write one system prompt per agent. For each, use the Elite System Prompt Template below.

Consult `references/prompt-frameworks.md` for advanced frameworks (Chain-of-Thought, ReAct, Tree-of-Thought, etc.) and `references/persona-patterns.md` for elite persona construction.

### Elite System Prompt Template

```markdown
## IDENTITY & ROLE
You are [SPECIFIC ROLE] specializing in [NARROW DOMAIN].
[1-2 sentences establishing expert-level identity with years/depth of experience implied.]
[Optional: Reference to methodology or school of thought the agent follows.]

## YOUR MISSION
[One sentence. What you must accomplish in this conversation/task.]
[Make it aspirational but concrete. Not "help the user" — "produce X that achieves Y."]

## CORE RESPONSIBILITIES
[List 3-6 specific responsibilities. Not generic. Tied to this agent's exact role.]
1. [Responsibility tied to this agent's specific domain]
2. [What this agent owns exclusively]
3. [What this agent produces that others depend on]

## OPERATING PROCESS
Follow this exact process for every task:

1. **[Step name]**: [What to do and why]
2. **[Step name]**: [What to do and why]
3. **[Step name]**: [What to check or validate]
4. **[Step name]**: [How to produce output]

[Include reasoning for steps, not just the steps themselves. Smart agents follow WHY, not just WHAT.]

## INPUT CONTRACT
Expect to receive: [Exact format of input — JSON, plain text, file path, etc.]
Key fields to parse: [List relevant fields]
If input is malformed: [What to do — ask for clarification, fail gracefully, etc.]

## OUTPUT CONTRACT
Always produce output in this exact format:

[Show exact template with field names and expected content]

Never deviate from this format. Other agents and systems depend on it.

## QUALITY STANDARDS
Before finalizing any output, verify:
- [ ] [Criterion 1 — specific and measurable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

[Optional: Include a self-scoring rubric if the agent must evaluate its own output.]

## HARD CONSTRAINTS
Never:
- [Constraint 1 — what the agent must NEVER do, with brief reason]
- [Constraint 2]
- [Constraint 3]

Always:
- [Non-negotiable behavior 1]
- [Non-negotiable behavior 2]

## EDGE CASE HANDLING
- If [scenario]: [exact behavior]
- If [scenario]: [exact behavior]
- If [scenario]: [exact behavior]

## COLLABORATION PROTOCOL
[Only for agents that communicate with others.]
When you receive output from [upstream agent]: [how to process it]
When you pass output to [downstream agent]: [what format, what fields must be populated]
```

### Step 3: Calibrate Tone and Depth per Model

The system prompt style should match the model assigned:

**For Opus agents (reasoning/judgment):**
- Longer process sections with explicit reasoning steps
- Include "think before you act" instructions
- Add explicit uncertainty handling ("if you are not confident, say so")

**For Sonnet agents (balanced):**
- Standard template, balanced between instruction and freedom
- Include examples where useful but not exhaustive

**For Haiku agents (speed/parsing):**
- Short, directive system prompts
- No long reasoning chains — just clear in/out contracts
- Focus on format compliance over reasoning depth

### Step 4: Test the Prompt Mentally

For each system prompt, run a mental simulation:
1. Give the agent a typical input
2. Does the process section tell it exactly what to do?
3. Does the output contract tell it exactly what to produce?
4. Are there any ambiguities that could cause inconsistent behavior?

Fix all ambiguities before handing off to agent-builder.

### Step 5: Document and Hand Off

Produce a System Prompts Document with all prompts clearly labeled:

```
# System Prompts for [AGENT NAME] — [date]

## Agent: [agent-name]
Model: [model]
Tools: [tools]

### System Prompt:
[full system prompt]

---

## Agent: [agent-name-2]
...
```

Then tell the user:
> "System prompts ready. The next step is **agent-builder** to create the actual plugin files. Say 'build the agents' to continue."

## Common System Prompt Mistakes

**Too generic:** "You are a helpful assistant that helps with marketing." — No domain expertise, no process, no constraints.

**Too rigid:** Listing 40 rules in ALL CAPS. — Agents follow principles, not military orders. Explain the why.

**Missing output contract:** Saying "produce a good analysis" without specifying format. — Downstream agents or users will receive inconsistent output.

**No edge cases:** Not handling the empty/invalid/unexpected input case. — Real data is messy. Agents must be robust.

**Identity mismatch:** System prompt says "expert analyst" but tools only allow reading one file. — Align identity with actual capabilities.

## Additional Resources

- **`references/prompt-frameworks.md`** — CoT, ReAct, ToT, Self-Consistency and other reasoning frameworks
- **`references/persona-patterns.md`** — How to build elite agent personas for different domains

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
