---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #funnel #cro #analytics #conversion #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# Script — L2.6 Conversion Architecture

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da CONV-LEAD senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `funnel-mapper.py`

**Scopo:** genera la stage map strutturata (JSON) a partire dal brief del committente.
Produce il template vuoto con i campi obbligatori per ogni stage (obiettivo APSOC, canale,
brief copy, brief email, landing flag). CA1 lo usa come scaffolding prima di compilare
il contenuto analitico.

**Input:** `{committente, prodotto, obiettivo, awareness_level, n_stage_ipotizzato}`
**Output:** `stage_map_template.json` in `marketing/cro/funnels/{funnel_id}/`
**Prerequisiti:** nessuno — produce un template, non fa analisi.

---

### `drop-rate-analyzer.py`

**Scopo:** legge il report di AN5 (drop rate per evento) e produce una diagnosi testuale
mappando ogni drop sulla sezione APSOC correlata secondo lo schema CA3. Produce input
strutturato per CA4 (diagnosi collo di bottiglia).

**Input:** `{funnel_id, landing_id, drop_report_AN5.json, micro_conversion_schema_CA3.json}`
**Output:** `sprint_input.json` con `collo_di_bottiglia`, `sezione_APSOC_correlata`,
`ipotesi_candidata` — pronto per essere passato a WF-CRO-SPRINT.
**Prerequisiti:** richiede schema CA3 + drop report AN5.

---

### `landing-audit-checklist.py`

**Scopo:** esegue il check strutturale APSOC su una lista di sezioni della landing
(input: lista sezioni nell'ordine attuale) e produce il report diagnostico delle 4 dimensioni
(APSOC, micro-conversioni, performance, mobile) con flag PASS/FAIL per ogni check.
Supporto a CA-QA in WF-LANDING-AUDIT.

**Input:** `{url_landing, sezioni_attuali[], obiettivo_originale, icp, dati_AN5 (opzionale)}`
**Output:** `audit_{audit_id}.json` con check APSOC + lista issue per dimensione +
template per 3 azioni prioritarie (CA-QA completa il campo impatto stimato).
**Prerequisiti:** struttura sezioni della landing disponibile (estratta manualmente o via
parsing HTML con permesso committente).

---

## Convenzioni

- Tutti gli script producono file in `marketing/cro/` (namespace corretto) — mai fuori.
- Nessun script fa chiamate API esterne autonome senza input esplicito dell'operatore.
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria su cui i script scrivono
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md` — usa `funnel-mapper.py`
- [[WF-CRO-SPRINT]] · `workflow/WF-CRO-SPRINT.md` — usa `drop-rate-analyzer.py`
- [[WF-LANDING-AUDIT]] · `workflow/WF-LANDING-AUDIT.md` — usa `landing-audit-checklist.py`
