# L4 — OUTPUT: Memory Architecture

**Livello:** 4  
**Stato:** COMPLETATO  
**Data:** 2026-07-20

---

## Memory System Design

### Categorie Principali

| Categoria | Scopo | Esempi | Path |
|-----------|-------|--------|------|
| **decisions** | Decisioni chiave | DEC-001, DEC-002, DEC-003 | decisions/ |
| **architecture** | Architetture e workflow | S5 Empire Studio, WF-YT-* | architecture/ |
| **planning** | Task board e roadmap | Taskboard Workshop, Gantt | planning/ |
| **restorming** | Revisione e miglioramento | RST-001, RST-002 | restorming/ |
| **checkpoints** | Checkpoint per livello/stream | CP-20260720-L1 | checkpoints/ |
| **performance** | Metriche reali | Revenue, video generati | performance/ |

### Protocollo Obbligatorio

1. Ogni decisione → `decisions/DEC-XXX-nome.md`
2. Ogni architettura → `architecture/`
3. Ogni planning → `planning/`
4. Ogni restorming → `restorming/`
5. Ogni fine livello → `checkpoints/`
6. Metriche → `performance/`

**Comando automatico:**
```bash
python scripts/memory_manager.py --checkpoint "<azione>" --phase <livello> --trace "ESTATE-WORKSHOP-PLANNING"
```

---

**Checkpoint L4:** CP-20260720-L4  
**Prossimo:** L5 — Ruflo Orchestration