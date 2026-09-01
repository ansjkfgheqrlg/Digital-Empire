# enrichment-research / relevance-analyzer

**Ruolo:** Prima fase del pipeline enrichment. Scansiona tutte le skill installate in `~/.claude/skills/` e assegna un punteggio di rilevanza rispetto agli atomi della nuova conoscenza. Produce `matched_skills.json` con le skill pertinenti ordinate per score.

## Come calcola la rilevanza
- Confronta domain degli atoms con domain dichiarato in SKILL.md (tag frontmatter, titolo, descrizione)
- Cerca keyword overlap tra atoms e contenuto SKILL.md
- Considera anche skill "adiacenti" (es. video su AI → skill di copywriting, workflow, prompt)

## Output Handoff
File: `memory/handoffs/matched_skills-<timestamp>.json`
```json
{
  "agent": "relevance-analyzer",
  "atoms_count": N,
  "matched_skills": [
    {"name": "copywriting", "path": "~/.claude/skills/copywriting/SKILL.md", "score": 0.87, "matched_keywords": ["prompt", "istruzioni", "tono"]},
    {"name": "opus", "path": "~/.claude/skills/opus/SKILL.md", "score": 0.95, "matched_keywords": ["claude", "opus", "modello"]}
  ],
  "threshold_used": 0.4,
  "timestamp": "..."
}
```
