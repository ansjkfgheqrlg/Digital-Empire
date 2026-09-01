# Playbook — intent-classifier

## Step 1 — Scansione URL
Cerca pattern: `https?://[^\s]+`, `youtube.com/watch`, `youtu.be/`, `tiktok.com/@`

## Step 2 — Scansione keywords
Lista completa: ingerisci, guarda, studia, analizza, analizza il video, prendi la formazione, metti nella wiki, vedi questo, scarica, fai il video, carica

## Step 3 — Classificazione
Applica tabella intent types in ordine di priorità.

## Step 4 — Determina piattaforma (se INGEST_LINK)
- youtube.com o youtu.be → "youtube"
- tiktok.com → "tiktok"
- github.com → "repo"
- altro → "web"

## Step 5 — Scrivi handoff
`memory/handoffs/intent-<YYYY-MM-DDTHH-MM-SS>.json`
