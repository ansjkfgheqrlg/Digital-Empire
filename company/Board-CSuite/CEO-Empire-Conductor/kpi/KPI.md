---
Type: CONCEPT
Status: Active
Tags: #ceo #kpi #governance #misure
Created: 2026-06-17
Last updated: 2026-06-17
---

# KPI — Indicatori Presidiati dalla Figura CEO / Empire-Conductor

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CEO.md` §KPI
> Principio: KPI "da misurare" — nessun numero inventato (Mandato Art.2 / MAXIMILIAN standard)
> Connessioni: [[ceo-okr-tracker]] · [[ceo-verificatore]] · [[WF-REVIEW-TRIMESTRALE]]

---

## Nota metodologica

I KPI elencati qui sono quelli che la figura CEO è responsabile di presidiare. I valori target
sono dichiarati come "da misurare" (DM) finché non esistono dati reali raccolti sul campo.
Il tag [DM] indica che la misurazione deve essere attivata prima di assegnare un target numerico.
La fonte del dato (dove si trova lo stato da leggere) è indicata per ogni KPI.

---

## KPI 1 — Decisioni cross-ecosistema chiuse senza stallo

**Cosa misura:** quante decisioni cross-ecosistema vengono portate a chiusura senza richiedere
il voto decisivo del conductor (stallo). L'assenza di stallo indica che il conductor propone
decisioni con consenso sufficiente prima del voto.

**Come si misura:** conteggio sessioni Board con `voto.esito = "approvata"` vs. `voto.esito =
"stallo_risolto_dal_conductor"`. Fonte: `state/direttive-dispatch/*.json` (campo voto).

**Target:** [DM] — da misurare su prime 10 sessioni Board; poi definire il target in WF-REVIEW-TRIMESTRALE.

**Frequenza:** per sessione Board.

---

## KPI 2 — Tempo proposta → decisione chiusa

**Cosa misura:** il tempo tra la ricezione dell'input decisionale e la chiusura della decisione
(checkpoint scritto + gate Mandato pass). Misura la velocità del processo decisionale.

**Come si misura:** `timestamp_output - timestamp_input` per ogni decisione nel log
`scripts/logs/dispatch_YYYYMMDD.log`. Aggregato: mediana e 90° percentile.

**Target:** [DM] — da misurare su prime 20 decisioni; l'obiettivo è < 1 sessione Board per decisioni
non straordinarie (dal v1 `CEO-Empire-Conductor.md`).

**Frequenza:** per decisione; report aggregato settimanale.

---

## KPI 3 — % decisioni architetturali con ADR scritto

**Cosa misura:** la percentuale di decisioni classificate come "architetturali" (impattano struttura,
workflow, regole) che hanno prodotto un ADR in `company/Memory/decisions/`.

**Come si misura:** n. ADR prodotti nello stato / n. decisioni con `tipo = "architetturale"` nel
log `checkpoint_writer.py`. Confronto tra i due conteggi.

**Target:** 100% — ogni decisione architetturale deve avere ADR. Non è negoziabile (ADR-002).

**Frequenza:** per decisione architetturale; report in WF-REVIEW-TRIMESTRALE.

---

## KPI 4 — % direttive eseguite entro deadline (tasso di esecuzione)

**Cosa misura:** la percentuale di handoff contract dispatched dal CEO che vengono completati
entro la deadline dichiarata con acceptance criteria soddisfatti.

**Come si misura:** n. handoff con stato "completato_verificato" / n. handoff totali dispatched
(da `state/direttive-dispatch/*.json`). Il verificatore aggiorna gli stati.

**Target:** [DM] — target iniziale: > 80%. Da calibrare dopo 1 trimestre di dati reali.

**Frequenza:** settimanale (report `board_report.py`); trimestrale per trend.

---

## KPI 5 — Coerenza ADR (0 contraddizioni attive)

**Cosa misura:** il numero di contraddizioni tra ADR attivi identificate dal contradiction check
della skill `decision-record`. L'obiettivo è sempre 0: nessun ADR attivo deve contraddirne un altro.

**Come si misura:** conteggio output `contradiction_check = "CONTRADDIZIONE con ADR-X"` nel log
di `checkpoint_writer.py`. Ogni contraddizione deve essere risolta prima di procedere.

**Target:** 0 contraddizioni attive. Ogni contraddizione identificata è un'anomalia da risolvere
nella stessa sessione in cui viene rilevata.

**Frequenza:** per ogni scrittura ADR; report trimestrale.

---

## KPI 6 — Checkpoint dopo ogni sessione Board

**Cosa misura:** la percentuale di sessioni Board che terminano con un checkpoint scritto in
`company/Memory/checkpoints/`. Misura la disciplina documentale della figura.

**Come si misura:** n. sessioni Board con CP del giorno / n. sessioni Board totali. Fonte:
file in `company/Memory/checkpoints/` con data corrispondente alle sessioni Board (da calendario
o da log `ceo-memoria`).

**Target:** 100% — ogni sessione Board produce un checkpoint. Non è negoziabile (ADR-002).

**Frequenza:** per sessione; report settimanale.

---

## KPI 7 — Fasi roadmap aperte senza gate verde della precedente

**Cosa misura:** il numero di fasi F1→F9+ di `PIANO-MAESTRO/08-ROADMAP-FASI.md` che sono "aperte"
(in corso o avviate) senza che la fase precedente abbia superato il proprio gate verde.

**Come si misura:** lettura di `08-ROADMAP-FASI.md` (stato di ogni fase) e verifica della catena
di gate. Eseguita da `ceo-conductor` in apertura di ogni WF-REVIEW-TRIMESTRALE.

**Target:** 0 — mai aprire una fase senza gate verde della precedente.

**Frequenza:** per review trimestrale; alert immediato se violato.

---

## KPI 8 — % OKR con progress report aggiornato

**Cosa misura:** la percentuale di OKR trimestrali che hanno ricevuto un progress report dall'ecosistema
owner entro i 7 giorni precedenti l'ultima raccolta.

**Come si misura:** n. OKR con `data_aggiornamento` ≤ 7 giorni / tot OKR in
`state/okr-trimestre/okr_correnti.json`. Calcolato da `collect_kpi_report.py`.

**Target:** [DM] — obiettivo iniziale: > 85%. Ecosistemi che non rispondono sono flaggati.

**Frequenza:** settimanale (ciclo `ceo-okr-tracker`).

---

## Connessioni

- [[ceo-okr-tracker]] · `agenti/ceo-okr-tracker.md`
- [[ceo-verificatore]] · `agenti/ceo-verificatore.md`
- [[ceo-memoria]] · `agenti/ceo-memoria.md`
- [[WF-REVIEW-TRIMESTRALE]] · `workflow/WF-REVIEW-TRIMESTRALE.md`
- [[STATE]] · `state/README.md`
- [[SCRIPTS]] · `scripts/README.md`
