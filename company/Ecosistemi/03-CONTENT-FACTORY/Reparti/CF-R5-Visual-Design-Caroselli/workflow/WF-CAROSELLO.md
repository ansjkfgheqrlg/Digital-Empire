---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R5 #carosello #swarm #dry-run #canva #render #carousel-factory #ADR-003
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-CAROSELLO — Pipeline Carosello IG

> **Reparto:** CF-R5 Visual & Design / Caroselli · **Area:** Produzione
> **[WRAPPA] carousel-factory — runtime originale non modificato (ADR-003)**
> **Dry-run obbligatorio:** produce copy + prompt a costo zero prima della generazione immagini

---

## Scopo

Produrre caroselli Instagram CF-grade da un `brief.json`: slide copy → swarm fan-out su 3
rami di generazione (Gemini prompt / Canva template / HTML+render.mjs Puppeteer) → gate
GATE-FORMATO e GATE-BRAND → caption + hashtag → deliverable completo per CF-R6.
L'asset più maturo di DE. Il carousel-factory preesistente viene wrappato senza modifica.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN | CF-R5-SLIDECOPY | `brief.json` | `slides-copy.json` + `prompt-set.json` (costo zero) | Copy conforme a formule carousel-factory |
| 1 | Approvazione dry-run | CF-R5-COORD | `slides-copy.json` + `prompt-set.json` | Approvazione scritta o richiesta rework | GATE-COPY preliminare interno (non sostituisce CF-R6-COPY) |
| 2A | Ramo A — Prompt AI | CF-R5-PROMPT | `prompt-set.json` approvato | `03-design/prompts/prompt-NNN.txt` × N slide | Prompt ultra-specifici: stile, palette, composizione |
| 2B | Ramo B — Canva template | CF-R5-CANVA | `slides-copy.json` + brand_template_id | `03-design/canva-export/slide-NNN.png` × N slide | Template coerente con brand_kit |
| 2C | Ramo C — HTML + render.mjs | CF-R5-RENDER | `slides-copy.json` + `brand_kit` | `04-render/PNG/slide-NNN.png` × N slide | Puppeteer render 1080×1350 |
| 2D | Ramo D — Arena Agent Workspace ✅ TESTATO | CF-R5-RENDER (wrapper `caroselli - preventa/`) | brief ricco (prodotto/pain/leve/target/prezzo), non `slides-copy.json` — l'Agent scrive il copy da solo | 8 PNG 4K + `copy.json` in `Arsenale Caroselli/<Prodotto>/` | Struttura fissa 8 slide, non riconfigurabile — vedi ARCHITETTURA.md |
| 3 | GATE-FORMATO | CF-R5-QA | PNG ramo scelto + `brand_kit` | `verdict-formato.json` | 1080×1350 ±2px; ≤8 slide+cover; < 8MB/slide; contrasto ≥4.5:1; safe-area 72px |
| 4 | GATE-BRAND | CF-R5-QA | PNG ramo scelto + `brand_kit` | `verdict-brand.json` | Palette, font, logo conforme brand_kit |
| 5 | Caption + hashtag | CF-R5-CANVA / CF-R4-CAPTION | `slides-copy.json` + brand_kit.voice | `caption.txt` + `hashtag-set.txt` | Caption ≤2.200 char IG; hashtag ≤30; parole_vietate assenti |
| 6 | Handoff CF-R6 | CF-R5-COORD | PNG + caption + state.json gate verdi | `pronto_per_cf_r6: true` | state.json aggiornato con fasi 03-design e 04-render PASS |

---

## Dry-run (passo obbligatorio 0 — costo zero)

Prima di qualsiasi generazione immagine, CF-R5-SLIDECOPY produce a costo zero:

