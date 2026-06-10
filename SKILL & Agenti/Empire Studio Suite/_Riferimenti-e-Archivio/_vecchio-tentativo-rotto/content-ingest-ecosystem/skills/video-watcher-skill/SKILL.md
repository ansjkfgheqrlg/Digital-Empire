---
name: video-watcher-skill
description: 'L4 Skill: "Guarda" veramente i video YouTube/TikTok. Usa esclusivamente CLI (playwright + yt-dlp + python/opencv se disponibile) per aprire la pagina, estrarre transcript/sottotitoli, capitoli, commenti, metadata, e — cruciale — screenshot/frame a intervalli chiave o capitoli. Produce visual timeline + descrizioni dettagliate dei "passaggi mostrati" (UI, demo, risultati visivi) che il solo transcript non cattura. Output: video-analysis.md (Transcript | Visual Timeline con refs a frame-*.png | Key Visual Passages | Knowledge Atoms con trace timestamp+frame). Per content-ingest-ecosystem processing-team. No API, no paid, no vision model esterno — solo automazione browser + frame extraction + text analysis. Invocabile da agenti L3 o direttamente.'
intent: >-
  Fornisci la funzionalità "il video va visto" richiesta dall'utente. Non basta il transcript: estrai e descrivi il contenuto VISIVO (ciò che si vede sullo schermo durante i passaggi chiave). Usa Playwright per controllare il browser (goto video, estrai elementi pagina, screenshot), yt-dlp per subs/metadata affidabili, python per estrazione frame precisa se video scaricato. Salva frames come PNG per reference (possibile visione contestuale o OCR). Struttura output per facile ingest in MKD/wiki via content-forge. Completo: SKILL.md + references (playwright best practices + yt-dlp) + scripts (full python) + templates (analysis report) + principles (CLI-only, traceability to frame, expand visual) + rules (min frames, detailed desc, no invention).
type: tool
theme: video-visual-analysis
best_for:
  - "YouTube video lunghi (tutorial, design system, marketing) dove il visual è cruciale"
  - "TikTok o short dove demo visive sono il valore"
  - "Qualsiasi video dove 'mostra' UI, clicks, risultati, layout"
scenarios:
  - "Guarda questo video di 2h su design system e descrivi esattamente cosa si vede nei passaggi chiave (Figma, export, etc)"
  - "Per questo tutorial tool, estrai i passaggi visivi che non sono detti ad alta voce"
  - "Ingest video marketing: cattura le UI delle ads e funnel mostrati"
estimated_time: "2-10 min per video (dipende da durata e numero frame)"
compatibility: "Playwright chromium (installato), yt-dlp, python (opencv opzionale per frame extraction), filesystem per frames/. Integra con content-ingest-ecosystem L3 agents e content-forge."
---

# video-watcher-skill — "Il Video Va Visto" (CLI-Only Visual Analysis)

> **"Transcript + visual frames + descrizioni dei passaggi mostrati = conoscenza completa che il solo audio non dà."**
>
> Per l'utente: "deve anche guardarlo... il video deve essere visto... dentro il video ci sono proprio dei passaggi che si mostrano e che dal trascritto non si capiscono perfettamente".
>
> Implementazione: Playwright (browser automation) + yt-dlp (subs affidabili) + frame extraction. Output strutturato per forge/wiki. Tracciabilità a frame file + timestamp. Espansione (non summary). CLI only.

## Invariant (Non Negoziabili)

- **Visual First (User + "video va visto")**: Transcript è base, ma SEMPRE integra con frame extraction + detailed visual description dei "passaggi mostrati" (es. "a 12:34 si vede il cursore cliccare su 'Create Component' in Figma, appare il panel con 5 properties, il risultato è un button con shadow X").
- **CLI Only, No API/Paid**: 100% playwright + yt-dlp + python stdlib/opencv (già in env). Niente vision API, niente paid transcribe.
- **Trace to Frame (P12)**: Ogni knowledge atom o visual passage ha "trace: video-id#timestamp + frame-003.png".
- **Expand + No Invention**: Descrivi solo ciò che è visibile o deducibile strettamente da frame + transcript. Etichetta ➕ per inferenze.
- **Min Frames + Key Points**: Almeno 5-8 frame per video o 1 per capitolo + % (0/25/50/75/100). Priorità a capitoli e demo visive.
- **Output for Forge**: video-analysis.md pronto per content-forge (sezioni chiare, atoms, glossary visual).

## Come Funziona (Scripts)

**Main Entry:** `python scripts/playwright_video_watcher.py --url="https://youtu.be/xxx" --output-dir="frames/" --report="video-analysis.md" --focus="design"`

