# Tools — conductor

| Tool | Uso |
|---|---|
| `run.py` | entrypoint CLI; orchestrazione stage + gate |
| `implementation/common.py` | `RunContext` (run dir, `state.json`, `trace.jsonl`, log, `validate_against_schema`) |
| `implementation/dealers.py` | `load_dealer(id)`, `list_dealers()` (multi-tenant) |
| `implementation/scraper.py` | S1 `scrape(ctx)` / `scrape_manual(ctx, html, foto)` |
| `implementation/parser.py` | S2 `parse(ctx)` |
| `implementation/pricer.py` | S4 `price(ctx, dealer)` |
| `translate_copy` (opz.) | S3 `translate(ctx, dealer)` — Half B |
| `render_pdf` (opz.) | S5 `render(ctx, dealer)` — Half B |
| `qa_gate` (opz.) | gate B/C/D — Half B |

## Config (da `.env`)
`BROWSER_PROFILE_DIR`, `PLAYWRIGHT_HEADLESS`, `NAV_TIMEOUT_MS`, `USER_AGENT`, `LOCALE`,
`PRICE_SURCHARGE_PCT`, `PRICE_FIXED_1`, `PRICE_FIXED_2`.

## Import difensivo
I moduli di Half B si importano con `importlib` (`_optional`): se assenti, lo stage è `skipped`
con nota handoff, non un errore.
