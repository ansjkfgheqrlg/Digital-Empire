# complexity-matrix

> Source: File system (`SKILL & Agenti\agent-factory\skills\agent-architect\references\complexity-matrix.md`)
> Collected: 2026-05-06
> Published: Unknown

# Complexity Matrix — Choosing the Right Architecture

Use this matrix to determine the correct architecture type from a set of requirements.

## Decision Dimensions

Score each dimension 1-3, then sum.

| Dimension | 1 (Simple) | 2 (Medium) | 3 (Complex) |
|---|---|---|---|
| **Number of distinct tasks** | 1-2 | 3-5 | 6+ |
| **Domain expertise required** | 1 domain | 2-3 domains | 4+ domains |
| **Parallel execution needed** | No | Some | Extensive |
| **External integrations** | None | 1-2 APIs | 3+ APIs/services |
| **Conditional branching** | None | Simple if/else | Complex routing |
| **Output complexity** | Single item | Multi-part | Full system |
| **Quality iteration needed** | No | Maybe | Yes, always |

## Scoring Key

| Total Score | Architecture | Plugin Pattern |
|---|---|---|
| 7-10 | Single Agent | 1 `.md` file |
| 11-14 | Specialist + Orchestrator | 3-5 `.md` files |
| 15-18 | Multi-Layer Orchestration | 6-10 `.md` files |
| 19-21 | Full Swarm | 10+ `.md` files |

## Model Selection Rules

| Task Type | Recommended Model | Reason |
|---|---|---|
| Deep reasoning, judgment calls, complex analysis | `opus` | Best reasoning |
| Balanced tasks, writing, coding | `sonnet` | Cost-performance balance |
| Parsing, classification, formatting, routing | `haiku` | Fast and cheap |
| Research + synthesis | `sonnet` or `opus` | Depends on depth |
| Final assembly / formatting | `haiku` | Speed matters here |

## Tool Selection Rules

| Task | Required Tools |
|---|---|
| Reading files | `Read`, `Glob` |
| Searching code/content | `Grep` |
| Writing/creating files | `Write` |
| Running scripts/commands | `Bash` |
| External web search | `WebSearch` |
| Fetching URLs | `WebFetch` |
| Browsing/scraping | `WebSearch`, `WebFetch` |
| Full autonomy (orchestrator) | all tools |

**Always apply least-privilege:** Give agents only the tools they actually need.

## Red Flags in Architecture Design

Watch for these anti-patterns:

- **God agent:** One agent does everything. Split it.
- **Chatty agents:** Agents exchanging 10+ messages. Restructure data flow.
- **Orphan agents:** Agent in architecture with no clear input source.
- **Missing failure modes:** No plan for when APIs fail, data is empty, or output is invalid.
- **All opus:** Using opus everywhere. Expensive and unnecessary for simple tasks.
- **Circular dependencies:** Agent A needs B's output, B needs A's output. Redesign.
