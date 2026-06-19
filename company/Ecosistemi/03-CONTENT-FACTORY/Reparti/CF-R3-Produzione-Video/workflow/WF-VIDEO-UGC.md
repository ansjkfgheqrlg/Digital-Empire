---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R3 #video-ugc #higgsfield #soul-id #dry-run #pipeline
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-VIDEO-UGC — Pipeline Video UGC Higgsfield

> **Reparto:** CF-R3 Produzione Video · **Area:** Produzione
> **[WRAPPA] port parametrizzato di hf-studio CF Exponium — originale non modificato (ADR-003)**
> **Dry-run obbligatorio Art.4.3:** produce `ugc-intent.json` a costo zero prima del render reale

---

## Scopo

Produrre video UGC completi via Higgsfield: soul-id ricorrente del brand → immagini 4K per
ogni scena → clip motion image-to-video → voiceover TTS → montaggio ffmpeg → gate interno.
Output: video pronto per CF-R6 (gate indipendente) e poi CF-R7 (pubblicazione).

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN | CF-R3-QUEUE | `order.json` + lista scene | `ugc-intent.json` (costo zero) | CF-SENT-COST: APPROVATO o BLOCCO |
| 1 | Soul lookup | CF-R3-SOUL | `brand_kit.soul_id` | `soul_id` validato | soul_id coerente con brand_kit |
| 2 | Immagini 4K | CF-R3-IMG | soul_id + scene dal brief | `03-design/scenes/scene-N.png` | risoluzione 4K confermata |
| 3 | Motion clips | CF-R3-MOTION | scene-N.png + motion_preset | `03-design/clips/clip-N.mp4` | durata e risoluzione conformi |
| 4 | Voiceover | CF-R3-VO | testo voiceover dal brief | `03-design/voiceover.wav` | peak < -1 dBFS; no clipping |
| 5 | Montaggio | CF-R3-EDIT | clips + voiceover + .srt | `04-render/video/video-NNN.mp4` | loudness -14 LUFS ±2; aspect target |
| 6 | Gate interno | CF-R3-QA | video finale + brand_kit | `verdict.json` interno | GATE-FORMATO + GATE-BRAND: PASS |
| 7 | Handoff CF-R6 | CF-R3-COORD | video + state.json | `pronto_per_cf_r6: true` | state.json aggiornato |

---

## Dry-run (passo obbligatorio 0 — Art.4.3)

Prima di qualsiasi render, CF-R3-QUEUE produce `ugc-intent.json` a costo zero:

```json
{
  "order_id": "CF-2026-0055",
  "tipo_workflow": "WF-VIDEO-UGC",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "soul_id": "mb-001",
  "n_scene": 4,
  "engine_calls": [
    { "engine": "higgsfield", "tipo": "image-4k", "n_asset": 4, "crediti_stimati": 40 },
    { "engine": "higgsfield", "tipo": "motion",   "n_asset": 4, "crediti_stimati": 80 },
    { "engine": "tts",        "tipo": "voiceover", "durata_s": 45, "crediti_stimati": 0 },
    { "engine": "ffmpeg",     "tipo": "montaggio", "crediti_stimati": 0 }
  ],
  "totale_crediti_stimati": 120,
  "budget_disponibile": 200,
  "decisione": "PENDING_APPROVAZIONE_CF-SENT-COST"
}
```

CF-SENT-COST risponde `APPROVATO` o `BLOCCO`. Senza APPROVATO il render non parte.

---

## Gate di uscita

**GATE-FORMATO (CF-R3-QA, obbligatorio):**
- Aspect ratio corretto per canale target (9:16 reel, 1:1 post, 16:9 YouTube)
- Durata nei limiti piattaforma (IG reel ≤60s, TikTok ≤3min, Shorts ≤60s)
- Codec h264 o h265
- Loudness -14 LUFS ±2 dB
- Sottotitoli sync se richiesti dal brief

**GATE-BRAND (CF-R3-QA, obbligatorio):**
- Soul_id del video corrisponde a `brand_kit.soul_id`
- Palette primaria riconoscibile in ≥5 frame campionati
- Nessuna parola_vietata da `brand_kit.voice.parole_vietate`

Entrambi i gate devono essere PASS. Un FAIL produce rework strutturato con specifica.
2 rework falliti → escalation L1-PROD.

---

## State machine (state.json durante il workflow)

```json
{
  "order_id": "CF-2026-0055",
  "workflow": "WF-VIDEO-UGC",
  "fasi": {
    "00-dry-run":   { "stato": "completato", "ts": "2026-06-19T10:00:00Z", "risultato": "APPROVATO CF-SENT-COST" },
    "01-soul":      { "stato": "completato", "ts": "2026-06-19T10:01:00Z", "soul_id": "mb-001" },
    "02-img-4k":    { "stato": "completato", "ts": "2026-06-19T10:05:00Z", "n_immagini": 4 },
    "03-motion":    { "stato": "completato", "ts": "2026-06-19T10:09:00Z", "n_clip": 4 },
    "04-voiceover": { "stato": "completato", "ts": "2026-06-19T10:10:00Z", "durata_s": 44.8 },
    "05-montaggio": { "stato": "completato", "ts": "2026-06-19T10:12:00Z", "video_path": "04-render/video/video-001.mp4" },
    "06-gate-interno": { "stato": "completato", "ts": "2026-06-19T10:13:00Z", "gate_formato": "PASS", "gate_brand": "PASS" },
    "07-handoff-cf-r6": { "stato": "in_attesa", "ts": null }
  },
  "crediti_consumati": 118,
  "pronto_per_cf_r6": true
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0055 · brand: mentalita-brutale · formato: video-ugc · 1 video 45s reel

**Passo 0 (dry-run):**
- CF-R3-QUEUE stima: 40 (img-4k) + 80 (motion) + 0 (tts) + 0 (ffmpeg) = 120 crediti.
- Budget disponibile: 200. Intent prodotto. CF-SENT-COST: APPROVATO.

**Passo 1:** CF-R3-SOUL → soul_id `mb-001` trovato in `cf/souls`. Coerente con brand_kit.

**Passo 2:** CF-R3-IMG → 4 immagini 4K (scene: ufficio notturno, grafici, scrivania, close-up persona).

**Passo 3:** CF-R3-MOTION → 4 clip motion (slow_zoom_in ×2, fast_push ×2), durata 3-4s/clip.

**Passo 4:** CF-R3-VO → voiceover `it-IT-DiegoNeural` "Non c'è via di mezzo..." → 8.2s → voiceover.wav.

**Passo 5:** CF-R3-EDIT → concat 4 clip (14s raw) + loop su 45s + voiceover + subtitle burn-in → loudnorm -14 LUFS → video-001.mp4 (45.3s, 9:16, h264).

**Passo 6:** CF-R3-QA → GATE-FORMATO: PASS; GATE-BRAND: soul mb-001 CONFORME, palette dark CONFORME.

**Passo 7:** CF-R3-COORD aggiorna state.json → `pronto_per_cf_r6: true`. Crediti consumati: 118/200.

---

## Connessioni

- [[cf-r3-coord]] · `agenti/cf-r3-coord.md` — orchestra questo workflow
- [[cf-r3-queue]] · `agenti/cf-r3-queue.md` — dry-run obbligatorio passo 0
- [[cf-r3-soul]] · `agenti/cf-r3-soul.md` — passo 1
- [[CF-R6-QA-Gate]] · gate indipendente dopo questo workflow
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §5(b) WF-VIDEO pipeline end-to-end
