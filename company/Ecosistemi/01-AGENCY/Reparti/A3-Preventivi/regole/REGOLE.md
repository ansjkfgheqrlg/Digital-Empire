---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #agency #preventivi #pricing #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# Regole Non Negoziabili — A3 Preventivi

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessuna proposta esce senza Gate Preventivo verde

Ogni proposta passa per AG-A3-QA (skill `proposal-gate`) prima dell'invio. Il gate è **bloccante**
e **binario**: PASS o FAIL. AG-A3-QA **blocca se non conforme — mai suggerisce soltanto**. Nessun
invio senza gate verde, nemmeno con il countdown 48h in scadenza.

Se c'è urgenza estrema → escalation ad AG-DIR: solo il direttore può decidere un invio con nota di
rischio esplicita. AG-A3-QA documenta qualsiasi bypass non autorizzato.

**Perché esiste questa regola:** il gate è l'ultima difesa del Mandato ("prove non promesse") e del
posizionamento prima che il documento raggiunga il cliente. Senza gate, la qualità è opinione.

---

## R2 — A3 seleziona dal catalogo; NON decide i prezzi

Il pricing è fisso: Outreach Factory €4.000 · Content Factory €3.500 · Second Brain €2.500 ·
Engine Room €8.000, one-time, €0 canoni. AG-A3-PRICE **seleziona** il prodotto/bundle adatto al
problema; non calcola, non sconta, non inventa configurazioni. Le decisioni di prezzo appartengono a
**team-prezzi (B-003)**: A3 le recepisce.

Nessun agente di A3 modifica un prezzo, crea un bundle non a catalogo, o applica uno sconto.

**Perché esiste questa regola:** un prezzo deciso fuori dal team-prezzi rompe la coerenza
dell'offerta a livello di holding e trasforma ogni trattativa in una negoziazione al ribasso.

---

## R3 — Nessuno sconto improvvisato

Qualsiasi richiesta di sconto (dal lead, in call, o in follow-up) → **NO automatico**. Una deroga è
possibile solo come **decisione Board registrata** (B-003). Mai uno sconto silenzioso per chiudere.

Questo vale in WF-PREVENTIVO (AG-A3-PRICE) e in WF-FOLLOWUP-COMMERCIALE (AG-A3-FUP non rinegozia).

**Perché esiste questa regola:** lo sconto improvvisato segnala che il prezzo era gonfiato e
addestra i clienti a negoziare; erode il valore percepito dell'intera offerta.

---

## R4 — Il problema del cliente apre il documento

Ogni proposta apre con il problema del cliente, mai con Digital Empire o con il prodotto. AG-A3-PROP
scrive problem-first; AG-A3-QA verifica nel gate. Un documento che apre con "chi siamo" o con il
prodotto = **FAIL automatico** senza analisi aggiuntiva.

L'awareness level (aware/unaware) calibra il tono, ma non l'ordine: il problema viene prima.

**Perché esiste questa regola:** è il principio cardine di `beast-preventivi`. Una proposta
prodotto-first vende caratteristiche; una problem-first vende la soluzione di un problema reale.

---

## R5 — Promesse = prove verificabili (Mandato Art.2)

Nessun claim numerico senza fonte. Ogni "otterrai X", ogni percentuale, ogni risultato citato deve
avere una prova verificabile (dato audit, benchmark con fonte, risultato passato reale). Dove il dato
non esiste → [DM], mai un numero inventato. AG-A3-QA blocca i claim non sostenuti.

**Perché esiste questa regola:** una promessa non provata vince il cliente sbagliato e, alla prima
verifica, distrugge la fiducia su cui si regge il posizionamento "agenzia da licenziare".

---

## R6 — Clausole obbligatorie in ogni proposta

Ogni proposta contiene, senza eccezioni: **proprietà del codice al cliente · €0 canoni ·
setup ≤7 giorni · supporto 90 giorni**. La mancanza di una sola clausola = gate FAIL.

**Perché esiste questa regola:** sono la promessa di autonomia messa per iscritto (Mandato Art.1).
Una proposta senza queste clausole vende dipendenza, non autonomia.

---

## R7 — Motivo di loss SEMPRE registrato

Nessun preventivo si chiude come loss senza un motivo (campo `causa`) registrato in `agency/reasoning`
da AG-A3-LEARN. Un loss senza motivo è un esito non chiuso e alimenta WF-LOSS-ANALYSIS con dati
incompleti. Inoltre: nessun pattern di loss dichiarato significativo su n < 5; nessuna conclusione su n < 3.

**Perché esiste questa regola:** la pipeline migliora solo se ogni perdita diventa conoscenza
riusabile. Senza motivo, il loss è solo un fallimento; con motivo, è un dato.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ag-a3-qa]] · `agenti/ag-a3-qa.md` — esecutore del Gate Preventivo (R1, R4, R5, R6)
- [[ag-a3-price]] · `agenti/ag-a3-price.md` — applica R2, R3 (catalogo, no sconti)
- [[01-ECOSISTEMA-AGENCY-V2]] · Mandato Art.1-2 + B-003 come fonte di R2-R6
