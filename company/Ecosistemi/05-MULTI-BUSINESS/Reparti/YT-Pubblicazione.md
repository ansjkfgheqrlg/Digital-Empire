> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.1 + 4.2 + 4.3 + 4.4

# Reparto L2 — YT-Pubblicazione (`MB-YT`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-YT-PUB · **Priorità:** ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Pubblicare ogni video ottimizzato e gate-verde su YouTube via Data API, distribuire i clip
cross-platform (Shorts/TikTok/Reels), schedulare le pubblicazioni rispettando la cadenza
editoriale, e chiudere il loop leggendo le metriche per retroalimentare la Strategia.

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-YT-PUBLISH` | 4 — Pubblicazione | Video pubblicato o schedulato su YouTube; clip cross-platform distribuiti; entry log wiki `log.md` |
| `WF-YT-ANALYTICS` | 4 → 1 (loop) | Report retention/CTR a 48h/7gg/28gg; raccomandazioni → memoria `mb/yt/<canale>/` + calendario |

**Passi 13-16 della pipeline:**
- Step 13: upload YouTube Data API (metadata, end screen, playlist)
- Step 14: scheduling (cadenza warm-up 2-3/sett; regime `[da ingestione F-MB1]`)
- Step 15: clip cross-platform ordinati a CF e distribuiti (Shorts/TikTok/Reels — 1-2/giorno)
- Step 16: analytics → feedback a Fase 1 Strategia

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-uploader-api | Upload via YouTube Data API: carica video, imposta metadata, end screen, playlist |
| T-scheduler | Scheduling pubblicazione rispettando cadenza canale e slot calendario |
| T-clip-crossposter | Ordina clip verticali a CF e li distribuisce su Shorts/TikTok/Reels |
| T-metrics-reader | Legge le metriche YouTube (CTR, retention, impression) a 48h/7gg/28gg |
| T-retention-analyst | Analizza drop-off, individua pattern, propone correzioni ai brief |

## Agenti L5 assegnati

- `mb-yt-publish-coord` (coordinator, Sonnet) — coordina pubblicazione e cross-posting
- `mb-yt-uploader` (worker, WASM/Haiku) — upload YouTube Data API
- `mb-yt-clipper` (worker, Haiku) — ordina clip a CF e distribuisce
- `mb-yt-retention-analyst` (worker, Sonnet) — analytics → diagnosi → correzioni

## Gate pre-upload (Policy/Brand Gate — obbligatorio)

Prima di ogni upload, `mb-qa-sentinel-liaison` esegue la checklist:
- Policy YouTube: reused content, disclosure contenuto AI (dove richiesta), no spam
- Niente clickbait ingannevole; zero keyword stuffing nei metadata
- Mandato Empire: conformità Brand Voice, zero claim senza prova
Gate rosso → blocco upload; report a mb-conductor.

## Vincolo review umana (attivo fino a revoca formale)

Review umana obbligatoria su ogni pubblicazione finché mb-conductor + C-Suite non revocano il
vincolo. Criterio di revoca: 20 pubblicazioni consecutive senza correzioni umane (dossier §4.4).

## Cadenza pubblicazione

- Warm-up (settimane 1-4): 2-3 video/settimana (anti spam detection, raccolta dati retention)
- Regime (mese 2+): `[da ingestione F-MB1: cadenza reale canali riferimento]` — default 3-5/sett SE gate reggono
- Shorts/clip: 1-2/giorno derivati dai long-form (costo marginale basso)

## KPI di reparto

- Upload completati senza errori API: ≥ 99%
- Metriche lette e loggate nei namespace entro 48h dal video: 100%
- Pattern WF-YT-ANALYTICS riusati nel calendario successivo: trend crescente
- Zero strike policy (strike → freeze canale + post-mortem ReasoningBank immediato)
