---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #infobusiness #prodotto #mkd #validazione #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# Script — IB-L2-PROD Produzione Prodotti

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da IB-COORD-PRODOTTO senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `idea_scorer.py` [TARGET-V2]

**Scopo:** calcola lo score /100 dell'idea prodotto sui 5 criteri di WF-VALIDAZIONE
(problema reale /20, raw disponibile /20, ICP chiaro /20, differenziazione /20, posizionamento DE /20)
a partire dal brief compilato. Produce il breakdown e il verdetto Gate 1 (≥60). IB-PROD-VALID lo usa
come scaffolding prima di avviare l'MVP test.

**Input:** `{idea_id, problema, raw_path, icp, differenziazione, posizionamento, evidenze[]}`
**Output:** `validazione/state.json` con `score`, `breakdown` per criterio, `gate_1` (PASS/FAIL).
**Prerequisiti:** nessuno — calcola sui campi del brief; non fa ricerca esterna.

---

### `content_forge_runner.py` [WRAPPA]

**Scopo:** orchestra la skill `content-forge` esistente sull'intera cartella raw → MKD, e produce
la checklist quantitativa atomi (n. sezioni fonte, n. atomi fonte, n. atomi MKD, rapporto espansione).
Wrappa il motore esistente (ADR-003), non lo riscrive. IB-PROD-MKD lo invoca; IB-PROD-QA legge la checklist.

**Input:** `{prodotto_id, raw_folder_path, brief_validato_path}`
**Output:** `corso/MKD-{prodotto}.md` + `corso/atomi-check-{prodotto}.json` con
`atomi_fonte`, `atomi_mkd`, `copertura_pct`, `rapporto_espansione`.
**Prerequisiti:** brief validato (WF-VALIDAZIONE PASS) + cartella raw accessibile.

---

### `smoke_test_runner.py` [TARGET-V2]

**Scopo:** esegue lo smoke test "studente fantasma" sul corso deployato: percorre il modulo 1
end-to-end (accesso, lezione, esercizio, progress tracking) e registra ogni errore/anomalia.
Supporto a IB-PROD-QA per il gate di deploy in WF-CORSO.

**Input:** `{prodotto_id, url_corso, credenziali_studente_fantasma, modulo_target}`
**Output:** `corso/smoke-test-{prodotto}.json` con lista check (PASS/FAIL), errori HTTP,
difetti rilevati e verdetto gate deploy.
**Prerequisiti:** corso deployato su piattaforma + credenziali studente di test (HC-PL-IB-01 completo).

---

## Convenzioni

- Tutti gli script producono file in `infobusiness/prod/` (namespace corretto) — mai fuori.
- Nessun script monta video, tocca il codice piattaforma o fa chiamate API esterne autonome (R3).
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace `infobusiness/prod` su cui gli script scrivono
- [[WF-VALIDAZIONE]] · `workflow/WF-VALIDAZIONE.md` — usa `idea_scorer.py`
- [[WF-CORSO]] · `workflow/WF-CORSO.md` — usa `content_forge_runner.py` + `smoke_test_runner.py`
- [[WF-EBOOK]] · `workflow/WF-EBOOK.md` — usa `content_forge_runner.py`
