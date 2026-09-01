# PT07 — Silent Observer Agents

> **Shape canonica**: Agenti che girano **dopo** il lavoro principale, **osservano** lo stato del sistema, **scrivono artifact in background** senza notificare l'utente. L'utente accede a quanto raccolto **solo se chiede esplicitamente**. Stage opzionale e condizionale. **Mai mid-run interrupt**.

## Quando applicarlo

✅ **Applica se**:
- Vuoi continuous improvement loop
- Bug e feedback emergono in produzione, non in test
- L'utente è "power user" che vuole controllo (non micro-management)

❌ **NON applicare se**:
- Skill one-shot (nessuna improvement da osservare)
- L'utente vuole notifiche push esplicite ("dimmi sempre cosa fai")
- Pipeline già ben validata, no failure mode aperti

## Perché funziona

### 1. Il valore degli observer è proporzionale al loro silenzio
Observer che notificano "ho trovato un FM!" diventano spam. Observer che lasciano file e exit silenziosi accumulano valore senza costo di attention.

### 2. User pull > system push
Pattern ricorrente in tool maturi (git, sentry, ecc.): il sistema osserva e accumula. L'utente legge "git log" quando vuole, "sentry dashboard" quando vuole.

Notification spam = soluzione facile ma rotta. Silent observer = soluzione difficile ma sostenibile.

### 3. Background work scopre cosa l'utente "non sa di non sapere"
L'utente nota problemi vistosi. Gli observer notano pattern: "questo bug ricorre in 5 categorie diverse" — insight che l'utente da solo non collegherebbe.

## Esempio dal nostro percorso

content-forge Stage 10 — Self-Improvement Loop:

```
Pipeline normale (Stage 1-9) finisce con artifact consegnato all'utente
       ↓
Stage 10 (silent observer team):

   SI1 failure-detector-agent
     - Triggered: se QA verdict FAIL/WARN o feedback utente negativo
     - Output: scrive FM in failure-modes-log/logged/
     - Silent: nessun messaggio all'utente

   SI2 triage-agent
     - Triggered: se count(logged/) ≥ 3
     - Output: classifica (severity/category/scope) sposta in triaged/
     - Silent: nessun messaggio

   SI3 phase-planner-agent
     - Triggered: se soglie raggiunte (≥3 major, etc.)
     - Output: genera PHASE-N-CANDIDATES.md
     - Silent: nessuna notifica
```

L'utente continua a usare normalmente. Mesi dopo:

> "Forge, cosa hai trovato di problematico?"
> Conductor: legge failure-modes-log/, risponde con riepilogo.

> "Forge, hai un plan per la prossima phase?"
> Conductor: controlla se esiste PHASE-N-CANDIDATES.md, mostra.

## Le 4 regole del Silent Observer Pattern

### Regola 1 — Trigger conditional, no run sempre
Observer girano solo se condizione vera. Run smooth = observer NON girano. Overhead zero.

```python
# Esempio: SI1 trigger condition
def should_spawn_si1(run_state):
    return (
        run_state.qa_verdict in ("FAIL", "WARN")
        or has_negative_user_feedback(run_state)
        or has_optimizer_warnings(run_state)
    )
```

### Regola 2 — Output strutturati con index navigabile
Observer producono file con naming consistente + INDEX.md auto-rigenerato. L'utente che esplora trova subito.

```
failure-modes-log/
├── INDEX.md       ← rigenerato a ogni run
├── logged/FM-001-*.md
├── triaged/FM-002-*.md
└── PHASE-10-CANDIDATES.md
```

### Regola 3 — Conductor NEVER mention observers spontaneamente
Hard rule nel SP del Conductor:
> "Stage 10 observer agents work silently. NEVER mention their output unless the user explicitly asks 'cosa hai trovato' or similar query."

Senza questa rule, Conductor tende a dire "Ho anche eseguito Stage 10 e..." → notification creep.

### Regola 4 — On-demand response = rich
Quando l'utente chiede, risposta dettagliata. Pattern:

```
User: "Forge, cosa hai trovato di problematico?"
Conductor:
  - legge failure-modes-log/INDEX.md
  - conta logged/triaged/resolved
  - se esiste PHASE-N-CANDIDATES.md, summarize
  - risposta strutturata con counts + breakdown + suggerimenti

User: "Forge, dimmi i triaged"
Conductor:
  - legge tutti i triaged/FM-*.md
  - raggruppa per category
  - mostra severity + summary di ognuno
```

Silent default + rich on request = combo che funziona.

## ➕ Esempio in altri domini

**Sentry / Bugsnag**: error tracking silent. Notifica solo prima occorrenza + threshold breach. Tutto resto: dashboard on-demand.

**Git reflog**: registra ogni HEAD change silently. Recovery utile (recupera commit "perso") ma nessuno lo guarda routinely.

**OS file system journaling**: registra ogni operazione filesystem per recovery. Silent. Usato solo on crash recovery.

**Telemetry in IDEs** (VS Code, JetBrains): raccoglie pattern di uso silent. Mai notifica all'utente. Used internally per improve product.

## Anti-pattern correlato

**AP03 — User-Driven Overhead**: l'opposto di silent observer. Richiede azione utente.

**Anti-pattern duale**: **Notification spam** — observer che si fanno sentire. Distrugge il valore.

**Edge anti-pattern**: **Silent for critical issues** — observer silenziosi anche su failure bloccanti. Se SI1 detect un blocker che impedisce skill di funzionare, deve notificare. Distingui: silent su observation, notify su action-required.

## Trade-off

| Pro | Contro |
|---|---|
| Attention budget rispettato | User non sa che observer girano |
| Continuous improvement automatico | Insight inutilizzati se user non chiede mai |
| Pattern detection a lungo termine | Implementation complessa (3+ agenti) |
| Memoria istituzionale dei bug | Storage cresce nel tempo |

## Decision tree

```
Vuoi loop di continuous improvement?
├─ NO → no observer pattern
└─ SÌ → continua
   ├─ Sei disposto a non vedere risultati finché non chiedi?
   │  ├─ NO → notification-based design invece
   │  └─ SÌ → silent observer pattern
   │
   ├─ Hai chiarezza su cosa observer dovrebbe catturare?
   │  ├─ NO → prima clarify (cosa è "bug" / "FM")
   │  └─ SÌ → procedi
   │
   └─ Implementa:
      1. Stage dedicato (es. Stage 10) post-pipeline
      2. Trigger conditions chiare (no run sempre)
      3. Output strutturato + INDEX.md auto-rigen
      4. Conductor "NEVER mention" rule hardcoded
      5. Pattern di response on-demand
      6. Tool JSON per orchestrazione (no user-CLI)
```

## Connessioni

- Implementa: P10 (Self-Improvement Loops)
- Combina con: P14 (Silent Operation by Default)
- Si oppone a: AP03 (User-Driven Overhead)
- Esempio reale: Stage 10 SI agents di content-forge

## Riferimenti

- Sentry / Bugsnag silent error tracking model
- Git reflog as silent ledger
- OS journaling filesystems
- Telemetry collection in IDEs
- Observer pattern in software design (Gang of Four)
