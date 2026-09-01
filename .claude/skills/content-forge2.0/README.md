# content-forge v2.0

> Trasforma contenuto testuale grezzo in artefatti operativi di alto valore.
> Mai riassume — **espande sempre**.

```
/forge <source-path> [--target=<target>] [--name=<slug>] [--recursive]
```

---

## Cosa fa

Prende in input contenuto disordinato — transcript YouTube, workshop, articoli, brief, appunti raw, cartelle intere — e produce uno tra 8 target operativi:

| Target | Output |
|---|---|
| `doc` | Documento markdown completo: TOC, esempi, schemi, glossario, FAQ |
| `agent` | Agente AI operativo: spec + system prompt + tools + playbook + eval cases |
| `team` | Team multi-agente: topologia + N agenti + handoff + failure handling |
| `skill` | Skill ufficiale Anthropic: SKILL.md + agents + references + templates + evals |
| `workflow` | Workflow end-to-end: DAG con step, stato, trigger, error handling, runbook |
| `orchestration` | Orchestration layer: supervisor + registry + routing + policies |
| `wiki` | Note Obsidian atomiche: MOC + wikilink integri (second brain) |
| `custom` | Forma custom: system prompt injection, config, RAG knowledge pack |

---

## 4 regole non negoziabili

1. **No riassunti.** L'output rispetta o supera la lunghezza del sorgente.
2. **No invenzione di fatti.** Tutto ciò che Forge genera (esempi, schemi, controesempi) è etichettato `➕`.
3. **Coverage completa.** Ogni atomo del Knowledge Graph compare nell'output finale.
4. **MKD sempre prodotto.** Prima di qualsiasi target finale, viene generato il Master Knowledge Document — il "documento perfetto" — come base canonica intermedia.

---

## Pipeline in 9 stage

```
/forge <source>
    │
    ▼
[Stage 1]  Ingestion          A1  — pulizia, chunking, multi-source aware
[Stage 2]  Deep Analysis      A2  — estrazione atomi (xN in parallelo)
[Stage 3]  Knowledge Graph    A3  — assemblaggio KG + gap detection
[Stage 4]  🌟 MKD             A5  — Master Knowledge Document (SEMPRE)
[Stage 5]  Target Selection   A4  — solo se target non specificato
[Stage 6]  Interactive Build  D1 + Bx — PLAN → ASK → BUILD → CRITIQUE → ITERATE
[Stage 7]  🆕 Depth Pass      Ox  — O1+O2 parallelo → O3 → O5 → O4
[Stage 8]  External QA        C1 + C3 — coverage check + schema validation
[Stage 9]  Packaging          scripts/ — deliverable finale + MKD bonus
```

---

## Architettura agenti (25 totali)

### L1 — Conductor
| Agente | Ruolo |
|---|---|
| `conductor.md` | Orchestratore principale — coordina tutti i layer |

### L2 — Pipeline (A1–A5)
| Agente | Codice | Stage |
|---|---|---|
| `ingestion-agent.md` | A1 | 1 — pulizia + multi-source |
| `analyst-agent.md` | A2 | 2 — estrazione atomi (parallelo) |
| `knowledge-graph-agent.md` | A3 | 3 — KG + gap |
| `mkd-builder-agent.md` | A5 | 4 — Master Knowledge Document |
| `target-advisor-agent.md` | A4 | 5 — selezione target |

### L2 — Builders (B1–B8)
| Agente | Target |
|---|---|
| `doc-builder-agent.md` | `doc` |
| `agent-builder-agent.md` | `agent` |
| `team-builder-agent.md` | `team` |
| `skill-builder-agent.md` | `skill` |
| `workflow-builder-agent.md` | `workflow` |
| `orchestration-builder-agent.md` | `orchestration` |
| `wiki-builder-agent.md` | `wiki` |
| `custom-builder-agent.md` | `custom` |

### L2 — QA (C1, C3)
| Agente | Ruolo |
|---|---|
| `coverage-verifier-agent.md` | C1 — verifica coverage atomi |
| `target-schema-validator-agent.md` | C3 — validazione schema output |

### L2 — Meta (D1)
| Agente | Ruolo |
|---|---|
| `question-designer-agent.md` | D1 — scaffolding domande adattive (Stage 6) |

### L2 — Optimizers (O1–O5) — 🆕 Stage 7
| Agente | Codice | Ruolo |
|---|---|---|
| `skill-depth-agent.md` | O1 | Approfondisce skill output |
| `agent-depth-agent.md` | O2 | Approfondisce agent output |
| `reference-expander-agent.md` | O3 | Espande le references |
| `formula-validator-agent.md` | O5 | Valida formule e schemi |
| `humanizer-agent.md` | O4 | Tono naturale, rimuove AI-slop |

