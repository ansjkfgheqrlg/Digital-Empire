# CHECKOUT -- STATO REALE (LOTTO 3 CASSA)

Ultimo aggiornamento: 2026-07-23 (via `python empire/tools/checkout.py --apply`)

## Tier attivo: 2 -- fallback ordine attivo (mailto verso ordine_email)

Il pagamento automatico (Stripe) NON e' ancora collegato. Il gradino attivo oggi e' il modulo d'ordine in pagamento.html: il cliente compila nome ed email, il client di posta si apre precompilato verso l'indirizzo configurato in rails.ordine_email, Max chiude l'ordine manualmente. Non esiste un tier 3: un funnel senza modo di pagare non e' un funnel.

## Rail configurati

| Rail | Attivo | Dettaglio |
|---|---|---|
| stripe_base | NO | MAX: crea Payment Link su Stripe |
| stripe_bump | NO | MAX: crea Payment Link bump su Stripe |
| paypal_me | NO | MAX: handle PayPal.me |
| bonifico | NO | MAX: IBAN |
| ordine_email | SI | max.infoproducer@gmail.com |

## Per raggiungere il Tier 1 (Stripe live)
1. Max crea 2 Payment Link su Stripe (prodotto base e bump order) e incolla i 2 URL in `checkout.config.json` -> `rails.stripe_base.url` e `rails.stripe_bump.url`, con `attivo: true`.
2. Rilancia `python empire/tools/checkout.py --apply`: i bottoni su manuale.html e pagamento.html passano automaticamente da tier 2 a tier 1.
