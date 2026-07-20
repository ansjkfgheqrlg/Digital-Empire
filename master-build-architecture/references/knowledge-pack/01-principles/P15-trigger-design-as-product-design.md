# P15 — Trigger Design as Product Design

> **Definizione canonica**: La `description` nel frontmatter di una skill **NON è metadata cosmetico**: è il prodotto stesso visto dall'utente. Una skill che non triggera quando dovrebbe è una skill che non esiste. Trigger design = product design. Va iterata, testata su prompt realistici, scritta "pushy" per combattere undertriggering Anthropic-noto.

## Perché funziona

### 1. Una skill che non triggera è invisibile
La skill può avere internamente 200 agenti perfetti, depth incredibile, validators stringenti. Se Claude non la attiva quando l'utente ne ha bisogno → è come non esistere.

Trigger è il **single point of failure** della distribuzione. Va trattato con la stessa cura del kernel della skill.

### 2. LLM hanno tendenza all'undertriggering
Documentato dalla guida `skill-creator` di Anthropic: Claude tende a NON usare skill anche quando sarebbero utili, specialmente per task che "può fare da solo" (anche male).

Counter-strategia: description "pushy" con marker espliciti ("make sure", "whenever", "even if", "use this") che dicono esplicitamente a Claude "considera questa skill anche in casi marginali".

### 3. Edge cases sono dove vivono i bug di triggering
Trigger funziona bene su prompt "ovvi" tipo "voglio una skill che...". I bug emergono su:
- Prompt indiretti ("ho dei transcript e non so cosa farne")
- Prompt che usano parole correlate ma diverse (es. "voglio fare una guida" invece di "documento")
- Near-miss negativi (prompt che hanno keyword della skill ma NON dovrebbero attivarla)

Testare solo su prompt ovvi → falso senso di sicurezza.

## Come applicarlo (operativo)

### Anatomia di una description forte

```yaml
description: >-
  # Cosa fa (frase chiara)
  Trasforma <input X> in <output Y> per <use case Z>.

  # Quando attivare (specifico, include casi non ovvi)
  Use this whenever <obvious trigger>, even if user doesn't explicitly say <keyword>.
  Triggers on phrases like "<example phrase 1>", "<example phrase 2>", "<example phrase 3>".

  # Quando NON attivare (esplicito anti-trigger)
  DO NOT use for: <anti-case 1>, <anti-case 2>, <anti-case 3>.

  # Pushy reinforcement
  Make sure to consider this skill whenever <broad trigger>, even without keyword X.
```

### I 6 marker "pushy" (anti-undertriggering)

```
"make sure"      ← imperativo diretto a Claude
"whenever"       ← amplia trigger semantici
"even if"        ← gestisce edge case
"always"         ← rinforza priority
"use this"       ← invito esplicito
"do not use"     ← anti-trigger esplicito
```

Una description forte ne ha **3-4 minimum**. Senza marker, undertriggering quasi certo.

### Il trigger eval set (10+10)

Per testare trigger, costruisci eval set bilanciato:

