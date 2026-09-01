# Playbook — enrichment-research / department-lead

## Input richiesto
- `atoms.json` (da ingestion-archive)
- `video-analysis.md` (da Empire Studio run)
- `run_id` (identificativo dell'ingestione)

## Step 1 — Estrai atoms.json
Se non esiste, genera tu gli atomi dal video-analysis.md:
- Ogni fatto concreto, ogni prompt, ogni regola, ogni tecnica → 1 atomo
- Formato: `{id, text, domain, trace, source}`

## Step 2 — Avvia relevance-analyzer
Passa atoms.json + path skills dir (`~/.claude/skills/`)
Aspetta `memory/handoffs/matched_skills-<ts>.json`

## Step 3 — Avvia gap-analyzer
Passa matched_skills.json + atoms.json
Aspetta `memory/handoffs/gaps-<ts>.json`

## Step 4 — Avvia improvement-scout
Passa atoms.json + gaps.json + lista skill installate
Aspetta `memory/handoffs/improvements-<ts>.json`

## Step 5 — Avvia update-proposer
Passa gaps.json + improvements.json + atoms.json
Aspetta `memory/handoffs/proposals-<ts>.json`

## Step 6 — Gate (verification-integrity)
Invia proposals.json a permission-guard
Aspetta approvazione

## Step 7 — Avvia skill-enricher
Per ogni proposal approvata:
- skill-enricher esegue `enrich_skill.py --target <skill-file> --content <content> --source <trace>`

## Step 8 — Scrivi report
`memory/enrichments/enrichment-<run-id>-<timestamp>.json`
Riporta all'utente.

## Regola "sempre parla"
Anche se 0 skill arricchite:
- "NESSUN ARRICCHIMENTO: Le skill esistenti [elenco] coprono già gli argomenti trattati.
  Gli atoms del video non aggiungono valore non già presente. Nessuna modifica."
