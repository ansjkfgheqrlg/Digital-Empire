# Tools — qa-translation-verifier

| Tool | Uso |
|---|---|
| `qa_gate.gate_b(ctx, dealer=None)` | esegue tutti i controlli di traduzione |
| `glossary_de_it.looks_german(token)` | rilevamento residuo tedesco (indipendente) |
| `qa_gate._specs_consistency(listing, specs_it)` | confronto numeri specs vs sorgente |
| `common.load_json` | lettura listing.json + listing_it.json |

## Indipendenza del rilevamento
`looks_german` NON usa la tabella di traduzione: giudica per umlaut (ä/ö/ü/ß), stopword tedesche e
morfemi tipici. Così un termine "tradotto male" che resta tedesco viene comunque colto.

## Dati
- Legge: `runs/<id>/listing.json`, `runs/<id>/listing_it.json`.
- Non scrive nulla.
