---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R5 #grafica-statica #canva #resize #gate #banner #ads
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-GRAFICA-STATICA — Pipeline Grafiche Statiche

> **Reparto:** CF-R5 Visual & Design / Caroselli · **Area:** Produzione
> **[WRAPPA] carousel-factory — runtime originale non modificato (ADR-003)**
> **Scopo:** grafiche one-shot per ads, banner, post singoli non-carosello

---

## Scopo

Produrre grafiche statiche singole (non carosello) per ads, banner, post IG singoli,
grafiche LinkedIn, copertine evento: brief → Canva (brand template o generate-design) →
resize per tutti i formati richiesti dall'ordine → GATE-FORMATO (dimensioni esatte,
peso, margini) → GATE-BRAND → delivery. Pipeline più corta rispetto a WF-CAROSELLO
perché non richiede swarm fan-out multi-ramo né copy multi-slide.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Brief parsing | CF-R5-COORD | `brief.json` (dimensioni, uso, canale, formato) + `brand_kit` | `design-spec.json` (formato, dimensioni, canale, tipo) | Dimensioni riconosciute; brand_kit presente e validato |
| 1 | Generazione grafica master | CF-R5-CANVA | `design-spec.json` + brand_template_id o generate-design | `03-design/grafica-master.png` nella dimensione nativa del template | Colori e font dal brand_kit; zero elementi fuori palette |
| 2 | Resize multi-formato | CF-R5-RESIZE | `grafica-master.png` + lista formati dall'ordine | `04-render/multi-formato/<formato>/` | Safe-area per formato; nessun crop logo o testo principale |
| 3 | GATE-FORMATO | CF-R5-QA | varianti PNG + spec canale target | `verdict-formato.json` | Dimensioni esatte (0px tolleranza per ads); peso sotto soglia piattaforma; margini brand_kit rispettati |
| 4 | GATE-BRAND | CF-R5-QA | varianti PNG + `brand_kit` | `verdict-brand.json` | Palette, font, logo conformi brand_kit |
| 5 | Delivery | CF-R5-COORD | varianti con gate PASS + `order.json` | Asset in `orders/<id>/delivery/` + `manifest.json` | manifest.json completo con lista asset, dimensioni, canale target |

---

## Formati standard supportati

| Formato | Dimensioni | Canale target | Peso max |
|---|---|---|---|
| `ig-post-quadrato` | 1080×1080 px | IG post singolo, LinkedIn post | 8 MB |
| `ig-post-verticale` | 1080×1350 px | IG post verticale | 8 MB |
| `ig-stories` | 1080×1920 px | IG Stories, Reel cover | 8 MB |
| `yt-thumbnail` | 1280×720 px | YouTube thumbnail | 2 MB |
| `fb-banner` | 1200×630 px | Facebook/LinkedIn banner, OG image | 4 MB |
| `display-banner-300x250` | 300×250 px | Display ads standard | 150 KB |
| `display-banner-728x90` | 728×90 px | Leaderboard display ads | 150 KB |

Se l'ordine richiede un formato non in lista → CF-R5-COORD segnala a CF-R2-COORD per
valutazione aggiunta al registry; non improvvisa dimensioni.

---

## GATE-FORMATO — specifiche per WF-GRAFICA-STATICA

La grafica statica ha tolleranze più strette del carosello perché spesso va su piattaforme
ads con specifiche millimetriche:

- **Dimensioni:** 0px tolleranza (per formati ads); ±2px per formati social (come WF-CAROSELLO).
- **Peso:** sotto soglia per formato (tabella sopra); per display ads la soglia è molto bassa (150 KB).
- **Margini brand_kit:** elementi testuali e logo rispettano i margini dichiarati in
  `brand_kit.visual.margini` (se assenti: 60px default).
- **Safe-area display:** per banner display: area "cliccabile" centrata con almeno 20px
  di margine dagli edge (alcuni ad network troncano i bordi).

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0120",
  "workflow": "WF-GRAFICA-STATICA",
  "brand": "brand-agency",
  "uso": "ads-facebook",
  "fasi": {
    "00-design-spec": {
      "stato": "completato",
      "ts": "2026-06-23T11:00:00Z",
      "design_spec_path": "orders/CF-2026-0120/03-design/design-spec.json",
      "formati_target": ["fb-banner", "ig-post-quadrato"]
    },
    "01-generazione": {
      "stato": "completato",
      "ts": "2026-06-23T11:08:00Z",
      "grafica_master_path": "orders/CF-2026-0120/03-design/grafica-master.png",
      "engine": "canva"
    },
    "02-resize": {
      "stato": "completato",
      "ts": "2026-06-23T11:10:00Z",
      "varianti": {
        "fb-banner": "orders/CF-2026-0120/04-render/multi-formato/fb-banner/grafica__fb-banner.png",
        "ig-post-quadrato": "orders/CF-2026-0120/04-render/multi-formato/ig-post-quadrato/grafica__ig-post-quadrato.png"
      }
    },
    "gate-formato": { "stato": "PASS", "ts": "2026-06-23T11:11:00Z" },
    "gate-brand":   { "stato": "PASS", "ts": "2026-06-23T11:12:00Z" },
    "delivery":     { "stato": "completato", "ts": "2026-06-23T11:13:00Z", "manifest_path": "orders/CF-2026-0120/delivery/manifest.json" }
  },
  "n_rework": 0,
  "consegnato": true
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0120 · brand: brand-agency · grafica ads Facebook + post IG quadrato
per promozione Content Factory

**Passo 0:** CF-R5-COORD legge brief: `uso: ads-facebook`, `formati: [fb-banner, ig-post-quadrato]`,
`brand_kit: brands/brand-agency/brand-kit.json`. Design-spec.json prodotto.

**Passo 1:** CF-R5-CANVA apre brand template "brand-agency-ads-v1" in Canva → modifica
testi (headline "Content Factory — 90 giorni" + subline "da 0 a pipeline completa") →
aggiunge logo brand-agency in alto a sinistra → esporta PNG 1200×630 (formato master).

**Passo 2:** CF-R5-RESIZE produce:
- `fb-banner` 1200×630: crop zero necessario (è il master) → peso 287KB ✓
- `ig-post-quadrato` 1080×1080: crop center, padding bg #FFFFFF 135px top+bottom → peso 312KB ✓

**Passo 3 GATE-FORMATO:** fb-banner: 1200×630 esatti ✓, 287KB < 4MB ✓, margini 80px ✓.
ig-post-quadrato: 1080×1080 ✓, 312KB < 8MB ✓ → PASS.

**Passo 4 GATE-BRAND:** Palette brand-agency #004AAD ✓, font Montserrat ✓, logo ✓ → PASS.

**Passo 5:** Manifest.json: `{asset: [fb-banner.png, ig-post-quadrato.png], brand: brand-agency,
uso: ads-facebook, gate: PASS}`. Delivery in `orders/CF-2026-0120/delivery/`. Committente (01-AGENCY) notificato.

---

## Connessioni

- [[cf-r5-canva]] · `agenti/cf-r5-canva.md` — generazione grafica master passo 1
- [[cf-r5-resize]] · `agenti/cf-r5-resize.md` — declinazioni multi-formato passo 2
- [[cf-r5-qa]] · `agenti/cf-r5-qa.md` — GATE-FORMATO e GATE-BRAND bloccanti
