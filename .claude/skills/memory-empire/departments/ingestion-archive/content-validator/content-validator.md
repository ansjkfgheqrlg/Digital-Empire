# ingestion-archive / content-validator

**Ruolo:** Verifica che il contenuto ingerito sia reale, tracciabile e completo. Gate anti-finto.

## Criteri di validazione
- Almeno 1 frame PNG reale per ogni 30s di video
- Ogni descrizione visiva ancorata a frame-NNN.png
- Transcript presente (VTT o testo estratto)
- video-analysis.md >= 1000 chars per video >5min
- Nessuna frase 'probabilmente' o 'sembra' senza '(✝ inferenza)'

## Output
memory/handoffs/validation-<ts>.json: {validated: true/false, issues: [...]}
