# department-lead - Evals (casi discriminanti)

## EV-01 - Video singolo
- **Input:** URL di un video
- **Atteso:** 1 run con ingest.json (id, durata, capitoli, subs)
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Canale con focus
- **Input:** URL canale + focus=design
- **Atteso:** videos.json con solo i video pertinenti, <= max
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Canale senza focus
- **Input:** URL canale
- **Atteso:** selezione per recency/views, cap rispettato
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Video rimosso
- **Input:** URL non valido
- **Atteso:** errore gestito, log in errors, nessun crash
- **Voto:** PASS se il criterio sopra e soddisfatto

