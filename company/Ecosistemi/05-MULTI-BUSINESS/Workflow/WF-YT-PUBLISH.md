> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2 + 4.3 + 4.4

# WF-YT-PUBLISH — Upload, scheduling e cross-posting

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Pubblicazione · **Fase:** 4 — Pubblicazione
**Owner gate:** `mb-yt-publish-coord` (review umana attiva) · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Pubblicare il video ottimizzato (gate #1 + #4 verdi) su YouTube via Data API, distribuire i
clip cross-platform, schedulare rispettando la cadenza. Attiva il Policy/Brand Gate pre-upload.
Review umana obbligatoria finché il vincolo non è revocato formalmente.

## Input

| Campo | Fonte |
|---|---|
| Pacchetto ottimizzato (gate #1 e #4 verdi) | WF-YT-OPT |
| brand_kit canale | `mb/yt/<canale-slug>/brand_kit.yaml` |
| Calendario slot | `mb/yt/<canale-slug>/calendar/` |
| Credenziali YouTube Data API | PLATFORM (code custody — NON in git) |

## Processo

### Step 0 — Policy/Brand Gate pre-upload (obbligatorio, bloccante)
`mb-qa-sentinel-liaison` esegue la checklist:
- **Policy YouTube:** no reused content non transformative; disclosure contenuto AI (dove richiesta); no spam/click-bait ingannevole; no violazioni copyright (asset tracciati nel payload CF)
- **Brand Gate:** Mandato Empire rispettato; zero claim senza prova; lingua/tono conforme brand_kit
- Gate rosso → blocco upload + report a mb-conductor

### Step 13 — Upload YouTube Data API
`mb-yt-uploader`: carica il file video, imposta tutti i metadata (titolo, descrizione, tag, categoria,
privacy: unlisted prima di review umana, playlist assegnata, end screen, cards)

### Step 14 — Review umana + scheduling
`mb-yt-publish-coord`: notifica review umana (Max o Gael). Dopo ok → publish immediato o
scheduling nella slot calendario (cadenza warm-up: 2-3/settimana; regime: `[da F-MB1]`)

### Step 15 — Clip cross-platform
`mb-yt-clipper`: compila ordine a CF per clip verticali: `{video_id, segmenti_target, formato: 9:16, durata: ≤60s}`
→ CF produce Shorts/TikTok/Reels → `mb-yt-clipper` distribuisce (1-2/giorno, costo marginale basso)

### Step 16 — Log e passaggio a WF-YT-ANALYTICS
Entry in wiki `log.md`: data, canale, titolo, stato gate, url video
Salvataggio metadata in `mb/yt/<canale-slug>/videos/<id>/published.yaml`

## Acceptance criteria

- Policy/Brand Gate: PASS (blocco assoluto se rosso)
- Review umana: firmata (vincolo attivo — revocabile solo con ADR dopo 20 pubblicazioni consecutive senza correzioni)
- Video pubblicato/schedulato su YouTube + playlist assegnata + end screen + cards
- Clip cross-platform ordinati a CF entro 24h dalla pubblicazione long-form
- Entry wiki log.md completata
