---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R3 #video-avatar #heygen #talking-head #dry-run #pipeline
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-VIDEO-AVATAR — Pipeline Avatar/Talking-Head HeyGen

> **Reparto:** CF-R3 Produzione Video · **Area:** Produzione
> **[WRAPPA] port parametrizzato di heygen-studio CF Exponium — originale non modificato (ADR-003)**
> **Dry-run obbligatorio Art.4.3:** produce `avatar-intent.json` a costo zero prima del render reale

---

## Scopo

Produrre video avatar/talking-head via HeyGen a partire da script CF-R4. Usato per brand
senza soul-id visivo Higgsfield (es. tutorial, newsletter video, spokesperson). L'avatar è
scelto in coerenza con `brand_kit.voice.tono`; il montaggio finale aggiunge intro/outro e
sottotitoli via ffmpeg.

---

## Prerequisiti

- Script in `orders/<id>/02-copy/script.md` con hook nei primi 3s e CTA (prodotto da CF-R4 WF-SCRIPT)
- `brand_kit.voice.tono` valorizzato per la selezione avatar
- Budget disponibile per crediti HeyGen

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN | CF-R3-QUEUE | `order.json` + script | `avatar-intent.json` (costo zero) | CF-SENT-COST: APPROVATO o BLOCCO |
| 1 | Selezione avatar | CF-R3-AVATAR | `brand_kit.voice.tono` | `avatar_id` + `voice_id` HeyGen | mapping tono→avatar trovato |
| 2 | Render HeyGen | CF-R3-AVATAR | `avatar_id` + script + `voice_id` | `03-design/avatar-raw.mp4` | video_id HeyGen; stato `done` |
| 3 | Montaggio | CF-R3-EDIT | avatar-raw.mp4 + intro/outro + .srt | `04-render/video/video-NNN.mp4` | loudness -14 LUFS; aspect target |
| 4 | Gate interno | CF-R3-QA | video finale + brand_kit | `verdict.json` interno | GATE-FORMATO + GATE-BRAND: PASS |
| 5 | Handoff CF-R6 | CF-R3-COORD | video + state.json | `pronto_per_cf_r6: true` | state.json aggiornato |

---

## Dry-run (passo obbligatorio 0 — Art.4.3)

CF-R3-QUEUE produce `avatar-intent.json` a costo zero prima di qualsiasi render HeyGen:

```json
{
  "order_id": "CF-2026-0060",
  "tipo_workflow": "WF-VIDEO-AVATAR",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "voice_tono": "diretto, brutale, zero fronzoli",
  "script_durata_stimata_s": 52,
  "engine_calls": [
    { "engine": "heygen", "tipo": "avatar-render", "durata_s": 52, "crediti_stimati": 50 },
    { "engine": "ffmpeg", "tipo": "montaggio",                      "crediti_stimati": 0 }
  ],
  "totale_crediti_stimati": 50,
  "budget_disponibile": 100,
  "decisione": "PENDING_APPROVAZIONE_CF-SENT-COST"
}
```

Il `avatar-intent.json` descrive esattamente quale avatar e quale script verranno usati,
permettendo a CF-SENT-COST di valutare costo e appropriatezza prima del render.

---

## Gate di uscita

**GATE-FORMATO (CF-R3-QA):**
- Aspect ratio corretto per canale target
- Durata coerente con script ±5s
- Codec h264 o h265
- Loudness -14 LUFS ±2 dB
- Sottotitoli presenti e sincronizzati (obbligatori per avatar video)

**GATE-BRAND (CF-R3-QA):**
- Avatar coerente con `brand_kit.voice.tono` (verifica mapping avatar_id ↔ tono)
- Nessuna parola_vietata da `brand_kit.voice.parole_vietate` nel testo del video
- Intro/outro con logo e colori brand_kit.visual se presenti nell'ordine

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0060",
  "workflow": "WF-VIDEO-AVATAR",
  "fasi": {
    "00-dry-run":       { "stato": "completato", "risultato": "APPROVATO 50/100 crediti" },
    "01-selezione-avatar": { "stato": "completato", "avatar_id": "av-masc-40-stern", "voice_id": "hg-voice-it-stern-01" },
    "02-render-heygen":  { "stato": "completato", "heygen_video_id": "hg-vid-2026-0060-01", "durata_s": 52 },
    "03-montaggio":     { "stato": "completato", "video_path": "04-render/video/video-001.mp4" },
    "04-gate-interno":  { "stato": "completato", "gate_formato": "PASS", "gate_brand": "PASS" },
    "05-handoff-cf-r6": { "stato": "in_attesa" }
  },
  "crediti_consumati": 47,
  "pronto_per_cf_r6": true
}
```

---

## Differenze chiave rispetto a WF-VIDEO-UGC

| Aspetto | WF-VIDEO-UGC | WF-VIDEO-AVATAR |
|---|---|---|
| Engine principale | Higgsfield (img + motion) | HeyGen (avatar render) |
| Asset base | Immagini 4K + motion clips | Script testo |
| Soul-id | Sì (CF-R3-SOUL) | No (avatar_id invece) |
| Voiceover separato | Sì (CF-R3-VO) | No (TTS integrato HeyGen) |
| Costo engine | image-4k + motion (alto) | avatar-render (medio) |
| Use case | Video emozionale visuale | Tutorial, spokesperson, newsletter video |

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0060 · brand: mentalita-brutale · script 52s · format: 9:16

**Passo 0 (dry-run):** CF-R3-QUEUE stima 50 crediti HeyGen / 100 disponibili. CF-SENT-COST: APPROVATO.

**Passo 1:** CF-R3-AVATAR legge `brand_kit.voice.tono` = "diretto, brutale". Mappa:
→ `avatar_id: av-masc-40-stern`, `voice_id: hg-voice-it-stern-01`.

**Passo 2:** Wrapper `heygen-generate generate({avatar_id, script, voice_id, aspect_ratio: 9:16})`.
→ HeyGen job `hg-vid-2026-0060-01`. Polling → done in 3m08s. avatar-raw.mp4 depositato.

**Passo 3:** CF-R3-EDIT → aggiunge intro 2s (logo brand su nero) + outro 3s (CTA sovrimpresso) →
concat → subtitle burn-in → loudnorm -14 LUFS → video-001.mp4 (57s, 9:16, h264).

**Passo 4:** CF-R3-QA → GATE-FORMATO: 9:16 PASS; 57s PASS (entro 60s); -14.2 LUFS PASS;
GATE-BRAND: avatar_id av-masc-40-stern mappa a tono "diretto brutale" CONFORME.

**Passo 5:** state.json aggiornato; `pronto_per_cf_r6: true`. Crediti: 47/100.

---

## Connessioni

- [[cf-r3-avatar]] · `agenti/cf-r3-avatar.md` — agente principale di questo workflow
- [[cf-r3-queue]] · `agenti/cf-r3-queue.md` — dry-run passo 0
- [[cf-r3-edit]] · `agenti/cf-r3-edit.md` — montaggio post-render
- [[CF-R4-Produzione-Testuale]] · WF-SCRIPT fornitore script prerequisito
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 CF-R3 WF-VIDEO-AVATAR
