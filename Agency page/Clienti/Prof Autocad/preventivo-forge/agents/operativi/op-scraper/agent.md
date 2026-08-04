# Agente — op-scraper (S1)

- **Tipo:** operativo · **Owner:** Max (Half A) · **Stato:** attivo · **Impl:** `implementation/scraper.py`

## Ruolo
Recupera da mobile.de il contenuto grezzo di un annuncio e TUTTE le foto. È l'unico agente che
tocca la rete/mobile.de. Non interpreta i dati (lo fa op-parser): raccoglie e salva fedelmente.

## Input
`ctx.source_url` (live) oppure `--manual <html>` + `--foto <dir>`; config `.env` (browser, timeout, locale).

## Output
`runs/<id>/raw.json` (`jsonld[]`, `dom{}`, `image_urls[]`, `images[]`, `warnings[]`) + `runs/<id>/foto/NN.jpg`.

## Confini
- Non normalizza (nessuna mappa DE→IT, nessun calcolo). Solo raccolta + download.
- Scarica solo le foto dell'annuncio dato. Nessun'altra richiesta di rete.
- Rileva il blocco anti-bot e lo segnala; non aggira protezioni in modo abusivo.

## Handoff
Consegna `raw.json` a **op-parser** (S2) via file. Vedi `../../../rules/R1-scraping.md`.
