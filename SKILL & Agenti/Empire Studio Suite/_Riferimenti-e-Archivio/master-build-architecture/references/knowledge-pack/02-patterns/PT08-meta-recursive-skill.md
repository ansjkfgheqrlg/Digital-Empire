# PT08 — Meta-Recursive Skill (skill that builds skills)

> **Shape canonica**: La skill produce artifact dello stesso tipo della skill stessa, o di tipo che la skill stessa potrebbe usare. La skill dogfoodss continuamente. `content-forge target=skill` produce skill che a loro volta potrebbero diventare componenti di altre orchestrazioni gestite dalla skill stessa. **Loop creativo + validation continua + meta-learning**.

## Quando applicarlo

✅ **Applica se**:
- Stai costruendo una skill che produce skill / agenti / workflow
- Vuoi credibility ("la skill funziona perché la usiamo per costruire lei stessa")
- Hai pattern di principi che vuoi codificare e applicare consistente

❌ **NON applicare se**:
- Skill di dominio diverso (es. trading, customer support): meta-recursività artificiale
- Skill mono-purpose senza variabilità
- Early-stage prototype (prima costruisci core, poi pensa meta)

## Perché funziona

### 1. Dogfooding = quality forzato
Se costruisci la skill applicando le sue stesse regole, ogni regola sbagliata o incoerente viene scoperta subito. Senza dogfooding, le regole restano teoriche fino a quando un utente le subisce.

### 2. Credibility con utenti tecnici
Quando un utente vede che la skill ha applicato a sé stessa il pattern che predica, fiducia aumenta. "Funziona perché loro stessi la usano così" è il più forte signal di robustezza.

### 3. Meta-learning = template per nuovi target
Quando aggiungi un nuovo target, hai esempio concreto da copiare: la skill stessa. "Come strutturo agents/?" → guarda agents/ della skill. "Come scrivo schema?" → guarda references/schemas/. Replicabilità.

## Esempio dal nostro percorso

**content-forge è meta-recursive at level 3** (il massimo):

### Level 0 — Stesso pattern internamente
content-forge applica internamente i principi che predica:
- P02 Progressive Disclosure → SKILL.md è 236 righe < 500 limite
- P04 Interactive Scaffolding → builder usano PLAN→ASK→BUILD→CRITIQUE→ITERATE
- P09 Failure Modes First-Class → ogni agente ha sezione "Failure modes"

### Level 1 — Stessa forma canonica
content-forge ha:
- SKILL.md + references/ + scripts/ + assets/ + evals/
Esattamente come le skill che produce.

### Level 2 — Auto-applicabilità (teorica)
`/forge content-forge/ --target=skill` produrrebbe una nuova versione di content-forge applicando il proprio pipeline. Non l'abbiamo fatto ma è strutturalmente possibile.

### Level 3 — Self-improvement loop
Stage 10 SI agents girano su content-forge stessa. Continuous improvement automatico.

## Come implementarlo (operativo)

### Step 1 — Identifica meta-recursive layer

Decidi quali layer della skill devono essere meta-recursive:
- Solo principi (applica internamente ciò che predica)?
- Anche struttura (stessa forma canonica)?
- Anche self-improvement (Stage 10 pattern)?

content-forge va fino al level 3. Skill più semplici possono fermarsi a level 0.

### Step 2 — Validation di coerenza

Per ogni principio P che la skill predica:
1. Lista esplicita in `references/conventions/` o equivalente
2. Self-check: la skill applica P internamente?
3. Se sì, validator automatizzato (lint, schema check)
4. Se no, razionale esplicito documentato

### Step 3 — Auto-applicabilità (opzionale)

Se vuoi level 2, la skill deve poter ricevere sé stessa come input:
- Sorgente = la cartella della skill stessa
- Target = stessa tipologia (es. target=skill produce skill)
- Output: nuova versione applicando il proprio pipeline

Test: `/forge <self-path> --target=<self-type>` produce output non distrutto.

### Step 4 — Self-improvement (opzionale, level 3)

Implementa PT07 (Silent Observer) sulla skill stessa:
- Observer agents catturano FM dell'uso della skill
- Triage + plan automatico
- Phase iterations alimentate dai FM accumulati

## ➕ Esempio in altri domini

**Compiler bootstrap**: GCC compila sé stesso. Bug nel compilatore = bug nel proprio compile. Detection automatica via dogfooding.

**Self-hosting programming languages**: Rust scritto in Rust, Go scritto in Go. Forza maturazione.

**Knuth's TeX**: tipografato in sé stesso. Sistema descritto in libro tipografato col sistema. Meta-recursive ad alto livello.

**Anthropic skill-creator**: skill che insegna a creare skill. Lei stessa è skill conforme a sua propria pattern. Sempre meta-recursive.

## Anti-pattern correlato

**AP-meta — Predicare senza praticare**: skill con principi documentati ma li viola internamente. Sintomo: applicare validator alla skill stessa → FAIL.

**Anti-pattern duale**: **Recursive paralysis** — perfezionismo meta blocca shipping. "Non rilascio la skill finché level 3 perfetto su tutti i principi". Risultato: niente release. Fix: level 0-1 mandatory, level 2-3 ideali ma posticipabili.

## Trade-off

| Pro | Contro |
|---|---|
| Quality forzato via dogfooding | Implementation complessa |
| Credibility con utenti | Bug della skill colpiscono produzione skill stessa |
| Template auto-evidente | Coupling tra logiche (skill che produce + skill prodotto) |
| Meta-learning | Difficile bootstrap (chicken-and-egg) |

## Decision tree

```
La tua skill produce artifact strutturalmente simili a sé stessa?
├─ NO → meta-recursive non applicabile, skip
└─ SÌ → continua
   ├─ Predichi principi specifici nel tuo dominio?
   │  ├─ NO → meta-recursive limited
   │  └─ SÌ → continua
   │
   ├─ Hai bandwidth per dogfooding?
   │  ├─ NO → almeno level 0 (applica principi internamente)
   │  └─ SÌ → continua
   │
   └─ Implementa progressivamente:
      Level 0 (mandatory) — Stesso pattern
        → Per ogni principio P, validate che skill stessa lo applica
      Level 1 (raccomandato) — Stessa shape canonica
        → Skill ha layout = skill che produce
      Level 2 (opzionale) — Auto-applicabilità
        → Skill può ricevere sé stessa come input
      Level 3 (advanced) — Self-improvement
        → Observer agents osservano la skill in uso
```

## Connessioni

- Implementa: P13 (Meta-Recursive Applicability)
- Combina con: PT07 (Silent Observer) — meta-recursive level 3 = silent observer su sé stessa
- Combina con: PT06 (Schema Tightening) — dogfooding genera evidence per tightening
- Esempio reale: Anthropic skill-creator + content-forge

## Riferimenti

- Hofstadter, *Gödel, Escher, Bach* — strange loops e self-reference
- Compiler bootstrap (GCC, LLVM)
- Self-hosting languages (Rust, Go)
- Knuth's TeX e self-typesetting
- Anthropic skill-creator come esempio di meta-recursive skill
