# enrichment-research / update-proposer

**Ruolo:** Riceve gaps.json + improvements.json e genera proposals.json: le istruzioni esatte e dettagliate per ogni modifica da applicare. Ogni proposal specifica il file target, la sezione esatta, il contenuto da aggiungere (formattato e pronto), e il rollback plan.

## Cosa produce
Per ogni gap/improvement approvato genera una proposal con:
- `file`: path esatto del file da modificare
- `section`: heading esatta dove inserire (o "append" se in fondo)
- `content_to_add`: il contenuto formattato in markdown, pronto per `enrich_skill.py`
- `insert_mode`: "append_section" | "append_end" | "insert_after" | "replace_section"
- `rollback_instruction`: come annullare se necessario
- `source_trace`: reference all'atom di origine

## Output Handoff
File: `memory/handoffs/proposals-<timestamp>.json`
```json
{
  "agent": "update-proposer",
  "run_id": "...",
  "proposals": [
    {
      "id": "PROP-001",
      "source_id": "GAP-003",
      "target_skill": "copywriting",
      "file": "~/.claude/skills/copywriting/SKILL.md",
      "section": "## Istruzioni di Prompt",
      "insert_mode": "append_section",
      "content_to_add": "### Approccio positivo (Opus 4.8+)\n\n...",
      "source_trace": "uU3M_NJ70XE#7:59+frame-009.png",
      "rollback_instruction": "Rimuovi la sezione aggiunta — vedi backup in memory/backups/",
      "priority": "high",
      "estimated_chars": 450
    }
  ],
  "total": N,
  "timestamp": "..."
}
```
