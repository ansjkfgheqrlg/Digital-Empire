---
Type: CONCEPT
Status: Active
Tags: #regole #cro #revenue #vincoli #operativi
Created: 2026-06-17
Last updated: 2026-06-17
---

# REGOLE OPERATIVE — CRO (Chief Revenue Officer)

> Regole operative specifiche del team CRO. Più concrete dei principi: descrivono comportamenti
> precisi, SLA, vincoli e divieti espliciti. Aggiornabili via ADR — mai in silenzio.

---

## R1 — Il Catalogo Prezzi È Immutabile Senza Lotto

**Regola:** Outreach Factory €4.000 / Content Factory €3.500 / Second Brain €2.500 /
Engine Room €8.000. Nessun agente, nessun operatore, nessuna eccezione modifica questi prezzi
senza aver completato WF-PRICING e ricevuto approvazione esplicita del lotto MAXIMILIAN/CEO.

**Violazione:** qualsiasi preventivo con prezzo diverso dal catalogo, emesso senza approvazione
lotto, è bloccato da `cro-pricing-arbiter` e ritirato se già uscito.

**ADR di riferimento:** Mandato Art.3 (invariante fino a nuovo ADR Board).

---

## R2 — Nessun Preventivo Senza Gate Preventivo PASS

**Regola:** prima che un preventivo esca verso un prospect, deve superare i 8 check del
proposal-gate (skill `proposal-gate`) eseguito da `cro-deal-desk`. Un FAIL non è un avviso:
è un blocco. Il preventivo non esce finché ogni punto bloccante non è risolto.

**SLA:** il gate-check deve completarsi entro 4h dal ricevimento del brief discovery.

---

## R3 — Nessun Numero nel Forecast Senza Fonte O [DM]

**Regola:** nel documento forecast per il CEO ogni voce numerica ha una fonte esplicita
(agente che ha fornito il dato, base di calcolo) oppure è marcata [DM] (da misurare) con
spiegazione del perché non è quantificabile ora. Voci con numeri inventati o approssimati
senza fonte vengono rigettate da `cro-forecast-analyst` e richieste di re-elaborazione.

---

## R4 — Discovery Call → Brief Entro 4h

**Regola:** dopo ogni discovery call, il brief strutturato (skill `discovery-call-brief`)
deve essere prodotto da A3-BRIEF di Agency entro 4h dalla call. Il `cro-deal-desk` non
avvia la strutturazione dell'offerta senza il brief; il conductor non avvia WF-DEAL senza
il brief.

**Eccezione:** se la call produce dati insufficienti per il brief → il conductor richiede
una seconda call o un questionario scritto entro 24h prima di procedere.

---

## R5 — Deal in Stallo >10gg: Alert Obbligatorio

**Regola:** qualsiasi deal fermo in stadio "preventivo inviato" da più di 10 giorni senza
risposta riceve un alert obbligatorio da `cro-pipeline-health` al conductor. Il conductor
attiva `cro-agency-pipeline` per l'analisi e decide: follow-up urgente, chiusura "loss con
motivo", o escalation a Max per call diretta.

**Nessun deal resta in "preventivo inviato" >15gg senza una decisione esplicita.**

---

## R6 — Ogni Win e Ogni Loss Vanno in cro-memoria

**Regola:** ogni deal chiuso (win o loss) viene archiviato in `cro-memoria` entro 24h dalla
chiusura, con: prodotto, prezzo praticato, canale origine, durata ciclo, motivo win/loss.
Un deal che non è in `cro-memoria` non è "chiuso" — è un dato perso.

**Enforcement:** il conductor verifica settimanalmente che n. deal chiusi = n. record in memoria.

---

## R7 — Cross-Sell Check Entro 48h da Lancio IB Chiuso

**Regola:** dopo ogni lancio InfoBusiness chiuso, `cro-cross-sell-mapper` deve produrre la
lista lead caldi (score ≥7) entro 48h. Il conductor valida la lista e la passa ad A2-Agency
per outreach dedicato entro ulteriori 24h. Totale: ≤72h da chiusura lancio a outreach avviato.

---

## R8 — Forecast Trimestrale: Consegna Entro Giorno 5 del Trimestre

**Regola:** il documento forecast per il CEO deve essere consegnato al CEO-conductor entro
il giorno 5 del trimestre. Il conductor avvia WF-FORECAST il giorno 1. Ogni agente source
ha 48h per consegnare il proprio input (giorni 1-3). L'elaborazione finale ha 48h (giorni 3-5).

**Penalità di processo:** se il forecast arriva dopo il giorno 5, il conductor registra il
motivo del ritardo in `board/cro/forecast/changelog.md`.

---

## R9 — Nessun Sconto Comunica Con Il Prospect Prima Del Lotto

**Regola:** se durante una negoziazione emerge la possibilità di una variazione prezzo,
nessun agente CRO (e nessun operatore di Agency) comunica al prospect un prezzo diverso dal
catalogo prima che il lotto abbia dato il suo ok. La risposta standard è: "valutiamo la
migliore configurazione per te e torniamo entro [X]gg".

---

## R10 — Churn Alert: Azione Entro 24h da Segnale A7

**Regola:** quando `cro-retention-revenue` riceve un segnale di rischio churn da A7-Account
Mgmt (NPS basso, silenzio, ticket multipli), produce l'alert al conductor entro 4h e il
conductor decide l'azione entro 24h dal segnale originale. Un cliente a rischio churn che
non riceve un'azione entro 24h è un'escalation automatica a Max.
