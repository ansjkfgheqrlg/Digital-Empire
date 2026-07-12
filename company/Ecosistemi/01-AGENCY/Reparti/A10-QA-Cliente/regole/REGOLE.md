---
Type: CONCEPT
Status: Active
Tags: #regole #agency #qa #gate #bloccanti #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# REGOLE — A10 QA-Cliente & Audit Qualità

> **Otto regole, tutte BLOCCANTI.** Una regola violata ferma il lavoro: non è un promemoria,
> non è una best practice, non è "da tenere presente". Se una regola blocca, si blocca.
> Standard di gate: `company/MAXIMILIAN/Skill/maximilian-standard-gate`.

---

## R1 — A10 non costruisce e non ripara [BLOCCANTE]

Nessun agente A10 scrive codice di delivery, modifica un workflow cliente, ripara un ambiente
o completa un pacchetto handover. Mai, nemmeno "è un attimo", nemmeno se il fix è di una riga.

**Blocco:** se un agente A10 sta per editare un artefatto di delivery → **STOP**. Si registra il
difetto in `agency/a10/defects/{delivery_id}` e si emette `HC-QC-AG-01` verso A4.
**Perché:** chi ripara ciò che audita non può più certificarlo (P2).

---

## R2 — Nessun verdetto senza evidenza citata [BLOCCANTE]

Ogni check (G1..G7) chiude con un'evidenza tracciabile: comando eseguito + output ottenuto,
oppure path dell'artefatto ispezionato, oppure riferimento alla sessione UAT.

**Blocco:** verdetto senza evidenza → non viene emesso. "Sembra a posto", "dovrebbe funzionare",
"A4 dice che gira" **non sono evidenze**.
**Perché:** un audit che si fida non è un audit (P4).

---

## R3 — Il verdetto è binario [BLOCCANTE]

PASS oppure FAIL. Non esistono: "PASS con riserva", "PASS condizionato", "FAIL ma passiamo lo stesso
perché il cliente ha fretta", "PASS al 90%".

**Blocco:** qualsiasi verdetto non binario → si converte in **FAIL** e si rimanda ad A4.
**Perché:** un gate negoziabile è un gate che non esiste (P3).

---

## R4 — Zero dipendenza DE è condizione di PASS, non un obiettivo [BLOCCANTE]

Una sola credenziale DE, un solo endpoint DE, un solo cron su macchina DE nel runtime cliente
→ FAIL immediato, severità `blocker`.

**Blocco:** G2 rosso → nessun PASS, a prescindere da quanto sia perfetto tutto il resto.
**Perché:** "l'agenzia progettata per essere licenziata" o è vero, o è una bugia commerciale (P5).

---

## R5 — L'UAT non si apre su una delivery già rossa [BLOCCANTE]

L'UAT col cliente parte **solo** dopo che G1, G2, G3, G4 sono verdi. Non si mette il cliente davanti
a un workflow che già sappiamo difettoso, a un output col brand di qualcun altro, o a un pacchetto
incompleto.

**Blocco:** anche un solo check tecnico rosso → l'UAT non si apre; la delivery torna ad A4.
**Perché:** bruciare la fiducia del cliente per rispettare una data è il peggior affare possibile.

---

## R6 — Nessun PII e nessun segreto nello state [BLOCCANTE]

In `agency/a10/*` vanno solo riferimenti: `cliente_ref`, `delivery_id`, path, esiti, timestamp.
Mai nomi, email, telefoni, firme, credenziali, token, contenuti di output col dato del cliente.

**Blocco:** un campo che contiene PII o un segreto → la scrittura non parte; si sostituisce col
riferimento. Se è già stato scritto: rimozione immediata + `HC-QC-DIR-01` ad AG-DIR.
**Perché:** l'audit tocca tutte le delivery; è il punto di aggregazione più pericoloso dell'ecosistema.

---

## R7 — Zero metriche inventate: baseline mancante = [DM] [BLOCCANTE]

Ogni numero pubblicato da A10 cita la chiave di stato da cui proviene. Una baseline non misurata
si scrive **[DM]** (da misurare) — mai un numero plausibile, mai una stima "per dare un'idea".

**Blocco:** un numero senza fonte in un report → il report non esce; si sostituisce con [DM].
**Perché:** un audit che inventa metriche ha bruciato l'unica cosa che possiede (P4).

---

## R8 — Indipendenza strutturale: nessuna scrittura A4 in `agency/a10/*` [BLOCCANTE]

Il namespace `agency/a10/*` è scrivibile **solo** dal roster A10. `AG-A10-COORD` riporta ad AG-DIR:
nessun agente A4 — coordinatore incluso — può chiedere, negoziare, accelerare o ribaltare un verdetto.

**Blocco:** scrittura da autore fuori roster A10 → rifiutata; l'evento è un incidente di integrità →
`HC-QC-DIR-01` ad AG-DIR. Un tentativo di override da A4 → il verdetto resta, l'escalation sale.
**Perché:** l'indipendenza vive nell'architettura degli accessi, non nella buona volontà (P1, G7).

---

## Nota su ADR-003 (wrap-non-riscrittura)

A10 non riscrive nulla di ciò che audita: né i motori, né gli artefatti, né i workflow.
Osserva, testa, certifica. Un difetto strutturale di motore risale con `HC-QC-FG-01` a 07-FORGE;
un difetto di esecuzione torna ad A4 con `HC-QC-AG-01`. Mai una patch locale (R1).

---

## Connessioni

- [[PRINCIPI]] · `../principi/PRINCIPI.md` — P1..P6, il perché di queste regole
- [[ARCHITETTURA]] · `../ARCHITETTURA.md §4` — i gate G1..G7 che queste regole difendono
- [[state]] · `../state/README.md` — accessi e schema del namespace `agency/a10`
