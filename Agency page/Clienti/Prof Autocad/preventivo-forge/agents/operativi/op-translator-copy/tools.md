# Tools — op-translator-copy

| Tool | Uso | Note |
|---|---|---|
| `translate_copy.translate(ctx, dealer)` | entrypoint S3 | scrive `content.*`, merge su `listing_it.json` |
| `translate_copy.translate_term(term)` | traduce un optional | frase→parola, umlaut ASCII gestiti |
| `translate_copy.build_specs_it(listing)` | scheda tecnica IT | traduce colore/interni/carrozzeria |
| `translate_copy.build_description_it(...)` | copy descrizione | solo dai fatti |
| `glossary_de_it.PHRASES / WORDS` | dizionario DE→IT | **estendere qui** i termini nuovi |
| `glossary_de_it.looks_german(token)` | rilevamento residui | euristica indipendente (usata anche da Gate B) |

## Dipendenze runtime
- Python 3.11, nessuna libreria esterna obbligatoria per S3 (solo stdlib + moduli locali).
- Arricchimento LLM opzionale: `TRANSLATE_BACKEND=llm` (OFF di default, richiede ok spesa Max).

## Dati
- Legge: `runs/<id>/listing.json`.
- Scrive: `runs/<id>/listing_it.json` (campo `content`).
- Contratto: `schema/listing_it.schema.json` (congelato da Max).
