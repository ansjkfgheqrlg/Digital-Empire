# R1 — Scraping (S1)

**OBIETTIVO:** recuperare da un annuncio mobile.de tutti i dati grezzi + TUTTE le foto e salvarli
in `runs/<id>/raw.json` + `runs/<id>/foto/`.

**TRIGGER:** `run.py` step 1 (dopo la creazione del RunContext). Script: `implementation/scraper.py`.

**INPUT**
| Campo | Obbligatorio | Esempio |
|---|---|---|
| `ctx.source_url` | sì (modo live) | `https://suchen.mobile.de/auto-inserat/.../456259857.html` |
| `--manual <html>` + `--foto <dir>` | sì (modo fallback) | `annuncio.html`, `./foto` |
| `.env` config | sì | `BROWSER_PROFILE_DIR`, `PLAYWRIGHT_HEADLESS`, `NAV_TIMEOUT_MS`, `LOCALE` |

**OUTPUT:** `raw.json` (`jsonld[]`, `dom{title,price_text,attributes,description,equipment,seller}`,
`image_urls[]`, `images[]`, `warnings[]`) + foto in `runs/<id>/foto/NN.jpg`.

**STEP-BY-STEP**
1. Live: `launch_persistent_context` (profilo persistente → mantiene consenso/cookie) con UA realistico e locale de-DE.
2. `goto(url)` → accetta consenso GDPR (`_accept_consent`, anche in iframe) → attende networkidle → scroll per lazy-load foto.
3. `page.content()` → HTML renderizzato. Se `_looks_blocked()` → errore con istruzioni fallback.
4. `_build_raw`: estrae JSON-LD, URL immagini (JSON-LD `image` → fallback `<img>/srcset`), DOM (titolo, prezzo testo, scheda `dt/dd` + label DE, equipaggiamento).
5. Scarica le foto con header `Referer` (3 retry) → `images[]`.
6. Modo `--manual`: stesso `_build_raw` su HTML salvato; foto collegate da `--foto`.

**GESTIONE ERRORI**
| Errore | Causa | Azione |
|---|---|---|
| Playwright non installato | setup mancante | messaggio: `pip install playwright && playwright install chromium` o usa `--manual` |
| Blocco anti-bot | mobile.de | `PLAYWRIGHT_HEADLESS=false` + consenso manuale (profilo persistente), o `--manual` |
| Foto 403 | hotlink CDN | retry con Referer; se persiste → warning (Gate A valuta) |
| 0 JSON-LD | mobile.de ha cambiato struttura | il parser userà i DOM `attributes`; warning |

**CASI LIMITE:** annuncio senza foto → warning (Gate A blocca); prezzo su richiesta/assente → `price_text=None` (Gate A blocca).

**LOG:** `logs/<run>.log` + `trace.jsonl` (evento `step S1`); `raw.json.warnings[]` per note non bloccanti.
