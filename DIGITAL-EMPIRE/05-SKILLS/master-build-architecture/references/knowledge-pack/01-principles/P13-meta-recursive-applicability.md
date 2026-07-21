# P13 — Meta-Recursive Applicability

> **Definizione canonica**: La skill applica a sé stessa il pattern che predica. Una skill che insegna "fai PLAN→ASK→BUILD→CRITIQUE→ITERATE" deve essere stata costruita con quel pattern. Una skill che produce skill deve essere essa stessa una skill conforme. **L'incoerenza tra principio predicato e principio applicato distrugge la credibilità.**

## Perché funziona

### 1. Coerenza percepita = trust
Gli utenti (umani e LLM) sentono l'incoerenza. Se una skill predica "no riassunti" ma la sua propria documentazione è scaffold-y, l'utente impara: "queste regole sono per qualcun altro, non per questa skill". Trust eroso.

Quando la skill **vive** i suoi principi, l'utente li impara per osmosi, e si fida che il sistema fa quello che dice.

### 2. Dogfooding cattura bug fondamentali
Se costruisci una skill X applicando le sue stesse regole, scopri quasi subito quando le regole non funzionano o si contraddicono. Senza dogfooding, le regole restano teoriche fino a quando un utente le subisce.

content-forge è meta-recursive: target=skill produce una skill applicando lo stesso pipeline che ha generato content-forge stessa. Ogni problema della skill emerge in produzione, non in test isolati.

### 3. Forza esplicitezza dei principi
Per applicare un pattern a te stesso devi **codificarlo formalmente**. Non puoi cavartela con "lo facciamo a sensazione". Diventa tracciabile, validabile, insegnabile.

## Come applicarlo (operativo)

### I 4 livelli di meta-recursività

**Livello 0 — Stesso pattern**: la skill usa internamente i pattern che predica.
Esempio: content-forge predica "interactive scaffolding" (P04), e i suoi builder usano interactive scaffolding internamente.

**Livello 1 — Stessa struttura canonica**: la skill ha la stessa forma canonica che genera per altre skill.
Esempio: content-forge ha `SKILL.md + references/ + scripts/ + evals/` esattamente come le skill che produce.

**Livello 2 — Auto-applicabilità**: la skill può prendere sé stessa come input e produrre output sensato.
Esempio: `/forge content-forge/ --target=skill` produrrebbe una nuova versione di content-forge applicando il proprio pipeline.

**Livello 3 — Self-improvement**: la skill osserva sé stessa in produzione e cattura miglioramenti automatici (Stage 10 SI agents).

Livelli 0 e 1 sono mandatory per essere "meta-recursive". Livelli 2 e 3 sono advanced.

### Check di coerenza

Per ogni principio P che la skill predica, chiedi:
1. La skill **applica** P internamente?
2. Se no, c'è un razionale esplicito (es. "P non si applica a questo tipo di componente perché...")
3. Se sì, è verificabile (validator, lint, eval)?

Se rispondi "no/sì incerto" a qualcuna, hai incoerenza meta-recursiva.

### Esempio di check applicato

| Principio | Predicato? | Applicato a sé? | Verifica |
|---|---|---|---|
| P02 Progressive Disclosure | Sì | Sì: SKILL.md di content-forge è 236 righe < 500 | Word count |
| P03 No-Summary | Sì | Sì: tutte le reference >150 righe, no parole-bandiera | `no_summary_lint.py` |
| P04 Interactive Scaffolding | Sì | Sì: builder usano PLAN→ASK→BUILD→CRITIQUE→ITERATE | Process docs |
| P06 Shapes & Canonical Forms | Sì | Sì: content-forge stessa ha shape skill canonica | `schema_validator.py --target skill` |
| P07 Three-Level Architecture | Sì | Sì: SKILL.md (L1) + agents/ (L2) + scripts/ (L3) | Filesystem layout |
| P08 Depth Over Breadth | Sì | Sì: phase 9 tightening schema enforce | `schema_validator.py v0.3` |
| P09 Failure Modes First-Class | Sì | Sì: ogni agente ha sezione "Failure modes" | Manual review |
| P10 Self-Improvement Loops | Sì | Sì: Stage 10 SI agents su content-forge stessa | Auto-execution |

content-forge passa il check di meta-recursività su tutti i principi che predica.

### Anti-pattern: predicare senza praticare

