---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #lanci #campagne #launch #calendario #IB-L2-LANC
Created: 2026-06-21
Last updated: 2026-06-21
---

# Script — IB-L2-LANC Lanci & Campagne

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da IB-COORD-LANCI senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `launch_calendar.py`

**Scopo:** genera il calendario T-30→T+7 deterministico a partire dai parametri del lancio.
Produce la timeline con date assolute, owner per task, dipendenze e gate per ogni step (T-30
planner, T-28 INT, T-21 CF, T-14 MK+gate APSOC, T-7 copy, T-3 asset, T-1 dry-run, T-0-ε go/no-go,
T0→T+4/6 cart open, ultime 48h cart close, T+7 debrief). IB-LANC-PLANNER lo usa come scaffolding.

**Input:** `{lancio_id, prodotto, data_cart_open, durata_cart_giorni, webinar (bool), owner_map}`
**Output:** `calendario.md` + `state.json` (scheletro step) in `infobusiness/lanci/{lancio_id}/`
**Prerequisiti:** nessuno — produce un calendario, non fa analisi.

---

### `dry_run_costs.py`

**Scopo:** consolida la stima costi del dry-run a T-1 (ads, tool, bonus) e calcola il delta vs
budget approvato da 09-OPERATIONS. Produce flag PASS/BLOCK secondo R6 (delta >10% → BLOCK) come
input strutturato per il go/no-go. IB-LANC-DRY lo usa in WF-LANCIO step T-1.

**Input:** `{lancio_id, costo_ads_stimato, costo_tool, costo_bonus, budget_approvato_OPS}`
**Output:** `dry-run.md` (sezione costi) con `totale_stimato`, `delta_vs_budget_%`,
`verdetto_budget` (PASS | BLOCK) — pronto per essere allegato al verbale go/no-go.
**Prerequisiti:** richiede budget approvato da 09-OPERATIONS in input.

---

### `launch_debrief_diff.py`

**Scopo:** calcola lo scarto piano vs reale per ogni KPI del lancio (conversione per step,
n. acquirenti, AOV, delta budget) leggendo il piano dal calendario e i numeri reali dal tracking.
Marca ogni scarto ≥10% come `richiede_root_cause`. Supporto a IB-LANC-DEBRIEF in WF-DEBRIEF-LANCIO.

**Input:** `{lancio_id, calendario.md, tracking_reale.json, dry-run.md, costo_reale}`
**Output:** `debrief_diff.json` con per-KPI `pianificato`, `reale`, `delta_%`,
`richiede_root_cause` (bool) — template per i ≥3 pattern che DEBRIEF completa manualmente.
**Prerequisiti:** richiede tracking reale post cart close + calendario del lancio.

---

## Convenzioni

- Tutti gli script producono file in `infobusiness/lanci/` (namespace corretto) — mai fuori.
- Nessun script fa chiamate API esterne autonome senza input esplicito dell'operatore.
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni del lancio.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria su cui gli script scrivono
- [[WF-LANCIO]] · `workflow/WF-LANCIO.md` — usa `launch_calendar.py` e `dry_run_costs.py`
- [[state/README]] · `state/README.md` — schema JSON degli output degli script
