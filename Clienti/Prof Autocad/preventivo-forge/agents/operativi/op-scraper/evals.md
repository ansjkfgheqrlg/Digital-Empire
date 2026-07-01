# Evals — op-scraper

## Casi
1. **Manuale su fixture:** HTML mobile.de salvato + foto → `raw.json` con jsonld o attributes, `images>=1`.
2. **Immagini:** n. foto scaricate == n. `image_urls` deduplicate (o warning per le fallite).
3. **Consenso:** su pagina con banner, dopo `_accept_consent` il contenuto principale è presente.
4. **Blocco:** su HTML con marker blocco → `_looks_blocked` True → errore con istruzioni.
5. **JSON-LD assente:** rimuovendo i tag ld+json, `raw.json` ha comunque `dom.attributes` non vuoti.
6. **Fedeltà:** `dom.description`/`equipment` in tedesco, non tradotti.

## Note
Test live mobile.de non deterministico (anti-bot) → usare fixture HTML per la CI. Aggiornare la
fixture quando mobile.de cambia struttura.