```json
{
  "order_id": "CF-2026-0101",
  "tipo_workflow": "WF-CAROSELLO",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "n_slide": 7,
  "slides_copy": {
    "slide-00-cover": {
      "hook": "Il 90% degli imprenditori sbaglia questo ogni mattina",
      "sottotitolo": "E non ne è consapevole"
    },
    "slide-01": { "titolo": "Errore #1", "corpo": "Iniziare la giornata controllando le notifiche. Questo attiva la modalità reattiva: rispondi agli altri invece di costruire il tuo." },
    "slide-07-cta": { "testo": "Salva questo post. Rileggilo domani mattina prima di toccare il telefono." }
  },
  "prompt_set": {
    "stile_globale": "dark brutale, sfondo #1A1A1A, accenti #E63946, tipografia Anton bold, zero elementi decorativi superflui",
    "slide-00-cover": "Imprenditore silhouette in piedi, sfondo urbano notturno sfocato, overlay rosso #E63946 30%, testo sovraimpresso, nessun volto riconoscibile",
    "slide-01": "Smartphone con notifiche sullo sfondo sfocato, mano che lo afferra, colori dark, overlay rosso leggero"
  },
  "costo_stimato": {
    "ramo_A": "dipende da engine AI scelto; dry-run non genera immagini",
    "ramo_B": "0 crediti (template Canva)",
    "ramo_C": "0 crediti (render.mjs locale)"
  },
  "decisione": "PENDING_APPROVAZIONE_CF-R5-COORD"
}
```

CF-R5-COORD risponde `APPROVATO` (con eventuale ramo preferito) o `REWORK` con specifica.

---

## Fan-out swarm — 3 rami paralleli

Dopo l'approvazione del dry-run, CF-R5-COORD sceglie il ramo (o avvia 2 rami in parallelo
per A/B interno) in base a:

| Criterio | Ramo preferito |
|---|---|
| Brand con Canva brand template validato | **Ramo B** (zero crediti AI, veloce) |
| Slide con immagini fotografiche/drammatiche | **Ramo A** (AI image, crediti engine) |
| Fallback / mock / batch ad alto volume | **Ramo C** (render.mjs, zero crediti, 100% locale) |

I 3 rami sono **indipendenti**: il fallimento di un ramo non ferma gli altri.
In modalità A/B, CF-R5-COORD avvia B + C in parallelo; confronta in passo 3 (GATE-FORMATO)
e consegna il ramo con gate verde (o entrambi se entrambi passano).

---

## Gate di uscita

**GATE-FORMATO (CF-R5-QA, obbligatorio, blocca):**
- Dimensioni: 1080×1350 px ±2px per ogni PNG
- Numero slide: ≤8 slide + 1 cover = ≤9 file totali per ordine singolo
- Peso: < 8 MB per singolo file PNG
- Contrasto testo: rapporto ≥4.5:1 (WCAG AA)
- Safe-area: nessun elemento testuale o logo nei 72px di margine perimetrale

**GATE-BRAND (CF-R5-QA, obbligatorio, blocca — solo se GATE-FORMATO PASS):**
- Palette: colori dominanti corrispondono a brand_kit.visual.palette (primary + accent + bg)
- Font: font visibile corrisponde a brand_kit.visual.font.display + .body
- Logo: presente in slide cover e ultima slide nella posizione brand_kit

Un FAIL su qualsiasi gate → rework strutturato (agente + campo + valore trovato + atteso).
2 rework falliti sullo stesso ordine → entry `cf/failures` + escalation CF-R5-COORD.

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0101",
  "workflow": "WF-CAROSELLO",
  "brand": "mentalita-brutale",
  "ramo_attivo": "B",
  "fasi": {
    "00-dry-run": {
      "stato": "completato",
      "ts": "2026-06-23T09:00:00Z",
      "risultato": "APPROVATO",
      "ramo_scelto": "B"
    },
    "03-design": {
      "stato": "completato",
      "ts": "2026-06-23T09:15:00Z",
      "slides_copy_path": "orders/CF-2026-0101/03-design/slides-copy.json",
      "canva_export_path": "orders/CF-2026-0101/03-design/canva-export/",
      "n_slide_prodotte": 8
    },
    "04-render": {
      "stato": "completato",
      "ts": "2026-06-23T09:20:00Z",
      "png_path": "orders/CF-2026-0101/04-render/PNG/",
      "n_png": 9
    },
    "gate-formato": { "stato": "PASS", "ts": "2026-06-23T09:21:00Z" },
    "gate-brand":   { "stato": "PASS", "ts": "2026-06-23T09:22:00Z" },
    "caption":      { "stato": "completato", "ts": "2026-06-23T09:23:00Z", "caption_path": "orders/CF-2026-0101/caption.txt" },
    "handoff-cf-r6":{ "stato": "in_attesa", "ts": null }
  },
  "n_rework": 0,
  "pronto_per_cf_r6": true
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0101 · brand: mentalita-brutale · formato: carosello-ig · 7 slide + cover

