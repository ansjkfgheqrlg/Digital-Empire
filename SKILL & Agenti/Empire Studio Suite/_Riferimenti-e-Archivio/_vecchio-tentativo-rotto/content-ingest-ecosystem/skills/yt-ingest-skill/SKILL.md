---
name: yt-ingest-skill
description: 'L4 Skill for YouTube/TikTok channel and video ingestion via pure CLI (yt-dlp). Handles single video, full channel, playlist, screening by topic/focus (marketing, design, automation, tools). Extracts metadata, auto-subs, info.json, thumbnails, chapters. Supports --recursive for channels, filtering, multi-video batch. Outputs structured metadata + subs paths ready for processing-team (video-watcher) and content-forge. No API, no paid. Complete with SKILL.md + references + scripts (Python + yt-dlp wrappers) + templates + principles (CLI-only, traceability, screening logic) + rules. Designed for content-ingest-ecosystem L2 ingestion-team and L3 yt-channel-ingester-agent.'
intent: >-
  Fornisce ingestion affidabile e scalabile per YT e TikTok (yt-dlp supporta entrambi). Da link singolo o canale a lista di video con metadata completi + subs. Supporta screening intelligente (match title/description per focus utente). Batch processing. Output: video-list.json + per-video metadata/subs/thumbs. Sempre espansione + trace (video ID). Integra con video-watcher per "guardare" e content-forge per wiki. CLI-only 100%.
type: tool
theme: content-ingestion-yt-tiktok
best_for:
  - "Screening e ingestion di interi canali YouTube su argomento specifico (marketing, skills, automazioni)"
  - "Singoli video lunghi o tutorial"
  - "TikTok channels o singoli per demo pratiche"
  - "Preparazione materiale grezzo per video-watcher + content-forge"
scenarios:
  - "Screening canale YT marketing, prendi solo video rilevanti su design system o tool usage"
  - "Ingest singolo video 2h e prepara per 'guardare' + forge"
  - "Canale TikTok su automazioni, estrai tutti i tutorial pratici"
estimated_time: "1-15 min per canale (dipende da size e filtro)"
compatibility: "yt-dlp (installato), python. Integra con content-ingest-ecosystem (L3 yt-*-ingester, processing-team) e content-forge2.0."
---

# yt-ingest-skill — Ingestion CLI per YouTube e TikTok (Screening + Metadata Completo)

> **"Da link canale o video a lista strutturata di materiale grezzo (metadata + subs + thumbs) pronto per visione e forging. Screening per focus, batch, CLI-only."**

## Invariant Cardinali
- **CLI Only (User)**: 100% yt-dlp + Python. Niente API YouTube ufficiali o pagate.
- **Screening Intelligente (User "screening di tutti i video di questo canale oppure dell'argomento")**: Per canali, filtra per --focus (marketing, design, automation, tools, skills) matchando title/description/tags. Non processa tutto se non serve.
- **Complete Metadata + Subs (per "trascrive tutto completamente")**: Sempre --write-auto-sub, --write-info-json, --write-thumbnail, chapters se presenti. Supporta playlist e canali interi (--playlist-end per sicurezza).
- **Traceability (P12)**: Ogni video ha ID univoco + trace in output. Output include source URL.
- **Ready for Downstream**: Output video-list.json + per-video dir con subs/metadata. Facile handoff a video-watcher L3/L4 e content-forge.
- **No Invention, Expand**: Metadata puliti, subs raw disponibili. Nessun riassunto qui (quello lo fa content-forge).

## Come Funziona
**Entry:** `python scripts/yt_ingest.py --input "https://youtube.com/@channel or video or playlist" --focus "marketing" --output-dir "ingest-run/" --max-videos 20`

**Steps (in script):**
1. yt-dlp extract (info + subs + thumbs) — single or --yes-playlist for channels.
2. Parse info.json per estrarre title, duration, description, chapters, tags.
3. Screening: if channel/playlist, filter videos where title.lower() or description contains focus keywords (or custom rules).
4. Per video rilevante: crea subdir con files (info.json, *.vtt subs, thumb).
5. Output: videos.json (list with paths, metadata summary, trace), summary.md.
6. Memory hook: caller runs manager.

**TikTok support**: yt-dlp gestisce molti TikTok link/canali allo stesso modo.

**Advanced search/web**: Per "ricerca estremamente avanzata su siti web" usa il web-ingest-skill companion (Playwright per Google-like o direct site crawl, no API).

## Output Example
ingest-run/
├── videos.json          # [{"id": "abc123", "title": "...", "url": "...", "focus_match": true, "subs_path": "abc123.en.vtt", "info_path": "...", "trace": "source:channel-url"} , ...]
├── summary.md
└── per-video/
    └── abc123/
        ├── abc123.info.json
        ├── abc123.en.vtt
        └── thumb.jpg

## Scripts
- `scripts/yt_ingest.py`: Full argparse, yt_dlp.YoutubeDL, filtering logic, batch, error handling, output structured.
- Helpers for playlist vs single, focus filter (customizable keywords per focus).

## Templates (assets/templates/)
- video-metadata-template.json
- ingest-summary-template.md

## References
- yt-dlp official (CLI options for subs, playlist, info, chapters).
- content-ingest-ecosystem SKILL.md (ingestion-team role + L3).
- master-build patterns for traceability and screening.

## Principles & Rules
- CLI purity.
- Screening before heavy processing (efficiency + user focus).
- Always provide raw subs + metadata (for watcher to "guardare").
- Trace every video to original input.
- Safe limits (max-videos, warn on huge channels).
- Expand: full info, not stripped.

**Evals**: Test screening accuracy on sample channel, verify subs present, output ready for watcher, CLI only.

**Status**: Full L4 skill ready. Script to be the main implementation (see scripts/). Perfect for L3 yt-channel-ingester-agent.

**Trace (P12)**: To user "link di un canale Youtube... screening di tutti i video... dell'argomento... Tik tok... siti web... presearch... ricerca estremamente avanzata... trascrive tutto completamente" + yt-dlp power + content-ingest ingestion + master-build complete skills.
