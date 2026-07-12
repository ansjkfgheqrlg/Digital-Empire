---
Type: WORKFLOW
Status: Active (WRAPPA — runtime esistente, intoccabile)
Tags: #workflow #agency #acquisizione #outreach #instagram #bibbia #pii #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-OUTREACH-INSTAGRAM — DM pattern 2 messaggi + follow-up

> **ID:** WF-A2-INSTAGRAM · **Owner:** `ag-a2-coord` · **Esecutore:** `ag-a2-ig` · **Reparto:** A2 (01-AGENCY)
> **Trigger:** run giornaliera schedulata (09-OPERATIONS), `/avvia-ig` o `/avvia-parallel`
> **ADR-003:** WRAPPA il flow Instagram esistente (`run_today.py`, `personalize.py`, `check_replies.py`). Zero modifiche al codice.

---

## Scopo

Inviare DM a profili target entro il cap reale di **30 DM/gg**, con il **pattern a 2 messaggi**
(corpo APSOC + link `presentazione-empire.vercel.app`) e follow-up automatico ai non-risponditori.
Il copy passa per il gate Bibbia; ogni conversazione passa il **PII-scan** prima dello store.
Il workflow avvolge il motore Instagram esistente — non lo riscrive (REGOLE R7).

---

## Cap reali (non superabili — REGOLE R2)

- Instagram: **≤30 DM/gg.** Cap raggiunto → run del giorno chiusa; il resto slitta.

---

## Attori

| Step | Agente A2 | Motore wrappato [WRAPPA] |
|---|---|---|
| Apertura run + pre-flight sessione | `ag-a2-coord` | — |
| Scout + qualify + DM | `ag-a2-ig` | `run_today.py`, `personalize.py` |
| Gate Bibbia sul copy | `ag-a2-qa` | `bibbia_team.py` |
| Check risposte | `ag-a2-ig` | `check_replies.py` |

---

## Flusso passo-passo

```
[TRIGGER] run schedulata / /avvia-ig / /avvia-parallel
         │
         ▼
[STEP 1] AG-A2-COORD + AG-A2-IG — pre-flight sessione
  → verifica sessione Instagram valida. Scaduta → run NON parte, alert.
  → legge cap residuo del giorno (≤30 DM)
  → GATE-0: sessione ok + cap_residuo > 0 → prosegui

         │
         ▼
[STEP 2] AG-A2-IG — hashtag scout + qualifier
  → individua profili target via hashtag e li qualifica

         │
         ▼
[STEP 3] AG-A2-WRITE/QA — copy DM + GATE BIBBIA
  → corpo APSOC (P prima di S) + CTA singola → presentazione-empire.vercel.app
  → GATE BIBBIA (3 check) ── FAIL → STOP, riscrive ── PASS → invio

         │
         ▼
[STEP 4] AG-A2-IG — DM pattern 2 messaggi (cap 30/gg)
  → messaggio 1: corpo · messaggio 2: link presentazione
  → cap 30 raggiunto → chiude la run del giorno
  → MAI doppio DM a chi ha già risposto

         │
         ▼
[STEP 5] AG-A2-IG — follow-up + PII-scan + routing
  → follow-up automatico SOLO ai non-risponditori
  → PII-scan (aidefence_has_pii) prima dello store della conversazione
  → risposte → AG-A2-TRIAGE (WF-REPLY-BOOKING)
  → aggiorna agency/a2/instagram/state.json (no PII)
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Sessione | Sessione Instagram valida + cap residuo > 0 | AG-A2-COORD/IG | Avvio run |
| **G1 — Gate Bibbia** | 3 check PASS sul copy DM | AG-A2-QA | Invio DM |
| G2 — Cap | dm_inviati_oggi < 30 | AG-A2-IG | DM oltre cap |
| G3 — No doppio DM | nessun secondo DM a chi ha risposto | AG-A2-IG | DM duplicato |
| G4 — PII-scan | pii_scan = passed | AG-A2-IG | Store conversazione |

---

## Input / Output del workflow

**Input trigger:**
```json
{ "canale": "instagram", "hashtag_target": ["#..."], "cap_dm": 30 }
```

**Output finale (state giornaliero):**
```json
{
  "data": "YYYY-MM-DD",
  "dm_inviati_oggi": 0,
  "cap_residuo": 30,
  "followup_pending": 0,
  "stato_run": "completata | cap_raggiunto | sospesa_sessione"
}
```

---

## State

File: `agency/a2/instagram/state.json` — contatore DM e cap residuo. Nessuna PII
nello schema (REGOLE R3). Ripartibilità a freddo dal cap residuo del giorno.

---

## Failure

- Sessione Instagram scaduta → run sospesa, alert, runbook rinnovo.
- Warning di limitazione piattaforma → riduzione ritmo, segnalazione ad AG-A2-COORD.
- PII-scan fallito → store bloccato, segnalazione (rischio sicurezza).
- Tentato superamento cap o doppio DM → bloccato (REGOLE R2).

---

## Connessioni

- [[ag-a2-ig]] · `agenti/ag-a2-ig.md` — esecutore del workflow
- [[ag-a2-qa]] · `agenti/ag-a2-qa.md` — gate Bibbia sui DM
- [[WF-REPLY-BOOKING]] · `workflow/WF-REPLY-BOOKING.md` — gestione risposte
- [[regole/REGOLE]] · `regole/REGOLE.md` — R2 cap IG, R3 PII
