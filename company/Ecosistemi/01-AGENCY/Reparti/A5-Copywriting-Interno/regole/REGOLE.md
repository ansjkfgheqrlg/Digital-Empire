---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #agency #copywriting #gate #prove #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# Regole Non Negoziabili — A5 Copywriting Interno

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Il Gate Bibbia è bloccante su ogni output

Nessun template, micro-copy preventivo, variante A/B o script call esce dal reparto senza
Gate Bibbia verde di AG-A5-QA. Il gate non ha deroga per urgenza, pressione del committente
o richiesta di A8. Un solo check FAIL → l'output torna al produttore, non parte.

**Perché esiste:** la qualità del copy operativo dell'agency è presidiata da un solo gate
condiviso con A2. Bypassarlo romperebbe il sistema di qualità (pattern 6).

---

## R2 — A5 NON produce pezzi grandi

Sales page, sequenze email lunghe, refresh strutturali completi, copy di campagna: questi
vengono da 04-MARKETING via `HC-AG-MK-01`. A5 produce solo copy operativo quotidiano e
adattamenti locali. Nessun agente di A5 scrive una sales page o una sequenza lunga "perché
era più veloce".

**Perché esiste:** un solo standard di copy lungo nella holding (04-MARKETING). A5 che
produce pezzi grandi crea duplicazione e drift di qualità.

---

## R3 — Nessun rollout universale senza dati A/B

Una variante di template non sostituisce il template attuale finché non c'è un verdetto A/B
su campione sufficiente (AG-A5-LEARN). Si rollout-a in graduale (batch 10% leads), si misura,
si adotta solo il winner. Un winner su campione insufficiente non si adotta: si registra il
learning e si attende più volume.

**Eccezione unica:** ritiro di un template che il Gate Bibbia boccia in serie (template rotto)
→ si ritira subito perché lo status quo è già fallimentare; la sostituzione passa comunque dal gate.

---

## R4 — Prove non promesse (Mandato Art.2) — anche internamente

La libreria obiezioni contiene SOLO risposte con prova reale (conversazione A2, esito A/B,
case study A6). Nessuna risposta inventata entra nel copy o negli script. Una risposta senza
prova è `non_validata` e non si usa. Nessun claim di risultato non provabile compare in un
template o in uno script di chiusura.

CA-QA del check 3 (no dependency + prove) blocca ogni claim senza prova. Violazione = FAIL.

---

## R5 — P prima di S in ogni output (Art.4.2 Mandato)

La sezione Problema precede sempre la sezione Soluzione, in ogni template, micro-copy e script.
Non esiste awareness level così alto da saltare il Problema: per most-aware il P può essere breve
(1 frase), ma deve esserci. AG-A5-WRITE/SCRIPT lo struttura; AG-A5-QA lo verifica nel gate.
Violazione = FAIL automatico senza analisi aggiuntiva (stesso criterio del gate di A2).

---

## R6 — A5 non produce senza dato/input reale

A5 non avvia un refresh senza un segnale di calo reale da `agency/outreach` (AG-A5-LEARN).
A5 non aggiunge un'obiezione alla libreria senza che arrivi da una conversazione reale
(`HC-AG-IN-01`). A5 non produce uno script per una nicchia senza le obiezioni validate di
quella nicchia. Quando il dato manca, A5 segnala il gap — non lo riempie con intuizione.

**Perché esiste:** A5 è un adattatore data-driven. Senza dato reale, qualsiasi output è
opinione travestita da copy (vedi P3, P5).

---

## R7 — Il gate non si ridefinisce localmente

AG-A5-QA usa i criteri canonici del Gate Bibbia di A2 (`../A2-Acquisizione/agenti/ag-a2-qa.md`).
Nessun criterio locale divergente, nessun "per A5 va bene così". Se un caso A5 nuovo rende un
criterio ambiguo, la questione si porta al gate canonico — non si crea un'eccezione locale.

**Perché esiste:** pattern 6 (una skill, molti reparti). Due definizioni dello stesso gate =
due standard = sistema di qualità rotto (ADR-003 wrap-not-rewrite).

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ag-a5-qa]] · `agenti/ag-a5-qa.md` — esecutore del Gate Bibbia (riuso A2)
- [[ag-a2-qa]] · `../A2-Acquisizione/agenti/ag-a2-qa.md` — definizione canonica del gate (R7)
- [[ARCHITETTURA]] · `ARCHITETTURA.md §3` — confine A5 vs 04-MARKETING (R2)
