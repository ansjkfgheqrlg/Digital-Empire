---
Type: KPI
Status: Active
Tags: #kpi #agency #preventivi #winrate #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# KPI — A3 Preventivi

> Metriche del reparto. Baseline storica: [DM] — win rate misurato dal giorno 1.
> Nessun numero inventato (Mandato Art.2 + principio P5 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Tempo call→preventivo | AG-A3-COORD | Ore tra disponibilità trascrizione call e invio proposta | [DM] | ≤48h |
| Win rate | AG-A3-COORD + AG-A3-FUP | N. proposte firmate / N. proposte inviate nel periodo | [DM] — dal giorno 1 | [DM] — si stabilisce dopo M1-M2 |
| Valore medio preventivo | AG-A3-COORD | Media valore proposte inviate (catalogo: 4.000/3.500/2.500/8.000 €) | [DM] | [DM] |
| Gate Preventivo PASS al primo tentativo | AG-A3-QA | % proposte che superano AG-A3-QA senza rework | [DM] | progressivo — migliora col volume |
| Preventivi chiusi con esito entro D+10 | AG-A3-FUP | % preventivi con esito win/loss entro 10gg dall'invio | [DM] | 100% chiusi con esito |
| Loss con motivo registrato | AG-A3-LEARN | % loss con campo `causa` popolato in `agency/reasoning` | [DM] | 100% loss documentati |
| Loss pattern mensile | AG-A3-LEARN | N. report WF-LOSS-ANALYSIS prodotti per ciclo (con pattern ≥5) | [DM] | 1 report/mese |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate bypass rate | AG-A3-QA | N. proposte inviate senza gate AG-A3-QA / tot proposte | 0 |
| Sconti/prezzi fuori catalogo | AG-A3-QA | N. proposte con prezzo o sconto non a catalogo (B-003) | 0 (R3 — violazione automatica) |
| Promesse senza prova | AG-A3-QA | N. proposte con claim non verificabile rilevati in gate | 0 (R5 — Mandato Art.2) |
| Documenti non problem-first | AG-A3-QA | N. proposte che NON aprono col problema del cliente | 0 (R4 — FAIL automatico) |

---

## Come si misurano

- **Tempo call→preventivo:** da `agency/03-preventivi/{id}` — differenza tra `data_invio` e timestamp
  disponibilità trascrizione. Calcolo automatico o manuale da AG-A3-COORD.
- **Win rate e valore medio:** da `agency/03-preventivi/` — conteggio esiti `win` / `inviato` e media
  del campo `prezzo` (sempre a catalogo).
- **Gate KPI:** AG-A3-QA registra ogni esito gate (PASS/FAIL) nel `state.json` del preventivo.
- **Loss KPI:** da `agency/reasoning` — ogni record di loss ha il campo `causa`; WF-LOSS-ANALYSIS
  aggrega e produce il loss pattern mensile.

---

## Cadenza di revisione

- KPI di pipeline (tempo, gate): ad ogni preventivo chiuso.
- Win rate e valore medio: settimanale + sintesi mensile ad AG-DIR.
- Loss pattern: mensile (WF-LOSS-ANALYSIS) → A5 + 08-INTELLIGENCE.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria dove i KPI vengono scritti
- [[ag-a3-qa]] · `agenti/ag-a3-qa.md` — presidia i gate KPI di qualità
- [[ag-a3-learn]] · `agenti/ag-a3-learn.md` — produce i loss KPI
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3` — KPI di reparto
