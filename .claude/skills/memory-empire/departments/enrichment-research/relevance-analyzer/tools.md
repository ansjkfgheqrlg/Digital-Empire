# Tools — relevance-analyzer

## Bash
- `python scripts/relevance_scan.py --atoms <atoms.json> --skills-dir ~/.claude/skills/`

## Glob
- `~/.claude/skills/*/SKILL.md`

## Read
- `memory/handoffs/atoms-<latest>.json`
- `~/.claude/skills/<name>/SKILL.md`

## Write
- `memory/handoffs/matched_skills-<timestamp>.json`
- `memory/analysis/relevance-<run-id>.json`
