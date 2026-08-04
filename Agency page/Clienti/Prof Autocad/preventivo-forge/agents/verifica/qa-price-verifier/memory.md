# Memory — qa-price-verifier

## Conoscenza persistente
- La formula prezzo è per-concessionaria (`dealer.pricing_resolved`): Prof Autocad = +3% +1500 +1500.
- Namespace memory (se Backbone attivo): `agency/preventivo/qa-price`.

## Lezioni apprese
- 2026-07-01: la vera indipendenza richiede di **riscrivere** la formula nel gate, non importare
  `pricer.compute_price` (altrimenti un bug si auto-conferma).
- Il rischio maggiore è a monte: il prezzo esposto tedesco mal parsato (punto migliaia). Il ricalcolo
  dal `price_listed_eur` è la rete di sicurezza.

## Nota per Prof Autocad
Breakdown NON mostrato al cliente, ma verificato internamente (deve comunque essere coerente).
Se cambiano i parametri prezzo del dealer, aggiornare config + rieseguire Gate C.
