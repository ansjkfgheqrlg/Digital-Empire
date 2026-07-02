# Evals — qa-immagini

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 completezza | 26 foto annuncio, 26 su disco | `(True, [])` |
| E2 foto persa | render ne impagina 25 su 26 | `(False, ["foto nel PDF (25) != ..."])` |
| E3 crop | template con `cover` | `(False, ["uso di 'cover' ..."])` |
| E4 file mancante | local_path senza file | `(False, ["foto ... mancante su disco"])` |
| E5 bassa risoluzione | foto 200x150 | `(False, ["... bassa risoluzione"])` |

## Metriche
- **Foto perse che passano** = 0 (R-09 assoluta).
- **Crop non rilevato** = 0.

## Comando di verifica
`gate_img(ctx, dealer)` → `(True, [])`. Verificato su fixture BMW (4 foto, contain).
