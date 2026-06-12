> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-CRON

# L3 — WF-CRON (Run Ricorrenti Schedulate)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** SCHEDULING
**Coordinator:** `ops-scheduler` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-CRON elimina il "lancio a mano": ogni run ricorrente della holding diventa un
job con espressione cron, runbook, rollback e monitoraggio. È il workflow che porta
a casa il DONE WHEN #3 di OPERATIONS: outreach giornaliero gira da solo.

**Vincolo ADR-003 (wrap, mai riscrittura):** gli script outreach attivi
(`run_parallel.py`, `AVVIA-*.bat` — 6 team Nemotron $0/giorno) non si toccano.
WF-CRON li invoca tramite le skill `avvia-*` e ne osserva l'esito.

## Schedule attive (al momento della stesura)

| Nome schedule | Frequenza | Trigger ufficiale | Owner |
|---|---|---|---|
| outreach-email | giornaliera | skill `avvia-email` | 01-AGENCY |
| outreach-ig | giornaliera | skill `avvia-ig` | 01-AGENCY |
| outreach-parallel | giornaliera | skill `avvia-parallel` | 01-AGENCY |
| wiki-garden | settimanale | handoff a 08-INTELLIGENCE | 08-INTELLIGENCE |
| trend-radar | mensile | handoff a 08-INTELLIGENCE | 08-INTELLIGENCE |
| backup-empire | settimanale | skill `asset-vault` / WF-BACKUP | 09-OPERATIONS |
| report-costi-board | settimanale | ops-cost-accountant | CFO / Board |

## Input / Output

**Registrazione schedule (una tantum):**
```json
{
  "nome": "outreach-email",
  "cron_expr": "0 8 * * 1-5",
  "trigger": "avvia-email",
  "budget_per_run": 0.00,
  "budget_mensile_max": 0.00,
  "runbook": "path/al/runbook.md",
  "rollback": "descrizione procedura rollback"
}
```
**Senza runbook e rollback: la schedule NON viene registrata (gate G-RUNBOOK).**

**Output per ogni esecuzione:**
```json
{
  "schedule": "outreach-email",
  "esito": "success|failed|skipped",
  "costo": 0.00,
  "durata_sec": 0,
  "note": "..."
}
```

## Processo decisionale (`ops-scheduler`)

1. Trigger temporale scatta → verifica pre-condizioni (token validi? daemon su?
   disco libero? — chiede a `ops-watchdog`). Pre-condizione rossa → NON lancia, alert.
2. Verifica budget residuo con `ops-cost-sentinel`: questa run entra nel budget mensile?
   No → sospende e alert. Mai "lancia e spera".
3. Lancia via trigger ufficiale (skill avvia-* o handoff). Non invoca mai internals.
4. Registra esito + durata + costo in `operations/schedule`.
5. Fallimento → 1 retry se runbook lo permette, poi escalation a ops-director.
6. Run in ritardo > finestra configurabile → segnala a ops-watchdog.

## Gate di qualità

- `G-RUNBOOK` — ogni schedule ha runbook + rollback; senza, non si registra
- `G-BUDGET` — budget per-run e mensile dichiarati e verificati prima di ogni lancio
- `G-WRAP` — si invoca solo tramite trigger ufficiale (ADR-003: mai toccare script attivi)

## KPI

| Metrica | Target |
|---|---|
| Run schedulate completate senza intervento | ≥ 95% |
| Schedules senza runbook | 0 |
| Token scaduti rilevati PRIMA che la run fallisca | 100% |
| Report costi Board inviato puntuale | 100% settimane |
