---
name: memory-management
description: >
  Pattern storage and retrieval system for building persistent knowledge across sessions.
  Store successful solutions, approaches, and patterns after each task. Retrieve them before
  starting similar tasks. Implements the AgentDB/HNSW concept from claude-flow adapted for
  Claude Code's memory system and wiki-based Second Brain.
  Use when: storing a solution that worked, searching for past patterns, building knowledge base.
trigger: "after completing a significant task or before starting work similar to past work"
skip: "ephemeral one-off tasks with no reuse value"
---

# Memory Management Pattern

## Core Principle
**Before starting any task**: search memory for similar past solutions.
**After completing any task**: store the pattern for future retrieval.

This is the foundation of the Second Brain (Cap.9-10 of Exponium).

## The Memory Cycle

```
1. SEARCH  → "have I solved something similar before?"
2. APPLY   → "use that pattern as starting point"
3. EXECUTE → "do the work"
4. STORE   → "save what worked for next time"
```

## How to Implement in Claude Code

### Before a Task (SEARCH)
Check:
1. GIORNATA.md — what was done in recent sessions
2. wiki/ pages — documented solutions and patterns
3. CLAUDE.md — project-specific rules

Pattern to apply:
- If similarity score is HIGH (same problem): reuse solution directly
- If similarity score is MEDIUM (similar problem): adapt and adjust
- If no match: proceed, then store after completion

### After a Task (STORE)
Document in GIORNATA.md:
```markdown
**Pattern discovered:**
- Problem: [what problem was being solved]
- Solution: [the approach that worked]
- Key code: [critical snippet or function signature]
- Gotchas: [what to avoid next time]
- Reuse when: [what future scenario triggers this pattern]
```

### Pattern Namespaces (mirrors AgentDB namespaces)

| Namespace | What to store |
|-----------|--------------|
| `scraper-patterns` | Working scraper code, anti-detection tricks, selectors |
| `email-patterns` | Email templates, subject lines, sequences that converted |
| `db-patterns` | SQLite schemas, query patterns, migration approaches |
| `ui-patterns` | React components, Tailwind patterns, layout solutions |
| `ai-patterns` | Prompts that work, AI chain patterns, Claude API usage |
| `error-patterns` | Common errors + their fixes |
| `canva-patterns` | Canva automation selectors, flows that work (Gael's namespace) |

## For Cap.9-10 (Second Brain Implementation)

The wiki itself IS the memory system:
```
second-brain/
├── patterns/
│   ├── scraper-solutions.md    ← every working scraper pattern
│   ├── email-templates.md      ← email sequences that converted
│   ├── ai-prompts.md           ← prompts that work
│   └── error-fixes.md          ← recurring errors + solutions
├── decisions/
│   └── architecture-log.md     ← why certain choices were made
└── index.md                    ← searchable index of all patterns
```

## HNSW Vector Search (future — Cap.9)
When Second Brain is built, implement semantic search:
```python
# patterns stored with embeddings for semantic retrieval
db.store(
    key="google-maps-scraper-v2",
    value="Solution: use requests + BeautifulSoup fallback when Playwright is blocked",
    namespace="scraper-patterns",
    embedding=embed(content)  # allows semantic search
)

# query: "how do I scrape maps when playwright is blocked?"
results = db.search(query, namespace="scraper-patterns", top_k=3)
```

## Anti-patterns
- **Storing without context**: saving "it worked" without HOW → useless later
- **Not searching before starting**: reinventing solved problems every session
- **Too granular**: storing every tiny code snippet → noise overwhelms signal
- **Too generic**: "fixed the bug" → impossible to retrieve later
