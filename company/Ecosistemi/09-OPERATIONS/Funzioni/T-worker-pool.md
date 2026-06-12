> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L4 T-worker-pool

# L4 — T-worker-pool (Worker Pool Parallelo)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** RUNTIME · **Workflow L3:** WF-SWARM-RUN
**Coordinator:** `ops-swarm-marshal`
**Connessione:** [[../ECOSISTEMA.md]] · [[../BACKBONE.md]]

## Missione

T-worker-pool spawna i worker e li coordina in parallelo fino alla concorrenza
dichiarata. Ogni worker elabora un shard assegnatogli da T-fanout e ne emette il
cost_event. Il pool gestisce il ciclo di vita dei worker: spawn, monitoring,
completamento, rilascio slot.

## Input / Output

**Input (da T-fanout):**
```json
{
  "shard": [{"shard_id": "S-001", "items": ["..."]}],
  "template_workflow": "WF-CAROUSEL-PRODUCER",
  "concurrency": 5,
  "tier": "Haiku",
  "budget_per_shard": 0.00,
  "brand_kit": "DE|<cliente>",
  "timeout_per_shard_sec": 300
}
```

**Output (per shard completato):**
```json
{
  "shard_id": "S-001",
  "stato": "completed|failed|timeout",
  "output": {},
  "cost_event": {"costo": 0.00, "durata_sec": 0, "tier": "Haiku"},
  "worker_id": "W-001"
}
```

## Gestione del pool

- Spawna fino a `concurrency` worker in parallelo (via Ruflo `agent_spawn` o Agent tool).
- Ogni slot liberato (worker completato) → shard successivo dalla coda.
- Worker in timeout → kill, shard finisce in `failed` per T-retry-failed.
- Worker con costo > `budget_per_shard` → STOP del worker (ops-cost-sentinel ha emesso kill).

**Topologia:** hierarchical temporanea — `ops-swarm-marshal` è il coordinator root
del sotto-swarm; i worker sono worker leaf. Il sotto-swarm è usa-e-getta (distrutto
a batch completato).

## Failure handling

- Worker fallito: registra shard in `failed[]`, slot liberato → shard successivo.
- Tutti i worker falliti su tipo di task → escalation a ops-director: potrebbe essere
  un problema di tier (Thompson Sampling aggiorna).
- Daemon Ruflo giù → fallback: lancia worker con bash/ps1 in sequenza (non parallelo);
  il batch continua con latenza maggiore, non si interrompe.

## KPI

| Metrica | Target |
|---|---|
| Utilizzo slot concorrenza (slot attivi / slot totali) | ≥ 80% durante batch |
| Worker in timeout | ≤ 2% per batch |
| Slot non rilasciati (leak) | 0 |
| Overhead spawn per worker | ≤ 5s |
