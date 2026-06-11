# Team L3 — WF-OUTREACH-INSTAGRAM (wrap)

> **ADR-003: runtime INVARIATO.** Path verificati su disco: 2026-06-11.
> **STATO: SOSPESO — blocker B-001 (token FB scaduto).**

## Identita'

| Campo | Valore |
|---|---|
| ID team | WF-OUTREACH-INSTAGRAM |
| Reparto | A2-ACQUISIZIONE |
| Coordinator | AG-A2-COORD |
| Stato | **SUSPENDED — token FB scaduto (B-001, owner: Max)** |
| Cap reali | 30 DM/gg, pattern 2 messaggi (corpo + link) |

## Runtime (path reali, verificati)

| Componente | Path | Ruolo L4 |
|---|---|---|
| Agenti DM | `Outreach/Instagram Automation/agents/` | T-ig-dm |
| Check risposte | `Outreach/Instagram Automation/check_replies.py` | T-reply-triage |
| Config | `Outreach/Instagram Automation/config.py` | — |
| Checklist operativa | `Outreach/Instagram Automation/daily_checklist.md` | runbook umano |
| Entrypoint | `Outreach/run_ig_email.py` | run operativa |

## Blocker B-001 — runbook sblocco (per Max)

1. Meta Developer Console -> rinnovo token FB/IG
2. Aggiorna il token nel `.env` locale (NON va in git — .gitignore attivo)
3. Run di test: 1-2 DM su account di prova
4. Se OK: riattiva run giornaliera 30 DM/gg
5. Aggiorna `company/Memory/state/agency/state.json`: rimuovi blocker B-001
6. Logga: `scripts/agency-trace.ps1 -CycleId "SYSTEM" -Step "A2.OUTREACH" -Event "blocker_resolved" -From "HUMAN" -Summary "token FB rinnovato, IG riattivato"`

## Interfaccia contract

- **Input**: lead qualificati via `HC-A1-A2-leads` (con instagram_handle valido)
- **Output**: risposta interessata -> `HC-A2-A3-call` (A3)

## Log memoria (B2)

```powershell
powershell -File scripts/agency-trace.ps1 -CycleId "DAILY" -Step "A2.OUTREACH" `
  -Event "completed" -From "A2" -Agent "WF-OUTREACH-INSTAGRAM" `
  -Summary "IG: N DM inviati, M risposte"
```

## Connessioni

- `company/01-agency/A2-ACQUISIZIONE/BACKBONE.md`
- `company/Memory/state/agency/state.json` — blocker B-001
