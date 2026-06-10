# video-single-ingester - Evals (casi discriminanti)

## EV-01 - Video con capitoli
- **Input:** URL con capitoli
- **Atteso:** chapters popolati in ingest.json
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Video senza capitoli
- **Input:** URL senza capitoli
- **Atteso:** nota per frame a intervalli
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Subs presenti
- **Input:** URL con auto-sub
- **Atteso:** vtt scaricato
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Resilienza
- **Input:** URL restricted
- **Atteso:** gestito senza crash, segnalato
- **Voto:** PASS se il criterio sopra e soddisfatto

