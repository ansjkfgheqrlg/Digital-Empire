---
Type: PROJECT
Status: Active
Tags: #exponium #aion-group #content-factory #architettura #holding-agenti #riferimento
Created: 2026-06-08
Last updated: 2026-06-08
---

# Exponium Content Factory — Analisi Architettonica Completa

## Overview
Azienda di agenti AI (holding **AION GROUP**) costruita per il lancio di Exponium (software algo 16 livelli). Struttura enterprise a 6 livelli gerarchici, 6 ecosistemi, backbone condiviso, 68 check automatici, produzione di massa parallela, auto-miglioramento. Scope: **solo contenuti per il lancio Exponium** — non fa nulla di generico.

Path fisico: `C:\Users\Utente\Desktop\qui tutto\Lavoro\Exponium\second-brain-exponium\Ecosistema - Content Factory`

## Gerarchia (6 livelli)

```
LX  Dipartimento Exponium (authority suprema, sopra tutti)
    Capi-Assoluti + Sentinelle-Exponium (compliance CONSOB obbligatoria)

L0  Board / C-Suite
    CEO=Conductor, COO, CTO, CMO, CRO, CFO
    Decisioni cross via hive-mind raft

L1  6 Ecosistemi (Business Unit indipendenti ma connesse)
    STUDIO · INTELLIGENCE · GROWTH · PLATFORM · FORGE · OPERATIONS

L2  Reparti / Direzioni (dentro ogni ecosistema)
    D1 Strategy, D2 Creative, D3 Operations, D4 Marketing,
    D5 QA, D6 Orchestration, D7 Research, D8 Engineering

L3  Workflow (team per flusso end-to-end)
L4  Funzioni (team per singola funzionalità)
L5  Agenti reali (worker running via claude-flow)
⊕   Guilds (comunità trasversali) + Sentinels (always-on)
```

### Regola strutturale fondamentale
**UN TEAM DI AGENTI PER OGNI SINGOLA FUNZIONALITÀ.** Ogni team ha: coordinator + worker agents, schema input/output rigoroso, acceptance criteria misurabili, escalation protocol, shared_state folder.

## Corporate Backbone (servizi condivisi)

| Componente | Funzione |
|---|---|
| **BUS** | Message bus 2 livelli (intra+inter ecosistema), handoff contract `{from, to, payload, acceptance_criteria}` |
| **BRAIN/AgentDB** | Memoria vettoriale HNSW 384-dim, causal graph, ReasoningBank (impara dagli errori) |
| **GOVERNANCE** | contradiction-analyzer Python, compliance gate CONSOB, policy, security (aidefence) |
| **IDENTITY-HR** | Registro unico tutti gli agenti (ruolo, costo, performance) |
| **OBSERVABILITY** | Metrics, neural_train, autopilot |
| **COORDINATION FABRIC** | Topologie: raft/byzantine/gossip/crdt/quorum |

## Pipeline UGC (flusso operativo)

```
D1  Brief + Budget Planner
D7  Research (trend, riferimenti) ← parallelo a D1
D6  Conductor → royal directives ai reparti
D2  T2.5 Soul ID → T2.1 Image 4K → T2.3 Motion → T2.4 Montaggio
D3  Render Queue + Cost Guard + Asset Storage ← durante D2
D4  Copy APSOC + caption + hook social
D5  QA gate (spec + brand + compliance CONSOB) ← OBBLIGATORIO
D8  Code custody ← trasversale
D6  Aggrega + consegna + ReasoningBank update
```

### Project state per ogni ordine
```
runtime/projects/<id>/
├── state.json        # fase, task, owner, status, budget
├── trace.jsonl       # log cronologico audit-proof
├── 01-brief/ 02-roadmap/ characters/ images/ clips/ motion/ final/
```

## Strato tecnico operativo

| Script | Funzione |
|---|---|
| `conductor.sh new "<brief>"` | Entry point — crea progetto, emette direttive |
| `dispatch.sh ugc <id>` | Esegue workflow UGC (reale o --dry) |
| `dispatch.sh ugc <id> --dry` | Stima costo senza spendere crediti |
| `swarm.sh ugc jobs.csv --parallel N --budget N` | Produzione di massa parallela |
| `verify.sh` | 68 check qualità (0 fail a regime) |
| `bootstrap.sh check` | Controlla ambiente e auto-ripara |
| `engines.sh` | Layer astrazione multi-motore (aggiunge nuovi motori senza toccare orchestrazione) |
| `wiki.sh context` | Carica index+log del second-brain |

