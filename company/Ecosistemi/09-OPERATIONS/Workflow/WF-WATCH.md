> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-WATCH

# L3 — WF-WATCH (Health Check Processi della Holding)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** MONITORING-DASHBOARD
**Coordinator:** `ops-watchdog` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-WATCH garantisce che nessun processo della holding giri al buio e che nessun
guasto resti invisibile più di 15 minuti. Always-on a polling (cron ogni 10-15 min)
+ ricezione passiva di heartbeat in mesh. Il watchdog verifica lo stato REALE dal
filesystem/processi — mai dichiarato (pattern catalog_status di Empire Studio).

## Perimetro di monitoraggio

| Processo | Frequenza check | SLA alert | Note |
|---|---|---|---|
| Run outreach (email/ig/parallel) | ogni 15 min | ≤ 15 min da fallimento | token FB è storico punto di failure |
| Daemon Ruflo (Windows) | ogni 10 min | ≤ 10 min | rischio #5: daemon non persistente su Windows |
| Token di accesso (FB, Instagram, LinkedIn) | ogni 60 min | alert PRIMA della scadenza | token FB è scaduto silenziosamente in passato |
| Sync Max↔Gael (empire-sync.ps1) | ogni 60 min | se >2h senza sync ok | ADR-004 |
| Spazio disco | ogni 60 min | alert se <10% libero | asset pesanti possono riempire disco |
| Queue WF-QUEUE | ogni 15 min | alert se coda > soglia | backpressure |
| Processi zombie | ogni 30 min | kill + log immediato | run che non terminano |

## Processo decisionale (`ops-watchdog`)

1. Per ogni processo censito nel runbook registry: atteso vivo? → verifica reale
   (processo attivo, file di log recente, timestamp ultimo esito). Stato letto, mai dichiarato.
2. Anomalia → classifica:
   - Run fallita → controlla retry policy del runbook; 1 retry se permesso → esito → CP.
   - Daemon Ruflo giù → bootstrap auto-riparante; se fallisce → fallback bash + alert.
   - Token in scadenza/scaduto → alert al proprietario PRIMA che il flusso fallisca.
   - Zombie (processo attivo da > timeout configurato) → kill + log.
3. SLA: run fallita scoperta entro ≤15 min dalla fine anomala.
4. Tre guasti uguali in 7 giorni → non è incidente ma pattern: handoff a INTELLIGENCE
   (ReasoningBank) + proposta fix strutturale a ops-director.
5. Ogni check: heartbeat in `operations/health` (AgentDB).

## Input / Output

**Heartbeat in ingresso (da processi monitorati):**
```json
{
  "processo": "outreach-email",
  "timestamp": "ISO8601",
  "stato": "running|completed|failed",
  "dettagli": "..."
}
```

**Alert in uscita (su anomalia):**
```json
{
  "alert_id": "ALR-YYYYMMDD-NNN",
  "processo": "outreach-email",
  "tipo": "run_failed|daemon_down|token_expired|zombie|disk_low",
  "priorita": 1,
  "azione_suggerita": "...",
  "destinatario": "ops-director|proprietario_workflow|Board"
}
```

## Gate di qualità

- `G-REAL-STATE` — stato letto dal filesystem/processo reale, mai dichiarato
- `G-SLA-15MIN` — run fallita rilevata entro 15 min
- `G-TOKEN-PREEMPT` — alert token PRIMA della scadenza, non dopo il fallimento

## KPI

| Metrica | Target |
|---|---|
| Tempo rilevazione run fallita | ≤ 15 min |
| Token scaduti senza pre-alert | 0 |
| False positive alert | ≤ 5% dei check |
| Zombie rilevati e killati | 100% entro 30 min |
