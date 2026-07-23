# 🏛️ DIGITAL EMPIRE — APEX System v2.0
## Adaptive Prompt EXecution Engine

> **Versione pragmatica** ispirata ai pattern di [RuFLO](https://github.com/ruvnet/ruflo) (swarm, memory, workflow) adattata per Arena.ai.

---

## Cos'è

Un ecosistema operativo per un'agenzia AI che produce:
1. **Skill Forge** → File `SKILL.md` eseguibili da agenti AI
2. **Carousel Engine** → Slide Instagram in stile glassmorphism premium
3. **Cold Outreach Machine** → Sequenze email B2B con framework APSOC

Ogni output passa attraverso un **quality gate** (score ≥ 7.5/10) e viene **salvato in memoria** per apprendere dalle iterazioni passate.

---

## Architettura

```
┌─────────────────────────────────────────────────────────┐
│                   META-ORCHESTRATOR                      │
│           (orchestrator.py + workflow JSON)              │
│                                                         │
│  Input → Decompose → Route → Execute → Critique → Loop │
└─────────────────────┬───────────────────────────────────┘
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │ PLANNER  │ │  WRITER  │ │ ANALYST  │
   │ Decompose│ │ Generate │ │ Research │
   │ & Route  │ │ Content  │ │ & Map    │
   └──────────┘ └──────────┘ └──────────┘
                      │
              ┌───────┴───────┐
              ▼               ▼
        ┌──────────┐   ┌──────────┐
        │  CRITIC  │──▶│ REFINER  │
        │ Score &  │   │ Improve  │
        │ Gate     │   │ & Polish │
        └──────────┘   └──────────┘
              │
              ▼ (score ≥ 7.5)
        ┌──────────┐
        │  OUTPUT  │
        │ + Memory │
        │   Save   │
        └──────────┘

═══════════════════════════════════════════════════════════
              💾 MEMORY ECOSYSTEM (5 layers)
═══════════════════════════════════════════════════════════

  Layer 1: ⚡ Working Memory    → Session context, variables
  Layer 2: 📝 Decision Log      → Every choice + why + alternatives
  Layer 3: 🎯 Strategy Store    → Winning patterns + usage tracking
  Layer 4: 🏗️ Arch. Snapshots  → System versions + diffs
  Layer 5: 🧬 Knowledge Base    → Lessons, best practices, anti-patterns
```

---

## Struttura File

```
digital-empire/
├── config/
│   └── system.json           # Configurazione globale
├── memory/
│   ├── working/context.json  # Sessione corrente
│   ├── decisions/log.json    # Log decisioni
│   ├── strategies/store.json # Pattern vincenti
│   ├── architecture/snapshots.json # Versioni sistema
│   └── knowledge/base.json   # Conoscenza compressa
├── prompts/
│   ├── skill-forge-v2.md     # Prompt Skill Forge
│   ├── carousel-engine-v2.md # Prompt Carousel Engine
│   └── cold-outreach-v2.md   # Prompt Cold Outreach
├── workflows/
│   ├── skill-forge-workflow.json
│   ├── carousel-workflow.json
│   └── cold-outreach-workflow.json
├── orchestrator.py           # CLI orchestrator
├── skills/                   # Output SKILL.md generati
├── output/                   # Output finali (carousel, email, ecc.)
└── ARCHITECTURE.md           # Questo file
```

---

## Come Usare

### 1. Vedere lo stato del sistema
```bash
python3 orchestrator.py status
```

### 2. Leggere la memoria
```bash
python3 orchestrator.py memory decisions
python3 orchestrator.py memory strategies
python3 orchestrator.py memory knowledge
```

### 3. Eseguire un workflow (descrizione)
```bash
python3 orchestrator.py workflow skill-forge
python3 orchestrator.py workflow carousel-engine
python3 orchestrator.py workflow cold-outreach
```

### 4. Registrare una decisione
```bash
python3 orchestrator.py decision "Scelta X" "Motivo Y"
```

### 5. Vedere le policy attive
```bash
python3 orchestrator.py policies
```

### 6. Usare i Prompt (in Arena.ai)
Copia il contenuto di ciascun file in `prompts/` e incollalo in Arena.ai come prompt. Ogni prompt è **auto-contenuto** e include:
- Istruzioni per l'agente
- Formato output obbligatorio
- Criteri di qualità (per il Critic Agent)
- Placeholder chiaramente identificabili

---

## Quality Gate

Ogni output passa attraverso 5 dimensioni di scoring:

| Dimensione | Peso | Threshold Min |
|---|---|---|
| Completezza | 25% | 8/10 |
| Precisione | 25% | 8/10 |
| Creatività | 20% | 7/10 |
| Actionability | 20% | 8/10 |
| Coerenza | 10% | 9/10 |

**Score totale ≥ 7.5** → Output approvato
**Score 4.0 - 7.4** → Refinement (max 3 loop)
**Score < 4.0** → Restart con strategia diversa

---

## Policy Attive

1. **Quality Gate**: Nessun output senza score ≥ 7.5/10
2. **Memory Write-Through**: Ogni decisione salvata con contesto
3. **Pragmatism First**: Se non è eseguibile in Arena.ai, non fa parte del sistema

---

## Differenze vs Planning "7 Livelli" Originale

| Concetto | Planning v1 (Teorico) | Sistema v2 (Pragmatico) |
|---|---|---|
| Memory | 7 layer concettuali | 5 layer implementati in JSON |
| Swarm | Multi-swarm autonomo | 6 agent roles orchestrati |
| Workflow | Dynamic self-routing | Workflow JSON con routing condizionale |
| Learning | Self-evolving | Policy + strategy tracking + anti-patterns |
| Execution | RuFLO full stack | Python orchestrator + prompt templates |
| Quality | Score generico | 5-dimension matrix con threshold |

---

*Generato da Digital Empire APEX v2.0 — 2026-07-23*
