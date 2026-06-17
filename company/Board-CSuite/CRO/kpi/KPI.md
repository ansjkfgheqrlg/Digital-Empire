---
Type: CONCEPT
Status: Active
Tags: #kpi #cro #revenue #metriche #tracking
Created: 2026-06-17
Last updated: 2026-06-17
---

# KPI — CRO (Chief Revenue Officer)

> I KPI presidiati dal team CRO. Fonte: Blueprint BP-CRO.md §KPI presidiati + v1 CRO.md §KPI.
> **Convenzione [DM]:** KPI operativo attivo; il valore target si fissa dopo i primi 60 giorni
> di dati reali. "Prove non promesse" (Mandato Art.2): nessun target inventato.

---

## KPI Primari (Revenue)

### KPI-CRO-001 — Deal Chiusi / Mese
**Metrica:** numero di contratti Agency firmati nel mese.
**Fonte dati:** `board/cro/deals/` (record win con data firma).
**Responsabile:** `cro-agency-pipeline` + `cro-conductor`.
**Target:** [DM] — da stabilire dopo primi 2 mesi di dati reali.
**Semaforo:** rosso = 0 deal/mese; giallo = 1 deal; verde = ≥2 deal (provvisorio, da aggiornare).
**Cadenza review:** settimanale in pipeline snapshot; mensile in report CEO.

---

### KPI-CRO-002 — Revenue Agency Mensile (€)
**Metrica:** somma dei contratti firmati nel mese (valore one-time, pagamento verificato).
**Fonte dati:** `board/cro/deals/` filtrato per data firma + pagamento ricevuto confermato.
**Responsabile:** `cro-conductor`.
**Target:** [DM].
**Nota:** separa "contratti firmati" da "pagamenti ricevuti" — il revenue è conteggiato al pagamento.

---

### KPI-CRO-003 — Revenue InfoBusiness per Lancio (€)
**Metrica:** revenue reale generato da ogni lancio IB (somma acquisti durante la finestra lancio).
**Fonte dati:** 02-INFO-BUSINESS → handoff `HC-IB-CRO-01` dopo chiusura lancio.
**Responsabile:** `cro-infobusiness-launches`.
**Target:** [DM] — varia per prodotto e canale.
**Nota:** confrontare con revenue atteso dichiarato prima del lancio (confronto pre/post obbligatorio).

---

### KPI-CRO-004 — Forecast vs Reale (%)
**Metrica:** scostamento % tra revenue forecast (scenario base) e revenue reale a fine trimestre.
**Formula:** `(reale - forecast_base) / forecast_base × 100`.
**Fonte dati:** `board/cro/forecast/forecast-QN-YYYY.json` + deal chiusi del trimestre.
**Responsabile:** `cro-forecast-analyst`.
**Target:** scostamento <20% (obiettivo di miglioramento continuo, non KPI statico).
**Cadenza:** trimestrale.

---

## KPI Pipeline Agency

### KPI-CRO-005 — Conversion per Stadio
**Metrica:** tasso di avanzamento tra stadi adiacenti del funnel.
| Conversione | Formula | Target |
|---|---|---|
| Lead → Risposta positiva | risposte / outreach inviati | [DM] |
| Risposta → Preventivo inviato | preventivi / risposte positive | [DM] |
| Preventivo → Contratto | contratti / preventivi inviati | >30% (da v1 CRO.md) |

**Fonte dati:** `cro-pipeline-health` snapshot settimanale.
**Responsabile:** `cro-pipeline-health` + `cro-agency-pipeline`.
**Cadenza:** settimanale.

---

### KPI-CRO-006 — Tempo Ciclo di Vendita (giorni)
**Metrica:** giorni medi da risposta positiva a contratto firmato.
**Fonte dati:** `board/cro/deals/` — campo `durata_ciclo_gg` per deal win.
**Responsabile:** `cro-agency-pipeline`.
**Target:** [DM] — media storica da costruire nei primi 3 mesi.
**Nota:** monitorare per stadio (dove si perde tempo: preventivo? chiusura?).

---

## KPI Cross-Sell e Retention

### KPI-CRO-007 — Cross-Sell Info → Agency (deal/lancio)
**Metrica:** numero di contratti Agency originati da acquirenti prodotti InfoBusiness.
**Fonte dati:** `board/cro/cross-sell/` — deal con canale_origine = "cross-sell-IB".
**Responsabile:** `cro-cross-sell-mapper`.
**Target:** [DM].
**Cadenza:** per lancio + riepilogo trimestrale.

---

### KPI-CRO-008 — LTV Medio per Cliente (€)
**Metrica:** somma di tutti gli acquisti (Agency + IB) per cliente, divisa per il numero di clienti.
**Fonte dati:** `board/cro/retention/ltv-registro.json`.
**Responsabile:** `cro-retention-revenue`.
**Target:** [DM].
**Cadenza:** aggiornato ad ogni nuovo acquisto; report trimestrale.

---

### KPI-CRO-009 — Churn Rate (%)
**Metrica:** % di clienti che non effettuano un secondo acquisto entro 12 mesi dal primo.
**Fonte dati:** `board/cro/retention/` — cohort per data primo acquisto.
**Responsabile:** `cro-retention-revenue`.
**Target:** [DM] — massimizzare la retention, non solo acquisire.
**Nota:** il churn è un sintomo: monitorare anche i segnali precursori (NPS, ticket, silenzio).

---

## KPI Qualità Processo

### KPI-CRO-010 — % Preventivi PASS Gate al Primo Giro
**Metrica:** preventivi che passano il proposal-gate senza iterazioni / totale preventivi checkati.
**Fonte dati:** log `cro-deal-desk` per sessione.
**Responsabile:** `cro-deal-desk`.
**Target:** >80% PASS al primo giro (qualità del brief e del lavoro A3).
**Cadenza:** mensile.

---

### KPI-CRO-011 — Deal in Memoria con Motivo Win/Loss (%)
**Metrica:** % di deal chiusi con campo `motivo` popolato in `cro-memoria`.
**Fonte dati:** `board/cro/deals/` — audit campi.
**Responsabile:** `cro-memoria` + `cro-conductor`.
**Target:** 100% — nessun apprendimento sprecato.

---

## Connessioni

- [[cro-conductor]] · `agenti/cro-conductor.md`
- [[cro-agency-pipeline]] · `agenti/cro-agency-pipeline.md`
- [[cro-forecast-analyst]] · `agenti/cro-forecast-analyst.md`
- [[cro-pipeline-health]] · `agenti/cro-pipeline-health.md`
- [[cro-retention-revenue]] · `agenti/cro-retention-revenue.md`
- [[cro-cross-sell-mapper]] · `agenti/cro-cross-sell-mapper.md`
- [[state/README]] · `company/Board-CSuite/CRO/state/README.md`
- [[CRO-v1]] · `company/Board-CSuite/CRO.md` §KPI
