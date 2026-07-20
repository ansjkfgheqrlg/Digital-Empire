# P11 — Anti-Summary as Cultural Posture

> **Definizione canonica**: Più di un anti-pattern: una **postura culturale** che permea tutta la skill. Lint automatici, agenti dedicati (humanizer), regole esplicite nei system prompt, parole-bandiera vietate. La skill **detesta** il riassunto. Differenza con P03 (No-Summary, Always Expansion): P03 è il principio operativo, P11 è la cultura che lo rende durevole.

## Perché funziona

### 1. Le regole singole vengono dimenticate, la cultura no
Se metti "non riassumere" solo nel SP di un agente, presto o tardi un altro agente non lo riceve. Se invece **embedding nella cultura della skill** (lint automatici + agente dedicato + regole nelle conventions + esempi negativi ovunque), il principio sopravvive a turnover di componenti.

### 2. Gli LLM hanno tendenza fortissima a riassumere
Training data premia "sii conciso", "vai dritto al punto", "non ripetere". Risultato: default LLM è comprimere. Per ottenere expansion serve **contro-corrente sistematica**.

P11 è quella contro-corrente sistematica.

### 3. La cultura si vede nei dettagli, non nei manifesti
Una skill con "no summary" scritto in cima ma che usa "in conclusione" ovunque nel corpo è incoerente. Una skill che ha lint che blocca "in conclusione", agente humanizer che riscrive aperture stereotipate, e tutti gli esempi nel SP sono espansioni → coerente. La differenza la fanno i dettagli.

## Come applicarlo (operativo)

### Le 6 manifestazioni di P11 in content-forge

#### 1. Lint automatico (`scripts/no_summary_lint.py`)

Cerca pattern vietati in tutti i file `.md`:

```python
FORBIDDEN_PHRASES_IT = [
    r"\bin\s+sintesi\b",
    r"\briassumendo\b",
    r"\bin\s+breve\b",
    r"\bin\s+conclusione\b",
    r"\btl;dr\b",
    r"\bper\s+farla\s+breve\b",
    r"\bi\s+(?:tre|quattro|cinque)\s+punti\s+chiave\b",
]
FORBIDDEN_PHRASES_EN = [
    r"\bin\s+summary\b",
    r"\bto\s+summarize\b",
    r"\bin\s+short\b",
    r"\bthe\s+(?:three|four|five)\s+key\s+points\b",
]
```

Exit code != 0 se trovato (esclusi contesti legittimi: PLAN docs, anti-patterns.md).

#### 2. Agente dedicato (`humanizer-agent` O4)

Stage 7 Optimizer #4. Elimina LLM-speak (aperture stereotipate, vocaboli gonfiati, struttura ripetitiva) mantenendo significato.

Condizionale: attivo per output human-facing, skip per code/config.

#### 3. Vincolo nei system prompt

Ogni SP di agente che genera testo include in "What to avoid":

```
- LLM-speak: "It's important to note", "leverage", "comprehensive", "let's dive into"
- "In summary" / "In conclusione" / "TL;DR"
- Apologetic patterns ("scusa se", "spero che")
- Marketing speak
```

Hardcoded, non opzionale.

#### 4. Catalogo anti-pattern (`references/conventions/anti-patterns.md`)

Documenta esplicitamente perché il riassunto è anti-pattern, con esempi reali, perché si commette, recovery. Letto da tutti i builder come reference.

#### 5. Whitelist per meta-contesti

Lint sa riconoscere quando le parole-bandiera sono **menzionate** (in PLAN docs, in conventions) vs **usate** (in output reale). Whitelist heuristic:

```python
LEGITIMATE_CONTEXT_MARKERS = [
    "evita", "non usare", "vietato", "anti-pattern",
    "do not use", "forbidden", "PLAN",
]
```

Senza whitelist, il lint stesso fail sui propri file di documentazione (catch-22). Con whitelist, funziona correttamente.

#### 6. Esempi narrativi sempre espansi nel knowledge pack

Tutti i file di reference, processes, patterns hanno almeno 1 esempio **completamente espanso**, non riassunto. Costituisce esempio implicito della cultura.

### Il principio di "etichettatura forzata"

Anche quando aggiungi materiale (esempio, schema, controesempio), DEVI etichettarlo:
- `➕ Esempio aggiuntivo` (generato da te)
- `**Esempio (sorgente)**` (verbatim dal sorgente)
- `**Esempio (sorgente, parafrasato)**` (dal sorgente ma riformulato)

Senza etichettatura, il lettore non sa cosa fidarsi.

