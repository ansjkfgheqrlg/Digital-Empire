# Tools — op-pricer

| Tool | Uso |
|---|---|
| `pricer.py` | calcolo + titolo + merge |
| `dealers.load_dealer` | parametri prezzo per concessionaria (`pricing_resolved`) |
| `common.RunContext` | path `listing.json` / `listing_it.json`, log/trace |

## Funzioni chiave (`pricer.py`)
- `compute_price(listed, surcharge_pct, fixed_1, fixed_2) -> breakdown`
- `build_title(make, model, variant, final_eur) -> str`
- `format_eur(n) -> "21.540"`
- `price(ctx, dealer) -> price_block` (carica listing, calcola, MERGE in `listing_it.json`)

## Parametri (per dealer, fallback `.env`)
`surcharge_pct` (default 3), `fixed_1` (1500), `fixed_2` (1500).