Sintomi tipici:
- Skill predica P03 (no riassunti) ma il suo README.md è 20 righe scaffold
- Skill predica P09 (failure modes) ma i suoi propri agenti non hanno failure_modes.md
- Skill predica P02 (progressive disclosure) ma il suo SKILL.md è 1500 righe monolitiche

Detection: schema_validator applicato alla skill stessa. Se la skill fail il proprio schema, c'è incoerenza meta-recursiva.

## Esempi

### Esempio 1 — content-forge come dogfood

content-forge ha 10 stage. Per testarla in Phase 7, ho:
1. Preso un sorgente reale (Manuale APSOC)
2. Eseguito il pipeline mentalmente seguendo il SP di ogni agente
3. Trovato 4 bug reali che ho fixato

Questo è dogfooding: la skill è messa alla prova dalle sue stesse regole. Senza, i 4 bug sarebbero emersi solo in produzione presso utenti reali.

### Esempio 2 — Errore di non-meta-recursività

Phase 8 v1.0 di content-forge predicava "no summary" ma il PLAN.md originale aveva sezioni tipo "In sintesi:" all'inizio. Quando l'utente ha letto il PLAN: "ma allora la regola vale per gli output, non per i PLAN?".

Fix: rimossi summary dai PLAN. Coerenza ripristinata.

### Esempio 3 — ➕ Pattern in altri sistemi

**Compiler bootstrap**: un compilatore che si auto-compila (es. il compiler GCC che compila sé stesso) è meta-recursive. Se il compilatore ha bug nel generare codice, il bug si propaga al compilatore stesso → detection automatica.

**Self-hosting programming languages**: linguaggi scritti in sé stessi (Rust, Go) sono meta-recursive. Costringono maturazione.

**Test framework**: framework di test (es. pytest) ha test scritti usando sé stesso. Coverage di se stesso è metrica di qualità.

## Anti-pattern correlato

**AP-meta — Predicare senza praticare**: skill che ha principi documentati ma li viola internamente. Sintomo: applicare schema_validator alla skill stessa → FAIL.

**Anti-pattern duale**: **Recursive paralysis** — voler meta-recursività perfetta blocca shipping. Es. "non posso rilasciare la skill perché applicare P10 a sé stessa richiederebbe..." → resta ferma in develop. **Fix**: meta-recursive ai livelli 0-1 è mandatory per shipping; livelli 2-3 sono ideali ma posticipabili.

## Decision tree: "la mia skill è meta-recursive?"

```
Per ogni principio P che la mia skill predica:
│
├─ La skill applica P a sé stessa?
│  ├─ NO → fix incoerenza prima di shipping
│  └─ SÌ → continua
│
├─ Esiste un test/validator che lo verifica?
│  ├─ NO → meta-recursività è informale, fragile
│  └─ SÌ → continua
│
└─ Il test passa sulla skill stessa?
   ├─ NO → fix la skill, non il test
   └─ SÌ → meta-recursive su questo principio ✅

Se passi check su TUTTI i principi:
   → meta-recursive at level 0-1 ✅

Se posso fare /forge skill/ --target=skill e produce nuova versione sensata:
   → meta-recursive at level 2 ✅

Se Stage 10 SI agents girano sulla skill stessa:
   → meta-recursive at level 3 ✅
```

## Quando NON applicare

- **Skill che gestiscono dominio diverso da quello di costruzione skill** (es. skill di trading): non c'è motivo di meta-recursività diretta. Si applica solo dove la skill può essere preda di sé stessa.
- **Skill in evoluzione molto rapida**: meta-recursività richiede stabilità di principi. Se principi cambiano ogni settimana, applicarli a sé stessa è instabile.

## Riferimenti esterni

- **Hofstadter**, *Gödel, Escher, Bach* — meta-recursive structures e strange loops come pattern epistemici.
- **Lisp / Scheme** — linguaggi homoiconic: code è data, meta-recursività naturale.
- **Compiler bootstrap** (es. GCC self-hosting).
- **Anthropic skill-creator** — meta-recursive: una skill che crea skill applicando le sue regole.

## Connessioni con altri principi

- Necessario per: P01 (Iterative Planning) — iterare il PLAN della skill è meta-applicazione di P01 a sé
- Combina con: P04 (Interactive Scaffolding) — la skill usa il pattern che predica
- Combina con: P10 (Self-Improvement Loops) — auto-osservazione è meta-recursività a livello 3
- Validato da: schema_validator applicato alla skill stessa + lint applicato ai propri file
