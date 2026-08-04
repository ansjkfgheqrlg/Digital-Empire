# Evals — op-parser

## Casi
1. **JSON-LD completo:** raw con Car ld+json → `listing.json` valido, prezzo/km/potenza corretti.
2. **Solo DOM:** raw senza jsonld ma con `attributes` DE → campi popolati da label DE.
3. **Numeri DE:** `28.900 €`→28900 · `12.345 km`→12345 · `100 kW`→power_kw=100, power_hp≈136.
4. **Enum:** `Diesel`→Diesel, `Automatik`→Automatico, `Allrad`→Integrale.
5. **Prezzo mancante:** raw senza prezzo → `price_listed_eur=null` + warning (no crash).
6. **Validazione:** output valida contro `listing.schema.json` (0 `_schema_errors`).
7. **Confine:** `equipment_de`/`description_de` restano in tedesco.

## Stato test
`_to_float` verificato (28.900/12.345/1.234.567/29900). Aggiungere fixture raw.json per e2e del parse.
