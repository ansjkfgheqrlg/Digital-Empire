# Prompt Frameworks for Agent System Prompts

## Framework 1: Chain-of-Thought (CoT)

**Use when:** The agent must solve multi-step problems where intermediate reasoning affects the final answer.

**How to embed in system prompt:**
```
Before providing your answer, reason through the problem step by step.
Structure your thinking as:
ANALYSIS: [What do you know about the input?]
REASONING: [What logic applies here?]
CONCLUSION: [What is the correct output?]
```

**Best for:** Analyst agents, decision-making agents, code review agents.

---

## Framework 2: ReAct (Reason + Act)

**Use when:** The agent uses tools and must interleave reasoning with tool calls.

**How to embed in system prompt:**
```
Follow the ReAct loop:
THOUGHT: What do I need to know or do next?
ACTION: [tool call]
OBSERVATION: What did I learn from the result?
[Repeat until you have enough to produce the final output]
FINAL ANSWER: [Produce output]
```

**Best for:** Research agents, code-writing agents, any agent using Bash/Read/Grep/WebSearch.

---

## Framework 3: Tree of Thoughts (ToT)

**Use when:** The problem has multiple possible approaches and the agent must explore and evaluate them.

**How to embed in system prompt:**
```
For this task, generate 3 different approaches before committing to one.
For each approach, briefly evaluate:
- Pros
- Cons
- Feasibility
Then select the best approach and execute it.
```

**Best for:** Architecture agents, strategy agents, creative agents where quality trumps speed.

---

## Framework 4: Self-Consistency

**Use when:** Accuracy is critical and the agent might make errors on single-pass reasoning.

**How to embed in system prompt:**
```
Solve this problem 3 times independently, then compare your answers.
If 2 or more answers agree, use that as your final answer.
If all 3 differ, analyze which reasoning chain is most sound and explain why.
```

**Best for:** Mathematical agents, data analysis agents, code generation agents.

---

## Framework 5: Critic-in-the-Loop

**Use when:** Quality control is built into a single agent (no separate critic agent available).

**How to embed in system prompt:**
```
After producing your output:
1. Switch to CRITIC mode
2. Evaluate your output against these criteria: [list criteria]
3. Score each criterion 1-5
4. If any criterion scores below 4, revise and repeat
5. Output only when all criteria score 4+
```

**Best for:** Copywriting agents, code generation agents, any quality-sensitive output.

---

## Framework 6: Persona-Grounded Reasoning

**Use when:** The agent's domain expertise should actively shape HOW it reasons, not just WHAT it produces.

**How to embed in system prompt:**
```
As a [EXPERT PERSONA], your reasoning is shaped by [methodology/school of thought].
When analyzing [input type], you instinctively consider:
- [Domain-specific lens 1]
- [Domain-specific lens 2]
- [Domain-specific lens 3]
Your outputs carry the authority and precision of [years/expertise level] in [domain].
```

**Best for:** Domain-specialist agents where generic AI thinking would produce generic results.

---

## Combining Frameworks

High-performance agents often combine frameworks. Example for a complex analyst agent:

```
## OPERATING PROCESS

1. ANALYSIS (CoT): Reason through the input step by step. What is being asked? What data is present? What is missing?

2. EXPLORATION (ToT): Generate 2-3 analytical approaches. Evaluate each briefly. Select the most sound.

3. EXECUTION (ReAct): Execute the selected approach using available tools.
   THOUGHT → ACTION → OBSERVATION [repeat]

4. QUALITY CHECK (Critic-in-the-Loop): Evaluate your analysis against the quality standards. Revise if needed.

5. OUTPUT: Produce the final output in the specified format.
```

This combination produces elite-level analytical outputs.
