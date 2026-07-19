---
Type: SCRIPTS
Status: Active (wrap — runtime esistente)
Tags: #scripts #agency #acquisizione #outreach #wrap #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# Script — A2 Acquisizione / Outreach

> **ADR-003:** questo file NON descrive script nuovi. Descrive come i motori ESISTENTI del
> runtime di outreach vengono INVOCATI dal reparto, tramite gli entrypoint installati.
> Nessuno script qui viene scritto, modificato o sostituito. I file reali vivono FUORI da A2.

---

## Dove vive il runtime (intoccabile)

```
Outreach/Outreach Workflow/          ← motore email + reply
├── orchestrator.py                  ← AG-A2-COORD: apre la run, fan-out canali
├── agents/strategist.py, insight.py ← AG-A2-STRAT: angolo APSOC per lead   [WRAPPA]
├── agents/writer.py, humanizer.py,
│   copy_knowledge.py                ← AG-A2-WRITE: copy APSOC + variazione   [WRAPPA]
├── agents/bibbia_team.py            ← AG-A2-QA: gate Bibbia 3 check          [WRAPPA]
├── agents/sender.py                 ← AG-A2-SEND: invio + rate limiter       [WRAPPA]
├── agents/followup_writer.py        ← AG-A2-FUP: sequenze follow-up          [WRAPPA]
├── agents/reply_monitor.py,
│   conversation_manager.py          ← AG-A2-TRIAGE / AG-A2-BOOK
├── run.py, run_followup.py,
│   run_reply_manager.py             ← entrypoint run
└── leads.db, emails_*_ready.json    ← state del motore (non duplicato qui)

Outreach/LinkedIn Automation/        ← motore LinkedIn
├── 01_scrape_leads.py
├── 02_send_connections.py
├── 03_check_accepted.py
├── 04_send_messages.py
├── 05_send_followups.py             ← AG-A2-LI: pipeline 01→05               [WRAPPA]
└── comment_posts.py                 ← AG-A2-LI: 30 commenti/gg               [WRAPPA]

Outreach/Instagram Automation/       ← motore Instagram
├── run_today.py                     ← AG-A2-IG: DM del giorno                [WRAPPA]
├── personalize.py, config.py
└── check_replies.py                 ← triage risposte IG
```

---

## Invocazione tramite skill installate (entrypoint preferito)

| Skill | Workflow attivato | Motore invocato (intoccabile) |
|---|---|---|
| `/avvia-email` | WF-OUTREACH-EMAIL | `run.py` → orchestrator.py → strategist → writer → bibbia_team → sender |
| `/avvia-linkedin` | WF-OUTREACH-LINKEDIN | scripts `01_…`→`05_…` + `comment_posts.py` |
| `/avvia-ig` | WF-OUTREACH-INSTAGRAM | Instagram `run_today.py` (DM + follow-up) |
| `/avvia-parallel` | EMAIL + INSTAGRAM in parallelo | due finestre, due motori, cap indipendenti |
| `/avvia-scraper` | (a monte) raccolta lead | `scrape_only.py` → popola `leads.db` |
| (event-driven) | WF-REPLY-BOOKING | `run_reply_manager.py` + `reply_monitor.py` + `conversation_manager.py` |

---

## Convenzioni di invocazione (wrap — non build)

- **Pre-flight obbligatorio:** prima di ogni run, AG-A2-COORD verifica credenziali (token FB,
  sessione LinkedIn, sessione Instagram). Credenziale scaduta → la run del canale NON parte.
- **Dry-run:** ogni canale supporta l'anteprima (messaggi + stima volumi) senza invio reale.
  Si usa dry-run quando un template è nuovo o appena rinnovato, prima della run con invio.
- **Cap enforced dal motore:** il rate limiter del `sender.py` e gli operatori canale applicano
  i cap (≤500/gg cap 100/h email · 20+20+30/gg LI · 30 DM/gg IG). Il reparto non li bypassa.
- **Gate prima dell'invio:** la pipeline email passa SEMPRE per `bibbia_team.py` prima di `sender.py`.
- **Nessuna modifica al codice:** se un motore va cambiato → ADR ad AG-DIR (REGOLE R7).
  Questo file descrive l'invocazione, non l'implementazione.

---

## Output e state prodotti dal motore

Il motore scrive il proprio state in `Outreach/Outreach Workflow/` (`leads.db`,
`emails_*_ready.json`, `scrape_checkpoint.json`, sessioni). Il reparto NON duplica questi file:
ne legge gli esiti e scrive il proprio layer di registrazione/learning nei namespace
`agency/outreach` e `agency/a2/{canale}/` (vedi `state/README.md`).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §6` — namespace script e invocazione del motore
- [[state/README]] · `state/README.md` — schema dei namespace memoria del reparto
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
