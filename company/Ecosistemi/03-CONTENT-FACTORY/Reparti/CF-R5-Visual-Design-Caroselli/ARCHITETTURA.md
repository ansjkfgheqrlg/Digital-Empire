---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #CF-R5 #visual #caroselli #produzione
Created: 2026-06-19
Last updated: 2026-06-19
---

# ARCHITETTURA — CF-R5 Visual & Design / Caroselli

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Produzione · **Reparto:** CF-R5
> **ADR-003 SUPREMA:** il `carousel-factory` runtime originale NON si modifica mai — si wrappa solo.

---

## Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (CF-D-LEAD)
│
└── L1-PROD — CAPO AREA PRODUZIONE
    │
    ├── CF-R3 — PRODUZIONE VIDEO
    ├── CF-R4 — PRODUZIONE TESTUALE
    └── CF-R5 — VISUAL & DESIGN / CAROSELLI  ← questo reparto
              CF-R5-COORD riporta a L1-PROD
```

CF-R5-COORD è il punto di contatto verso L1-PROD per ogni escalation, report di stato
e decisione di engine (Canva MCP vs render locale). Non riporta mai direttamente al
CF-Director: usa sempre il canale L1-PROD (separazione gerarchica MEGA-REPARTO ADR-007).

---

## Architettura engine: Canva MCP vs Render Locale

CF-R5 orchestra due engine di produzione paralleli. La scelta è strutturata, non arbitraria:

```
                          [CF-R5-COORD decide engine]
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
   RAMO A                    RAMO B                   RAMO C
   (Prompt AI)             (Canva MCP)            (Render Locale)
          │                         │                         │
CF-R5-PROMPT               CF-R5-CANVA             CF-R5-RENDER
  │                    generate-design          render.mjs Puppeteer
  ▼                    brand-template           HTML→PNG 1080x1350
Gemini / Higgsfield    editing-operations       [WRAPPA carousel-factory]
  immagini             export PNG
  (oggi: collo
   di bottiglia
   segnalato)
```

**Regola di selezione engine (CF-R5-COORD):**
- `brand_kit.visual.canva_brand_template_ids` non vuoto → Ramo B (Canva MCP preferito)
- Brief con stile fotografico o UGC → Ramo A (Gemini/Higgsfield per le immagini di fondo)
- Brief con slide HTML parametriche o brand senza Canva → Ramo C (render locale)
- Batch ≥ 5 caroselli → swarm fan-out su tutti i rami; merge al GATE-FORMATO

**Il ramo C usa `render.mjs` che è parte del `carousel-factory`.
Non si modifica `render.mjs`: si chiama come wrapper esterno. Dichiarazione obbligatoria:
`[WRAPPA] carousel-factory/render.mjs — runtime originale non modificato.`**

---

## Carousel-factory — architettura wrap (ADR-003)

```
carousel-factory/         ← RUNTIME ATTIVO — MAI MODIFICATO (ADR-003)
│  render.mjs             ← chiamato da cf-r5-render come processo esterno
│  brands/                ← seed del registry CF-R2; letto solo in read
│  ...
│
company/03-content-factory/wf-carosello/   ← PATH PULITO (wrappa, non duplica)
│  skill cf-carousel      ← skill wrapper (dichiara il wrapping, non il runtime)
│
company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R5-Visual-Design-Caroselli/
   scripts/               ← wrapper scripts (chiamano carousel-factory come black-box)
   workflow/WF-CAROSELLO.md  ← orchesta il wrap
```

I file v1 in `carousel-factory/` non vengono mai aperti in scrittura. Ogni chiamata
a `render.mjs` passa tramite i wrapper in `scripts/` che aggiungono i parametri
multi-tenant (brand_kit, icp) senza modificare l'input API del runtime originale.

---

## Flusso WF-CAROSELLO (principale)

```
[IN] brief.json da CF-R1 (struttura_formato: slide-deck)
  + brand_kit.json da CF-R2 (palette, font, logo, canva_brand_template_ids)
        │
        ▼
CF-R5-COORD
  Verifica: brand_kit + icp presenti e leggibili
  Sceglie: engine primario in base a brand_kit.visual.canva_brand_template_ids
  Avvia: CF-R5-SLIDECOPY → copy slide
        │
        ▼
