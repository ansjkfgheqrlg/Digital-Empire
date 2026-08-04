# Tools — qa-extraction-verifier

| Tool | Uso |
|---|---|
| `qa_gate.gate_a(ctx, dealer=None)` | esegue tutti i controlli di estrazione |
| `common.validate_against_schema(obj, "listing.schema.json")` | validazione contratto |
| `common.load_json(path)` | lettura listing.json |
| filesystem `ctx.dir / local_path` | verifica esistenza foto |

## Dipendenze
- `jsonschema` (validazione schema). Se assente, il check schema è saltato con nota (non falso PASS).

## Dati
- Legge: `runs/<id>/listing.json` + file foto in `runs/<id>/foto/`.
- Non scrive nulla (solo verdetto).
