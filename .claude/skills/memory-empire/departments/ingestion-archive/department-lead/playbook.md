# Playbook — ingestion-archive / department-lead

## Step 1: Ricevi run-id
Leggi da `memory/handoffs/routing-result-<latest>.json`

## Step 2: Leggi output Empire Studio
`runs/<run-id>/video-analysis.md` + `ingest.json`

## Step 3: Invoca content-validator
Aspetta `memory/handoffs/validation-<ts>.json`

## Step 4: Se validated=true → invoca knowledge-keeper
Passa: run-id, source-type (youtube/tiktok/web), content-path

## Step 5: Invoca wiki-syncer
Passa: run-id, content-path, wiki-target-section

## Step 6: Genera atoms.json
Estrai da video-analysis.md ogni fatto concreto, prompt, tecnica, regola
Formato: `{id, text, domain, trace, source}`
Salva in `knowledge/<run-id>/atoms.json`

## Step 7: Notifica enrichment-research
Scrivi `memory/handoffs/ingestion-ready-<ts>.json`:
```json
{"run_id": "...", "atoms_path": "knowledge/<run-id>/atoms.json", "status": "ready"}
```

## Step 8: Log
`memory/ingestions/ingestion-<run-id>-<ts>.json`
