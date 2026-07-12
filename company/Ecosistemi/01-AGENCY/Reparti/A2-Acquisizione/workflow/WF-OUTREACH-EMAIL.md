---
Type: WORKFLOW
Status: Active (WRAPPA — runtime esistente, intoccabile)
Tags: #workflow #agency #acquisizione #outreach #email #apsoc #bibbia #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-OUTREACH-EMAIL — Email fredde a lead qualificati

> **ID:** WF-A2-EMAIL · **Owner:** `ag-a2-coord` · **Reparto:** A2 Acquisizione (01-AGENCY)
> **Trigger:** run giornaliera schedulata (09-OPERATIONS) o `/avvia-email`
> **ADR-003:** WRAPPA il runtime esistente — `orchestrator.py`, `run.py`, `sender.py`, `bibbia_team.py`. Zero modifiche al codice fino a validazione del wrapper.

---

## Scopo

Inviare email fredde APSOC a lead qualificati, entro i cap reali (**≤500/gg, cap 100/h**),
con CTA standard `presentazione-empire.vercel.app`. Ogni email passa il **gate Bibbia
(3 check sequenziali)** PRIMA dell'invio. Il workflow avvolge la pipeline esistente:
non riscrive nessuno script (REGOLE R7).

---

## Cap reali (non superabili — REGOLE R2)

- Email: **≤500/gg**, **cap 100/h**. Cap raggiunto → run del giorno chiusa; il resto slitta.

---

## Attori

| Step | Agente A2 | Motore wrappato [WRAPPA] |
|---|---|---|
| Apertura run + pre-flight | `ag-a2-coord` | `orchestrator.py` / `run.py` |
| Angolo APSOC | `ag-a2-strat` | `strategist.py`, `insight.py` |
| Scrittura copy | `ag-a2-write` | `writer.py`, `humanizer.py`, `copy_knowledge.py` |
| Gate Bibbia | `ag-a2-qa` | `bibbia_team.py` |
| Invio + rate limiter | `ag-a2-send` | `sender.py` |

---

## Flusso passo-passo

```
[TRIGGER] run schedulata / /avvia-email
         │
         ▼
[STEP 1] AG-A2-COORD — pre-flight + carico batch
  → verifica credenziali (token FB / SMTP). Scaduta → run NON parte, alert.
  → legge cap residuo del giorno da agency/a2/email/state.json
  → carica batch lead qualificati (leads.db, score >= soglia)
  → GATE-0: credenziali ok + cap_residuo > 0 → prosegui

         │
         ▼
[STEP 2] AG-A2-STRAT — angolo di attacco (per lead)
  → insight.py: segnali reali del lead (no invenzioni)
  → deduce awareness_level; sceglie P dominante, S leva, O probabile
  → dichiara dosaggio APSOC; consegna brief vincolante ad AG-A2-WRITE

         │
         ▼
[STEP 3] AG-A2-WRITE — copy APSOC
  → writer.py + copy_knowledge.py: scrive in ordine A→P→S→O→CTA (P PRIMA di S)
  → humanizer.py: varia per evitare pattern bulk
  → CTA singola → presentazione-empire.vercel.app
  → consegna messaggio ad AG-A2-QA

         │
         ▼
[STEP 4] AG-A2-QA — GATE BIBBIA (3 check sequenziali) — BLOCCANTE
  → check 1: struttura APSOC (P prima di S)  ── FAIL → STOP, torna a WRITE
  → check 2: CTA corretta (link presentazione) ─ FAIL → STOP, torna a WRITE
  → check 3: no dependency-language            ─ FAIL → STOP, torna a WRITE
  → tutti PASS → autorizza l'invio
  → registra esito (pass/fail + check) in agency/a2/email/

         │  (solo PASS)
         ▼
[STEP 5] AG-A2-SEND — invio entro cap
  → verifica cap residuo (≤500/gg, ≤100/h); esaurito → coda al giorno/ora dopo
  → sender.py invia con rate limiting
  → logga invio in agency/outreach; aggiorna cap_residuo, bounce
  → cap_residuo = 0 → chiude la run del giorno

         │
         ▼
[STEP 6] Risposte → WF-REPLY-BOOKING (event-driven)
  → reply_monitor.py rileva → AG-A2-TRIAGE classifica
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Pre-flight | Credenziali valide + cap residuo > 0 | AG-A2-COORD | Avvio run |
| **G1 — Gate Bibbia** | I 3 check (APSOC · CTA · no-dependency) tutti PASS | AG-A2-QA | **Invio del messaggio** |
| G2 — Cap | inviati_oggi < 500 e ultimo'ora < 100 | AG-A2-SEND | Invio oltre cap |

---

## Input / Output del workflow

**Input trigger:**
```json
{ "batch_id": "BATCH-20260622-001", "canale": "email", "lead_ref": "leads.db (score >= soglia)" }
```

**Output finale (state batch):**
```json
{
  "batch_id": "BATCH-20260622-001",
  "inviati": 0,
  "cap_residuo": 500,
  "bounce": 0,
  "gate_bibbia": {"pass": 0, "fail": 0},
  "stato_run": "completata | cap_raggiunto | sospesa_credenziale"
}
```

---

## State

File: `agency/a2/email/state.json` — aggiornato a ogni invio (cap residuo, gate
pass/fail). Permette la **ripartibilità a freddo**: una run interrotta riprende dal cap residuo
del giorno senza risuperare i lead né sforare i cap. Schema completo in `state/README.md`.

---

## Failure

- Credenziale scaduta in pre-flight → run NON parte, alert, runbook rinnovo.
- Gate Bibbia boccia in serie lo stesso template (2+ cicli) → template ritirato, refresh ad A5/04-MARKETING.
- Bounce rate in salita → Sentinel Quality + pattern in `agency/reasoning`.
- Cap orario/giornaliero raggiunto → coda automatica, nessun superamento (REGOLE R2).

---

## Connessioni

- [[ag-a2-qa]] · `agenti/ag-a2-qa.md` — il gate Bibbia di questo workflow
- [[ag-a2-send]] · `agenti/ag-a2-send.md` — invio + rate limiter
- [[WF-REPLY-BOOKING]] · `workflow/WF-REPLY-BOOKING.md` — gestione risposte
- [[ARCHITETTURA]] · `ARCHITETTURA.md §2` — pipeline STRAT→WRITE→QA→SEND
