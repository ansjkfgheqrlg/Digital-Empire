---
Type: PRINCIPI
Status: Active
Tags: #principi #strategia #intelligence #backlog #roadmap #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# Principi — IB-L2-STRA Strategia & Intelligence

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.

---

## P1 — La strategia vive qui; la validazione e la produzione altrove

IB-L2-STRA è il lavoro a monte: identifica temi emergenti, mappa i gap competitor, aggiorna l'ICP,
scrive le bozze idea con uno score, propone la top idea al Director. **Non valida i prodotti, non li
costruisce.** La validazione formale (test mercato, smoke test, go/no-go) è di IB-L2-PROD via
WF-VALIDAZIONE. La produzione è di IB-L2-PROD via WF-CORSO.

La prova pratica: l'idea pre-validata è il documento di confine. STRA la produce con score ≥60 e fonti.
PROD la riceve via HC-STRA-PROD-01 e decide. **Pre-validazione ≠ validazione** non è uno slogan: è il
confine che impedisce a STRA di sovrappormi a PROD e a PROD di dover cercare idee da zero.

---

## P2 — Prove, non opinioni (l'idea senza fonte non esiste)

"Questo prodotto piacerebbe" non è una ragione per metterlo in roadmap. Il segnale di mercato con fonte
(volume ricerche, N domande community datate, lancio competitor con URL) è la ragione. La pressione a
proporre un'idea "perché piace a qualcuno" si gestisce sempre allo stesso modo: si chiede l'evidenza.
Se non c'è, l'idea resta parcheggiata (40-59) finché qualcuno non porta il dato.

Questo principio rende il gate IB-STRA-QA inevitabile, non burocratico: la differenza tra "idea
pre-validata" e "opinione" è esattamente la presenza di una fonte reale e verificabile.

---

## P3 — Lo score è deterministico, non un'impressione

Ogni idea riceve uno score /100 su 5 criteri (20 punti ciascuno): domanda di mercato, gap competitor,
fit ICP, fattibilità produzione, potenziale revenue/strategico. Ogni punto deve essere ancorato a un
dato citato — non a un "sento che". Lo score è il linguaggio comune tra STRA e PROD: a parità di criteri,
due analisti diversi devono arrivare allo stesso intervallo di punteggio.

Soglie: `<40` scartata · `40-59` parcheggiata (serve più evidenza) · `≥60` candidabile · `≥80` priorità alta.
Uno score gonfiato rispetto all'evidenza è una violazione che IB-STRA-QA blocca in G-SCORE.

---

## P4 — La roadmap deve essere sostenibile, non ambiziosa sulla carta

Una roadmap che la produzione non può reggere è peggio di nessuna roadmap: genera slittamenti silenziosi
e brucia la fiducia del Director. Ogni prodotto a roadmap ha un lead time stimato (da capacità reale
IB-L2-PROD) e un buffer ≥30gg dal lancio precedente, perché la lista deve riprendersi tra un lancio e
l'altro (recovery list).

La tentazione di comprimere i lanci arriva quando il backlog è pieno di idee buone. La risposta corretta
è: sequenziare per dipendenze e capacità, non per entusiasmo. Una roadmap rispettata vale più di una
roadmap ambiziosa disattesa.

---

## P5 — L'ICP è vivo, non un documento fossile

L'ICP info-business (≠ ICP AGENCY) si aggiorna con dati freschi: domande ricorrenti dalla community,
segnali cross-sell, obiezioni post-vendita da IB-L2-COMM. Un ICP che non cambia da due trimestri è un
ICP che ha smesso di guardare il mercato. Ogni aggiornamento è datato e tracciato in `icp_changelog.md`.

I pain point "non ancora coperti dai prodotti attuali" sono il giacimento di idee: l'ICP aggiornato
alimenta direttamente il backlog (criterio 3 dello score).

---

## P6 — Si fa evolvere il business col mercato, non lo si rincorre

Il reparto esiste per anticipare, non per reagire in ritardo. Quando un trend cambia in modo dirompente
(nuovo formato che domina, competitor che ridefinisce la categoria), IB-COORD-STRATEGIA escala al Director
con dossier e proposta di ri-priorizzazione — non aspetta il ciclo mensile. Anticipare con dati è il
mestiere; rincorrere senza dati è il fallimento che il reparto previene.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili (più stringenti dei principi)
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-STRA`
- [[README]] · `README.md` — missione del reparto e sistema di scoring
