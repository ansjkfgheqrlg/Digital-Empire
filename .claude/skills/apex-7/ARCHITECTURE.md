# APEX-7 Architecture

> Complete system architecture of the Adaptive Prompt EXecution Engine.

## System Overview

```
┌────────────────────────────────────────────────────────────────┐
│                        APEX-7 SYSTEM                            │
│                                                                 │
│  ┌─────────┐   ┌──────────┐   ┌─────────┐   ┌───────┐         │
│  │ ORCHES- │──→│ PLANNER  │──→│ ANALYST │   │WRITER │         │
│  │ TRATOR  │   └──────────┘   │  (∥)    │   │ (∥)   │         │
│  │   L1    │                  └─────────┘   └───────┘         │
│  └────┬────┘                       │             │             │
│       │                            └──────┬──────┘             │
│       │                                   │                    │
│       │                            ┌──────▼──────┐             │
│       │                            │    CRITIC   │             │
│       │                            │  5-dim score│             │
│       │                            └──────┬──────┘             │
│       │                                   │                    │
│       │              ┌────────────────────┼────────────┐       │
│       │              │                    │            │       │
│       │         ┌────▼────┐        ┌──────▼──────┐    │       │
│       │         │ REFINER │        │  GATE AGENT │    │       │
│       │         │ (fixes) │        │  7 levels   │    │       │
│       │         └────┬────┘        └──────┬──────┘    │       │
│       │              │                    │            │       │
│       │              └────────────────────┘            │       │
│       │                                               │       │
│       │         ┌─────────────────────────────────────┘       │
│       │         │                                             │
│       │    ┌────▼─────┐                                       │
│       └───→│   META   │←─── Every 3 cycles                    │
│            │  AGENT   │                                        │
│            └────┬─────┘                                        │
│                 │                                              │
│    ┌────────────┼──────────────────────────────┐              │
│    │            │                              │              │
│ ┌──▼──┐   ┌─────▼──────┐   ┌─────────────┐    │              │
│ │EVENT│   │  MEMORY    │   │SELF-EVOLVE  │    │              │
│ │ BUS │   │ 5 LAYERS   │   │  ENGINE     │    │              │
│ └─────┘   └────────────┘   └─────────────┘    │              │
│                                                │              │
│                   ┌────────────────────────────┘              │
│                   │                                           │
│              ┌────▼─────┐                                     │
│              │  OUTPUT  │                                     │
│              │  FINALE  │                                     │
│              └──────────┘                                     │
└────────────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Input → ORCHESTRATOR**: User goal received, session initialized
2. **ORCHESTRATOR → PLANNER**: Goal + memory context for decomposition
3. **PLANNER → ORCHESTRATOR**: Plan with subtasks, risks, priorities
4. **ORCHESTRATOR → ANALYST + WRITER** (parallel):
   - ANALYST: memory deep dive → patterns → Context Package
   - WRITER: receives Context Package → draft
5. **WRITER → CRITIC**: Draft evaluated on 5 dimensions
6. **CRITIC → REFINER** (if REFINE): Fixes applied, back to CRITIC
7. **Output → GATE AGENT**: 20 criteria across 7 levels
8. **GATE → ORCHESTRATOR**: PASS/FAIL with remediation
9. **Every 3 cycles → META AGENT**: System health, patterns, evolution
10. **ORCHESTRATOR → USER**: Final assembled output

## Component Details

### Agents (L2)
- **ORCHESTRATOR** (L1): Queen coordinator, routing, monitoring
- **PLANNER**: Strategic decomposition, risk analysis
- **ANALYST**: Context mapping, pattern detection, insight generation
- **WRITER**: Structure design, draft creation, self-review
- **CRITIC**: 5-dimension scoring, verdict, fix proposals
- **REFINER**: Surgical fixing, consistency preservation
- **GATE AGENT**: 20 criteria, 7 levels, zero tolerance at L5-L7
- **META AGENT**: System health, pattern detection, evolution control

### Memory (5 Layers)
- **L1 Working Memory**: Session context (volatile)
- **L2 Decision Log**: All decisions with reasoning (permanent)
- **L3 Strategy Store**: Winning strategies with ranking (permanent)
- **L4 Architecture Snapshots**: System versioning with diffs (permanent)
- **L5 Compressed Knowledge**: Lessons, best practices, anti-patterns (permanent, distilled)

### Event Bus
- **P0 (CRITICO)**: Immediate delivery, max 10 retries every 1s
- **P1 (ALTO)**: Delivery within 5s, max 5 retries
- **P2 (NORMALE)**: Delivery within 30s, max 3 retries
- **P3 (BASSO)**: Best-effort, 1 retry then DROP

### Quality Gates (7 Levels)
- **L1→L2 (Base)**: 3 specific criteria, threshold 0.80
- **L2→L3 (Structure)**: Feedback loops, max iterations, routing
- **L3→L4 (Parallelism)**: Race conditions, checkpoints, rollback
- **L4→L5 (Meta)**: Visibility, scoring calibration, pattern thresholds
- **L5→L6 (Safety)**: ⚠️ ZERO TOLERANCE — stability, human override, safety limits
- **L6→L7 (APEX)**: ⚠️ ZERO TOLERANCE — all previous, E2E test, ≥150% performance
