---
Type: KPI
Status: Active
Tags: #kpi #strategia #intelligence #backlog #roadmap #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# KPI — IB-L2-STRA Strategia & Intelligence

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo ciclo intelligence + prima roadmap.
> Nessun numero inventato (Mandato Art.2 "prove non promesse" + Regola R6 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Idee backlog con score ≥60 | IB-STRA-BACKLOG | N. idee candidabili (score ≥60, ≥1 fonte reale) in coda in `backlog/idee.json`; alimentano IB-L2-PROD | [DM] — primo ciclo | ≥3 idee candidabili sempre in coda |
| Lead time intelligence → idea validata → produzione | IB-COORD-STRATEGIA | Giorni dal segnale mercato (trend_YYYYMM) all'ingresso in WF-CORSO (IB-L2-PROD) | [DM] | [DM] — si stabilisce dopo 2-3 idee a regime |
| % prodotti a roadmap che arrivano a lancio nei tempi | IB-STRA-ROADMAP | N. prodotti lanciati nella finestra pianificata / tot prodotti a roadmap nel periodo | [DM] | aderenza roadmap senza slittamenti silenziosi |
| Aggiornamenti ICP per trimestre | IB-STRA-ICP | N. revisioni `icp_infobusiness.md` con dati freschi citati (no ICP fossile) | [DM] | ≥1 aggiornamento/trimestre con fonte |
| Idee con fonte verificata al gate QA | IB-STRA-QA | % idee proposte che superano G-FONTI senza rework (ogni claim ha fonte reale) | [DM] | progressivo — migliora col rigore |
| Dossier competitor aggiornati | IB-STRA-COMP | N. competitor con dossier `_YYYYMMDD.md` aggiornato nel trimestre (prezzi+posizionamento con data) | [DM] | copertura competitor core sempre <90gg |
| Buffer ≥30gg rispettato in roadmap | IB-STRA-ROADMAP | % coppie di lanci consecutivi con gap ≥30gg (lista recovery) in `roadmap_corrente.md` | [DM] | 100% — nessun lancio entro 30gg dal precedente |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate QA bypass rate | IB-STRA-QA | N. idee/roadmap consegnate senza gate IB-STRA-QA / tot output | 0 (gate bloccante) |
| Claim senza fonte rilevati al gate | IB-STRA-QA | N. claim di mercato/competitor senza fonte citata trovati in G-FONTI | 0 (Regola R1 — fonte obbligatoria) |
| Metriche stimate spacciate per reali | IB-STRA-QA | N. metriche stimate presentate senza etichetta [stima]/[DM] | 0 (R2 — violazione automatica) |
| Idee passate a PROD con score <60 | IB-COORD-STRATEGIA | N. handoff HC-STRA-PROD-01 con score <60 | 0 (R3 — soglia non negoziabile) |

---

## Come si misurano

- **Idee backlog e score:** conteggio da `infobusiness/strategia/backlog/idee.json` — ogni idea ha
  campo `score` e `fonti[]`. Idempotente: idee aggiornate, non duplicate.
- **Lead time:** calcolato dal `timestamp` del segnale in `intelligence/state.json` alla data
  di ingresso in WF-CORSO (IB-L2-PROD) — richiede handoff HC-STRA-PROD-01 datato.
- **% prodotti nei tempi e buffer:** da `roadmap/roadmap_corrente.md` confrontata con date di lancio reali
  ricevute da IB-L2-LANC; deriva tracciata in `roadmap_archivio/`.
- **KPI ICP:** da `icp_changelog.md` — ogni revisione ha trimestre + fonte dei dati.
- **KPI gate:** IB-STRA-QA registra ogni gate (PASS/FAIL + motivo) nello state del workflow corrispondente.

---

## Cadenza di revisione

- KPI backlog e gate: ad ogni ciclo WF-PRODUCT-INTELLIGENCE (mensile).
- KPI roadmap e buffer: ad ogni ciclo WF-ROADMAP-PRODOTTI (trimestrale) + dopo ogni lancio.
- KPI ICP: ad ogni aggiornamento profilo (almeno trimestrale).
- Report di sintesi a ib-director: ogni ciclo trimestrale completato.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace `infobusiness/strategia/` dove i KPI vengono letti
- [[ib-stra-qa-verificatore-strategia]] · `agenti/ib-stra-qa-verificatore-strategia.md` — presidia gate KPI
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md` — produce KPI backlog
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-STRA` — KPI area
