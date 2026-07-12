---
Type: CONCEPT
Status: Active
Tags: #principi #agency #closing #sales-call #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# PRINCIPI — A8 Closing / Sales-Call

> I principi orientano il giudizio quando la regola non copre il caso.
> Le regole vincolano (`regole/REGOLE.md`, R1–R8); i principi spiegano **perché** quelle regole esistono.
> Se un principio e una regola sembrano in conflitto, vince la regola — e il conflitto va in ADR.

---

## P1 — Prove, non promesse (Mandato Art.2)

**Principio:** in call, ogni promessa deve poter essere seguita da un fatto verificabile. Se la
prova non esiste, la promessa non si fa. Non "si ammorbidisce": **non si fa**.

**Razionale:** Digital Empire si posiziona come "l'agenzia progettata per essere licenziata" —
autonomia del cliente, non dipendenza. Un claim non verificabile in call è un debito che il cliente
scopre in delivery: costa il rimborso, la reputazione e il case study. Un `[DM]` dichiarato in call
("questo numero non l'ho misurato su un caso come il suo") costruisce più fiducia di una
percentuale inventata — e la fiducia è ciò che fa firmare. Il costo di dire "non lo so" è di
secondi; il costo di una promessa scoperta è il contratto e il cliente successivo.

**Conseguenza operativa:** AG-A8-OBJ non scrive risposte senza prova; AG-A8-PREP marca `[DM]` ogni
promessa scoperta e la mette nel blocco "cosa NON promettere"; AG-A8-QA blocca (R3).

---

## P2 — La call resta umana; A8 possiede la preparazione

**Principio:** Max conduce la call e possiede la relazione. A8 non scrive cosa dire parola per
parola come un gobbo: costruisce il **terreno** su cui Max improvvisa bene.

**Razionale:** una call di chiusura è un atto di fiducia tra persone. Automatizzarla la
distruggerebbe; lasciarla senza struttura (come nel v1) la rende dipendente dall'energia del giorno.
La soluzione non è sostituire l'umano, è **eliminare l'improvvisazione sui fatti**: numeri, scope,
prezzi, prove e obiezioni sono preparati; il tono, l'ascolto e il giudizio restano di Max. Un agente
che pretendesse di chiudere al posto suo produrrebbe call peggiori, non migliori.

**Conseguenza operativa:** l'unico output di A8 verso l'esterno è il dossier pre-call. Il dossier è
il documento di confine: prima è A8, dopo è Max.

---

## P3 — Zero pressione, zero scarsità artificiale

**Principio:** vietato "solo 2 slot rimasti", "il prezzo sale domani", "se non decide oggi",
urgenza fabbricata, colpa, ansia. Se il prospect ha bisogno di tempo, il tempo è parte dell'offerta.

**Razionale:** la pressione funziona una volta e produce il cliente peggiore: quello che ha firmato
per non litigare, che in delivery resiste e in retention scappa. La CRO insegna esattamente questo
sulle landing; la stessa fisica vale in call. Una scarsità **reale** (capacità di delivery
effettivamente limitata) si può dire perché è vera — ed è verificabile. Una scarsità **inventata**
è un claim falso, e ricade sotto P1: è una promessa senza prova, quindi vietata.

**Conseguenza operativa:** AG-A8-SCRIPT e AG-A8-OBJ hanno un filtro anti-pressione esplicito;
AG-A8-QA blocca alla prima occorrenza (R4, bloccante assoluta).

---

## P4 — Il prezzo viene dal catalogo, mai dalla call

**Principio:** i prezzi sono a catalogo fisso (team-prezzi, B-003). In call non si inventano
prezzi, non si concedono sconti, non si "vede cosa si può fare".

**Razionale:** un prezzo negoziato in call comunica che il prezzo di listino era finto, e con esso
diventa sospetto tutto il resto del preventivo. Peggio: distrugge la comparabilità dei KPI (K1, K2)
e rende impossibile capire se perdiamo per il prezzo o per lo scope. Il catalogo fisso è ciò che
permette di dire "questo è il prezzo" senza esitazione — ed è l'esitazione, non il numero, che il
prospect percepisce. Una deroga è possibile, ma è una **decisione Board registrata**, non una mossa
di chi è in call sotto stress.

**Conseguenza operativa:** richiesta sconto → NO automatico + registrazione del motivo nel debrief.
Il pattern "perdiamo per prezzo" si porta a team-prezzi con evidenze, non si risolve improvvisando.

---

## P5 — Nessuna call si chiude senza motivo

**Principio:** ogni call finisce con un `esito` **e** un `motivo`, con le parole del prospect.
Una call senza motivo registrato **non è chiusa**, qualunque cosa sia successa.

**Razionale:** il motivo è l'unico asset che una call persa produce. Senza motivo, un loss è puro
costo; con il motivo, è l'input che corregge la libreria obiezioni (A5), il preventivo (A3) e
l'ICP (A1). L'errore classico è registrare **l'interpretazione** invece del motivo: "era troppo
caro" (opinione di chi ha condotto) al posto di "devo confrontarlo con l'altra agenzia" (fatto).
La prima chiude l'indagine; la seconda la apre. Il motivo si registra entro 2h perché oltre le 2h
la memoria si riscrive da sola in una storia coerente — e le storie coerenti sono quasi sempre false.

**Conseguenza operativa:** R7 bloccante; AG-A8-DEBRIEF non può chiudere il record; K5 target 100%.

---

## P6 — Wrappare, non riscrivere (ADR-003)

**Principio:** A8 **usa** gli artefatti degli altri reparti (preventivo A3, libreria obiezioni A5,
script standard A5, dossier lead A1) senza riscriverli. Li aggrega, li personalizza in un layer
tracciabile, e restituisce **proposte** di miglioramento al proprietario.

**Razionale:** se A8 riscrivesse il preventivo per "farlo suonare meglio in call", esisterebbero due
versioni della verità e il cliente firmerebbe quella sbagliata. Se riscrivesse la libreria obiezioni,
A5 perderebbe il controllo del suo asset e i miglioramenti non tornerebbero agli altri canali (ads,
email, landing). Il confine di proprietà è ciò che permette a un pattern scoperto in call di
migliorare **tutta** l'agenzia, non solo la prossima call. A8 impara e restituisce; non colonizza.

**Conseguenza operativa:** AG-A8-LEARN propone ad A5/A3, non modifica. AG-A8-PREP cita il preventivo
**verbatim**. AG-A8-SCRIPT wrappa lo script standard e dichiara il `delta_vs_standard`.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole R1–R8 che traducono questi principi in vincoli
- [[ag-a8-qa]] · `agenti/ag-a8-qa.md` — il gate che li rende esecutivi
- [[README]] · `README.md` — missione e confini del reparto
