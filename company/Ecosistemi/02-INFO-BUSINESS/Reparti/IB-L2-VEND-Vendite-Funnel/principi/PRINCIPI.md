---
Type: PRINCIPI
Status: Active
Tags: #principi #vendite #funnel #evergreen #cro #IB-L2-VEND
Created: 2026-06-21
Last updated: 2026-06-21
---

# Principi — IB-L2-VEND Vendite & Funnel

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.

---

## P1 — L'offer stack vive qui; i numeri di prezzo vivono in team-prezzi (B-003)

IB-L2-VEND progetta l'architettura dell'offerta: value stack, bonus, garanzia, order bump,
upsell, naming. È il cervello dell'offerta. Ma i valori numerici dei prezzi NON si decidono
qui: arrivano dal catalogo approvato di team-prezzi (B-003, ADR-005). IB-VEND-OFFER slotta
lo stack pronto e recepisce i numeri prima del go live.

La prova pratica: il catalogo prezzi approvato è il documento di confine. Senza prezzo
approvato per un prodotto, l'offer stack resta architettura e il go live slitta. Nessun
prezzo "provvisorio" o placeholder esce in produzione.

---

## P2 — L'evergreen è un reparto, non un ripiego post-lancio

Il funnel evergreen — lead magnet → opt-in → nurture → sales page → checkout — gira tutti
i 365 giorni con workflow propri. Un lancio valida l'offerta; il funnel evergreen la scala.
Trattare l'evergreen come "quello che resta dopo il lancio" produce un funnel trascurato che
non converte. Qui ha pari dignità del lancio: tracking su ogni step, loop CRO settimanale,
revenue continua e pipeline lead per gli altri ecosistemi.

WF-FUNNEL-EVERGREEN non è subordinato a WF-SALESPAGE: lo riusa come componente, ma vive
di vita propria.

---

## P3 — Si ottimizza solo su dati, mai su opinioni

"Questa headline converte meglio" non è una ragione per cambiare. Il dato di IB-VEND-TRACK
(conversione per step) è la ragione. L'ipotesi falsificabile di IB-VEND-CRO è il metodo.
Il campione minimo statistico è il giudice.

Nessun test parte senza uno step a bassa conversione identificato. Nessun test si dichiara
"conclusivo" prima del campione minimo. [DM] è la risposta corretta quando il dato non esiste
ancora — non un numero inventato. La baseline si stabilisce al primo funnel live, non prima.

---

## P4 — Una variante = un solo elemento cambiato

Cambiare headline + prezzo + posizione CTA + order bump in un unico test non permette di
sapere cosa ha funzionato. Cambiare un solo elemento per test è più lento ma produce conoscenza
reale, che si accumula in `infobusiness/vendite/funnel/tests/`. Il rollout avviene su una %
del traffico, mai su tutto: una variante non testata non sostituisce il controllo finché i
dati non lo confermano.

La tentazione di "rifare tutto" arriva quando il funnel non performa. La risposta corretta è:
identificare lo step più debole, testare la variante minima, aspettare il campione.

---

## P5 — Prove non promesse, anche nell'offerta e nell'evergreen (Mandato Art.2)

Nessun claim senza documentazione. Nessun caso studio inventato. Soprattutto: l'evergreen NON
usa scarcity artificiale. Una "deadline" su un funnel permanente è una bugia. Se esiste un
bonus a scadenza, la scadenza deve essere reale e applicata davvero. IB-VEND-QA blocca ogni
deadline finta, contatore farlocco o "ultimi posti" non veri.

Questo vale anche per i numeri: un opt-in rate atteso o una conversione stimata pre-lancio
sono [DM], non promesse.

---

## P6 — Il reparto NON scrive copy da zero; lo assembla e lo gata

La direzione APSOC e i framework arrivano da 04-MARKETING. IB-VEND-SALESPAGE applica la skill
`cro-copy-architect` per assemblare e adattare il copy della sales page e delle email; non
inventa una linea editoriale di brand. IB-VEND-QA verifica APSOC ≥80 + "prove non promesse"
su ogni elemento prima del deploy.

Il confine: strategia di brand e copy di reparto → MARKETING; assemblaggio funnel + gate
vendite → IB-L2-VEND. Se il reparto inizia a definire la voce di brand, il confine si rompe.

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili (più stringenti dei principi)
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confine B-003 / 04-MARKETING / 06-PLATFORM in dettaglio
- [[README]] · `README.md` — missione del reparto
