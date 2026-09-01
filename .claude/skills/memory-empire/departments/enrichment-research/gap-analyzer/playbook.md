# Playbook — gap-analyzer

## Step 1: Per ogni skill in matched_skills.json
Read SKILL.md + references/*.md se esistono

## Step 2: Per ogni atom
Cerca: è già presente? In quale forma?
- Presente identico → skip
- Presente ma meno specifico → GAP con tipo "specificità"
- Assente → GAP

## Step 3: Assegna suggested_section
Trova il heading più pertinente nel file target

## Step 4: Assegna priorità
- high: atom molto rilevante + totalmente assente
- medium: atom rilevante + parzialmente coperto
- low: atom adiacente + lacuna minore

## Step 5: Scrivi gaps.json
