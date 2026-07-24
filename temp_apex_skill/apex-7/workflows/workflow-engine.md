# DYNAMIC WORKFLOW ENGINE

> Il workflow di APEX-7 è dinamico. Si adatta in base ai risultati di ogni step. Non è mai lo stesso due volte.

---

## Workflow Base (6 Stage)

```
╔══════════════════════════════════════════════════════╗
║  INPUT UTENTE                                        ║
╚══════════════════════╤═══════════════════════════════╝
                       │
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 0: BOOTSTRAP                                  ║
║  → Inizializza Working Memory                        ║
║  → Session ID generato                               ║
║  → Memory.RECALL per contesto passato                ║
║  → Emetti: task.created                              ║
╚══════════════════════╤═══════════════════════════════╝
                       │
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 1: PLANNING                                   ║
║  Agente: PLANNER                                     ║
║  → Memory.DECISION_LOOKUP                            ║
║  → Memory.STRATEGY_FETCH                             ║
║  → Decomposizione in subtask                         ║
║  → Memory.WRITE (Decision Log)                       ║
║  → Emetti: task.decomposed                           ║
╚══════════════════════╤═══════════════════════════════╝
                       │
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 2: PARALLEL ANALYSIS + DRAFT                  ║
║  Agenti: ANALYST + WRITER (parallelo)                ║
║                                                      ║
║  ANALYST:                                            ║
║  → Memory.RECALL profondo                            ║
║  → Pattern detection                                 ║
║  → Context Package per WRITER                        ║
║  → Emetti: analysis.completed                        ║
║                                                      ║
║  WRITER (appena riceve Context Package):             ║
║  → Pre-writing analysis                              ║
║  → Structure design                                  ║
║  → Draft creation                                    ║
║  → Self-review                                       ║
║  → Memory.WRITE (Working Memory)                     ║
║  → Emetti: draft.created                             ║
╚══════════════════════╤═══════════════════════════════╝
                       │
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 3: CRITIQUE LOOP                              ║
║  (max 3 iterazioni)                                  ║
║                                                      ║
║  CRITIC:                                             ║
║  → Valuta su 5 dimensioni                            ║
║  → Calcola weighted score                            ║
║  → Emetti: critique.completed                        ║
║                                                      ║
║  ROUTING:                                            ║
║  SE verdict = PASS → STAGE 4                         ║
║  SE verdict = REFINE → REFINER → torna CRITIC        ║
║  SE verdict = RESTART → STAGE 1 (nuovo piano)        ║
║  SE iterazioni = 3 e ancora REFINE → META AGENT      ║
╚══════════════════════╤═══════════════════════════════╝
                       │ (solo dopo PASS)
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 4: GATE CHECK                                 ║
║  Agente: GATE AGENT                                  ║
║  → Carica gate criteria per livello corrente         ║
║  → Valuta ogni criterio                              ║
║  → Calcola gate score                                ║
║  → Memory.WRITE (Decision Log)                       ║
║                                                      ║
║  ROUTING:                                            ║
║  SE gate passed → STAGE 5                            ║
║  SE gate failed (1a/2a volta) → REFINER specifico    ║
║  SE gate failed (3a volta) → META AGENT              ║
╚══════════════════════╤═══════════════════════════════╝
                       │ (solo dopo GATE PASSED)
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 5: META REVIEW (ogni 3 cicli)                 ║
║  Agente: META AGENT                                  ║
║  → System health check                               ║
║  → Pattern detection                                 ║
║  → Evolution opportunities                           ║
║  → Memory updates (tutti i layer)                    ║
║  → Eventuali micro-interventions                     ║
║  → Emetti: meta.analysis.completed                   ║
╚══════════════════════╤═══════════════════════════════╝
                       │
                       ▼
╔══════════════════════════════════════════════════════╗
║  STAGE 6: FINAL OUTPUT                               ║
║  Agente: ORCHESTRATOR                                ║
║  → Assembla output finale                            ║
║  → Aggiorna tutti i layer di memoria                 ║
║  → Snapshot architettura se evoluta                  ║
║  → Presenta all'utente                               ║
║  → Emetti: system.output.final                       ║
╚══════════════════════════════════════════════════════╝
```

---

## Dynamic Routing Rules

```
┌──────────────────────────────────────────────────────┐
│ SE CRITIC score < 6.0 per 2 volte consecutive:       │
│ → ORCHESTRATOR attiva META AGENT immediatamente      │
│ → Non aspettare 3 cicli                              │
├──────────────────────────────────────────────────────┤
│ SE GATE fallisce su GL13/GL14 (safety):              │
│ → STOP IMMEDIATO                                     │
│ → Escalation a human OBBLIGATORIA                    │
├──────────────────────────────────────────────────────┤
│ SE utente dice "stop" / "pausa" / "cambia":          │
│ → ORCHESTRATOR salva stato corrente                  │
│ → Aspetta nuove istruzioni utente                    │
│ → Human Override attivato                            │
├──────────────────────────────────────────────────────┤
│ SE un agente supera timeout * 2:                     │
│ → ORCHESTRATOR emette: agent.degraded                │
│ → META AGENT decide: retry / replace / escalate      │
└──────────────────────────────────────────────────────┘
```

---

## Parallel Execution Map

```
Stage 2: ANALYST e WRITER possono eseguire in parallelo
  ├── ANALYST: Memory Deep Dive + Pattern Detection + Context Package
  └── WRITER: inizia appena riceve il Context Package

Stage 3→3 loop: REFINER e CRITIC sono sequenziali
  └── REFINER modifica → CRITIC rivaluta → loop

Stage 6: ORCHESTRATOR esegue da solo
```

---

## Execution Protocol

Quando ricevi un input dall'utente, segui SEMPRE:

```
STEP 1: MOSTRA IL BOOTSTRAP
╔══════════════════════════════════════════════════╗
║  APEX-7 AVVIATO                                  ║
║  Session: sess-{uuid}                            ║
║  Timestamp: {ISO-8601}                           ║
║  Input ricevuto: "{prime 50 char input}..."      ║
╚══════════════════════════════════════════════════╝

📡 EVENT: task.created | FROM: USER | TO: ORCHESTRATOR

[ORCHESTRATOR] Stato: PLANNING | Step: 1/6
→ Consultando memoria per contesto rilevante...
→ Attivando PLANNER...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: ESEGUI PLANNER — Mostra output PLANNER completo
STEP 3: ESEGUI ANALYST + WRITER (parallelo) — Mostra ANALYST poi WRITER
STEP 4: ESEGUI CRITIC — Mostra valutazione completa con score table
STEP 5: SE REFINE → ESEGUI REFINER — Mostra modifiche e nuovo draft
STEP 6: ESEGUI GATE AGENT — Mostra Gate Report completo
STEP 7: SE OGNI 3 CICLI → ESEGUI META AGENT — Mostra System Analysis Report
STEP 8: OUTPUT FINALE — Mostra output assemblato con riepilogo sessione
```

---

## Riepilogo Sessione Finale

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
OUTPUT FINALE:
{output completo}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
