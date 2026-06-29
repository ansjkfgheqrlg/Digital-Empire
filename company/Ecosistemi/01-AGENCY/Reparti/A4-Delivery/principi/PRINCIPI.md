---
Type: PRINCIPI
Status: Active
Tags: #principi #agency #delivery #autonomia #handover #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# Principi — A4 Delivery & Implementazione

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.

---

## P1 — L'agenzia è progettata per essere licenziata

L'obiettivo della delivery non è creare dipendenza, è creare autonomia. A fine handover il
cliente deve poter "licenziare" Digital Empire: eseguire le run da solo, sul suo server, con
i suoi dati, senza chiamare nessuno. Una delivery che lascia il cliente dipendente da DE è
una delivery fallita, anche se "funziona".

La prova pratica: in UAT il cliente esegue **una run da solo**. Se non ci riesce, non è
training mancato del cliente — è handover incompleto da parte nostra.

---

## P2 — Sul server del cliente, non in locale, non in staging

I 3 prodotti girano **sul server del cliente, con la sua macchina, con i suoi dati**. Una
demo in locale DE o in staging non è delivery: è un prototipo. Il valore si trasferisce solo
quando il workflow gira nell'ambiente del cliente e il cliente lo controlla.

Questo cambia l'ordine delle priorità: il giorno-1 è verifica ambiente, non installazione.
Se l'ambiente non regge, tutto il resto è teatro.

---

## P3 — Il countdown 7gg parte solo ad ambiente conforme

La promessa "≤7 giorni" è protetta contrattualmente: parte dal momento in cui l'ambiente
del cliente è conforme, non dalla firma. Se il giorno-1 l'ambiente fallisce, AG-A4-COORD
decide il **rollback**: il countdown non parte, il cliente riceve il runbook dei requisiti,
Max viene allertato. Non si forza una delivery su un ambiente che non regge.

La tentazione di "partire comunque per non perdere il giorno" produce delivery che falliscono
al giorno-5. La risposta corretta è: ambiente prima, countdown poi.

---

## P4 — Wrap, non rewrite (ADR-003)

I motori (Outreach, Content Factory, Second Brain) esistono già. A4 li **clona e parametrizza**
sul server del cliente — non li riscrive. Se un motore ha bisogno di modifiche strutturali,
A4 apre handoff al reparto proprietario (03-CF, 08-INTELLIGENCE), non patcha in locale durante
la delivery.

Riscrivere un motore in delivery significa creare una variante non testata sotto pressione
di tempo: è il modo più rapido per rompere qualcosa che funzionava.

---

## P5 — Multi-tenant è isolamento, non condivisione

Ogni cliente è un tenant isolato: il suo `brand_kit` e il suo `icp` vengono iniettati nei
workflow (pattern 11), ma i suoi dati, i suoi secrets e il suo stato vivono sul suo server.
Nessun dato di un cliente tocca un altro cliente. Nessun secret cliente entra nel namespace DE.

Il pattern 11 multi-tenant non è una comodità tecnica: è la base della fiducia. Un leak tra
tenant è un fallimento di sicurezza, non un bug.

---

## P6 — Prova non promessa anche nei numeri di delivery

Il Mandato Art.2 vale anche qui. Non si promette "UAT pass al 100%" o "NPS 9/10" prima di
avere dati. I KPI hanno [DM] finché non c'è una baseline reale. Il cliente che chiede "quante
delivery avete chiuso in 7 giorni" merita un numero vero, non uno gonfiato.

I [DM] sono onestà, non debolezza: si riempiono alla prima delivery reale.

---

## P7 — Il supporto 90gg punta a rendersi inutile

L'obiettivo del supporto non è massimizzare i ticket, è **decrescerli**. Ogni ticket risolto
deve lasciare il cliente più autonomo del prima. Un trend di ticket piatto o crescente nei
90gg è il segnale che l'handover non ha trasferito davvero la conoscenza.

A 90gg la review con A7 misura proprio questo: il cliente è più autonomo di quando ha firmato?

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili (più stringenti dei principi)
- [[ARCHITETTURA]] · `ARCHITETTURA.md §3` — il Gate Delivery come prova pratica di P1
- [[README]] · `README.md` — missione del reparto
