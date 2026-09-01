# Playbook — knowledge-keeper

## Step 1: Crea directory
mkdir knowledge/<run-id>/

## Step 2: Copia file
cp runs/<run-id>/video-analysis.md knowledge/<run-id>/contenuto-integrale.md
cp runs/<run-id>/ingest.json knowledge/<run-id>/ingest-manifest.json

## Step 3: Verifica completezza
Se < 500 chars → fail

## Step 4: Scrivi handoff
memory/handoffs/kept-<ts>.json
