# WF-FUNNEL-EVERGREEN — Lead Magnet → Vendita Continua 365gg

## Reparto: L2-VENDITE-FUNNEL
## Owner: IB-SALES-funnel

## Trigger
Prodotto lanciato almeno una volta con dati reali (il lancio valida l'offerta; l'evergreen la scala). Oppure: decisione di mettere Manuale Claude Code come lead magnet gratuito nel funnel evergreen (gate B1 prerequisito: ruolo funnel deciso).

## Input (payload)
```json
{
  "prodotto_principale": "nome corso/ebook",
  "sales_page_url": "url page",
  "prezzo": "EUR",
  "lead_magnet": "Manuale Claude Code gratuito | altro asset",
  "opt_in_page_url": "url da costruire",
  "sequenza_nurture_n_email": 7,
  "checkout_url": "url checkout",
  "dati_lancio": "conversione lancio precedente (se disponibile)"
}
```

## Pipeline

1. **Lead magnet → Opt-in page**
   - Asset: Manuale Claude Code gratuito (203pp, già pronto) oppure asset da skill `lead-magnets`
   - Opt-in page: promessa chiara (cosa riceve), form minimo (nome + email), design Empire premium
   - GATE: APSOC ≥80 sull'headline opt-in; pagina mobile-first; evento tracking configurato

2. **Sequenza nurture** (skill `emails` + frame Founder Authority Stack Beggiato):
   - 7 email (frequenza: 1 ogni 2 giorni): valore → autorità → case study → obiezione → offerta soft → social proof → offerta diretta
   - Ogni email: 1 idea, 1 CTA (leggi, guarda, vai alla sales page)
   - GATE: APSOC ≥80 per ogni email; nessuna email di pura vendita nelle prime 4

3. **Sales page evergreen**
   - Variante della sales page di lancio: stessa offerta, zero deadline finte, scarcity basata su realtà (prezzo che sale, bonus a esaurimento reale)
   - `IB-COPY-liaison` → MARKETING per stesura → APSOC ≥80 → build empire-premium-style
   - GATE: percorso cliccabile dal click email → checkout in <3 step

4. **Checkout + Order bump + Upsell**
   - Checkout configurato con `IB-SALES-funnel` + T-checkout (PLATFORM)
   - Order bump: prodotto complementare a basso prezzo (es. template pack) — da `pricing` + `paywalls`
   - Upsell post-acquisto: corso avanzato o sessione 1-to-1 (se disponibile)
   - GATE: transazione test reale verde; ricevuta automatica attiva

5. **Tracking eventi**
   - T-tracking configura: pixel opt-in, email open/click, page view sales page, add-to-cart, acquisto, upsell-accept
   - UTM su ogni fonte traffico
   - Dashboard minimo: conversione per step (opt-in rate, open rate email, CTR email, conv rate sales page, AOV)

6. **Post-acquisto → Community**
   - Acquirente → WF-ONBOARDING automatico (IB-COMMUNITY-manager, ≤24h)
   - Community → T-crosssell → segnali cross-sell → AGENCY

7. **Loop ottimizzazione**
   - `IB-SALES-funnel` legge dashboard ogni 2 settimane
   - Identifica step con conversion rate più basso
   - Propone 1 test A/B alla volta (con T-cro-funnel + `ab-testing`)
   - Test girato per almeno 200 visitatori unici prima di decidere il vincitore

## Gate (soglie)
| Gate | Criterio |
|---|---|
| Gate opt-in | APSOC ≥80 headline; tracking configurato |
| Gate nurture | APSOC ≥80 ogni email; nessuna promessa non provata |
| Gate sales page | Percorso ≤3 click; APSOC ≥80; checkout testato |
| Gate tracking | 100% step coperti da evento |
| Gate test A/B | Minimo 200 visitatori per variante prima della decisione |

## Output
Revenue continua + pipeline lead qualificati per AGENCY (senza dipendere dai lanci).
Dashboard attivo con dati reali per ogni step del funnel.

## Dry-run: come si esegue
1. Percorri l'intero funnel come utente anonimo: opt-in → email (usa inbox test) → click → sales page → checkout (transazione simbolica) → accesso corso → benvenuto
2. Verifica che ogni evento di tracking si registri correttamente
3. Stima costo mensile infrastruttura (email tool, hosting, piattaforma) → Cost-Sentinel

## Handoff in uscita
```json
{
  "from": "infobusiness/funnel-evergreen",
  "to": "infobusiness/community",
  "payload": {
    "acquirente_email": "email",
    "prodotto": "nome",
    "fonte": "utm_source",
    "data_acquisto": "timestamp"
  },
  "acceptance_criteria": ["evento acquisto tracciato", "accesso piattaforma configurato in <24h"]
}
```
