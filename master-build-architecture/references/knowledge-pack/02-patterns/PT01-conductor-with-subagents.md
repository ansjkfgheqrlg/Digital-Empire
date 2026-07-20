# PT01 — Conductor with Subagents

> **Shape canonica**: Un'istanza LLM principale (Conductor = il caller della skill) coordina N subagenti specializzati spawnati via Task tool. Il Conductor non fa lavoro cognitivo specializzato lungo: routing, dialogo utente, mantenimento stato. I subagenti hanno scope ristretto, system prompt mirato, lifecycle indipendente.

## Quando applicarlo

✅ **Applica sempre se**:
- La skill ha ≥3 task cognitivi distinti (estrarre, analizzare, generare, validare)
- Ogni task beneficerebbe di system prompt dedicato (>500 parole specifiche)
- I task sono parallelizzabili almeno parzialmente

❌ **NON applicare se**:
- Skill mono-purpose con 1 task chiaro
- Latency-critical (<5 secondi end-to-end): overhead spawn troppo alto
- Sub-task <50 parole di logica: meglio inline nel kernel

## Perché funziona

Tre meccanismi:

### 1. Scope isolation = quality boost
Un agente con SP focused su "estrarre atomi" è meglio di un Conductor multitasking. Anthropic raccomanda esplicitamente: focused agents > general purpose.

### 2. Parallelism quando possibile
Conductor spawna N agenti in parallelo nello stesso turno. Es. A2 analyst-agent spawnato xN per chunk diversi → 4x speedup su sorgenti grandi.

### 3. Debug & evolution
Bug isolato a un agente specifico. Fix lì, gli altri non toccati. Senza Conductor pattern, ogni cambio impatta il monolite.

## Esempio dal nostro percorso

`content-forge` ha esattamente questa shape:

```
L1 Conductor (caller LLM, ha SKILL.md + state)
   │
   ├─► A1 ingestion-agent       (Stage 1)
   ├─► A2 analyst-agent (×N)    (Stage 2, parallel)
   ├─► A3 knowledge-graph-agent (Stage 3)
   ├─► A5 mkd-builder-agent     (Stage 4)
   ├─► A4 target-advisor-agent  (Stage 5)
   ├─► D1 question-designer     (Stage 6 ASK)
   ├─► Bx target-builder        (Stage 6 BUILD)
   ├─► O1-O5 optimizer team     (Stage 7, partially parallel)
   ├─► C1+C3 in parallelo       (Stage 8 QA)
   └─► SI1+SI2+SI3              (Stage 10, conditional)
```

Conductor (te, l'LLM principale) decide quale spawn quando, mantiene `state.json`, parla con l'utente. **Non fa mai lavoro cognitivo specializzato**.

## ➕ Esempio in altri domini

**Microservices architecture**: API Gateway = Conductor; ogni microservice = subagente. Stesso pattern strutturale.

**Orchestrator-Worker** in distributed systems (Airflow, Temporal, Celery): orchestrator decides + workers execute.

**Pair programming + tools**: senior dev = Conductor, junior + linter + test runner = subagenti.

## Anti-pattern correlato

**God-Conductor**: Conductor che fa tutto da solo senza spawnare. Sintomo: SKILL.md gigante, zero subagenti, tutto in 1 SP da 5000 parole.

**Anti-pattern duale**: **Spawn fatigue** — spawn agenti per ogni cosa banale (es. agente per uppercase string). Overhead Token > beneficio. Soglia: spawn solo se task >100 parole di logica.

## Trade-off

| Pro | Contro |
|---|---|
| Modularity, debug isolato | Overhead spawn (token + latency) |
| Parallelism possibile | Coordination state complexity |
| Specialist quality > general | Più file da mantenere |
| Sviluppo indipendente per agente | Curva apprendimento iniziale |

## Decision tree

```
Hai ≥3 task cognitivi distinti?
├─ NO → mono-agent design, no Conductor pattern
└─ SÌ → continua
   ├─ Almeno 1 task è parallelizzabile su istanze?
   │  ├─ NO → considera comunque per scope isolation
   │  └─ SÌ → strong fit per Conductor pattern
   ├─ Hai bandwidth per mantenere N agent files?
   │  ├─ NO → meno agenti (forse merge alcuni)
   │  └─ SÌ → procedi
   │
   └─ Implementa:
      1. Conductor SP minimo (routing only)
      2. Per ogni task → agente in agents/<family>/<name>-agent.md
      3. State.json schema per coordinamento
      4. Task tool spawn pattern (parallel quando possibile)
```

## Connessioni

- Necessario per: P07 (Three-Level Architecture)
- Combina con: PT02 (Pipeline Stages with Handoff)
- Combina con: PT04 (Question Designer Pattern)
- Vedi anche: Anthropic docs "Subagents via Task tool"

## Riferimenti

- Anthropic Claude docs — Task tool & subagents
- Microservices patterns (Chris Richardson)
- Actor model (Carl Hewitt 1973)
