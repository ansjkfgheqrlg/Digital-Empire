---
Type: REGOLE
Status: Active
Tags: #regole #email #lifecycle #pii #gate #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# Regole Non Negoziabili — L2.3 Email & Lifecycle

> Regole bloccanti: nessuna di queste può essere derogata senza ADR esplicito.
> Ogni violazione è un incidente da loggare e segnalare a MKT-Conductor.

---

## R1 — PII check obbligatorio prima di ogni elaborazione lista (Mandato Art.7.2)

`aidefence_has_pii` è OBBLIGATORIO su ogni campione di lista email prima di qualsiasi
elaborazione. Se dati personali non pseudonimizzati sono presenti → blocco immediato.
Escalation a MKT-Conductor e al committente. Il task si ferma finché il committente non
dichiara la base giuridica e pseudonimizza i dati. Non esiste urgenza che deroga questa regola.

## R2 — Il cold outreach operativo resta in 01-AGENCY (ADR-003)

L2.3 non tocca il runtime cold di 01-AGENCY: né `writer.py`, né le sequenze Outreach Workflow,
né le liste cold. L2.3 possiede lo standard qualitativo (APSOC+V) e può fare QA dei template
cold su richiesta esplicita di 01-AGENCY via T-REVIEW di L2.1. Non modifica, non riscrive,
non suggerisce "miglioramenti" al runtime operativo.

## R3 — E2 e E-QA sono gate bloccanti — nessun bypass

E2 (deliverability) e E-QA (qualità finale) sono gate bloccanti su ogni sequenza.
Nessun bypass per urgenza, deadline, richiesta del committente o del Board. L'unico sblocco
lecito è una deroga formale di EMAIL-LEAD con rationale documentato e rischio accettato per
iscritto. Il bypass silenzioso è un incidente che si logga e si segnala.

## R4 — Nessun invio senza gate completo

Nessuna sequenza email parte senza il pacchetto completo: report E2 PASS + report E-QA PASS.
Un output parziale (anche se il 90% è PASS) non è un output consegnabile. Il committente
riceve il pacchetto completo o niente.

## R5 — La scarcity deve essere reale (Mandato Art.2.3)

Nessuna urgenza falsa nelle sequenze email. "Solo 48 ore" è reale solo se il carrello chiude
davvero in 48 ore. "Ultimi posti" è reale solo se ci sono davvero pochi posti. Le finte
scarcity sono vietate dal Mandato Art.2.3 ("prove non promesse") e danneggiano la fiducia
a lungo termine. E-QA verifica questo check sulle email di chiusura.

## R6 — Nessuna spesa ESP reale senza ok esplicito del committente (Mandato Art.4.3)

L'integrazione con ESP (invio effettivo delle email) richiede l'ok esplicito del committente.
Il reparto consegna il pacchetto (sequenze + report); il caricamento su ESP e l'invio è
responsabilità del committente, che accetta esplicitamente prima di procedere.

## R7 — Ogni sequenza ha un sequence_id e un report archivato

Nessuna sequenza è "fatta" senza sequence_id assegnato, report E2 e report E-QA salvati
in `marketing/email/sequences/{tipo}/{sequence_id}/`. La tracciabilità è obbligatoria.
Un output senza id non è rintracciabile, non è auditabile, non è migliorabile.

---

## Connessioni

- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — principi operativi
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — §5 PII policy; §3 confine cold; §4 namespace
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
