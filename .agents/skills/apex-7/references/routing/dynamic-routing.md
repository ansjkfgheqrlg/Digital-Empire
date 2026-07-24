# ROUTING RULES — Regole di Routing Dinamico

> Il workflow di APEX-7 non è statico. Queste regole determinano il percorso dell'esecuzione in base ai risultati di ogni stage.

---

## Regola 1: Critique-Based Routing

```
INPUT: Verdict di CRITIC dopo valutazione draft

┌─────────────────────────────────────────────────┐
│ VERDICT = PASS (weighted_total ≥ 8.0)           │
│ → Procedi a STAGE 4 (Gate Check)                │
├─────────────────────────────────────────────────┤
│ VERDICT = REFINE (weighted_total 6.0-7.9)       │
│ → Attiva REFINER con critique completa          │
│ → REFINER produce nuovo draft                   │
│ → Torna a CRITIC per rivalutazione              │
│ → Max 3 iterazioni totali                       │
├─────────────────────────────────────────────────┤
│ VERDICT = RESTART (weighted_total < 6.0)        │
│ → Torna a STAGE 1 (nuovo piano da PLANNER)      │
│ → Passa contesto del fallimento a PLANNER       │
├─────────────────────────────────────────────────┤
│ VERDICT = REFINE ma ci sono BLOCCANTI           │
│ → REFINE è il minimo, anche se score ≥ 8.0     │
└─────────────────────────────────────────────────┘
```

---

## Regola 2: Gate-Based Routing

```
INPUT: Gate Report da GATE AGENT

┌─────────────────────────────────────────────────┐
│ GATE PASSED (gate_score ≥ threshold)            │
│ → Procedi a STAGE 5 (Meta Review) o STAGE 6     │
├─────────────────────────────────────────────────┤
│ GATE FAILED — tentativo 1 o 2                    │
│ → Invia remediation list a REFINER              │
│ → REFINER applica fix specifici                 │
│ → Torna a GATE AGENT per nuovo check            │
├─────────────────────────────────────────────────┤
│ GATE FAILED — tentativo 3                        │
│ → ESCALATE a META AGENT                         │
│ → META AGENT decide: micro/macro/human           │
├─────────────────────────────────────────────────┤
│ GATE FAILED su GL13 o GL14 (Safety)             │
│ → STOP IMMEDIATO                                │
│ → Escalation a HUMAN OBBLIGATORIA               │
│ → Nessun automatismo possibile                  │
└─────────────────────────────────────────────────┘
```

---

## Regola 3: Meta Activation Triggers

```
META AGENT si attiva quando:

┌─────────────────────────────────────────────────┐
│ 1. ROUTINE: Ogni 3 cicli completi               │
│ 2. CRITICAL: Gate fallito 3 volte consecutive   │
│ 3. CRITICAL: CRITIC ha dato RESTART             │
│ 4. CRITICAL: REFINER non risolve dopo 3 cicli   │
│ 5. CRITICAL: Agente timeout 2x il normale       │
│ 6. MANUAL: ORCHESTRATOR richiede esplicitamente │
└─────────────────────────────────────────────────┘
```

---

## Regola 4: Escalation Conditions

```
┌─────────────────────────────────────────────────┐
│ CONDIZIONE                  │ AZIONE            │
├─────────────────────────────┼───────────────────┤
│ CRITIC score < 6.0 × 2      │ META immediato    │
│ GATE fail × 3               │ META AGENT        │
│ REFINER fail × 3            │ META AGENT        │
│ Safety gate fail (GL13/14)  │ HUMAN immediato   │
│ Agente DEGRADED             │ META decide       │
│ Evento P0 non risolto 60s   │ HUMAN + rollback  │
│ Quality drop > 10% (5 run)  │ ROLLBACK auto     │
└─────────────────────────────┴───────────────────┘
```

---

## Regola 5: Human Override Protocol

```
L'utente può interrompere in qualsiasi momento con:
"stop", "pausa", "cambia", "aspetta", "ferma"

AZIONE:
1. ORCHESTRATOR salva stato corrente in Working Memory
2. Tutti gli agenti attivi vengono messi in pausa
3. Event Bus smista evento "human.override"
4. ORCHESTRATOR comunica: "Sistema in pausa. In attesa di tue istruzioni."

L'utente può:
- "continua" → riprendi dal checkpoint
- "cambia X" → modifica parametro e riprendi
- "ricomincia da Y" → rollback a stage specifico
- "basta così" → output corrente come finale
```

---

## Regola 6: Parallel vs Sequential Decision

```
DECISIONE: Un subtask può essere parallelizzato?

CHECK:
1. Il subtask ha dipendenze da altri subtask non completati?
   → NO: candidato per parallelizzazione
   → SÌ: sequenziale

2. Il subtask condivide risorse (Working Memory) con conflitti?
   → NO: OK per parallel
   → SÌ: sequenziale o lock

3. Due agenti possono lavorare su dati indipendenti?
   → SÌ: parallel (es. ANALYST + WRITER su fonti diverse)
   → NO: sequenziale

DEFAULT: ANALYST e WRITER in parallelo (Stage 2)
         Tutto il resto sequenziale
```
