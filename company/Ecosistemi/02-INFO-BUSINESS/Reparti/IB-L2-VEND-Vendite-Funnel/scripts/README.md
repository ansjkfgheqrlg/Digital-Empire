---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #vendite #funnel #cro #tracking #IB-L2-VEND
Created: 2026-06-21
Last updated: 2026-06-21
---

# Script — IB-L2-VEND Vendite & Funnel

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da IB-COORD-VENDITE senza approvazione aggiuntiva.

---

## Script pianificati (build in V2)

### `offer-stack-builder.py`

**Scopo:** genera il template strutturato dell'offer stack (JSON) con i campi obbligatori —
value stack, bonus, garanzia, order bump, upsell, naming — lasciando i campi prezzo VUOTI e
marcati `attesa_B003`. IB-VEND-OFFER lo usa come scaffolding prima di recepire i numeri dal
catalogo approvato. Lo script NON inventa prezzi (vincolo B-002/B-003).

**Input:** `{prodotto_id, value_items[], bonus[], garanzia, bump_proposto, upsell_proposto}`
**Output:** `offer_stack.json` in `infobusiness/vendite/salespage/{prodotto_id}/` con campi prezzo `null` + flag `attesa_B003`.
**Prerequisiti:** nessuno — produce un template; i prezzi arrivano via `HC-B003-IB-VEND-01`.

---

### `step-conversion-analyzer.py`

**Scopo:** legge gli eventi di tracking (view → opt-in → email → click → checkout → purchase) e
calcola la conversione per ogni step, identificando lo step a conversione più bassa. Produce
input strutturato per IB-VEND-CRO (loop settimanale WF-CRO-OTTIMIZZAZIONE).

**Input:** `{funnel_id, periodo, eventi_config.json, eventi_raw.json}`
**Output:** `metriche_step.json` con `conversione_per_step[]`, `step_piu_debole`, `volume_per_step`
in `infobusiness/vendite/funnel/` — pronto per la formulazione dell'ipotesi CRO.
**Prerequisiti:** eventi tracciati e verificati in debug da IB-VEND-TRACK.

---

### `ab-sample-checker.py`

**Scopo:** dato un test A/B in corso e il volume di traffico per variante, calcola se il campione
minimo statistico è stato raggiunto. Restituisce un verdetto binario `campione_sufficiente`
che IB-VEND-CRO usa per non dichiarare conclusioni premature (Regola R5).

**Input:** `{test_id, variante_a_n, variante_b_n, conversioni_a, conversioni_b, mde_atteso}`
**Output:** `sample_check_{test_id}.json` con `campione_sufficiente: true|false`,
`n_minimo_richiesto`, `nota` — mai una decisione di adozione (quella resta umana/CRO).
**Prerequisiti:** test registrato in `infobusiness/vendite/funnel/tests/{test_id}.json`.

---

## Convenzioni

- Tutti gli script producono file in `infobusiness/vendite/` (namespace corretto) — mai fuori.
- Nessuno script inventa o pubblica prezzi: i campi prezzo restano `null`/`attesa_B003` finché B-003 non approva.
- Nessuno script fa chiamate API esterne autonome senza input esplicito dell'operatore.
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace `infobusiness/vendite/` su cui gli script scrivono
- [[WF-SALESPAGE]] · `workflow/WF-SALESPAGE.md` — usa `offer-stack-builder.py`
- [[WF-CRO-OTTIMIZZAZIONE]] · `workflow/WF-CRO-OTTIMIZZAZIONE.md` — usa `step-conversion-analyzer.py` + `ab-sample-checker.py`
- [[state/README]] · `state/README.md` — schema dei file di stato prodotti
