> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-LOOP

# L3 — WF-LOOP (Loop Self-Paced su Condizione)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** SCHEDULING
**Coordinator:** `ops-scheduler` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-LOOP gestisce i flussi che non hanno un trigger temporale fisso ma una condizione
di uscita: "ripeti finché la coda non è vuota", "controlla il deploy ogni 5 minuti
finché non è verde", "elabora tutti i lead nuovi uno per uno".

Si basa sulle skill `loop` e `schedule` (cloud agents cron) già esistenti nel sistema.

Differenza rispetto a WF-CRON: WF-CRON ha un trigger temporale fisso (es. ore 8:00);
WF-LOOP ha una condizione logica e un passo da ripetere finché la condizione è vera.

## Tipologie di loop supportate

| Tipo | Condizione | Esempio |
|---|---|---|
| Queue drain | lista non vuota | elabora lead dal CRM uno per uno |
| Poll until ready | stato atteso | aspetta che il deploy Vercel sia green |
| Rate-limited batch | N items ogni M minuti | invio email a 10/min per rispettare rate limit |
| Retry until success | tentativi < MAX | retry scraping con backoff esponenziale |
| Time-bounded | durata < timeout | processa al massimo 30 minuti poi stop |

## Input / Output

**Registrazione loop:**
```json
{
  "nome": "drain-lead-queue",
  "condizione_uscita": "len(queue) == 0 OR tentativi > 100",
  "passo": "skill avvia-scraper --single",
  "intervallo_sec": 30,
  "budget_per_iterazione": 0.00,
  "budget_totale_max": 0.00,
  "timeout_totale_sec": 3600,
  "rollback": "svuota queue parzialmente elaborata"
}
```

**Output (a loop terminato):**
```json
{
  "iterazioni": 0,
  "esito_uscita": "condizione_soddisfatta|timeout|budget_esaurito|errore",
  "costo_totale": 0.00,
  "durata_sec": 0
}
```

## Processo decisionale (`ops-scheduler`)

1. Verifica che condizione_uscita sia definita e che timeout_totale_sec sia presente.
   Senza timeout: il loop NON parte (un loop senza uscita è un zombie).
2. Prima di ogni iterazione: verifica budget residuo (budget_per_iterazione × iterazioni_attese ≤ budget_totale_max).
3. Esegue il passo; valuta la condizione; se falsa → attende intervallo_sec → ripete.
4. Se COST-GUARD segnala budget esaurito → uscita anticipata con log.
5. A loop terminato: emette cost_event complessivo + HC-ME-POST a 10-MEMORY.

## Gate di qualità

- `G-TIMEOUT` — ogni loop ha un timeout totale; senza, non parte
- `G-BUDGET` — budget per iterazione e totale dichiarati
- `G-EXIT-CONDITION` — condizione di uscita obbligatoria e testabile

## KPI

| Metrica | Target |
|---|---|
| Loop terminati per condizione (non timeout) | ≥ 90% |
| Loop zombie (senza uscita rilevata in > 2h) | 0 |
| Costo loop / stima iniziale | ≤ +15% |
