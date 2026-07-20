# ADR-MB-001 — API-first con Business Login for Instagram

- **Data:** 2026-07-20
- **Stato:** ATTIVO
- **Decisori:** Chief-Forge / MB Social Director

## Contesto

Il publisher legacy usa Playwright, sessioni browser e selettori Instagram/Drive. È fragile, custodiva password in config e non chiudeva il loop Insights.

## Decisione

Usare Instagram Platform ufficiale con Business Login for Instagram, Graph API v25.0 configurabile, scope core basic/content_publish/insights. Il browser runtime resta fallback non certificato finché il percorso API non supera canary.

## Alternative scartate

- Browser automation primaria — fragile e ad alto rischio credenziali.
- Aggregatore SaaS — costo/dipendenza prima di provarne la necessità.
- Facebook Login for Business — valido, ma richiede Page collegata e non serve al core owner-only attuale.

## Conseguenze

Servono app Business, token, URL media HTTPS e token lifecycle. In cambio: contratti stabili, media id, publishing limit, insights e automazione controllabile.

## Contradiction-check

Coerente con ADR-003: non rimuove il runtime attivo; costruisce e certifica un sostituto prima del cutover.
