# Team L3 — WF-REPLY-FOLLOWUP (wrap)

> **ADR-003: runtime INVARIATO.** Path verificati su disco: 2026-06-11.
> E' il team che converte risposte in call prenotate: l'anello tra outreach e revenue.

## Identita'

| Campo | Valore |
|---|---|
| ID team | WF-REPLY-FOLLOWUP |
| Reparto | A2-ACQUISIZIONE |
| Coordinator | AG-A2-COORD |
| Stato | **ACTIVE** |

## Runtime (path reali, verificati)

| Componente | Path | Ruolo L4 |
|---|---|---|
| Monitor risposte | `Outreach/Outreach Workflow/agents/reply_monitor.py` | T-reply-triage |
| Gestione conversazione | `Outreach/Outreach Workflow/agents/conversation_manager.py` | T-reply-triage |
| Follow-up writer | `Outreach/Outreach Workflow/agents/followup_writer.py` | T-followup |
| Entrypoint follow-up | `Outreach/run_followup_b3.bat` | run operativa |
| Skill triage | `.claude/skills/outreach-reply-triage/SKILL.md` (NUOVA F4) | T-reply-triage |

## Flusso

```
reply_monitor -> triage (4 classi) -> conversation_manager -> followup_writer -> booking call
```

Classi triage (skill outreach-reply-triage):
INTERESSATO -> proponi call | OBIEZIONE -> rispondi con prova (max 2 follow-up) |
NO -> archivia, ZERO follow-up | OOF -> attendi/archivia

## Interfaccia contract

- **Input**: risposte dai 3 canali (email/LI/IG)
- **Output**: call prenotata -> **`HC-A2-A3-call`** verso A3-PREVENTIVI
  Questo e' lo handoff che AVVIA un ciclo revenue nel project state.

## Log memoria (B2) — IL PIU' IMPORTANTE

Ogni call prenotata apre un ciclo nel project state:

```powershell
# 1. Crea il ciclo (manuale o via Claude): aggiungi cycle object in state.json (cycles.active)
# 2. Logga lo handoff:
powershell -File scripts/agency-trace.ps1 -CycleId "CY-YYYYMMDD-NNN" -Step "A2.REPLY" `
  -Event "handoff_sent" -From "A2" -To "A3" -Hc "HC-A2-A3-call" `
  -Agent "WF-REPLY-FOLLOWUP" -Summary "call prenotata con <azienda> per <data>"
```

PII: thread conversazione -> `aidefence_has_pii` prima dello store in agency/conversations.

## Connessioni

- `company/01-agency/A2-ACQUISIZIONE/handoffs/HC-A2-A3-call.json`
- `company/01-agency/A3-PREVENTIVI/BACKBONE.md` — riceve la call
- `.claude/skills/outreach-reply-triage/SKILL.md`
