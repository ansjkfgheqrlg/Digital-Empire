# 🔨 07 — FORGE

> **Livello:** L1 · **Priorità:** TRASVERSALE · **Stato:** parziale (skill-creator + content-forge installati)
> Dossier completo: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §FORGE

## Missione

Fabbrica organizzativa di Digital Empire: **crea skill, agenti, team e interi ecosistemi**.
Unico ecosistema autorizzato ad assumere e ritirare agenti dal roster.
Ogni nuovo componente organizzativo nasce qui.

## Come funziona (processo obbligatorio)

```
Richiesta (gap funzionale documentato)
  ↓
forge-intake (brief: problema → spec → eval criteria)
  ↓
MKD — Markdown Design Document (spec completa)
  ↓
Build (skill-creator / content-forge / System OMEGA)
  ↓
Eval gate (evals.json superato)
  ↓
Consegna al richiedente + update registro-agenti.yaml
```

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Skill Lab | forgia skill Claude Code (kernel + references + evals) | `Reparti/Skill-Lab/` |
| L2.2 | Agent Factory | crea agenti (identità, I/O, reasoning, KPI) | `Reparti/Agent-Factory/` |
| L2.3 | Team Assembly | assembla team canonici (coordinator + workers) | `Reparti/Team-Assembly/` |
| L2.4 | Ecosystem Design | progetta nuovi ecosistemi L1 (solo Board può approvare) | `Reparti/Ecosystem-Design/` |

## Motori esistenti (già installati)

| Tool | Funzione | Path |
|---|---|---|
| skill-creator | forgia skill da documenti/transcript | `~/.claude/skills/skill-creator/` |
| content-forge v2 | trasforma raw in 8 target (skill, agent, team, wiki, ...) | `~/.claude/skills/content-forge/` |
| System OMEGA | creazione progetti e skill strutturate | `SKILL & Agenti/System_Omega*/` |
| SPARC agents | spec → pseudocode → arch → refinement → completion | skill installate |
| agency-scalping | skill di scaling agenzia | `~/.claude/skills/agency-scalping/` |

## Skill da forgiare (P0 — vedere Chief-Forge.md)

empire-verify · forge-intake · ecosystem-scaffold · team-canonical-template ·
context-pack · wiki-sync-guard · empire-swarm · cost-ledger · budget-guard · empire-brand-gate

## Come si collega al Backbone

- **BUS:** riceve richieste da tutti gli ecosistemi; consegna skill/agenti/team
- **IDENTITY-HR:** aggiorna `registro-agenti.yaml` dopo ogni assunzione/ritiro
- **BRAIN:** ReasoningBank — distilla pattern da ogni build
- **Chief Forge:** supervisione C-Suite diretta

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` · Aggiornato: 2026-06-11*
