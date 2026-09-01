# routing-dispatch / activation-monitor

**Ruolo:** Verifica che il workflow attivato da workflow-router stia effettivamente girando. Se Empire Studio non ha creato la run directory o i file di output attesi, lo segnala immediatamente al dept-lead per re-attivazione.

## Cosa verifica per Empire Studio

| File atteso | Significato |
|-------------|-------------|
| `runs/<run-id>/ingest.json` | yt_ingest completato |
| `runs/<run-id>/frames/manifest.json` | frame_extractor completato |
| `runs/<run-id>/frames/frame-001.png` | almeno un frame estratto |

## Output Handoff
File: `memory/handoffs/monitor-result-<timestamp>.json`
```json
{
  "agent": "activation-monitor",
  "workflow": "empire-studio",
  "run_id": "...",
  "status": "confirmed|failed",
  "checks_passed": ["ingest.json", "frames/manifest.json"],
  "checks_failed": [],
  "action_required": null
}
```
