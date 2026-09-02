---
name: memory-ecosystem-skill
tier: tier0-orchestration
description: "Skill che governa l'intero ecosistema di memoria (16 categorie): garantisce l'aggiornamento dopo ogni azione, l'INDEX vivo, i nomi Windows-safe. Coordina il reparto Memory Management."
uses_scripts:
  - scripts/memory_manager.py
---

# memory-ecosystem-skill (tier0-orchestration)

> Il sistema nervoso: ogni decisione/bug/sessione/aggiornamento e' registrato.

## Cosa fa
- Espone memory_manager.py a tutti i reparti (checkpoint/decisioni/bug/...).
- Mantiene MEMORY-INDEX.md vivo e i nomi file Windows-safe.
- Coordina gli 8 agenti del reparto Memory Management.

## Come si usa
```
python scripts/memory_manager.py --checkpoint "..." --phase N
python scripts/memory_manager.py --status
```

## Invarianti
- Memory-first (P10).
- Nomi Windows-safe (no 0x80070057).
- 16 categorie reali.

## Agenti che la impugnano
- `memory-management-department/department-lead`
- `memory-management-department/memory-auditor`

## Trace
risponde a 'un intero ecosistema di memoria gestito da agenti'.
