> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L4 T-merge-results

# L4 — T-merge-results (Unione Output degli Shard)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** RUNTIME · **Workflow L3:** WF-SWARM-RUN
**Coordinator:** `ops-swarm-marshal`
**Connessione:** [[../ECOSISTEMA.md]] · [[../BACKBONE.md]]

## Missione

T-merge-results unisce gli output di tutti gli shard completati in un risultato
coerente, calcola il costo totale aggregato, segnala i falliti a T-retry-failed e
produce il report finale per il committente. È il penultimo step del WF-SWARM-RUN.

## Input / Output

**Input (da T-worker-pool, tutti gli shard chiusi):**
```json
{
  "shard_results": [
    {"shard_id": "S-001", "stato": "completed", "output": {}, "cost_event": {}},
    {"shard_id": "S-002", "stato": "failed", "errore": "timeout"},
    "..."
  ],
  "output_type": "lista|file|stream|aggregato"
}
```

**Output (risultato unificato):**
```json
{
  "completati": 48,
  "falliti": 2,
  "shard_failed": ["S-002", "S-007"],
  "output_merged": ["path_1", "...", "path_48"],
  "cost_totale": 0.00,
  "duration_totale_sec": 0,
  "cost_event_aggregato": {"costo": 0.00, "ecosistema": "...", "workflow": "..."}
}
```

## Strategie di merge

| Output type | Come unisce |
|---|---|
| `lista` | concatena le liste di ogni shard nell'ordine originale |
| `file` | colleziona i path dei file prodotti; nessuna fusione fisica |
| `stream` | ordina per timestamp di completamento |
| `aggregato` | somma/media secondo schema dichiarato nel template |

**Ordine di output:** T-merge-results mantiene l'ordine originale degli items
(non lo shard order, che potrebbe essere casuale). Importante per output numerati
(es. caroselli con slide in sequenza).

## Failure handling

- Shard failed → passati a T-retry-failed; T-merge-results NON li include nel
  merged output (li segna come `pendenti_retry`).
- Se tutti i shard sono falliti → merge restituisce output vuoto + escalation a ops-director.
- Output parziale (falliti > 20% del totale) → il committente riceve flag `partial: true`
  con lista dei shard mancanti.

## KPI

| Metrica | Target |
|---|---|
| Integrità ordine output (items nell'ordine originale) | 100% |
| Tempo di merge (N=100 shard) | ≤ 5s |
| Cost_event aggregato emesso | 100% dei batch |
| Output con shard mancanti senza flag `partial` | 0 |
