---
Type: PRINCIPI
Status: Active
Tags: #principi #conversion #funnel #cro #marketing #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# Principi — L2.6 Conversion Architecture

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.

---

## P1 — La strategia di conversione vive qui; l'implementazione in 06-PLATFORM

L2.6 è il cervello della conversione: progetta cosa deve fare ogni pagina, ogni stage,
ogni sequenza di step. 06-PLATFORM è il corpo: costruisce la pagina secondo il brief.
Il confine non è negoziabile. Se L2.6 inizia a costruire pagine o 06-PLATFORM inizia
a decidere la struttura senza brief approvato, il sistema si rompe.

La prova pratica: il brief tecnico è il documento di confine. L2.6 lo produce e lo firma.
06-PLATFORM lo riceve e lo implementa. Senza brief firmato, nessuna pagina si costruisce.

---

## P2 — Il funnel serve APSOC end-to-end, non stage per stage

Un funnel non è una collezione di pagine indipendenti. È una progressione logica dove ogni
stage prepara il visitatore per il prossimo. La sezione A (Attenzione) del ToFu non ha
completato il suo lavoro se il visitatore non sa ancora quale problema ha quando arriva
al MoFu. La sezione P (Problema) del MoFu non ha completato il suo lavoro se il visitatore
arriva alla sales page senza capire perché il problema lo riguarda.

CA-QA verifica la coerenza end-to-end, non solo la qualità di ogni singolo stage.
Un funnel con ogni stage ottimo ma progressione incoerente non converte.

---

## P3 — Si ottimizza solo su dati, mai su opinioni

"Questa headline funzionerà meglio" non è una ragione per cambiare qualcosa. Il dato
di AN5 (drop rate per sezione APSOC) è la ragione. Il verdetto di AN3 (WF-AB-TEST) è
la conferma. Il learning di CA3 (schema micro-conversioni) è il metodo di diagnosi.

Nessun sprint CRO parte senza segnale di drop. Nessun winner si implementa senza
verdetto statisticamente valido. Nessun threshold si dichiara senza dato reale.
[DM] è la risposta corretta quando il dato non esiste ancora — non un numero inventato.

---

## P4 — Una variante = un elemento cambiato

Cambiare headline + proof + posizione CTA + form in un unico test non permette di sapere
cosa ha funzionato. Cambiare un solo elemento per variante è più lento ma produce conoscenza
reale. La conoscenza reale si accumula in `marketing/copy/patterns/{icp}` e vale più di
qualsiasi ottimizzazione temporanea.

La tentazione di "redesignare tutto" arriva quando il funnel non performa e non si vuole
aspettare. La risposta corretta è: identificare il collo di bottiglia, testare la variante
minima, aspettare il verdetto.

---

## P5 — Il message-match è il fondamento, non il dettaglio

La conversione inizia prima che il visitatore atterri sulla landing. La promessa dell'ad,
del post, dell'email deve matchare esattamente il frame dell'headline della landing. Una
landing perfetta con un ad che promette qualcosa di diverso perde utenti nel salto.

CA2 dichiara il message-match in ogni brief tecnico. CA-QA lo verifica. Non è un
campo facoltativo.

---

## P6 — Prova non promessa anche nell'architettura

Il Mandato Art.2 vale anche per i brief tecnici e le architetture funnel. Non si
specifica "alta conversione attesa" senza base. Non si dichiara un impatto stimato
in un audit senza motivazione APSOC. I [DM] sono onestà, non debolezza.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili (più stringenti dei principi)
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §11 pre-mortem
- [[README]] · `README.md` — missione del reparto
