# Evals — update-proposer

## PASS se:
- [ ] Ogni proposal ha: file, section, content_to_add, insert_mode, rollback
- [ ] content_to_add include il tag Memory Empire con data e fonte
- [ ] insert_mode è uno dei 4 validi
- [ ] File target esiste (verificato)
- [ ] Nessun contenuto già presente nella skill (no duplicati)

## FAIL se:
- [ ] content_to_add è un riassunto (< 100 chars per gap non banale)
- [ ] File target non verificato
- [ ] Manca rollback_instruction
- [ ] source_trace non tracciabile
