# Playbook — update-proposer

## Input
- `gaps.json`
- `improvements.json`
- Accesso in lettura alle skill target

## Step 1 — Merge e de-duplica
Combina gaps e improvements in una lista unica ordinata per priority.

## Step 2 — Per ogni item
a. Read del file target (SKILL.md o altro)
b. Trova heading section target
c. Scrivi content_to_add in markdown
d. Assegna insert_mode

## Step 3 — Verifica contenuto
- Non è già presente nella skill? (evita duplicati)
- È tutto il valore, non un riassunto?
- Fonte tracciata?

## Step 4 — Assegna priorità finale
high → da eseguire questa sessione
medium → da eseguire nella prossima sessione
low → backlog

## Step 5 — Scrivi proposals.json
`memory/handoffs/proposals-<timestamp>.json`

## Step 6 — Preview a dept-lead
Elenca le proposals in formato leggibile per il dept-lead:
"PROP-001: Aggiungo a copywriting/SKILL.md sezione 'Approccio positivo Opus 4.8' (450 chars)"
