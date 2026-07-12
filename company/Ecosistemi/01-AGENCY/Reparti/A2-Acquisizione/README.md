---
Type: REPARTO
Status: Active
Tags: #reparto #agency #acquisizione #outreach #apsoc #bibbia #A2
Created: 2026-07-11
Last updated: 2026-07-11
---

# A2 — Acquisizione / Outreach

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A2`
> **Standard:** CF-grade (ADR-007) · **Topologia:** `star` sui 3 canali, `pipeline` dentro ogni canale
> ⚠️ **ADR-003: il runtime è ATTIVO in produzione — si WRAPPA, non si riscrive.**

---

## Missione

Convertire i lead qualificati di A1 in **discovery call prenotate**, su 3 canali (email,
LinkedIn, Instagram), restando dentro i cap reali di piattaforma. CTA standard di ogni
canale: `presentazione-empire.vercel.app`.

A2 non possiede il codice di outreach: il motore vive in `Outreach/Outreach Workflow/`,
`Outreach/LinkedIn Automation/`, `Outreach/Instagram Automation/`. Il reparto lo registra
nell'organigramma, ne definisce i contratti di handoff e aggiunge il layer CF-grade —
**Gate Bibbia formalizzato**, KPI, namespace memoria, state ripartibile.

---

## Roster del reparto (10 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A2-COORD` | Coordinatore Outreach | `agenti/ag-a2-coord.md` | coordinator | sonnet | Apre la run, pre-flight credenziali, carica il batch, fan-out sui canali [WRAPPA `orchestrator.py`] |
| `AG-A2-STRAT` | Stratega d'Angolo | `agenti/ag-a2-strat.md` | worker | sonnet | Definisce l'angolo APSOC per lead [WRAPPA `strategist.py`, `insight.py`] |
| `AG-A2-WRITE` | Copywriter APSOC | `agenti/ag-a2-write.md` | worker | sonnet | Scrive il messaggio APSOC + variazione [WRAPPA `writer.py`, `humanizer.py`] |
| `AG-A2-FUP` | Follow-up Writer | `agenti/ag-a2-fup.md` | worker | sonnet | Sequenze follow-up multi-touch [WRAPPA `followup_writer.py`] |
| `AG-A2-QA` | Gate Bibbia (3 check) | `agenti/ag-a2-qa.md` | verifier | sonnet | **Bloccante pre-invio**: APSOC · CTA · no dependency-language [WRAPPA `bibbia_team.py`] |
| `AG-A2-SEND` | Sender Email | `agenti/ag-a2-send.md` | worker | haiku | Invio + rate limiter + log [WRAPPA `sender.py`] |
| `AG-A2-LI` | Operatore LinkedIn | `agenti/ag-a2-li.md` | worker | haiku | Connessioni + messaggi + commenti [WRAPPA scripts 01→05, `comment_posts.py`] |
| `AG-A2-IG` | Operatore Instagram | `agenti/ag-a2-ig.md` | worker | haiku | DM Instagram + follow-up 2 step [WRAPPA Instagram DM flow] |
| `AG-A2-TRIAGE` | Triage Risposte | `agenti/ag-a2-triage.md` | worker | haiku | Classifica la risposta: interessato / obiezione / no / OOO [skill `outreach-reply-triage`] |
| `AG-A2-BOOK` | Booking Call | `agenti/ag-a2-book.md` | worker | sonnet | Interessato → slot call → conferma → handoff ad A8-Closing |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-OUTREACH-EMAIL** | `workflow/WF-OUTREACH-EMAIL.md` | Pipeline email: STRAT → WRITE → Gate Bibbia → SEND, dentro i cap di deliverability | AG-A2-QA: 3/3 check Bibbia PASS prima dell'invio |
| **WF-OUTREACH-LINKEDIN** | `workflow/WF-OUTREACH-LINKEDIN.md` | Engagement LinkedIn: connessioni + messaggi + commenti entro i cap giornalieri | AG-A2-QA: gate Bibbia sui messaggi; cap giornalieri non sforati |
| **WF-OUTREACH-INSTAGRAM** | `workflow/WF-OUTREACH-INSTAGRAM.md` | DM Instagram con pattern 2 messaggi (corpo + link) e follow-up | AG-A2-QA: gate Bibbia sul DM; cap giornaliero non sforato |
| **WF-REPLY-BOOKING** | `workflow/WF-REPLY-BOOKING.md` | Event-driven: risposta in ingresso → triage → conversazione → call prenotata | AG-A2-QA: PII-scan prima dello store; call confermata con slot |

