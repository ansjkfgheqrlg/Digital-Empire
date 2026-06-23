---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R5 #thumbnail #concept #AB-test #resize #CTR #gate
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-THUMBNAIL — Pipeline Thumbnail & Copertine

> **Reparto:** CF-R5 Visual & Design / Caroselli · **Area:** Produzione
> **[WRAPPA] carousel-factory — runtime originale non modificato (ADR-003)**
> **Dry-run:** produce 3 concept testuali a costo zero; zero generazione immagini prima dell'approvazione concept

---

## Scopo

Produrre thumbnail YouTube e copertine visual per ogni video prodotto dal reparto CF-R3,
con varianti A/B per ottimizzazione CTR. Il flusso è: 3 concept testuali → generazione
per il concept approvato → resize A/B → GATE-FORMATO con verifica leggibilità a 10% →
GATE-BRAND → consegna. Il committente sceglie la variante A o B: la scelta va in `cf/patterns`.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | 3 Concept testuali (dry-run) | CF-R5-CONCEPT | `brief.json` (titolo video, angle, emozione, canale) + `brand_kit` | `concept-set.json` (3 concept: A/B/C) | Zero immagini; approvazione concept prima della generazione |
| 1 | Approvazione concept | CF-R5-COORD / committente | `concept-set.json` | Concept selezionato (A, B o C) | Concept approvato prima di avviare generazione |
| 2 | Generazione thumbnail | CF-R5-CANVA (Canva template) o CF-R5-PROMPT → CF-R5-RENDER (AI image) | Concept approvato + brand_kit | `03-design/thumbnail-master.png` (1080×1350 o risoluzione nativa) | Engine coerente con concept type |
| 3 | Resize varianti A/B | CF-R5-RESIZE | `thumbnail-master.png` + formati: `yt-thumbnail` (1280×720) + `ig-stories` (1080×1920) | `04-render/multi-formato/`: 2 formati × 2 varianti = 4 file | Safe-area per formato; nessun crop logo |
| 4 | GATE-FORMATO | CF-R5-QA | 4 varianti PNG + spec piattaforma | `verdict-formato.json` | Leggibilità a 10% (thumbnail ridotta); dimensioni esatte; peso < 2MB per YT thumb |
| 5 | GATE-BRAND | CF-R5-QA | 4 varianti PNG + `brand_kit` | `verdict-brand.json` | Palette, font, logo coerenti brand_kit |
| 6 | Scelta committente + A/B log | CF-R5-COORD | Verdetti PASS + comunicazione committente | `ab-choice.json` + entry `cf/patterns` | Scelta registrata; nessuna thumbnail senza scelta committente |
| 7 | Handoff CF-R3 / CF-R7 | CF-R5-COORD | thumbnail selezionata + state.json | `thumbnail_selezionata_path` in state.json | Pronta per WF-PUBLISH-YT |

---

## Dry-run — 3 concept testuali (passo obbligatorio 0)

CF-R5-CONCEPT produce `concept-set.json` a costo zero:

```json
{
  "order_id": "CF-2026-0110",
  "tipo_workflow": "WF-THUMBNAIL",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "brief": {
    "titolo_video": "Perché il 95% dei business fallisce nei primi 3 anni",
    "angle": "errore-costoso",
    "emozione_target": "shock + chiarezza",
    "canale": "youtube"
  },
  "concepts": [
    {
      "id": "A",
      "nome": "Headline Frontale",
      "composizione": "Numero '95%' in rosso #E63946 grandissimo a sinistra; testo 'fallisce' in bianco bold Anton; sfondo #1A1A1A piatto. Massima leggibilità a dimensione ridotta.",
      "engine_suggerito": "canva",
      "ctr_storico_composizione": "[DM]"
    },
    {
      "id": "B",
      "nome": "Drama Visivo",
      "composizione": "Grafico a linea che crolla (stilizzato, non reale), colore rosso su sfondo dark. Testo headline in basso a contrasto alto. Emozione: dati che fanno paura.",
      "engine_suggerito": "canva",
      "ctr_storico_composizione": "[DM]"
    },
    {
      "id": "C",
      "nome": "Contro-intuitivo",
      "composizione": "Sfondo bianco (inatteso). Logo mentalità brutale in rosso. Testo nero. Singola parola enorme: 'FALLISCE'. Elemento di sorpresa.",
      "engine_suggerito": "canva",
      "ctr_storico_composizione": "[DM]"
    }
  ],
  "costo_generazione": "0 — nessuna immagine generata in questa fase",
  "decisione": "PENDING_APPROVAZIONE_CONCEPT"
}
```

