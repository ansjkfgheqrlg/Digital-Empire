# 🔀 COORDINATION — Ruflo (Fabric di coordinamento)

> **Backbone component.** Ruflo è il motore di coordinamento di EMPIRE OS.
> `ruflo@3.10.13` installato globalmente su Mac di Max. Su PC di Gael: da verificare.

## Funzione

```
Ruflo = COORDINA (stato, memoria, routing, swarm, consensus)
Claude Code = ESEGUE (codice, file, contenuti, comandi)
```

## Capacità attive

| Funzione | Tool Ruflo | Stato |
|---|---|---|
| Coordinamento ecosistemi | `swarm_init`, `coordination_orchestrate` | ruflo installato |
| Decisioni cross (Board) | `hive-mind_init/propose/vote/consensus` (raft) | da init |
| Cervello | `memory_store/search` (AgentDB HNSW) | da init |
| Apprendimento | `neural_train`, `reasoningbank-*`, `autopilot_*` | da costruire F8 |
| Agenti reali | `agent_spawn`, `managed_agent_*` | da usare in F8 |
| Sicurezza | `aidefence_scan/is_safe/has_pii` | disponibile |
| Workflow dinamici | `task_orchestrate`, `workflow_create/execute` | disponibile |
| Routing costi | 3-tier (WASM/Haiku/Sonnet-Opus) + Thompson Sampling | disponibile |

## Setup da completare in F2 (task 2.1)

```powershell
# Nella root di Digital Empire (o company/):
ruflo init
ruflo daemon start
ruflo memory init
ruflo memory init --namespace agency
# ... (tutti i namespace ecosistema)
```

> ⚠️ `ruflo init` è per-cartella. Ruflo globale (npm -g) ≠ ruflo init per-progetto.
> Ogni progetto dove si usa ruflo deve fare il proprio `ruflo init`.

## Topologie swarm standard

| Topologia | Uso in DE |
|---|---|
| `hierarchical` | default — coordinator + workers per team |
| `parallel` | fan-out reparti disgiunti (build fasi parallele) |
| `pipeline` | workflow sequenziali (lancio T-30→T+7) |
| `mesh` | Board consensus |

## Stato: ruflo installato globalmente; init EMPIRE OS da fare (F2, task 2.1)
