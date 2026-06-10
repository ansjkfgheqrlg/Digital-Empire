# Conductor Tools (L1)

## Core Tools (CLI + Python + Handoff)

1. **Memory Manager**
   - Command: `python /home/user/empire-studio/scripts/memory_manager.py --checkpoint "desc" --phase=N --target=/home/user/empire-studio`
   - Or for run: `--target=phase-runs/<run-id>`
   - Always after action. Creates CP + appends INDEX.

2. **yt-dlp (Ingestion)**
   - `yt-dlp --write-auto-sub --write-info-json --write-thumbnail --skip-download -o "%(id)s.%(ext)s" "https://youtube.com/..." `
   - For channel: `--playlist-end 50 --match-filter "title *= marketing" `
   - Python: `import yt_dlp; ydl = yt_dlp.YoutubeDL({...}); info = ydl.extract_info(url, download=False)`

3. **Playwright (Video Watcher + Web)**
   - `python -m playwright install` (done)
   - Script: `python skills/video-watcher-skill/scripts/playwright_video_watcher.py --url="https://youtu.be/xxx" --output=phase-runs/xxx/frames/ --report=video-analysis.md`
   - In python: from playwright.sync_api import sync_playwright; with sync_playwright() as p: browser = p.chromium.launch(headless=True); page = browser.new_page(); page.goto(url); page.screenshot(path="frame.png"); # extract text, selectors for chapters/comments
   - For frames: use page.evaluate for video currentTime + screenshot, or combine with yt-dlp download + opencv (available) for precise extraction.

4. **Content-Forge Invocation (L4 wrapper)**
   - `python scripts/forge_invoker.py --source=phase-runs/<run>/analysis/ --target=wiki --name=<slug> --memory-sync`
   - Internally calls the content-forge skill (assumed available as /forge or python -m content_forge or npx if set).
   - Ensures MKD + wiki output + trace.

5. **Handoff / Spawn (Simulated or Ruflo)**
   - Structured JSON handoff as in system-prompt.
   - Bash: `python -c "import json; ..."` or direct script call for L4.
   - Future: npx ruflo swarm or Task tool for sub-agents.

6. **Web / TikTok (no API)**
   - Playwright for Google search simulation or direct site navigation + parse (respect robots if possible, but for user content).
   - yt-dlp supports TikTok too for many cases.

7. **Validation**
   - `python scripts/validator.py --check-7files --check-cli-only --target=agents/...`
   - Coverage: grep for trace headers, count atoms vs sources.

## Schemas for Outputs

**Handoff Input Schema (JSON):**
```json
{"agent_id": "video-watcher-agent", "inputs": {"video_url": "...", "focus": "design", "previous": {"transcript": "path.vtt"}}, "output_paths": ["video-analysis.md", "frames/"]}
```

**Video Analysis Output Schema (partial):**
```json
{"video_id": "abc123", "duration": "2:15:30", "chapters": [{"time": "12:34", "title": "..."}], "transcript_path": "...", "frames": [{"file": "frame-003.png", "time": "12:34", "visual_desc": "Mostra Figma con 12 components, click su 'Create Style', export JSON tokens visible"}], "key_passages": ["Visual demo of token export not in transcript"], "knowledge_atoms": [{"atom": "Design tokens export flow", "trace": "video:abc123#12:34+frame-003", "source_type": "visual+transcript"}]}
```

**Wiki Note Schema (for content-forge):**
- Atomic .md with frontmatter or wikilinks: `[[source-video-abc123#12:34]]`
- Trace section at bottom.

## Python Helpers in scripts/

- All scripts use argparse, output JSON + files, call memory_manager at end.
- Embed P05 markdown+python in this file and playbooks.

**Trace (P12):** To master-build tools section + content-forge scripts + playwright repos + user "attraverso skill o funzionalità" + "script Python".
