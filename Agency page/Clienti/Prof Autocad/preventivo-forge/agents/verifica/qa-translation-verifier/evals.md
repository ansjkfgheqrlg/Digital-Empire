# Evals — qa-translation-verifier

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 happy path | content IT pulito | `(True, [])` |
| E2 residuo | "Rückfahrkamera" non tradotto | `(False, ["... residui tedeschi ..."])` |
| E3 disallineamento | equipment 10→9 | `(False, ["equipment_it non allineato 1:1"])` |
| E4 prezzo nel titolo | "BMW 320d 30.707 €" in title_it | `(False, ["title_it non deve contenere il prezzo"])` |
| E5 anno alterato | specs Anno 2019 vs listing 2020 | `(False, ["specs Anno alterato ..."])` |
| E6 troppi highlight | 7 highlights | `(False, ["highlights_it > 6"])` |

## Metriche
- **Tedesco che passa** = 0 (falsi negativi obiettivo zero).
- **Falsi positivi** minimizzati ma tollerati (costano un'estensione glossario, non un difetto cliente).

## Comando di verifica
`gate_b(ctx, dealer)` su run pulita → `(True, [])`. Verificato su BMW 320d.
