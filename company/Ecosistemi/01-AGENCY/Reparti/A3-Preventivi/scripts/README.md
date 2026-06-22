---
Type: SCRIPTS
Status: Mixed (wrapper attivo + target V2)
Tags: #scripts #agency #preventivi #audit #wrapper #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# Script — A3 Preventivi

> Script di supporto del reparto. Uno wrappa un asset esistente (ADR-003: wrap, mai riscrittura);
> gli altri sono target V2. Standard: input strutturato, output JSON/MD, nessun side-effect senza
> input esplicito, nessuna spesa API autonoma, eseguibili da AG-A3-COORD senza approvazione aggiuntiva.

---

## Script wrappati (attivi — ADR-003)

### `cro_audit.py` [WRAPPA-ESISTENTE]

**Scopo:** audit tecnico deterministico di un sito/landing del cliente per quantificare le criticità
di conversione. È un asset esistente: A3 lo **invoca come servizio**, non lo riscrive (ADR-003).
Usato da AG-A3-AUDIT nello Step 2 di `WF-PREVENTIVO` quando il problema riguarda sito/conversione.

**Input:** `{url_sito, icp (opzionale)}`
**Output:** report criticità CRO (JSON/MD) → input per la quantificazione del problema di AG-A3-AUDIT.
**Prerequisiti:** URL del sito disponibile e accessibile. Se non applicabile (problema operativo,
non di sito) → AG-A3-AUDIT lo salta dichiarando lo skip e procede con `market-audit` + dato cliente.
**Vincolo:** nessuna modifica al codice dell'asset esistente; solo invocazione con input strutturato.

---

## Script pianificati (build in V2)

### `preventivo-state-init.py`

**Scopo:** inizializza il `state.json` di un nuovo preventivo in `agency/03-preventivi/{id}/` con i
campi obbligatori vuoti (id, lead, prodotto, esito_gate, data_invio, stato, last_updated). AG-A3-COORD
lo usa come scaffolding allo Step 0 di `WF-PREVENTIVO`.

**Input:** `{lead_id, call_source}`
**Output:** `state.json` con stato iniziale `in_lavorazione` in `agency/03-preventivi/{id}/`.
**Prerequisiti:** nessuno — produce un template, non fa analisi.

---

### `followup-scheduler.py`

**Scopo:** dato il `data_invio`, calcola le date dei 3 touch (D+3, D+7, D+10) e produce il piano di
follow-up per AG-A3-FUP. Non invia nulla: produce solo la schedulazione (gli invii restano azioni esplicite).

**Input:** `{preventivo_id, data_invio}`
**Output:** `followup_plan.json` con le 3 date touch → usato da `WF-FOLLOWUP-COMMERCIALE`.
**Prerequisiti:** preventivo in stato `inviato`.

---

### `loss-pattern-aggregator.py`

**Scopo:** legge i record di loss in `agency/reasoning` nella finestra 30gg e raggruppa per
categoria × nicchia, applicando la soglia statistica (significativo ≥5, nessuna conclusione n < 3).
Produce l'input strutturato per il report di `WF-LOSS-ANALYSIS`.

**Input:** `{periodo: "30gg"}`
**Output:** `loss_aggregato.json` con pattern significativi/emergenti + conteggi → usato da AG-A3-LEARN.
**Prerequisiti:** record loss con campo `causa` popolato (Regola R7).

---

## Convenzioni

- Tutti gli script producono file in `agency/03-preventivi/` o `agency/reasoning` — mai fuori.
- Nessuno script invia comunicazioni o fa chiamate API esterne autonome senza input esplicito.
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- `cro_audit.py` è wrappato, non modificato (ADR-003): si invoca, non si riscrive.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria su cui gli script scrivono
- [[ag-a3-audit]] · `agenti/ag-a3-audit.md` — invoca `cro_audit.py` (wrapper)
- [[WF-PREVENTIVO]] · `workflow/WF-PREVENTIVO.md` — usa `preventivo-state-init.py` + `cro_audit.py`
- [[WF-LOSS-ANALYSIS]] · `workflow/WF-LOSS-ANALYSIS.md` — usa `loss-pattern-aggregator.py`
