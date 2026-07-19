# Reference Esterne — Fonti Primarie

> **Fonte:** Knowledge Pack 10-references + estrazioni da Ruflo, Content-Forge, Context-Engineering-Advisor, Skill-Creator.

## Fonti Primarie (Clonate/Installate)

### 1. Ruflo
**Path:** `projects/ruflo/`
**Tipo:** Framework swarm coordination
**Contenuto chiave:**
- Swarm topologies (hierarchical/mesh/pipeline)
- AgentDB + HNSW (ricerca semantica)
- SONA memory (short/long-term)
- Federation (zero-trust, mTLS, PII strip)
- MCP tools (~210)
- Hooks/workers (background learning)
- 100+ agenti di riferimento
- Plugin marketplace
- GOAP goal planner

**Estrazioni applicate:**
- PT01 (Conductor-with-Subagents)
- DT01 (Topology Selection)
- DT03 (Memory Strategy)
- P10 (Memory-first)

---

### 2. Content-Forge 2.0
**Path:** `projects/content-forge2.0/`
**Tipo:** Pipeline trasformazione contenuto
**Contenuto chiave:**
- 9-stage pipeline (Ingestion → Packaging)
- 25 agenti (conductor + families)
- MKD (Master Knowledge Document) always
- No-summary invariant (P03)
- Interactive scaffolding (P04)
- Optimizers O1-O5 (Stage 7)
- Self-improvement (Stage 10)
- failure-modes-log
- references/ con stages/patterns/processes/schemas
- scripts/ (Python atomizer, coverage, validators)
- evals/

**Estrazioni applicate:**
- PR02 (Content-Forge Pipeline)
- PT02 (Pipeline-Stages-with-Handoff)
- PT03 (Builder-Then-Optimizer)
- P03 (No-Summary-Expansion)

---

### 3. Context-Engineering-Advisor
**Path:** `projects/.agents/skills/context-engineering-advisor/SKILL.md`
**Tipo:** Skill per context management
**Contenuto chiave:**
- Context stuffing vs engineering
- Two-layer memory (short-term conversational + long-term persistent)
- Research→Plan→Reset→Implement cycle
- 5 diagnostic questions + falsification test
- Context Manifest template
- Ownership principle
- Just-in-time retrieval

**Estrazioni applicate:**
- P10 (Memory-first) — two-layer exact
- PR05 (Memory Lifecycle) — Research→Plan→Reset→Implement
- DT03 (Memory Strategy)

---

### 4. Skill-Creator
**Path:** `projects/content-forge2.0/references/external/skill-creator.md`
**Tipo:** Meta-skill per creazione skill
**Contenuto chiave:**
- SKILL.md anatomy (frontmatter + ≤500 lines + progressive disclosure)
- Bundled resources (scripts/references/assets)
- Test cases + evals.json + benchmark viewer
- Iteration loop
- Description optimization (trigger design)
- Grader/comparator/analyzer agents
- Packaging (.skill)
- Human review + quantitative
- Blind comparison optional

**Estrazioni applicate:**
- PR07 (Packaging & Release)
- PT08 (Meta-Recursive-Skill)
- P15 (Trigger Design as Product)
- evals/ structure

---

## Fonti Esterne (Documentazione)

### Brooks — "The Mythical Man-Month"
**Concetto:** "The planning part of a software project is the most critical."
**Applicazione:** P01 (Iterative Planning), PR01 (Iterative Plan Creation)

### Hickey — "Clean Code"
**Concetto:** "Readable code is maintainable code."
**Applicazione:** P05 (Markdown+Python), P08 (Depth over Breadth)

### Fowler — "Patterns of Enterprise Application Architecture"
**Concetto:** Repository pattern, Unit of Work, Data Mapper.
**Applicazione:** PT05 (Canonical Files per Target), struttura agenti

### Matuschka — "Building LLM-Powered Applications"
**Concetto:** Context windows, token management, retrieval-augmented generation.
**Applicazione:** P02 (Progressive Disclosure), P10 (Memory-first)

### Anthropic — Claude Documentation
**Concetto:** System prompts, tool use, multi-turn conversations.
**Applicazione:** SKILL.md structure, agent system-prompt.md format

---

## Reference Integrity Check

### Verificato
- [x] Ruflo cloned and accessible
- [x] Content-Forge 2.0 cloned and accessible
- [x] Context-Engineering-Advisor installed
- [x] Skill-Creator reference available
- [x] All extractions traceable (P12)

### Da Verificare (se necessario)
- [ ] Ruflo version (last commit date)
- [ ] Content-Forge version (last commit date)
- [ ] Context-Engineering-Advisor version
- [ ] Skill-Creator version

---

## Connessioni
- **Principi correlati:** P02 (progressive disclosure), P05 (Markdown+Python), P10 (memory-first), P12 (traceability)
- **Pattern correlati:** PT01 (conductor), PT02 (pipeline), PT09 (multi-source)
- **Processi correlati:** PR02 (Content-Forge pipeline), PR05 (Memory lifecycle), PR07 (Packaging)
- **Agenti:** Tutti usano queste reference come fonte di verità
