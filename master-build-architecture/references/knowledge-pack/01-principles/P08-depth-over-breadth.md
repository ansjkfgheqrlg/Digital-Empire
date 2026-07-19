# P08 — Depth Over Breadth

> **Definizione canonica**: Meglio 5 file profondi che 20 scaffold. Schemi stringenti che bloccano output magri. Content minimums enforced via validator. Quantità ≠ qualità: 50 reference scheletriche da 50 righe ognuna sono inutili rispetto a 5 reference operative da 300 righe.

## Perché funziona

### 1. Lo scaffold è debt mascherato da deliverable
Quando hai file con titolo + 3 frasi + TODO, sembri "completo" (alle metriche grezze: file count). Ma quando un agente o un umano legge quei file per fare lavoro, scopre che sono **vuoti**.

A quel punto: o fa fake-work (genera output a sua volta scaffold-y), o sospende e va a chiedere chiarimenti. **In entrambi i casi, hai pagato debt che non sapevi di avere.**

### 2. La profondità cattura il valore implicito
Un file con definizione canonica + 3 esempi + schema + anti-pattern + cross-ref **forza** chi lo scrive a pensare a tutto questo. Lo scaffold permette di evitare il pensiero.

L'agente downstream che legge il file con depth capisce. Quello che legge scaffold deve inferire.

### 3. La densità informativa scala meglio
File a depth alta sono usabili da agenti, umani, validator, future skill. File scaffold sono usabili solo come placeholder.

Trend: una volta che hai investito in 1 file profondo, riusi quel contenuto in molti contesti. 1 file scaffold = 1 uso (e quel uso è fake).

## Come applicarlo (operativo)

### Soglie operative per file in `references/`

| Tipo file | Minimo righe | Target righe | Cosa deve contenere |
|---|---|---|---|
| Concept/principle | 150 | 200-300 | Def + perché + 3 esempi + anti-pattern + decision tree + refs |
| Process | 200 | 300-500 | Step-by-step + esempio reale + failure modes + handoff |
| Pattern | 100 | 150-250 | Shape + when to apply + esempi + trade-off |
| Anti-pattern | 80 | 100-200 | Descrizione + perché si commette + esempio + recovery |
| Stage doc | 100 | 150-300 | Obiettivo + agente + I/O + failure modes + contract |
| Reference index | 30 | 50-100 | Lista + brief description |

Se un file è sotto soglia, **non è completo**. Stage 7 O3 (reference-expander) lo arricchisce automaticamente.

### Schemi stringenti come guardian

Phase 9 di content-forge ha aggiunto a `agent.schema.v0.3`:
```python
"agent_md_min_words": 400,
"system_prompt_min_words": 500,
"system_prompt_max_words": 1500,
"playbook_min_conversations": 5,
"failure_modes_min_count": 7,
"eval_cases_min": 8,
"eval_cases_max": 15
```

Risultato: skill validator fail se output thin. Forza builder + optimizer a fare lavoro vero.

Senza questi minimi, output scaffold passavano.

### Validator come gatekeeper non negoziabile

Schema validator non è "suggerimento". Se fail, pipeline non procede. Punto.

Pattern: PRIMA tighteni schema, POI vedi cosa rompe, POI fixi i builder/optimizer. **Mai** abbassare schema per fare passare output. Lo schema è la verità.

### Filosofia: file count = vanity metric

Conta:
- **Coverage atomi del KG nell'output** (P03 traceability)
- **Profondità media file** (parole / file)
- **Cross-reference density** (link interni per file)
- **Esempi etichettati `➕` per file**

NON conta:
- Numero totale file
- Dimensione totale repo
- "Quante cartelle ho"

## Esempi

### Esempio 1 — content-forge prima e dopo Phase 9

