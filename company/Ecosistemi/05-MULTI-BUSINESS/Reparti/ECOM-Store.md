> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.3 + 6

# Reparto L2 — ECOM-Store (`MB-ECOM`) ⚠️ DORMIENTE

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-ECOM-STORE · **Priorità:** MEDIA (struttura minima)
**Stato:** DORMIENTE — attivabile solo in fase E2 (post gate E1 + budget approvato)
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Setup dello store e-commerce MVP: ≤10 listing iniziali. Il copy è ordinato a Marketing (04),
i visual a Content-Factory (03). Questo reparto gestisce la struttura tecnica dello store e
l'assemblaggio del listing — non produce copy né visual internamente.

## Workflow L3 di competenza

| Workflow | Stato | Output |
|---|---|---|
| `WF-ECOM-STORE` | DORMIENTE (attivabile in E2) | Store configurato, ≤10 listing pubblicati con copy APSOC (Marketing) e visual (CF) |

## Funzioni L4

| Team | Responsabilità | Stato |
|---|---|---|
| T-store-setup | Configurazione store sulla piattaforma scelta (E1): Shopify / Amazon Seller / Etsy / Printful | Dormiente |
| T-listing-ecom | Assemblaggio listing prodotto: copy (da Marketing) + visual (da CF) + pricing + categorie | Dormiente |

## Agenti L5 assegnati

- `mb-ecom-coord` (coordinator, Sonnet) — supervisione (dormiente fino a F-MB7)

## Handoff attesi in fase E2

| Da → A | Contratto |
|---|---|
| MB-ECOM → Marketing (04) | `{brand_kit, icp, formato_copy: product_description + title, framework: APSOC, vincoli_piattaforma: <store>}` |
| MB-ECOM → Content-Factory (03) | `{brand_kit, formato: product_visual, spec: dimensioni_piattaforma, quantità: ≤10}` |
| MB-ECOM → Platform (06) | Se serve tooling custom (integrazione API store, webhook) |

## Gate di attivazione (tutti obbligatori prima di E2)

1. Dossier WF-ECOM-PRODUCT completato (ECOM-Ricerca, fase E1)
2. Scelta modello (dropshipping/POD/digitale) approvata da mb-conductor + ok umano
3. Budget approvato da Cost-Sentinel (Operations, 09)
4. Platform: eventuale tooling store censito nel registry PLATFORM

## Note di progettazione (post E1)

Il modello store sarà scelto in E1. La struttura di questo reparto è intenzionalmente minima:
- **POD (sinergia MB-PUB):** Printful/Merch by Amazon — zero inventory, stesso brand_kit dei libri
- **Digitale:** Gumroad/Shopify Digital — prodotti già esistenti (ebook, corsi) distribuiti qui
- **Dropshipping:** da valutare solo se POD non è applicabile (più complessità operativa)

## KPI (post-attivazione E2)

- Listing pubblicati conformi a copy/visual approvati: 100%
- Tempo setup store → primo listing live: ≤ 5 giorni lavorativi
- Zero store aperti senza gate E1 superato (blocco Cost-Sentinel)
