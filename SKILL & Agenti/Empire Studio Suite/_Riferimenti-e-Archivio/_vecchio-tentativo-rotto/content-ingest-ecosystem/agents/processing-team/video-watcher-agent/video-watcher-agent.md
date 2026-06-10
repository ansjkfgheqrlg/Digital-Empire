# video-watcher-agent (L3 — Processing Team)

**Role:** Specialized L3 agent that "guarda" i video usando la L4 video-watcher-skill. Estrae transcript + visual frames + descrizioni dettagliate dei passaggi mostrati. Produce video-analysis.md + frames + atoms con trace perfetta. Chiamato dal processing-team L2 o direttamente dal conductor per singoli video.

**Part of:** processing-team (L2)
**7 Canonical Files:** This + system-prompt.md + tools.md + playbook.md + evals.md + failure-modes.md + memory.md (all to be populated one-by-one per PT05 from master-build).

**Handoff from L2/Conductor:** 
Input: video_url, focus, previous (subs if any).
Output: video-analysis.md, frames/*.png, atoms.json, summary.

**Core:** Invoca `python /home/user/content-ingest-ecosystem/skills/video-watcher-skill/scripts/playwright_video_watcher.py --url=... --focus=...`

**Trace (P12):** To user "video va visto... skill... script Python" + L4 skill + playwright + content-ingest processing.

**Status:** Spec + integration with L4. Full 7 files next (system-prompt with extracts from user vision + L4 + master P08/P12, etc.).