## Skills installate

| Skill | Funzione | Stato |
|---|---|---|
| `exponium-context` | Second brain Exponium (prodotto, ICP, compliance, voice) | Attiva |
| `heygen-generate` | Avatar talking-head Marco (HeyGen) | Pronta, non connessa |
| `higgsfield-generate` | UGC/immagini/motion | Attiva |
| `higgsfield-soul-id` | Personaggio ricorrente (stessa identità su tutti i video) | Attiva |
| `higgsfield-marketplace-cards` | Card e-commerce | Attiva |
| `higgsfield-product-photoshoot` | Foto prodotto | Attiva |
| `context-engineering-advisor` | Ottimizzazione prompt (cross-funzionale) | Attiva |

## Stato build (2026-06-01)

| Build | Cosa | Stato |
|---|---|---|
| BUILD 1-4 | Fondamenta, orchestratore, MVP UGC, reparti supporto | ✅ COMPLETATI |
| BUILD 3 test | Primo video reale (2026-05-29): Soul→Img4K→Motion→final_ugc.mp4 (2MB, ~12 crediti) | ✅ FATTO |
| BUILD 5 | QA avanzato + lint | ⏳ |
| BUILD 6 | Self-improvement attivo | ⏳ |
| BUILD 7 | Editing pro, video t2v, product | ⏳ |

### Cosa manca ancora
- Prima produzione con budget reale allocato
- Riconnessione stabile Ruflo MCP
- Audio/TTS nel montaggio
- Auto-pubblicazione social (API Instagram/TikTok/YouTube)
- Dati reali per INTELLIGENCE (oggi usa conoscenza generica)
- Dashboard web visuale
- FORGE esecutiva autonoma

## Confronto con Digital Empire (cosa replicare, cosa aggiungere)

Exponium Content Factory è **mono-scopo** (solo lancio Exponium). Digital Empire ne ha bisogno di una versione **multi-scopo** e molto più grande perché include Agency, Info Products, SaaS, e la stessa produzione di workflow come prodotto.

| Ecosistema CF | Ruolo in DE | Δ aggiunto per DE |
|---|---|---|
| STUDIO | Creazione contenuti | Multi-brand, multi-cliente |
| GROWTH | Marketing + copy APSOC | Outreach agency, lead gen |
| INTELLIGENCE | Research e trend | Competitive intel per clienti |
| PLATFORM | Engineering | Produzione SaaS, Second Brain prodotto |
| FORGE | Crea nuovi team | Crea interi info products (corsi, ebook) |
| OPERATIONS | Runtime e massa | Gestione multi-progetto multi-cliente |
| ❌ assente | — | **CLIENT DELIVERY** (reparti CRO, delivery sprint) |
| ❌ assente | — | **SALES** (outreach, funnel, onboarding clienti) |
| ❌ assente | — | **PRODUCT** (info products: corsi, ebook, membership) |

## Pattern architettonici chiave (da replicare)

1. **Team canonico con schema fisso**: ogni team ha coordinator, agents con input/output espliciti, acceptance criteria, failure handling, shared_state
2. **Handoff contract**: ogni passaggio tra team è un messaggio strutturato con acceptance criteria
3. **Dry run mode**: ogni workflow ha una modalità stima-costo senza effetti reali
4. **Gate obbligatorio**: niente esce senza passare per il QA/compliance gate
5. **ReasoningBank**: ogni fallimento viene loggato e distillato in pattern per non ripetersi
6. **Skill come knowledge layer separato**: lo stesso skill è usabile da più agenti in più reparti
7. **Progressive disclosure nel SKILL.md**: kernel ≤500 righe, tutto il dettaglio in `references/`
8. **Invariant cardinali**: regole non negoziabili scritte esplicitamente nel SKILL.md (es. compliance prima di velocità)
9. **Cost guard**: agente dedicato al budget che blocca prima di sforare
10. **Sentinels always-on**: agenti di monitoraggio sempre accesi (costi, qualità, salute sistema)

## Connessioni
- [[Digital_Empire_6_Phase_Process]]
- [[Tool_ClaudeFlow_Orchestration]]
- [[Concept_Pivot_Implementazioni_AI]]
