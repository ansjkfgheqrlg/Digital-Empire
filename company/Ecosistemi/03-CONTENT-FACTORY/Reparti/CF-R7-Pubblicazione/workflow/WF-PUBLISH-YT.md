---
Type: WORKFLOW
Status: Active
Tags: #workflow #CF-R7 #youtube #upload #metadati #thumbnail #ab-test #pipeline
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-PUBLISH-YT — Pubblicazione YouTube

> **Reparto:** CF-R7 Pubblicazione & Distribuzione · **Area:** Post-Produzione
> **Thumbnail:** selezionata dal committente tra varianti A/B da WF-THUMBNAIL (CF-R5)
> **REVIEW UMANA OBBLIGATORIA:** gate manuale non bypassabile (policy Board)

---

## Scopo

Upload completo su YouTube di video con gate verdi CF-R6. Il workflow gestisce tutti i
metadati (titolo, descrizione, tag, playlist, orario schedulato) e la thumbnail selezionata
tra le varianti A/B prodotte da WF-THUMBNAIL. La thumbnail approvata dal committente è
un prerequisito bloccante: nessun upload senza thumbnail selezionata.

**Dry-run:** produce un piano upload con lista metadati compilati senza eseguire l'upload.
Utile per review del committente prima di schedulare.

---

## Passi del workflow

| # | Passo | Agente | Input | Output | Gate |
|---|---|---|---|---|---|
| 0 | DRY-RUN (opzionale) | CF-R7-COORD | order.json + state.json | `yt-upload-plan.json` a zero effetti | Metadati visibili per review |
| 1 | Pre-check gate | CF-R7-QA | state.json + canale YT | `pre-publish-verdict.json` | Gate verdi CF-R6 + review umana + thumbnail selezionata |
| 2 | Compilazione metadati | CF-R7-YT | brief + brand_kit + icp | titolo, descrizione, tag, playlist, orario | Titolo max 100 char; tag max 500 char; keyword nelle prime 5 parole del titolo |
| 3 | REVIEW UMANA | — (gate manuale) | `yt-upload-plan.json` | `state.json → review_umana.eseguita: true` | Obbligatorio; pipeline ferma fino a ok umano |
| 4 | Upload video | CF-R7-YT | video_path + metadati + orario | video_id + URL YT | Upload OK; video_id ricevuto |
| 5 | Upload thumbnail | CF-R7-YT | thumbnail_selezionata + video_id | thumbnail associata | Dimensioni 1280×720; max 2MB; associata a video_id |
| 6 | Assegnazione playlist e schedule | CF-R7-YT | video_id + playlist + orario | video schedulato | Playlist corretta; orario slot WF-CALENDAR |
| 7 | Verifica live | CF-R7-CHECK | URL YT (video_id) | check_result | URL attivo (200 OK o available after schedule) |
| 8 | Log e chiusura | CF-R7-COORD | check_result + URL | state.json aggiornato | URL definitivo in trace.jsonl |
| 9 | Feedback schedulato | CF-R7-FEEDBACK | URL + ts_publish | scheduling 48h + 7gg | — |

---

## Dry-run (passo 0)

```json
{
  "order_id": "CF-2026-0099",
  "dry_run": true,
  "brand": "mentalita-brutale",
  "yt_upload_plan": {
    "video_path": "orders/CF-2026-0099/04-render/video/video-001.mp4",
    "thumbnail": "orders/CF-2026-0099/04-render/thumbnails/thumb-A.jpg",
    "titolo": "Come costruire disciplina mentale in 30 giorni | Mentalità Brutale",
    "descrizione_preview": "Se aspetti la motivazione, hai già perso...\n\nhttps://mentalitabrutale.com\n\n[prima 200 char]",
    "tag_count": 12,
    "playlist": "Mentalità Brutale — Episodi",
    "orario_schedulato": "2026-06-25T09:00:00Z"
  },
  "pre_check": { "gate_verdi": true, "thumbnail_selezionata": true, "review_umana_presente": false },
  "decisione": "PRONTO — in attesa review umana e conferma metadati"
}
```

---

## Gate non bypassabili

