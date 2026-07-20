---
name: fas-agent-smith
reparto: FORGE-AGENT-SKILL
intestazione_adr008: { proprietario: 06b-FORGE (L2.2 AGENT-WORKS), controllore: fas-qa-gate, origine: FORGE, governo: ADR-001/003/006 }
versione: v1 (2026-07-20)
---

# fas-agent-smith — Forgia agenti e team (CF-grade)

## Scopo
Trasforma un FORGE-PLAN in agenti/team completi, nello **standard 7 file canonici** dell'impero.

## Motore
`/forge <sorgente> --target=agent|team --name=<slug>` (motore `content-forge2.0/`, wrapper
`.claude/skills/content-forge`). Per architetture di team complesse: `/master-architect --target=swarm`.
**MAI modificare i motori (ADR-003):** gli adattamenti impero si applicano come layer post-forgia.

## Standard di uscita (per OGNI agente)
```
<ecosistema>/agents/<slug>/
├── spec.md           ← ruolo, input/output, vincoli, intestazione ADR-008
├── system-prompt.md  ← prompt operativo completo (≥80 righe per agenti di piano, mai monoriga)
├── tools.md          ← strumenti/consensi (bash, fetch, file) + limiti
├── playbook.md       ← 3+ scenari d'uso esempio
├── evals.md          ← 5+ casi test con atteso (come lo valuti)
├── failure-modes.md  ← tabella failure|sintomo|prevenzione|rilevamento|recupero (≥5 righe)
└── memory.md         ← cosa ricorda tra run, dove (checkpoints, namespace)
```
Team: + `topology.md` (conductor → specialisti, handoff, merge/persistenza).

## Regole
1. Nessun agente "figlio del nome": lo slug dichiara reparto (`ag-a1-x`, `fas-*`, `yt-*`…).
2. Invenzioni rispetto alla sorgente marcate `➕`.
3. Ogni file scritto subito (write-early, lezione RETRO CP-20260711-002).
4. Idempotenza: rilanciare il build non duplica, aggiorna.
