# Playbook — op-parser

1. Carica `raw.json`. Copia `warnings` iniziali.
2. `_pick_car_jsonld` → blocco Car/Vehicle/Product.
3. `_from_jsonld` → marca/modello/prezzo/km/cambio/alimentazione/potenza/porte/posti/anno/colore/VIN/descrizione.
4. `_from_dom_attributes` → riempi i buchi dalle label DE; salva `raw_specs`; estrai kW/PS da "Leistung".
5. `_finalize` → prezzo da testo se manca; deriva kW↔CV; equipment/descrizione dal DOM; marca/modello/variant dal titolo se assenti; collega `images`; aggiungi warning per prezzo/foto/descrizione mancanti.
6. Applica enum DE→IT (alimentazione/cambio/trazione).
7. Salva `listing.json`; `validate_against_schema`; logga esito + `_schema_errors`.

## Checklist handoff
- [ ] `make`, `model`, `price_listed_eur` presenti · [ ] `images` collegate · [ ] schema valido (o errori loggati)
- [ ] `equipment_de`/`description_de` in tedesco (non tradotti) · [ ] numeri sono numeri