**Passo 0 (dry-run):**
CF-R5-SLIDECOPY genera `slides-copy.json` (8 slide) + `prompt-set.json` (7 prompt AI).
Nessuna immagine generata. CF-R5-COORD approva il copy, sceglie Ramo B (brand template Canva).

**Passo 1:** CF-R5-COORD segnala APPROVATO + ramo: B.

**Passo 2B:** CF-R5-CANVA apre brand template Canva "mentalita-brutale-carosello-v2" →
`perform-editing-operations` per ogni slide (sostituisce testi, mantiene palette/font) →
`export-design` PNG 1080×1350 → 9 file in `03-design/canva-export/`.

**Passo 3 GATE-FORMATO:** CF-R5-QA verifica 9 PNG: tutte 1080×1350 ✓, peso max 4.1MB ✓,
contrasto testo su sfondo dark ≥16:1 ✓, safe-area 72px libera ✓. → PASS.

**Passo 4 GATE-BRAND:** Palette: primary #E63946 rilevato, font Anton rilevato, logo
in cover e CTA → PASS.

**Passo 5:** CF-R5-CANVA esporta la caption dall'ordine. CF-R4-CAPTION aggiunge hashtag
(≤30, aderenti al brand_kit e al topic del carosello).

**Passo 6:** state.json aggiornato. `pronto_per_cf_r6: true`. CF-R6-GATE gestisce GATE-COPY-APSOC.

---

## Esempio operativo REALE — Ramo D (unico eseguito davvero, 2026-08-06)

A differenza dell'esempio sopra (Ramo B, illustrativo — nessun `orders/` esisteva su
disco prima di oggi), questo è un run reale, verificato con screenshot e file scaricati.
Ordine: `CF-2026-PREVENTA-001` · brand: Preventa · vedi
`orders/CF-2026-PREVENTA-001/` per state.json e trace.jsonl completi.

1. Niente dry-run separato: il brief ricco (prodotto, pain point, leve psicologiche,
   target, prezzo, tono) viene mandato direttamente all'Agent Arena, che genera copy
   e visual insieme, slide per slide.
2. Generazione slide 1-2 riuscita, poi `"The AI took too long to respond"` (timeout
   reale lato Arena) — risolto mandando `"continua"`, non un rework CF-R5-QA.
3. 8/8 slide completate, l'Agent chiede conferma "Questo compito è riuscito? Sì/No" —
   confermato Sì.
4. GATE-FORMATO verificato **a mano** (non da CF-R5-QA automatico, non ancora costruito):
   1080×1350 ✓ (upscalate da 4K), 8 PNG ✓, peso 1.27-1.66MB/slide (< 8MB) ✓.
   GATE-BRAND verificato a mano: prezzo €2.000, target import Germania, brand Digital
   Empire in slide 8/8 — coerenti con `brand_kit` Preventa (mai formalizzato in CF-R2,
   solo nella wiki `Preventa_Logica_Completa_Metodo`).
5. Output finale in `Arsenale Caroselli/Preventa/2026-08-06_tempo-perso-import/`
   (non `orders/<id>/04-render/PNG/` — l'Arsenale è la libreria per-prodotto, l'ordine
   traccia lo stato del batch, vedi ARCHITETTURA.md).

**Gap onesto verso lo standard CF-R5**: GATE-FORMATO/GATE-BRAND non sono stati
eseguiti dall'agente `cf-r5-qa` (non ancora costruito come script reale) — verifica
visiva manuale. `brand_kit.json` di Preventa non esiste come file CF-R2 formale.
Handoff a CF-R6 non eseguito (CF-R6 non costruito). Questo run dimostra che il Ramo D
funziona, non che l'intero reparto CF-R5 sia operativo end-to-end.

---

## Connessioni

- [[cf-r5-slidecopy]] · `agenti/cf-r5-slidecopy.md` — produce il dry-run copy passo 0
- [[cf-r5-qa]] · `agenti/cf-r5-qa.md` — esegue GATE-FORMATO e GATE-BRAND bloccanti
- [[cf-r5-canva]] · `agenti/cf-r5-canva.md` — ramo B Canva template
