# Master App Builder — skill ufficiale

Skill di progetto (project-level, `.claude/skills/master-app-builder/`), condivisa via repo con chiunque lavori su Digital Empire (Max o Gael).

## Comando

```
/master-app-builder
```

Claude Code la propone automaticamente anche in autonomia quando il task è "crea/costruisci una nuova app/tool", grazie alla `description` nel frontmatter di `SKILL.md`.

## Cosa fa, in breve

1. **Studia prima di costruire** (Fase 0.0): cerca nel repo un'app precedente con dominio/stack/UI simile (PreventivoForge, EmpireDesk, ecc.) e riusa il pattern invece di reinventarlo — coerente con ADR-003 (wrap, mai riscrittura).
2. Segue un ciclo a 9 checkpoint (0-8): pattern mining → workflow WF-0 → requisiti (SRS) → architettura → UX → implementazione a vertical slice → test/QA → performance/sicurezza → documentazione → consegna.
3. Coordina una squadra di ~25 ruoli logici (ORCH, PM, ARC, BE, FE, QA, SEC, ...) attivati solo quando il rischio/ambito lo richiede — catalogo esteso in `docs/agents/REGISTRY.md`.
4. Un **Supervisore (SUP)** blocca il passaggio a una fase nuova se la precedente ha lacune materiali.
5. Mantiene memoria persistente a due livelli: `docs/memory/` del progetto in costruzione, e — quando si opera dentro Digital Empire — il livello canonico `company/Memory/` (checkpoint + STATO-EMPIRE, regola memory-first di `CLAUDE.md`).

## Struttura

```
master-app-builder/
├── SKILL.md              # kernel operativo (~550 righe), questo è l'entry point
├── README.md              # questo file
├── docs/
│   ├── agents/REGISTRY.md      # catalogo esteso ruoli/trigger di attivazione
│   ├── rules/                  # workflow.md, graphics-ui.md, links-integrations.md, delivery-workflow.md
│   ├── references/README.md    # catalogo fonti REF (standard, RFC, doc ufficiali)
│   ├── workflows/README.md     # template WF-0
│   └── memory/                 # template INDEX/decisions/risks/references/session_handover per il progetto costruito
└── scripts/
    └── session_bootstrap.py    # verifica ambiente Python (versione, venv, dipendenze)
```

## Origine

Contenuto derivato ed esteso da `master-app-builder-skill/` (bozza di lavoro nella root del repo, non installata come skill). Il tie-in con i reparti EMPIRE OS (`06a-PLATFORM/L2.2 PRODUCT-ENGINEERING`, `06b-FORGE/L2.1 SKILL-WORKS`) e la Fase 0.0 di pattern mining sui progetti reali del repo sono stati aggiunti in fase di installazione ufficiale (vedi checkpoint Memory).
