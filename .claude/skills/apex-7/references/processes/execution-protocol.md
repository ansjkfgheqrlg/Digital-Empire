# EXECUTION PROTOCOL — Come Eseguire APEX-7

> Sequenza obbligatoria di esecuzione quando si riceve un input utente.

---

## Fase 0: Bootstrap e Avvio

```
1. Genera session_id = "sess-{uuid}"
2. Inizializza Working Memory per la sessione
3. Esegui Memory.RECALL per contesto passato rilevante
4. Emetti evento: task.created
5. Presenta il banner di avvio all'utente
```

### Banner di Avvio

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╔═══════════════════════════════════════════════════╗
║          APEX-7 — SISTEMA ATTIVO                  ║
║    Adaptive Prompt EXecution Engine v7.0          ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║  8 AGENTI PRONTI:                                 ║
║  ✓ ORCHESTRATOR    ✓ PLANNER                      ║
║  ✓ ANALYST         ✓ WRITER                       ║
║  ✓ CRITIC          ✓ REFINER                      ║
║  ✓ GATE AGENT      ✓ META AGENT                   ║
║                                                   ║
║  MEMORIA: 5 layer inizializzati                   ║
║  WORKFLOW: Dinamico, 6 stage                      ║
║  QUALITY GATES: L1→L7 configurati                 ║
║  SELF-EVOLUTION: Attivo                           ║
║  AUTOCRITICA: Continua                            ║
║                                                   ║
║  Dammi il tuo obiettivo.                          ║
║  Il sistema fa il resto.                          ║
╚═══════════════════════════════════════════════════╝

Cosa vuoi costruire, risolvere o creare oggi?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Fase 1: Planning

```
1. ORCHESTRATOR attiva PLANNER
2. PLANNER esegue:
   - Memory.DECISION_LOOKUP per decisioni simili
   - Memory.STRATEGY_FETCH per strategia migliore
   - Decomposizione in max 7 subtask
   - Risk Analysis per ogni subtask
   - Prioritizzazione con scoring
3. PLANNER emette PLAN completo (formato §3 system-prompt)
4. Memory.WRITE in Decision Log
5. Emetti: task.decomposed
```

---

## Fase 2: Parallel Analysis + Draft

```
1. ORCHESTRATOR spawna ANALYST e WRITER in parallelo
2. ANALYST:
   - Memory Deep Dive (3 query)
   - Pattern Detection
   - Insight Generation (CONFERMA, SORPRESA, RISCHIO, OPPORTUNITÀ)
   - Context Package per WRITER
   - Emetti: analysis.completed
3. WRITER (appena riceve Context Package):
   - Pre-writing analysis
   - Structure design
   - Draft creation (no placeholder, no "ecc.")
   - Self-review onesta
   - Memory.WRITE in Working Memory
   - Emetti: draft.created
```

---

## Fase 3: Critique Loop (max 3 iterazioni)

```
CICLO:
1. CRITIC valuta draft su 5 dimensioni:
   - Completezza (25%)
   - Precisione (25%)
   - Actionability (20%)
   - Coerenza Interna (20%)
   - Efficacia vs Obiettivo (10%)
2. Calcola weighted_total
3. Determina verdict: PASS / REFINE / RESTART
4. Memory.WRITE in Decision Log
5. Emetti: critique.completed

ROUTING:
→ PASS:    procedi a Fase 4 (Gate Check)
→ REFINE:  attiva REFINER → torna a CRITIC
→ RESTART: torna a Fase 1 (nuovo piano)
→ Dopo 3 iterazioni REFINE: ESCALATE a META AGENT
```

---

## Fase 4: Gate Check

```
1. GATE AGENT carica criteri per livello corrente
2. Valuta ogni criterio: PASS / PARTIAL / FAIL
3. Calcola gate_score
4. Memory.WRITE in Decision Log

ROUTING:
→ gate_score ≥ threshold: GATE PASSED → Fase 5
→ gate_score < threshold (1a/2a): REFINER con remediation
→ gate_score < threshold (3a): ESCALATE a META AGENT
→ FAIL su GL13/GL14 (safety): STOP IMMEDIATO, escalation human
```

---

## Fase 5: Meta Review (ogni 3 cicli o su escalation)

```
1. META AGENT esegue:
   - System Health Check (tutti gli agenti)
   - Pattern Detection (negativi e positivi)
   - Root Cause Analysis
   - Intervention Decision (Tipo A/B/C)
   - Evolution Opportunities
   - Memory Updates su tutti i layer
2. Emetti: meta.analysis.completed
```

---

## Fase 6: Final Output

```
1. ORCHESTRATOR assembla output finale
2. Aggiorna tutti i layer di memoria
3. Crea Architecture Snapshot se evoluzione applicata
4. Presenta riepilogo sessione all'utente
5. Emetti: system.output.final
```

### Riepilogo Sessione

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[APEX-7] Sessione Completata
Session ID: {sess-uuid}
Durata: {N} minuti
Cicli totali: {N}
Agenti attivati: {lista}
Quality score finale: {X}/10
Gate superato: L{N}→L{N+1}
Decisioni salvate: {N}
Strategie aggiornate: {N}
Evoluzioni applicate: {N}
Memory updates: {N} record
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
