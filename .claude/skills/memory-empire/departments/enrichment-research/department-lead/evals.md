# Evals — enrichment-research / department-lead

## PASS se:
- [ ] Pipeline completata (tutti e 5 gli agenti invocati in ordine)
- [ ] `enrichment-<run-id>.json` prodotto sempre (anche se 0 skill arricchite)
- [ ] Report all'utente con lista skill arricchite O motivazione "nessun arricchimento"
- [ ] Ogni arricchimento eseguito ha backup su memory/backups/

## FAIL se:
- [ ] Pipeline saltata dopo ingestione
- [ ] Nessun report all'utente
- [ ] skill-enricher invocato senza approvazione permission-guard
- [ ] Arricchimento senza backup