**Prima (Test #2 v1.0)**:
- 6 sub-skill in `copy-workflow/skills/`
- Ogni sub-skill: 1 file (`SKILL.md`) da ~10 righe
- File count: 6 ✅
- Profondità: ~10 righe/file ❌
- Usabili: 0/6 ❌

**Dopo (Phase 9 v1.1)**:
- 6 sub-skill (stesso count)
- Ogni sub-skill: 5 file (SKILL + 3 references + evals)
- File count: 30
- Profondità: ~150 righe/file
- Usabili: 6/6 ✅

Stessa intent originale, depth completamente diversa.

### Esempio 2 — Sezione "anti-patterns.md" magra vs ricca

**Magra** (P03 + P08 violati):
```markdown
# Anti-patterns
11 errori (5 bloccanti, 6 riduttori).
```
3 righe. Tecnicamente esiste. Praticamente: inutile.

**Ricca** (P08 rispettato):
```markdown
# Anti-patterns

> Catalogo di errori comuni nel costruire preventivi, con esempio reale e recovery.

## AP-01 — Preventivo single-page tipo fattura

**Cos'è**: condividere il preventivo come 1 pagina arida con solo prezzi + voci, senza
narrazione, brand, contesto.

**Perché si commette**: efficacy bias — "il cliente ha chiesto un preventivo, dico il prezzo".

**Esempio reale**:
"Ciao Mario, ecco il preventivo: sito web €1500. Saluti, Pier."
→ Tasso chiusura: ~5%.

**Perché non funziona**: il cliente non vede valore, solo costo. Difficile decidere senza
narrazione del progetto.

**Recovery**: minimo 5 pagine — copertina + presentazione + servizio + metodo + investimento.
Tasso chiusura medio: ~25-30%.

**Anti-pattern correlato**: AP-03 (lista della spesa).

## AP-02 — Parola "costo" invece di "investimento"

[... altre 5+ righe per ogni AP ...]
```

200+ righe. Operativo, riutilizzabile, formativo.

### Esempio 3 — ➕ Software architecture analogy

**Code review**: una PR con 50 file da 10 righe ognuno è peggio di 1 PR con 1 file da 200 righe ben strutturate. La review trova bug nel secondo, miss il pattern nel primo (death by 1000 paper cuts).

**Documentation**: 1 README ben fatto > 50 file di docs scattershot. Mike Bostock di D3.js famously diceva: "fewer, better" — vale per docs come per features.

## Anti-pattern correlato

**AP01 — Scaffold as Deliverable**: trattare scaffold come prodotto finito. Sintomo: declare "skill completata" quando in realtà serve solo come template da riempire a mano dopo.

**Anti-pattern duale**: **Bloat per metric** — gonfiare file per superare soglie validator (es. ripetere stessa info in 3 modi). Validator passa, qualità peggiora. **Fix**: depth = info density, non word density. Se il file è gonfio ma vuoto, è ancora violazione P08.

## Decision tree: "questo file è abbastanza profondo?"

```
File ha tutte le sezioni canoniche per il suo tipo? (definizione, esempio, ecc.)
├─ NO → ESPANDI sezioni mancanti
└─ SÌ → continua
   ├─ Lunghezza ≥ soglia minima per tipo?
   │  ├─ NO → ESPANDI con esempi, anti-pattern, refs
   │  └─ SÌ → continua
   ├─ Ha almeno 2 esempi distinti (1 sorgente, 1 ➕)?
   │  ├─ NO → AGGIUNGI esempi
   │  └─ SÌ → continua
   ├─ Ha schema/diagramma se applicabile?
   │  ├─ NO → AGGIUNGI se atomo strutturato
   │  └─ SÌ → continua
   ├─ Ha ≥2 cross-reference ad altri file?
   │  ├─ NO → AGGIUNGI in sezione "Connessioni"
   │  └─ SÌ → continua
   │
   └─ Apri il file con eyes fresh dopo 1 mese: capisci tutto senza altro?
      ├─ NO → ESPANDI ancora
      └─ SÌ → file OK
```

## Quando NON applicare (legittimo essere brevi)

- **Index/TOC files** (es. `references/_INDEX.md`): scopo è navigazione, non insegnamento. 20-50 righe OK.
- **README.md di sub-cartelle**: scopo è "cosa c'è qui", non documentare ogni file. 50-100 righe OK.
- **Frontmatter-only files** (es. config metadata): pura struttura YAML, 10 righe OK.
- **Catch-all glossary entries**: brevi entry sono OK in glossary se il termine è semplice.

## Riferimenti esterni

- **Anthropic skill-creator** — Pattern di "expand reference files when needed" è P08 implicit.
- **Edward Tufte**, *The Visual Display of Quantitative Information* — densità informativa come metrica di qualità.
- **Strunk & White**, *The Elements of Style* — "Omit needless words" — duale: includi parole necessarie. P08 = "include needed depth".
- **John Ousterhout**, *A Philosophy of Software Design* — concetto "deep modules": classi/funzioni che fanno molto con interfaccia semplice. P08 in software.
- **Andy Matuschak**, *Evergreen Notes* — note "evergreen" sono per definizione deep, non scaffold.

## Connessioni con altri principi

- Combina con: P03 (No-Summary, Always Expansion) — espandere significa fare depth
- Combina con: P06 (Shapes & Canonical Forms) — shape con content minimums forza depth
- Necessario per: P09 (Failure Modes First-Class) — failure_modes.md ricco richiede depth
- Validato da: scripts/schema_validator.py + Phase 9 Stage 7 (O3 reference-expander)
