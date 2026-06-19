---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R3 #shortform #ffmpeg #reel #tiktok #shorts #costo-zero
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-SHORTFORM — Montaggio Reel/TikTok/Shorts da Asset Esistenti

> **Reparto:** CF-R3 Produzione Video · **Area:** Produzione
> **Costo engine:** ZERO — ffmpeg locale, nessuna chiamata a engine a crediti
> **Dry-run:** non applicabile (nessuna spesa engine); stima formale uguale a 0 crediti

---

## Scopo

Montare reel, TikTok e YouTube Shorts da asset video e immagini già esistenti nell'ordine
senza generare nuovi asset via engine a crediti. Usa esclusivamente ffmpeg locale. Il gate
è GATE-FORMATO shortform: ≤60s, 9:16, loudness -14 LUFS.

Casi d'uso tipici:
- Clip B-roll esistenti da ordini precedenti → reel 30s con sottotitoli
- Video lungo tagliato in clip ≤60s per Shorts
- Immagini slideshow con voiceover TTS → short form
- Repurposing: video YouTube → clip Instagram reel

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 1 | Asset check | CF-R3-COORD | `orders/<id>/assets/` | lista asset verificati, diritti confermati | asset presenti; nessun copyright non liberato |
| 2 | Stima costo | CF-R3-QUEUE | lista asset + tipo montaggio | `shortform-intent.json` (0 crediti) | stima formale 0 crediti; bypass CF-SENT-COST |
| 3 | Montaggio | CF-R3-EDIT | asset + voiceover (opt) + .srt | `04-render/video/short-NNN.mp4` | loudness -14 LUFS; 9:16; durata ≤60s |
| 4 | Gate interno | CF-R3-QA | short video + brand_kit | `verdict.json` interno | GATE-FORMATO shortform + GATE-BRAND |
| 5 | Handoff CF-R6 | CF-R3-COORD | video + state.json | `pronto_per_cf_r6: true` | state.json aggiornato |

---

## Stima formale (shortform-intent.json)

Anche se il costo è zero, CF-R3-QUEUE produce il documento intent per tracciabilità:

```json
{
  "order_id": "CF-2026-0070",
  "tipo_workflow": "WF-SHORTFORM",
  "dry_run": true,
  "engine_calls": [
    { "engine": "ffmpeg", "tipo": "montaggio-shortform", "crediti_stimati": 0 }
  ],
  "totale_crediti_stimati": 0,
  "nota": "costo zero: ffmpeg locale; bypass CF-SENT-COST per costo zero confermato",
  "asset_esistenti": ["asset-clip-01.mp4", "asset-clip-02.mp4"],
  "diritti_verificati": true
}
```

Il bypass di CF-SENT-COST è automatico solo quando `totale_crediti_stimati = 0` ed è
dichiarato esplicitamente nel documento. Non è un bypass del controllo: è una conferma
documentata che non c'è spesa da approvare.

---

## Gate di uscita GATE-FORMATO shortform (specifico per piattaforma)

| Piattaforma | Durata max | Aspect | Loudness | Note |
|---|---|---|---|---|
| Instagram Reel | 60s | 9:16 | -14 LUFS | safe area titoli 15% bordi |
| TikTok | 180s | 9:16 | -14 LUFS | verifica no watermark altro brand |
| YouTube Shorts | 60s | 9:16 | -14 LUFS | must be ≤60s per classificazione Shorts |

**GATE-BRAND (CF-R3-QA):**
- Logo e palette brand_kit visibili se template brand richiesto
- Nessuna parola_vietata nei sottotitoli
- Nessun asset di brand_kit diverso da quello dell'ordine nel video

---

## Operazioni ffmpeg standard

```bash
# Concat clip esistenti
ffmpeg -f concat -i concat.txt -c copy raw-concat.mp4

# Crop a 9:16 da 16:9 (center crop)
ffmpeg -i raw-concat.mp4 -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920" cropped.mp4

# Subtitle burn-in + loudnorm + output
ffmpeg -i cropped.mp4 -i voiceover.wav \
  -vf "subtitles=srt_file:force_style='Fontname=Anton,PrimaryColour=&Hffffff'" \
  -af "loudnorm=I=-14:TP=-1:LRA=11" \
  -c:v libx264 -c:a aac \
  short-001.mp4

# Trim a ≤60s (se necessario)
ffmpeg -i short-001.mp4 -t 60 short-001-trimmed.mp4
```

CF-R3-EDIT costruisce il comando ffmpeg adatto alle specifiche dell'ordine; questi
sono i template base, non i comandi fissi per ogni ordine.

---

## State machine (state.json)

```json
{
  "order_id": "CF-2026-0070",
  "workflow": "WF-SHORTFORM",
  "fasi": {
    "01-asset-check":   { "stato": "completato", "n_asset": 3, "diritti": "verificati" },
    "02-stima-zero":    { "stato": "completato", "crediti_stimati": 0, "bypass_cf_sent_cost": true },
    "03-montaggio":     { "stato": "completato", "video_path": "04-render/video/short-001.mp4", "durata_s": 38 },
    "04-gate-interno":  { "stato": "completato", "gate_formato": "PASS", "gate_brand": "PASS" },
    "05-handoff-cf-r6": { "stato": "in_attesa" }
  },
  "crediti_consumati": 0
}
```

---

## Esempio operativo

**Ordine:** CF-2026-0070 · brand: mentalita-brutale · 3 clip B-roll esistenti → reel 30s Instagram

1. Asset check: 3 clip in `orders/CF-2026-0070/assets/` → presenti, durata totale 45s, diritti verificati.
2. Stima zero: shortform-intent.json prodotto; 0 crediti; bypass CF-SENT-COST.
3. CF-R3-EDIT:
   - Concat 3 clip (45s) → trim a 30s (taglio dinamico ai punti chiave).
   - Crop 16:9 → 9:16 center crop → scale 1080x1920.
   - Voiceover non richiesto dall'ordine; musica_bg: silenzio.
   - Subtitle burn-in: Anton bianco su righe centrate.
   - Loudnorm: -14 LUFS output.
4. CF-R3-QA: GATE-FORMATO 30s/9:16/-14 LUFS → PASS; GATE-BRAND logo brand in frame finale → PASS.
5. Handoff CF-R6. Crediti consumati: 0.

---

## Connessioni

- [[cf-r3-edit]] · `agenti/cf-r3-edit.md` — agente principale (ffmpeg locale)
- [[cf-r3-qa]] · `agenti/cf-r3-qa.md` — gate interno GATE-FORMATO shortform
- [[cf-r3-coord]] · `agenti/cf-r3-coord.md` — orchestra; verifica asset esistenti
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §3 CF-R3 WF-SHORTFORM