**10 should-trigger** (la skill DEVE attivarsi):
- 2-3 prompt "ovvi" che menzionano keyword
- 3-4 prompt indiretti (intent c'è, keyword no)
- 2-3 prompt casuali / colloquiali (utente non-formale)
- 1-2 edge case sospetti

**10 should-NOT-trigger** (la skill NON deve attivarsi):
- 3-4 near-miss (keyword presenti ma intent diverso)
- 3-4 prompt che chiedono opposto (es. summary per skill no-summary)
- 2-3 prompt completamente unrelated

Esegui mentalmente o via tool real (es. `scripts/run_loop.py` di skill-creator). Target: 90%+ accuracy.

### Description optimization loop

Pattern formalizzato da Anthropic skill-creator:

1. Scrivi description v0
2. Run eval set
3. Misura accuracy + tasso trigger su should-trigger + tasso non-trigger su should-NOT
4. Identifica failure pattern (es. "tutti i prompt indiretti falliscono")
5. Iter description aggiungendo marker o frasi specifiche
6. Re-run eval
7. Ripeti fino a accuracy ≥90% E test set ≥80%

### Length sweet spot

| Lunghezza desc | Effetto |
|---|---|
| <500 chars | Troppo corta, Claude non ha contesto |
| 500-2500 chars | **Sweet spot** (sweet spot empirico) |
| >2500 chars | Diluition, Claude perde il punto |

content-forge v1.0: description 1694 chars con 6 pushy markers. Sweet spot.

### Anti-trigger esplicito è valore

Molti pensano che description debba solo dire "quando usare". Sbagliato. Dire **quando NON usare** è altrettanto importante:

```
DO NOT use this skill for:
- summaries/TL;DRs (it does the opposite — expands)
- simple file operations (rename/translate/format)
- single-question Q&A
- code generation
- when source is <500 words
```

Questo riduce falsi positivi e mantiene precision alta.

## Esempi

### Esempio 1 — content-forge v1.0 description

```yaml
description: >-
  Transforms raw, long, messy textual content (YouTube transcripts, workshop
  recordings, scattered articles, internal briefs, raw braindumps — single file
  OR an entire folder of files) into high-value operational artifacts: expanded
  markdown documents, AI agents, multi-agent teams, official Anthropic skills,
  executable workflows, orchestration layers, Obsidian second-brain wiki notes,
  or custom injections [...]. Never summarizes — always EXPANDS. [...]
  Use this skill whenever the user has raw text and wants to operationalize
  /refactor/expand it, even if they describe the target informally
  ("I have these transcripts and want to make an agent", "ho questi appunti e
  vorrei trasformarli in qualcosa"). Triggers on Italian phrases like "ho dei
  transcript/appunti/file da trasformare in...", "voglio estrarre tutto da
  questo materiale", and English equivalents. DO NOT use for: summaries/TL;DRs,
  simple file operations, single-question Q&A, code generation requests, or
  when source is <500 words. Make sure to consider this skill whenever the user
  mentions raw content + transformation intent, even without explicit "forge"
  keyword.
```

1694 chars, 6/6 pushy markers, esempi bilingui, DO NOT explicit.
Heuristic eval: 20/20 (100% accuracy).

### Esempio 2 — Errore di v1.0 corretto in v1.1

v1.0 description aveva:
- 3/6 pushy markers (no "do not use")
- Solo 1 lingua (italiano)
- No examples di phrasing
- 1251 chars

Trigger heuristic test: 80% accuracy. 4 falsi positivi/negativi.

v1.1 fix: + "do not use", + esempi bilingue, + phrasing examples → 100% accuracy.

### Esempio 3 — ➕ Pattern in altri contesti

**SEO meta description**: stesso identico problema. Page può essere perfetta ma se meta description non attrae click, page invisibile.

**App store optimization**: app icon + title + description. Decide install rate. Mesi di engineering possono essere distrutti da ASO sbagliato.

**Email subject lines**: stesso. Content può essere oro, ma se subject non apre, content non viene letto.

Pattern universale: **interface decide visibility**.

## Anti-pattern correlato

**AP-trigger-weak — Description debole**: descrizione vaga, generica, senza marker, senza anti-trigger. Sintomo: skill esiste ma "non triggera mai" dall'utente.

**Anti-pattern duale**: **Description aggressive over-triggering** — description così pushy che attiva la skill anche dove non dovrebbe. Sintomo: skill triggera su prompt unrelated, utenti irritati. **Fix**: bilanciare con DO NOT use esplicito.

## Decision tree: "la mia description è abbastanza forte?"

```
La description ha 3+ pushy markers ("make sure", "whenever", "even if", "always", "use this", "do not use")?
├─ NO → riscrivi con marker espliciti
└─ SÌ → continua
   ├─ Include "DO NOT use" section?
   │  ├─ NO → aggiungi (riduce falsi positivi)
   │  └─ SÌ → continua
   ├─ Include esempi di phrasing reale ("Triggers on 'X', 'Y'")?
   │  ├─ NO → aggiungi 3-5 esempi
   │  └─ SÌ → continua
   ├─ Length 500-2500 chars?
   │  ├─ NO (troppo corta) → espandi con esempi + anti-trigger
   │  ├─ NO (troppo lunga) → focus su core, rimuovi ridondanze
   │  └─ SÌ → continua
   │
   ├─ Eval set (10 should-trigger + 10 should-NOT) accuracy ≥90%?
   │  ├─ NO → identifica pattern fail, itera description
   │  └─ SÌ → description ready ✅
   │
   └─ Iterato ≥3 volte?
      ├─ NO → continua iteration, è normale
      └─ SÌ → diminishing returns, considera ship + monitor
```

## Quando NON applicare full P15

- **Skill private/internal** (no risk di undertriggering perché tu sai quando usarla)
- **Skill always-on** (es. monitoring background): non triggerano on demand, P15 N/A
- **Prototipi early-stage**: prima fai funzionare il core, poi ottimizza trigger

## Riferimenti esterni

- **Anthropic skill-creator** — Sezione "Description Optimization" è P15 formalizzato.
- **SEO best practices** — meta description optimization, stessi principi.
- **App Store Optimization (ASO)** — analogo: title + icon + description decidono install.
- **Persuasion theory** (Cialdini, Pratkanis) — perché certe formule linguistiche aumentano action probability.

## Connessioni con altri principi

- Combina con: P11 (Anti-Summary Cultural) — anti-trigger esplicito è applicazione cultura a description level
- Combina con: P09 (Failure Modes First-Class) — undertriggering è failure mode da catturare
- Combina con: P10 (Self-Improvement Loops) — se SI agents notano "skill non triggera su queste query", log FM → fix description
- Validato da: eval set + manual review + (opzionale) `scripts/run_loop.py` di skill-creator
