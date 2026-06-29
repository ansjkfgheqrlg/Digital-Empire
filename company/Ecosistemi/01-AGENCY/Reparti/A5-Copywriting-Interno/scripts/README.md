---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #agency #copywriting #refresh #obiezioni #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# Script — A5 Copywriting Interno

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da AG-A5-COORD senza approvazione aggiuntiva.
> **Il Gate Bibbia NON è uno script di A5:** è il motore `bibbia_team.py` condiviso con A2
> (pattern 6, ADR-003). A5 lo invoca via la pipeline esistente, non lo riscrive qui.

---

## Script pianificati (build in V2)

### `reply-rate-analyzer.py`

**Scopo:** legge i dati di performance per variante da `agency/outreach` e produce il trend del
reply rate per template/canale negli ultimi 30 giorni, con flag dei template sotto baseline per
2 cicli. Supporto a AG-A5-LEARN per il trigger di WF-COPY-REFRESH.

**Input:** `{canale, periodo, performance_outreach.json}`
**Output:** `reply_rate_report.json` con `template`, `trend`, `sotto_baseline`, `diagnosi_candidata`
**Prerequisiti:** dati reali in `agency/outreach` — se assenti, output `[DM]` (no numero inventato).

---

### `variant-ab-comparator.py`

**Scopo:** confronta le varianti A/B post-rollout (controllo vs varianti) sui dati reali e
determina se il campione è sufficiente per un verdetto. Produce winner/inconclusivo con il
volume osservato. Supporto a AG-A5-LEARN nello STEP 7 di WF-COPY-REFRESH.

**Input:** `{refresh_id, varianti[], controllo, dati_reply_per_variante}`
**Output:** `ab_verdetto.json` con `verdetto`, `campione_sufficiente`, `variante_adottabile`
**Prerequisiti:** dati reply reali per variante; senza campione sufficiente → `inconclusivo`.

---

### `objection-coverage-checker.py`

**Scopo:** verifica la copertura della libreria obiezioni per una nicchia: quali obiezioni
ricorrenti hanno almeno una risposta `validata`, quali sono ancora `non_validata`. Supporto a
AG-A5-OBJ e gate G2 di WF-SCRIPT-CALL.

**Input:** `{nicchia, libreria_obiezioni.json}`
**Output:** `coverage_report.json` con `obiezioni_validate`, `gap`, `non_validate_residue`
**Prerequisiti:** `agency/a5/obiezioni` popolato (anche solo parzialmente).

---

## Convenzioni

- Tutti gli script producono file in `agency/a5/` (namespace corretto) — mai fuori.
- Nessuno script fa chiamate API esterne autonome senza input esplicito dell'operatore.
- Nessuno script duplica il Gate Bibbia: il gate è il motore condiviso di A2 (pattern 6).
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace memoria su cui gli script scrivono
- [[WF-COPY-REFRESH]] · `workflow/WF-COPY-REFRESH.md` — usa `reply-rate-analyzer.py` e `variant-ab-comparator.py`
- [[WF-SCRIPT-CALL]] · `workflow/WF-SCRIPT-CALL.md` — usa `objection-coverage-checker.py`
- [[ag-a2-qa]] · `../A2-Acquisizione/agenti/ag-a2-qa.md` — motore Gate Bibbia (non duplicato qui)
