# P05 — Markdown + Python Embedded

> **Definizione canonica**: Il markdown è la spina dorsale (file leggibili da LLM come istruzioni), Python è il muscolo (logica deterministica). I file `.md` contengono blocchi ```python embedded quando il codice esatto chiarisce meglio della prosa. Reference machine-validable hanno dual format: `.schema.md` (umano) + `.schema.json` (parsabile).

## Perché funziona

### 1. Forza separation of concerns naturale
Quando devi decidere "questo è md o py?" ti poni la domanda: **chi legge questo?**
- LLM come istruzione → md
- Macchina come logica eseguibile → py
- Entrambi (es. uno schema) → entrambi (.schema.md + .schema.json)

Questa singola decisione driva architettura intera. Non è cosmetica.

### 2. Le LLM leggono male il codice in prosa, le macchine leggono male la prosa in codice
Se metti un algoritmo descritto in prosa, l'LLM lo "capisce" ma genera implementazioni leggermente diverse ogni volta = bug nondeterministici.

Se metti uno schema JSON come codice Python, una macchina lo deve eseguire — overhead inutile.

Embed Python in md = best of both: l'LLM **vede il codice** (zero ambiguità), e il file resta documentazione.

### 3. La doppia rappresentazione (md + json) è un investimento minimo per ROI alto
Il JSON Schema è parsato da validator. Il .md sta lì per umani che leggono. Stesso contenuto, due forme. Il costo di mantenerli sincronizzati è basso (validator stesso può checkare). Il beneficio: nessuno legge JSON volentieri, nessun validator parsa prosa.

## Come applicarlo (operativo)

### La regola di decisione

| Domanda | Esito |
|---|---|
| Il file è letto da un LLM come istruzione? (system prompt, processo, pattern) | → `.md` |
| Il file è eseguito da una macchina? (validator, parser, packager) | → `.py` |
| Il file è uno schema validabile sia da umani sia da macchine? | → **doppio** (.schema.md + .schema.json) |
| Dentro un `.md`, c'è un comportamento più chiaro come codice che prosa? | → blocco ```python (o ```json) embedded |

### Quando embeddare Python in .md

Esempi concreti di **quando aggiunge valore**:

```markdown
## Shape esatta di eval_cases.json

Il builder DEVE produrre questa shape:

```python
eval_cases_schema = {
    "agent_name": str,
    "cases": [
        {
            "id": str,
            "category": "happy" | "edge" | "failure" | "constraint",
            "prompt": str,
            "expected_behavior": str,
            "assertions": list
        }
    ]
}
```
```

L'LLM downstream vede esattamente cosa generare. Zero ambiguità.

Altri casi:
- Regex anti-pattern: `re.compile(r"\bin\s+sintesi\b", re.I)` invece di "cerca 'in sintesi' case insensitive"
- Algoritmi: Kahn's topological sort scritto come Python invece che descritto a parole
- Shape di dict: meglio `{"key": str, "value": int}` che "il dict ha key string e value int"

### Quando NON embeddare

- **Spiegare il "perché"** (rationale) → resta prosa
- **Spiegare il "quando"** (trigger condizionali) → resta prosa
- **Dialogo con l'utente** → resta prosa
- **Codice >40 righe** → spostalo in `scripts/lib/` e referenzialo, non incollarlo

### Lo schema dual: pattern

```
references/schemas/
├── agent.schema.md         ← human-readable: "qui spieghiamo che agent ha 7 file canonici, sono..."
└── agent.schema.json       ← Draft 2020-12: validato da scripts/schema_validator.py
```

Workflow:
1. Quando cambi qualcosa allo schema, **prima** modifica .json (autoritativo)
2. Poi aggiorna .md (descrittivo)
3. Validator usa .json
4. Builder e Conductor leggono .md per capire

Se i due divergono, .json wins (è quello che fail i test).

### Scripts/lib/ per codice riusabile

Quando hai logica riutilizzata da più script, NON copia-incollare. Metti in `scripts/lib/`:

```
scripts/
├── transcript_cleaner.py    # importa da lib
├── coverage_check.py        # importa da lib
└── lib/
    ├── kg_loader.py        # KG class, load_kg(), topological_atoms()
    ├── atom_matcher.py     # match lessicale + semantico
    ├── frontmatter.py      # parse/serialize YAML
    ├── markdown_tools.py   # extract_headings, build_toc, ecc.
    └── obsidian.py         # slugify, wikilink integrity
```

Pattern: ogni script è un orchestratore che usa moduli lib. Lib non importano da script.

## Esempi

### Esempio 1 — content-forge

References con embed Python:

- `references/processes/skill.md` ha:
  ```python
  PUSHY_MARKERS = [r"\bmake sure\b", r"\bwhenever\b", ...]
  def is_pushy(d): return any(re.search(p, d, re.I) for p in PUSHY_MARKERS)
  ```
  L'agente B4 (skill-builder) usa questo codice come riferimento per validare description.

- `references/processes/workflow.md` ha:
  ```python
  def has_cycle(edges, nodes):
      # Kahn's topological sort
      ...
  ```
  L'agente B5 (workflow-builder) deve generare DAG no-cycle. Avere l'algoritmo qui rende la generazione robusta.

- `references/processes/wiki.md` ha:
  ```python
  def slugify(title, style="kebab"):
      ...
  ```
  Tutti gli agenti che producono note Obsidian usano stessa convenzione.

### Esempio 2 — Lib usato da 3 script diversi

`scripts/lib/atom_matcher.py` è usato da:
- `scripts/coverage_check.py` (C1)
- Indirettamente da `scripts/schema_validator.py` (C3)
- Indirettamente da test in `scripts/tests/`

Se cambi la logica di match, cambi in un punto solo. Senza lib, avresti 3 copie e divergerebbero.

### Esempio 3 — ➕ Anthropic skill-creator

`skill-creator` stessa segue P05:
- `SKILL.md` (md, kernel)
- `references/` (md, documentazione)
- `scripts/aggregate_benchmark.py` (py, calcolo benchmark)
- `scripts/run_loop.py` (py, optimization loop)
- `scripts/package_skill.py` (py, packaging)
- `agents/grader.md` (md, SP subagente con embedded JSON schema della grading.json)

Stessa pattern. Universale per skill complesse.

## Anti-pattern correlato

**AP02 — Permissive schemas**: schema JSON con `additionalProperties: true` ovunque, nessun `required`, nessun `minLength`. Risultato: schema validator passa tutto, garantisce nulla. Phase 9 ha tightened a v0.3.

**Anti-pattern duale**: **Code-in-prose stack overflow** — scrivere algoritmi complessi in prosa narrativa ("prima ordini, poi se è maggiore di 5 fai...") invece di pseudocode/code. Risultato: bug nondeterministici. **Fix**: appena la prosa diventa ambigua, switcha a code block.

## Decision tree: "questo bit di info dove va?"

```
È istruzione per un LLM?
├─ SÌ → file .md
│  └─ La parte specifica è codice/struttura?
│     ├─ SÌ → embed ```python o ```json nel .md
│     └─ NO → prosa nel .md
│
È logica deterministica eseguibile?
├─ SÌ → file .py
│  └─ Usato da ≥2 altri script?
│     ├─ SÌ → scripts/lib/
│     └─ NO → scripts/ direttamente
│
È schema validabile?
└─ SÌ → DUAL: .schema.md + .schema.json
```

## Quando NON applicare

- **Skill puramente conversazionali** (no struttura, no validator): un solo SKILL.md, nessun script, nessuno schema. P05 è overkill.
- **Prototipi throwaway**: tutto in 1 file, decideremo dopo.
- **Skill che orchestrano solo skill esistenti** (target=orchestration con componenti esterni): poco codice proprio, prevalentemente reference.

## Riferimenti esterni

- **Anthropic skill-creator** — Pattern stesso (md + py + json schemas).
- **JSON Schema Draft 2020-12** — Standard ufficiale per schemi.
- **Literate Programming** (Donald Knuth) — Idea originale: codice e documentazione mescolati. P05 è una variante leggera applicata al contesto LLM.
- **Sphinx + autodoc** (Python ecosystem) — Same idea: doc e codice convivono, doc estrae dal codice.

## Connessioni con altri principi

- Combina con: P02 (Progressive Disclosure) — la decisione "md vs py vs lib" è una sub-decisione di "che livello?"
- Combina con: P06 (Shapes & Canonical Forms) — gli schemi dual sono la formalizzazione delle shapes
- Necessario per: P08 (Depth Over Breadth) — depth richiede precisione, embedded Python la fornisce
