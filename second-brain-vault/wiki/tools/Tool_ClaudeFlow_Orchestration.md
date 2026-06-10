---
Type: TOOL
Status: Active
Tags: #ai #orchestration #multi-agent #skills #claude-code #ruflo
Created: 2026-05-29
Last updated: 2026-05-30
---

# Ruflo (ex Claude-Flow V3) — Multi-Agent Orchestration Layer

## Overview
Ruflo (ex claude-flow) è un orchestration layer open-source creato da ruvnet. Versione attuale: **3.7.0-alpha.8** (6,000+ commit). Coordina più agenti AI in parallelo sopra Claude Code / OpenAI Codex CLI con memoria vettoriale persistente, swarm, federation e self-learning. **22M+ download ecosistema, 115k clone in 14 giorni.**

## Regola fondamentale (critica)

```
Ruflo = COORDINA   (traccia stato, memoria, routing)
Claude Code = ESEGUE  (scrive codice, crea file, comandi shell)
```
Ruflo non esegue nulla da solo. È il "sistema nervoso" che coordina agenti che poi lavorano in parallelo.

## Architettura a 3 strati

```
User → Ruflo CLI/MCP → Router → Swarm → Agenti → Memory → LLM
                     ↑                         ↓
                     └──── Learning Loop ←──────┘
```

| Strato | Ruolo | Tecnologia |
|--------|-------|-----------|
| **Ruflo CLI/MCP** | Orchestratore, traccia stato, coordina | Node.js, 314 MCP tools |
| **Claude Code / Codex** | Esecutore — scrive codice, comandi | Claude Sonnet/Opus/Haiku |
| **AgentDB + HNSW** | Memoria vettoriale persistente cross-sessione | Rust engine, HNSW index |
| **Skills library** | 100+ SKILL.md per dominio | Markdown-based prompts |

## Numeri reali (dal zip analizzato)

| Feature | Numero |
|---------|--------|
| MCP tools | **314** |
| Agent types | **100+** (60+ ruoli definiti) |
| CLI commands | **26** comandi, **140+ subcomandi** |
| Hooks | **27 hooks** + **12 background workers** |
| Plugin marketplace | **33 plugin nativi Claude Code** + 21 npm plugin |
| Topologie swarm | 4 (hierarchical, mesh, ring, adaptive) |
| Provider LLM | Claude, GPT, Gemini, Cohere, Ollama |

## 3-Tier Model Routing (ADR-026) — risparmio di costo

| Tier | Handler | Latency | Costo | Quando |
|------|---------|---------|-------|--------|
| **1** | Agent Booster (WASM) | <1ms | **$0** | Transform semplici: var→const, add types, async/await |
| **2** | Haiku | ~500ms | $0.0002 | Task semplici (<30% complessità) |
| **3** | Sonnet/Opus | 2-5s | $0.003-0.015 | Ragionamento complesso, architettura, sicurezza |

Dal v3.7: **Thompson Sampling** — il router impara quale tier usare basandosi sui risultati passati. Si auto-corregge dopo ~50 outcomes senza configurazione manuale.

## Memory System (AgentDB / HNSW)

- **150x-12,500x** più veloce della ricerca brute force
- Persistente cross-sessione (non si resetta tra conversazioni)
- Recupero semantico: "come ho risolto X la settimana scorsa?" → risposta immediata
- Punteggio: >0.7 = usa il pattern, 0.5-0.7 = adatta, <0.5 = nuova soluzione

```bash
# Workflow tipo
memory_search(query="task keywords")     # impara dai pattern passati
swarm_init(topology="hierarchical")      # coordinamento (istantaneo)
# ... Claude Code fa il lavoro reale ...
memory_store(key="pattern", namespace="patterns")  # ricorda per dopo
```

## Self-Learning (SONA + ReasoningBank)

- **SONA neural patterns** — apprende dai successi passati
- **ReasoningBank** — bank di ragionamenti riutilizzabili
- **Trajectory learning** — ogni run completo diventa training data
- **Self-consistency orchestrator** — vota tra N soluzioni per accuracy +5-15pp

## Topologie Swarm

