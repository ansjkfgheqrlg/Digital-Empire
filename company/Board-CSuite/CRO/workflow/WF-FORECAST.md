---
Type: WORKFLOW
Status: Active
Tags: #workflow #cro #forecast #trimestrale #revenue #ceo
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-FORECAST — Forecast Trimestrale Revenue → CEO

> **ID:** WF-CRO-002 · **Owner:** `cro-conductor` · **Blueprint:** `BP-CRO.md`
> **Cadenza:** trimestrale (inizio Q) + alert fuori banda se anomalia >20%

---

## Scopo

Produrre ogni trimestre un documento forecast revenue disaggregato per fonte (Agency pipeline,
lanci InfoBusiness, retention/upsell) con 3 scenari (pessimistico/base/ottimistico), consegnarlo
al CEO-conductor come input per gli OKR del trimestre, e confrontarlo con il reale a fine
trimestre per migliorare iterativamente il modello di forecast.

---

## Attori

| Step | Agente |
|---|---|
| Orchestrazione | `cro-conductor` |
| Dati pipeline Agency | `cro-pipeline-health` + `cro-agency-pipeline` |
| Dati lanci IB | `cro-infobusiness-launches` |
| Dati retention/upsell | `cro-retention-revenue` |
| Elaborazione scenari | `cro-forecast-analyst` |
| Confronto vs reale | `cro-forecast-analyst` + `cro-memoria` |
| Consegna CEO | `cro-conductor` → HC-CRO-CEO-01 |

---

## Flusso passo-passo

```
[TRIGGER]
Inizio trimestre (o anomalia rilevata >20% da forecast corrente)
         │
         ▼
[STEP 1] cro-conductor — avvia raccolta dati
  → notifica tutti gli agenti source: "produce input forecast entro 48h"
  → timeout: se un agente non risponde entro 48h → alert + proceed con dati disponibili (nota [DM])
         │
         ▼
[STEP 2] Raccolta dati in parallelo (48h)

  [A] cro-pipeline-health
      → snapshot per stadio: n. deal per stadio + tassi conversione storici
      → classifica ogni deal: certo / probabile / possibile

  [B] cro-infobusiness-launches
      → calendario lanci trimestre: titoli, date, prezzi (se definiti)
      → revenue atteso per lancio (da storico `cro-memoria`)
      → blocchi attivi (prezzi non definiti → esclusione dal base scenario)

  [C] cro-retention-revenue
      → upsell in corso: clienti, prodotto proposto, probabilità
      → win-back pipeline: candidati attivi, valore atteso
      → stima retention revenue 30-90gg

  → tutti e 3 consegnano JSON input al cro-forecast-analyst
         │
         ▼
[STEP 3] cro-forecast-analyst — elaborazione scenari
  → classifica ogni voce (certa / probabile / possibile)
  → calcola 3 scenari (pessimistico / base / ottimistico) per fonte
  → identifica rischi (voci non classificabili, prezzi mancanti, deal in stallo)
  → produce priorità revenue: 3-5 azioni ad alto impatto per il trimestre
  → GATE: ogni voce ha fonte documentata O è marcata [DM]; nessun numero inventato
         │
         ▼
[STEP 4] cro-memoria — confronto vs trimestre precedente
  → legge il forecast del trimestre precedente + revenue reale archiviato
  → calcola scostamento %
  → se scostamento >20%: produce nota analisi causa (modello da aggiornare? evento esogeno?)
  → alimenta la sezione "confronto_precedente" del documento forecast
         │
         ▼
[STEP 5] cro-conductor — review e firma documento
  → legge il documento prodotto da cro-forecast-analyst
  → verifica: scenario raccomandato è il base? tutte le voci hanno fonte? rischi documentati?
  → GATE: documento completo e coerente → procede; lacune → ritorna a cro-forecast-analyst
  → aggiunge sintesi esecutiva (3-5 righe) per il CEO
         │
         ▼
[STEP 6] Handoff CEO — HC-CRO-CEO-01
  → documento forecast consegnato al CEO-conductor
  → CEO usa il documento come input per gli OKR del trimestre
  → `cro-conductor` archivia il documento in `board/cro/forecast/`
         │
         ▼
[STEP 7 — fine trimestre] Confronto vs reale
  → cro-conductor raccoglie il revenue reale (da `cro-memoria`: deal chiusi + lanci chiusi)
  → cro-forecast-analyst calcola scostamento
  → se scostamento >20%: analisi causa + proposta aggiornamento modello
  → documento retrospettivo archiviato in `board/cro/forecast/retro-QN.md`
```

---

## Gate bloccanti

| Gate | Condizione PASS | Blocca |
|---|---|---|
| G1 — Dati source completi | Almeno 2/3 fonti rispondono entro 48h | Nota [DM] per fonte mancante |
| G2 — No numeri inventati | Ogni voce con fonte O marcata [DM] | `cro-forecast-analyst` rigetta la voce |
| G3 — Documento coerente | Scenari calcolati, rischi documentati, priorità presenti | `cro-conductor` rimanda a revisione |
| G4 — Confronto trimestre precedente | Sezione confronto popolata (anche se primo trimestre: "N/A" esplicito) | `cro-memoria` obbligatorio |

---

## Input del workflow

```json
{
  "trigger": "inizio_trimestre | anomalia",
  "trimestre": "Q3-2026",
  "data_avvio": "2026-07-01",
  "scadenza_consegna_ceo": "2026-07-05"
}
```

## Output del workflow (documento forecast)

```json
{
  "documento_forecast": {
    "trimestre": "Q3-2026",
    "data_produzione": "2026-07-04",
    "scenario_base_totale": 0,
    "scenario_pessimistico_totale": 0,
    "scenario_ottimistico_totale": 0,
    "per_fonte": {
      "agency_pipeline": {"pessimistico": 0, "base": 0, "ottimistico": 0},
      "infobusiness_lanci": {"pessimistico": 0, "base": 0, "ottimistico": 0},
      "retention_upsell": {"pessimistico": 0, "base": 0, "ottimistico": 0}
    },
    "rischi_principali": [],
    "priorita_revenue": [],
    "confronto_trimestre_precedente": {
      "forecast": 0,
      "reale": 0,
      "scostamento_pct": 0
    },
    "fonti_dati": ["cro-pipeline-health", "cro-infobusiness-launches", "cro-retention-revenue"]
  }
}
```

---

## State

File: `board/cro/forecast/forecast-QN-YYYY.json`
- 1 file per trimestre, aggiornato con il reale a fine trimestre.
- Storico consultabile da `cro-memoria` per calibrare i forecast futuri.

---

## Connessioni

- [[cro-conductor]] · `agenti/cro-conductor.md`
- [[cro-forecast-analyst]] · `agenti/cro-forecast-analyst.md`
- [[cro-pipeline-health]] · `agenti/cro-pipeline-health.md`
- [[cro-infobusiness-launches]] · `agenti/cro-infobusiness-launches.md`
- [[cro-retention-revenue]] · `agenti/cro-retention-revenue.md`
- [[cro-memoria]] · `agenti/cro-memoria.md`
- [[WF-DEAL]] · `workflow/WF-DEAL.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