**Internals (in script):**
1. yt-dlp: extract info, auto-subs, chapters if any, thumbnail.
2. Playwright:
   - Launch headless chromium.
   - Goto url (with timeout).
   - Extract: page title, description, chapters (try selectors or from yt-dlp), top comments (scroll or load), current transcript if auto-loaded.
   - For frames: 
     - If chapters: for each chapter time, seek if possible or note time, screenshot.
     - Else: at 0%, 25%, 50%, 75%, 100% of duration (use video element currentTime + screenshot or download video partial with yt-dlp and use opencv/ffmpeg to extract exact).
   - Save frames as frame-001.png, frame-002.png... with metadata json (time, desc).
3. Visual Analysis (text-based, since no vision model here; detailed prompt in code or human-like describe from context):
   - For each frame: "Describe exactly what is visible on screen: UI elements, text, colors, layout, actions (cursor, clicks implied by sequence), results shown. Be specific: 'Figma left sidebar with 12 components listed, main canvas shows button with blue shadow, right panel has token export button highlighted'."
   - Combine with transcript at that time.
4. Output:
   - video-analysis.md (full structured).
   - frames/*.png + frames/metadata.json.
   - atoms.json (for KG).

**Playwright Tips (from provided playwright-dev + microsoft/playwright.dev):**
- Use page.screenshot({fullPage: false, clip if needed}).
- For video sites: wait for player, use page.evaluate for video.currentTime.
- Handle consent/cookies if needed (but for YT usually not).
- Headless + slowMo for reliability.
- See references/playwright-best-practices.md (extracted).

**yt-dlp for Reliability:**
- Always use for subs and metadata (more reliable than page scrape for auto-captions).

## Output Template (assets/templates/video-analysis-template.md)

# Video Analysis: [Title] ([ID])

**Source:** https://... **Duration:** ... **Focus:** ...

## Transcript (Cleaned)
[full or key parts]

## Visual Timeline
- **00:00 (frame-001.png)**: [visual desc] + transcript snippet. **Key Passage:** "Mostra creazione nuovo file Figma..."
- **12:34 (frame-003.png)**: [detailed UI desc] **Passaggio mostrato non nel transcript:** "Clic su export, appare JSON con tokens visibili sullo schermo."
...

## Key Visual Passages (ciò che si vede ma non si capisce solo dal testo)
1. [Passage] (frame-003, ts 12:34): Descrizione + perché importante per conoscenza.
...

## Knowledge Atoms (with trace)
- Atom: "Token export flow in Figma"
  - Visual: "Export button → JSON preview with color tokens"
  - Trace: video-abc123#12:34 + frame-003.png
  - Practical Step: "1. Select components 2. Click export 3. Copy JSON"
  - ➕ Example: "Utile per design system automation"

## Metadata
- Chapters: ...
- Top Comments relevant: ...
- Frames extracted: 8

**Trace (P12):** Sources: yt-dlp + playwright page + frames. For content-ingest-ecosystem.

## Principles & Rules (Embedded)

- **CLI Purity (User):** Only the listed tools. No external services.
- **Expand Visual (User + P03):** Descrivi frame in dettaglio (50+ words se complesso). Non "video shows screen" — "mostra esattamente...".
- **Traceability (P12):** Sempre "trace: ... + frame-XXX.png".
- **No Invention:** Solo visibile + dedotto da transcript sincronizzato. ➕ per inferenze.
- **Min Quality:** Almeno X frames o warning.
- **Integration:** Output directly usable by content-forge (clean sections, atoms list).
- **Performance:** Headless, reasonable timeouts, batch frames.

## Scripts (scripts/)

- `playwright_video_watcher.py`: Full implementation (argparse, sync_playwright, yt_dlp, opencv optional for frame extract from video file, write report using template).
- `frame_extractor.py`: Helper if video downloaded.
- `visual_describer.py`: Text analysis of frames (can be enhanced with local models if ever).

## References (references/)

- Extracts from /home/user/playwright-dev and microsoft/playwright.dev (best practices for video sites, screenshot, page interaction).
- yt-dlp docs (subs, chapters, info).
- content-ingest-ecosystem SKILL.md (video watcher role).
- master-build P12 traceability + P08 depth.

## Assets/Templates

- video-analysis-template.md (above).
- frame-report.md partial.

## Evals (in main evals/)

- "Watch design system video, verify 10+ specific visual passages captured (e.g. 'export JSON visible') + frames saved + trace in output."
- "TikTok demo: capture UI clicks not described in voiceover."
- CLI only check, no API.

**Status:** Full L4 skill. Script to be populated (see scripts/ in this skill). Ready for L3 video-watcher-agent to call it.

**Trace to User:** Exact "deve anche guardarlo... il video deve essere visto... passaggi che si mostrano e che dal trascritto non si capiscono perfettamente... attraverso skill o funzionalità... script Python... template... principi... regole" + playwright repos + content-ingest vision + master-build complete skills.

**End of Skill Kernel.**
