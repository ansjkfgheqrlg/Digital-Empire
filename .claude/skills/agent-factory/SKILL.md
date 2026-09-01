---
name: agent-factory
description: "Pipeline di 4 skill per progettare, scrivere, costruire e validare agenti Claude Code professionali. Include agent-architect (blueprint), system-prompt-forge (system prompt), agent-builder (file .md), agent-quality-sentinel (audit e scoring)."
---

# Agent Factory

Pipeline di 4 skill collaborative per creare agenti Claude Code di qualita' professionale.

## Pipeline

```
[1] agent-architect       → Design the blueprint
        ↓
[2] system-prompt-forge   → Write elite system prompts
        ↓
[3] agent-builder         → Build plugin files
        ↓
[4] agent-quality-sentinel → Audit, score, and fix
```

## Quando usarla

USE THIS SKILL when the user wants to:
- Create a new Claude Code agent from scratch
- Design agent architecture with proper data flow and model assignments
- Write production-grade system prompts for agents
- Build agent .md files with proper frontmatter
- Audit and score existing agents for quality
- Fix agent triggering, structure, or prompt quality issues

## Sub-skills

Each sub-skill lives in `skills/` and can be invoked independently:

1. **agent-architect** — Defines agent map, data flow, model tier, tool matrix, failure modes
2. **system-prompt-forge** — Transforms blueprint into elite system prompts (CoT, ReAct, ToT, Critic-in-the-Loop)
3. **agent-builder** — Builds .md files, validates frontmatter, produces install instructions
4. **agent-quality-sentinel** — Multi-dimensional audit: structural validity, trigger quality, prompt depth, architecture coherence
