# Conductor Playbook (Step-by-Step + Examples)

## Overall Flow (10 Stages + Memory) — Aggiornato con Strategy System (Step 3)

**Sempre:**
- Memory bootstrap or update at start of turn/stage.
- Log to trace.jsonl.
- Update state.json.
- After handoff/result: CP + INDEX append + manager.
- Research (read refs, clones, previous) → Plan (this playbook or vN) → Reset (clean context) → Implement.

**Integrazione Strategie (obbligatoria):**
- Dopo Stage 0: Chiama Strategy Department (Strategy Coordinator) per selezionare strategie e generare Strategy Manifest.
- Il Manifest viene passato a tutti i team L2 e deve essere rispettato (controllato da Strategy Controller).
- Ogni team deve loggare come ha applicato le regole del Manifest.

**Stage 0: Bootstrap + Strategy Selection (always)**
1. Ensure phase-runs/<ts>/
2. python scripts/memory_manager.py --init --target=... --vision=...
3. Create state.json, trace.jsonl
4. **Chiama Strategy Coordinator**: "Seleziona strategie per questo input e crea Strategy Manifest".
5. Ricevi Manifest e salvalo in state.
6. Brief user plan (includi strategie scelte).

**Stage 1: Ingestion (spawn L2 ingestion-team)**
- Determine input type.
- Call yt_ingest.py or equivalent for YT/TikTok.
- For web: web_research.py + playwright.
- Output: list of video metadata + subs paths.
- Memory CP "Ingestion complete for N videos".

