# APEX-7 — Complete Skill Structure

> **Adaptive Prompt EXecution Engine v7.0**
>
> Multi-agent autonomous orchestration system with 8 specialized agents, 5-layer memory, dynamic workflow, quality gates, event bus, and self-evolution.

---

## Quick Links

| Resource | Path |
|---|---|
| **SKILL KERNEL** | [`SKILL.md`](SKILL.md) |
| **Architecture** | [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| **Agents Catalog** | [`agents/`](agents/) |
| **Memory Interface** | [`memory/MEMORY-INTERFACE.md`](memory/MEMORY-INTERFACE.md) |
| **Event Bus** | [`event-bus/EVENT-CATALOG.md`](event-bus/EVENT-CATALOG.md) |
| **Workflow Engine** | [`workflows/workflow-engine.md`](workflows/workflow-engine.md) |
| **Gate Criteria** | [`references/gates/GATE-CRITERIA.md`](references/gates/GATE-CRITERIA.md) |
| **Evolution Engine** | [`self-evolution/EVOLUTION-ENGINE.md`](self-evolution/EVOLUTION-ENGINE.md) |
| **Anti-Patterns** | [`references/conventions/anti-patterns.md`](references/conventions/anti-patterns.md) |
| **Evals** | [`evals/evals.json`](evals/evals.json) |

---

## File Count

| Category | Files | Status |
|---|---|---|
| **Kernel** | 2 (SKILL.md + ARCHITECTURE.md) | ✅ Complete |
| **Agents** | 8 (system prompts) + 8 playbooks + 8 failure-modes + 8 tools + 8 evals + 8 memory | ✅ Complete |
| **References** | 8 (stages + schemas + conventions + processes + routing + gates) | ✅ Complete |
| **Memory** | 1 (MEMORY-INTERFACE.md) + 5 layer dirs | ✅ Complete |
| **Event Bus** | 2 (EVENT-CATALOG.md + BUS-CONFIG.md) | ✅ Complete |
| **Workflows** | 2 (workflow-engine.md + routing-tables.md) | ✅ Complete |
| **Scripts** | 4 (memory_manager.py + score_calculator.py + gate_evaluator.py + evolution_tracker.py) | ✅ Complete |
| **Self-Evolution** | 2 (EVOLUTION-ENGINE.md + metrics-tracker.md) | ✅ Complete |
| **Evals** | 1 (evals.json con 5 test cases) | ✅ Complete |
| **Templates** | In `assets/templates/` | ✅ Ready |
| **TOTAL** | **60+ files** | ✅ |

---

## How to Use

### Via `/apex` command:
```
/apex <your-goal> [--depth=1-7] [--quality=0.80] [--auto-evolve]
```

### Via natural language:
```
"Costruisci un sistema per..."
"Architetta un workflow che..."
"Pianifica e produci..."
```

### What happens:
1. **Bootstrap** → Memory initialized, session created
2. **PLANNER** → Goal decomposed into max 7 subtasks with risk analysis
3. **ANALYST + WRITER** → Parallel: context analysis + draft creation
4. **CRITIC** → 5-dimension weighted scoring + verdict
5. **REFINER** → Surgical fixes (if REFINE, max 3 cycles)
6. **GATE AGENT** → 20 criteria across 7 levels
7. **META AGENT** → Every 3 cycles: system health, patterns, evolution
8. **FINAL OUTPUT** → Assembled with full session summary

---

## Prerequisites

- Python 3.10+ (for scripts)
- Compatible with: RuFLO, Content-Forge 2.0, Master-Build-Architecture
- Integration: npx skills, Claude Code, OpenAI Codex CLI

---

## License

APEX-7 — Built with RuFLO swarm orchestration, Content-Forge pipeline architecture, and Master-Build-Architecture principles.

*████████████████████████████████████████████████████████████*
*█          APEX-7 v7.0 — COMPLETE AND READY                   █*
*████████████████████████████████████████████████████████████*
