# Evals — intent-classifier

## PASS se:
- [ ] URL YouTube → INGEST_LINK con confidence >= 0.95
- [ ] "ingerisci questo contenuto" (senza URL) → INGEST_KEYWORD
- [ ] "come funziona Digital Empire?" → QUERY_DE
- [ ] Output sempre JSON valido
- [ ] File handoff sempre scritto

## FAIL se:
- [ ] URL presente ma classified come QUERY_DE o OTHER
- [ ] Output in prosa invece di JSON
- [ ] File handoff non scritto
