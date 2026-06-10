# yt-channel-ingester - Evals (casi discriminanti)

## EV-01 - Lista canale
- **Input:** URL canale
- **Atteso:** videos.json con id/titolo/durata
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Screening applicato
- **Input:** lista id selezionati
- **Atteso:** solo quelli ingeriti con subs
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Dedup
- **Input:** playlist con duplicati
- **Atteso:** nessun id ripetuto
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Resilienza
- **Input:** canale con 2 video privati
- **Atteso:** ingeriti gli altri, privati in errors
- **Voto:** PASS se il criterio sopra e soddisfatto

