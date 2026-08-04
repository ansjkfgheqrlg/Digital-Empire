# Agente — op-pricer (S4)

- **Tipo:** operativo · **Owner:** Max (Half A) · **Stato:** attivo · **Impl:** `implementation/pricer.py`

## Ruolo
Calcola il **prezzo finale al cliente** e il **titolo** del preventivo, in modo deterministico e
per-concessionaria. È l'autorità unica sul prezzo (la verità che il PDF mostrerà).

## Input
`listing.json.price_listed_eur`, `dealer.pricing_resolved` (`surcharge_pct`, `fixed_1`, `fixed_2`),
opz. `listing_it.json.content` (per nome IT nel titolo).

## Output
`listing_it.json.price` = `{listed_eur, final_eur, final_title, breakdown{...}}` (MERGE: preserva `content`).

## Formula
`finale = round(esposto × (1 + surcharge_pct/100) + fixed_1 + fixed_2)`. Default: 3% + 1500 + 1500.
Verificato: 18.000 → **21.540 €**.

## Confini
- Deterministico e riproducibile: nessuna dipendenza da testo/AI. Solo aritmetica + config dealer.
- Non tocca `content` (Half B). Non decide sconti/trattative: applica la regola del dealer.

## Handoff
`final_title` + `final_eur` a op-pdf-renderer (S5). Ricalcolo indipendente = qa-price-verifier (Gate C).
Vedi `../../../rules/R4-pricing.md`.
