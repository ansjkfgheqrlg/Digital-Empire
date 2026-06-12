> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 5 (registry engine — ffmpeg)

# T-FFMPEG — Engine FFmpeg (Montaggio, Cut, Crop, Subtitle, Audio)

> Layer engine condiviso · Livello: L4 · Usato da: CF-R2 (montaggio video)
> Fonte: dossier 03 §5, §4b.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità engine

| Campo | Valore |
|---|---|
| Engine ID | ffmpeg |
| Capability servite | montaggio, cut, crop, subtitle-burn, audio-mix, concat, loudness |
| Stato | ATTIVO (locale, costo zero, nessuna dipendenza API esterna) |
| Launcher | `engines/ffmpeg.sh` (da creare) — wrapper shell su `ffmpeg` locale |
| Fallback | nessuno (ffmpeg è il fallback degli altri engine per post-processing) |
| Tier modello owner | haiku (CF-R2-A06-editor-ffmpeg) |

---

## Contratto engine (non negoziabile — pattern §5 del dossier)

| Operazione | Implementazione | Descrizione |
|---|---|---|
| `generate(job)` | esegue comando ffmpeg con parametri del job (input/output path, filtri) | Montaggio o conversione video |
| `check()` | `ffmpeg -version` — ritorna `{available: true/false, version: "..."}` | Health probe istantaneo |
| `status()` | sincrono (processo in-line) — ritorna exit code 0/non-0 | |
| `estimate(job)` | `{crediti: 0, tempo_stimato_sec: N}` basato su durata input e complessità filtri | Costo zero — sempre approvato da CF-SENT-cost |

---

## Capability operative

### concat (unisci clip)
```bash
ffmpeg -i "concat:clip1.mp4|clip2.mp4" -c copy output.mp4
# oppure con filter_complex per clip di formati diversi
```

### crop + aspect ratio
```bash
# 16:9 → 9:16 (reel/short)
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0" -c:a copy output_916.mp4
# 9:16 → 1:1
ffmpeg -i input.mp4 -vf "crop=ih:ih:(iw-ih)/2:0" -c:a copy output_11.mp4
```

### subtitle-burn (burn-in SRT)
```bash
ffmpeg -i input.mp4 -vf "subtitles=sub.srt:force_style='FontName=Anton,FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,BorderStyle=1,Outline=2'" output_sub.mp4
```

### loudness (-14 LUFS standard streaming)
```bash
ffmpeg -i input.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" output_norm.mp4
```

### audio-mix (voiceover + musica di sottofondo)
```bash
ffmpeg -i video.mp4 -i voiceover.mp3 -i music.mp3 \
  -filter_complex "[1:a]volume=1.0[vo];[2:a]volume=0.15[bg];[vo][bg]amix=inputs=2[a]" \
  -map 0:v -map "[a]" -c:v copy output_mixed.mp4
```

---

## Standard output CF-DE

| Formato | Parametri |
|---|---|
| Reel/Short/TikTok | 9:16, 1080x1920, h264, 30fps, -14 LUFS, subtitle burn-in |
| IG Post Video | 1:1, 1080x1080, h264, 30fps, -14 LUFS |
| YouTube | 16:9, 1920x1080, h264/h265, 30fps, -14 LUFS |
| Thumbnail Preview | estratto frame: `ffmpeg -i video.mp4 -ss 00:00:01 -frames:v 1 thumb.png` |

---

## Regole di routing

1. ffmpeg è usato in OGNI pipeline video come step di post-processing (dopo Higgsfield o HeyGen).
2. È l'unico engine per `cut`, `crop`, `subtitle-burn`, `audio-mix`, `concat`.
3. `check()` al boot del reparto CF-R2 — se non disponibile: blocco DELL'INTERA produzione video.
4. Costo zero: `estimate()` ritorna sempre 0 crediti → CF-SENT-cost approva automaticamente.

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — registry engine §5
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Produzione-Video/README.md`
- `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A06-editor-ffmpeg.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §5

*Fonte: dossier 03 §5 · Aggiornato: 2026-06-11*
