# Tools — op-parser

| Tool | Uso |
|---|---|
| `parser.py` | logica di normalizzazione |
| `common.validate_against_schema` | validazione contro `listing.schema.json` (jsonschema) |
| `common.RunContext` | path `raw.json`/`listing.json`, log/trace |

## Funzioni chiave (`parser.py`)
- `parse(ctx)` — entrypoint.
- `_pick_car_jsonld`, `_from_jsonld`, `_from_dom_attributes`, `_finalize`.
- `_norm(table, value)` (enum DE→IT), `_to_int`, `_to_float` (numeri formato tedesco).

## Mappe
`FUEL_MAP`, `GEARBOX_MAP`, `DRIVE_MAP`. Estendere quando compaiono valori DE nuovi (non bloccante:
il valore originale viene mantenuto se non mappato).
