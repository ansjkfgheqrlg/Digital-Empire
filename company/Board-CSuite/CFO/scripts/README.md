---
Type: CONCEPT
Status: Active
Tags: #cfo #scripts #budget #ledger #automazione
Created: 2026-06-18
Last updated: 2026-06-18
---

# SCRIPTS — Script di Cost Guard e Report della Figura CFO

> Descrizione degli script previsti (non implementazione). Build effettiva: fase V2-build CFO.
> Connessioni: [[WF-BUDGET]] · [[WF-COST-REPORT]] · [[STATE]]

---

## Convenzione

Script in Python (logica) e PowerShell (dispatch/schedule Windows). Ogni script legge da `state/`
o da JSON passato come argomento, scrive in `state/`, logga in `scripts/logs/`. Nessuno script
scrive nei file Memory senza passare dalla skill corrispondente. Il CFO è Haiku-heavy: gli script
fanno il lavoro deterministico, gli agenti solo il giudizio.

---

## Script 1: `budget_check.py`

### Cosa fa
Implementa la skill `budget-guard`: data una richiesta di run con stima dry-run, confronta con
l'envelope dell'ecosistema e restituisce approvato / bloccato_pre_sforo. Decrementa l'envelope
atomico all'approvazione.

### Input
- `richiesta_run.json` — {workflow, ecosistema, stima_costo, run_id}.
- `state/budget-envelope/envelope_<trimestre>.json` — envelope correnti.

### Output
- Decisione in `state/budget-decisions/<run_id>.json`.
- Envelope aggiornato. Log in `scripts/logs/budget_YYYYMMDD.log`.
- Return code: 0 approvato, 1 bloccato_pre_sforo, 2 stima mancante (blocco pattern #3).

---

## Script 2: `cost_ledger.py`

### Cosa fa
Implementa la skill `cost-ledger`: registra eventi di costo (append-only) e calcola gli aggregati
per ecosistema/commessa. Fonte di verità dei consuntivi.

### Input
- `evento_costo.json` — {run_id, ecosistema, agente, tier, costo, durata, commessa, esito}.

### Output
- Append in `state/ledger/eventi_YYYYMMDD.json`.
- Aggiornamento `state/ledger/aggregato_<trimestre>.json`.
- Log con copertura % (run con evento / run totali). Return code: 0 ok, 1 evento malformato.

---

## Script 3: `tier_route.py`

### Cosa fa
Implementa la skill `tier-router`: classifica un task e restituisce il tier (WASM/Haiku/Sonnet/Opus).
Registra ogni decisione per il KPI 3.

### Input
- `task.json` — {task, attributi: {deterministico, criticita, volume, richiede_giudizio}}.

### Output
- `state/tier-decisions/YYYYMMDD.json` (append).
- Return code: 0 (sempre, è una decisione, non un blocco).

---

## Script 4: `cost_report.py`

### Cosa fa
Produce il report costi periodico per il CEO/Board: spesa per ecosistema, copertura ledger,
quota tier economico, sforamenti, ROI dove disponibile. Nessun numero inventato: ogni campo cita la fonte.

### Input
- `--periodo YYYYMMDD-YYYYMMDD` · `--formato markdown | json`.
- Legge `state/ledger/`, `state/budget-decisions/`, `state/tier-decisions/`.

### Output
- `reports/cost_report_YYYYMMDD.md` con sezioni: spesa per ecosistema, KPI 1-8, alert aperti, nota CFO.
- Log in `scripts/logs/cost_report_YYYYMMDD.log`.

---

## Script 5: `spend_guard.ps1`

### Cosa fa
Monitora l'avvicinamento ai limiti di budget e produce gli alert all'80% (skill di `cfo-cost-sentinel`).
Gira su schedule. Scrive alert in `state/alerts/`. Intercetta le richieste di spesa REALE e le instrada
a `cfo-spend-approver` (ok esplicito obbligatorio).

### Input
- `state/budget-envelope/*.json` + `state/ledger/aggregato_*.json`.

### Output
- `state/alerts/YYYYMMDD_HHMM_alert.json` per ogni soglia 80% raggiunta o spesa reale pendente.
- Log in `scripts/logs/spend_guard_YYYYMMDD.log`. Schedule: ogni 2 ore in giornata lavorativa.

---

## Connessioni

- [[WF-BUDGET]] · `workflow/WF-BUDGET.md`
- [[WF-COST-REPORT]] · `workflow/WF-COST-REPORT.md`
- [[WF-SPEND-APPROVAL]] · `workflow/WF-SPEND-APPROVAL.md`
- [[cfo-budget-guard]] · [[cfo-cost-accountant]] · [[cfo-cost-sentinel]]
- [[STATE]] · `state/README.md`
