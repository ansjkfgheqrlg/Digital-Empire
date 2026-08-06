---
Type: SCRIPTS
Status: Active
Tags: #scripts #CF-R5 #visual #carousel-factory #render #gate #resize #canva #ADR-003
Created: 2026-06-23
Last updated: 2026-06-23
---

# Scripts — CF-R5 Visual & Design / Caroselli

> **ADR-003 critico:** carousel-factory e render.mjs non vengono modificati.
> I wrapper aggiungono il layer di parametrizzazione brand_kit e ordine; l'originale
> resta intatto. Qualsiasi fix alla logica di render va in un wrapper, mai nel runtime.

---

## Wrapper asset attivi (ADR-003 — non modificare gli originali)

### `cf-carousel` (wrapper carousel-factory + render.mjs)

**Scopo:** Port parametrizzato del carousel-factory in
`Workfolw crea caroselli à/carousel-factory/`. Espone la capability di render HTML→PNG
con parametri `brand_kit` e `slides-copy.json` invece dei parametri hard-coded
dell'originale.

**[WRAPPA] carousel-factory — runtime originale non modificato**

**Contratto esposto:**
```
render(job)     → avvia render.mjs Puppeteer con template HTML del carousel-factory,
                  iniettando i valori di brand_kit (palette, font) e slides-copy.json
                  (testi per ogni slide); output: PNG 1080×1350 in orders/<id>/04-render/PNG/
check()         → verifica che Node.js + Puppeteer siano disponibili localmente (OK / ERRORE)
estimate(job)   → stima numero file PNG da produrre e tempo stimato (costo: 0 crediti engine)
dry_run(job)    → produce solo slides-copy.json + prompt-set.json senza avviare render.mjs
```

**Parametri aggiuntivi rispetto all'originale:**
- `brand_kit_path` → inietta palette HEX, font family e logo path nei template HTML
- `slides_copy_path` → `orders/<id>/03-design/slides-copy.json` con testi per slide
- `output_dir` → `orders/<id>/04-render/PNG/` invece del path originale fisso
- `n_slide` → numero di slide da renderizzare (1-9 incluso cover)

**Cosa NON fa:**
- Non modifica i file in `carousel-factory/`: né `render.mjs`, né i template HTML, né
  `package.json`, né le configurazioni.
- Non fa upgrade di dipendenze del carousel-factory.
- Non aggiunge nuove funzioni al render.mjs: nuove capability → nuovo wrapper o richiesta
  a 07-FORGE.

---

### `cf-carousel-arena` (wrapper Arena Agent Workspace — Ramo D) ✅ VERIFICATO 2026-08-06

**Scopo:** Wrappa l'Agent workspace già costruito dentro Arena.ai stessa (non nostro
codice — vive lato Arena, raggiunto via UI + chat archiviata "PROMPT INGEGNERIZZATI
PER [ARENA.AI]" + comando `/inizio-generazione`). **Unico ramo di CF-R5 con un output
reale verificato** — vedi `orders/CF-2026-PREVENTA-001/` e [[CP-20260805-013]].

**[WRAPPA] Arena Agent Workspace — asset esterno, non modificabile da qui.**

**Implementazione reale** (fuori da `company/`, per ADR-003 — stesso pattern di
`carousel-factory/`): `SKILL & Agenti/Workflow agency creative/caroselli - preventa/`
- `run_content_factory.py` — apre la chat, attiva/salta `/inizio-generazione`, manda il brief
- `check_status.py` — osservazione pura, quante slide su 8 sono pronte
- `resume_generation.py` — manda "continua" se un timeout Arena blocca la generazione
- `confirm_and_download.py` — conferma "Sì" e scarica il file reale in
  `Arsenale Caroselli/<Prodotto>/<data_topic>/`

**Contratto esposto (informale — non ancora un modulo Python richiamabile da coord):**
```
genera(brief_ricco)  → esegue i 4 script in sequenza, produce 8 PNG + copy.json + zip
check_stato()        → quante slide generate finora, se bloccato su timeout
```

**Differenza strutturale dagli altri rami:** non prende `slides-copy.json` come
input — il brief ricco (testo libero: prodotto, pain point, leve, target, prezzo,
tono) viene mandato direttamente, l'Agent scrive copy e genera visual insieme.
Struttura slide fissa (8: problema/verità/soluzione/come funziona/risultato/
domanda/CTA), non parametrica come gli altri rami.

**Cosa NON fa (ancora):**
- Non è richiamabile come funzione/modulo da `cf-r5-coord` — sono script standalone,
  lanciati a mano da riga di comando.
