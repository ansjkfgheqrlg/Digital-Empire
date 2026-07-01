# Evals — qa-price-verifier

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 happy path | 26.900, pct3/1500/1500 | ricalcolo 30.707 == dichiarato → `(True, [])` |
| E2 finale manomesso | final_eur=30.000 | `(False, ["prezzo finale non riproducibile ..."])` |
| E3 breakdown incoerente | surcharge_eur errato | `(False, ["surcharge_eur incoerente ..."])` |
| E4 titolo senza prezzo | final_title="BMW 320d" | `(False, ["final_title senza prezzo ..."])` |
| E5 param mancanti | pricing_resolved assente e no breakdown | `(False, ["parametri prezzo incompleti ..."])` |

## Metriche
- **Errori di prezzo che passano** = 0 (obiettivo assoluto).
- **Riproducibilità** = 100% sui casi con dati completi.

## Comando di verifica
`gate_c(ctx, dealer)` → `(True, [])`. Verificato su BMW 320d (30.707 €).
