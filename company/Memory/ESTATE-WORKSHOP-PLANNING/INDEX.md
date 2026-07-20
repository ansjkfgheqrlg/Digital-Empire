# 🧠 ESTATE WORKSHOP PLANNING — MEMORY INDEX

**Fase:** Planning Avanzato (Livelli 1-8)  
**Progetto:** Estate Workshop Workflow System  
**Owner:** Chief Forge Department

---

## Struttura del Memory Ecosystem (Planning Phase)

```
company/Memory/ESTATE-WORKSHOP-PLANNING/
├── decisions/          ← Decisioni prese durante il planning
├── architecture/       ← Output architetturali di ogni livello
├── planning/           ← Documenti di planning per livello
├── restorming/         ← Sessioni di revisione
├── checkpoints/        ← Checkpoint per livello
└── performance/        ← Metriche del planning
```

---

## Livelli di Planning

| Livello | Nome | Stato | Output Principale | Memory Link |
|---------|------|-------|-------------------|-------------|
| L1 | Scoping & Visione | ⬜ Da fare | Visione + Principi | L1-scoping/ |
| L2 | Stream Breakdown | ⬜ Da fare | Breakdown S1-S6 | L2-stream-breakdown/ |
| L3 | Agent Identification | ⬜ Da fare | Catalogo Agenti | L3-agent-identification/ |
| L4 | Memory Architecture | ⬜ Da fare | Memory System Design | L4-memory-architecture/ |
| L5 | Ruflo Orchestration | ⬜ Da fare | Ruflo Topology | L5-ruflo-orchestration/ |
| L6 | Content-Forge Integration | ⬜ Da fare | Forge Process | L6-content-forge-integration/ |
| L7 | Verification Gates | ⬜ Da fare | Gate Definition | L7-verification-gates/ |
| L8 | Final Workflow Assembly | ⬜ Da fare | Master Workflow Map | L8-final-workflow-assembly/ |

---

## Protocollo di Salvataggio

- Ogni livello → propria cartella in `planning-workshop/`
- Ogni decisione → `decisions/`
- Ogni restorming → `restorming/`
- Ogni checkpoint → `checkpoints/`

**Comando memoria:**
```bash
python scripts/memory_manager.py --checkpoint "L<X> completato" --phase <livello> --trace "ESTATE-WORKSHOP-PLANNING"
```

---

**Creato:** 2026-07-20  
**Versione:** 1.0 — Planning Phase Attiva