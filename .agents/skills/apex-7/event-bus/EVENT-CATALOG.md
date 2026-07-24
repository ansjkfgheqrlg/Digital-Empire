# EVENT BUS — Catalogo Completo Eventi

> Il sistema comunica attraverso eventi. **Nessun agente chiama un altro direttamente.** Tutto passa per l'Event Bus.

---

## Formato Visualizzazione

Quando esegui come APEX-7, mostra gli eventi all'utente in questo formato:

```
📡 EVENT: {nome_evento} | FROM: {agente} | TO: {agente/i} | PRIORITY: {P0-P3}
```

---

## Priorità e Retry Policy

| Priorità | Significato | Retry | Max Retry |
|---|---|---|---|
| **P0** | CRITICO — Richiede attenzione immediata | Ogni 1s | 10 |
| **P1** | ALTO — Blocca il flusso se non gestito | Ogni 5s | 5 |
| **P2** | NORMALE — Flusso standard | Ogni 30s | 3 |
| **P3** | BASSO — Background, droppabile | Ogni 60s | 1 poi DROP |

---

## TASK LIFECYCLE EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `task.created` | P2 | ORCHESTRATOR | PLANNER, MEMORY | Nuovo task ricevuto dall'utente |
| `task.decomposed` | P2 | PLANNER | WRITER, ANALYST, MEMORY | Piano creato e task decomposto |
| `task.started` | P2 | ORCHESTRATOR | ALL | Esecuzione task iniziata |
| `task.completed` | P1 | ANY | ORCHESTRATOR, MEMORY | Task completato con successo |
| `task.failed` | P0 | ANY | ORCHESTRATOR, META | Task fallito |
| `task.restarted` | P1 | ORCHESTRATOR | PLANNER | Task riavviato con nuovo piano |

---

## DRAFT LIFECYCLE EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `draft.created` | P2 | WRITER | CRITIC, MEMORY | Nuovo draft generato |
| `draft.refined` | P2 | REFINER | CRITIC, MEMORY | Draft migliorato dopo critica |
| `draft.approved` | P1 | CRITIC | GATE_AGENT, MEMORY | Draft approvato da CRITIC |

---

## CRITIQUE EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `critique.completed` | P1 | CRITIC | ORCHESTRATOR, MEMORY | Valutazione completata |
| `critique.pass` | P1 | CRITIC | GATE_AGENT | Verdict = PASS |
| `critique.refine` | P1 | CRITIC | REFINER | Verdict = REFINE |
| `critique.restart` | P0 | CRITIC | ORCHESTRATOR, META | Verdict = RESTART |

---

## GATE EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `gate.check.requested` | P1 | ORCHESTRATOR | GATE_AGENT | Richiesta gate check |
| `gate.passed` | P1 | GATE_AGENT | ORCHESTRATOR, MEMORY | Gate superato |
| `gate.failed` | P1 | GATE_AGENT | REFINER, ORCHESTRATOR | Gate fallito (1a/2a volta) |
| `gate.escalated` | P0 | GATE_AGENT | META_AGENT, ORCHESTRATOR | Gate fallito 3a volta |

---

## ANALYSIS EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `analysis.completed` | P2 | ANALYST | WRITER, MEMORY | Analisi completata, Context Package pronto |

---

## REFINEMENT EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `refinement.completed` | P2 | REFINER | CRITIC, MEMORY | Refinement completato |

---

## MEMORY EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `memory.updated` | P3 | MEMORY | META_AGENT | Memoria aggiornata |
| `memory.pattern.found` | P3 | META_AGENT | STRATEGY_STORE | Pattern rilevato |
| `memory.compressed` | P3 | MEMORY | META_AGENT | Compressione eseguita |

---

## SYSTEM EVENTS

| Evento | Priorità | FROM | TO | Descrizione |
|---|---|---|---|---|
| `system.cycle.started` | P2 | ORCHESTRATOR | ALL | Nuovo ciclo iniziato |
| `system.cycle.ended` | P2 | ORCHESTRATOR | META_AGENT | Ciclo completato |
| `meta.activated` | P1 | ORCHESTRATOR | META_AGENT | META AGENT attivato |
| `meta.analysis.completed` | P1 | META_AGENT | ORCHESTRATOR | Meta analisi completata |
| `meta.intervention` | P0 | META_AGENT | ORCHESTRATOR | Intervento deciso |
| `system.evolved` | P2 | META_AGENT | ALL, MEMORY | Sistema evoluto |
| `agent.spawned` | P3 | META_AGENT | ORCHESTRATOR | Nuovo agente spawnato |
| `agent.degraded` | P0 | META_AGENT | ORCHESTRATOR | Agente in stato DEGRADED |
| `system.output.final` | P1 | ORCHESTRATOR | USER | Output finale presentato |

---

## Bus Routing Rules

```
1. Eventi P0: consegna immediata, coda prioritaria
2. Eventi P1: consegna entro 5s
3. Eventi P2: consegna entro 30s
4. Eventi P3: consegna best-effort

5. ORCHESTRATOR è l'unico consumer che può reagire a tutti gli eventi
6. META AGENT riceve copia di tutti gli eventi P0 e P1
7. Eventi di memoria (P3) sono fire-and-forget per gli agenti,
   ma META AGENT li processa in batch
```
