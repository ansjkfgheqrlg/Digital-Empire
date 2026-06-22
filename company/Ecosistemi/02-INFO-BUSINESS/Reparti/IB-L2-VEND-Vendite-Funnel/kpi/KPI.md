---
Type: KPI
Status: Active
Tags: #kpi #vendite #funnel #evergreen #cro #IB-L2-VEND
Created: 2026-06-21
Last updated: 2026-06-21
---

# KPI — IB-L2-VEND Vendite & Funnel

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo funnel evergreen live (M1).
> Nessun numero inventato (Mandato Art.2 — prove non promesse).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Conversione evergreen | IB-VEND-TRACK + IB-VEND-CRO | % visitatori sales page evergreen → acquisto (loop 365gg) | [DM] — primo funnel live | [DM] — si stabilisce dopo M1-M2 |
| Opt-in rate lead magnet | IB-VEND-LEAD + IB-VEND-TRACK | % visitatori opt-in page → lead in lista email | [DM] | [DM] |
| AOV (Average Order Value) | IB-VEND-OFFER + IB-VEND-TRACK | Valore medio ordine incluso effetto order bump + upsell; numeri prezzo da catalogo B-003 | [DM] | [DM] — sale con take-rate bump/upsell |
| Email open rate (per email) | IB-VEND-SALESPAGE + IB-VEND-TRACK | % aperture per ogni email della sequenza nurture (5-7) | [DM] | [DM] |
| Revenue per lead | IB-VEND-TRACK | Revenue totale / n. lead in lista (efficienza del funnel) | [DM] | [DM] |
| Copertura tracking | IB-VEND-TRACK | % step funnel con evento configurato e verificato in debug | [DM] | 100% step tracciati |
| Test A/B chiusi con decisione | IB-VEND-CRO | N. test con campo `decisione` popolato (adottato/scartato); nessun test lasciato aperto | [DM] | 100% test chiusi con decisione |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate G-VEND bypass rate | IB-VEND-QA | N. output del reparto consegnati senza gate G-VEND / tot output | 0 (gate bloccante) |
| Prezzi non approvati in produzione | IB-VEND-QA | N. pagine live con prezzo non da catalogo B-003 approvato | 0 (vincolo B-002/B-003) |
| Copy non gated APSOC | IB-VEND-QA | N. sales page/email live con score APSOC <80/100 | 0 (G-VEND) |
| Scarcity artificiale rilevata | IB-VEND-QA | N. deadline finte / scarcity falsa sull'evergreen | 0 (Mandato Art.2 — FAIL automatico) |
| Test conclusi sotto campione minimo | IB-VEND-CRO | N. test dichiarati "conclusivi" prima del campione statistico minimo | 0 (Regola R5) |

---

## Come si misurano

- **Conversione, opt-in rate, AOV, open rate, revenue per lead:** prodotti da IB-VEND-TRACK
  leggendo gli eventi pixel/UTM e il report periodico in `infobusiness/vendite/tracking/report/`.
- **Copertura tracking:** verificata in debug mode da IB-VEND-TRACK prima di ogni go live (gate WF-SALESPAGE step 4).
- **Test A/B KPI:** da `infobusiness/vendite/funnel/tests/{test_id}.json` — ogni test ha `decisione`.
- **Gate KPI:** IB-VEND-QA registra ogni esito (PASS/FAIL) in `infobusiness/vendite/salespage/{prodotto_id}/qa_log.json`.

---

## Cadenza di revisione

- Loop CRO settimanale: IB-VEND-TRACK identifica lo step a conversione più bassa (WF-CRO-OTTIMIZZAZIONE).
- Conversione evergreen: 2 settimane dopo il go live (dati iniziali) + 30gg (dati stabili).
- Report di sintesi a ib-director: ad ogni debrief lancio + ogni funnel evergreen live.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace `infobusiness/vendite/` dove i KPI vengono scritti
- [[ib-vend-track]] · `agenti/ib-vend-track.md` — owner primario delle metriche di conversione
- [[ib-vend-qa]] · `agenti/ib-vend-qa.md` — presidia i KPI di qualità (gate G-VEND)
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-VEND — KPI area
