# Tools — op-scraper

| Tool | Uso |
|---|---|
| Playwright (chromium) | `launch_persistent_context` headless/headful, `goto`, consenso, scroll, `content()` |
| BeautifulSoup + lxml | `extract_from_html`: JSON-LD, immagini, DOM attributes/description/equipment |
| requests | download foto con header `Referer` (3 retry) |
| `common.RunContext` | cartelle, log, trace, `raw.json` path |

## Funzioni chiave (`scraper.py`)
- `scrape(ctx)` — live. `scrape_manual(ctx, html, foto)` — fallback.
- `_fetch_live`, `_accept_consent` (anche iframe), `_scroll_to_load_gallery`, `_looks_blocked`.
- `_build_raw`, `_extract_jsonld`, `_extract_image_urls`, `_extract_dom`, `_download_images`, `_link_local_images`.

## Config (`.env`)
`BROWSER_PROFILE_DIR`, `PLAYWRIGHT_HEADLESS`, `NAV_TIMEOUT_MS`, `USER_AGENT`, `LOCALE`.

## Setup
`pip install -r requirements.txt` + `playwright install chromium`.
