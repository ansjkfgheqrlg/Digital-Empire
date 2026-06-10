# Conductor Evals (5+ Discriminating Cases)

**Protocol (Skill-Creator + Master-Build + Content-Forge style):**
- 5+ cases: happy core, happy batch, edge, failure/recovery, constraint/meta.
- Simulate or real run.
- Grade: coverage % (atoms + visual trace), memory live CPs/DECs/INDEX, CLI-only (no API calls in logs), gerarchia respected (L2/L3 spawn), 7-files if new agents, no-summary + MKD, wiki output with trace, update proposal if relevant.
- Benchmark vs baseline (no this ecosystem = manual watch + manual wiki).
- Iterate: if <9/10, log FM, fix playbook/tools, re-run.
- Human review + quantitative (e.g. "visual passages captured: 12/12").
- Add to evals.json.

**Case CON-001 Happy Core (User: single video 2h design system → wiki + Claude sa fare)**
- Prompt: "/ingest https://youtu.be/design-2h --target=wiki --focus=design --name=design-system-knowledge"
- Expected: yt-dlp subs + playwright watcher (15+ frames + visual desc of Figma steps not in audio), MKD 30p+, content-forge wiki 8+ atomic notes with [[trace video#ts+frame]], coverage 95%+, memory 10+ CPs with P10/P12 headers, update proposal for existing workflows, CLI only (yt/playwright logs).
- Grade target: 9.5/10
- Trace P12: to user video example + "guardarlo" + content-forge + wiki + claude code.

**Case CON-002 Happy Batch (Canale YT marketing screening)**
- Prompt: canale link --recursive --focus=marketing
- Expected: screening 50→12, parallel watch 12 (frames for ad visuals), wiki "Marketing 2026" 20+ notes, 2 update proposals, memory live, gerarchia L1→L2 teams→L3.
- Delta vs baseline: +80% time save, +visual knowledge.

**Case CON-003 Edge (Poor data video)**
- Prompt: old video no chapters.
- Expected: proceed with subs + 5 frames, note limitation in analysis, still produce wiki with available, coverage 70% but acceptable, offer upgrade.
- No crash.

**Case CON-004 Failure/Recovery (Low coverage visual)**
- Simulate forge misses visual atoms.
- Expected: qa detects, FM logged, re-spawn watcher with more frames or forge with explicit visual template, recovery to 92% coverage, CP for recovery (like CS04).
- Prevention in playbook.

**Case CON-005 Constraint/Meta (Update existing + self)**
- Prompt: ingest on skill creation video + "aggiorna i miei flussi"
- Expected: wiki + specific update proposal to "skill-creator" or "master-build" with trace to video visual, + meta self-ref "this run updates this ecosystem's ingestion-team filtering per PT08".
- Memory P10 loops, P13 meta.

**Case CON-006 CLI-Only + Gerarchia (Stress)**
- Prompt: mix YT + TikTok + web.
- Expected: all via yt-dlp/playwright (no API), L2 teams spawned for each dept, L3 agents used, L4 skills called, memory after every, no paid.

**Benchmark & Iteration:**
- Run 1 (initial): 7/10 (visual weak).
- FM → fix watcher script + template.
- Run 2: 9.5/10.
- Human: "Visual passages from frames captured perfectly, now Claude Code has the design system knowledge."
- evals.json updated with results + traces.

**Trace (P12):** To user "no api... CLI... gerarchia... team... agenti completi... video guardato... content-forge... wiki... aggiornare flussi... skill... template... principi" + master-build evals + content-forge + our CPs.
