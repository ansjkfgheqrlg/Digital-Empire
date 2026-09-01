# Playbook — workflow-router

## Step 1: Leggi classificazione
Apri `memory/handoffs/intent-<latest>.json`

## Step 2: Mappa intento → workflow
Usa tabella in workflow-router.md

## Step 3: Genera run-id (se Empire Studio)
`<slug-titolo>-<YYYY-MM-DD>` (max 30 char, windows-safe)

## Step 4: Attiva workflow
- Empire Studio: lancia yt_ingest.py → frame_extractor.py
- Altro: invoca skill o workflow appropriato

## Step 5: Scrivi handoff
`memory/handoffs/routing-result-<timestamp>.json`

## Step 6: Notifica activation-monitor
Passa: `{workflow: "empire-studio", run_id: "...", launched_at: "..."}`
