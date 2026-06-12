> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 4.2 + 4.3

# WF-YT-OPT — Ottimizzazione titolo/SEO/thumbnail

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** YT-Ottimizzazione · **Fase:** 3 — Ottimizzazione
**Owner gate:** `mb-yt-opt-coord` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Massimizzare il CTR e la visibilità organica di ogni video prima della pubblicazione:
titolo finale, descrizione SEO, tag, end screen, thumbnail selezionata. Questo workflow
possiede i gate #1 (Script, eseguito all'inizio) e #4 (SEO, eseguito alla fine).

## Input

| Campo | Fonte |
|---|---|
| Asset video consegnati da CF (gate #2 e #3 verdi) | WF-YT-VIDEO-ORDER |
| Script del video (file testo) | CF via contratto Bus |
| Keyword target (primaria + secondarie) | `mb/yt/<canale-slug>/calendar/<slot>` |
| Pattern titoli/thumbnail vincenti | `mb/yt/patterns` (cross-canale) |

## Processo (step 10-12 pipeline + gate #1 e #4)

### Step A — Gate #1 Script (PRIMO, bloccante)
`mb-yt-opt-coord` + Brand-Voice Sentinel verificano lo script ricevuto da CF:
- Hook nei primi 15s presente e funzionale
- Struttura retention (loop aperti, payoff dichiarato)
- Aderenza brand_kit (tono, persona, lingua)
- Lunghezza ±10% del target (brand_kit: durata_minuti_target × parole_per_minuto_TTS)
- Zero claim non verificabili
- Similarity < soglia vs ultimi 20 script del canale (anti-ripetitività)
- Lingua/grammatica pulita

Gate #1 rosso → script torna a CF. WF-YT-OPT non procede.

### Step B — Ottimizzazione (passi 10-12)
10. `mb-yt-title-smith`: genera 5+ varianti titolo; seleziona la migliore (CTR-first, keyword primaria, ≤100 char, policy-safe)
11. `mb-yt-seo-writer`: descrizione SEO ≥200 parole (keyword + timestamp + CTA); tag 10-15 pertinenti; end screen + cards
12. `mb-yt-thumb-strategist`: seleziona thumbnail da quelle consegnate da CF; spec A/B test; verifica leggibilità 120px

### Step C — Gate #4 SEO (ULTIMO, bloccante)
`mb-yt-seo-writer` + `mb-yt-opt-coord` verificano:
- Titolo ≤100 caratteri con keyword primaria
- Descrizione ≥200 parole con keyword, timestamp e CTA
- 10-15 tag pertinenti, niente keyword stuffing
- End screen + cards impostate
- Metadata policy-safe (no clickbait ingannevole, no spam)

Gate #4 rosso → rifacimento ottimizzazione; log ReasoningBank.

## Output pacchetto ottimizzato (formato per WF-YT-PUBLISH)

```yaml
canale_slug: ""
video_id_interno: ""
titolo_finale: ""
descrizione: ""
tag: []
end_screen: []
cards: []
thumbnail_selezionata: "<path>"
thumbnail_ab_variante: "<path | null>"
gate_1_script: "PASS"
gate_4_seo: "PASS"
pronto_per_publish: true
```

## Acceptance criteria

- Gate #1 Script: PASS prima di procedere all'ottimizzazione
- Gate #4 SEO: PASS prima di passare a WF-YT-PUBLISH
- Pacchetto salvato in `mb/yt/<canale-slug>/videos/<id>/` + log wiki
- Zero override manuali di gate senza decisione mb-conductor
