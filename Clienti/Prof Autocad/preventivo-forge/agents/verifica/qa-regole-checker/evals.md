# Evals — qa-regole-checker

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 tutto ok | run conforme Novacar | R-01…R-14 tutte PASS, `(True, [])` |
| E2 manca logo cover | template senza `logo-only` | R-01 FAIL |
| E3 dati azienda assenti | config senza `legal.vat` | R-03 FAIL |
| E4 prezzo assente | listing_it senza price | R-08 + R-12 FAIL |
| E5 tedesco residuo | content con parola DE | R-11 FAIL (via Gate B) |
| E6 foto tagliate | template `cover` | R-09 FAIL (via qa-immagini) |
| E7 report | qualsiasi run | `regole-check.json` esiste con 14 voci |

## Metriche
- **Regole sacre violate che passano** = 0 (obiettivo assoluto).
- **Copertura** = 14/14 regole valutate a ogni run.

## Comando di verifica
`gate_regole(ctx, dealer)` → `(True, [])` + `regole-check.json`. Verificato: 14/14 PASS su fixture BMW/novacar.
