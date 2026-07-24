# Failure Modes Log — `content-forge`

> **Workspace agent-managed**. L'utente NON tocca questi file direttamente.
> Tutta la logica è gestita da 3 agenti in `agents/self-improvement/`:
>
> - **SI1 `failure-detector-agent`** scrive automaticamente in `logged/` quando rileva problemi nel run
> - **SI2 `triage-agent`** sposta automaticamente in `triaged/` quando soglia accumulo è raggiunta
> - **SI3 `phase-planner-agent`** genera automaticamente `PHASE-N-CANDIDATES.md` quando soglia è raggiunta
>
> Lo script `scripts/log_failure.py` è un **tool interno** chiamato dagli agenti, non eseguito dall'utente.

---

## 📁 Struttura

```
failure-modes-log/
├── README.md              ← questo
├── TEMPLATE.md            ← usato da SI1 per creare nuovi FM
├── INDEX.md               ← rigenerato automaticamente
├── logged/                ← FM scritti da SI1 (waiting for triage)
├── triaged/               ← FM analizzati da SI2 (waiting for phase plan)
├── resolved/              ← FM fixati in una phase successiva
└── PHASE-N-CANDIDATES.md  ← generato da SI3 quando soglia raggiunta
```

---

## 🔄 Flusso automatico

```
Tu usi /forge
    ↓
Stage 1-9 normali
    ↓
Stage 10 (Self-Improvement Observe) — automatico
    │
    ├─► SI1 attivo SE:
    │     • QA (Stage 8) ha verdict FAIL/WARN
    │     • utente ha segnalato problema esplicitamente
    │   → scrive FM-NNN-slug.md in logged/
    │
    ├─► Conductor controlla count logged/
    │     SE count ≥ 3:
    │       spawn SI2 → triage automatico
    │
    └─► Conductor controlla triaged/ contro soglie:
          SE ≥3 major OR ≥1 blocker OR ≥5 totali:
            spawn SI3 (silenzioso) → genera PHASE-N-CANDIDATES.md
```

---

## 👀 Come vedere lo stato (quando vuoi, opzionale)

Puoi chiedere al Conductor in conversazione:

> "Forge, dimmi lo stato dei failure mode"

→ Conductor legge `INDEX.md` e ti riassume.

Oppure:

> "Forge, c'è già un piano per la prossima phase?"

→ Conductor controlla se esiste `PHASE-N-CANDIDATES.md` e te lo mostra.

NIENTE da fare attivamente da parte tua. Il sistema osserva e accumula in background.

---

## 🛠 Tool interni (per agenti)

Gli agenti SI1/SI2/SI3 usano lo script `scripts/log_failure.py` via Bash:

```bash
# SI1 invoca:
python3 scripts/log_failure.py --quick "<descrizione>" --auto

# SI2 invoca:
python3 scripts/log_failure.py --triage --auto \
  --fm-id FM-001 --severity major --category builder ...

# SI3 invoca:
python3 scripts/log_failure.py --plan-phase N
```

L'utente non chiama mai questi comandi direttamente.