### L2 — Self-Improvement — 🆕 v2.0
| Agente | Ruolo |
|---|---|
| `failure-detector-agent.md` | Rileva pattern di fallimento |
| `phase-planner-agent.md` | Pianifica iterazioni di miglioramento |
| `triage-agent.md` | Prioritizza fix e regressioni |

---

## Struttura del repo

```
content-forge/
│
├── SKILL.md                     ← kernel: routing, invariant, input modes
├── ARCHITECTURE.md              ← mappa navigabile completa
├── PLAN.md … PLAN-v6.md         ← storia delle decisioni di design
│
├── agents/                      ← 25 agenti (conductor + 6 famiglie)
│   ├── conductor.md
│   ├── pipeline/                ← A1–A5
│   ├── builders/                ← B1–B8 (uno per target)
│   ├── qa/                      ← C1, C3
│   ├── meta/                    ← D1
│   ├── optimizers/              ← O1–O5 (Stage 7 Depth Pass)
│   └── self-improvement/        ← failure-detector, phase-planner, triage
│
├── references/                  ← conoscenza on-demand (caricata solo quando serve)
│   ├── stages/                  ← 9 stage documentati
│   ├── patterns/                ← 9 framework cognitivi (P1–P9)
│   ├── processes/               ← 8 processi end-to-end (uno per target)
│   ├── schemas/                 ← 12 entità × 2 file (md + json)
│   ├── conventions/             ← naming, markdown-style, anti-patterns
│   └── external/                ← skill-creator Anthropic mirror
│
├── assets/
│   └── templates/               ← 57 template scaffolding (8 set, uno per target)
│
├── scripts/                     ← 9 script + 5 lib + 14 test (pytest)
│   ├── transcript_cleaner.py    ← S1
│   ├── atomizer.py              ← S2
│   ├── coverage_check.py        ← S3
│   ├── no_summary_lint.py       ← S4
│   ├── length_check.py          ← S5
│   ├── schema_validator.py      ← S6
│   ├── obsidian_packager.py     ← S7
│   ├── package_target.py        ← S8
│   ├── validate_dag.py          ← S9
│   ├── lib/
│   └── tests/
│
├── evals/
│   └── evals.json
│
├── failure-modes-log/           ← 🆕 registro fallimenti rilevati dai self-improvement agents
├── phase9-regression/           ← 🆕 test di regressione Stage 9
├── packaged-final-v1.1/         ← output packaged v1.1
└── packaged-final-v1.2/         ← output packaged v1.2
```

---

## Input supportati

| Tipo | Sintassi |
|---|---|
| Singolo file | `/forge transcript.md` |
| Cartella flat | `/forge ./yt-transcripts/` |
| Cartella ricorsiva | `/forge ./materiale/ --recursive` |
| Lista esplicita | `/forge file1.md,file2.md,file3.md` |
| Glob | `/forge "yt-*.md"` |

**Comfort zone**: 500–200k parole (singolo file) · 1k–500k parole, 1–30 file (cartella)
**Hard limit**: 500k parole (singolo file) · 1M parole, 100 file (cartella)

---

## Quick start

```bash
# Transcript → skill ufficiale
/forge transcript_rag.md --target=skill --name=rag-coach

# Cartella di appunti → wiki Obsidian
/forge ./appunti/ --target=wiki --recursive

# Brief grezzo → agente AI
/forge brief_agente.md --target=agent --name=sales-closer

# Lascia che Forge proponga il target migliore
/forge materiale_grezzo.md
```

---

## Cosa è nuovo in v2.0

| Feature | Dettaglio |
|---|---|
| **Stage 7 — Depth Pass** | 5 optimizer agents (O1–O5) approfondiscono l'output dopo la build |
| **Self-improvement agents** | 3 agenti rilevano fallimenti, pianificano fix, triaggiano regressioni |
| **failure-modes-log** | Log persistente dei pattern di fallimento |
| **phase9-regression** | Suite di regressione per Stage 9 |
| **PLAN-v6** | Nuove decisioni architetturali documentate |
| **File totali** | 1059 (erano 434 in v1) |

---

## Numeri

| Categoria | Conteggio |
|---|---|
| Agenti totali | 25 (1 conductor + 24 specialist) |
| Stage pipeline | 9 |
| Target supportati | 8 |
| Script Python | 9 main + 5 lib + 14 test |
| Reference markdown | 34+ |
| Schema (md + json) | 24 (12 entità × 2) |
| Template scaffolding | 57 |
| File totali | 1059 |
