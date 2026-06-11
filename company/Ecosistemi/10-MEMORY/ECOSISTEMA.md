# 🧠 10 — MEMORY

> **Livello:** L1 · **Priorità:** MASSIMA (costruita per prima) · **Stato:** ✅ OPERATIVO (ME-0/ME-1)
> Dossier completo: `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md`
> ADR fondativo: `company/Memory/decisions/ADR-002-memory-first.md`

## Missione

**Memoria operativa della holding.** Garantisce che nessun task parta senza contesto
e nessun task finisca senza traccia. La holding non impara se non scrive.

**Regola non negoziabile (pattern #13 — Memory-first):**
- **PRIMA di ogni task:** leggi `Memory/STATO-EMPIRE.md` + `Memory/INDEX.md`
- **DOPO ogni task:** scrivi checkpoint in `Memory/checkpoints/CP-YYYYMMDD-NNN.md`
- **Nessun task è "fatto" finché non è salvato in MEMORY**

## Componenti operativi (già costruiti)

| Componente | File | Stato |
|---|---|---|
| Index maestro | `Memory/INDEX.md` | ✅ ATTIVO |
| Stato corrente | `Memory/STATO-EMPIRE.md` | ✅ ATTIVO |
| Decisioni (ADR) | `Memory/decisions/ADR-001..004` | ✅ ATTIVO |
| Checkpoint | `Memory/checkpoints/CP-20260610-001..003` | ✅ ATTIVO |
| Template CP/ADR | `Memory/templates/` | ✅ ATTIVO |
| Piani | `Memory/plans/PIANI.md` | ✅ ATTIVO |
| Sessioni | `Memory/sessions/` | ✅ ATTIVO |
| Tasks per ecosistema | `Memory/tasks/` | struttura pronta |
| State progetti | `Memory/state/` | struttura pronta |
| Audit | `Memory/audit/` | struttura pronta |

## Reparti L2 (da costruire in fasi successive)

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Checkpoint Engine | scrittura automatica checkpoint post-task | `Reparti/Checkpoint/` |
| L2.2 | ADR Registry | decisioni architetturali, conflitti, override | `Reparti/ADR/` |
| L2.3 | State Tracker | stato per progetto/ordine (state.json + trace) | `Reparti/State/` |
| L2.4 | Audit Trail | log modifiche, backup refs, sicurezza | `Reparti/Audit/` |

## Template da usare SEMPRE

```bash
# Nuovo checkpoint:
cp company/Memory/templates/CP-template.md company/Memory/checkpoints/CP-YYYYMMDD-NNN.md

# Nuova decisione:
cp company/Memory/templates/ADR-template.md company/Memory/decisions/ADR-NNN-titolo.md
```

## Come si collega al Backbone

- **BRAIN:** fa parte del BRAIN — è la memoria strutturata (checkpoint/ADR/piani) che
  affianca AgentDB (memoria vettoriale) e wiki (fonte di verità umana)
- **GOVERNANCE:** memory-first è un gate di governance: nessun task parte senza interrogazione

*Fonte: `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md` · Aggiornato: 2026-06-11*
