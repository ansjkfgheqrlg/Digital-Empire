# 🔧 09 — OPERATIONS

> **Livello:** L1 · **Priorità:** TRASVERSALE · **Stato:** parziale (ruflo installato, swarm non inizializzato)
> Dossier completo: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §OPERATIONS

## Missione

Il runtime dell'intera holding: coordina gli swarm, gestisce i costi, programma
le esecuzioni, attribuisce i costi per ecosistema/agente. È il guardiano del budget.
**Nessun workflow va in produzione senza passare per il cost guard di OPERATIONS.**

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Swarm Engine | Ruflo: topologie swarm, hive-mind consensus, agent_spawn | `Reparti/Swarm/` |
| L2.2 | Budget Guard | cost-attribution per agente, alert 70%, blocco pre-sforo | `Reparti/Budget-Guard/` |
| L2.3 | Scheduling | run schedulate, cron, trigger asincroni | `Reparti/Scheduling/` |
| L2.4 | Storage | gestione artefatti, render queue, pulizia periodica | `Reparti/Storage/` |

## Strumenti chiave

| Tool | Funzione | Stato |
|---|---|---|
| `ruflo@3.10.13` | orchestrazione swarm, hive-mind, AgentDB | installato globalmente |
| `scripts/empire-sync.ps1` | sync bidirezionale Max↔Gael | ATTIVO |
| `verify-empire.sh` (da creare) | gate struttura holding | da forgiare (P0) |
| `empire-swarm` skill (da creare) | lancia swarm per qualsiasi task | da forgiare (P0) |
| `budget-guard` skill (da creare) | blocca spesa pre-sforo | da forgiare (P0) |
| `cost-ledger` skill (da creare) | ledger costi per agente | da forgiare (P0) |

## Topologie swarm standard (da `07-BACKBONE-RUFLO-SKILLS.md`)

| Topologia | Quando usarla |
|---|---|
| `hierarchical` | default — coordinator + workers (un team per workflow) |
| `parallel` | fan-out su reparti disgiunti (build F1 in parallelo) |
| `pipeline` | output di A è input di B (workflow sequenziali) |
| `mesh` | tutti comunicano con tutti (decisioni Board) |

## Come si collega al Backbone

- **BUS:** riceve richieste di run da tutti; ottimizza routing e scheduling
- **BRAIN:** legge AgentDB per routing Thompson Sampling; scrive metriche performance
- **COORDINATION:** è il gestore del Coordination Fabric (Ruflo)
- **COO:** supervisione C-Suite diretta

## Pending F2

- `ruflo init` nella root `company/` (o root DE) — task 2.1
- Daemon Ruflo + memory init — task 2.1
- Bus handoff queue — task 2.3
- AgentDB namespace per ecosistema — task 2.4

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` · Aggiornato: 2026-06-11*
