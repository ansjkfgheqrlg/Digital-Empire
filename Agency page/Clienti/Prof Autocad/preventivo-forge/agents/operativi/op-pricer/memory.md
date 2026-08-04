# Memory — op-pricer

## Per-run
- `runs/<id>/listing_it.json.price` — prezzo finale + breakdown + titolo (verità del prezzo).
- `_meta.price_by = "op-pricer (Max)"` — tracciamento autore.

## Cross-run
- Nessuno stato mutabile. I parametri prezzo vivono nella config del dealer (`concessionarie/<id>/config.json`).

## Apprendimento (da riportare a Max)
- Se il cliente cambia la regola prezzo (es. gestione IVA, sconti, altra fee) → aggiornare la
  config del dealer e, se serve, `compute_price` + schema `breakdown`. Coordinare con Gate C (Gael).
Annotare qui data + regola vecchia → nuova.
