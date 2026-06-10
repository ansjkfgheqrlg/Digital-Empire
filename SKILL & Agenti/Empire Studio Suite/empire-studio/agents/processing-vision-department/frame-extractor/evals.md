# frame-extractor - Evals (casi discriminanti)

## EV-01 - Capitoli
- **Input:** video con capitoli
- **Atteso:** 1 frame per capitolo + manifest
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Senza capitoli
- **Input:** video senza capitoli
- **Atteso:** frame a intervalli regolari
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Frame validi
- **Input:** qualunque
- **Atteso:** PNG non vuoti, size>0
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Manifest
- **Input:** qualunque
- **Atteso:** manifest.json mappa frame->timestamp->capitolo
- **Voto:** PASS se il criterio sopra e soddisfatto

