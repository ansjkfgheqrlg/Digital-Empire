# Evals — qa-extraction-verifier

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 happy path | listing valido, 4 foto su disco | `(True, [])` |
| E2 prezzo mancante | `price_listed_eur=null` | `(False, ["price_listed_eur ..."])` |
| E3 foto fantasma | local_path senza file | `(False, ["N foto non presenti ..."])` |
| E4 schema rotto | campo extra non ammesso | `(False, ["schema: ..."])` |
| E5 descrizione vuota | `description_de=""` | `(False, ["description_de vuota"])` |
| E6 make/model persi | entrambi null | `(False, ["make mancante","model mancante"])` |

## Metriche
- **Falsi PASS** = 0 (obiettivo assoluto: nessun difetto di estrazione passa oltre).
- **Chiarezza issue** = ogni causa comprensibile senza leggere il codice.

## Comando di verifica
`gate_a(ctx, dealer)` su una run valida → `(True, [])`. Verificato su BMW 320d.
