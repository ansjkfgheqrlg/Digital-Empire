# Empire Studio Agents Catalog (Updated 2026-06-07 - Full 4 Departments + Projects Team Added)

**Name:** Empire Studio (official, per user decision 2026-06-07)

**Hierarchical Structure (4 Levels):**
- **L1:** Conductor (agents/conductor/ - full 7 files)
- **L2:** 4 Symmetric Department Teams + Cross-cutting (Strategy, Verification, Memory, Forge)
  - **YouTube Department** (agents/ingestion-team/ + youtube-specific): yt-channel-ingester-agent, etc.
  - **TikTok Department**: tiktok-ingester (to be expanded)
  - **Web Department**: web-researcher, site-ingester (to be expanded)
  - **Projects, Repos & Workloads Department** (agents/projects-repos-workloads-team/ - NEW fourth, full focus on deep study)
- **L3:** Specialized Agents (each with full 7 canonical files: .md spec + system-prompt.md + tools.md + playbook.md + evals.md + failure-modes.md + memory.md)
- **L4:** Skills (dozens planned/complete: SKILL.md + python/CLI scripts + templates + principles + rules in skills/)

**4 L2 Departments (Symmetric, per user):**
1. **YouTube Department** (Ingestion + YT specific agents)
2. **TikTok Department**
3. **Web Department** (advanced research + sites)
4. **Projects-Repos-Workloads Department** (quarto reparto): deep study of user-provided workflow reports, GitHub/local repos, projects, and other internal workloads WITHOUT EVER MODIFYING ORIGINALS. Uses CLI reads (cat/grep/find/python parsers). Analyzes in minuti dettagli: "come è stato fatto, perché è stato fatto così, come funziona, quanto funziona bene" (strengths/weaknesses, patterns/anti-patterns using master-build principles). Extracts atoms with exact trace to specific files/sections. Then same content-forge → MKD → atomic wiki notes pipeline + update proposals for existing flows (cross-dept).

**Key L3 Agents in Projects-Repos-Workloads Department (agents/projects-repos-workloads-team/):**
- workflow-deep-analyzer-agent (deep study of reports: architecture, decisions "perché", how it works, strengths/weaknesses, trace to file+section, no modify original)
- repo-deep-study-agent (repo analysis: structure, patterns, decisions from docs/code, principle extraction via CLI)
- project-knowledge-extractor (turns deep analysis into traceable atoms for content-forge/wiki)
- workload-comparator (compares to existing Empire Studio knowledge for update proposals)
- empire-projects-strategist (specific strategies for this dept, integrates with Strategy Department)
- project-ingester-agent
- workflow-analyzer-agent
- workload-knowledge-extractor

**Process for 4th Dept (exact user req):**
- User provides report or repo path (or content).
- Deep study (analogous to "deve anche guardarlo... il video deve essere visto... passaggi che si mostrano... attraverso skill... no api... CLI..."): read all files/sections via cat/grep/find/Python, analyze architecture/decisions/"perché"/how it works/how well it works.
- No modification of originals ever.
- Extract knowledge atoms with precise trace (e.g. "file: src/app.js section: lines 42-67").
- Then content-forge → wiki with full traceability.
- Memory updated after every action (CP-XXX etc.).
- Can generate update proposals for Empire Studio flows or other workloads (cross-dept).

**Other L2 Teams (Cross-cutting + Legacy mapping):**
- Ingestion Team (YouTube primary): agents/ingestion-team/yt-channel-ingester-agent/
- Processing Team (video "watching" with Playwright frames + visual "passaggi mostrati" analysis): agents/processing-team/video-watcher-agent/
- Forge Team: agents/forge-team/ (content-forge-wrapper)
- Verification & Control Team: agents/verification-control-team/visual-verifier-agent/
- Memory Management Team: agents/memory-management-team/ (bug-error-tracker-agent, memory-auditor-agent)
- Strategy Department: agents/strategy-department/ (strategy-coordinator/, strategy-controller/, strategy-improver/ - all full 7 files; + content-type-strategist, department-strategist, meta-strategy-manager, strategy-applicator - specs)

**Full 7 Files Agents (examples):**
- conductor/ (all 7)
- strategy-coordinator/, strategy-controller/, strategy-improver/ (all 7 each)
- yt-channel-ingester-agent/ (spec + partial)
- video-watcher-agent/ (spec)
- New projects agents: specs created, full 7 files in progress (start with workflow-deep-analyzer-agent)

**Strategies (multi-strategy system, managed by Strategy Dept):**
- /strategies/STRATEGY-REGISTRY.md
- youtube/youtube-design-system-strategy-v1.1.md (frame rules, visual depth >60 words, decision tree, wiki template, update-proposal mandatory)
- content-types/marketing-content-wiki-implementation-strategy.md
- tiktok/tiktok-automation-strategy-v1.0.md
- web/web-research-strategy-v1.0.md
- projects-repos-workloads/ sub-strategies (to expand)
- Tool: scripts/generate_strategy_manifest.py (--input-type, --focus, --duration, --output, --run-id) → JSON + .md manifest with selected_strategies + rules + rationale + trace

**Skills (L4 - expanding to dozens):**
- skills/yt-ingest-skill/ (SKILL.md + scripts)
- skills/video-watcher-skill/ (SKILL.md + scripts/playwright_video_watcher.py - real Playwright for frames + visual analysis)
- skills/content-forge-wrapper-skill/ (SKILL.md + integration with Manifest)
- More to be added: frame-extractor, visual-analyzer, repo-parser, atomic-note-creator, memory-checkpoint, strategy-applicator, workflow-report-parser, etc. (see skills/ expansion)

**Memory:** /memory/ with checkpoints/ (11 CPs, safe names), decisions/, sessions/, plans/, architectures/, strategy-applications/, etc. Actively managed by memory agents. P10 protocol, two-layer. Update after EVERY action/decision/bug/handoff.

**Verification & Control:** Constant via dedicated team + evals in every agent.

**Scripts/Tools:**
- scripts/generate_strategy_manifest.py
- scripts/memory_manager.py
- (more CLI for deep study: python parsers for reports/repos)

**Trace to User Req:** "Empire Studio", "quarto reparto per progetti, le repo e gli altri workload", "studiarlo, studiarlo nei minimi dettagli. Come è stato fatto, perché è stato fatto così, come funziona, quanto funziona bene", "non lo devi modificare", "la stessa cosa" (content-forge pipeline), "tutti gli agenti", "tutte le decine e decine di skill", "tutta l'immensità della struttura d'archettatura", "tutti i file, tutti i flussi", "deve anche guardarlo... il video deve essere visto... passaggi che si mostrano... attraverso skill... no api... CLI..."

**Download for Local Claude Code Edit:** Use ONLY empire-studio-clean.zip (or .tar.gz / super-clean). See README.md for exact instructions. Clean archives exclude old dirs/bad names.

**Status:** Base hierarchy + 4 depts described + projects-repos-workloads-team/ created with 8 agent dirs + specs. Strategy full for priority agents. Skills expanding. Ready for user-provided workflow report to trigger 4th dept deep study (CLI + manifest + forge + memory update).

All per exact user instructions: full 7 files where prioritized, multi specific strategies, memory updates, CLI-only, 4th dept deep study no modify, content-forge linkage.
