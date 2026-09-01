# routing-dispatch / workflow-router

**Ruolo:** Riceve la classificazione da intent-classifier e attiva il workflow corretto. Conosce la mappa completa intento→workflow. È la rete di sicurezza per Empire Studio.

## Mappa Routing

| Intent Type | Platform | Workflow | Azione |
|-------------|----------|----------|--------|
| INGEST_LINK | youtube | Empire Studio (youtube-dept) | `yt_ingest.py` + `frame_extractor.py --interval 2` |
| INGEST_LINK | tiktok | Empire Studio (tiktok-dept) | tiktok pipeline |
| INGEST_LINK | repo | Empire Studio (projects-dept) | repo deep study |
| INGEST_LINK | web | Empire Studio (web-dept) | crawl + screenshot |
| INGEST_KEYWORD | any | Empire Studio | pipeline completa |
| QUERY_DE | - | digital-empire-context | carica wiki + knowledge |
| WORK_DE | outreach | avvia-email / avvia-linkedin | richiama workflow |
| WORK_DE | books | printing-press | richiama workflow |
| ENRICHMENT_COMPLETE | - | enrichment-research | attiva pipeline |

## Output Handoff
File: `memory/handoffs/routing-result-<timestamp>.json`
```json
{
  "agent": "workflow-router",
  "timestamp": "...",
  "intent_type": "INGEST_LINK",
  "workflow_activated": "empire-studio",
  "activation_method": "direct_script",
  "run_id": "...",
  "status": "activated"
}
```