**GATE PRE-PUBLISH (passo 1):**
- Gate verdi CF-R6 in state.json (4 gate: PASS).
- `thumbnail_selezionata` in state.json (scelta committente tra A/B).
- `review_umana.eseguita: true` in state.json.
- Token YouTube API valido.

**GATE THUMBNAIL (passo 5):**
- Dimensioni esatte: 1280×720 pixel.
- Peso: max 2MB.
- Formato: JPG o PNG.
- La thumbnail selezionata deve corrispondere a una delle varianti A/B prodotte da WF-THUMBNAIL.

---

## I/O JSON completo di esempio

**Output finale state.json:**
```json
{
  "order_id": "CF-2026-0099",
  "workflow": "WF-PUBLISH-YT",
  "fasi": {
    "01-pre-check":     { "stato": "PASS", "thumbnail_ok": true, "gate_cf_r6": "PASS", "ts": "2026-06-23T09:55:00Z" },
    "02-metadati":      { "stato": "compilati", "titolo_char": 68, "tag_count": 12, "ts": "2026-06-23T09:56:00Z" },
    "03-review-umana":  { "stato": "completato", "eseguita": true, "ts": "2026-06-23T09:57:00Z", "nome": "Gael" },
    "04-upload-video":  { "stato": "completato", "video_id": "XxXxXxXxX", "ts": "2026-06-23T10:00:00Z" },
    "05-upload-thumb":  { "stato": "completato", "associata": true, "ts": "2026-06-23T10:01:00Z" },
    "06-schedule":      { "stato": "schedulato", "orario": "2026-06-25T09:00:00Z", "playlist": "Mentalità Brutale — Episodi" },
    "07-check":         { "stato": "URL_ATTIVO", "url": "https://www.youtube.com/watch?v=XxXxXxXxX" },
    "08-feedback":      { "ts_48h": "2026-06-27T09:00:00Z", "ts_7gg": "2026-07-02T09:00:00Z" }
  },
  "publish": [
    { "canale": "youtube", "url": "https://www.youtube.com/watch?v=XxXxXxXxX", "esito": "SCHEDULATO", "ts_pubblicazione": "2026-06-25T09:00:00Z" }
  ]
}
```

---

## Esempio operativo end-to-end

**Ordine:** CF-2026-0099 · brand: mentalita-brutale · video 8min · slot 2026-06-25T09:00

**Passo 0 (dry-run):** Piano con titolo (68 char), descrizione preview, 12 tag, thumbnail-A,
playlist "Mentalità Brutale — Episodi". Inviato a Gael per review.

**Passo 1 (pre-check):** Gate CF-R6 PASS; thumbnail-A selezionata in state.json; review_umana.eseguita: true → PASS.

**Passo 2 (metadati):** Titolo "Come costruire disciplina mentale in 30 giorni | Mentalità Brutale";
descrizione 1200 char; 12 tag (280 char totali); playlist assegnata.

**Passo 3 (review umana):** Gael approva metadati alle 09:57. `review_umana.eseguita: true`.

**Passo 4 (upload):** video-001.mp4 (320MB) → video_id `XxXxXxXxX` in 45s.

**Passo 5 (thumbnail):** thumb-A.jpg (1280×720, 1.2MB) → associata a `XxXxXxXxX`.

**Passo 6 (schedule):** Orario 2026-06-25T09:00:00Z; playlist "Mentalità Brutale — Episodi" → OK.

**Passo 7 (check):** URL `https://www.youtube.com/watch?v=XxXxXxXxX` → 200 OK (visibile dopo orario schedule).

**Passi 8-9:** state.json chiuso. Feedback 48h: 2026-06-27. Feedback 7gg: 2026-07-02.

---

## Connessioni

- [[cf-r7-coord]] · `agenti/cf-r7-coord.md` — orchestra questo workflow
- [[cf-r7-yt]] · `agenti/cf-r7-yt.md` — executor passi 2-6
- [[cf-r7-check]] · `agenti/cf-r7-check.md` — verifica URL YT live
- [[CF-R5-Visual-Design]] · WF-THUMBNAIL fornitore varianti A/B thumbnail
