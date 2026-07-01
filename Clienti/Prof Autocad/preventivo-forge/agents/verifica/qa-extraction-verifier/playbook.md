# Playbook — qa-extraction-verifier

## Quando gira
Subito dopo S2 (parsing), prima di S3. Chiamata: `gate_a(ctx, dealer)`.

## Interpretare i risultati
| Issue | Significato | Chi corregge |
|---|---|---|
| `schema: ...` | listing.json non conforme | S2 parser (Max) |
| `price_listed_eur non numerico/mancante` | prezzo non estratto | S1/S2 (parsing prezzo DE) |
| `make/model mancante` | dati identificativi persi | S2 (fallback da titolo) |
| `N foto non presenti su disco` | download foto fallito | S1 scraper (retry/Referer) |
| `description_de vuota` | descrizione non catturata | S1 (selettore) |

## Azione su rosso
1. Ferma la pipeline (non procedere a S3).
2. Riporta le cause all'operatore.
3. Se il blocco è anti-bot/scraping → suggerire fallback `--manual`.

## Riferimento verificato
Run BMW 320d / GLA → Gate A PASS (schema valido, 4 foto su disco, prezzo numerico).
