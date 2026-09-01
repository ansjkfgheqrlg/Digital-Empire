# Tools — routing-dispatch / department-lead

## Read
- Legge routing-map.md
- Legge file handoff JSON da memory/handoffs/
- Legge SKILL.md di Empire Studio (se serve re-attivazione manuale)

## Write
- Scrive log in memory/routing/

## Bash
- `python scripts/yt_ingest.py --input <URL> --run <run-id>` (fallback manuale)
- `python scripts/frame_extractor.py --run <run-id> --interval 2` (fallback manuale)

## Agent / Task (Claude Code tool)
- Invoca intent-classifier come subagente
- Invoca workflow-router come subagente
- Invoca activation-monitor come subagente