### Tone matching alla voce del sorgente

Il humanizer (O4) **non rende formale** un sorgente informale. Se il sorgente è transcript YouTube italiano con anglicismi naturali ("brief", "lead", "funnel"), l'output mantiene quello stile. Senza tone matching, "humanizer" sarebbe solo "formalizer" — ancora LLM-speak diverso.

## Esempi

### Esempio 1 — Run reale Phase 9

Test #1 con sorgente preventivi:
- MKD generato (5743 parole, 1.88x sorgente) → no_summary_lint passa (zero parole-bandiera trovate)
- Tutti gli esempi `➕` etichettati
- Tone Italian informal preservato
- Zero "in summary" / "in conclusione" nell'output finale

Phase 9 verdict per Test #1: PASS senza interventi humanizer (la cultura ha funzionato preventivamente).

### Esempio 2 — Catch reale del lint

Durante development di v1.1 ho scritto in un agente: "In conclusione, l'agente fa X..." → lint catch durante validation. Fix: riscritta come "L'agente fa X. Inoltre Y. Quindi Z."

Stesso meaning, zero LLM-speak.

### Esempio 3 — ➕ Pattern simile in altri domini

**Hemingway editor**: tool che cerca pattern verbosi, passive voice, parole complesse. Stessa filosofia di P11 (lint culturale) applicata a writing humanity.

**Strunk & White**, *The Elements of Style*: regole esplicite ("omit needless words", "use the active voice") che diventano cultura editoriale.

**Plain Language movement**: in legal writing, "no jargon" è cultura, non solo regola. Cattura tutti i casi via training continuo dei drafter.

## Anti-pattern correlato

**AP04 — LLM-Speak Output**: usare "leverage", "comprehensive", "robust", "delve into", aperture stereotipate. P11 esiste apposta per prevenirlo sistematicamente.

**Anti-pattern duale**: **Over-correction sterile** — humanizer aggressivo che rimuove ogni segno di "AI" rendendo l'output sterilizzato e privo di personalità. **Fix**: tone matching da sorgente, non standard "human voice" predefinito.

## Decision tree: "la mia skill ha postura anti-summary o solo regola?"

```
Hai un lint automatico che cerca parole-bandiera?
├─ NO → solo regola, fragile
└─ SÌ → continua
   ├─ Il lint è invocato in QA (bloccante)?
   │  ├─ NO → regola conoscibile ma evitabile
   │  └─ SÌ → enforce
   ├─ C'è un agente dedicato (humanizer) attivo per output testuali?
   │  ├─ NO → solo prevenzione, no correzione
   │  └─ SÌ → continua
   ├─ I SP di tutti gli agenti che generano testo hanno "avoid" list?
   │  ├─ NO → coerenza compromessa
   │  └─ SÌ → continua
   ├─ Il catalogo anti-pattern è scritto e referenziato?
   │  ├─ NO → cultura implicita, frail
   │  └─ SÌ → cultura esplicita ✅
   │
   └─ Hai whitelist per meta-contesti (PLAN, anti-patterns.md)?
      ├─ NO → lint catch-22, frustrato dai propri file
      └─ SÌ → cultura coerente e durevole ✅
```

## Quando NON applicare

- **Output puramente tecnico/code/config**: niente prosa, niente riassunto possibile. Humanizer skip.
- **Skill che fa esplicitamente riassunti** (es. "skill che riassume contratti legali"): P11 incompatibile. Costruisci skill diversa, non content-forge.
- **Skill multilingua con linguaggio non supportato dal lint**: serve estendere FORBIDDEN_PHRASES per quella lingua prima.

## Riferimenti esterni

- **Hemingway Editor** — Tool per writing style.
- **Strunk & White**, *The Elements of Style* — Cultura editoriale via regole.
- **Plain Language movement** — Anti-jargon in legal/government writing.
- **George Orwell**, *Politics and the English Language* — "Never use a long word where a short one will do" (ironicamente è proprio P11 applicato).
- **Anthropic Constitutional AI** — Approach simile: cultura embedded nei training data, non solo regole.

## Connessioni con altri principi

- Implementa: P03 (No-Summary, Always Expansion) — P03 è principio, P11 è la cultura che lo rende durevole
- Combina con: P05 (Markdown + Python) — il lint stesso è Python (L3), le regole sono in MD (conventions/anti-patterns.md)
- Necessario per: P08 (Depth Over Breadth) — depth richiede espansione, espansione richiede assenza di summary
- Validato da: scripts/no_summary_lint.py + agente O4 humanizer
