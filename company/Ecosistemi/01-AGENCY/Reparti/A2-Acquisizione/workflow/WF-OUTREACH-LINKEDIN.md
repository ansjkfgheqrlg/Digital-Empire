---
Type: WORKFLOW
Status: Active (WRAPPA — runtime esistente, intoccabile)
Tags: #workflow #agency #acquisizione #outreach #linkedin #bibbia #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-OUTREACH-LINKEDIN — Connessioni + Messaggi + Commenti

> **ID:** WF-A2-LINKEDIN · **Owner:** `ag-a2-coord` · **Esecutore:** `ag-a2-li` · **Reparto:** A2 (01-AGENCY)
> **Trigger:** run giornaliera schedulata (09-OPERATIONS) o `/avvia-linkedin`
> **ADR-003:** WRAPPA gli script esistenti `01→05` + `comment_posts.py`. Zero modifiche al codice.

---

## Scopo

Massimizzare l'engagement su profili target entro i cap reali: **20 connessioni + 20 messaggi
+ 30 commenti/gg**. I messaggi APSOC passano per il gate Bibbia prima dell'invio; i commenti
sono umani (pattern di umanizzazione), mai bulk identico. Il workflow avvolge gli script di
automazione LinkedIn esistenti — non li riscrive (REGOLE R7).

---

## Cap reali (non superabili — REGOLE R2)

- **20 connessioni/gg + 20 messaggi/gg + 30 commenti/gg.** Cap raggiunto su un'attività →
  quell'attività si ferma per il giorno; le altre proseguono fino al loro cap.

---

## Attori

| Step | Agente A2 | Motore wrappato [WRAPPA] |
|---|---|---|
| Apertura run + pre-flight sessione | `ag-a2-coord` | — |
| Scrape lead | `ag-a2-li` | `01_scrape_leads.py` |
| Connessioni | `ag-a2-li` | `02_send_connections.py` |
| Check accettati | `ag-a2-li` | `03_check_accepted.py` |
| Messaggi (copy gated) | `ag-a2-li` + `ag-a2-qa` | `04_send_messages.py` + `bibbia_team.py` |
| Follow-up | `ag-a2-li` | `05_send_followups.py` |
| Commenti umani | `ag-a2-li` | `comment_posts.py` |

---

## Flusso passo-passo

```
[TRIGGER] run schedulata / /avvia-linkedin
         │
         ▼
[STEP 1] AG-A2-COORD + AG-A2-LI — pre-flight sessione
  → verifica sessione LinkedIn valida. Scaduta → run NON parte, alert, runbook.
  → legge state del giorno (fatti_oggi / cap residui)
  → GATE-0: sessione ok → prosegui

         │
         ▼
[STEP 2] AG-A2-LI — scrape + connessioni (cap 20/gg)
  → 01_scrape_leads.py: profili target
  → 02_send_connections.py: fino a 20 richieste connessione
  → cap 20 raggiunto → ferma le connessioni per il giorno

         │
         ▼
[STEP 3] AG-A2-LI — check accettati
  → 03_check_accepted.py: chi ha accettato → eleggibile al messaggio

         │
         ▼
[STEP 4] AG-A2-WRITE/QA — messaggio APSOC + GATE BIBBIA (cap 20/gg)
  → copy APSOC per il profilo (P prima di S, CTA → presentazione-empire.vercel.app)
  → GATE BIBBIA (3 check) ── FAIL → STOP, riscrive ── PASS → invio
  → 04_send_messages.py: fino a 20 messaggi; cap 20 → ferma messaggi per il giorno

         │
         ▼
[STEP 5] AG-A2-LI — commenti umani (cap 30/gg)
  → comment_posts.py: fino a 30 commenti umani su post target (no bulk identico)
  → cap 30 → ferma i commenti per il giorno

         │
         ▼
[STEP 6] AG-A2-LI — follow-up + routing risposte
  → 05_send_followups.py: follow-up ai non-risponditori (mai a un "no")
  → risposte → AG-A2-TRIAGE (WF-REPLY-BOOKING)
  → aggiorna agency/02-acquisizione/linkedin/state.json
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Sessione | Sessione LinkedIn valida | AG-A2-COORD/LI | Avvio run |
| **G1 — Gate Bibbia** | 3 check PASS sul messaggio | AG-A2-QA | Invio messaggio |
| G2 — Cap | conn <20, msg <20, commenti <30 | AG-A2-LI | Azione oltre cap |
| G3 — Commenti umani | nessun commento bulk identico | AG-A2-LI | Commento non umanizzato |

---

## Input / Output del workflow

**Input trigger:**
```json
{ "canale": "linkedin", "lead_ref": "profili target", "cap": {"connessioni": 20, "messaggi": 20, "commenti": 30} }
```

**Output finale (state giornaliero):**
```json
{
  "data": "YYYY-MM-DD",
  "fatti_oggi": {"connessioni": 0, "messaggi": 0, "commenti": 0},
  "accettazioni_pending": 0,
  "stato_run": "completata | cap_raggiunto | sospesa_sessione"
}
```

---

## State

File: `agency/02-acquisizione/linkedin/state.json` — contatori per attività aggiornati durante
la run. Ripartibilità a freddo: una run interrotta riprende dai cap residui del giorno.

---

## Failure

- Sessione LinkedIn scaduta → run sospesa, alert, runbook rinnovo.
- Warning di limitazione account → riduzione del ritmo, segnalazione ad AG-A2-COORD.
- Tentato superamento cap → bloccato (REGOLE R2); nessun invio in bulk non approvato.

---

## Connessioni

- [[ag-a2-li]] · `agenti/ag-a2-li.md` — esecutore del workflow
- [[ag-a2-qa]] · `agenti/ag-a2-qa.md` — gate Bibbia sui messaggi
- [[WF-REPLY-BOOKING]] · `workflow/WF-REPLY-BOOKING.md` — gestione risposte
- [[regole/REGOLE]] · `regole/REGOLE.md` — R2 cap LinkedIn
