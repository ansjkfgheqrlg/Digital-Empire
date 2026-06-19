---
Type: SYNTHESIS
Status: Active
Tags: #claude-flow #exponium #applicazioni #mapping #strategic
Created: 2026-05-29
Last updated: 2026-05-29
---

# Claude-Flow → Exponium: Mapping Completo delle Applicazioni

## Overview
Analisi di come i 138 pattern di Claude-Flow V3 si mappano sui 3 prodotti Exponium.
Distingue: **implementazione immediata** vs **implementazione futura** vs **non applicabile**.

## Matrice di Applicazione

### Prodotto 1 — Outreach Platform

| Pattern Claude-Flow | Capitolo | Impatto | Quando |
|--------------------|---------|---------|--------|
| SPARC Methodology | Cap.1-7 | Alto | Ora — ogni sessione dev |
| verification-quality | Cap.2-4 | Alto | Ora — quality gate 95% |
| agent-specification | Cap.2A+ | Alto | Ora — spec prima del codice |
| agent-architecture | Cap.2A+ | Alto | Ora — schema DB prima della funzione |
| agent-coder patterns | Cap.2-7 | Alto | Ora — BaseScraper, SQLite context manager |
| agent-tester (pytest) | Cap.2+ | Medio | Ora — test per ogni scraper |
| Swarm parallel workers | Cap.6 | Alto | Cap.6 — 4 scrapers paralleli |
| memory-management | Cap.6+ | Medio | Cap.6 — storea pattern scraper riusciti |
| workflow-automation | Cap.7 | Alto | Cap.7 — daily scrape workflow |

### Prodotto 2 — Content Factory

| Pattern Claude-Flow | Capitolo | Impatto | Quando |
|--------------------|---------|---------|--------|
| agent-researcher | Canva-B | Alto | Ora per Gael — mapping UI sistematico |
| agent-specification | Canva-A+ | Alto | Ora per Gael — spec ogni flusso Canva |
| pair-programming | Canva-C+ | Medio | Gael può usare — build collaborativo |
| canva-patterns namespace | Canva-G | Alto | Dopo Cap.9 — storea selettori Canva |
| workflow-automation | Cap.8D-F | Alto | Max — pipeline AI copy + Canva |
| Swarm (Max+Gael pipeline) | Cap.8F | Medio | Cap.8F — integrazione finale |

### Prodotto 3 — Second Brain

| Pattern Claude-Flow | Capitolo | Impatto | Quando |
|--------------------|---------|---------|--------|
| AgentDB Memory System | Cap.9 | **Critico** | Cap.9 — questa IS l'architettura |
| HNSW Vector Search | Cap.9 | **Critico** | Cap.9 — semantic search sui pattern |
| memory-management skill | Cap.9-10 | Alto | Cap.9 — 7 namespace, store/search API |
| neural-training | Cap.10 | Medio | Cap.10 — pattern learning dal comportamento |
| hooks-automation | Cap.10 | Alto | Cap.10 — hooks di sessione automatici |
| agentdb-advanced | Cap.9 | Alto | Cap.9 — advanced DB patterns |
| agentdb-vector-search | Cap.9 | Alto | Cap.9 — HNSW implementation |

## Skills Installate Ora (effetto immediato)

```
sparc-methodology     → ogni sessione è ora strutturata in 5 fasi
agent-specification   → Max e Gael scrivono la spec PRIMA del codice
agent-architecture    → schema DB e firme funzioni PRIMA dell'implementazione
agent-coder           → pattern Python/TypeScript standard per Exponium
agent-tester          → ogni feature ha un test minimo
agent-reviewer        → code review sistematica prima di ogni commit
verification-quality  → 95% gate: mai ship di roba rotta
github-automation     → commit automatici a fine sessione
memory-management     → documenta soluzioni in GIORNATA.md
agent-researcher      → research sistematica all'inizio di ogni capitolo
agent-planner         → TodoWrite strutturato per ogni sessione
pair-programming      → Max/Gael possono lavorare in modo più collaborativo
workflow-automation   → pipeline daily outreach definita come workflow
hooks-automation      → session-start e session-end standardizzati
swarm-orchestration   → pronto per Cap.6 scrapers paralleli
```

## Miglioramento ai Piani Esistenti

### CLAUDE_CODE_SESSIONS.md — aggiornato con SPARC
Ogni capitolo ora inizia con blocco SPARC:
```
PRIMA DI SCRIVERE CODICE — segui SPARC:
[ ] Ph.1: scrivi la spec (cosa, perché, done-when)
[ ] Ph.2: pseudocode (logica in prosa, edge cases)
[ ] Ph.3: architettura (file, schemi, firme funzioni)
[ ] Ph.4: implementa (50 righe → test → 50 righe)
[ ] Ph.5: verifica (95% quality gate, poi commit)
```

### GAEL_TASKS.md — aggiornato con agent-researcher
Gael ora ha un checklist research sistematico per ogni task Canva:
- Identifica selettori CSS/attributi prima di scrivere codice Playwright
- Testa ogni interazione manualmente prima di automatizzare
- Documenta selettori in `canva_ui_map.md` per riuso

### MASTER_PLAN.md — Cap.9 aggiornato con AgentDB spec
Cap.9 ora ha l'architettura completa del memory system:
- `agentdb.py` con store/search API
- 7 namespace (scraper, email, db, ui, ai, error, canva)
- HNSW index con hnswlib
- search_cli.py per query da terminale

## Valore stimato

| Area | Prima | Dopo | Delta |
|------|-------|------|-------|
| Sessioni dev che producono codice funzionante al primo try | ~40% | ~75% | +35pp |
| Tempo perso a reinventare soluzioni già trovate | alto | basso | -60% |
| Codice committato con bug bloccanti | ~20% | ~5% | -75% |
| Pattern riusabili tra sessioni diverse | 0 | ∞ | +∞ |

## Connessioni
- [[Tool_ClaudeFlow_Orchestration]] — fonte di tutti i pattern
- [[SPARC_Methodology]] — metodologia principale estratta
- [[AgentDB_Memory_System]] — architettura Second Brain
- [[Swarm_Orchestration_Pattern]] — Cap.6+ scrapers paralleli
