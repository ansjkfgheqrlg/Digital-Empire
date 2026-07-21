# 📐 PLAN v3 — Skill `content-forge` (comando `/forge`)

> **Cosa cambia rispetto a v2:**
> - C2 `quality-critic` **collassato** come fase di self-critique interna ad ogni builder → totale **11 agenti** (4 pipeline + 8 builder + 2 QA + 1 designer) + Conductor.
> - D1 `question-designer` **confermato come agente separato** (più performante, riusato da tutti i builder).
> - I processi end-to-end per ogni target sono **già scritti in versione lunga** nei file `references/processes/<target>.md` (vedi §6 e l'albero in §9).

---

## 0. Filosofia (invariata)

`content-forge` è un **sistema operativo cognitivo**:
- `SKILL.md` = kernel
- `agents/` = processi specializzati (subagenti via Task tool)
- `scripts/` = operazioni deterministiche
- `references/` = conoscenza on-demand
- `assets/templates/` = forme canoniche

Allineato al pattern Anthropic skill-creator (che a sua volta usa `agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md`, `scripts/aggregate_benchmark.py`, ecc.).

---

## 1-3. (Invariate da v1/v2)

Conservate: intent, 9 pattern cognitivi P1-P9, 8 target.

---

## 4. 🤖 Architettura multi-agente (aggiornata: 11 agenti + Conductor)

### 4.1 Modello di esecuzione (invariato)

3 livelli: **L1 Conductor** (Claude principale) → **L2 Specialist Agents** (subagenti via Task tool) → **L3 Scripts** (Python).

### 4.2 Inventario agenti (aggiornato a 11)

#### 🅰️ Family A — Pipeline cognitiva (4)
| # | Agente | File |
|---|---|---|
| A1 | `ingestion-agent` | `agents/pipeline/ingestion-agent.md` |
| A2 | `analyst-agent` | `agents/pipeline/analyst-agent.md` |
| A3 | `knowledge-graph-agent` | `agents/pipeline/knowledge-graph-agent.md` |
| A4 | `target-advisor-agent` | `agents/pipeline/target-advisor-agent.md` |

#### 🅱️ Family B — Target builders (8) — ognuno include la sua fase di self-critique interna
| # | Agente | Target | File |
|---|---|---|---|
| B1 | `doc-builder-agent` | `doc` | `agents/builders/doc-builder-agent.md` |
| B2 | `agent-builder-agent` | `agent` | `agents/builders/agent-builder-agent.md` |
| B3 | `team-builder-agent` | `team` | `agents/builders/team-builder-agent.md` |
| B4 | `skill-builder-agent` | `skill` | `agents/builders/skill-builder-agent.md` |
| B5 | `workflow-builder-agent` | `workflow` | `agents/builders/workflow-builder-agent.md` |
| B6 | `orchestration-builder-agent` | `orchestration` | `agents/builders/orchestration-builder-agent.md` |
| B7 | `wiki-builder-agent` | `wiki` (Obsidian) | `agents/builders/wiki-builder-agent.md` |
| B8 | `custom-builder-agent` | `custom` | `agents/builders/custom-builder-agent.md` |

#### 🅲 Family C — QA esterna (2, era 3) — il quality-critic è ora step interno ai builder
| # | Agente | File |
|---|---|---|
| C1 | `coverage-verifier-agent` | `agents/qa/coverage-verifier-agent.md` |
| C3 | `target-schema-validator-agent` | `agents/qa/target-schema-validator-agent.md` |

> Nota: la numerazione salta C2 di proposito, per coerenza con il razionale dell'evoluzione (C2 = self-critique fase del builder, non più agente).

#### 🅳 Family D — Meta (1)
| # | Agente | File |
|---|---|---|
| D1 | `question-designer-agent` | `agents/meta/question-designer-agent.md` |

#### + Conductor
| Agente | File |
|---|---|
| `conductor` (system prompt del coordinatore principale, non spawnato — è il caller) | `agents/conductor.md` |

**Totale: 11 agenti specialisti + Conductor.**

---

## 5. Diagramma di flusso (aggiornato)

```
┌──────────────────────────────────────────────────────────────────┐
│                          CONDUCTOR (L1)                          │
└────────────────────────────────┬─────────────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
   [Stage 1] ─▶ A1 ingestion ─▶ cleaned.md, chunks.json
   [Stage 2] ═▶ A2 analyst ×N (parallelo) ─▶ atoms-*.json
   [Stage 3] ─▶ A3 knowledge-graph ─▶ kg.json, kg.md
   [Stage 4] ─▶ A4 target-advisor (se serve) ─▶ recommendation.md
        │
        ▼
   [Stage 5 ASK]   ─▶ D1 question-designer ─▶ domande adattive
   [Stage 5 BUILD] ─▶ Bx target-builder
                       ├─ PLAN interno
                       ├─ BUILD file canonici
                       └─ SELF-CRITIQUE interno (era C2)
        │
        ▼
   [Stage 6 QA] ═▶ C1 coverage-verifier  ┐
                  C3 schema-validator    ├─▶ qa-report.md (parallelo)
        │
        ▼
   PASS → Stage 7 packaging
   FAIL → loop ITERATE: Bx rilavora con qa-report
```

---

## 6. Processi end-to-end per target

I 8 processi sono **già scritti in versione lunga** (con esempi, pattern applicati, file canonici dettagliati) nei file:

- `references/processes/doc.md`
- `references/processes/agent.md`
- `references/processes/team.md`
- `references/processes/skill.md`
- `references/processes/workflow.md`
- `references/processes/orchestration.md`
- `references/processes/wiki.md`
- `references/processes/custom.md`

Sono organizzati con struttura standard a 11 sezioni: identità, forma canonica output, input atteso, PLAN, ASK, BUILD, self-critique (interno), critique esterna, iterate, failure modes, esempio realistico, handoff.

> Vai a leggerli per i dettagli: sono il cuore operativo della skill.

---

## 7-8. Scripts (8) e References (invariati da v2)

Vedi PLAN-v2 §7-8.

---

## 9. 📁 Struttura file finale (v3)

```
content-forge/
├── SKILL.md
├── agents/
│   ├── conductor.md
│   ├── pipeline/
│   │   ├── ingestion-agent.md             # A1
│   │   ├── analyst-agent.md               # A2
│   │   ├── knowledge-graph-agent.md       # A3
│   │   └── target-advisor-agent.md        # A4
│   ├── builders/
│   │   ├── doc-builder-agent.md           # B1
│   │   ├── agent-builder-agent.md         # B2
│   │   ├── team-builder-agent.md          # B3
│   │   ├── skill-builder-agent.md         # B4
│   │   ├── workflow-builder-agent.md      # B5
│   │   ├── orchestration-builder-agent.md # B6
│   │   ├── wiki-builder-agent.md          # B7
│   │   └── custom-builder-agent.md        # B8
│   ├── qa/
│   │   ├── coverage-verifier-agent.md     # C1
│   │   └── target-schema-validator-agent.md # C3
│   └── meta/
│       └── question-designer-agent.md     # D1
├── references/
│   ├── stages/             (7 file)
│   ├── patterns/           (9 file, P1-P9)
│   ├── processes/          (8 file, uno per target) ⭐
│   ├── schemas/            (6 file)
│   ├── conventions/        (3 file)
│   └── external/skill-creator.md
├── assets/templates/       (8 set, uno per target)
├── scripts/                (8 script + tests/)
└── evals/evals.json
```

**Totale: 11 agenti + 8 script + ~34 reference + 8 set di template + 1 kernel.**

---

## 10. Roadmap

| Fase | Cosa produciamo | Stato |
|---|---|---|
| 0. PLAN v1/v2/v3 | piano | ✅ v3 in corso |
| 0c. PROCESSES (versione lunga) | 8 file `references/processes/*.md` | ⏳ **in scrittura ora** |
| 1. ARCHITECTURE | scheletro file completo | ⏭ next |
| 2. AGENTI | system prompt completi per gli 11 agenti + Conductor | |
| 3. PATTERNS & STAGES | contenuto vero di stages/ e patterns/ | |
| 4. SCRIPTS & SCHEMAS | 8 script Python + 6 schemi + test | |
| 5. SKILL.md KERNEL | scrittura finale del kernel | |
| 6. TEMPLATES | template di scaffolding per ogni target | |
| 7. EVALS & TEST | evals.json + run dei 4 test case + iterazione | |
| 8. PACKAGING | `.skill` finale | |
