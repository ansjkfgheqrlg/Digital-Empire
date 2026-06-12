> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-QUEUE

# L3 — WF-QUEUE (Render/Job Queue con Backpressure)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** RUNTIME
**Coordinator:** `ops-swarm-marshal` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-QUEUE implementa la render queue di EMPIRE OS: quando i worker sono saturi,
i job in attesa non vengono droppati né lanciati comunque — entrano in coda con
priorità, concorrenza limitata e backpressure. Pattern di riferimento: render queue
CF (Content Factory Exponium), portato in DE.

Differenza rispetto a WF-SWARM-RUN: WF-SWARM-RUN esegue un batch singolo dal
principio alla fine; WF-QUEUE gestisce il flusso continuo di job eterogenei da
ecosistemi diversi con contesa sulle risorse di esecuzione.

## Input / Output

**Input (job in ingresso):**
```json
{
  "job_id": "J-YYYYMMDD-NNN",
  "tipo": "content|build|outreach|ingest|...",
  "priorita": 1,
  "payload": {},
  "budget_max": 0.00,
  "concurrency_slot": 1,
  "timeout_sec": 300
}
```

**Output (risultato per job):**
```json
{
  "job_id": "J-YYYYMMDD-NNN",
  "stato": "completed|failed|timeout|killed",
  "cost_event": { "costo": 0.00, "durata_sec": 0 },
  "output": {}
}
```

## Logica della coda

| Priorità | Tipo job | Concorrenza max |
|---|---|---|
| 1 (urgente) | blocchi COST-GUARD, gate governance | 1 (always first) |
| 2 (alta) | run outreach (AGENCY revenue) | 3 |
| 3 (normale) | batch content, build siti | 5 |
| 4 (background) | backup, wiki-garden, trend-radar | 2 |

**Backpressure:** se tutti i slot di concorrenza sono occupati e arriva un job di
priorità 3+, il job viene accodato. Se la coda supera N (configurabile) → alert a
ops-director + Board: capacità insufficiente, potrebbe servire scaling.

## Processo decisionale

1. Job in ingresso → valida campi obbligatori (budget_max, tipo, priorità).
2. Assegna slot di concorrenza in base alla priorità; se non disponibile → enqueue.
3. Prima del lancio: verifica con COST-GUARD (budget residuo) e con ops-watchdog
   (pre-condizioni: daemon vivo, token validi, disco libero).
4. Lancia job; monitora timeout; job scaduto → kill + retry policy.
5. A job chiuso: emette cost_event, aggiorna `operations/schedule`, notifica richiedente.

## Gate di qualità

- `G-BUDGET` — ogni job deve avere budget_max; COST-GUARD approva prima del lancio
- `G-ATTRIBUTION` — cost_event obbligatorio a job chiuso
- `G-TIMEOUT` — ogni job ha un timeout; nessun job vive per sempre in coda

## KPI

| Metrica | Target |
|---|---|
| Job completati senza timeout | ≥ 95% |
| Tempo di attesa in coda (priorità 1) | ≤ 60s |
| Tempo di attesa in coda (priorità 3) | ≤ 15 min |
| Job con cost_event mancante | 0 |
