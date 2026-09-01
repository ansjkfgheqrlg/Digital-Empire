# Stage 10 — Self-Improvement Observe

> 🆕 Stage **silenzioso e condizionale** introdotto dopo Phase 9.
> Implementa il **continuous improvement loop** in modo completamente automatico.
> **L'utente non interagisce mai con questo stage** — è osservativo, scrive solo file in `failure-modes-log/`.

## Obiettivo

Catturare automaticamente i failure mode di ogni run, classificarli, e generare piani per le phase di miglioramento future — **senza richiedere all'utente alcun comando manuale**.

## Agenti coinvolti (team Self-Improvement)

| Agente | Cosa fa | Quando attivo |
|---|---|---|
| **SI1 `failure-detector-agent`** | Logga FM in `failure-modes-log/logged/` | Solo se QA verdict FAIL/WARN, o feedback utente negativo, o Ox warnings |
| **SI2 `triage-agent`** | Sposta FM da logged/ a triaged/ con metadata (severity, category, scope) | Solo se count(logged/) ≥ 3 |
| **SI3 `phase-planner-agent`** | Genera `PHASE-N-CANDIDATES.md` in `failure-modes-log/` | Solo se soglie raggiunte (vedi cmd_check_thresholds) |

## Spawn order (decisione del Conductor)

```
Stage 9 (Packaging) completed
       ↓
[Stage 10] Conductor decide cosa spawnare:
       │
       ├─ SI1?
       │   IF qa_verdict in [FAIL, WARN] OR user_feedback_negative OR ox_warnings:
       │     SPAWN SI1 → analyze run → write FM(s) to logged/
       │   ELSE:
       │     skip (overhead zero)
       │
       ├─ SI2?
       │   IF count(failure-modes-log/logged/) >= 3:
       │     SPAWN SI2 → triage all FMs in logged/ → move to triaged/
       │   ELSE:
       │     skip
       │
       └─ SI3?
           IF scripts/log_failure.py --check-thresholds → exit 0:
             SPAWN SI3 (silently) → generate PHASE-N-CANDIDATES.md
           ELSE:
             skip
```

## Quando questo stage si attiva

**Sempre**, alla fine di ogni run di `/forge`. Ma gli agenti SI1/SI2/SI3 vengono spawnati **solo se le rispettive condizioni sono vere** (overhead zero quando non c'è nulla da fare).

## Tool usato (interno, per agenti)

`scripts/log_failure.py` con 4 modi operativi auto:

| Comando | Usato da | Quando |
|---|---|---|
| `--quick "desc" --auto --source-stage X --source-agent Y --observation "..."` | SI1 | Crea nuovo FM in logged/ |
| `--triage --auto --fm-id X --severity Y --category Z --scope W --confidence V --effort U` | SI2 | Triage di un singolo FM |
| `--check-thresholds` | Conductor | Verifica se soglie SI3 raggiunte (exit code 0/1) |
| `--plan-phase N` | SI3 | Genera PHASE-N-CANDIDATES.md |

L'utente **non chiama mai** questi comandi direttamente.

## Output

In `failure-modes-log/`:
- `logged/FM-*.md` — FM in attesa di triage (scritti da SI1)
- `triaged/FM-*.md` — FM classificati (spostati da SI2)
- `resolved/FM-*.md` — FM fixati in phase successive (gestiti manualmente o da future versioni)
- `INDEX.md` — lista master (auto-rigenerata)
- `PHASE-N-CANDIDATES.md` — piano della prossima phase (auto-generato da SI3)

Nel workspace del run:
- `stage-10/` — eventuali report dei 3 agenti SI per **questo specifico run** (per audit trail)

## Quando si conclude

Quando tutti i 3 agenti hanno completato (status: ok/skipped). Il Conductor procede normalmente a comunicare il completamento del run all'utente, **senza menzionare niente di Stage 10**.

## 🔇 Principio cardine: silenzio operativo

Stage 10 è progettato per **non aggiungere rumore** all'esperienza utente:

- Nessun "ho trovato un problema!" mid-run
- Nessuna richiesta di conferma per loggare un FM
- Nessuna notifica push di "piano Phase N pronto"
- Nessun rallentamento del flusso primary

L'utente è **libero di ignorare completamente** Stage 10 per mesi. I FM si accumulano silenziosamente. Quando l'utente avrà tempo/voglia di pensare a improvement, può chiedere al Conductor:

> "Forge, cosa hai trovato di problematico?"
> "Forge, hai preparato un piano per la prossima phase?"
> "Forge, mostrami lo stato dei failure mode"

A quel punto il Conductor legge `failure-modes-log/INDEX.md` e i file rilevanti, e risponde.

## Contratto con phase future

Quando l'utente decide di iniziare una nuova phase (es. Phase 10):
1. Legge `failure-modes-log/PHASE-10-CANDIDATES.md` (generato silenziosamente da SI3)
2. Decide cosa includere
3. Scrive `PLAN-v7.md` (manualmente o con aiuto di Conductor)
4. Esegue la phase
5. Sposta i FM fixati in `failure-modes-log/resolved/` (manualmente o future automation)

## Failure modes specifici di Stage 10

| Failure | Mitigazione |
|---|---|
| SI1 logga troppi FM (rumore) | Soglia hardcoded: max 5 FM per run; se più, batch in 1 FM |
| SI2 categorizza male | Conservative defaults; `category: other` + `confidence: low` se incerto |
| SI3 genera plan duplicato | Lock file + check mtime (skip se piano <7 giorni) |
| FM persistono per anni mai risolti | OK: è scelta utente; non vengono mai forzati |
| Conductor menziona Stage 10 spontaneamente | Hard rule nel SP: NEVER mention Stage 10 unless user asks |

## Note operative

- Stage 10 è **molto leggero**: <1 min totale quando attivo
- Non incide su `qa-report.md` finale visto dall'utente
- Il file `failure-modes-log/` è incluso nella skill ma escluso dal `.skill` packaging finale (è dati operativi, non parte della skill)

## Riferimenti

- `agents/self-improvement/failure-detector-agent.md` (SI1)
- `agents/self-improvement/triage-agent.md` (SI2)
- `agents/self-improvement/phase-planner-agent.md` (SI3)
- `scripts/log_failure.py` (tool interno)
- `failure-modes-log/README.md` (agent-managed workspace)
