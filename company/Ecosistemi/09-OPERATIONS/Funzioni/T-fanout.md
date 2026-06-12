> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L4 T-fanout

# L4 — T-fanout (Sharding del Batch in Shard Disgiunti)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** RUNTIME · **Workflow L3:** WF-SWARM-RUN
**Coordinator:** `ops-swarm-marshal`
**Connessione:** [[../ECOSISTEMA.md]] · [[../BACKBONE.md]]

## Missione

T-fanout prende un batch di N items e lo divide in M shard disgiunti da distribuire
ai worker in parallelo. Ogni shard è indipendente: un fallimento su un shard non
blocca gli altri. La dimensione degli shard bilanicia efficienza (shard grandi =
meno overhead) e resilienza (shard piccoli = retry granulare).

## Input / Output

**Input:**
```json
{
  "items": ["item_1", "...", "item_N"],
  "concurrency": 5,
  "strategia": "round_robin|batch_size|by_tipo"
}
```

**Output:**
```json
{
  "shard": [
    {"shard_id": "S-001", "items": ["item_1", "item_2"]},
    {"shard_id": "S-002", "items": ["item_3", "item_4"]},
    "..."
  ],
  "total_shards": 5,
  "items_per_shard": 2
}
```

## Logica di sharding

| Strategia | Quando usarla | Come divide |
|---|---|---|
| `round_robin` | items omogenei, nessuna dipendenza | 1 item per turno a ogni shard |
| `batch_size` | vuoi shard di dimensione fissa N | items / N = numero shard |
| `by_tipo` | items con tipo diverso (es. email vs LinkedIn) | raggruppa per tipo |

**Regola invariante:** nessun item compare in due shard (disgiunti).
Sovrapposizione = bug critico (produzione duplicata, doppio costo).

## Failure handling

- Se `len(items) == 0` → T-fanout emette warning e restituisce lista shard vuota
  (ops-swarm-marshal decide se è un errore del committente o un batch legittimamente vuoto).
- Se `concurrency > len(items)` → riduce concurrency a len(items) (un worker per item).
- Items non serializzabili → messi in `shard_rejected` con motivo, il resto procede.

## KPI

| Metrica | Target |
|---|---|
| Items duplicati tra shard | 0 assoluto |
| Items persi (non in nessun shard) | 0 assoluto |
| Tempo di fanout (N=100 items) | ≤ 2s |
