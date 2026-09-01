# Playbook — activation-monitor

## Step 1: Ricevi routing-result
Leggi `memory/handoffs/routing-result-<latest>.json` → estrai `run_id` e `workflow`

## Step 2: Costruisci path attesi
`<empire-studio-root>/runs/<run_id>/`

## Step 3: Verifica file
- Glob: `runs/<run-id>/ingest.json`
- Glob: `runs/<run-id>/frames/manifest.json`
- Glob: `runs/<run-id>/frames/frame-001.png`

## Step 4: Valuta
- Tutti presenti → confirmed
- Anche 1 mancante → failed + lista file mancanti

## Step 5: Scrivi handoff
`memory/handoffs/monitor-result-<timestamp>.json`

## Step 6: Se failed → segnala a dept-lead
"ATTENZIONE: Empire Studio non ha prodotto output. File mancanti: [...]"
