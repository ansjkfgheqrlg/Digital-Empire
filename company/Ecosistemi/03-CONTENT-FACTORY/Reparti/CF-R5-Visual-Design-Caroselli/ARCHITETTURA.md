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

## Architettura engine: Canva MCP vs Render Locale vs Arena Agent Workspace

CF-R5 orchestra quattro engine di produzione paralleli. La scelta è strutturata, non
arbitraria.

> **⚠️ AGGIORNAMENTO STATO REALE — 2026-08-27 (CP-20260825-003).** Il quadro qui sotto
> è cambiato: **il Ramo C è vivo e ha il primo ordine eseguito**
> (`orders/CF-2026-PREVENTA-002/`), **il Ramo D è fermo**.
>
> | Ramo | Stato al 2026-08-06 | Stato oggi |
> |---|---|---|
> | C (render locale) | mai eseguito | ✅ **operativo**, primo ordine reale, gate automatico |
> | D (Arena browser) | unico verificato | ⛔ **fermo su questa macchina** |
>
> Perché il Ramo D è fermo (verificato, non presunto): `playwright_stealth` non è
> installato quindi ogni script muore all'import; `ArenaAI/session_data/` non esiste e
> serve un login Google interattivo (la cartella è gitignorata, quindi non arriva col
> repo); e anche funzionando richiede sorveglianza umana per ogni run (attesa, controllo
> stato a mano, eventuale resume, download separato). Non è stato smontato niente: resta
> raggiungibile con `--engine arena`, che oggi esce con un errore che spiega cosa manca.
>
> Il Ramo C ha inoltre richiesto **3 bug fix reali** nel runtime `carousel-factory`
> (font mai caricati, parole incollate, screenshot prima dei webfont): vedi
> `## Carousel-factory` più sotto e il checkpoint.

**Stato al 2026-08-06** (storico, lasciato per contesto): Rami A/B/C progettati ma mai
eseguiti, Ramo D unico verificato con un output reale (primo carosello Preventa,
[[CP-20260805-013]]) — vedi `orders/CF-2026-PREVENTA-001/`.

```
                          [CF-R5-COORD decide engine]
                                    │
     ┌──────────────┬───────────────┼───────────────┬──────────────┐
     │              │               │               │
  RAMO A          RAMO B          RAMO C          RAMO D
 (Prompt AI)     (Canva MCP)   (Render Locale)  (Arena Agent Workspace)
     │              │               │               │
CF-R5-PROMPT    CF-R5-CANVA    CF-R5-RENDER    [WRAPPA Arena Agent Mode]
  │           generate-design  render.mjs      chat archiviata
  ▼           brand-template   Puppeteer       "PROMPT INGEGNERIZZATI"
Gemini /      editing-ops      HTML→PNG        + comando /inizio-generazione
Higgsfield    export PNG       1080x1350       → 8 slide 4K + copy.json + ZIP
immagini      [WRAPPA carousel-factory]        [WRAPPA caroselli - preventa/*.py]
(mai testato) (mai testato)    (mai testato)   ✅ TESTATO — Preventa 2026-08-06
```

**Regola di selezione engine (CF-R5-COORD):**
- `brand_kit.visual.canva_brand_template_ids` non vuoto → Ramo B (Canva MCP preferito)
- Brief con stile fotografico o UGC → Ramo A (Gemini/Higgsfield per le immagini di fondo)
- Brief con slide HTML parametriche o brand senza Canva → Ramo C (render locale)
- **Brief con struttura fissa a 8 slide (problema/verità/soluzione/come funziona/
  risultato/domanda/CTA) e brand senza asset Canva pronti → Ramo D (default oggi,
  unico verificato)**
- Batch ≥ 5 caroselli → swarm fan-out su tutti i rami; merge al GATE-FORMATO

**Il ramo C usa `render.mjs` che è parte del `carousel-factory`.
Non si modifica `render.mjs`: si chiama come wrapper esterno. Dichiarazione obbligatoria:
`[WRAPPA] carousel-factory/render.mjs — runtime originale non modificato.`**

> **Nota 2026-08-27**: il file reale si chiama `scripts/render.js` (non `render.mjs`, che
> non è mai esistito con quel nome). Il comando `caroselli.py` lo invoca come processo
> esterno (`node scripts/generate.js <piano.json>`), quindi il wrap regge. **Ma il
> runtime È stato modificato**, e va dichiarato invece di far finta: `render.js` aveva
> tre difetti che rendevano ogni slide sbagliata in silenzio (font mai caricati per
> policy di origine su `page.setContent`, parole incollate dallo split sull'accent,
> screenshot scattato prima dei webfont). Erano bug, non personalizzazioni: ADR-003
> vieta di duplicare o riscrivere un runtime, non di ripararlo. Nessuna logica di
> business toccata.

### Ramo D — Arena Agent Workspace (dettaglio, ADR-003 wrap)

Non un motore nuovo: **wrappa** un Agent workspace già costruito dentro Arena stessa
(non in questo repo — vive lato Arena, raggiungibile solo via UI). Il wrapper locale
(`caroselli - preventa/*.py`, in
`SKILL & Agenti/Workflow agency creative/`, fuori da `company/` per ADR-003 — stesso
pattern di `carousel-factory/`, mai duplicato dentro `company/Ecosistemi/`) pilota
questo workspace via Playwright:

1. Apre `arena.ai` → Search → tab Archived → chat **"PROMPT INGEGNERIZZATI PER
   [ARENA.AI]"** (asset esterno, non nostro — di proprietà dell'account Arena).
2. Scrive `/inizio-generazione` (se non già attivo).
3. Manda un brief ricco (prodotto, pain point, leve, target, prezzo, tono — NON un
   one-liner, l'Agent non ha contesto di suo).
4. L'Agent genera 8 slide fisse (struttura non configurabile: IL PROBLEMA, LA VERITÀ,
   LA SOLUZIONE, COME FUNZIONA, IL RISULTATO, LA DOMANDA VERA, INIZIA ORA) + copy.json
   + ZIP, con eventuali timeout risolti mandando "continua".
5. Il wrapper scarica il file reale (non si fida del testo "pronto" in chat) e lo
   deposita in `Arsenale Caroselli/<Prodotto>/<data_topic>/` (libreria output finiti,
   parallela a `orders/` — vedi nota sotto).

**Limite noto**: struttura a 8 slide fissa, non parametrica come i Rami A/B/C — va bene
per un formato "advertorial" standard, non per format custom (es. thumbnail singola,
grafica statica). Per quei casi restano i Rami A/B/C, quando verranno costruiti.

**`orders/` vs `Arsenale Caroselli/`**: `orders/<id>/` è il tracking per-ordine
(WIP, state machine, gate) coerente con lo schema CF-R5 esistente. `Arsenale Caroselli/`
(`SKILL & Agenti/Workflow agency creative/Arsenale Caroselli/`) è la libreria degli
output FINITI per prodotto, indipendente da quale ordine/ramo li ha generati — un
carosello passato dal Ramo D finisce in entrambi i posti: lo stato in `orders/`, il
file finale nell'Arsenale.

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
