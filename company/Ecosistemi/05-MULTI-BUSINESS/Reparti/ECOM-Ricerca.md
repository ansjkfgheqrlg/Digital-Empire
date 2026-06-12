> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.3 + 6

# Reparto L2 — ECOM-Ricerca (`MB-ECOM`) ⚠️ DORMIENTE

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-ECOM-RIC · **Priorità:** MEDIA (struttura minima)
**Stato:** DORMIENTE — attivabile solo dopo gate F-MB5 + F-MB6 (dossier §6, fase E1)
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Identificare il prodotto e-commerce più adatto al profilo Multi-Business (sinergia prioritaria:
POD/merch derivato dal Publishing con gli stessi brand_kit e cover). Validare margine e modello
prima di qualsiasi spesa. Unico workflow attivabile ora: `WF-ECOM-PRODUCT` (ricerca pura, zero spesa).

## Stato attuale

- Org documentata ✓
- Agenti definiti ✓
- Namespace `mb/ecom/*` riservato in AgentDB ✓
- Workflow attivi: **solo `WF-ECOM-PRODUCT`** (ricerca prodotto pura, eseguita da Intelligence
  su ordine MB — zero spesa, output = dossier wiki)
- Tutto il resto: **dormiente fino a F-MB7**

## Workflow L3 di competenza

| Workflow | Stato | Output |
|---|---|---|
| `WF-ECOM-PRODUCT` | **ATTIVABILE ora** | Ordine a Intelligence: `{dominio: ecom, output: dossier_wiki}` → dossier prodotto con scorecard (margine, domanda, logistica, rischio, sinergia con MB-PUB) |

## Funzioni L4

| Team | Responsabilità | Stato |
|---|---|---|
| T-product-scout | Ricerca prodotto: analisi mercato, trend domanda, modelli (dropshipping/POD/digitale) | Dormiente (WF-ECOM-PRODUCT è eseguito da Intelligence) |
| T-margin-calculator | Calcolo margine netto per modello e canale (Amazon FBA, Shopify, Etsy, POD) | Dormiente |

## Agenti L5 assegnati

- `mb-ecom-coord` (coordinator, Sonnet) — **dormiente fino a F-MB7**
- `mb-ecom-product-scout` (worker, Sonnet) — **dormiente**

## Fasi future (gate vincolati — dossier §6)

| Fase | Gate di ingresso | Cosa |
|---|---|---|
| E1 | Dossier WF-ECOM-PRODUCT + decisione mb-conductor + ok umano | Scelta modello: dropshipping / POD / digitale (POD agganciato a MB-PUB = sinergia prioritaria) |
| E2 | E1 chiusa, budget approvato | Store MVP: 1 store, ≤10 listing (copy → Marketing, visual → Content-Factory) |
| E3 | E2 live, tracking attivo | Ads test (strategia con Marketing/Advertising) |
| E4 | E3 con unit economics positivi | Fulfillment monitor + scaling |

## Sinergia MB-PUB → MB-ECOM (prioritaria)

La prima incarnazione e-commerce sarà probabilmente **POD/merch derivato dal Publishing**:
- Stesso brand_kit dei libri KDP → rischio minimo, zero nuovi asset
- Cover libri → t-shirt/poster/gadget (Merch by Amazon, Redbubble, Printful)
- Decisione formale nella fase E1 — non anticipare

## KPI (post-attivazione F-MB7)

- Margine netto per ordine: > 30% (soglia minima per sostenibilità)
- Unit economics positivi entro 90gg da E3 (ads test)
- Zero spese prima di E1 approvata (violazione = blocco Cost-Sentinel)
