# Playbook — relevance-analyzer

## Step 1: Estrai keywords da atoms
Leggi atoms.json → lista unica di domain keywords

## Step 2: Scansione skill
```bash
python scripts/relevance_scan.py --atoms atoms.json --skills-dir ~/.claude/skills/
```
Oppure: leggi SKILL.md di ogni skill, calcola overlap manualmente

## Step 3: Filtra (score >= 0.4)

## Step 4: Aggiungi skill "sempre" se dominio AI/Claude

## Step 5: Scrivi matched_skills.json

## Step 6: Log in memory/analysis/relevance-<run-id>.json
