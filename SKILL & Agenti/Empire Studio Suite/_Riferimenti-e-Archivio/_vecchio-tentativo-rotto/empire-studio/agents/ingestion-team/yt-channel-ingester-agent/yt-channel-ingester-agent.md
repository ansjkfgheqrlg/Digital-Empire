# yt-channel-ingester-agent (L3 — Ingestion Team)

**Role:** L3 specialist per ingestion e screening di canali YouTube/TikTok (o singoli video). Usa la L4 yt-ingest-skill per estrarre metadata + subs completi, fare screening per focus/argomento, preparare batch per il processing-team (video-watcher per "guardare").

**Part of:** ingestion-team (L2)
**Handoff:** Da conductor o ingestion-team L2: input URL (canale o video), focus, max. Output: videos.json + per-video assets + summary, trace full.

**Core Action:** 
`python /home/user/empire-studio/skills/yt-ingest-skill/scripts/yt_ingest.py --input "URL" --focus "..." --output-dir "..."`

**7 Files:** This spec + system-prompt.md (to be added) + tools.md (yt-dlp + L4 call) + playbook.md (screening logic + examples from user canali) + evals.md + failure-modes.md (e.g. private video, huge channel) + memory.md (P10 per video batch).

**Trace (P12):** To user "link di un canale... screening di tutti i video... dell'argomento... Tik tok" + L4 yt-ingest-skill + yt-dlp + content-ingest L2 ingestion + master-build L3 domain agents.

**Status:** Spec + L4 integration. Full 7 files next (one-by-one PT05).
