# wiki-writer - Evals (casi discriminanti)

## EV-01 - Scrittura
- **Input:** note + url
- **Atteso:** note in wiki/sources con front-matter
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Log
- **Input:** ingest
- **Atteso:** riga INGEST in log.md con data
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - No overwrite
- **Input:** nota con nome esistente
- **Atteso:** versionata, non sovrascritta
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Dry-run
- **Input:** --dry-run
- **Atteso:** mostra azioni senza scrivere
- **Voto:** PASS se il criterio sopra e soddisfatto

