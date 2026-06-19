# architecture-patterns
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > agent-factory > skills > agent-architect > references]]

## Content

# Agent Architecture Patterns

## Pattern 1: Single Agent

**When to use:** One well-defined task, no need for parallelism, low complexity.

**Structure:**
```
User → Agent → Output
```

**Example:** A code reviewer that reads a file and produces a review report.

**Frontmatter model:** `inherit` or `sonnet`

**Anti-pattern:** Using a single agent for tasks that require 3+ distinct domains of expertise.

---

## Pattern 2: Specialist + Orchestrator

**When to use:** 2-5 sub-tasks that are clearly separable, sequential or parallel execution needed.

**Structure:**
```
User → Orchestrator → [Specialist A]
                    → [Specialist B]
                    → [Specialist C]
                    ↓
               Final Assembly → Output
```

**Example:** A content creation system:
- Orchestrator: receives brief, routes tasks, assembles final output
- Researcher: finds information, facts, data
- Writer: produces draft content
- Editor: refines tone, grammar, CTA

**Key rules:**
- Orchestrator NEVER does specialist work
- Specialists NEVER communicate directly with each other
- All data passes THROUGH the orchestrator

---

## Pattern 3: Multi-Layer Orchestration

**When to use:** Complex workflows with conditional branching, sub-systems that themselves have orchestrators, large-scale production systems.

**Structure:**
```
User → Master Orchestrator
           ├── Sub-Orchestrator A → [Specialists A1, A2]
           ├── Sub-Orchestrator B → [Specialists B1, B2, B3]
           └── Final Assembler
```

**Example:** A full marketing automation agent:
- Master Orchestrator: understands campaign goal, routes to subsystems
- Research Sub-Orchestrator: manages audience research, competitor analysis, trend detection
- Content Sub-Orchestrator: manages copy writing, image prompts, CTA generation
- Analytics Sub-Orchestrator: manages performance tracking, A/B test decisions
- Final Assembler: compiles full campaign package

**Key rules:**
- Sub-orchestrators only communicate with Master Orchestrator
- Specialists only communicate with their immediate sub-orchestrator
- Final assembler is a specialist, not another orchestrator

---

## Pattern 4: Pipeline (Sequential Chain)

**When to use:** Linear transformation workflows where each step MUST complete before the next can begin.

**Structure:**
```
Input → Step 1 → Step 2 → Step 3 → Step 4 → Output
```

**Example:** Document processing pipeline:
- Extractor: parses raw document
- Normalizer: standardizes format
- Analyzer: extracts insights
- Formatter: produces final report

**Key rules:**
- Each step must validate its output before passing to the next
- Include checkpoints for human review if needed
- Pipeline stages can run in isolation for debugging

---

## Pattern 5: Fan-Out / Fan-In (Parallel)

**When to use:** Same task needs to run on multiple inputs simultaneously, or multiple specialists analyze the same input from different angles.

**Structure:**
```
Input → Splitter → [Worker 1] ↘
                → [Worker 2]  → Aggregator → Output
                → [Worker 3] ↗
```

**Example:** Multi-platform content adaptation:
- Splitter: takes one piece of content
- Worker 1: adapts for LinkedIn
- Worker 2: adapts for Twitter/X
- Worker 3: adapts for Instagram
- Aggregator: packages all versions together

---

## Pattern 6: Critic-Reviser Loop

**When to use:** Quality-critical outputs where iteration is needed, self-improving agents.

**Structure:**
```
Task → Generator → Output
          ↑            ↓
          └── Critic ←─┘
          (loop N times or until quality threshold met)
```

**Example:** High-quality copywriting agent:
- Generator: writes first draft
- Critic: scores draft against criteria (clarity, CRO, tone)
- If score < threshold: Generator revises
- Loop max 3 times, then output best version

**Key rules:**
- Critic must use explicit scoring criteria, not vague "make it better"
- Set maximum iteration limit (3-5) to prevent infinite loops
- Always output even if threshold not met (with quality score attached)

---

## Combining Patterns

Real production agents combine patterns. Example of a "Big Agent" using multiple patterns:

```
User → Master Orchestrator (Pattern 2)
          ├── Research Pipeline (Pattern 4)
          │     └── [Scraper → Parser → Summarizer]
          ├── Content Generation (Pattern 6)
          │     └── [Writer ↔ Critic × 3]
          ├── Multi-Platform Adaptation (Pattern 5)
          │     └── [LinkedIn → Twitter → Instagram]
          └── Quality Gate (Pattern 6 variant)
                └── [Final Reviewer → Publish/Revise]
```

This is what a truly "grande e potente" agent looks like.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
