# Scraper Performance Dashboard

Questo cruscotto traccia lo stato, le prestazioni e la salute del motore di scraping.

## Stato Attuale ed Ultima Run

- **Ultimo Eseguito**: 2026-07-24 (Run con province di Verona, Padova, Vicenza)
- **Stato Generizzazione**: 🟢 Operativo
- **Lead Totali nel Database**: 61 (Run Milano/Bergamo/Brescia) + nuove run
- **Percentuale Priorità ALTA**: ~72% (Filtro `--only-alta` attivo di default)

## Metriche di Performance (KPI)

| KPI | Valore Bench | Stato | Note |
|---|---|---|---|
| Tempo medio / Lead | `~8-12 secondi` | 🟢 | Include i delay di caricamento Playwright e scansione sito |
| Successo bypass cookies | `> 95%` | 🟢 | Selettori aggiornati dei banner cookie |
| Error rate / Timeout | `< 5%` | 🟢 | Gestito tramite timeout di 8s per pane e 15s per feed |
| Deduplica Sheets | `100%` | 🟢 | Controllo telefonico normalizzato pre-inserimento |

## Prossimi Passaggi / Manutenzione
- Monitorare costantemente eventuali modifiche ai selettori di Google Maps (es: `div[role="feed"]` e `div[role="article"]`).
- In caso di picco di CAPTCHA, verificare l'attivazione della modalità `--headed` e l'incremento del jitter nel file `browser.py`.
