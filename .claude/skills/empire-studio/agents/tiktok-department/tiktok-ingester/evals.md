# tiktok-ingester - Evals (casi discriminanti)

## EV-01 - Ingest base
- **Input:** URL TikTok
- **Atteso:** ingest.json con metadata
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Hashtag
- **Input:** video con hashtag
- **Atteso:** hashtag estratti per focus
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Senza subs
- **Input:** TikTok muto
- **Atteso:** procede senza crash
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Geoblock
- **Input:** video bloccato
- **Atteso:** gestito, segnalato
- **Voto:** PASS se il criterio sopra e soddisfatto

