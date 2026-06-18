---
Type: CONCEPT
Status: Active
Tags: #cfo #state #namespace #ledger #agentdb
Created: 2026-06-18
Last updated: 2026-06-18
---

# STATE — Schema dello Stato della Figura CFO

> Namespace AgentDB: `board/cfo`
> Connessioni: [[cfo-memoria]] · [[cfo-cost-accountant]] · [[cfo-cost-sentinel]] · [[SCRIPTS]]

---

## Panoramica

Lo stato della figura CFO è mantenuto in due livelli:

1. **AgentDB namespace `board/cfo`** — stato in-memory per le sessioni attive. Lettura aperta a
   tutti gli agenti CFO; solo `cfo-memoria` scrive le chiavi di storico, solo `cfo-cost-accountant`
   scrive il ledger.
2. **File system `state/`** — stato persistente tra sessioni. I file JSON sono la fonte di verità
   per gli script e per il `cfo-cost-sentinel`. Ledger e alert sono append-only.

---

## Schema namespace `board/cfo` (AgentDB)

| Chiave | Tipo | Owner (scrive) | Chi legge | Cosa contiene |
|---|---|---|---|---|
| `board/cfo/ledger` | array of JSON | `cfo-cost-accountant` | tutti gli agenti CFO | Eventi di costo del periodo (append-only) |
| `board/cfo/budget-envelope` | JSON | `cfo-budget-guard` | `cfo-conductor`, `cfo-forecast-finance` | Envelope di spesa per ecosistema/trimestre |
| `board/cfo/tier-decisions` | array of JSON | `cfo-tier-router` | `cfo-cost-accountant` | Decisioni di routing tier per task |
| `board/cfo/forecast` | JSON | `cfo-forecast-finance` | `cfo-conductor`, `cfo-roi-analyst` | Forecast costi + runway |
| `board/cfo/roi-ecosistemi` | JSON | `cfo-roi-analyst` | `cfo-conductor` | ROI per ecosistema (valore/costo) |
| `board/cfo/spese-approvate` | array of JSON | `cfo-spend-approver` | `cfo-cost-accountant` | Spese reali con ok esplicito (pattern #3) |
| `board/cfo/alerts` | array of JSON | `cfo-cost-sentinel` | `cfo-conductor` | Alert aperti (80% budget, sforo, drift) |
| `board/cfo/runway` | JSON | `cfo-runway-tracker` | `cfo-conductor` | Risorse di sessione residue, budget-guard 20% |

---

## Schema file system `state/` (persistente)

```
state/
├── ledger/
│   ├── eventi_YYYYMMDD.json          ← eventi di costo del giorno (append-only)
│   └── aggregato_Q2-2026.json        ← aggregato costi per ecosistema/commessa
├── budget-envelope/
│   ├── envelope_Q2-2026.json         ← envelope correnti per ecosistema
│   └── archivio/envelope_Q1-2026.json
├── budget-decisions/
│   └── <run_id>.json                 ← una decisione approvato/bloccato per run
├── tier-decisions/
│   └── YYYYMMDD.json                 ← decisioni di routing tier del giorno
├── forecast/
│   └── forecast_Q2-2026.json         ← forecast costi + scostamento vs reale
├── spese-approvate/
│   └── SPESA-YYYYMMDD-NNN.json        ← spese reali con ok esplicito
└── alerts/
    └── YYYYMMDD_HHMM_alert.json       ← alert prodotti da spend_guard.ps1
```

---

## Schema dei file chiave

### `state/ledger/eventi_YYYYMMDD.json`
```json
{
  "data": "2026-06-18",
  "eventi": [
    {
      "run_id": "RUN-20260618-014", "ecosistema": "01-AGENCY", "agente": "outreach-writer",
      "tier": "haiku", "costo": 8, "unita": "crediti", "durata_s": 42,
      "commessa": "cliente-X", "esito": "ok", "timestamp": "ISO8601"
    }
  ],
  "copertura": "98.5%"
}
```

### `state/budget-envelope/envelope_<trimestre>.json`
```json
{
  "trimestre": "Q2-2026",
  "envelope": [
    {"ecosistema": "06-PLATFORM", "assegnato": 1000, "residuo": 690, "unita": "crediti"}
  ],
  "soglia_alert_pct": 80
}
```

### `state/alerts/<timestamp>_alert.json`
```json
{
  "alert_id": "ALERT-CFO-YYYYMMDD-NNN",
  "tipo": "soglia_80 | sforo | drift_costo | spesa_reale_pendente | runway_sotto_20",
  "ecosistema": "06-PLATFORM | null",
  "run_id": "RUN-... | null",
  "priorita": "critica | alta | media",
  "stato_alert": "aperto | preso_in_carico | risolto",
  "timestamp_creazione": "ISO8601",
  "nota": "string"
}
```

---

## Lifecycle degli stati

```
BUDGET-DECISION: richiesta → (stima dry-run) → approvato | bloccato_pre_sforo
SPESA REALE:     richiesta → ok_esplicito (cfo-spend-approver) → registrata nel ledger
ALERT:           aperto → preso_in_carico → risolto
RUNWAY:          ok (>20%) → warning (<20% → chiudi col COMMIT, no nuovi build)
```

---

## Regole di accesso

- **Ledger append-only:** `cfo-cost-accountant` è l'unico che scrive; nessuna modifica/cancellazione.
- **Envelope atomico:** il decremento avviene all'approvazione di `budget-guard`, mai retroattivo.
- **Spese reali:** solo `cfo-spend-approver` scrive `spese-approvate`, e solo con ok esplicito.
- **Lettura aperta:** tutti gli agenti CFO leggono il namespace; lo storico (`cfo-memoria`) non si sovrascrive.

---

## Connessioni

- [[cfo-memoria]] · `agenti/cfo-memoria.md`
- [[cfo-cost-accountant]] · `agenti/cfo-cost-accountant.md`
- [[cfo-cost-sentinel]] · `agenti/cfo-cost-sentinel.md`
- [[cfo-runway-tracker]] · `agenti/cfo-runway-tracker.md`
- [[SCRIPTS]] · `scripts/README.md`
- [[KPI]] · `kpi/KPI.md`
- [[ARCHITETTURA]] · `ARCHITETTURA.md`