**Stage 2: Processing & Watch (spawn L2 processing-team → L3 video-watcher etc)**
- For each relevant video (filter by focus or all):
  - Handoff to video-watcher-agent (L3) + L4 skill.
  - Input: url, previous subs.
  - Output: video-analysis.md + frames/*.png + atoms.json
- Parallel where safe (multiple videos).
- "Guarda" details in L3/L4 spec.
- CP "Video X watched: transcript + 8 visual frames + key passages extracted".

**Stage 3-4: KG + MKD**
- Assemble KG (or delegate).
- Produce MKD (or /forge --target=doc first).
- Memory update.

**Stage 5-6: Target + Interactive + Forge (spawn forge-team)**
- If target=wiki (default): prepare source dir with all analysis + MKD.
- ASK if needed (e.g. "Quale focus principale per la wiki?").
- Invoca forge_invoker.py --target=wiki.
- content-forge produces MKD + wiki/ atomic notes.
- CP "Forge to wiki complete. N notes created".

**Stage 7-8: Depth + QA (spawn qa-team)**
- Optimizers if complex.
- coverage-verifier (atoms from original videos/frames present in wiki? %).
- schema-validator.
- If low: iterate (re-spawn watcher or forge with fixes).
- Real test: "Con questa wiki, Claude Code può ora replicare il design system dal video?"

**Stage 9: Wiki Integration + Update Proposals (forge-team or qa)**
- Copy or link wiki notes to user wiki (or output folder with instructions).
- For update-existing: analyze new knowledge vs known workflows (from memory or user context).
- Generate update-proposals.md with "Suggestion: update your skill-creator with this visual token export pattern from video Y#timestamp (see frame Z). Rationale: ... Trace: ..."

**Stage 10: SI (silenzioso, qa-team)**
- If signals (QA fail, user "non funziona", many FMs): spawn failure-detector etc.
- Log FM-*.md.
- Generate phase plan if thresholds.
- Only surface if user asks "stato failure mode" or "piano miglioramento".

## 5+ Examples (Happy, Edge, Failure/Recovery, Constraint, Meta — from User Vision + Master-Build CS)

**Example 1 Happy (User core: video 2h design system → wiki → Claude sa fare)**
- Input: https://youtu.be/design-system-2h --target=wiki --focus=design
- Stage 1: yt-dlp subs + info (duration 2h, 12 chapters).
- Stage 2: processing-team → video-watcher: playwright open, 12 chapters + 20 frames (at chapter starts + mid), visual "a 34:12 mostra creazione di 5 components in Figma, style guide panel, export to JSON visible on screen".
- Atoms: "Design system creation flow: 1. Audit existing 2. Create primitives 3. Tokens export (visual demo not in audio)".
- Stage 4-6: MKD (30p espanso) → content-forge --target=wiki → 8 atomic notes "[[Design-System-Primitives]]", "[[Token-Export-Process]]" with trace "video:xxx#34:12+frame-007".
- Stage 8: Coverage 98% (visual atoms included).
- Stage 9: Wiki updated. Proposal: "Aggiungi al tuo 'master-build-architecture' o skill creation workflow il pattern visual token export dal video (trace frame). Claude Code ora sa fare design system completo."
- Memory: 15+ CPs (one per video stage + forge + proposal), trace P12 full.
- Result: User gets wiki + "ora il tuo Claude Code ha la conoscenza del pro di 2h".

**Example 2 Happy (Canale YT marketing, screening + batch)**
- Input: canale link --recursive --focus=marketing
- Stage 1: yt-dlp playlist, filter 47→9 relevant (title match marketing + views).
- Stage 2: parallel watch 9 videos (playwright for each, frames for visual demos like ad creatives, funnel screenshots).
- ... → wiki "Marketing Playbook 2026" with 25+ notes, trace to specific videos.
- Update proposal for "existing content creation workflow": incorporate "visual ad testing pattern from video Z".

**Example 3 Edge (Incomplete data: no chapters, poor subs)**
- Input: old video.
- Stage 2: watcher gets only auto-subs + 5 generic frames (no chapters).
- Note in analysis: "Limited visual — used thumbnails + % frames".
- Proceed with what available, higher coverage threshold later.
- Recovery: offer "Vuoi che scarichi full video per meglio frames con ffmpeg?" (if user confirms, use yt-dlp download + opencv extract).

**Example 4 Failure/Recovery (content-forge not responding or low coverage)**
- Stage 6: forge call fails or coverage 60% (visual atoms missing in wiki).
- Symptom: "no visual in final wiki".
- Prevention (in playbook): always include frames/ in forge source + "visual timeline" section in template.
- Detection: qa coverage check + grep "frame-" in wiki notes.
- Recovery: log FM-004, re-spawn forge with explicit "include all visual desc and frame refs", iterate max 2, then user escalation "Coverage basso su parti visive, vuoi procedere o re-watch con più frames?".
- Trace to CS04 (real-test) from master-build + our build.

**Example 5 Constraint/Meta (Large channel + self-ref)**
- Input: huge canale 200 video.
- Constraint: "process only 20, focus automation".
- Meta: "This run's lessons (better filtering in ingestion-team) feed back to v2 per PT08/P13. Use our CPs for memory in next ingest."
- In playbook: at end "meta: feed this batch (filtering logic, visual success) to update-proposer for this ecosystem itself + user workflows".

**Example 6 Constraint (User: update existing)**
- After ingest marketing video on "skill creation best practices".
- Stage 9: "Proposal for your 'claudedesignskills' or skill-creator: add visual demo pattern for 'live preview' from this video (trace #45:00 frame). This matches your P15 trigger design."
- Trace full to video + master-build P15 + user "aggiornare i flussi esistenti".

All examples enforce P10 (CPs), P12 (trace), P03 (expand), P08 (depth visual), PT05 (if new agents), CLI (yt/playwright), content-forge wiki, gerarchia (L2/L3 spawn), user "video visto" (frames + visual passages).

**Handoff Examples in Playbook:**
- To ingestion-team: "Spawn ingestion-team with input list of links, focus. Expect metadata + subs in stage-01/."
- To processing: "Process these 3 videos. Use video-watcher L3 for each. Include visual analysis per user 'il video va visto'."

**Continuous Improvement:**
- After run: SI agents review FMs, propose playbook vN or new L3 agent.
- Meta: "This playbook creation itself is example of P13: conductor managing conductor-like flow."

**Trace (P12):** To user "workflow... team di agenti... video... guardarlo... skill... content-forge... wiki... aggiornare i flussi esistenti... agenti... completi... skill... markdown... script Python... template... principi... regole... architettato... no api... CLI" + master-build playbook style + content-forge stages + CS examples + playwright for watcher + our CP-000+.

**Status:** Playbook with 6 examples covering user vision + principles. Ready for use in L1.
