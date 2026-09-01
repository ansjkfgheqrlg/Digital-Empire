# Tools — enrichment-research / department-lead

## Read
- `video-analysis.md` (da empire-studio run)
- `memory/handoffs/*.json` (output degli agenti)
- `~/.claude/skills/*/SKILL.md` (per capire le skill installate)

## Write
- `memory/enrichments/enrichment-<run-id>-<timestamp>.json`
- `memory/handoffs/atoms-<timestamp>.json` (se non già generati)

## Agent / Task
- Invoca relevance-analyzer, gap-analyzer, improvement-scout, update-proposer, skill-enricher

## Bash
- `python scripts/enrich_skill.py --dry-run` (per preview prima di applicare)
