# Playbook — op-scraper

## Live
1. Avvia contesto persistente (profilo da `.env`), UA + locale de-DE, viewport desktop.
2. `goto(url, domcontentloaded)`. Accetta consenso GDPR (bottone o iframe).
3. Attendi (2.5s + networkidle best-effort). Scroll 6× per il lazy-load foto.
4. `content()` → HTML. Se `_looks_blocked` → errore con istruzioni (headful / `--manual`).
5. `_build_raw`: JSON-LD + URL foto + DOM. Scarica foto (3 retry, Referer). Salva `raw.json`.

## Manuale (fallback)
1. Leggi HTML salvato. 2. `_build_raw` uguale. 3. Collega le foto dalla cartella `--foto`.

## Checklist prima dell'handoff
- [ ] `raw.json` esiste · [ ] almeno 1 foto in `foto/` · [ ] almeno una fonte dati (jsonld o dom.attributes)
- [ ] `price_text` o JSON-LD offers presente (altrimenti warning) · [ ] warnings registrati
