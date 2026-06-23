---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R5 #brand-kit #template #canva #asset #CF-R2 #onboarding
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-BRANDKIT-VISUAL — Pipeline Visual Brand Kit

> **Reparto:** CF-R5 Visual & Design / Caroselli · **Area:** Produzione
> **[WRAPPA] carousel-factory — runtime originale non modificato (ADR-003)**
> **Trigger:** richiesta in ingresso da CF-R2 (WF-BRAND-ONBOARDING o WF-BRAND-MAINTENANCE)

---

## Scopo

Produrre e aggiornare il layer visivo del brand_kit: template Canva per ogni formato
standard, caricamento asset nel workspace Canva del brand, validazione QA dell'intero
visual kit. Output: template funzionanti per tutti i formati standard, asset caricati
con naming convention, `canva_brand_template_ids` aggiornati nel `brand_kit.json`. Questo
workflow è il "fornitore di strumenti" degli altri workflow: WF-CAROSELLO, WF-THUMBNAIL e
WF-GRAFICA-STATICA usano i template prodotti qui.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | Ricezione richiesta da CF-R2 | CF-R5-COORD | `richiesta-brand-visual.json` da CF-R2 con brand_slug + brand_kit.json validato | Conferma ricezione + slot pianificato | brand_kit.json schema completo (CF-R2-QA già ha validato); in assenza → rifiuto con motivo |
| 1 | Upload asset brand | CF-R5-ASSET | `brands/<slug>/assets/` (logo, palette swatch, font preview) | `canva-asset-index.json` aggiornato; asset_id per ogni file | Tutti gli asset caricati con naming convention; zero upload parziali |
| 2 | Creazione template Canva × 4 formati | CF-R5-CANVA | brand_kit.visual (palette, font, logo asset_id) | 4 template Canva con ID: carosello (1080×1350), stories (1080×1920), thumbnail (1280×720), quadrato (1080×1080) | Ogni template ha: palette applicata, font configurati, logo inserito, elemento placeholder testo |
| 3 | Validazione QA template | CF-R5-QA | 4 template Canva (export preview PNG) + brand_kit | `verdict-brand-kit.json` | GATE-BRAND su ogni template: palette, font, logo; 4/4 PASS richiesti |
| 4 | Aggiornamento brand_kit.json | CF-R5-COORD | verdetti PASS + template IDs Canva | `brand_kit.visual.canva_brand_template_ids` aggiornato | brand_kit.json scritto con i 4 template_id; versione patchata con changelog |
| 5 | Notifica CF-R2 | CF-R5-COORD | brand_kit.json aggiornato | `notifica-cf-r2.json` + stato `brand_visual_completato: true` | CF-R2-COORD riceve notifica; brand disponibile per ordini produzione |

---

## Formati template richiesti (standard)

Ogni brand onboardato deve avere template Canva funzionanti per tutti e 4 i formati:

| Formato | Dimensioni | Template name Canva | Uso in CF-R5 |
|---|---|---|---|
| Carosello IG | 1080×1350 px | `<slug>-carosello-v<N>` | WF-CAROSELLO Ramo B |
| Stories/Reel | 1080×1920 px | `<slug>-stories-v<N>` | WF-GRAFICA-STATICA, WF-THUMBNAIL |
| YT Thumbnail | 1280×720 px | `<slug>-thumbnail-v<N>` | WF-THUMBNAIL |
| Post Quadrato | 1080×1080 px | `<slug>-post-quadrato-v<N>` | WF-GRAFICA-STATICA |

Un brand senza tutti e 4 i template non è disponibile per ordini produzione.
Eccezione: brand con un solo canale dichiarato in `brand_kit.canali` → obbligatori
solo i formati pertinenti al canale + template carosello (sempre).

---

## Struttura richiesta in ingresso (da CF-R2)

```json
{
  "tipo": "brand-visual-request",
  "brand_slug": "mentalita-brutale",
  "brand_kit_path": "brands/mentalita-brutale/brand-kit.json",
  "trigger": "WF-BRAND-ONBOARDING",
  "asset_locali_disponibili": [
    "brands/mentalita-brutale/assets/logo-white-horizontal.png",
    "brands/mentalita-brutale/assets/logo-dark-horizontal.png",
    "brands/mentalita-brutale/assets/logo-white-square.png"
  ],
  "priorita": "normale | alta (lancio imminente)",
  "richiesto_da": "CF-R2-COORD",
  "note": "primo onboarding brand; nessun template Canva esistente"
}
```

---

## Gate GATE-BRAND per template

Il GATE-BRAND su template non verifica un PNG prodotto ma il template Canva stesso.
CF-R5-QA esporta un'anteprima PNG di ogni template con testo segnaposto e verifica:

