# 🧬 SISTEMA NERVOSO — Integrazione Ruflo (clonato 21/07 in `05-SKILLS/ruflo`)
> Ruflo = agent meta-harness: da agli agenti tools, memoria, loop, swarm, controlli. Nel workshop è il L1 (nervous system) tra agenti (L3) e memoria (L0).

## 1. Mappatura concetti Ruflo → Digital Empire

| Concetto Ruflo | Dove vive nel workshop |
|---|---|
| Swarm (hierarchical, queen-led) | `chief-forge` = queen/orchestratore; reparti = worker swarm (swarm.estate.yaml) |
| Hooks (17 hooks + background workers) | hook pre/post task → `memory_manager.py` (vedi §3); EOD worker → WF-MEM-EOD |
| Memory AgentDB/HNSW | cache semantica opzionale; **source of truth = `00-MEMORY/` file-based** (umano-leggibile, diffabile) |
| Guidance/control plane | gates P5 + evals degli agenti + zero-stub validator |
| Router/provider | non richiesto questa settimana (esecuzione umana+Claude); pronto per scaling |
| `npx ruflo init` | comando di attivazione quando l'ambiente lo consente (Node ≥ 20) |

## 2. Attivazione (quando possibile)
```bash
# Prerequisito: Node.js >= 20
npx ruflo init --namespace estate-2026
# poi caricare la topologia:
npx ruflo swarm spawn --config 06-NERVOUS-SYSTEM/swarm.estate.yaml
```
**Modalità degradata (default ora)**: senza npx, l'orchestrazione gira da file: `03-WORKFLOWS/workflows.yaml` + loop WF-MASTER + hook memoria manuali. Nulla si blocca (ADR-EST-008 fallback file-based).

## 3. Hook contract (da registrare in ruflo all'attivazione)
| Hook | Trigger | Azione |
|---|---|---|
| pre_task | inizio qualsiasi WF | carica `MEMORY-INDEX.md` + decisioni ATTIVE nel contesto dell'agente |
| post_task | chiusura task | `python3 00-MEMORY/memory_manager.py checkpoint --task <wf> --note "<esito>"` |
| on_failure | eccezione/fallimento | `... error --wf <wf> --note "<errore>"` + attiva fallback ladder (P5) |
| on_metric | KPI prodotto | `... metric --name <k> --value <v>` |
| eod (worker) | daily 19:00 | WF-MEM-EOD (metriche, dashboard, CP) |
| on_decision | veto scaduto / decisione presa | aggiorna stato DEC-EST-* e notifica WF-MASTER |
| session_end (learning) | fine sessione | pattern candidati → `reasoning-bank` (auto-apprendimento Ruflo → ReasoningBank) |

## 4. SONA/memory sync
La memoria vettoriale di ruflo (AgentDB) indicizza gli atomi di `00-MEMORY/` per retrieval semantico (`memory_store`/`memory_search`). Sync: ad ogni atomo nuovo → embed + upsert. Fallback: `memory_manager.py search` (full-text) già attivo.

## 5. Vincoli rispettati
- Un solo swarm pesante alla volta → `max_parallel_heavy: 1` in swarm.estate.yaml (CP-20260711-002).
- Secrets: ruflo non riceve mai chiavi nei prompt; solo variabili `.env` locali (regola dossier 4).
- ReasoningBank: i pattern appresi dal learning loop di ruflo vengono persistiti come atomi `RB-*` (sopravvivono alle sessioni).
