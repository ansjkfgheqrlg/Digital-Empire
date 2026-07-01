# Memory — op-parser

## Per-run
- `runs/<id>/listing.json` — contratto canonico (fonte di verità per S3/S4/S5).
- `raw_specs` dentro `listing.json` — scheda DE completa per audit/fallback.
- `_schema_errors` + `warnings` — qualità dell'estrazione.

## Cross-run
- Nessuno stato persistente. La logica di mapping vive nel codice (`FUEL_MAP` ecc.).

## Apprendimento (da riportare a Max)
- Valori DE nuovi non mappati → aggiungerli alle mappe enum.
- Campi mobile.de nuovi/utili → estendere lo schema (coordinare: è la cucitura, avvisare Gael).
Annotare qui data + campo + decisione.
