> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-SWARM-RUN

# L3 — WF-SWARM-RUN (Produzione di massa via swarm)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** RUNTIME
**Coordinator:** `ops-swarm-marshal` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-SWARM-RUN esegue qualsiasi batch di produzione a N items in parallelo:
50 caroselli, 30 capitoli KDP, 20 pagine sito, 100 email personalizzate.
Pattern di riferimento: CF `swarm.sh --parallel N --budget N`, portato in DE
come skill `empire-swarm` (da forgiare — priorità ALTA).

## Input / Output

**Input (handoff inbound):**
```json
{
  "items": ["<item_1>", "...", "<item_N>"],
  "template": "<workflow_di_produzione>",
  "budget_max": 0.00,
  "brand_kit": "DE|<cliente>",
  "icp": "<profilo>",
  "concurrency": 5,
  "dry_run": true
}
```

**Output (result outbound):**
```json
{
  "completed": N,
  "failed": [],
  "cost_total": 0.00,
  "duration_sec": 0,
  "output_paths": ["..."],
  "cost_event": "emesso a COST-GUARD"
}
```

## Funzioni L4 contenute

| Team L4 | Funzione | Path |
|---|---|---|
| T-fanout | sharding del batch in shard disgiunti | `Funzioni/T-fanout/` |
| T-worker-pool | spawna e coordina i worker in parallelo | `Funzioni/T-worker-pool/` |
| T-merge-results | unisce gli output degli shard completati | `Funzioni/T-merge-results/` |
| T-retry-failed | rilancia solo i shard falliti (max 2 retry) | `Funzioni/T-retry-failed/` |

## Processo decisionale (come ragiona `ops-swarm-marshal`)

1. Valida handoff: items presenti, acceptance_criteria, budget_max dichiarato?
   Mancante → reject con note (handoff senza criteri è invalido per contratto).
2. `dry_run: true` → stima `items × costo_per_item_del_tier` → se stima > budget: STOP.
   Propone: ridurre batch, scendere di tier, oppure ok umano al CFO.
3. Sceglie topologia: shard disgiunti → parallel fan-out; dipendenze sequenziali → pipeline.
4. Lancia T-worker-pool con concurrency dichiarata; ogni shard emette evento costo (G-ATTRIBUTION).
5. A fine corsa: T-merge-results → T-retry-failed su falliti (max 2 retry, poi escalation).
6. Report finale al committente + HC-ME-POST a 10-MEMORY con costi inclusi.

## Gate di qualità

- `G-DRYRUN` — dry-run obbligatoria prima di ogni run reale con stima costi
- `G-BUDGET` — budget dichiarato e approvato da COST-GUARD prima della run
- `G-ATTRIBUTION` — ogni shard emette evento costo; run senza evento = non valida
- `G-ACCEPTANCE` — acceptance criteria devono essere misurabili e presenti nell'handoff

## KPI

| Metrica | Target |
|---|---|
| Shard completati / shard totali | ≥ 98% |
| Costo reale / stima dry-run | ≤ +10% |
| Retry rate per batch | ≤ 5% |
| Escalation per budget sforato | 0 |
