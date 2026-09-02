# error-triage-controller - Evals (casi discriminanti)

## EV-01 - Triage
- **Input:** lista errori
- **Atteso:** classificati e prioritizzati
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-02 - Critico
- **Input:** errore bloccante
- **Atteso:** priorita' alta + escalation
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-03 - Recovery
- **Input:** errore risolvibile
- **Atteso:** assegnato e risolto
- **Voto:** PASS se il criterio sopra e soddisfatto

## EV-04 - Log
- **Input:** qualunque
- **Atteso:** registrato in memory/errors
- **Voto:** PASS se il criterio sopra e soddisfatto

