---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #marketing-interno #proof #case-study #inbound #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# Script — A6 Marketing Interno & Proof

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da AG-A6-COORD senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `proof-intake.py`

**Scopo:** genera il template strutturato (JSON) per la raccolta proof a fine 90gg. Produce i
campi obbligatori (metriche con fonte, testimonianza, consenso) e pre-carica i dati già
documentati da A4-Delivery (`agency/kpi`) per ridurre il carico sul cliente. AG-A6-PROOF lo
usa come scaffolding prima di contattare il cliente.

**Input:** `{cliente, gate_delivery_status, riferimento_kpi_A4}`
**Output:** `proof_template_{cliente}.json` in `agency/a6/proof/{cliente}/`
**Prerequisiti:** Gate Delivery firmato; produce un template, non fa analisi.

---

### `case-study-scaffold.py`

**Scopo:** legge il proof verificato e produce lo scheletro APSOC del case study (sezioni A/P/S/O/C/CTA
vuote con i numeri reali già inseriti nella sezione C con la fonte). AG-A6-CASE compila la
narrazione; lo script garantisce che ogni numero presente abbia il campo `fonte` popolato
(blocca lo scaffold se un numero arriva senza fonte).

**Input:** `{cliente, proof_status, metriche[] (ognuna con fonte), testimonianza, servizio}`
**Output:** `case_study_{case_id}_scaffold.md` + `state.json` in `agency/a6/case-studies/{case_id}/`
**Prerequisiti:** proof verificato da AG-A6-PROOF; rifiuta numeri senza fonte (R1).

---

### `inbound-attribution.py`

**Scopo:** legge i dati di tracking (06-PLATFORM/04-MARKETING) e attribuisce ogni lead a inbound
(landing/presentazione) o outreach, calcolando il tasso di conversione visita → call per asset
della vetrina. Produce input per AG-A6-INBOUND. Se il tracking non è disponibile → emette
baseline [DM], non un numero stimato.

**Input:** `{periodo, dati_tracking.json, asset_vetrina[], case_study_pubblicati[]}`
**Output:** `inbound_{periodo}.json` con `lead_inbound`, `tasso_conversione`, `drop_identificati`,
`ottimizzazioni_suggerite` — pronto per WF-ASSET-VETRINA.
**Prerequisiti:** richiede dati di tracking; assenti → output con campi [DM].

---

## Convenzioni

- Tutti gli script producono file in `agency/a6/` (namespace corretto) — mai fuori.
- Nessuno script fa chiamate API esterne autonome senza input esplicito dell'operatore.
- Nessuno script inserisce un numero senza campo `fonte` (R1 — prove non promesse).
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria su cui i script scrivono
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md` — usa `proof-intake.py` e `case-study-scaffold.py`
- [[WF-ASSET-VETRINA]] · `workflow/WF-ASSET-VETRINA.md` — usa `inbound-attribution.py`
- [[state/README]] · `state/README.md` — schema dei file di stato prodotti
