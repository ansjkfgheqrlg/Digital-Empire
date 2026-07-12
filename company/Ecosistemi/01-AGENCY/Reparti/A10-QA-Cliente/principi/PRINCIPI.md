---
Type: CONCEPT
Status: Active
Tags: #principi #agency #qa #audit #indipendenza #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# PRINCIPI — A10 QA-Cliente & Audit Qualità

> I principi dicono **perché**. Le regole (`../regole/REGOLE.md`) dicono **cosa è vietato**.
> Se un principio e una regola confliggono, vince la regola: i principi ispirano, le regole bloccano.

---

## P1 — Chi costruisce non certifica

Un reparto che si auto-valuta non sta valutando: sta firmando. Nel v1 il Gate Delivery viveva
dentro A4, sotto lo stesso coordinatore che aveva pianificato la consegna e che aveva tutto
l'interesse a chiuderla entro il venerdì.

A10 esiste per rompere quel circuito. La linea di riporto ad **AG-DIR** non è organigramma:
è l'unico motivo per cui un FAIL può sopravvivere alla pressione di chi lo riceve.

---

## P2 — A10 audita, non costruisce

Nessun agente di A10 scrive codice di delivery, ripara un ambiente, patcha un workflow o
completa un pacchetto handover. Elenca ciò che non va, con evidenza, e rimanda a chi ha costruito.

Il motivo è semplice: **chi ripara si affeziona alla riparazione**. Un reviewer che ha sistemato
lui stesso lo script non è più in grado di bocciarlo. La separazione dei poteri non è un rituale —
è la condizione tecnica della credibilità del verdetto.

---

## P3 — Il gate blocca, non suggerisce

Un gate che produce "raccomandazioni" è un gate che non esiste. Il verdetto di A10 è **binario**:
PASS o FAIL. Non esistono il "PASS con riserva", il "PASS ma sistemate X", il "FAIL però la
delivery è urgente". Un FAIL ferma la chiusura della delivery e la pubblicazione del case study.

Standard di riferimento: `company/MAXIMILIAN/Skill/maximilian-standard-gate` — criteri espliciti
prima del test, verdetto binario, evidenza citata, nessun verdetto senza prova.

---

## P4 — Si prova col comportamento, non con le affermazioni

"Il workflow gira" non è un'evidenza: è un'opinione. L'evidenza è il comando eseguito sul server
del cliente, l'output ottenuto, l'output atteso. Il codice si esegue, il README si segue,
l'output si guarda, il cliente si osserva mentre lavora.

Corollario duro su G6: un cliente che firma l'UAT ma non sa spiegare cosa ha appena eseguito
**non è autonomo**. La firma misura la cortesia; la spiegazione misura la comprensione.

---

## P5 — L'obiettivo è essere licenziati

Digital Empire è "l'agenzia progettata per essere licenziata". A10 è il reparto che verifica
che la promessa sia mantenuta: zero credenziali DE nel runtime cliente, zero nodi DE, zero
"per quello chiamateci".

Ogni dipendenza residua che A10 lascia passare è un cliente che tra sei mesi non potrà licenziarci —
e quindi una promessa commerciale trasformata in una bugia. G2 e G6 sono il cuore del reparto.

---

## P6 — Un difetto che si ripete è un difetto di sistema

La prima volta è un errore dell'esecutore. La terza volta, sullo stesso step, con clienti diversi,
è un difetto del **motore** — e continuare a bocciare l'esecutore è pigrizia intellettuale.

Per questo A10 non finisce con il verdetto: `AG-A10-LEARN` conta le occorrenze, incrocia le review
con i ticket 90gg e spinge il pattern upstream — ad A4 se è esecuzione, a **07-FORGE** se è struttura.
Un audit che accumula FAIL senza mai cambiare il sistema che li genera è un audit inutile.

---

## Connessioni

- [[REGOLE]] · `../regole/REGOLE.md` — R1..R8, la forma bloccante di questi principi
- [[ARCHITETTURA]] · `../ARCHITETTURA.md §7` — il confine A10 ↔ A4
- [[KPI]] · `../kpi/KPI.md` — come si misura il rispetto di P5 e P6
