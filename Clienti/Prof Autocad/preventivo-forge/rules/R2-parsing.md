# R2 — Parsing / Normalizzazione (S2)

**OBIETTIVO:** trasformare `raw.json` nel contratto canonico `listing.json` conforme a
`schema/listing.schema.json`. Normalizza SOLO dati strutturali; la prosa resta per Half B.

**TRIGGER:** `run.py` step 2 (dopo S1). Script: `implementation/parser.py`.

**INPUT**
| Campo | Obbligatorio | Note |
|---|---|---|
| `runs/<id>/raw.json` | sì | output di S1 |
| `schema/listing.schema.json` | sì | per validazione |

**OUTPUT:** `runs/<id>/listing.json` (validato). Campo informativo `_schema_errors[]` per il conductor.

**STEP-BY-STEP**
1. `_pick_car_jsonld`: sceglie il blocco JSON-LD `Car`/`Vehicle`/`Product`.
2. `_from_jsonld`: marca/modello/nome, prezzo (`offers.price`), km (`mileageFromOdometer`), cambio, alimentazione, potenza (`vehicleEngine.enginePower`), porte/posti, immatricolazione→anno, colore, VIN, descrizione.
3. `_from_dom_attributes`: riempie i buchi dalle label DE (`Erstzulassung`, `Kilometerstand`, `Leistung`, `Kraftstoff`, `Getriebe`, `Antriebsart`, ...). Conserva `raw_specs`.
4. `_finalize`: prezzo da testo se manca in JSON-LD; deriva kW↔CV; equipment/descrizione dal DOM; marca/modello/variant dal titolo se assenti; collega `images`; aggiunge `warnings`.
5. Mappe enum DE→IT strutturali: alimentazione (Diesel/Benzina/Ibrida/Elettrica/GPL/Metano), cambio (Manuale/Automatico), trazione (Integrale/Anteriore/Posteriore).
6. Valida contro schema → logga errori.

**TEMPLATE numeri DE (`_to_float`):** `28.900 €`→28900 · `12.345 km`→12345 · `1.234.567`→1234567 · gestisce `.` migliaia e `,` decimali.

**GESTIONE ERRORI**
| Errore | Causa | Azione |
|---|---|---|
| `price_listed_eur` nullo | prezzo assente/non parsato | warning; Gate A blocca il pricing |
| schema non valido | campo tipo errato | logga `_schema_errors`; conductor decide (warning) |
| enum non mappata | valore DE nuovo | tiene il valore originale (non blocca) |

**CASI LIMITE:** JSON-LD assente → solo DOM; `equipment_de` vuoto → Half B non avrà dotazioni (warning).

**LOG:** `logs/<run>.log` + `trace.jsonl` (`step S2`); esito validazione schema.