| Topologia | Caso d'uso | Default |
|-----------|-----------|---------|
| `hierarchical` | Team coordinato, anti-drift | ✅ preferita |
| `mesh` | Agenti peer-to-peer | parallel scraping |
| `ring` | Processing sequenziale | pipeline email |
| `adaptive` | Switch dinamico | produzione |

## Agent Federation — "Slack per Agenti"

Agenti su macchine/org diverse si coordinano in sicurezza:
- Zero-trust: mTLS + ed25519, niente API key condivisi
- PII stripping automatico prima di ogni messaggio in uscita
- Trust scoring comportamentale (formula: 0.4×success + 0.2×uptime + 0.2×threat + 0.2×integrity)
- Compliance HIPAA/SOC2/GDPR built-in

## Percorsi di installazione

| Path | Cosa dà | Quando usarlo |
|------|---------|--------------|
| **Plugin** (`/plugin install ruflo-core@ruflo`) | Solo slash commands | Provare singole funzioni |
| **Full CLI** (`npx ruflo@latest init`) | Tutto — MCP server, hooks, daemon, 98 agenti | Produzione |

### Stato installazione locale (macchina Max) — 2026-05-30

- **Installato in GLOBALE**: `npm install -g ruflo` → `ruflo@3.10.13`. Comando `ruflo` ora su PATH (`C:\Users\Utente\AppData\Roaming\npm\ruflo.ps1`), disponibile da qualsiasi cartella/progetto.
- **Distinzione chiave**: la copia in [orchestration/vendor/ruflo/](../../../SKILL%20&%20Agenti/Ecosistema%20-%20Content%20Factory/orchestration/vendor/ruflo/) (snapshot sorgente ~6800 file, v3.10.10) è **vendoring per archivio/riproducibilità**, NON un'installazione. Era inerte: niente comando, e i suoi `.claude/agents/` (sottocartella annidata) non vengono caricati da Claude Code, che scansiona solo `.claude/` del progetto corrente e quello globale `~/.claude/`.
- **Prossimo step per usarlo in un progetto**: `ruflo init` dentro quella cartella (registra MCP server, hooks, daemon, agenti). L'install globale dà solo il comando, non wira il runtime nei singoli progetti.

## UI e Tool Web

- **flo.ruv.io** — Web UI multi-modello con ~210 tool MCP, WASM gallery offline
- **goal.ruv.io** — Goal Planner: scrivi un obiettivo in italiano → GOAP A* lo decompone in task → agenti eseguono

## 33 Plugin disponibili (categorie)

- **Core**: ruflo-core, ruflo-swarm, ruflo-autopilot, ruflo-loop-workers, ruflo-workflows, ruflo-federation
- **Memory**: ruflo-agentdb, ruflo-rag-memory, ruflo-rvf, ruflo-ruvector, ruflo-knowledge-graph
- **Intelligence**: ruflo-intelligence, ruflo-graph-intelligence, ruflo-daa, ruflo-ruvllm, ruflo-goals
- **Code Quality**: ruflo-testgen, ruflo-browser, ruflo-jujutsu, ruflo-docs
- **Security**: ruflo-security-audit, ruflo-aidefence
- **Architecture**: ruflo-adr, ruflo-ddd, ruflo-sparc
- **DevOps**: ruflo-migrations, ruflo-observability, ruflo-cost-tracker
- **Domain**: ruflo-iot-cognitum, ruflo-neural-trader, ruflo-market-data

## Skill estratte e installate in Digital Empire (2026-05-29)

Installate in `~/.claude/skills/`:
`sparc-methodology`, `swarm-orchestration`, `memory-management`, `verification-quality`, `github-automation`, `pair-programming`, `workflow-automation`, `hooks-automation`, `agent-specification`, `agent-architecture`, `agent-researcher`, `agent-planner`, `agent-reviewer`, `agent-tester`, `agent-coder`

## Connessioni
- [[Exponium_Outreach_Platform]] — applica swarm per scrapers paralleli (Cap.6+)
- [[SPARC_Methodology]] — metodologia estratta da ruflo
- [[AgentDB_Memory_System]] — memory system per il Second Brain
- [[Swarm_Orchestration_Pattern]] — topologie per team multipli