Entrypoint operativi (skill installate): `/avvia-email` · `/avvia-linkedin` · `/avvia-ig` ·
`/avvia-parallel`. Mappatura completa motore ↔ agente → `scripts/README.md`.

---

## Gate del reparto — Gate Bibbia

**Presidio: AG-A2-QA. Bloccante e binario — niente "quasi".** I 3 check sono **sequenziali**:
il check N+1 parte solo se il check N è PASS.

| # | Check | FAIL se |
|---|---|---|
| 1 | **Struttura APSOC** | Manca una sezione APSOC, oppure la Soluzione compare prima del Problema |
| 2 | **CTA corretta** | CTA assente, link diverso da `presentazione-empire.vercel.app`, doppia CTA confusa |
| 3 | **No dependency-language** | Linguaggio che crea dipendenza dall'agenzia, o promesse non provabili |

Un solo check FAIL → **il messaggio NON parte**: torna ad AG-A2-WRITE con le note del checker.
Se il gate boccia in serie lo stesso template → template ritirato e refresh richiesto ad A5.

---

## KPI e cap reali

| KPI / vincolo | Owner | Valore |
|---|---|---|
| Cap email | AG-A2-SEND | ≤500/gg, cap 100/h — **non negoziabile** |
| Cap LinkedIn | AG-A2-LI | 20 connessioni + 20 messaggi + 30 commenti/gg |
| Cap Instagram | AG-A2-IG | 30 DM/gg |
| Reply rate · positive reply rate | AG-A2-COORD | [DM] — baseline dal giorno 1, mai inventata |
| Call prenotate/settimana | AG-A2-BOOK | [DM] — output finale del reparto |
| Gate Bibbia bypass rate | AG-A2-QA | Target 0 |

I cap non si alzano senza dati: proteggono deliverability e account. Dettaglio → `kpi/KPI.md`.

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A1-Ricerca | Batch di lead qualificati da `leads.db` (score ≥ soglia) |
| ← riceve da | 09-OPERATIONS | Scheduling run giornaliere, cost guard, pre-flight credenziali |
| ← riceve da | A5-Copywriting-Interno | Template rinfrescati (già passati dal Gate Bibbia) |
| → consegna a | A8-Closing | `HC-AG-CL-01` — call confermata + slot + thread di conversazione |
| → consegna a | A7-Account-Management | `HC-AG-AM-01` — apertura anagrafica cliente |
| → consegna a | A5-Copywriting-Interno | Dati di reply reali per il refresh dei template |
| → consegna a | 08-INTELLIGENCE | Obiezioni reali, motivi di rifiuto, domande ricorrenti (anonimizzati) |
| → consegna a | 02-INFO-BUSINESS | Lead "non ora / budget basso" per nurturing |

---

## Namespace AgentDB

**Chiave canonica: `agency/a2`** (+ `agency/outreach` cross-canale) — fonte di verità: `../../NAMESPACE.md`.

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/outreach` | Template attivi, performance per variante, log invii | AG-A2-WRITE, AG-A2-SEND |
| `agency/a2/email` | Per batch: n. inviati, bounce, esiti gate Bibbia | AG-A2-SEND |
| `agency/a2/linkedin` | Connessioni/messaggi/commenti per giorno, accettazioni | AG-A2-LI |
| `agency/a2/instagram` | DM inviati/gg, stato follow-up | AG-A2-IG |
| `agency/a2/reply` | Thread per lead, stato triage, esito | AG-A2-TRIAGE, AG-A2-BOOK |

**Regola PII:** PII-scan (`aidefence_has_pii`) prima di ogni store nel namespace `reply`.
Lo schema di state non contiene PII: solo riferimenti interni e contatori.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md` (R1 gate bloccante · R3 PII-scan)
- Stato e ripartibilità a freddo (cap residuo del giorno) → `state/README.md`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — gerarchia, pipeline, Gate Bibbia, namespace
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A2`
- [[ag-a2-qa]] · `agenti/ag-a2-qa.md` — presidio del Gate Bibbia
- [[WF-OUTREACH-EMAIL]] · `workflow/WF-OUTREACH-EMAIL.md`
- [[WF-REPLY-BOOKING]] · `workflow/WF-REPLY-BOOKING.md`
- [[A1-Ricerca]] · fornitore dei lead qualificati
- [[A8-Closing]] · destinatario della call confermata