1. **Palette applicata:** colori dominanti corrispondono a `brand_kit.visual.palette` (primary + accent + bg).
2. **Font configurato:** headline usa `brand_kit.visual.font.display`; corpo usa `brand_kit.visual.font.body`.
3. **Logo inserito:** logo del brand presente nella posizione standard (in alto a sinistra o centrato in base al canale).
4. **Testo segnaposto visibile e sostituibile:** il template ha un elemento testo nominato "HEADLINE" e "CORPO" (o equivalente) modificabile via `perform-editing-operations` MCP.

4/4 PASS richiesti. Un template con gate FAIL viene segnalato con specifica del campo
(es. "font.body non configurato: trovato Arial, atteso Inter") e reinviato a CF-R5-CANVA per correzione.

---

## State machine (state.json durante il workflow)

```json
{
  "brand_slug": "mentalita-brutale",
  "workflow": "WF-BRANDKIT-VISUAL",
  "trigger": "WF-BRAND-ONBOARDING",
  "fasi": {
    "00-ricezione": {
      "stato": "completato",
      "ts": "2026-06-23T14:00:00Z",
      "brand_kit_validato": true
    },
    "01-upload-asset": {
      "stato": "completato",
      "ts": "2026-06-23T14:10:00Z",
      "asset_caricati": 3,
      "indice_path": "brands/mentalita-brutale/canva-asset-index.json"
    },
    "02-template-canva": {
      "stato": "completato",
      "ts": "2026-06-23T14:30:00Z",
      "template_ids": {
        "carosello": "DAFzX9kQ5vL",
        "stories": "DAFzX9kQ5vM",
        "thumbnail": "DAFzX9kQ5vN",
        "post-quadrato": "DAFzX9kQ5vO"
      }
    },
    "03-gate-brand-template": {
      "stato": "PASS",
      "ts": "2026-06-23T14:35:00Z",
      "template_pass": 4,
      "template_fail": 0
    },
    "04-brand-kit-update": {
      "stato": "completato",
      "ts": "2026-06-23T14:36:00Z",
      "brand_kit_versione": "1.1"
    },
    "05-notifica-cf-r2": {
      "stato": "completato",
      "ts": "2026-06-23T14:37:00Z",
      "brand_visual_completato": true
    }
  },
  "n_rework": 0,
  "brand_disponibile_per_ordini": true
}
```

---

## Esempio operativo end-to-end

**Richiesta:** CF-R2-COORD · brand: mentalita-brutale · primo onboarding brand

**Passo 0:** CF-R5-COORD riceve la richiesta da CF-R2. Verifica brand_kit.json (schema
completo, palette, font, voice, logo path). Conferma slot.

**Passo 1:** CF-R5-ASSET carica 3 logo PNG su Canva:
- `mentalita-brutale__logo__white-horizontal.png` → asset_id `BAF8x7kQ2mN`
- `mentalita-brutale__logo__dark-horizontal.png` → asset_id `BAF8x7kQ2mP`
- `mentalita-brutale__logo__white-square.png` → asset_id `BAF8x7kQ2mQ`
`canva-asset-index.json` aggiornato.

**Passo 2:** CF-R5-CANVA crea 4 template Canva:
- Carosello 1080×1350: sfondo #1A1A1A, headline Anton bold bianco, accento #E63946, logo bianco in alto sx → template_id `DAFzX9kQ5vL`
- Stories 1080×1920: stesso stile, formato verticale esteso → `DAFzX9kQ5vM`
- Thumbnail 1280×720: sfondo dark, testo grande centrato, accento rosso → `DAFzX9kQ5vN`
- Post Quadrato 1080×1080: layout simmetrico, logo centrale → `DAFzX9kQ5vO`

**Passo 3:** CF-R5-QA esporta anteprima PNG di ogni template → GATE-BRAND × 4:
palette dark + #E63946 ✓, font Anton ✓, logo bianco ✓, elementi testo modificabili ✓ → 4/4 PASS.

**Passo 4:** `brand_kit.json` aggiornato con `canva_brand_template_ids`: 4 ID. Versione 1.1.

**Passo 5:** CF-R5-COORD notifica CF-R2-COORD: brand mentalita-brutale disponibile per ordini produzione.

---

## Connessioni

- [[cf-r5-asset]] · `agenti/cf-r5-asset.md` — passo 1: upload asset su Canva per il brand
- [[cf-r5-canva]] · `agenti/cf-r5-canva.md` — passo 2: crea i 4 template Canva
- [[cf-r5-qa]] · `agenti/cf-r5-qa.md` — passo 3: GATE-BRAND su ogni template prodotto