CF-R5-SLIDECOPY
  Input: brief.json (angle, hook_type, icp.dolori, vincoli_brand)
  Applica: formule carousel-factory per hook slide 1, body slide 2-N, CTA finale
  Output: slides-copy.json (testo per ogni slide)
  → deposita in orders/<id>/03-design/slides-copy.json
        │
        ▼ [swarm fan-out — 3 rami paralleli]
        │
   RAMO A                          RAMO B                   RAMO C
CF-R5-PROMPT                  CF-R5-CANVA              CF-R5-RENDER
Prompt Gemini/Higgsfield       template brand Canva     HTML+slides-copy.json
per ogni slide del deck        editing operations       → render.mjs Puppeteer
output: prompt-set.json        export 1080x1350         → PNG 1080x1350
                               PNG slide per slide      [WRAPPA carousel-factory]
        │                          │                        │
        └──────────────────────────┴────────────────────────┘
                                   │
                        [merge in orders/<id>/04-render/PNG/]
                                   │
                                   ▼
CF-R5-QA — GATE-FORMATO (BLOCCANTE)
  Controlla: dimensioni 1080x1350 esatte
  Controlla: numero slide ≤ 8 + cover
  Controlla: peso < 8MB per slide
  Controlla: testo leggibile (contrasto sufficiente)
  Controlla: nessun elemento tagliato in safe-area (72px margini)
  PASS → avanza al GATE-BRAND
  FAIL → motivo strutturato → CF-R5-COORD → rework ramo specifico
                                   │
                                   ▼
CF-R5-QA — GATE-BRAND (BLOCCANTE)
  Controlla: palette colori vs brand_kit.visual.palette (hex match ±10%)
  Controlla: font vs brand_kit.visual.font (display e body)
  Controlla: logo presente nella posizione corretta (slide cover e ultima)
  PASS → avanza a CF-R6-GATE per GATE-COPY-APSOC indipendente
  FAIL → motivo strutturato → CF-R5-COORD → rework ramo corretto
                                   │
                                   ▼
CF-R4-CAPTION (o CF-R5-CANVA caption export)
  Produce: caption + hashtag calibrati per canale da brand_kit.voice
                                   │
                                   ▼
[OUT] orders/<id>/04-render/PNG/*.png (cover + N slide)
      orders/<id>/04-render/caption.txt
      state.json aggiornato: fase "04-render" completata
      report-batch: { pezzi_ok, rework, costo_stima, engine_usato }
```

**Dry-run:** produce solo `slides-copy.json` + `prompt-set.json` (ramo A completo)
a costo zero. Nessuna chiamata a Canva MCP né a render.mjs. Si attiva con `dry_run: true`.

---

## State machine dell'ordine (fasi CF-R5)

```
orders/<id>/state.json fasi:
  "03-design": {
    "stato": "completata",
    "timestamp": "<ISO>",
    "owner": "cf-r5-coord",
    "slides_copy_path": "orders/<id>/03-design/slides-copy.json",
    "engine": "canva | render | prompt-ai",
    "n_slide": 8
  },
  "04-render": {
    "stato": "completata | gate-fallito | rework",
    "timestamp": "<ISO>",
    "owner": "cf-r5-render | cf-r5-canva",
    "gate_formato": "PASS | FAIL",
    "gate_brand": "PASS | FAIL",
    "n_rework": 0,
    "PNG_path": "orders/<id>/04-render/PNG/",
    "peso_max_mb": 7.2
  }
```

---

## Topologia swarm per batch

Per ordini con `quantita` ≥ 5:
- CF-R5-COORD fan-out N job carosello indipendenti.
- Ogni job ha il suo ramo engine (assegnato da coord in base a capacità Canva MCP disponibile).
- CF-R5-QA su ogni job indipendentemente: 1 job fallito non ferma gli altri.
- ≥ 3 job falliti per stesso motivo → escalation a L1-PROD con pattern errore.
- CF-SENT-COST approva stima totale PRIMA dell'avvio del batch (Mandato Art.4.3).

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R5`
- [[CF-R2-Brand-Kit-Tenant-Registry]] · fornitore brand_kit e canva_brand_template_ids
- [[CF-R6-QA-Gate]] · GATE-COPY-APSOC indipendente post-produzione
- [[WF-CAROSELLO]] · `workflow/WF-CAROSELLO.md`
