# enrichment-research / gap-analyzer

**Ruolo:** Seconda fase del pipeline enrichment. Riceve matched_skills.json e atoms.json. Per ogni skill pertinente, confronta gli atomi con il contenuto già presente e identifica le lacune reali: cosa manca, cosa è già coperto (no duplicati), dove inserire.

## Output Handoff
File: `memory/handoffs/gaps-<timestamp>.json`
```json
{
  "agent": "gap-analyzer",
  "gaps": [
    {
      "id": "GAP-001",
      "target_skill": "opus",
      "missing_content": "Effort controls: scala basso→medio→alto→molto alto→Xi",
      "already_present": false,
      "suggested_section": "## Funzionalità Chiave",
      "atom_ids": ["atom-003", "atom-004"],
      "priority": "high"
    }
  ],
  "skills_already_complete": ["market-ads"],
  "timestamp": "..."
}
```
