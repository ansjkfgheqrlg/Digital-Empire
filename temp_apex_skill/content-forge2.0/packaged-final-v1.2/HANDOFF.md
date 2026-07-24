# 🎉 `content-forge` v1.2 — Self-Improvement Loop (auto)

> Deliverable post Phase 9. Generata: 2026-05-26.
> Aggiunge **Stage 10 self-improvement loop completamente autonomo**.
> L'utente non scrive comandi né tocca file: gli agenti loggano, triano e pianificano da soli.

---

## 🆕 Cosa cambia rispetto a v1.1

v1.1 aveva il sistema failure-modes-log/ ma richiedeva all'utente di eseguire comandi Python manualmente (`log_failure.py --quick ...`). **Era sbagliato per il modello d'uso reale.**

v1.2 fixa: **gli agenti fanno tutto da soli**.

### Pipeline ora a 10 stage

```
Stage 1-9 (invariati da Phase 9)
       ↓
[Stage 10] 🆕 SELF-IMPROVEMENT OBSERVE — silenzioso, automatico, condizionale
       │
       ├─ SI1 failure-detector → logga FM se QA fail/warn o feedback utente negativo
       ├─ SI2 triage → triage automatico quando logged/ ≥ 3 FM
       └─ SI3 phase-planner → genera PHASE-N-CANDIDATES.md silenziosamente quando soglie raggiunte
```

### 3 nuovi agenti (team SI in `agents/self-improvement/`)

| Agente | Quando attivo | Cosa fa |
|---|---|---|
| **SI1 — failure-detector-agent** | Stage 10, solo se QA fail/warn o feedback negativo o Ox warnings | Scrive automaticamente FM in `failure-modes-log/logged/` via script |
| **SI2 — triage-agent** | Stage 10, solo se `count(logged/) ≥ 3` | Triage auto: assegna severity/category/scope/confidence/effort, sposta in `triaged/` |
| **SI3 — phase-planner-agent** | Stage 10, solo se soglie raggiunte (≥3 major, o ≥1 blocker, o ≥5 totali) | Genera silenziosamente `PHASE-N-CANDIDATES.md` |

### Modalità AUTO dello script (per agenti)

`scripts/log_failure.py` ora supporta:
- `--quick "desc" --auto --source-stage X --source-agent Y --observation "..."` (per SI1)
- `--triage --auto --fm-id X --severity Y --category Z --scope W --confidence V --effort U` (per SI2)
- `--check-thresholds` (per Conductor — exit code 0 se soglie raggiunte)
- `--plan-phase N` (per SI3)

Tutti i comandi ritornano **JSON parsabile**, gli agenti li chiamano via Bash e parsano output.

L'utente **non chiama mai** questi comandi manualmente.

---

## 🔇 Principio cardine: silenzio operativo

Stage 10 è **completamente silenzioso**:
- Nessun "ho trovato un problema!" durante un run
- Nessuna richiesta di conferma per loggare un FM
- Nessuna notifica push di "piano Phase N pronto"
- Nessun rallentamento del flusso primary

L'utente può **ignorare completamente** Stage 10 per mesi.

### Quando vuoi sapere cosa è successo

Chiedi semplicemente al Conductor in conversazione:

> "Forge, cosa hai trovato di problematico?"
> "Forge, hai preparato un piano per la prossima phase?"
> "Forge, mostrami lo stato dei failure mode"

Il Conductor legge `failure-modes-log/INDEX.md` e file rilevanti, risponde.

---

## ✅ Test end-to-end (interno)

Tutti i modi auto verificati:

| Test | Risultato |
|---|---|
| SI1 mode (`--quick --auto`) | ✅ Crea FM in logged/ |
| SI2 mode (`--triage --auto`) | ✅ Triage + sposta in triaged/ |
| `--check-thresholds` con 1 FM | ✅ Exit code 1 (soglia non raggiunta) |
| `--check-thresholds` con 3 FM major | ✅ Exit code 0 (soglia raggiunta) |
| SI3 mode (`--plan-phase N`) | ✅ Genera PHASE-N-CANDIDATES.md |
| Pytest full suite | ✅ 80/80 passed |
| Nuovi agenti SI frontmatter | ✅ 3/3 validi |

---

## 📊 Stato repo

| Metrica | v1.1 | v1.2 |
|---|---|---|
| File totali | 207 | 217 (+10) |
| Agenti specialisti | 17 | **20** (+3 SI) |
| Stage pipeline | 9 | **10** |
| Test pytest | 69 | 80 (+11 da log_failure tests) |
| Dimensione .skill | 364 KB | 392 KB |

---

## 🚀 Come usarla

```bash
# Installa
unzip content-forge-v1.2.skill -d ~/.claude/skills/
```

Poi usa la skill normalmente con `/forge`. **Niente di nuovo nel tuo flusso.**

Il sistema self-improvement gira in background. Dopo che hai usato la skill per qualche settimana, **chiedi**:

> "Forge, cosa hai trovato di problematico?"

E vedrai il report.

---

## 🛣 Storia completa versioni

| Phase | Cosa | Esito |
|---|---|---|
| 0-8 | Build iniziale → v1.0 (Phase 8 packaging) | ✅ |
| 9 | Depth Architecture → v1.1 | ✅ |
| **Post-9** | **Self-Improvement Loop auto → v1.2** | **✅ questa** |

---

## ⏭ Quando aspettarsi v1.3+

Quando hai usato v1.2 per ≥1 settimana, fa:

> "Forge, hai preparato un piano per la prossima phase?"

Se SI3 ha generato `PHASE-10-CANDIDATES.md`, lo vedrai. Usalo come input per Phase 10.

Se non ha generato nulla, significa che la skill sta funzionando bene per te (no FM accumulati, no soglie raggiunte).
