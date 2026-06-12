> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-ATTRIBUTION

# L3 — WF-ATTRIBUTION (Ledger Costi per Agente/Run/Commessa)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** COST-GUARD
**Coordinator:** `ops-cost-accountant` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-ATTRIBUTION raccoglie TUTTI gli eventi costo della holding in un ledger unico e
li attribuisce per agente, run, commessa ed ecosistema. Senza attribution non si sa
dove vanno i soldi: è la base del report Board settimanale e del KPI "costo attribuito
/ costo totale ≥ 98%". Una run senza evento costo è una run non valida (gate G-ATTRIBUTION).

## Struttura del ledger

Il ledger risiede in `operations/ledger` (namespace AgentDB) e in file
`company/runtime/ledger-YYYYMM.jsonl` (append-only, mai overwrite — pattern backup
di Memory Empire).

**Evento costo standard (emesso da ogni run/agente):**
```json
{
  "evento_id": "CE-YYYYMMDD-NNNN",
  "timestamp": "ISO8601",
  "ecosistema": "01-AGENCY",
  "workflow": "WF-OUTREACH-EMAIL",
  "agente": "ops-swarm-marshal",
  "commessa": "DE|<cliente_id>",
  "brand_kit": "DE",
  "tier": "Haiku",
  "token_input": 0,
  "token_output": 0,
  "costo_usd": 0.00000,
  "durata_sec": 0,
  "esito": "success|failed|partial"
}
```

## Report settimanale Board (output di WF-ATTRIBUTION)

Generato ogni lunedì mattina da `ops-cost-accountant`, inviato al CFO + Board:

| Ecosistema | Costo settimana | vs settimana prec. | Budget residuo mese |
|---|---|---|---|
| 01-AGENCY | $X.XX | +/-N% | $Y.YY |
| ... | ... | ... | ... |
| **TOTALE** | **$X.XX** | **+/-N%** | **$Y.YY** |

Sotto: top 3 agenti per costo, top 3 workflow per costo, alert aperti.

## Processo decisionale (`ops-cost-accountant`)

1. Riceve eventi costo in stream dal Bus; li valida (campi obbligatori presenti?).
2. Appende al ledger JSONL (mai sovrascrive — append-only per audit trail).
3. Aggiorna gli aggregati in AgentDB `operations/ledger` (per query veloci).
4. Ogni run chiusa senza evento costo → alert a ops-director: "run X di ecosistema Y
   non ha emesso cost_event — run dichiarata non valida".
5. Ogni lunedì: aggrega, calcola delta, genera report Board, invia via Bus al CFO.
6. Drift di costo (run costosa >2σ dalla media storica) → alert a ops-cost-sentinel.

## Gate di qualità

- `G-ATTRIBUTION` — ogni run emette cost_event; assenza = run non valida
- `G-APPEND-ONLY` — ledger è append-only; nessuna riga viene cancellata o modificata
- `G-REPORT` — report Board ogni lunedì senza mancanze

## KPI

| Metrica | Target |
|---|---|
| Costo attribuito / costo totale (copertura ledger) | ≥ 98% |
| Run senza cost_event rilevate | 0 a regime |
| Report Board inviati puntuale | 100% settimane |
| Tempo di ingestione evento costo | ≤ 10s |
