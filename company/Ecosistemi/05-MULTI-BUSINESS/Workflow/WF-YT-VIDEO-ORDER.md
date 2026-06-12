> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2 + 4.3

# WF-YT-VIDEO-ORDER — Ordine video a Content-Factory e validazione consegna

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Produzione · **Fase:** 2 — Produzione
**Owner gate:** `mb-yt-handoff-validator` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Compilare il contratto Bus per richiedere a Content-Factory (03) la produzione di un video
completo (script + voiceover TTS + visual AI + thumbnail), e validare la consegna contro i
gate #2 (Audio) e #3 (Visual). Il Gate #1 Script è attivato da mb-yt-opt-coord all'interno di
WF-YT-OPT. Questo workflow NON produce contenuti: li ordina e li valida.

## Input

| Campo | Fonte |
|---|---|
| Slot calendario (titolo provvisorio + keyword + formato) | `mb/yt/<canale-slug>/calendar/` |
| brand_kit canale | `mb/yt/<canale-slug>/brand_kit.yaml` |
| Stima costo (dry-run obbligatorio pre-ordine) | Cost-Sentinel (Operations 09) |

## Processo

1. `mb-yt-brief-compiler`: dry-run stima costo (TTS provider + image gen + montaggio) → Cost-Sentinel verde
2. `mb-yt-brief-compiler`: compila contratto Bus verso CF (schema sotto)
3. Contratto inviato via Bus → Content-Factory esegue step 5-9
4. CF consegna: script + audio + video + thumbnail
5. `mb-yt-handoff-validator`: verifica Gate #2 Audio (criteri §4.3 dossier)
6. `mb-yt-handoff-validator` + Quality Sentinel: verifica Gate #3 Visual
7. Gate verde → asset archiviati in `mb/yt/<canale-slug>/` + passa a WF-YT-OPT
8. Gate rosso → report failure + CF rilavora; log in ReasoningBank

## Contratto Bus verso Content-Factory

```json
{
  "from": "05-MULTI-BUSINESS/WF-YT-VIDEO-ORDER",
  "to": "03-CONTENT-FACTORY",
  "payload": {
    "brand_kit": "<path o hash brand_kit.yaml>",
    "formato": "video_long | video_short",
    "quantita": 1,
    "spec": {
      "durata_minuti_target": 0,
      "tts_voice_id": "",
      "stile_visual": "animazione_2d | b_roll | avatar_ai | mixed",
      "risoluzione_minima": "1080p",
      "thumbnail": true
    },
    "topic": "",
    "keyword_primaria": "",
    "deadline_giorni": 0,
    "budget_approvato": true,
    "canale_slug": ""
  },
  "acceptance_criteria": [
    "Script completo con hook nei primi 15s",
    "Voiceover TTS senza artefatti, loudness -14 LUFS",
    "Video >=1080p, zero frame neri/watermark",
    "Sync audio-video verificato",
    "Thumbnail leggibile a 120px"
  ],
  "status": "pending | fulfilled | rejected"
}
```

## Gate di competenza (bloccanti)

| Gate | Criteri | Chi blocca |
|---|---|---|
| **#2 Audio** | Zero artefatti/glitch; pronuncia corretta; loudness -14 LUFS; durata audio = script ±5%; pacing conforme brand_kit | mb-yt-handoff-validator |
| **#3 Visual** | ≥1080p; zero frame neri/corrotti/watermark; coerenza stile visual brand_kit; sync audio-video; thumbnail leggibile 120px; volto/soggetto + ≤4 parole | mb-yt-handoff-validator + Quality Sentinel |

## Acceptance criteria workflow

- Contratto Bus compilato senza campi vuoti
- Cost-Sentinel verde prima dell'invio (dry-run cost approvato)
- Entrambi i gate #2 e #3 verdi prima di passare a WF-YT-OPT
- Asset archiviati in namespace `mb/yt/<canale-slug>/` con metadata completi
- Ogni gate rosso loggato in ReasoningBank con causa failure
