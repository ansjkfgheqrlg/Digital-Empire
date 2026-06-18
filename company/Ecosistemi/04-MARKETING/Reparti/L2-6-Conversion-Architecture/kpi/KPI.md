---
Type: KPI
Status: Active
Tags: #kpi #conversion #funnel #cro #marketing #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — L2.6 Conversion Architecture

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo funnel live.
> Nessun numero inventato (Mandato Art.2 + principio P3 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Funnel conversion rate per stage | CONV-LEAD + AN5 | Drop rate per sezione APSOC nel funnel (ToFu→MoFu→BoFu); da AN5 post-launch | [DM] — primo funnel live | [DM] — si stabilisce dopo M1-M2 |
| Micro-conversion rate per landing | CA3 + AN5 | Tasso di completamento degli eventi critici (scroll_50, form_view, form_submit, cta_click) per ogni landing | [DM] | [DM] |
| Sprint CRO chiusi con verdetto | CA4 | N. sprint con campo `verdetto` popolato (winner o inconclusivo) nel periodo; target qualità = nessuno sprint lasciato aperto senza verdetto | [DM] | 100% sprint chiusi con verdetto |
| Audit landing completati con 3 azioni | CA-QA | N. audit in `marketing/cro/audits/` con campo `azioni_prioritarie` con 3 azioni complete (elemento + impatto + tipo intervento) | [DM] | 100% audit con 3 azioni |
| Gate CA-QA PASS al primo tentativo | CA-QA | % funnel design che passano il gate CA-QA senza cicli di rework | [DM] | progressivo — migliora col volume |
| Brief tecnici accettati da 06-PLATFORM al primo invio | CONV-LEAD | % brief tecnici accettati da 06-PLATFORM senza richiesta di completamento | [DM] | target qualità struttura |
| Funnel riusati da archivio (efficienza) | CONV-LEAD | % funnel che riusano architettura esistente da `marketing/cro/funnels/` vs progettati ex novo | [DM] | cresce col volume di funnel archiviati |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate bypass rate | CA-QA | N. output L2.6 consegnati senza gate CA-QA / tot output | 0 (Mandato Art.4.1) |
| Sprint avviati senza segnale drop AN5 | CA4 | N. sprint avviati su opinione senza report AN5 / tot sprint | 0 (Regola R3) |
| Copy non gated in produzione | CA-QA | N. landing con copy non gated (score <80/85) | 0 |
| P prima di S violazioni | CA-QA | N. funnel con S prima di P rilevati in gate | 0 (R5 — violazione automatica) |

---

## Come si misurano

- **Funnel conversion rate e micro-conversion rate:** letti da AN5 (L2.4) post-lancio.
  L2.6 riceve i report di AN5, non li produce direttamente.
- **Sprint KPI:** da `marketing/cro/sprints/` — conteggio automatico con `drop-rate-analyzer.py`
  (quando disponibile) o manuale da CONV-LEAD.
- **Audit KPI:** da `marketing/cro/audits/` — ogni file di audit ha il campo `azioni_prioritarie`.
- **Gate KPI:** CA-QA registra ogni gate (PASS/FAIL) nel `state.json` del funnel corrispondente.
  MKT-Conductor o AN-OBSERVER (L2.4) possono aggregare per report di ecosistema.

---

## Cadenza di revisione

- Sprint KPI: ad ogni sprint chiuso.
- Funnel conversion rate: 2 settimane dopo il lancio (dati iniziali) + 30gg (dati stabili).
- Report di sintesi al CMO: ogni ciclo di reparto completato (almeno 1 funnel live).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria dove i KPI vengono scritti
- [[ca-qa-conversion-verifier]] · `agenti/ca-qa-conversion-verifier.md` — presidia gate KPI
- [[L2-4-Analytics]] · AN5 è il fornitore primario dei dati di conversion rate e drop rate
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §7.2` — KPI ecosistema
