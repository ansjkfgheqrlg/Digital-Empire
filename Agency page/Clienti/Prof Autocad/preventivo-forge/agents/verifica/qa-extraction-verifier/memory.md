# Memory — qa-extraction-verifier

## Conoscenza persistente
- Le cause di blocco ricorrenti indicano dove S1/S2 sono fragili → alimentano il backlog di Half A.
- Namespace memory (se Backbone attivo): `agency/preventivo/qa-extraction`.

## Lezioni apprese
- 2026-07-01: il controllo "foto dichiarate == foto su disco" è essenziale: lo scraper può
  registrare un'immagine e fallirne il download (403 CDN). Senza questo check la gallery a valle
  risulterebbe incompleta senza spiegazione.
- Gate A minimo built-in in `run.py` è più debole (non valida schema né presenza foto su disco):
  questo agente lo estende. Wiring pieno da concordare con Max.

## Nota
Non giudica la qualità del testo tedesco (spetta a Gate B): resta un gate strutturale.
