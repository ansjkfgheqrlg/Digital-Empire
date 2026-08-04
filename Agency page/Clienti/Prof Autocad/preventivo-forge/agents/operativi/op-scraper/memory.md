# Memory — op-scraper

## Per-run
- `runs/<id>/raw.json` — output grezzo (fonte di verità dell'estrazione).
- `runs/<id>/foto/` — foto scaricate (gitignored).
- `warnings[]` in `raw.json` — tutto ciò che è mancato.

## Cross-run
- `browser-profile/` (gitignored): sessione/consenso mobile.de persistenti → meno blocchi.

## Apprendimento (da riportare a Max)
- Se cambiano i **selettori di consenso** → aggiornare `CONSENT_SELECTORS`.
- Se cambia la **struttura scheda** → aggiornare `GERMAN_LABELS` / estrazione `dt/dd`.
- Se il **CDN foto** cambia pattern → aggiornare `_extract_image_urls`.
Annotare qui data + sintomo + fix applicato.
