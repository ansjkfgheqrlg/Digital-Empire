---
name: frame-extractor-skill
description: 'CLI-only skill for extracting frames from video at chapters or % intervals using yt-dlp + ffmpeg or Playwright screenshots. Used by video-watcher for "visione" + "passaggi mostrati" analysis. Part of Empire Studio L4 Skills. Supports youtube + tiktok video watching.'
---
# frame-extractor-skill

**Purpose:** Extract visual frames from video content for detailed "guarda il video" analysis in Empire Studio (YouTube/TikTok depts). No API.

**CLI Tools:** yt-dlp (download), ffmpeg (frames), or playwright for page screenshots at timestamps.

**Scripts:** scripts/extract_frames.py (to be implemented with yt-dlp --write-info-json + ffmpeg -ss ... -vframes 1)

**Templates:** frame-description-template.md ( "Frame at 25%: shows [detailed visual description >60 words as per youtube-design-system-strategy]")

**Principles:** Visual depth > transcript only. Every frame described in context of "passaggi che si mostrano". Trace to timestamp + chapter.

**Rules:** Extract at 0/25/50/75/100% + chapter points. Save to assets/frames/ per video. Integrate with visual-analyzer-skill.

**Integration:** Called by processing-team/video-watcher-agent. Output feeds knowledge-extractor + content-forge.

**Version:** v1.0 Empire Studio

**Trace:** Supports "il video deve essere visto... passaggi che si mostrano... attraverso skill"
