# 🧠 MEMORY — Indice Maestro (Ecosistema 10, EMPIRE OS)

> **Regola memory-first (pattern #13):** questo file si carica all'INIZIO di ogni sessione
> e prima di ogni task. Dopo ogni task: checkpoint in `checkpoints/`. Una riga per voce,
> solo puntatori — il contenuto vive nei file.

## Stato corrente
- [STATO-EMPIRE.md](STATO-EMPIRE.md) — fase roadmap, lavori in corso, RIPRESA DA

## Decisioni attive (ADR)
- [ADR-001](decisions/ADR-001-empire-os-10-ecosistemi.md) — EMPIRE OS: holding di 10 ecosistemi su modello AION GROUP
- [ADR-002](decisions/ADR-002-memory-first.md) — Pattern memory-first: interroga prima, checkpoint dopo, sempre
- [ADR-003](decisions/ADR-003-migrazione-wrap-non-riscrittura.md) — Migrazione asset = wrap, mai riscrittura; sistemi attivi intoccabili finché sostituto non validato
- [ADR-004](decisions/ADR-004-github-monorepo-sync.md) — Monorepo GitHub ansjkfgheqrlg/digital-empire + sync automatico bidirezionale Max↔Gael

## Checkpoint
- [CP-20260611-001](checkpoints/CP-20260611-001.md) — F1 Scaffolding EMPIRE OS completato (Gael) — gate PASS 92/92
- [CP-20260610-001](checkpoints/CP-20260610-001.md) — Prodotto PIANO-MAESTRO completo (10 dossier, swarm 7 agenti + conductor)
- [CP-20260610-002](checkpoints/CP-20260610-002.md) — GitHub monorepo + sync: LIVE (push 966 MiB + motore testato)
- [CP-20260610-003](checkpoints/CP-20260610-003.md) — Skill `empire-context` creata (project-level, condivisa con Gael via repo)

## Piani
- [PIANI.md](plans/PIANI.md) — registro piani versionati (→ PIANO-MAESTRO/)

## Sessioni
- [session-20260610](sessions/session-20260610.md) — produzione Piano Maestro EMPIRE OS

## Template (usare SEMPRE questi)
- [CP-template](templates/CP-template.md) · [ADR-template](templates/ADR-template.md) · [session-template](templates/session-template.md)

## Cartelle operative
- `tasks/<ecosistema>/` — log task per ecosistema (01-agency … 10-memory)
- `state/<progetto-id>/` — state.json + trace.jsonl per progetto/ordine in corso
- `audit/` — audit trail modifiche e backup refs