---

## Gate GATE-FORMATO — verifica leggibilità a 10%

La thumbnail YouTube viene visualizzata in dimensioni ridotte (circa 120×68 px nel feed).
Il GATE-FORMATO include la verifica "leggibilità a 10%": CF-R5-QA ridimensiona la thumbnail
al 10% della larghezza originale (128px per 1280×720) e verifica che:
- Il testo principale sia ancora leggibile (caratteri distinguibili).
- Il colore primario del brand sia ancora riconoscibile.
- Il numero o l'elemento centrale (se presente) sia identificabile.

Se la thumbnail supera il gate a piena risoluzione ma fallisce a 10% → FAIL GATE-FORMATO
con specifica "illeggibile a scala ridotta" e suggerimento di aumentare la dimensione del
font principale (unico caso in cui CF-R5-QA fornisce un'indicazione tecnica, non creativa).

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0110",
  "workflow": "WF-THUMBNAIL",
  "brand": "mentalita-brutale",
  "fasi": {
    "00-concept-set": {
      "stato": "completato",
      "ts": "2026-06-23T10:00:00Z",
      "concept_set_path": "orders/CF-2026-0110/03-design/concept-set.json",
      "concept_approvato": "A"
    },
    "02-generazione": {
      "stato": "completato",
      "ts": "2026-06-23T10:10:00Z",
      "thumbnail_master_path": "orders/CF-2026-0110/03-design/thumbnail-master.png",
      "engine": "canva"
    },
    "03-resize": {
      "stato": "completato",
      "ts": "2026-06-23T10:12:00Z",
      "varianti": {
        "yt-thumbnail-A": "orders/CF-2026-0110/04-render/multi-formato/yt-thumbnail/thumbnail-v-A__yt-thumbnail.png",
        "yt-thumbnail-B": "orders/CF-2026-0110/04-render/multi-formato/yt-thumbnail/thumbnail-v-B__yt-thumbnail.png"
      }
    },
    "gate-formato": { "stato": "PASS", "ts": "2026-06-23T10:13:00Z", "leggibilita_10pct": "PASS" },
    "gate-brand":   { "stato": "PASS", "ts": "2026-06-23T10:14:00Z" },
    "ab-choice":    { "stato": "in_attesa", "scelta_committente": null }
  },
  "n_rework": 0,
  "thumbnail_selezionata_path": null
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0110 · brand: mentalita-brutale · YouTube thumbnail per video "95% fallisce"

**Passo 0:** CF-R5-CONCEPT produce 3 concept (A: headline frontale; B: grafico drama; C: sfondo bianco
contro-intuitivo). Nessuna immagine. CF-R5-COORD presenta i concept al committente.

**Passo 1:** Committente sceglie Concept A (headline frontale). Approvazione registrata.

**Passo 2:** CF-R5-CANVA apre template Canva "mentalita-brutale-thumbnail-v1" → modifica testi
("95%" grande, "fallisce", "nei primi 3 anni") → esporta PNG 1280×720.

**Passo 3:** CF-R5-RESIZE produce 2 varianti YT thumbnail (A: layout originale; B: testo leggermente
più grande per test leggibilità ridotta) + variante ig-stories per social.

**Passo 4 GATE-FORMATO:** Dimensioni 1280×720 ✓; peso 187KB ✓ (< 2MB); leggibilità a 10%:
"95%" e "FALLISCE" distinguibili a 128px ✓ → PASS.

**Passo 5 GATE-BRAND:** Palette dark ✓; font Anton ✓; logo → ✓ → PASS.

**Passo 6:** `ab-choice.json` in attesa committente. Scelta comunicata → variante A selezionata.
Entry `cf/patterns`: `{mb × thumbnail × headline-frontale × concept-A-scelto}`.

**Passo 7:** state.json aggiornato con `thumbnail_selezionata_path`. Pronta per WF-PUBLISH-YT.

---

## Connessioni

- [[cf-r5-concept]] · `agenti/cf-r5-concept.md` — produce i 3 concept testuali passo 0
- [[cf-r5-resize]] · `agenti/cf-r5-resize.md` — produce le varianti A/B multi-formato
- [[cf-r5-qa]] · `agenti/cf-r5-qa.md` — esegue GATE-FORMATO (incluso leggibilità 10%) e GATE-BRAND
