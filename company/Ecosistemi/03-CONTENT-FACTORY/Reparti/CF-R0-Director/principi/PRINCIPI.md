---
Type: PRINCIPI
Status: Active
Tags: #principi #content-factory #cf-r0 #director #ordini #multi-tenant
Created: 2026-06-19
Last updated: 2026-06-19
---

# Principi Operativi — CF-R0 Director

> **Reparto:** CF-R0 · **Ecosistema:** 03-CONTENT-FACTORY · **Versione:** v2

---

## P1 — Nessun lavoro senza ordine valido

CF-DE non produce nulla senza un ordine passato il gate CF-D-QA con esito PASS.
Nessuna eccezione, nessun "avvia pure e sistemiamo il contratto dopo". Il gate
è il contratto sociale tra CF-DE e i suoi committenti: rispettarlo tutela tutti.

Un'area che riceve richieste informali fuori dall'ordine deve rifiutarle e
reindirizzare il committente al canale ufficiale (WF-ORDER-INTAKE). Il capo area L1
non ha autorità per bypassare il gate del Director.

---

## P2 — Multi-tenant non negoziabile: brand_kit + icp sono obbligatori

CF-DE è un sistema multi-tenant a ordine (pattern 11 Piano Maestro). Ogni asset
che CF-DE produce appartiene a un brand specifico con voce, palette e target precisi.
Un contenuto prodotto senza brand_kit è un contenuto senza identità: non può essere
consegnato, non può essere pubblicato, non rappresenta il committente.

Il gate CF-D-QA che blocca ordini senza brand_kit non è burocrazia: è la garanzia
che nessun contenuto "generico" esca mai da CF-DE con il nome di un brand che non
lo ha approvato.

---

## P3 — Nessuna metrica inventata (Mandato Art.2)

I KPI di CF-DE sono dichiarati con fonte esplicita (registry `cf/orders`, `state.json`,
`trace.jsonl`) o marcati [DM] (Da Misurare — baseline al primo run reale). Non esiste
una via di mezzo: un numero senza fonte è un'opinione travestita da dato.

CF-D-LEAD rigetta ogni report che presenta numeri senza fonte. CF-D-LEARN rimuove
dalla bozza qualsiasi stima non supportata da evidenza. Il Board riceve solo dati reali.

---

## P4 — La regola coda è non discrezionale

La regola di precedenza (deadline → revenue impact → interno) non è un suggerimento:
è un algoritmo fisso che CF-D-LEAD applica senza eccezioni. Non si privilegia un
committente per simpatie, urgenza percepita o pressione: si applicano i criteri.

Se un committente contesta la priorità assegnata, CF-D-LEAD spiega il criterio
applicato. Se il committente ha informazioni nuove (es. data pubblica non dichiarata
nell'ordine), la priorità viene rivalutata con il nuovo dato e il trace aggiornato.
La regola si applica — non si aggira.

---

## P5 — Il gate QA di CF-R6 è indipendente dalla produzione

L'invariant cardinale di CF-DE: chi produce non si auto-valuta. R6 QA & Gate è
indipendente da tutti i reparti di produzione (CF-R3, CF-R4, CF-R5). Questa
separazione non si bypassa neanche sotto pressione di deadline.

CF-D-LEAD non può autorizzare il bypass del gate QA su nessun ordine. Se il tempo
non è sufficiente per la QA: si rinegozia la deadline con il committente, non si
salta il gate.

---

## P6 — Escalation con dossier, non con rumore

Ogni escalation al Board deve contenere: il problema specifico, il dato che lo
dimostra, la durata del problema (quanti cicli), le opzioni valutate e perché non
bastano, la raccomandazione specifica. "Le cose non funzionano" non è un'escalation:
è una conversazione. Il dossier è la forma dell'escalation in CF-DE.

---

## Connessioni

- [[README]] · `README.md` — roster agenti e workflow del reparto
- [[WF-ORDER-INTAKE]] · `workflow/WF-ORDER-INTAKE.md` — gate BLOCCANTE ordini (P1, P2, P3)
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §1 §3`