- Non passa da GATE-FORMATO/GATE-BRAND automatico (`cf-r5-qa` non costruito) — verifica
  manuale finora.
- Non aggiorna `state.json`/`trace.jsonl` in automatico — scritti a mano per l'ordine
  CF-2026-PREVENTA-001.

---

## Script target CF-R5 (da costruire quando i wrapper sono collegati)

### `format-gate-check`

**Scopo:** Esegue GATE-FORMATO su un set di PNG in modo autonomo, senza attivare
l'intero flusso CF-R5-QA. Utile per CF-R5-COORD per verifiche rapide post-render
o per debug di un ramo specifico.

**Input:** cartella PNG + spec formato target (dimensioni, peso max, safe-area)
**Output:** JSON con esito per ogni criterio e per ogni file

**Dipendenza:** libreria di analisi immagine locale (dimensioni da metadata PNG,
peso da filesystem, contrasto via analisi pixel campione)

**Esempio di output:**
```json
{
  "cartella": "orders/CF-2026-0101/04-render/PNG/",
  "formato_target": "ig-carosello",
  "risultati": [
    {
      "file": "slide-00-cover.png",
      "dimensioni":    { "atteso": "1080x1350", "rilevato": "1080x1350", "esito": "PASS" },
      "peso_mb":       { "limite": 8, "rilevato": 3.1, "esito": "PASS" },
      "contrasto":     { "minimo": 4.5, "rilevato": 16.3, "esito": "PASS" },
      "safe_area_px":  { "margine": 72, "violazioni": 0, "esito": "PASS" },
      "verdetto": "PASS"
    },
    {
      "file": "slide-03.png",
      "dimensioni":    { "atteso": "1080x1350", "rilevato": "1080x1350", "esito": "PASS" },
      "peso_mb":       { "limite": 8, "rilevato": 9.2, "esito": "FAIL" },
      "contrasto":     { "minimo": 4.5, "rilevato": 12.1, "esito": "PASS" },
      "safe_area_px":  { "margine": 72, "violazioni": 0, "esito": "PASS" },
      "verdetto": "FAIL",
      "motivo": "peso 9.2MB supera limite 8MB"
    }
  ],
  "verdetto_batch": "FAIL",
  "n_pass": 8,
  "n_fail": 1
}
```

---

### `resize-multiformat`

**Scopo:** Esegue il resize di un asset master verso tutti i formati standard supportati
(ig-carosello, ig-stories, yt-thumbnail, ig-post-quadrato) con crop intelligente e
padding brand_kit.

**Input:** path asset master + lista formati target + brand_slug (per recuperare bg color)
**Output:** varianti PNG nelle sottocartelle per formato; report con dimensioni e pesi

**Logica:**
- Per ogni formato: calcola il crop center-weighted
- Applica padding con `brand_kit.visual.palette.bg` se necessario per aspect ratio incompatibili
- Verifica safe-area dopo il crop (72px per IG carosello; 48px per YT thumb; 150px per stories)
- Segnala se crop taglia elementi logo (analisi margini 15% del bordo)

**Nota:** non applica effetti creativi; è un'operazione geometrica pura. Qualsiasi
richiesta di "migliorare" il visual durante il resize → rifiuto con segnalazione a
CF-R5-COORD. Il resize produce varianti tecniche, non varianti creative.

---

### `canva-export`

**Scopo:** Esporta un design Canva (per ID) in formato PNG alla risoluzione specificata
e lo deposita nel path corretto dell'ordine. Wrapper del comando `export-design` del
MCP Canva con validazione del formato output.

**Input:** design_id Canva + formato (risoluzione) + order_id + cartella destinazione
**Output:** file PNG in `orders/<id>/03-design/canva-export/` + conferma checksum

**Logica:**
- Chiama `export-design` MCP con `format: "png"` e risoluzione target
- Verifica che il file scaricato abbia le dimensioni attese (non sempre garantite da Canva
  se il design ha impostazioni non standard)
- Se dimensioni non conformi → segnala a CF-R5-CANVA per verifica template; non avvia
  il gate su un file con dimensioni sbagliate

**Dipendenza:** MCP Canva attivo con token valido; timeout: 30s per export; al secondo
timeout → segnalazione a CF-R5-COORD + log in `trace.jsonl`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio ADR-003 e layer engine CF-R5
- [[WF-CAROSELLO]] · `workflow/WF-CAROSELLO.md` — usa cf-carousel (Ramo C) e canva-export (Ramo B)
- [[cf-r5-render]] · `agenti/cf-r5-render.md` — esegue il wrapper cf-carousel per il render
