# transcript-processor - Evals (casi discriminanti)

## EV-01 - Pulizia
- **Input:** vtt rumoroso
- **Atteso:** testo leggibile senza duplicati
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Ancore
- **Input:** vtt con cue
- **Atteso:** testo con timestamp preservati
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Assente
- **Input:** nessun vtt
- **Atteso:** limite dichiarato, nessun crash
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Encoding
- **Input:** vtt con accenti
- **Atteso:** nessun mojibake
- **Voto:** PASS se il criterio sopra e soddisfatto

