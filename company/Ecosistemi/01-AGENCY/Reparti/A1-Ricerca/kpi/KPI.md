---
Type: KPI
Status: Active
Tags: #kpi #ricerca #lead #intelligence #agency #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# KPI — A1 Ricerca & Market Intelligence

> Metriche del reparto. Baseline storica: [DM] — da misurare alle prime run reali.
> Nessun numero inventato (Mandato Art.2 + principio P3 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Lead qualificati/gg | AG-A1-QUAL | N. lead con score ≥ soglia inseriti in leads.db al giorno | [DM] — prima run | [DM] — si stabilisce dopo M1 |
| % qualifica su scraped | AG-A1-QUAL | Lead qualificati / totale raccolti per run | [DM] | [DM] — migliora con calibrazione ICP |
| Freschezza dati media | AG-A1-QA | Età media dei dati lead al momento dell'outreach | [DM] | [DM] — soglia da definire con A2 |
| Dossier pre-call entro SLA | AG-A1-BRIEF | % dossier consegnati ad A8 ≥2h prima della call | [DM] | 100% entro SLA |
| Report nicchia con fonti verificabili | AG-A1-INTEL | % report con campo `fonti[]` non vuoto e link verificabili | [DM] | 100% (Mandato Art.2) |
| ICP aggiornati per nicchia attiva | AG-A1-ICP | N. nicchie attive con profilo ICP aggiornato nel periodo | [DM] | 1 per nicchia attiva |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate bypass rate | AG-A1-QA | N. output A1 consegnati senza gate QA / tot output | 0 (Mandato Art.4.1) |
| Lead duplicati in leads.db | AG-A1-QA | N. duplicati rilevati post-store (dedup mancato) | 0 |
| Metriche intel inventate | AG-A1-QA | N. report con metrica senza fonte citata | 0 (Regola R4) |
| Scraping senza ICP esplicito | AG-A1-COORD | N. run avviate su nicchia nuova senza profilo ICP | 0 (Regola R2) |

---

## Come si misurano

- **Lead KPI:** da `leads.db` + namespace `agency/leads` — conteggio per run/giorno.
  `qualifier.py` produce lo score; AG-A1-QUAL aggrega.
- **Freschezza dati:** timestamp di scraping vs timestamp di outreach (handoff ad A2).
- **Dossier SLA:** timestamp di consegna del dossier vs orario della discovery call (da A8).
- **Intel KPI:** da `agency/a1/intel` — ogni report ha il campo `fonti[]`. AG-A1-QA verifica.
- **Gate KPI:** AG-A1-QA registra ogni gate (PASS/FAIL) nello `state.json` della run.

---

## Cadenza di revisione

- Lead KPI: ad ogni run di sourcing (giornaliera se schedulata).
- Report nicchia: settimanale (cadenza WF-MARKET-INTEL).
- Report di sintesi ad AG-DIR: ogni ciclo di reparto completato.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §6` — namespace dove i KPI vengono scritti
- [[ag-a1-qa]] · `agenti/ag-a1-qa.md` — presidia i gate e i KPI di qualità
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1` — KPI di reparto
