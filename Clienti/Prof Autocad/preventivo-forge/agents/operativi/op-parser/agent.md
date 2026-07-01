# Agente — op-parser (S2)

- **Tipo:** operativo · **Owner:** Max (Half A) · **Stato:** attivo · **Impl:** `implementation/parser.py`

## Ruolo
Trasforma `raw.json` (grezzo) nel contratto canonico `listing.json` conforme a
`schema/listing.schema.json`. È il guardiano della qualità strutturale dei dati.

## Input
`runs/<id>/raw.json` (da op-scraper) + `schema/listing.schema.json`.

## Output
`runs/<id>/listing.json` validato (+ `_schema_errors[]` informativo per il conductor).

## Confini
- Normalizza SOLO dati strutturali (numeri, enum tecniche DE→IT: alimentazione/cambio/trazione).
- NON traduce prosa: `description_de` e `equipment_de` restano in tedesco (per op-translator-copy).
- NON calcola prezzi (quello è op-pricer).

## Handoff
Consegna `listing.json` a op-translator-copy (S3, Gael) e op-pricer (S4). Vedi `../../../rules/R2-parsing.md`.
