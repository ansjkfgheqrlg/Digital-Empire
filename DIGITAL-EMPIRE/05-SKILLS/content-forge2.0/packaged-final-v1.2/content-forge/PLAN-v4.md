# 📐 PLAN v4 — Skill `content-forge` (comando `/forge`)

> **Cosa cambia rispetto a v3:**
> Policy esplicita **"Markdown è la spina, Python è il muscolo"**.
> - Tutti gli **agenti** restano `.md` (sono system prompt — devono essere letti da un LLM).
> - Tutte le **istruzioni operative** (stages, processes, patterns, conventions) restano `.md`.
> - **Embedded Python blocks** dentro i `.md` ovunque chiariscono un comportamento (JSON schema esatto, snippet che l'agente deve generare, pseudocodice di validazione).
> - **Reference machine-validable** (schemas) ora hanno **doppio file**: `.schema.md` (umano) + `.schema.json` (JSON Schema, parsabile).
> - **Aggiunta `scripts/lib/`**: moduli Python condivisi importati dagli script principali, per evitare duplicazione.
> - Inventario aggiornato: **8 scripts principali + 5 moduli `lib/` + 6 JSON Schema** in aggiunta a tutto v3.

---

## 0. La policy "Markdown + Python embedded"

### 0.1 Regola di decisione

| Domanda | Esito |
|---|---|
| Il file è letto da un LLM come istruzione (system prompt, processo, pattern, convention)? | → `.md` |
| Il file è eseguito da una macchina (verifica, parsing, packaging)? | → `.py` |
| Il file è uno schema che deve essere validato sia da umani sia da macchine? | → **doppio**: `.schema.md` + `.schema.json` |
| Dentro un `.md`, c'è un comportamento che è *più chiaro come codice* che come prosa? | → blocco ```python (o ```json) embedded |

### 0.2 Quando embeddare Python in un .md

Esempi concreti di quando un blocco python aggiunge valore:

- **In un agente builder**: "Quando produci `eval_cases.json`, deve avere ESATTAMENTE questa shape:" + blocco python con `dict literal` o blocco json.
- **In un processo**: "Lo step `coverage check` esegue questa logica:" + blocco python con pseudocodice eseguibile.
- **In una convention**: "Naming slug: applicare questa regex:" + blocco python `re.sub(...)`.
- **In un agente QA**: "La validazione DAG cerca cicli con questo algoritmo:" + blocco python con Kahn's algorithm.

Il principio: **se l'agente LLM produce o controlla codice/struttura, mostrargli il codice esatto è molto più potente che descriverlo a parole**. Riduce ambiguità a zero.

### 0.3 Quando NON embeddare Python

- Quando si sta spiegando il "perché" (rationale) o il "quando" (trigger) → resta prosa.
- Quando si sta dialogando con l'utente → resta prosa.
- Quando il codice sarebbe >40 righe → spostarlo in `scripts/lib/` come modulo e referenziarlo.

---

## 1-5. (Sezioni invariate da v3)

Conservate: intent, 9 pattern, 8 target, 11 agenti, diagramma di flusso.

---

## 6. Processi end-to-end (versione lunga in `references/processes/`)

Tutti già scritti. **In Fase 1 verranno arricchiti** con blocchi Python embedded nei punti chiave (es. forma esatta di `eval_cases.json`, validazione DAG, frontmatter parsing, ecc.). Vedi §8 per la lista delle aggiunte previste.

---

## 7. 📜 Inventario scripts (aggiornato: 8 principali + 5 lib)

### 7.1 Scripts principali (`scripts/`) — invariati da v3

| # | Script | Razionale |
|---|---|---|
| S1 | `transcript_cleaner.py` | Pulizia deterministica trascript |
| S2 | `atomizer.py` | Pre-segmentazione NLP per A2 |
| S3 | `coverage_check.py` | Verifica copertura atomi (lexical + semantic) |
| S4 | `no_summary_lint.py` | Lint anti-riassunto |
| S5 | `length_check.py` | Verifica vincoli di lunghezza |
| S6 | `schema_validator.py` | Validazione output contro JSON Schema |
| S7 | `obsidian_packager.py` | Integrità wikilink + MOC builder |
| S8 | `package_target.py` | Packaging finale `output/` |

### 7.2 Moduli condivisi (`scripts/lib/`) — **nuovo in v4**

| # | Modulo | Razionale |
|---|---|---|
| L1 | `kg_loader.py` | Carica/valida `kg.json`, espone API uniforme per accedere atomi, cluster, edge |
| L2 | `atom_matcher.py` | Match lessicale + semantico atomo↔testo (usato da S3, anche da agenti) |
| L3 | `frontmatter.py` | Parsing/serializzazione YAML frontmatter (usato da S6, S7) |
| L4 | `markdown_tools.py` | Parsing/manipolazione markdown (heading tree, TOC, link extraction) |
| L5 | `obsidian.py` | Helper specifici Obsidian: slug, wikilink integrity, MOC scaffold |

Tutti i moduli con test in `scripts/tests/test_lib_*.py`.

### 7.3 Tests (`scripts/tests/`)

Test pytest per ogni script principale e ogni modulo lib. Pattern: `test_<name>.py`. Eseguibili in CI o in locale con `pytest scripts/tests/`.

---

## 8. 📚 Inventario references (aggiornato per schemas dual)

### 8.1 Stages (7 `.md`) — invariato
### 8.2 Patterns (9 `.md`) — invariato
### 8.3 Processes (8 `.md`) — invariato, ma **da arricchire con embed Python** in:
- `skill.md`: aggiungere blocco `python` con shape esatta di `evals.json` e di `SKILL.md` frontmatter dict
- `agent.md`: aggiungere blocco `python` con shape esatta di `eval_cases.json` e formato schemas dell'agente
- `workflow.md`: aggiungere blocco `python` con pseudocodice validazione DAG (cycle detection)
- `team.md`: aggiungere blocco `python` con esempio di RACI matrix dict
- `wiki.md`: aggiungere blocco `python` con regex di slugification e formato esatto del frontmatter Obsidian
- `orchestration.md`: aggiungere blocco `python` con formato esatto di `registry.json`
- `custom.md`: aggiungere blocco `python` con shape esatta di `coverage_map.md` (tabella)
- `doc.md`: aggiungere blocco `python` con regex anti-summary

### 8.4 Schemas (6 entries — ognuna **dual file**) — **nuovo formato v4**

```
references/schemas/
├── kg.schema.md            # descrizione human-readable
├── kg.schema.json          # JSON Schema 2020-12, validabile
├── agent.schema.md
├── agent.schema.json
├── team.schema.md
├── team.schema.json
├── workflow.schema.md
├── workflow.schema.json
├── orchestration.schema.md
├── orchestration.schema.json
├── wiki-note.schema.md
├── wiki-note.schema.json
├── skill.schema.md
└── skill.schema.json
```

`schema_validator.py` (S6) carica il `.schema.json` e valida l'output del builder contro di esso. La versione `.md` è per documentazione umana.

### 8.5 Conventions (3 `.md`) — invariato
### 8.6 External (1 `.md`) — invariato

---

## 9. 📁 Struttura file finale (v4 — definitiva, pronta per scaffolding)

```
content-forge/
├── SKILL.md
├── agents/                                      # 11 agenti + Conductor (tutti .md)
│   ├── conductor.md
│   ├── pipeline/
│   │   ├── ingestion-agent.md                   # A1 — può avere ```python embedded per regex cleaner
│   │   ├── analyst-agent.md                     # A2
│   │   ├── knowledge-graph-agent.md             # A3 — embed schema kg.json
│   │   └── target-advisor-agent.md              # A4
│   ├── builders/                                # B1-B8 — tutti con ```python embed dove serve
│   │   ├── doc-builder-agent.md
│   │   ├── agent-builder-agent.md
│   │   ├── team-builder-agent.md
│   │   ├── skill-builder-agent.md
│   │   ├── workflow-builder-agent.md
│   │   ├── orchestration-builder-agent.md
│   │   ├── wiki-builder-agent.md
│   │   └── custom-builder-agent.md
│   ├── qa/
│   │   ├── coverage-verifier-agent.md           # C1 — embed pseudocodice match
│   │   └── target-schema-validator-agent.md     # C3 — embed riferimento a schema_validator.py
│   └── meta/
│       └── question-designer-agent.md           # D1
├── references/
│   ├── stages/                                  # 7 .md
│   │   ├── 01-ingestion.md
│   │   ├── 02-analysis.md
│   │   ├── 03-knowledge-graph.md
│   │   ├── 04-target-selection.md
│   │   ├── 05-interactive-build.md
│   │   ├── 06-coverage-check.md
│   │   └── 07-packaging.md
│   ├── patterns/                                # 9 .md (P1-P9)
│   │   ├── P1-atomic-extraction.md
│   │   ├── P2-claim-evidence-example.md
│   │   ├── P3-hierarchy-dependency.md
│   │   ├── P4-steelmanning.md
│   │   ├── P5-procedural-decomposition.md
│   │   ├── P6-mental-model-surfacing.md
│   │   ├── P7-schema-generation.md
│   │   ├── P8-cross-reference.md
│   │   └── P9-target-shape-mapping.md
│   ├── processes/                               # 8 .md (uno per target)
│   │   ├── doc.md
│   │   ├── agent.md
│   │   ├── team.md
│   │   ├── skill.md
│   │   ├── workflow.md
│   │   ├── orchestration.md
│   │   ├── wiki.md
│   │   └── custom.md
│   ├── schemas/                                 # 6 entries, dual .md + .json
│   │   ├── kg.schema.md
│   │   ├── kg.schema.json
│   │   ├── agent.schema.md
│   │   ├── agent.schema.json
│   │   ├── team.schema.md
│   │   ├── team.schema.json
│   │   ├── workflow.schema.md
│   │   ├── workflow.schema.json
│   │   ├── orchestration.schema.md
│   │   ├── orchestration.schema.json
│   │   ├── wiki-note.schema.md
│   │   ├── wiki-note.schema.json
│   │   ├── skill.schema.md
│   │   └── skill.schema.json
│   ├── conventions/                             # 3 .md
│   │   ├── naming.md                            # con regex Python embedded
│   │   ├── markdown-style.md
│   │   └── anti-patterns.md
│   └── external/
│       └── skill-creator.md
├── assets/
│   └── templates/                               # 8 set di template
│       ├── doc/
│       ├── agent/
│       ├── team/
│       ├── skill/
│       ├── workflow/
│       ├── orchestration/
│       ├── wiki/
│       └── custom/
├── scripts/                                     # 8 principali + 5 lib + tests
│   ├── transcript_cleaner.py
│   ├── atomizer.py
│   ├── coverage_check.py
│   ├── no_summary_lint.py
│   ├── length_check.py
│   ├── schema_validator.py
│   ├── obsidian_packager.py
│   ├── package_target.py
│   ├── lib/                                     # NUOVO
│   │   ├── __init__.py
│   │   ├── kg_loader.py
│   │   ├── atom_matcher.py
│   │   ├── frontmatter.py
│   │   ├── markdown_tools.py
│   │   └── obsidian.py
│   └── tests/
│       ├── test_transcript_cleaner.py
│       ├── test_atomizer.py
│       ├── test_coverage_check.py
│       ├── test_no_summary_lint.py
│       ├── test_length_check.py
│       ├── test_schema_validator.py
│       ├── test_obsidian_packager.py
│       ├── test_package_target.py
│       ├── test_lib_kg_loader.py
│       ├── test_lib_atom_matcher.py
│       ├── test_lib_frontmatter.py
│       ├── test_lib_markdown_tools.py
│       └── test_lib_obsidian.py
└── evals/
    └── evals.json
```

**Conteggi finali v4:**
- **11 agenti** + Conductor (12 file `.md`)
- **34 reference markdown** (7 stages + 9 patterns + 8 processes + 7 schemas-md + 3 conventions)
- **6 schemas JSON** (machine-validable)
- **8 script principali Python**
- **5 moduli Python condivisi** in `lib/`
- **13 file di test Python**
- **8 set di template** (numero di file in `assets/templates/` dipende dai template — ~25-30 file totali)
- **1 SKILL.md** kernel
- **1 evals.json**

**Totale: ~115 file** distribuiti in modo coerente con progressive disclosure.

---

## 10. Roadmap (aggiornata)

| Fase | Cosa produciamo | Stato |
|---|---|---|
| 0/0b/0c. PLAN v1-v3 + processes lunghi | piani e processi | ✅ |
| **0d. PLAN v4** | policy markdown+python | ✅ questo documento |
| 0e. Embed Python in processes esistenti | aggiungere blocchi `python`/`json` nei file processes | ⏳ in corso |
| **1. ARCHITECTURE** | scheletro completo di TUTTA la cartella `content-forge/` | ⏭ **next, subito** |
| 2. AGENTI | system prompt completi per gli 11 agenti + Conductor | |
| 3. PATTERNS & STAGES | contenuto vero di stages/ e patterns/ | |
| 4. SCRIPTS & SCHEMAS | 8 script + 5 lib + 6 JSON schema + tests | |
| 5. SKILL.md KERNEL | scrittura finale del kernel | |
| 6. TEMPLATES | template di scaffolding per ogni target | |
| 7. EVALS & TEST | evals.json + run dei 4 test case + iterazione | |
| 8. PACKAGING | `.skill` finale | |
