---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #marketing-interno #proof #case-study #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# Regole Non Negoziabili — A6 Marketing Interno & Proof

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessun claim pubblico senza proof verificata (Mandato Art.2)

Ogni numero in un case study, in landing, in presentazione o in un post social proof deve
avere una fonte tracciabile in `agency/a6/proof`, verificata dal cliente o dal report di
A4-Delivery. Nessun numero inventato, proiettato, arrotondato o stimato.

Se il dato non esiste o non è verificabile → il case study è qualitativo (descrittivo, senza
numeri), non fabbricato. AG-A6-QA blocca qualsiasi claim numerico senza fonte.

**Perché esiste questa regola:** il posizionamento "agenzia progettata per essere licenziata"
si regge sull'onestà. Un claim falso scoperto distrugge la fiducia su cui si basa tutto il brand.

---

## R2 — Consenso del cliente obbligatorio per ogni pubblicazione

Nessun nome cliente, metrica o testimonianza viene pubblicato senza consenso esplicito e
documentato del cliente. Senza consenso → case study anonimizzato (settore + risultato, senza
nome) o blocco.

Il consenso è registrato in `agency/a6/proof/{cliente}`. AG-A6-QA verifica il consenso prima
di ogni pubblicazione.

**Perché esiste questa regola:** pubblicare dati di un cliente senza permesso è una violazione
del rapporto e potenzialmente legale; un solo episodio compromette la reputazione dell'agency.

---

## R3 — Mai upsell durante il supporto attivo

L'upsell si attiva SOLO dopo Gate Delivery firmato + NPS ≥8. Mai durante i 90gg di supporto
attivo. Il referral ask segue solo una review positiva (NPS ≥8).

Eccezione: nessuna. Se il cliente stesso chiede un'offerta aggiuntiva durante il supporto →
si registra l'interesse e si processa la proposta a fine ciclo, non si interrompe il supporto
con una vendita.

**Perché esiste questa regola:** vendere durante il supporto erode la fiducia e contraddice
"autonomia cliente, non dipendenza". Il valore deve essere dimostrato prima di proporre il next.

---

## R4 — AG-A6-QA è bloccante su ogni asset pubblico

Nessun case study, nessuna modifica landing, nessun post social proof esce senza gate verde
di AG-A6-QA. Il Brand Gate non ha deroga per urgenza.

Se c'è urgenza → AG-A6-COORD può consegnare un output parziale con nota di rischio esplicita
SOLO con approvazione di AG-CONDUCTOR (01-AGENCY). AG-A6-QA documenta ogni bypass non autorizzato.

---

## R5 — P prima di S in ogni case study (Art.4.2 Mandato)

La sezione Problema deve precedere la sezione Soluzione in ogni case study. Il caso APRE con
il problema del cliente, non con Digital Empire. Non esiste un risultato così forte da saltare
il problema: senza problema, non c'è identificazione e il caso non converte.

AG-A6-CASE struttura l'APSOC con `case-study-forge`. AG-A6-QA verifica nel gate finale.
Violazione = FAIL automatico senza analisi aggiuntiva.

---

## R6 — A6 non scrive copy lungo né tocca il codice

A6 non scrive sales page strutturali (vengono da A5-Copywriting-Interno / 04-MARKETING) e non
costruisce né deploya pagine (vengono da 06-PLATFORM). A6 produce case study, proof e brief.

Nessun agente di A6 modifica HTML/CSS della landing o configura il deploy. Ogni modifica
strutturale passa da un ticket a 06-PLATFORM (HC-AG-PL-01), con Brand Gate prima del deploy.

**Perché esiste questa regola:** la responsabilità tecnica è di 06-PLATFORM e la qualità del
copy lungo è presidiata dal gate G1 di A8. A6 che invade questi confini rompe i due sistemi.

---

## R7 — Nessun target di conversione senza dato reale

I KPI del reparto hanno campo [DM] (Da Misurare) ovunque non esista baseline storica. Nessun
agente dichiara "tasso conversione inbound atteso X%" o "lead inbound previsti Y" senza dato
reale da misurazione precedente. I [DM] si riempiono al primo periodo di tracking reale.

Committente che chiede previsioni di inbound pre-lancio → risposta corretta: "la baseline si
stabilisce al primo periodo di tracking. Possiamo dichiarare la struttura della vetrina e i
case study disponibili, non i numeri di conversione." (Mandato Art.2: prove non promesse.)

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ag-a6-qa]] · `agenti/ag-a6-qa.md` — esecutore del Brand Gate (R1, R4, R5)
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confini A6 vs 06-PLATFORM / A5 / 03-CF in dettaglio
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6` — Mandato Art.2 + Art.4.2
