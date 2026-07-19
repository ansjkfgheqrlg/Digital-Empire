# P07 — Three-Level Architecture

> **Definizione canonica**: Una skill complessa è organizzata in 3 livelli con responsabilità nettamente separate: **L1 Kernel/Conductor** (entry point, routing, dialogo con l'utente), **L2 Specialists** (subagenti spawnati con scope ristretto), **L3 Tools** (script Python deterministici). I livelli non si confondono: ognuno fa quello che fa meglio.

## Perché funziona

### 1. Ogni livello sfrutta le sue caratteristiche
- **L1 Conductor** (LLM "principale", quello dell'utente): ha contesto pieno della conversazione, sa parlare con l'utente, mantiene state. Bravo a coordinare, debole su task specializzati lunghi.
- **L2 Specialists** (subagenti): ognuno è un LLM con scope ristretto, system prompt mirato, zero distrazioni. Bravo su task complessi singoli, debole su coordinamento.
- **L3 Tools** (Python): deterministici, veloci, gratis (no token), riproducibili. Bravi su operazioni meccaniche, incapaci di giudizio semantico.

Mescolare i livelli = inefficienza. LLM che fanno regex (overkill), Python che fa giudizi (impossibile).

### 2. Modularità e debugging
Se qualcosa va male, sai dove guardare:
- Conductor confonde routing → guarda SKILL.md
- Output di un agente specifico fa schifo → guarda quell'agente
- Validator sbaglia → guarda lo script
- I 3 livelli sono ortogonali: bug in uno non contamina gli altri (di solito).

### 3. Scaling indipendente
Vuoi aggiungere un nuovo target (es. `team`)? Aggiungi un agente B3 in L2 + uno script di validation in L3. Il Conductor (L1) resta invariato (solo nuova entry nella routing table).

Senza 3-level, ogni cambiamento richiederebbe rimaneggiare tutto.

## Come applicarlo (operativo)

### Mappa responsabilità per livello

| Livello | Chi è | Cosa fa | Cosa NON fa |
|---|---|---|---|
| **L1 Conductor** | Istanza LLM che ha chiamato la skill | Routing, dialogo utente, mantiene state, spawna agenti via Task tool | Non esegue lavoro cognitivo specializzato lungo. Non gira regex/parse. |
| **L2 Specialists** | Subagenti spawnati via Task tool | Un task specializzato bene definito (es. estrai atomi, genera SP, valida schema) | Non parla all'utente. Non spawna altri agenti (di norma). |
| **L3 Tools** | Script Python eseguiti via Bash tool | Operazioni deterministiche: parse, validate, transform, package | Non fa giudizi semantici. Non interpreta linguaggio naturale. |

### Pattern di interazione

```
USER input
   ↓
L1 Conductor riceve, capisce intent
   ↓
L1 spawn L2 specialist via Task tool
   │
   ├─ L2 specialist riceve task con istruzioni esplicite
   │    │
   │    ├─ L2 può chiamare L3 tools (script Python via Bash)
   │    │    es. python3 scripts/validate_schema.py --target agent ...
   │    │
   │    └─ L2 produce output (file su disk + return JSON)
   │
   └─ L1 riceve output L2, decide next step
   ↓
L1 risponde all'utente o spawna next L2
```

### Dove vivono i livelli (filesystem)

```
content-forge/
├── SKILL.md                  ← L1 (kernel)
├── agents/                   ← L2
│   ├── conductor.md          ← SP per L1 stesso quando agisce come orchestrator
│   ├── pipeline/            ← A1-A5
│   ├── builders/            ← B1-B8
│   ├── qa/                  ← C1, C3
│   ├── optimizers/          ← O1-O5
│   ├── meta/                ← D1
│   └── self-improvement/    ← SI1-SI3
├── references/               ← L1+L2 reading material (on-demand)
└── scripts/                  ← L3 tools
    ├── *.py                  ← script principali
    ├── lib/                  ← moduli condivisi
    └── tests/                ← pytest
```

### Regole di confine

**Mai violare:**
- L1 NON spawna altri Conductor (no nested orchestration)
- L2 NON parla all'utente direttamente (sempre via L1)
- L3 NON contatta LLM (è puro Python deterministico)
- L2 NON modifica state.json del Conductor (solo L1)
- L1 NON esegue regex elaborate o parsing manuale (usa L3)

## Esempi

### Esempio 1 — content-forge (nostro caso)

Run completo `/forge transcript.md --target=skill`:

| Step | Livello | Componente | Cosa fa |
|---|---|---|---|
| 1 | L1 | Conductor | Legge SKILL.md, capisce intent skill, crea workspace |
| 2 | L1 → L2 | spawn A1 ingestion | Pulizia sorgente |
| 3 | L2 → L3 | A1 chiama scripts/transcript_cleaner.py | Regex deterministiche |
| 4 | L2 → L1 | A1 ritorna stats | Conductor riceve report |
| 5 | L1 → L2 (xN) | spawn A2 analyst in parallelo | Estrazione atomi |
| 6 | L1 → L2 | spawn A3 KG agent | Assembla grafo |
| 7 | L1 → L2 | spawn A5 MKD builder | Produce documento ampliato |
| 8 | L1 ↔ user | Conductor chiede target choice (se non noto) | ASK phase |
| 9 | L1 → L2 | spawn D1 question-designer | Genera ASK domande |
| 10 | L1 ↔ user | Conductor porge domande | Raccoglie answers |
| 11 | L1 → L2 | spawn B4 skill-builder | Costruisce skill |
| 12 | L1 → L2 (xN) | spawn O1-O5 optimizer team | Depth pass |
| 13 | L1 → L2 (x2) | spawn C1+C3 in parallelo | QA |
| 14 | L1 → L3 | scripts/package_target.py | Packaging |
| 15 | L1 → user | "ecco il tuo deliverable" | Response finale |

**Conductor è SEMPRE il caller di L2 e L3. L2 può chiamare L3 ma mai L1 direttamente. L3 non chiama nulla.**

### Esempio 2 — Errore evitato

Se mettessi la logica di "validate schema" in un agente (L2) invece che in script (L3):
- Costo: 5-10x tokens per ogni validation
- Latency: 10-30s vs <100ms
- Non-determinismo: lo stesso input può ritornare risultati leggermente diversi
- Difficoltà debug: errori nel "ragionamento" del LLM vs errori in Python (deterministic)

P07 evita questo: validation è L3 (script_validator.py), agente C3 è solo wrapper LLM che orchestra + spiega risultati.

### Esempio 3 — ➕ Pattern simile in software engineering

**Hexagonal Architecture / Ports and Adapters** (Alistair Cockburn):
- Core business logic (analogo L2 specialists — domain experts)
- Application services (analogo L1 conductor — orchestration)
- Adapters (analogo L3 tools — external I/O)

Stessa filosofia: ogni livello fa ciò che fa meglio, confini netti.

Altri: **Clean Architecture** (Robert C. Martin), **Onion Architecture** (Jeffrey Palermo). Tutti convergono sullo stesso pattern.

## Anti-pattern correlato

**AP03 — User-Driven Overhead**: il sistema chiede all'utente di fare task che dovrebbero essere automatici (es. eseguire script Python manualmente). Sintomo: utente segue una "to-do list" di comandi. **Fix**: aggiungi agenti L2 + script L3 che fanno tutto automatico.

(Questo era esattamente il bug della v1.1 di content-forge: avevo costruito sistema log_failure.py user-CLI invece di agenti SI che lo chiamano. Phase 9 → v1.2 fix.)

**Anti-pattern duale**: **God-Conductor** — Conductor che fa tutto da solo invece di spawn. Sintomo: SKILL.md gigante, niente agenti specializzati, niente script. Risultato: lento, costoso, non manutenibile.

## Decision tree: "questo task in quale livello va?"

```
Il task richiede dialogo con l'utente?
├─ SÌ → L1 (Conductor)
└─ NO → continua
   ├─ Il task è un giudizio semantico / generation creativa / decisione complessa?
   │  ├─ SÌ → L2 (agente specializzato)
   │  └─ NO → continua
   │
   ├─ Il task è regola deterministica, parse, validate, transform meccanico?
   │  ├─ SÌ → L3 (script Python)
   │  └─ NO → continua
   │
   └─ Il task è ibrido (parte L2, parte L3)?
      → L2 agent che chiama L3 script (pattern comune)
      Es: coverage-verifier-agent (L2) chiama coverage_check.py (L3)
```

## Quando NON applicare

- **Skill molto piccole** (1-2 agenti): three-level è overkill, può vivere tutto in SKILL.md + scripts/ minimi.
- **Skill puramente generative** senza validation strutturata: forse non serve L3.
- **Skill solo orchestrazione** (target=orchestration di componenti esterni): L2 e L3 sono nei componenti esterni, la tua skill è solo L1.

## Riferimenti esterni

- **Alistair Cockburn**, *Hexagonal Architecture* (2005) — Ports and Adapters.
- **Robert C. Martin**, *Clean Architecture* (2017) — Dependency Rule, layered architecture.
- **Eric Evans**, *Domain-Driven Design* — Bounded Contexts come analogia di L2 specialists.
- **Anthropic skill-creator** — Implementa P07 explicitly: kernel + agents/ + scripts/.
- **Microservices architecture** — pattern simile: API gateway (L1) + microservices (L2) + databases/queues (L3).

## Connessioni con altri principi

- Necessario per: P02 (Progressive Disclosure) — i livelli sono i "level" di disclosure
- Combina con: P05 (Markdown + Python) — la decisione "md vs py" è correlata a "L2 vs L3"
- Si appoggia a: P06 (Shapes) — ogni livello ha sue shape canoniche
- Validato implicitamente da: pytest che testa solo L3, agent eval che testa solo L2
