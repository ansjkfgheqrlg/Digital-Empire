---
Type: KPI
Status: Active
Tags: #kpi #lanci #campagne #launch #infobusiness #IB-L2-LANC
Created: 2026-06-21
Last updated: 2026-06-21
---

# KPI — IB-L2-LANC Lanci & Campagne

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo lancio live.
> Nessun numero inventato (Mandato Art.2 + principio P5 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Aderenza calendario | IB-LANC-PLANNER + IB-COORD-LANCI | % task del calendario T-30→T+7 completati entro la data pianificata; letta da `calendario.md` + `state.json` | [DM] — primo lancio live | ≥90% task on-time |
| Conversione lancio | IB-LANC-TRACKER | % lista email → acquisto durante cart open; da `tracking/` per step (opt-in→click→checkout→acquisto) | [DM] | [DM] — si stabilisce dopo 1-2 lanci |
| Scarto piano vs reale per step | IB-LANC-DEBRIEF | delta % tra KPI pianificato e KPI reale per ogni step del funnel di lancio | [DM] | ogni scarto ≥10% ha root cause nel debrief |
| Delta budget dry-run | IB-LANC-DRY | scostamento % tra stima costi a T-1 e costo reale post-lancio | [DM] | <10% (oltre soglia → blocco go/no-go, R6) |
| Pattern ReasoningBank per lancio | IB-LANC-DEBRIEF | n. pattern distillati e validati scritti in `reasoningbank/` per lancio | [DM] | ≥3 pattern per lancio (gate WF-DEBRIEF-LANCIO) |
| Copy gated APSOC al primo invio | IB-LANC-COPY-LIAISON | % asset rientrati da 04-MARKETING con APSOC ≥80 (≥85 sales page) senza rework | [DM] | target qualità handoff HC-IB-MK-01 |
| Lanci con go/no-go formale registrato | IB-COORD-LANCI | % lanci con verbale `go-nogo.md` (consensus 5 voci) completo prima di T0 | [DM] | 100% lanci con go/no-go registrato |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate bypass rate | IB-LANC-QA | N. output lancio consegnati senza gate IB-LANC-QA / tot output | 0 (gate bloccante R4) |
| Lanci partiti senza dry-run | IB-LANC-DRY | N. lanci con cart open senza `dry-run.md` a T-1 / tot lanci | 0 (R5 — dry-run obbligatorio) |
| Copy non gated in produzione | IB-LANC-QA | N. asset live con copy non gated (APSOC <80) | 0 |
| Scarcity non verificabile pubblicata | IB-LANC-QA | N. deadline/bonus a scadenza non reali rilevati | 0 (R3 — Mandato Art.2) |
| Lanci senza prodotto a gate PASS | IB-COORD-LANCI | N. lanci avviati senza prodotto WF-CORSO/WF-EBOOK PASS | 0 (R1 — prerequisito di avvio) |

---

## Come si misurano

- **Aderenza calendario:** confronto `calendario.md` (date pianificate) vs `state.json` (timestamp reali) —
  conteggio con `launch_calendar.py` (quando disponibile) o manuale da IB-LANC-PLANNER.
- **Conversione lancio e scarto per step:** letti da `tracking/` (report giornalieri IB-LANC-TRACKER)
  post cart open. IB-LANC-DEBRIEF consolida a T+7 in `debrief.md`.
- **Delta budget dry-run:** confronto stima `dry-run.md` (T-1) vs costo reale post-lancio (DEBRIEF).
- **Pattern ReasoningBank:** conteggio voci distillate in `reasoningbank/` per lancio.
- **Gate KPI:** IB-LANC-QA registra ogni gate (PASS/FAIL) nello `state.json` del lancio corrispondente.
  ib-director aggrega per report di ecosistema.

---

## Cadenza di revisione

- KPI di step (conversione, tracking): ogni 24h durante cart open (IB-LANC-TRACKER).
- Scarto piano vs reale + pattern ReasoningBank: a T+7, in fase di debrief (gate di uscita WF-DEBRIEF-LANCIO).
- Delta budget: a chiusura cart, confronto stima vs reale.
- Report di sintesi a ib-director: a ogni lancio chiuso (con update CATALOGO).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria dove i KPI vengono scritti
- [[IB-LANC-QA]] · `agenti/IB-LANC-QA.md` — presidia i gate KPI (copy/asset/dry-run)
- [[IB-LANC-DEBRIEF]] · `agenti/IB-LANC-DEBRIEF.md` — consolida scarto piano vs reale e pattern
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-LANC — KPI area
