# P06 — Shapes & Canonical Forms

> **Definizione canonica**: Ogni target ha una **forma canonica** (file canonici, sezioni obbligatorie, campi minimi). La skill conosce le shape, mappa il knowledge graph del sorgente sopra di esse, valida il risultato contro lo schema canonico. **Senza shape, hai output che sembrano completi ma sono inutilizzabili.**

## Perché funziona

### 1. Le shape sono contratti
Quando un agente sa che il suo output deve essere "un agente con 7 file canonici", non c'è ambiguità su cosa produrre. Quando lo schema enforce questo, non c'è ambiguità su cosa accettare.

Senza shape, ogni agente produce "qualcosa che sembra un agente" e l'utente downstream deve indovinare se è installabile.

### 2. Le shape catturano expertise di dominio
La forma canonica di un agente (7 file: agent.md, system_prompt.md, tools.md, playbook.md, failure_modes.md, eval_cases.json, README.md) NON è arbitraria. È il risultato di esperienza accumulata di cosa serve per avere un agente production-ready.

Quando codifichi questa expertise in una shape, tutti i builder beneficiano. Senza, ogni builder reinventa.

### 3. Le shape rendono validabile la "completezza"
"Questa skill è completa?" è una domanda vaga senza shape. Con shape canonica, diventa: "ha tutti i file richiesti? Hanno il minimo content? Schemi referenziali sono integri?". Domande binarie, automatizzabili.

## Come applicarlo (operativo)

### Le shape canoniche di content-forge (esempi)

#### Shape `agent` (7 file canonici)

```
<agent-slug>/
├── agent.md              ← ≥400 parole, sezioni: Identità, Obiettivi, Utente, Comportamento, Vincoli, Tono, Metriche
├── system_prompt.md      ← 500-1500 parole, copy-paste ready
├── tools.md              ← 1 tool min, ognuno con schema I/O, esempi, errori
├── playbook.md           ← 5+ conversazioni: 3 happy + 1 edge + 1 failure recovery
├── failure_modes.md      ← 7+ failure, tabella ID|Failure|Sintomo|Prev|Rilev|Recupero
├── eval_cases.json       ← 8-15 cases, distribuzione 40h/30e/20f/10c
└── README.md             ← 100+ parole, installazione + uso
```

#### Shape `skill` (Anthropic-compliant)

```
<skill-slug>/
├── SKILL.md              ← 80-500 righe, frontmatter (name + description pushy)
├── references/           ← min 3 file, min 300 righe totali
│   └── ... (concepts/, stages/, processes/, patterns/, conventions/, schemas/)
├── agents/               ← se serve (skill complex)
├── scripts/              ← se serve (logica deterministica)
├── assets/templates/     ← se serve
├── evals/evals.json      ← 4+ test prompts
└── README.md
```

#### Shape `team` (multi-agente)

```
<team-slug>/
├── topology.md           ← supervisor | pipeline | peer-to-peer | hub-spoke | hybrid
├── coordinator.md        ← se topology in [supervisor, hub-spoke]
├── agents/               ← min 2 agenti, ognuno con ≥5/7 file canonici
├── communication_protocol.md
├── handoff_rules.md      ← RACI strict (1 R per responsibility)
├── failure_handling.md   ← ≥5 failure mode
├── shared_state.md
├── team_eval_cases.json  ← ≥3 scenari end-to-end
└── README.md
```

### Dual schema (md + json) per ogni shape

```
references/schemas/
├── agent.schema.md     ← human-readable
├── agent.schema.json   ← Draft 2020-12, validabile
├── skill.schema.md
├── skill.schema.json
├── team.schema.md
├── team.schema.json
└── ... (uno per ogni target)
```

### Validazione bloccante

Schema validator (`scripts/schema_validator.py`) controlla:
- File canonici presenti
- Frontmatter ha campi obbligatori
- Content minimums rispettati (parole, conversazioni, ecc.)
- Integrità referenziale (i pointer interni risolvono)
- Check custom per target (es. DAG no-cycle per workflow)

Se fail: pipeline NON procede. Output non viene packaged.

### Tightening progressivo

Le shape evolvono: cominci con schema permissivo (additionalProperties: true), poi tighteni man mano che vedi cosa va male.

