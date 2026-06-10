---
name: memory-checkpoint-skill
description: 'Active memory management skill for Empire Studio. Creates safe-named checkpoints, decisions, updates all memory categories after every action. Used by all agents + Memory Management Department.'
---
# memory-checkpoint-skill

**Purpose:** Enforce P10 two-layer memory. Auto-generate CP-XXX-...md with exact format, update INDEX, projects-state etc. Prevent bad filenames.

**Scripts:** (wraps /scripts/memory_manager.py ) scripts/log_checkpoint.py , scripts/audit_memory.py

**Templates:** checkpoint-template.md

**Principles:** Update after EVERY action. Safe filenames (no (), :, +). Full headers with trace/phase/strategy.

**Rules:** Always use memory_manager.py . For 4th dept: special projects-state/ subdir.

**Integration:** Called by every agent (conductor, strategy, workflow-deep-analyzer, etc.). Audited by memory-auditor-agent.

**Version:** v1.0

**Trace:** "full memory ecosystem (checkpoints/decisions/... with agents that actively manage it)"
