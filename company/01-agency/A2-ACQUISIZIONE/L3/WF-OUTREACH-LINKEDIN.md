# Team L3 — WF-OUTREACH-LINKEDIN (wrap)

> **ADR-003: runtime INVARIATO.** Path verificati su disco: 2026-06-11.

## Identita'

| Campo | Valore |
|---|---|
| ID team | WF-OUTREACH-LINKEDIN |
| Reparto | A2-ACQUISIZIONE |
| Coordinator | AG-A2-COORD |
| Stato | **ACTIVE** |
| Cap reali | 20 connessioni + 20 messaggi + 30 commenti/gg — MAI aumentare senza dati |

## Runtime (path reali, verificati)

| Componente | Path | Ruolo L4 |
|---|---|---|
| Scrape lead | `Outreach/LinkedIn Automation/01_scrape_leads.py` | T-scraper |
| Connessioni | `Outreach/LinkedIn Automation/02_send_connections.py` | T-li-engage |
| Check accettate | `Outreach/LinkedIn Automation/03_check_accepted.py` | T-li-engage |
| Messaggi | `Outreach/LinkedIn Automation/04_send_messages.py` | T-li-engage |
| Follow-up | `Outreach/LinkedIn Automation/05_send_followups.py` | T-followup |
| Commenti | `Outreach/LinkedIn Automation/comment_posts.py` | T-li-engage |
| Check risposte | `Outreach/LinkedIn Automation/check_replies.py` | T-reply-triage |
| Config | `Outreach/LinkedIn Automation/config.py` | — |
| Entrypoint | `Outreach/run_linkedin_only.py` | run operativa |

## Flusso

```
01_scrape -> 02_connections -> 03_check_accepted -> 04_messages -> 05_followups
                + comment_posts (engagement parallelo)
```

## Interfaccia contract

- **Input**: lead qualificati via `HC-A1-A2-leads`
- **Output**: risposta interessata -> `HC-A2-A3-call` (A3)

## Log memoria (B2)

```powershell
powershell -File scripts/agency-trace.ps1 -CycleId "DAILY" -Step "A2.OUTREACH" `
  -Event "completed" -From "A2" -Agent "WF-OUTREACH-LINKEDIN" `
  -Summary "LI: N connessioni, M messaggi, K commenti"
```

## Rischio canale

Ban/limitazione LinkedIn: cap conservativi GIA' attivi, pattern umanizzazione esistenti.
Su error rate anomalo: STOP run, attendere 24h, log in agency/reasoning.

## Connessioni

- `company/01-agency/A2-ACQUISIZIONE/BACKBONE.md`
- `WF-OUTREACH-EMAIL.md` — canale primario (fallback se LI limitato)
