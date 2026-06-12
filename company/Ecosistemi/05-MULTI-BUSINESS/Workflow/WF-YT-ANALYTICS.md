> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2 + 10

# WF-YT-ANALYTICS — Metriche → feedback a Strategia

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Pubblicazione · **Fase:** 4 → 1 (loop)
**Owner gate:** `mb-yt-retention-analyst` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Chiudere il loop di apprendimento: leggere le metriche YouTube a 48h/7gg/28gg dal
video pubblicato, diagnosticare drop-off e CTR, distillare raccomandazioni verso il
calendario e i brief futuri. Ogni pattern imparato si salva in `mb/yt/patterns` e
ReasoningBank — non si ri-impara ad ogni video.

## Trigger

- 48 ore dalla pubblicazione (lettura iniziale CTR + retention)
- 7 giorni dalla pubblicazione (lettura completa primaria)
- 28 giorni dalla pubblicazione (lettura finale, decisione kill/relaunch)

## Input

| Campo | Fonte |
|---|---|
| YouTube Analytics API: CTR, retention, impression, click, sub gained, revenue | YouTube Data API (credenziali PLATFORM) |
| Metadata video (topic, titolo, thumbnail, keyword) | `mb/yt/<canale-slug>/videos/<id>/` |
| Benchmark canale (baseline post 10 video) | `mb/yt/<canale-slug>/analytics/baseline.yaml` |

## Processo

1. `mb-yt-retention-analyst`: pull metriche via YouTube Data API per il video/periodo
2. `mb-yt-retention-analyst`: confronto con baseline canale (o media storica se >=5 video)
3. `mb-yt-retention-analyst`: identifica drop-off principali (grafico retention: dove scende)
4. `mb-yt-retention-analyst`: classifica il video: WINNER / MEDIO / WEAK / FAIL
5. Per DROP-OFF: propone correzione al template script (durata sezione, hook, transizioni)
6. Per CTR basso: propone varianti titolo/thumbnail → A/B per video successivo
7. Per WINNER: estrae il pattern → `mb/yt/patterns` (cross-canale) + ReasoningBank
8. Aggiorna il calendario: rinforza topic/angoli vincenti; rimuove slot simili ai FAIL

## KPI tracciati per video

| Metrica | Note |
|---|---|
| CTR thumbnail | Baseline fissata dopo i primi 10 video — NON si inventano benchmark prima `[da F-MB1 + dati reali]` |
| Retention media % | |
| % vista dei primi 30s | Indicatore di hook quality |
| Impression (reach organico) | |
| Sub gained per video | |
| RPM (post-monetizzazione) | Solo dopo YPP approvata |

## Output (report + update namespace)

```yaml
video_id: ""
canale_slug: ""
periodo: "48h | 7gg | 28gg"
metriche:
  ctr: 0.0
  retention_media_pct: 0.0
  vista_30s_pct: 0.0
  impressioni: 0
  sub_gained: 0
classificazione: "WINNER | MEDIO | WEAK | FAIL"
drop_off_principali: []
raccomandazioni_script: []
raccomandazioni_titolo_thumbnail: []
pattern_estratti: []
aggiornamento_calendario: true
```

## Acceptance criteria

- Report generato a 48h, 7gg, 28gg senza intervento manuale
- Pattern WINNER salvati in `mb/yt/patterns` (cross-canale) + ReasoningBank (INTELLIGENCE)
- Calendario aggiornato dopo ogni report 28gg
- Nessun benchmark inventato — tutti i KPI sono baseline calcolate su dati reali
