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
- [ADR-005](decisions/ADR-005-backlog-non-blocca.md) — Blocker minori → BACKLOG.md, mai fermare la costruzione; team-prezzi per le decisioni di prezzo
- [ADR-006](decisions/ADR-006-ciclo-fase-9-passi.md) — Ciclo di Fase Empire a 9 passi (metodo ufficiale, swarm obbligatorio per Max e Gael) → `PIANO-MAESTRO/10-METODO-CICLO-FASE.md`
- [ADR-007](decisions/ADR-007-piano-v2-scala.md) — **PIANO V2 Direttiva di Scala**: 1 workflow=CF Exponium, Board=workflow×10+ agenti, reparti=team+workflow CF-grade, Mandato-ecosistema, organo MAXIMILIAN → `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md`

## Corpus Maximilian
- [direttiva-20260611-scala-v2](maximilian-corpus/direttiva-20260611-scala-v2.md) — prima direttiva integrale di Max (addestramento organo MAXIMILIAN; ogni futura direttiva si appende qui)

## Backlog
- [BACKLOG.md](BACKLOG.md) — cose rimandabili (token FB, prezzo manuale, team-prezzi B-003, ...)

## Checkpoint
- [CP-20260616-010](checkpoints/CP-20260616-010.md) — STEP 4(c): blueprint Board via ARCHITETTURA (8 file, 70 agenti progettati, primo uso reale WF-ARCH-DESIGN) — Max
- [CP-20260616-009](checkpoints/CP-20260616-009.md) — STEP 3: organo MAXIMILIAN (15 file, review-gate 5-bis + maximilian-standard-gate eseguibile, gate+review PASS) — Max
- [CP-20260616-008](checkpoints/CP-20260616-008.md) — STEP 2 Genesi Core: FORGE completa (34 file, Mappa-Motori 15 motori reali, gate+review PASS) — Max
- [CP-20260616-007](checkpoints/CP-20260616-007.md) — STEP 1 Genesi Core: organo ARCHITETTURA costruito (dossier 14 + 30 file, gate+review PASS) — Max
- [CP-20260616-006](checkpoints/CP-20260616-006.md) — V2-2 lotto 2: dossier v2 mega-reparti CONTENT-FACTORY (5 livelli/76 agenti) + INFO-BUSINESS (48 agenti) — Gael
- [CP-20260616-005](checkpoints/CP-20260616-005.md) — V2-2 lotto 1: dossier v2 AGENCY (10 reparti/75 agenti) + MARKETING (6 reparti/49 agenti) — Gael
- [CP-20260616-004](checkpoints/CP-20260616-004.md) — V2-2: dossier MANDATO-ecosistema (PIANO-MAESTRO/13) — blueprint governo per V2-5 — Gael
- [CP-20260616-003](checkpoints/CP-20260616-003.md) — V2-2 AVVIATA: dossier MAXIMILIAN (PIANO-MAESTRO/12) — blueprint organo per V2-3 — Gael
- [CP-20260616-002](checkpoints/CP-20260616-002.md) — F1-bis COMPLETATO: gate verde (0 vuote, 0 magri, 317 file) + review pass; prossima V2-2 — Gael
- [CP-20260616-001](checkpoints/CP-20260616-001.md) — Fix collisione case-insensitive 06-PLATFORM/Reparti (5 doppioni MAIUSCOLO rimossi, contenuto arricchito preservato) — Gael
- [CP-20260613-001](checkpoints/CP-20260613-001.md) — Fix critico Empire Studio: RULES.md + agenti verification aggiornati + run Andrei Pascu avviata
- [CP-20260611-008](checkpoints/CP-20260611-008.md) — PIANO V2 Direttiva di Scala codificata (ADR-007) + corpus Maximilian + pivot roadmap V2
- [CP-20260611-007](checkpoints/CP-20260611-007.md) — F4 GATE VERDE: ciclo dry-run end-to-end CY-20260611-001 (Gael) — gate PASS 113/113
- [CP-20260611-006](checkpoints/CP-20260611-006.md) — F4 B2 wrap 4 WF outreach come L3 + agency-trace.ps1 (Gael) — gate PASS 107/107
- [CP-20260611-005](checkpoints/CP-20260611-005.md) — Metodo 9 passi (ADR-006) + handover a Gael; F1-bis arricchimento a metà (session limit)
- [CP-20260611-004](checkpoints/CP-20260611-004.md) — F4 AGENCY live B1 completato (Gael) — gate PASS 97/97
- [CP-20260611-003](checkpoints/CP-20260611-003.md) — F3 Migrazione asset completato (Gael) — gate PASS 70/70
- [CP-20260611-002](checkpoints/CP-20260611-002.md) — F2 Backbone operativo completato (Gael) — gate PASS 59/59
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
