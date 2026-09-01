# Playbook — routing-dispatch / department-lead

## Step 1 — Ricezione input
- Ricevi messaggio utente + sessione corrente
- Annota timestamp di arrivo
- Prepara file input per intent-classifier

## Step 2 — Classificazione intento
- Passa a intent-classifier: messaggio + URL estratti + keywords
- Aspetta `memory/handoffs/intent-<timestamp>.json`
- Timeout: 10 secondi (se non arriva, classifica manualmente come INGEST se c'è un URL)

## Step 3 — Routing
- Leggi `intent_type` dal JSON di classificazione
- Mappa su routing-map.md per il workflow target
- Passa a workflow-router con `{classification: ..., action: "activate"}`
- Aspetta `memory/handoffs/routing-result-<timestamp>.json`

## Step 4 — Monitor attivazione
- Passa a activation-monitor: `{workflow: ..., activation_time: ...}`
- Aspetta `memory/handoffs/monitor-result-<timestamp>.json`
- Se `status: "confirmed"` → procedi
- Se `status: "failed"` → attiva workflow manualmente con istruzione esplicita

## Step 5 — Re-attivazione manuale (se fallisce)
```
Se Empire Studio non è partito:
  1. Leggi SKILL.md in empire-studio/
  2. Esegui: python scripts/yt_ingest.py --input <URL> --run <run-id>
  3. Esegui: python scripts/frame_extractor.py --run <run-id> --interval 2
  4. Procedi con la visione dei frame
  NOTA: Non aspettare. Fallo tu direttamente.
```

## Step 6 — Log
- Scrivi `memory/routing/routing-<YYYY-MM-DDTHH-MM-SS>.json`:
  ```json
  {
    "timestamp": "...",
    "input_summary": "...",
    "intent_type": "...",
    "workflow_activated": "...",
    "activation_status": "confirmed|failed|manual",
    "notes": "..."
  }
  ```

## Step 7 — Report al Conductor
- Testo breve: "Routing completato. Workflow: Empire Studio. Stato: attivo. Run-id: ..."
