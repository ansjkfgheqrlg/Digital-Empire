# Team L3 — WF-OUTREACH-EMAIL (wrap)

> **ADR-003: runtime INVARIATO.** Questo file e' l'interfaccia contract+memoria
> attorno alla pipeline email ATTIVA. Nessuna modifica al codice sorgente.
> Path verificati su disco: 2026-06-11.

## Identita'

| Campo | Valore |
|---|---|
| ID team | WF-OUTREACH-EMAIL |
| Reparto | A2-ACQUISIZIONE |
| Coordinator | AG-A2-COORD (mappa a `orchestrator.py`) |
| Stato | **ACTIVE — sistema in produzione, NON TOCCARE** |
| Cap reali | <=500 email/gg, cap 100/h |

## Runtime (path reali, verificati)

| Componente | Path | Ruolo L4 |
|---|---|---|
| Orchestratore | `Outreach/Outreach Workflow/agents/orchestrator.py` | AG-A2-COORD |
| Scraper | `Outreach/Outreach Workflow/agents/scraper.py` + maps_browser/apify/outscraper/google_scraper.py | T-scraper (A1) |
| Qualifier | `Outreach/Outreach Workflow/agents/qualifier.py` | T-qualifier (A1) |
| Strategist | `Outreach/Outreach Workflow/agents/strategist.py` + insight.py | T-strategist |
| Writer APSOC | `Outreach/Outreach Workflow/agents/writer.py` + humanizer.py + copy_knowledge.py | T-writer-apsoc |
| Gate Bibbia | `Outreach/Outreach Workflow/agents/bibbia_team.py` (3 checker) | T-bibbia-qa — BLOCCA |
| Sender | `Outreach/Outreach Workflow/agents/sender.py` | T-sender |
| Storage lead | `Outreach/Outreach Workflow/leads.db` | A1 (usa-cosi') |
| Entrypoint | `Outreach/AVVIA-EMAIL-LIVE.bat`, `Outreach/run_parallel.py`, `Outreach/TEST-EMAIL-10.bat` | run operative |

## Flusso

```
scraper -> qualifier -> strategist -> writer (APSOC) -> GATE BIBBIA (blocca) -> sender
```

## Interfaccia contract

- **Input**: lead qualificati via `HC-A1-A2-leads` (A1-RICERCA)
- **Output**: risposta positiva -> WF-REPLY-FOLLOWUP -> `HC-A2-A3-call` (A3)

## Log memoria (B2)

Dopo ogni run reale, registrare l'esito nel project state:

```powershell
powershell -File scripts/agency-trace.ps1 -CycleId "DAILY" -Step "A2.OUTREACH" `
  -Event "completed" -From "A2" -Agent "WF-OUTREACH-EMAIL" `
  -Summary "email batch: N inviate, M bounce, K reply"
```

Namespace AgentDB: `agency/outreach` (template, performance, esiti Bibbia).

## Regola ferrea B2

Qualsiasi modifica al wrapper si valida in **dry-run e su batch piccolo**
(`TEST-EMAIL-10.bat`) prima di toccare la run da 500. Il rollback del wrap =
rimozione di questo file; il runtime resta intatto.

## Connessioni

- `company/01-agency/A2-ACQUISIZIONE/BACKBONE.md`
- `company/Ecosistemi/01-AGENCY/Workflow/outreach-wrapper.md` (wrap F3, livello ecosistema)
- `Outreach/SISTEMA_OUTREACH_COMPLETO.md` + `Outreach/Outreach Workflow/ARCHITETTURA_COMPLETA.md` (docs runtime)
