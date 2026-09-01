# ARCHITECTURE — `content-forge`

> Mappa navigabile dell'intera skill. **Aggiornata a PLAN-v5** (8 stage + MKD obbligatorio + multi-source).
> Lo scopo: dare a chi entra nel repo (o all'LLM che lo apre) un punto unico per orientarsi.

---

## Pipeline in 8 stage (v5)

```
INVOCAZIONE /forge <source> [opzioni]
    │
    ▼
[Stage 1] Ingestion             A1                 (file singolo O cartella multi-source)
[Stage 2] Deep Analysis         A2 (xN parallel)
[Stage 3] Knowledge Graph       A3
[Stage 4] 🌟 MASTER KNOWLEDGE   A5                 (SEMPRE — base canonica)
          DOCUMENT (MKD)
[Stage 5] Target Selection      A4                 (se target ignoto)
[Stage 6] Interactive Build     D1 + Bx            (PLAN→ASK→BUILD→CRITIQUE→ITERATE)
[Stage 7] External QA           C1 + C3 parallel
[Stage 8] Packaging             scripts/           (deliverable + MKD bonus)
```

---

## Hierarchy file

```
content-forge/
├── SKILL.md                                       # kernel (routing + invariant + input modes)
├── ARCHITECTURE.md                                # questo file
├── PLAN.md, PLAN-v2..v5.md                        # storia decisioni
├── README.md
│
├── agents/                                        # 12 agenti + Conductor
│   ├── conductor.md                               # L1 — main orchestrator
│   ├── pipeline/                                  # 5 agenti pipeline
│   │   ├── ingestion-agent.md                     # A1 — multi-source aware
│   │   ├── analyst-agent.md                       # A2 — xN parallel
│   │   ├── knowledge-graph-agent.md               # A3
│   │   ├── mkd-builder-agent.md                   # A5 — 🌟 NUOVO (Stage 4)
│   │   └── target-advisor-agent.md                # A4
│   ├── builders/                                  # B1-B8 — uno per target finale
│   │   ├── doc-builder-agent.md                   # ora MKD adapter (snello)
│   │   ├── agent-builder-agent.md
│   │   ├── team-builder-agent.md
│   │   ├── skill-builder-agent.md
│   │   ├── workflow-builder-agent.md
│   │   ├── orchestration-builder-agent.md
│   │   ├── wiki-builder-agent.md
│   │   └── custom-builder-agent.md
│   ├── qa/
│   │   ├── coverage-verifier-agent.md             # C1
│   │   └── target-schema-validator-agent.md       # C3
│   └── meta/
│       └── question-designer-agent.md             # D1
│
├── references/
│   ├── stages/                                    # 8 stage (v5)
│   │   ├── 01-ingestion.md
│   │   ├── 02-analysis.md
│   │   ├── 03-knowledge-graph.md
│   │   ├── 04-master-document.md                  # 🌟 NUOVO
│   │   ├── 05-target-selection.md
│   │   ├── 06-interactive-build.md
│   │   ├── 07-coverage-check.md
│   │   └── 08-packaging.md
│   ├── patterns/                                  # 9 framework cognitivi (invariati)
│   │   ├── P1-atomic-extraction.md
│   │   ├── P2-claim-evidence-example.md
│   │   ├── P3-hierarchy-dependency.md
│   │   ├── P4-steelmanning.md
│   │   ├── P5-procedural-decomposition.md
│   │   ├── P6-mental-model-surfacing.md
│   │   ├── P7-schema-generation.md
│   │   ├── P8-cross-reference.md
│   │   └── P9-target-shape-mapping.md
│   ├── processes/                                 # 8 processi end-to-end (invariati)
│   │   └── <8 file: doc/agent/team/skill/workflow/orchestration/wiki/custom>.md
│   ├── schemas/                                   # 12 entities × 2 (md + json)
│   │   ├── kg.schema.{md,json}
│   │   ├── doc.schema.{md,json}
│   │   ├── agent.schema.{md,json}
│   │   ├── team.schema.{md,json}
│   │   ├── skill.schema.{md,json}
│   │   ├── workflow.schema.{md,json}
│   │   ├── orchestration.schema.{md,json}
│   │   ├── wiki.schema.{md,json}
│   │   ├── wiki-note.schema.{md,json}
│   │   ├── custom.schema.{md,json}
│   │   ├── mkd.schema.{md,json}                   # 🌟 NUOVO
│   │   └── sources.schema.{md,json}               # 🌟 NUOVO (multi-source)
│   ├── conventions/
│   │   ├── naming.md
│   │   ├── markdown-style.md
│   │   └── anti-patterns.md
│   └── external/
│       └── skill-creator.md                       # mirror Anthropic
│
├── assets/
│   └── templates/                                 # 8 set scaffolding (invariati)
│
├── scripts/                                       # 9 main + 5 lib + 14 test
│   ├── transcript_cleaner.py                      # S1 — ora multi-source aware
│   ├── atomizer.py                                # S2
│   ├── coverage_check.py                          # S3
│   ├── no_summary_lint.py                         # S4
│   ├── length_check.py                            # S5
│   ├── schema_validator.py                        # S6 (ora valida anche mkd/sources)
│   ├── obsidian_packager.py                       # S7
│   ├── package_target.py                          # S8 — ora include MKD nel deliverable
│   ├── validate_dag.py                            # S9
│   ├── lib/
│   │   ├── __init__.py
│   │   ├── kg_loader.py
│   │   ├── atom_matcher.py
│   │   ├── frontmatter.py
│   │   ├── markdown_tools.py
│   │   └── obsidian.py
│   └── tests/                                     # pytest scaffolds
│
└── evals/
    └── evals.json
```

---

## Conteggio file (v5 deliverable)

| Categoria | Pre-v5 | Post-v5 | Stato |
|-----------|--------|---------|-------|
| Kernel (SKILL.md) | 1 | 1 | ✅ aggiornato v5 |
| Conductor SP | 1 | 1 | ✅ aggiornato v5 |
| Pipeline agents | 4 | **5** (+A5 mkd) | ✅ |
| Builder agents (B1-B8) | 8 | 8 | ✅ aggiornati con MKD input |
| QA agents (C1, C3) | 2 | 2 | ✅ |
| Meta agent (D1) | 1 | 1 | ✅ |
| References — stages | 7 | **8** (+ MKD stage) | ✅ |
| References — patterns | 9 | 9 | ✅ |
| References — processes | 8 | 8 | ✅ |
| References — schemas | 20 (10×2) | **24** (12×2, +mkd, +sources) | ✅ |
| References — conventions | 3 | 3 | ✅ |
| References — external | 1 | 1 | ✅ |
| Assets — templates | 57 | 57 | invariati |
| Scripts — principali | 9 | 9 | ✅ |
| Scripts — lib | 6 (5 + init) | 6 | ✅ |
| Scripts — tests | 14 | 14 | ✅ |
| Evals | 1 | 1 | ✅ |
| Plan & meta | 6 (PLAN x5 + ARCH + README) | 7 | ✅ |
| **TOTALE** | 187 | **~194** | |

---

## Cosa è cambiato in v5 (vista alto livello)

1. **🌟 Stage 4 nuovo — MKD (Master Knowledge Document)**: il "documento perfetto" ampliato è prodotto sempre, prima della selezione del target. Diventa la base canonica da cui i builder dei target finali attingono per la prosa.

2. **Multi-source nativo**: A1 ora supporta cartelle, ricorsione, glob, lista esplicita. `sources.json` traccia ogni file di origine. Atomi e MKD hanno tracciabilità per fonte.

3. **Renumber stage**: ora sono 8 (era 7). Stage 4-7 vecchi diventano 5-8.

4. **Doc-builder semplificato**: ora è "MKD adapter" — molto più snello, si focalizza su adattamento stilistico (audience, registro, lingua) invece di costruire da zero.

5. **Altri builder potenziati**: B2-B8 leggono il MKD come fonte primaria di prosa (+ KG per struttura). Riducono duplicazione di lavoro.

6. **Deliverable arricchito**: il pacchetto finale (Stage 8) include SEMPRE il MKD come bonus, anche se l'utente ha chiesto target ≠ doc.

7. **Limiti di dimensione documentati**: comfort zone + hard limits espliciti in SKILL.md e A1.

---

## Roadmap fasi successive

| Fase | Cosa | Stato |
|---|---|---|
| **0-3** | PLAN v1-v5, scaffolding, contenuti operativi | ✅ |
| **PHASE 2.5 (questa)** | Refactor v5: MKD + multi-source | ✅ |
| **PHASE 4** | Implementazione Python (scripts + lib + test) | ⏭ next |
| 5 | Rifinitura finale SKILL.md | |
| 6 | Esempi reali nei templates | |
| 7 | Test end-to-end reali | |
| 8 | Packaging .skill finale | |

---

## Principi guida (recap)

1. **Markdown è la spina, Python è il muscolo** (PLAN-v4 §0).
2. **Progressive disclosure**: nessun file >500 righe ideali; caricare reference on-demand.
3. **Interactive scaffolding** per i target complessi (PLAN-v3 §0).
4. **No summary, ever** (catalogo `references/conventions/anti-patterns.md`).
5. **Coverage misurabile** (script + agente C1).
6. **Forme canoniche per target** validabili (schemas + agente C3).
7. **🌟 MKD intermedio obbligatorio** (PLAN-v5): prima trasformiamo il sorgente nel "documento perfetto", poi lo modelliamo nel target richiesto.
8. **🌟 Multi-source nativo** (PLAN-v5): cartelle e liste di file gestite end-to-end con tracciabilità.
