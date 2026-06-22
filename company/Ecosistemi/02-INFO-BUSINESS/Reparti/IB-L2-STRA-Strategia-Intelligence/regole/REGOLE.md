---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #strategia #intelligence #backlog #IB-L2-STRA
Created: 2026-06-21
Last updated: 2026-06-21
---

# Regole Non Negoziabili — IB-L2-STRA Strategia & Intelligence

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessun claim di mercato o competitor senza fonte citata

Ogni dato di mercato, ogni prezzo competitor, ogni segnale di domanda deve avere una fonte reale
dichiarata: URL + data di rilevazione, screenshot, oppure log community con conteggio e periodo.
Un dato senza provenienza non entra in nessun output del reparto.

**Perché esiste questa regola:** è il cuore dell'area. La differenza tra "idea pre-validata" e "opinione"
è la fonte. IB-STRA-QA verifica in G-FONTI; un claim senza fonte = FAIL automatico, l'output torna allo
specialista responsabile prima di poter proseguire.

---

## R2 — Nessuna metrica stimata presentata come reale

Le stime sono ammesse, ma devono essere etichettate: `[stima]` per una proiezione ragionata, `[DM]`
(Da Misurare) dove la baseline non esiste ancora. "Potenziale 1500 lead", "conversione attesa 4%",
"mercato da 2M€" senza etichetta e senza fonte sono vietati.

**Perché esiste questa regola:** una stima travestita da dato reale contamina lo score e inganna il
Director. Committente che chiede previsioni → risposta corretta: "la baseline si stabilisce al primo
dato reale; possiamo dichiarare la struttura del segnale e la sua forza, non i numeri." (Mandato Art.2.)

---

## R3 — Nessuna idea passa a IB-L2-PROD con score <60

L'handoff HC-STRA-PROD-01 verso l'Area Prodotto richiede score ≥60 **e** almeno una fonte reale che
sostiene l'idea **e** ICP fit dichiarato. Le idee 40-59 restano parcheggiate (serve più evidenza); le
idee <40 si scartano e si archiviano in `backlog/archivio/`.

**Perché esiste questa regola:** la soglia ≥60 è il contratto con PROD. Passare idee sotto soglia
significa scaricare a valle il lavoro di pre-validazione, rompendo il principio che PROD non deve mai
cercare idee. Score ≥80 = priorità alta, candidabile per il primo slot disponibile a roadmap.

---

## R4 — IB-STRA-QA è bloccante su ogni idea e ogni roadmap in uscita

Nessuna idea proposta al Director, nessuna roadmap, nessun dossier consegnato esce senza gate verde di
IB-STRA-QA. Il gate verifica prove, non merito: non giudica se l'idea è buona, giudica se è sostenuta
da dati reali. Il gate non ha deroga per urgenza.

Se c'è urgenza → IB-COORD-STRATEGIA può presentare un output etichettato come parziale con nota di rischio
esplicita SOLO con il difetto dichiarato (es. "fonte da consolidare"). Mai spacciare un parziale per gated.

---

## R5 — STRA non valida e non costruisce prodotti

Il reparto fa il lavoro a monte. La validazione formale (test mercato, smoke test, go/no-go) è di
IB-L2-PROD via WF-VALIDAZIONE. La produzione (corso, ebook, comunità) è di IB-L2-PROD via WF-CORSO.
Nessun agente di STRA esegue smoke test, decide go/no-go, o produce materiale di prodotto.

**Perché esiste questa regola:** pre-validazione ≠ validazione. STRA che valida crea un doppio gate e
confonde la responsabilità del go/no-go, che deve restare di PROD col Director.

---

## R6 — Nessuna roadmap senza lead time per prodotto e buffer ≥30gg

Ogni prodotto a roadmap ha un lead time stimato (da capacità reale IB-L2-PROD, non inventato). Ogni
coppia di lanci consecutivi ha un gap ≥30gg perché la lista (recovery list) deve riprendersi. Una
roadmap senza questi due requisiti non si presenta al Director.

Se la produzione non regge il ritmo → IB-STRA-ROADMAP ricalcola con lead time reali e
IB-COORD-STRATEGIA negozia le priorità. Mai una roadmap che la produzione non può sostenere (P4).

---

## R7 — La ricerca pesante si delega a 08-INTELLIGENCE, non si improvvisa

Scraping, profili competitor estesi, analisi trend di settore profonde si delegano a 08-INTELLIGENCE
via HC-INT-STRA-01. STRA riceve dataset + fonti dichiarate; non raccoglie dati pesanti da solo e non
accetta un dataset senza provenienza (URL + data). Schema richiesta:
`{tipo: trend|competitor|icp_data, scope, profondità: rapida|completa, deadline}`.

**Perché esiste questa regola:** evita che STRA produca dati di seconda mano senza tracciabilità,
violando R1. La provenienza segue il dato per tutta la pipeline fino al gate.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ib-stra-qa-verificatore-strategia]] · `agenti/ib-stra-qa-verificatore-strategia.md` — esecutore del gate
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confini STRA vs PROD e handoff contract
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · Mandato Art.2 "prove non promesse" come fonte di R1, R2, R3
