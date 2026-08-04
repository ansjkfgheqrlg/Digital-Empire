# Tools — qa-price-verifier

| Tool | Uso |
|---|---|
| `qa_gate.gate_c(ctx, dealer=None)` | ricalcolo indipendente + verifica titolo |
| `dealer.pricing_resolved` | parametri prezzo (surcharge_pct, fixed_1, fixed_2) |
| `common.load_json` | lettura listing.json (esposto) + listing_it.json (price) |

## Formula (riscritta indipendentemente)
```
finale = round(listed × (1 + surcharge_pct/100) + fixed_1 + fixed_2)
```
Prof Autocad: `surcharge_pct=3, fixed_1=1500, fixed_2=1500`. Es.: 26.900 → round(27.707+3.000)=30.707.

## Dati
- Legge: `runs/<id>/listing.json` (`price_listed_eur`), `runs/<id>/listing_it.json` (`price`).
- Non scrive nulla.

## Nota di indipendenza
Il gate NON importa `pricer.compute_price`: ricalcola la formula in loco, così un bug del pricer non
si "auto-conferma".
