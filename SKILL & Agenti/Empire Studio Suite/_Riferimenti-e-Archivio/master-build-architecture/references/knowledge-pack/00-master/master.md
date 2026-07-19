# Master Knowledge Document (MKD)

> **Documento maestro.** Espansione completa di tutta la conoscenza estratta da Ruflo, Content-Forge 2.0, Context-Engineering-Advisor, Skill-Creator e Knowledge Pack.

## Struttura

Questo documento è la fonte di verità per il skill Master-Build-Architecture. Contiene:

1. **15 Principi** (P01-P15) — vedi `01-principles/`
2. **11 Pattern** (PT01-PT11) — vedi `02-patterns/`
3. **9 Anti-Pattern** (AP01-AP09) — vedi `03-anti-patterns/`
4. **7 Processi** (PR01-PR07) — vedi `04-processes/`
5. **6 Decision Tree** (DT01-DT06) — vedi `05-decision-trees/`
6. **4 Case Studies** (CS01-CS04) — vedi `06-case-studies/`
7. **Template** — vedi `07-templates/`
8. **Glossario** — vedi `08-glossary/`
9. **FAQ** — vedi `09-faq/`
10. **Reference Esterne** — vedi `10-references/`

## Sintesi dei 15 Principi

| # | Principio | Essenza |
|---|---|---|
| P01 | Iterative Planning | Mai un piano solo; PLAN-v1 → vN |
| P02 | Progressive Disclosure | SKILL.md lean, dettagli in refs |
| P03 | No-Summary-Expansion | Ogni atomo diventa più ricco, mai più povero |
| P04 | Interactive Scaffolding | PLAN → ASK → BUILD → CRITIQUE → ITERATE |
| P05 | Markdown+Python | Markdown per struttura, Python embedded per logica |
| P06 | Shapes & Canonical Forms | Forme canoniche per ogni target |
| P07 | Three-Level Architecture | Kernel + Specialists + Tools |
| P08 | Depth over Breadth | Profondità prima di ampiezza |
| P09 | Failure-Modes First-Class | failure-modes.md in ogni agente |
| P10 | Self-Improvement Loops | Memory first, CP dopo OGNI step |
| P11 | Anti-Summary Culture | Espandere, mai riassumere |
| P12 | Traceability | Ogni output cita ≥3 fonti |
| P13 | Meta-Recursive | Skill che produce skill |
| P14 | Silent Operation | Default: non disturbare |
| P15 | Trigger Design as Product | I trigger sono prodotto, non dopo-pensiero |

## Sintesi degli 11 Pattern

| # | Pattern | Applicazione |
|---|---|---|
| PT01 | Conductor-with-Subagents | Ruflo queen, orchestrazione |
| PT02 | Pipeline-Stages-with-Handoff | Content-Forge 9 stadi |
| PT03 | Builder-Then-Optimizer | Costruisci, poi ottimizza |
| PT04 | Question-Designer | Domande adattive |
| PT05 | Canonical-Files-per-Target | 7 file per agente |
| PT06 | Schema-Tightening-Loop | Schema evolve v1→vN |
| PT07 | Silent-Observer | Osservazione senza side-effects |
| PT08 | Meta-Recursive-Skill | Skill che produce se stessa |
| PT09 | Multi-Source-with-Traceability | Più fonti, tracciamento |
| PT10 | Master-Document-Intermediate | MKD come intermedio |
| PT11 | Validation-with-Auto-Fix | Valida e auto-correggi |

## Sintesi dei 9 Anti-Pattern

| # | Anti-Pattern | Sintomo | Prevenzione |
|---|---|---|---|
| AP01 | Scaffold-as-Deliverable | Stub spacciati per completi | Gate di completezza |
| AP02 | Permissive-Schemas | Accettare tutto | PT06 schema-tightening |
| AP03 | User-Driven-Overhead | Troppi step manuali | Automazione canonica |
| AP04 | LLM-Speak-Output | Output vago/LLM-style | Concretezza, esempi |
| AP05 | Monolithic-Skill-MD | SKILL.md >500 righe | Progressive disclosure |
| AP06 | Feature-Creep | Aggiungere senza motivo | Scope definito |
| AP07 | Skipping-the-Plan | Partire senza PLAN-v1 | P01/P04 |
| AP08 | No-Failure-Mode-Doc | Agenti senza failure-modes | P09 |
| AP09 | Premature-Optimization | Ottimizzare prima di costruire | P08 depth-first |

## Sintesi dei 7 Processi

| # | Processo | Steps | Quando |
|---|---|---|---|
| PR01 | Iterative Plan Creation | Vision → PLAN-v1 → ASK → BUILD → CRITIQUE → PLAN-vN | Sempre |
| PR02 | Content-Forge Pipeline | Ingestion → Analysis → MKD → Build → Depth → SI → Validate → Package | Per ogni contenuto |
| PR03 | Agent Construction | Schema → spec → system-prompt → tools → playbook → evals → failure-modes → memory | Per ogni agente |
| PR04 | Validation Cycle | Schema check → Coverage → FM validation → Fix → Re-validate | Dopo ogni build |
| PR05 | Memory Lifecycle | Bootstrap → CP/DEC dopo ogni step → INDEX update → Sync → Consolidate | Sempre |
| PR06 | Self-Improvement | Failure detect → Triage → Silent observe → Plan fix → Apply → Verify | Continuo |
| PR07 | Packaging & Release | Validate all → Bundle → .skill → Test install → Document → Release | Fine progetto |

## Sintesi dei 6 Decision Tree

| # | Decision Tree | Domanda | Esiti |
|---|---|---|---|
| DT01 | Topology Selection | Tipo di swarm? | Hierarchical / Mesh / Pipeline |
| DT02 | Agent Count | Quanti agenti? | Minimal (≤10) / Standard (10-25) / Large (25+) |
| DT03 | Memory Strategy | Quale memoria? | Short-term only / Two-layer / Full (AgentDB) |
| DT04 | Depth vs Breadth | Priorità? | Depth-first (P08) / Breadth-first |
| DT05 | Meta-Recursive Need | Skill che produce skill? | Sì (PT08) / No |
| DT06 | Release Readiness | Pronto per release? | Sì / No (gap list) |

## Connessioni

Questo documento è il nodo centrale. Ogni sezione punta a file dettagliati nelle cartelle specifiche. Gli agenti della skill usano questo MKD come riferimento per estrarre principi, pattern e processi.

**Trace:** Ruflo (swarm/memory/federation) + Content-Forge 2.0 (9-stage pipeline, 25 agents, MKD) + Context-Engineering-Advisor (two-layer memory, Research→Plan→Reset→Implement) + Skill-Creator (evals loop, SKILL.md anatomy) + Knowledge Pack (15P, 11PT, 9AP, 4CS, glossary).
