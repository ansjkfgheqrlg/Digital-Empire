> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L4 T-retry-failed

# L4 — T-retry-failed (Retry Mirato dei Shard Falliti)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** RUNTIME · **Workflow L3:** WF-SWARM-RUN
**Coordinator:** `ops-swarm-marshal`
**Connessione:** [[../ECOSISTEMA.md]] · [[../BACKBONE.md]]

## Missione

T-retry-failed rilancia SOLO i shard falliti, senza ripetere l'intero batch. Massimo
2 retry per shard; oltre il limite → escalation. Questo riduce drasticamente il costo
dei fallimenti parziali: se 2 shard su 50 falliscono, si rilanciano 2, non 50.

## Input / Output

**Input (da T-merge-results):**
```json
{
  "shard_failed": [
    {"shard_id": "S-002", "errore": "timeout", "items": ["item_3", "item_4"]},
    {"shard_id": "S-007", "errore": "cost_exceeded", "items": ["item_13"]}
  ],
  "retry_count_corrente": 0,
  "max_retry": 2,
  "budget_retry_residuo": 0.00
}
```

**Output (dopo retry):**
```json
{
  "shard_recovered": ["S-002"],
  "shard_definitivamente_falliti": ["S-007"],
  "motivo_fallimento_S007": "budget_esaurito — escalation a ops-director",
  "cost_retry": 0.00
}
```

## Logica di retry

| Tipo di errore | Azione retry |
|---|---|
| timeout | riprova con timeout esteso (+50%) |
| rate_limit | attendi back-off (30s, poi 60s) prima di rilanciare |
| cost_exceeded | prima valuta se scendere di tier; se non possibile → escalation |
| worker_crash | cambia worker (rispawna); se 2 crash → escalation |
| errore_contenuto (accept. criteria non soddisfatti) | riprova con parametri aumentati |

**Dopo 2 retry falliti sullo stesso shard:**
- Log dettagliato dell'errore in `operations/health`
- Escalation a ops-director con shard_id + stacktrace/log
- Il committente riceve il batch senza quel shard (flag `partial: true`)
- Pattern → ReasoningBank via 08-INTELLIGENCE se stesso tipo di errore per 3 batch

## Failure handling

- Budget retry esaurito → NO più retry; escalation a COST-GUARD + ops-director.
- Tutti i shard nel retry falliscono di nuovo → escalation Board (non è un problema
  isolato — qualcosa di sistemico è rotto).

## KPI

| Metrica | Target |
|---|---|
| Shard recuperati al primo retry | ≥ 80% dei failed |
| Shard che richiedono escalation (2 retry falliti) | ≤ 2% del totale shard |
| Costo retry / costo batch totale | ≤ 10% |
| Escalation processata entro SLA | ≤ 15 min |
