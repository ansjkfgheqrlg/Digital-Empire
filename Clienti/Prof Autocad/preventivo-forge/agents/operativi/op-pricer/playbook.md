# Playbook — op-pricer

1. Carica `listing.json`. Se `price_listed_eur` manca → `ValueError` (stop; problema a monte).
2. Prendi `dealer.pricing_resolved` (surcharge_pct, fixed_1, fixed_2).
3. `compute_price` → `breakdown` (listed, surcharge_eur, fixed, final).
4. Nome: usa `listing_it.content.title_it` se presente, altrimenti `make/model/variant` da `listing.json`.
5. `build_title` → `"{nome} {format_eur(final)} €"`.
6. MERGE in `listing_it.json`: scrivi `price` + `_meta.price_by`, **preserva `content`**.
7. Logga `esposto → finale` + `final_title` in trace.

## Checklist handoff
- [ ] `final_eur` intero, coerente con la formula · [ ] `final_title` contiene il prezzo IT + `€`
- [ ] `breakdown` completo (per Gate C) · [ ] `content` NON alterato
