# Playbook — conductor

## Procedura di run
1. **Init.** Parso args. `load_dealer(--dealer)`. Creo `RunContext` → cartella `runs/<id>/`.
2. **S1 scraping.** `scrape(ctx)` o `scrape_manual`. Su blocco anti-bot → messaggio via manuale, exit 2.
3. **S2 parsing.** `parse(ctx)` → `listing.json`. Registro `_schema_errors` come warning.
4. **GATE A.** Check estrazione (prezzo presente, foto presenti, marca/modello). Rosso → exit 3.
5. **S3 traduci+copy** (se `translate_copy` presente) → `listing_it.json.content`. Altrimenti `skipped`.
6. **GATE B** (se Half B) → traduzione fedele. Rosso → stop.
7. **S4 pricing.** `price(ctx, dealer)` → `listing_it.json.price` + `final_title`. Fail → exit 4.
8. **GATE C** (se Half B) → ricalcolo prezzo indipendente. Rosso → stop.
9. **S5 PDF** (se `render_pdf` presente) → `preventivo_*.pdf`. Altrimenti nota handoff.
10. **GATE D** (se Half B) → PDF completo. Rosso → stop.
11. **Chiusura.** Stampo prezzo finale + percorsi. Stato finale in `state.json`.

## Regola di consegna
Consegno il PDF SOLO se tutti i gate attivi sono verdi. Altrimenti riporto il blocco.

## Retry/fallback (vedi policies.md)
Foto → 3 retry. Stage → 1 retry, poi stop. S1 bloccato → `--manual`.
