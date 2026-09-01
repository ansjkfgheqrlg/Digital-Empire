# Evals — activation-monitor

## PASS se:
- [ ] Controlla sempre i 3 file (ingest.json, manifest.json, frame-001.png)
- [ ] "confirmed" solo se tutti e 3 presenti
- [ ] "failed" se anche solo 1 mancante
- [ ] JSON output sempre valido

## FAIL se:
- [ ] Dichiara "confirmed" senza verificare i file
- [ ] Non scrive il file handoff
