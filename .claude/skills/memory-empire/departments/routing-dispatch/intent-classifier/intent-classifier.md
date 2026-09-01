# routing-dispatch / intent-classifier

**Ruolo:** Classifica l'intento di ogni messaggio utente in Digital Empire. Output: JSON strutturato con tipo, confidenza, URL estratti, workflow target.

## Intent Types

| Tipo | Descrizione | Workflow Target |
|------|-------------|-----------------|
| `INGEST_LINK` | Messaggio contiene URL (yt, tiktok, sito, repo) | empire-studio |
| `INGEST_KEYWORD` | "ingerisci", "guarda", "studia", "analizza", "prendi la formazione" | empire-studio |
| `QUERY_DE` | Domanda su Digital Empire, agenzia, corsi, SaaS | digital-empire-context |
| `WORK_DE` | Lavoro su outreach, email, IG, libri, siti | workflow specifico |
| `ENRICHMENT_COMPLETE` | Empire Studio ha finito → attiva enrichment | enrichment-research |
| `OTHER` | Nessun match specifico | nessuno |

## Output Handoff
File: `memory/handoffs/intent-<timestamp>.json`
```json
{
  "agent": "intent-classifier",
  "timestamp": "...",
  "input_summary": "...",
  "intent_type": "INGEST_LINK",
  "confidence": 0.98,
  "extracted_urls": ["https://youtube.com/watch?v=..."],
  "keywords_matched": [],
  "workflow_target": "empire-studio",
  "platform": "youtube"
}
```
