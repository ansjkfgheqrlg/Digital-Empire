# 🌐 05 — MULTI-BUSINESS

> **Livello:** L1 · **Priorità:** MEDIA-ALTA · **Stato:** parziale (KDP + workflow libri attivi)
> Dossier completo: `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md`

## Missione

Gestire i business paralleli scalabili di Digital Empire: canali passivi e semi-automatizzati
che generano revenue indipendente dall'agency. **Multi-tenant by design** — le pipeline
prodotte qui sono proof concreta per i clienti Content Factory.

## Business units

| Business | Stato | Priorità build |
|---|---|---|
| **Publishing/KDP** | PARZIALE — workflow libri + KDP esistono | P1 |
| **YouTube Automation** | DA COSTRUIRE — canali @Legamidiamore + @dosementale come riferimento | P1 (F7) |
| **E-commerce** | DA COSTRUIRE | P2 |

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Publishing | libri KDP end-to-end: idea → ricerca → scrittura → cover → publish | `Reparti/Publishing/` |
| L2.2 | YouTube Automation | 16-step pipeline: niche → script → voiceover → video → thumbnail → SEO → upload | `Reparti/YouTube/` |
| L2.3 | E-commerce | prodotto → store → ads → fulfillment | `Reparti/Ecommerce/` |

## Workflow principali

- `WF-KDP-LIBRO` — idea ricerca → scrittura AI → formatting → cover → publish Amazon KDP
- `WF-YT-VIDEO` — 16 step: niche research → script → TTS → stock video → montaggio → thumbnail → SEO → upload
- `WF-ECOMM-PRODUCT` — (da costruire in F11)

## Come si collega al Backbone

- **BUS:** invia "proof" (demo canale YT, libro pubblicato) ad AGENCY come materiale di vendita; riceve script/copy da MARKETING; riceve video da CONTENT-FACTORY
- **BRAIN:** namespace `multibusiness/*` — performance canali, revenue KDP, metriche store
- **GOVERNANCE:** QA video (ffprobe 9:16, durata, orientamento) — eredita da AION CF

## Asset esistenti (da migrare in F3)

- `Workflow-libri/` — workflow libri KDP
- `KDP - prodottti digitali/` — materiale KDP
- `SKILL & Agenti/Ecosistema - Content Factory/` — pipeline video adattabile per YT
- `printing-press` (vendor) — per libri

## Canali YouTube di riferimento (da ingestire in Empire Studio — task 7.0/F-MB1)

- @Legamidiamore — NON ancora ingerito
- @dosementale — NON ancora ingerito

⚠️ Ingestione Empire Studio: sessione dedicata (non fare in questa sessione).

*Fonte: `PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md` · Aggiornato: 2026-06-11*
