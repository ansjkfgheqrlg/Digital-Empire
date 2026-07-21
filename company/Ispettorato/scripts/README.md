---
Type: SCRIPTS
Status: Active (M3 — previsti, implementazione M4)
Tags: #ispettorato #scripts #deterministico #zero-api
Created: 2026-07-20
Last updated: 2026-07-20
---

# Scripts — Ispettorato Generale

> Backbone dati deterministico, **€0 API** (Mandato Art.4.3): i report si COMPILANO dai dati con
> script Python senza LLM; gli agenti `isp-*` interpretano solo dove serve giudizio. Zero numeri
> inventati: un dato assente si scrive "nessun dato", mai uno zero finto.

Convenzione return code comune: `0` = ok · `1` = errore d'uso (argomenti/percorsi) · `2` = dati
mancanti o corrotti (l'agente chiamante deve gestire il "nessun dato", non fallire in silenzio).

---

## trace_collector.py
**Cosa fa:** legge la telemetria grezza di una run (`telemetry/runs/<workflow>/<run-id>.jsonl`,
eventi `run_id, ts, step, gate, exit, dur_ms, err`) e la normalizza in una struttura pronta per
l'audit (timeline ordinata, durate per step, esito gate, exit code).
**Input:** `--run-id`, `--workflow` (o path al `.jsonl`).
**Output:** struttura normalizzata su stdout (JSON) + eventuale `telemetry/daily/<data>.md` snapshot.
**Return:** `0` ok · `2` trace assente/malformata (→ l'auditor segna "nessun dato").
**Chiamato da:** `isp-telemetry-collector`.

## report_generator.py
**Cosa fa:** compila i report dal template fisso (dossier 15 §8) a partire dai dati normalizzati +
KPI + voci registro. Produce run-report, daily, escalation con TUTTE le sezioni; dove manca un dato
scrive "nessun dato".
**Input:** `--type run|daily|escalation`, `--run-id` / `--date`, path ai KPI e ai registri.
**Output:** `report/run/<run-id>.md` · `report/daily/<YYYY-MM-DD>.md` · `report/escalation/<id>.md`.
**Return:** `0` ok · `1` tipo/argomenti non validi · `2` dati insufficienti per il template.
**Chiamato da:** `isp-report-forger`.

## recidiva_check.py
**Cosa fa:** confronta un errore nuovo con le voci `ERR-*` di `registro/REGISTRO-ERRORI.md`
(match su sintomo/causa radice normalizzati). Match → segnala RECIDIVA (gate ROSSO).
**Input:** `--symptom`, `--root-cause` (o path a un descrittore errore).
**Output:** esito su stdout: `NEW` oppure `RECIDIVA <ERR-id>`; codice per il gate.
**Return:** `0` errore nuovo · `3` RECIDIVA trovata (gate ROSSO) · `2` registro illeggibile.
**Chiamato da:** `isp-recidiva-sentinel` (batch gemello).

## revision_metrics.py
**Cosa fa:** calcola `revisioni_medie_per_task` e trend dalle voci `REV-*`/`SUC-*` dei registri.
Se i task sono troppo pochi per una media affidabile → "dato insufficiente" (mai un numero finto).
**Input:** finestra temporale (`--from`, `--to`) o `--last N` task.
**Output:** metrica + trend su stdout (JSON), pronta per `kpi/`.
**Return:** `0` ok · `2` dati insufficienti (metrica = "dato insufficiente", non errore fatale).
**Chiamato da:** `isp-kpi-analyst` (batch gemello) · `isp-revision-analyst`.

---

## Connessioni
- [[ARCHITETTURA]] · `../ARCHITETTURA.md` — backbone dati €0 API (Mandato Art.4.3)
- [[15-DOSSIER-ISPETTORATO]] · §6 (convenzione trace JSONL) · §8 (template report)
- `../skills/SKILLS.md` — le skill che wrappano questi script con I/O JSON
