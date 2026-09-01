# Stage 1: Planning

## Obiettivo
Decomporre il goal utente in un piano eseguibile con subtask, rischi e priorità.

## Agente Responsabile
**PLANNER** (AG-02)

## Input
- Goal utente (da Working Memory)
- Contesto da Memory.RECALL
- Strategie da Memory.STRATEGY_FETCH
- Decisioni passate da Memory.DECISION_LOOKUP

## Processo (5 Step)

### P1 — Comprensione Profonda
- Interpretare il vero obiettivo dell'utente
- Identificare vincoli impliciti
- Definire il "goal reale" in una frase

### P2 — Memory Query
- Cercare richieste simili passate
- Recuperare strategie vincenti
- Identificare anti-pattern da evitare

### P3 — Decomposizione
- Scomporre in max 7 subtask
- Assegnare 1 agente per subtask
- Definire criteri di completamento misurabili
- Identificare dipendenze esplicite
- Marcare subtask parallelizzabili

### P4 — Risk Analysis
- Per ogni subtask: cosa può andare storto?
- Piano B per ogni rischio
- Costo del fallimento

### P5 — Prioritizzazione
- Priority score (1-10)
- Estimated complexity (low/medium/high)
- Estimated time (fast/medium/slow)
- Blocking status

## Output
- PLAN formattato con:
  - GOAL REALE
  - MEMORIA CONSULTATA
  - RISCHI PRINCIPALI
  - Tabella SUBTASK (ID, Descrizione, Agente, Prio, Dipendenze)
  - GRUPPI PARALLELI
  - SEQUENZA CRITICA
  - PIANO B
  - CONFIDENCE

## Post-Actions
1. Memory.WRITE in Decision Log (Layer 2)
2. Emetti evento `task.decomposed`
3. Passa controllo a ORCHESTRATOR

## Criteri di Completamento
- [x] Goal reale interpretato
- [x] Memory consultata (almeno 1 query)
- [x] Subtask decomposti (3-7)
- [x] Risk analysis per ogni subtask
- [x] Prioritizzazione completa
- [x] Confidence score assegnato

## Next Stage
→ Stage 2: Parallel Analysis + Draft
