---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #agency #acquisizione #outreach #bibbia #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# Regole Non Negoziabili — A2 Acquisizione / Outreach

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation ad AG-DIR, non violazione.

---

## R1 — Il gate Bibbia è bloccante: blocca, non suggerisce

Nessun messaggio (email, DM LinkedIn, DM Instagram, follow-up) parte senza gate Bibbia verde.
I 3 check di `AG-A2-QA` (struttura APSOC · CTA corretta · no dependency-language) sono
**sequenziali e binari**. Un solo check FAIL → il messaggio NON viene inviato: torna al
writer con le note. Il gate non produce suggerimenti opzionali; produce un PASS o un FAIL.

**Perché esiste:** un messaggio fuori standard inviato è irreversibile e danneggia
deliverability e reputazione del brand. Il gate è l'unica barriera pre-invio.

---

## R2 — I cap reali non si superano mai

- Email: **≤500/gg**, **cap 100/h**.
- LinkedIn: **20 connessioni + 20 messaggi + 30 commenti/gg**.
- Instagram: **30 DM/gg**.

Questi cap sono applicati dal rate limiter del sender e dagli operatori canale. Non si alzano
per urgenza, per richiesta del committente, per "recuperare il batch". Un cap raggiunto
chiude la run del canale per quel giorno; il resto del batch slitta al giorno successivo.

**Perché esiste:** superare i cap brucia domini, account e sessioni in modo permanente.
Una modifica ai cap richiede dati + ADR, mai una decisione di run.

---

## R3 — PII-scan prima di ogni store; nessuna PII nello schema di state

Ogni thread di risposta passa il PII-scan (`aidefence_has_pii`) prima di essere scritto in
`agency/02-acquisizione/reply/`. Lo schema di state del reparto contiene solo riferimenti
interni e contatori: nessun nome, email, handle, numero di telefono in chiaro.

**Perché esiste:** lo state è versionato e condiviso; PII in chiaro è un rischio legale e
di sicurezza che nessun beneficio operativo giustifica.

---

## R4 — Nessun KPI inventato: baseline `[DM]` finché non misurate

Nessun agente dichiara un reply rate, un positive reply rate o un tasso di booking "atteso"
senza dato reale. Le metriche non ancora misurate restano `[DM]` (Da Misurare) e si riempiono
al primo ciclo reale. Committente che chiede previsioni pre-lancio → risposta corretta:
"la baseline si stabilisce dal primo ciclo; possiamo dichiarare struttura e cap, non i numeri."

---

## R5 — Mai rispondere a un "no" definitivo

Un lead classificato "no" dal triage chiude la conversazione: nessun follow-up, nessuna
riproposta, nessuna sequenza. Il follow-up multi-touch di `AG-A2-FUP` serve SOLO chi non ha
ancora risposto o ha un'obiezione aperta. Insistere su un "no" è vietato.

**Perché esiste:** rispettare il "no" protegge la reputazione del brand e la deliverability;
forzare non produce call e brucia il dominio/account.

---

## R6 — Nessun handoff ad A8 senza slot call confermato

`AG-A2-BOOK` passa un lead ad A8-Closing (`HC-AG-CL-01`) solo dopo che lo slot della discovery
call è **confermato** dal lead. Un "interessato" senza slot confermato resta in gestione ad
AG-A2-FUP/BOOK; non si scarica su A8 una conversazione incompleta.

---

## R7 — Il runtime non si tocca (ADR-003)

Nessun agente, nessuno script di questo reparto modifica i file di runtime in
`Outreach/Outreach Workflow/`, `Outreach/LinkedIn Automation/`, `Outreach/Instagram Automation/`.
A2 invoca i motori esistenti tramite gli entrypoint (skill `/avvia-*`, .bat, run\*.py) e
documenta come farlo. Qualsiasi necessità di modifica del motore → proposta di ADR ad AG-DIR.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ag-a2-qa]] · `agenti/ag-a2-qa.md` — esecutore del gate Bibbia (R1)
- [[ARCHITETTURA]] · `ARCHITETTURA.md §0` — confine ADR-003 (R7)
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
