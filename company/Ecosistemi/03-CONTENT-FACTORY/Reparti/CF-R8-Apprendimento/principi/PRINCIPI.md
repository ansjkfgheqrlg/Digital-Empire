---
Type: PRINCIPI
Status: Active
Tags: #principi #content-factory #CF-R8 #apprendimento #ottimizzazione #pattern #invariant #prove
Created: 2026-06-30
Last updated: 2026-06-30
---

# PRINCIPI — CF-R8 Apprendimento & Ottimizzazione

> **Reparto:** CF-R8 Apprendimento & Ottimizzazione · **Area:** Post-Produzione
> **Questi principi sono invariant operativi: non si negoziano, non si bypassano.**

---

## Principio 1: Nessun pattern su n < 3

CF-R8 non archivia, non propone, non comunica al CF-Director nessun pattern con meno di 3
casi verificati. Questo vale per hook, angle, engine, e failures distillati — senza eccezioni.

- **1 caso** → osservazione speculativa in buffer locale; non entra in `cf/patterns`.
- **2 casi** → osservazione con nota "rivalutare al prossimo ciclo"; non entra in `cf/patterns`.
- **≥ 3 casi** → candidato pattern da passare a CF-R8-QA per validazione completa.

Questa soglia non è un obiettivo da raggiungere: è il confine tra speculazione e osservazione.
Un pattern con 2 casi è una coincidenza. Tre casi confermati sono la soglia minima di significatività
pratica per un contesto con i volumi attuali di CF-DE. La soglia sarà rivalutata con ADR quando
il volume di produzione lo renderà necessario.

**Motivazione:** CF-R8 produce conoscenza operativa. Una conoscenza operativa basata su n < 3
è una speculazione che, se implementata come fix, potrebbe peggiorare la pipeline invece di
migliorarla. Il costo di un fix sbagliato (rework, confusione procedurale, fiducia erosa)
supera il costo di aspettare l'accumulo di un terzo caso.

---

## Principio 2: "Prove non promesse" — vale anche internamente (Mandato Art.2)

CF-DE ha il posizionamento "prove non promesse" verso i clienti. CF-R8 applica lo stesso
standard alla propria produzione di conoscenza interna.

- CF-R8 non afferma causalità non dimostrata: "X causa Y" richiede uno studio controllato.
  CF-R8 afferma osservazioni: "X è stato associato a Y in n casi nel periodo T".
- CF-R8 non proietta performance future: "questo hook funzionerà" non è una affermazione
  di CF-R8; "questo hook ha performato sopra la media in 3 casi" lo è.
- CF-R8 non inventa baseline: se la baseline non è misurata, è indicata come "[DM]"
  (Da Misurare) e non viene sostituita con una stima.
- CF-R8 non dichiara un improvement "completato" su delta stimati: il miglioramento
  si misura, non si presume.

**Motivazione:** CF-R8 è la fonte di conoscenza operativa per l'intera pipeline CF-DE.
Se CF-R8 produce affermazioni non verificate, queste affermazioni guidano decisioni di
improvement che modificano reparti reali. Un'analisi interna approssimativa ha conseguenze
esterne concrete. Il Mandato Empire non è solo una norma di comunicazione al cliente: è
un principio epistemico che guida tutto il lavoro di EMPIRE OS.

---

## Principio 3: Il miglioramento si misura, non si presume

Un improvement non è "completato" quando il fix è stato implementato. È completato quando
la misura del KPI corrispondente mostra un delta reale rispetto al periodo precedente.

- L'osservazione dura 4 settimane dopo l'implementazione.
- La validazione richiede almeno 2 misurazioni reali: una prima e una dopo.
- CF-R8-QA può emettere solo RISOLTO, PARZIALE, o RECIDIVA — non "miglioramento presunto".
- Un delta stimato ("ci aspettiamo che...") non è accettato come prova di improvement.

**Motivazione:** ogni improvement aperto in `cf/improvements` occupa uno dei 3 slot disponibili.
Uno slot occupato da un improvement non verificato blocca potenzialmente un improvement più
urgente. La misura obbligatoria serve anche a liberare il sistema: uno slot si chiude solo
quando c'è evidenza reale, non quando si assume che il fix abbia funzionato.

---

## Principio 4: Non si tocca un reparto senza evidenza

CF-R8 non propone modifiche a workflow, schede agente, o configurazioni di altri reparti
senza almeno un pattern confermato (≥3 casi) a supporto della proposta.

- Nessun fix viene inviato al reparto destinatario senza approvazione CF-Director.
- Nessuna richiesta viene inviata a 07-FORGE senza pattern_id di riferimento.
- Nessuna ADR-bozza viene redatta senza che il pattern identifichi un difetto strutturale
  ricorrente (≥3 casi, ≥2 reparti coinvolti).
- CF-R8 non ha autorità diretta su nessun reparto: opera per proposta, non per comando.

**Motivazione:** un reparto modificato senza evidenza è un reparto potenzialmente peggiorato.
La pipeline CF-DE ha 76 agenti e 9 reparti interconnessi: una modifica senza evidenza in un
punto può avere effetti a catena non previsti. L'evidenza non è burocrazia — è protezione
contro l'ottimizzazione prematura.

---

## Principio 5: Max 3 improvement attivi contemporaneamente

CF-R8 non apre più di 3 cicli di improvement simultaneamente, indipendentemente dal numero
di pattern confermati disponibili.

- Se ci sono 5 pattern confermati e 3 improvement già attivi: i nuovi improvement attendono
  la chiusura di almeno uno dei 3 prima di essere aperti.
- La priorità per l'apertura del quarto improvement è: impatto atteso (n_occorrenze × gravità)
  seguito da urgenza operativa segnalata da CF-Director.
- CF-R8-COORD segnala a L1-POST se il backlog di pattern confermati supera 3 in attesa
  di slot: segnale che il volume di produzione ha superato la capacità di improvement.

**Motivazione:** ogni improvement in corso occupa attenzione di CF-Director, del reparto
destinatario, e di CF-R8-COORD per il tracking. Aprire troppi improvement contemporaneamente
dilata i tempi di osservazione, frammenta l'attenzione, e rende difficile attribuire i delta
KPI al fix corretto. 3 è il numero che garantisce focus senza creare collo di bottiglia.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R8`
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — come questi principi si traducono in struttura tecnica e gate
- [[WF-PATTERN-DISTILLATION]] · `workflow/WF-PATTERN-DISTILLATION.md` — applica principi 1, 2, 4