Phase 9 di content-forge è stata esattamente questo: schemas v0.2 (permissivi) → v0.3 (stringenti):
- `references_min_files: 3` aggiunto (era senza minimo)
- `playbook_min_conversations: 5` aggiunto
- `failure_modes_min_count: 7` aggiunto
- `system_prompt_min_words: 500` aggiunto

Risultato: skill che prima passavano sintatticamente ora vengono bloccate se thin.

## Esempi

### Esempio 1 — Shape applicata in content-forge

Quando l'utente chiede target=skill, B4 (skill-builder) sa esattamente cosa produrre perché legge `references/schemas/skill.schema.md` E `references/processes/skill.md`. Genera, poi C3 valida contro `skill.schema.json`. Se fail → loop ITERATE.

### Esempio 2 — Errore catturato dallo schema

Test reale Phase 9: `copy-workflow` v1.0 aveva 6 sub-skill con UN solo `SKILL.md` ciascuna (no references/). Schema v0.3 con `references_min_files: 3` → schema validator emette 6 errori bloccanti. Forge non procede a packaging. Stage 7 O1 espande automaticamente.

Senza shape stringente: 6 sub-skill thin sarebbero state packaged, l'utente avrebbe ottenuto roba inutile.

### Esempio 3 — ➕ Shape in Domain-Driven Design

In DDD (Eric Evans), gli **Aggregate** sono shape canoniche: "un Order Aggregate ha root Order, contains OrderLines, has Invariant 'total = sum(lines)'". Codice che non rispetta la shape (es. modifica OrderLine senza passare per Order root) fallisce build/test.

Same idea: shape canonica + validator che enforce.

Altri: **OpenAPI specs** per API REST, **Avro schemas** per data pipelines, **Protobuf messages** per gRPC.

## Anti-pattern correlato

**AP01 — Scaffold as Deliverable**: produrre output strutturalmente valido (passa schema permissivo) ma con content placeholder. Sintomo: file presenti ma vuoti / `<REPLACE>` ovunque. **Fix**: schema con content minimums (P06 + P08 combinati).

**Anti-pattern duale**: **Over-constraining schemas** — schema così stringenti che nessun output reale li passa. Risultato: builder forzati a generare riempitivo per soddisfare il validator. **Fix**: tighten progressivo basato su esperienza, non a priori.

## Decision tree: "ho bisogno di definire una nuova shape?"

```
Sto producendo un tipo di artefatto NUOVO (non variante di esistenti)?
├─ NO → riusa shape esistente, eventualmente con varianti opzionali
└─ SÌ → continua
   ├─ L'artefatto avrà ≥3 file canonici?
   │  ├─ NO → 1-2 file, basta convenzione informale (no schema)
   │  └─ SÌ → continua
   ├─ Verrà prodotto da agenti automaticamente (non solo umani)?
   │  ├─ NO → solo .md documentale, no JSON Schema
   │  └─ SÌ → DUAL: .schema.md + .schema.json
   │
   └─ Procedi con definire:
      1. Required files (lista)
      2. Required sections in main file
      3. Content minimums (words/items)
      4. Referential integrity rules
      5. Custom checks (es. DAG no-cycle)
```

## Quando NON applicare

- **Output narrativo libero** (es. saggio creativo): forzare shape uccide la flessibilità.
- **Prototipi monouso**: shape è investimento per riuso. Senza riuso, è overhead.
- **Output puramente esplorativi**: brainstorming, ideazione. Shape distruggerebbe la divergenza.

## Riferimenti esterni

- **Eric Evans**, *Domain-Driven Design* (2003) — Aggregate, Bounded Context, Ubiquitous Language. Tutto è formalizzato in shape.
- **JSON Schema** — Standard per validation. Draft 2020-12 è il più recente.
- **OpenAPI** — Shape per REST APIs.
- **Apache Avro / Protocol Buffers** — Shape per data serialization.
- **Anthropic skill-creator** — Pattern di skill con SKILL.md + frontmatter required è già una shape canonica.

## Connessioni con altri principi

- Combina con: P05 (Markdown + Python) — shapes sono espresse in dual schema (md + json)
- Combina con: P08 (Depth Over Breadth) — shape con content minimums forza depth
- Validato da: C3 (target-schema-validator-agent) + scripts/schema_validator.py
- Applicato via: P9 nel framework patterns (Target-Shape Mapping pattern)
