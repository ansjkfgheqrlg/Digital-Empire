---
Type: SKILLS
Status: Active (M3 — definite, wiring M4)
Tags: #ispettorato #skills #io-json #deterministico
Created: 2026-07-20
Last updated: 2026-07-20
---

# Skills — Ispettorato Generale

> Skill del reparto: interfacce a I/O JSON che wrappano gli script deterministici (`scripts/`,
> €0 API — Mandato Art.4.3). Contratto: input JSON → output JSON. Un dato assente diventa
> `"nessun dato"` nell'output, mai uno zero o un numero finto (Gate 4 ARCHITETTURA).

---

## run-audit
**Cosa fa:** audita una singola run — normalizza la telemetria, valuta i gate, calcola gli
scostamenti KPI, produce l'esito VERDE/ROSSO e l'elenco errori. Wrappa `trace_collector.py` +
`report_generator.py`.
**Input JSON:** `{ "run_id": "...", "workflow": "...", "kpi_thresholds_ref": "kpi/..." }`
**Output JSON:** `{ "esito": "VERDE|ROSSO", "exit": 0, "durata_ms": 0, "gate": {"verdi": n, "tot": n}, "kpi": {...|"nessun dato"}, "errori_nuovi": ["ERR-..."], "recidiva": ["ERR-..."], "report_path": "report/run/<run-id>.md" }`
**Usata da:** `isp-run-auditor` · `isp-report-forger`.

## recidiva-check
**Cosa fa:** confronta un errore nuovo col `REGISTRO-ERRORI.md`; match → RECIDIVA → gate ROSSO +
segnale di escalation. Wrappa `recidiva_check.py`.
**Input JSON:** `{ "symptom": "...", "root_cause": "...", "run_id": "..." }`
**Output JSON:** `{ "stato": "NEW|RECIDIVA", "match": "ERR-...|null", "gate": "VERDE|ROSSO", "escalation_richiesta": true|false }`
**Usata da:** `isp-recidiva-sentinel` (batch gemello) · `isp-error-registrar`.

## revision-study
**Cosa fa:** studia la catena COMPLETA di correzioni di un task → pattern + regola generale →
voce `REV-*`; se 0 correzioni → voce `SUC-*`. Aggiorna `revisioni_medie_per_task`
(wrappa `revision_metrics.py`).
**Input JSON:** `{ "task_ref": "...", "correzioni": [ {"n":1, "cosa":"...", "perche":"..."} ], "esito": "accettato" }`
**Output JSON:** `{ "voce": "REV-YYYYMMDD-NNN|SUC-YYYYMMDD-NNN", "pattern": "...", "regola_generale": "...", "revisioni_medie_per_task": 0.0|"dato insufficiente" }`
**Usata da:** `isp-revision-analyst` · `isp-kpi-analyst` (batch gemello).

## daily-report
**Cosa fa:** aggrega le run del giorno + KPI trend + autocritica + top-3 azioni nel daily report.
Wrappa `report_generator.py --type daily`.
**Input JSON:** `{ "date": "YYYY-MM-DD" }`
**Output JSON:** `{ "report_path": "report/daily/<date>.md", "kpi_trend": {...|"nessun dato"}, "top3_azioni": [ {"azione":"...","owner":"...","scadenza":"..."} ] }`
**Usata da:** `isp-report-forger` · `isp-improvement-dispatcher`.

---

## Connessioni
- [[ARCHITETTURA]] · `../ARCHITETTURA.md` — namespace stato, gate
- `../scripts/README.md` — gli script deterministici che queste skill wrappano
- [[15-DOSSIER-ISPETTORATO]] · §6 backbone dati · §8 template
- Riferimento formato: `company/Board-CSuite/CFO/skills/SKILLS.md`
