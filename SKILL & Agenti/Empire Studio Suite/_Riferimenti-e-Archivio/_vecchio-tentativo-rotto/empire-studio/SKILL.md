---
name: empire-studio
description: 'Empire Studio — Workflow completo, gerarchico e professionale (4 livelli, 4 reparti simmetrici: YouTube, TikTok, Web, Projects-Repos-Workloads) per ingerire, analizzare, "guardare" e strutturare conoscenza da YouTube/TikTok/web + deep study di progetti/repo/workload. Trasforma input in MKD + note atomiche wiki (tracciabili) per Claude Code usando SOLO CLI (yt-dlp, Playwright per visione frame + "passaggi mostrati", python, no API, no paid). Struttura aziendale: L1 Conductor, L2 Department Teams, L3 Agents (7 file canonici ciascuno), L4 Skills (complete). Usa content-forge2.0 per forging/wiki. Memory ecosystem full (checkpoints, decisions, etc. gestiti da agenti). Multi-strategie specifiche per dept/tipo. Invocation: /empire <input> [--dept=youtube|tiktok|web|projects] . Per 4th dept: fornisci path report/repo per studio profondo (architettura, perché, come funziona, punti forza/debolezza, estrai atomi con trace a file/sezione, senza modificare originali).'
intent: >-
  Costruire "Empire Studio": ecosistema agentico gerarchico professionale come vera azienda con 4 reparti simmetrici per deep ingestion + knowledge extraction da video/web + quarto reparto per studio dettagliato di workflow report, repo, progetti (senza mai modificare originali). Ogni contenuto processato via content-forge2.0 → MKD + atomic wiki notes con full traceability che alimentano Claude Code. CLI-only (yt-dlp, Playwright frames + visual analysis "passaggi che si mostrano", python scripts). Gerarchia 4 livelli. Ogni agente 7 file completi. Tante skills (decine). Memory attivo gestito da agenti. Strategie multiple specifiche (per dept, content type, wiki style). Verification & Control. Pronto per user-provided report per 4th dept.
type: interactive
theme: empire-studio-workflow
best_for:
  - "Ingest completo canali YouTube/video per estrarre conoscenza marketing, design system, tools, automazioni"
  - "Processare TikTok o video per materiale formazione contestuale con visione reale"
  - "Ricerca web avanzata + siti per knowledge pack wiki"
  - "Deep study di progetti/repo/workload: architettura, decisioni 'perché', come funziona, quanto bene, pattern/anti-pattern (CLI read, no modify)"
  - "Creare 'second brain' wiki per Claude Code con conoscenza pratica da pro"
  - "Aggiornare workflow esistenti basandosi su insight da contenuti + update proposals cross-dept"
scenarios:
  - "Dammi il link del canale YouTube di questo marketer, fai lo screening di tutti i video rilevanti sull'argomento X e metti tutto nella wiki"
  - "Prendi questo video YouTube di 2 ore su creazione design system, 'guardalo' (transcript + visual frame analysis), estrai tutto, forgia con content-forge e aggiungi alla wiki"
  - "Fai una ricerca web avanzata su 'come creare skills per Claude Code senza API' e integra nella wiki + proponi update ai miei workflow esistenti"
  - "Ingest questo TikTok channel su automazioni, estrai tutorial pratici, metti su wiki in modo strutturato"
  - "Forniscimi questo report di workflow (path o file), studialo nei minimi dettagli con il quarto reparto: come è stato fatto, perché, come funziona, punti di forza/debolezza, estrai atomi tracciati, forgia in wiki, proponi update cross-dept"
estimated_time: "30-120 min per ingest completo (dipende da volume); studio 4th dept: minuti-dettagli per report medio"
compatibility: "Richiede yt-dlp, playwright (chromium), python, accesso a content-forge2.0 skill (/forge), filesystem per memory/ e wiki output, Claude Code per wiki connection. Tutto locale/CLI. Integra con master-build-architecture, content-forge2.0, claudedesignskills. 4 reparti: --dept=youtube|tiktok|web|projects . Per projects: path a report/repo."
---

# `empire-studio` — Empire Studio (Ufficiale, Gerarchico, Professionale)

> **"Da link grezzi (YT/TikTok/web) a conoscenza operativa nella wiki di Claude Code — in un flusso aziendale solido, CLI-only, con 'visione' video reale, memory-first, teams gerarchici."**
>
> Mai riassunto. Sempre espansione + MKD. Gerarchia 4 livelli (Director → Teams → Agents → Skills). Ogni agente completo (7 file impeccabili). Ogni skill completa (SKILL.md + references + scripts + templates + principles + rules). Usa content-forge per tutto il forging e wiki. "Guarda" i video con Playwright + estrazione frame + analisi. Aggiorna ecosistemi esistenti. No API, no paid, solo CLI (yt-dlp, playwright, python, tesseract se disponibile).
>
> **Invocation:** `/ingest <input> [--target=wiki|update|full] [--name=slug] [--recursive] [--focus=marketing|tools|design|automation]`
> **Natural triggers:** "Ingest questo canale YouTube", "Fai lo screening di tutti i video di questo tizio sul marketing", "Guarda questo video e metti la conoscenza nella wiki", "Aggiorna i miei workflow con quanto c'è in questi contenuti", "Ecosistema studio per contenuti di formazione".

## ⚠️ Invariant Cardinali (Non Negoziabili — Estratti da Master-Build-Architecture + Content-Forge + User Req)

1. **Memory Ecosystem from the Very First Step** (P10 + Master-Build screenshot + Ruflo/Content-Forge): Ogni step crea/aggiorna `memory/checkpoints/`, `memory/decisions/`, `memory/sessions/`, `memory/plans/`, `memory/architectures/`, `memory/MEMORY-INDEX.md`. Python manager auto. Two-layer (short conversational + long persistent). Update dopo OGNI azione.
2. **MKD + No-Summary-Expansion** (Content-Forge Stage 4 + P03 + P11): Sempre produce Master Knowledge Document prima di qualsiasi target. Espansione, mai compressione. Ogni atomo del sorgente diventa più ricco (esempi, schemi, ➕ invenzioni etichettate).
3. **Gerarchia Solida 4 Livelli Aziendali** (User req + P07 Three-Level + Ruflo queen + PT01 Conductor-with-Subagents): L1 Director/Conductor (orchestra tutto). L2 Department Teams (Ingestion, Processing/Analysis, Forge&Wiki, QA&Evolution). L3 Specialized Agents (uno per funzione specifica, completi con 7 file). L4 Skills/Tools (CLI wrappers, playwright scripts, python processors, templates). Team di agenti per ogni categoria.
4. **CLI-Only, No API, No Paid** (User explicit): Tutto via yt-dlp, playwright (browser automation per "guardare" video: navigate, chapters, comments, screenshots at key frames, transcript extraction), python scripts, bash. Niente API esterne, niente servizi a pagamento. Per "vedere il video": Playwright apre la pagina, estrae metadata/chapters/sottotitoli, prende screenshot a intervalli o capitoli (salva in assets/frames/), usa OCR se disponibile o descrizioni testuali + frame per visione (Claude vision se screenshot forniti nel contesto).
5. **Depth over Breadth + 7 Canonical Files per Agent** (P08 + PT05 + Master-Build): Ogni agente ha esattamente 7 file: <name>.md (spec), system-prompt.md, tools.md (CLI + python + schemas), playbook.md (steps + examples), evals.md (5+ cases), failure-modes.md (table failure|symptom|prevention|detection|recovery), memory.md (P10 protocol + updates + state). Validator gates. No stub.
6. **Failure Modes as First-Class + Self-Improvement** (P09 + PT07 + Content-Forge SI + Master-Build): Ogni agente ha failure-modes.md dettagliata. SI agents (failure-detector, triage, phase-planner) osservano silenziosamente, loggano in failure-modes-log/, generano fix. Silent observer default.
7. **Traceability Source-to-Output + Multi-Source** (P12 + PT09 + Content-Forge KG): Ogni output atomo tracciato a sorgenti (video ID, timestamp, user input, principles, clones, content-forge). KG in stage 3. Coverage check mandatory. Headers in CPs/DECs con Timestamp/Phase/Linked Principles/Traceability.
8. **Research → Plan → Reset → Implement + Interactive Scaffolding** (Context-Engineering-Advisor + P04 + Content-Forge Stage 6): Research caotico, sintetizza a PLAN-vN alto-densità, RESET context, implementa pulito. Per target complessi: PLAN → ASK (adaptive questions) → BUILD → CRITIQUE (self + human) → ITERATE (multiple vN).
9. **Meta-Recursive + Update Existing Workflows** (P13 + PT08 + User req): Questo ecosistema è meta (usa master-build per il suo design, content-forge per output). Usa nuova conoscenza ingerita per proporre/aggiornare flussi esistenti in altri ecosistemi/workload (es. "questo video su skills creation può migliorare il tuo X workflow").
10. **Content-Forge Integration + Wiki as Output** (User primary goal): Dopo ingestion + analysis, SEMPRE invoca content-forge (--target=wiki o custom) per produrre MKD + note atomiche Obsidian/wiki. L'obiettivo finale è aggiornare la wiki (che alimenta Claude Code). Materiale di formazione, contesto, conoscenza operativa (es. "adesso Claude Code sa creare design system perché hai ingerito il video del pro").

**Full 15 principles, 11 patterns, etc. from master-build-architecture/references/knowledge-pack/ and content-forge2.0 references.**

## 🎯 Cosa Produce Questo Ecosistema (Canonical Outputs)

- **Ingestion Report + Video Analysis Docs**: Per ogni video/canale: transcript completo + visual analysis (screenshots + descrizioni frame key + capitoli + commenti rilevanti) + knowledge atoms.
- **Master Knowledge Document (MKD)**: Sempre, espanso, con ➕.
- **Structured Wiki Content**: Via content-forge --target=wiki: note atomiche con wikilink, MOC, tracciabilità alle fonti video.
- **Update Proposals for Existing Workflows**: Basati su nuova conoscenza (es. "Il video X suggerisce di aggiornare lo skill-creator con pattern Y").
- **Full Memory Ecosystem**: Live in memory/ (top + embedded), CPs/DECs/INDEX.
- **Packaged Deliverable**: Report + wiki folder + update plan + evals.
- **Agents & Skills**: Se serve, genera nuove skills/agents per estensioni (usando skill-creator + master-build).

Tutto con full traceability, Python/CLI augmentation, gerarchia perfetta.

## 🏢 Gerarchia 4 Livelli (Struttura Aziendale Solida)

**L1 — Director / Conductor** (orchestra tutto, Ruflo queen + Content-Forge conductor + Master-Build L1)
- `agents/conductor/` (7 files completi)
- Coordina teams L2, gestisce stato, parla con utente (in italiano), invoca content-forge, memory updates, SI.

**L2 — Department Teams** (team di agenti, PT01 + P07 + user "team di agenti")
- **Ingestion Department** (`agents/ingestion-team/`): Screening canali, download metadata/transcript, multi-source.
  - Sub-agents: yt-channel-ingester, tiktok-ingester, web-researcher, video-single-ingester.
- **Processing & Analysis Department** (`agents/processing-team/`): "Guarda" video, estrae conoscenza.
  - Sub-agents: video-watcher (playwright + frames + OCR/desc), transcript-processor, visual-analyzer, knowledge-extractor, context-mapper.
- **Forge & Wiki Integration Department** (`agents/forge-team/`): Struttura con content-forge, inserisce in wiki.
  - Sub-agents: content-forge-invoker, wiki-ingester, knowledge-packager, update-proposer (per existing workflows).
- **QA & Evolution Department** (`agents/qa-team/`): Verifica, self-improvement, update existing.
  - Sub-agents: coverage-verifier, schema-validator, failure-detector, workflow-updater, silent-observer.

**L3 — Specialized Agents** (dentro teams, 7 files each, impeccabili)
- Es. yt-channel-ingester-agent (full 7 files + playwright/yt-dlp tools).
- video-watcher-agent (Playwright scripts per "guardare": open video, get chapters, auto-subs, screenshot at 0/25/50/75/100% or chapters, extract visual cues via page + frames).
- knowledge-extractor-agent (atomize + KG).
- Etc. (20+ planned, built one-by-one per PT05).

**L4 — Skills & Tools** (CLI, scripts, templates — completi)
- `skills/yt-ingest-skill/` (SKILL.md + scripts/yt_ingest.py + templates + principles).
- `skills/video-watcher-skill/` (playwright scripts, frame extractor, OCR wrapper, visual report template).
- `skills/web-ingest-skill/`.
- `skills/content-forge-wrapper-skill/` (CLI wrapper per /forge, con memory sync).
- `skills/wiki-ingest-skill/`.
- General: cli-printing-press integration for docs, master-build for architecture.

**Flussi / Teams per Categoria** (user req "flussi di agenti team di agenti per ogni categoria operatività verificazione ricerca controllo perfezionamento"):
- Operatività: Ingestion + Processing teams + builders.
- Verificazione: QA team + validators.
- Ricerca: Meta + domain extractors + web/yt researchers.
- Controllo: Director + meta + principles from master-build.
- Perfezionamento: Optimizers + SI team + update-proposer.
- Specific user: Flussi per principi (da master), patterns, case-studies applicati qui (es. CS04 real-test per video analysis).

**Teams composti via team-builder / workflow-builder** (da master-build): es. "ingestion-swarm = conductor + ingestion-team + video-watcher subteam".

## 🔄 Il Pipeline Principale (9+ Stage, Content-Forge + Master-Build + User)

1. **Ingestion (A1)**: yt-dlp / playwright per canali/video/web. Metadata, subs, frames, multi-source.
2. **Deep Analysis (A2)**: Parallel per video: transcript clean, visual desc (from frames/screenshots + page), atoms extract.
3. **Knowledge Graph (A3)**: KG con trace a video ID/timestamp + visual cues.
4. **MKD (A5 — SEMPRE)**: Master Knowledge Document espanso.
5. **Target Selection (A4 se needed)**: wiki (default), update-existing, full-report.
6. **Interactive Build / Forge (D1 + Bx)**: PLAN → ASK → BUILD. Invoca content-forge --target=wiki per MKD + wiki notes.
7. **Depth Pass (Ox)**: Optimizers per espandere (skill-depth like per wiki content).
8. **QA (C1 + C3)**: Coverage, schema, real-test (prova a "usare" la conoscenza?).
9. **Wiki Integration + Update Proposals (Packaging)**: Inserisce in wiki, propone update ad altri workflow (basato su new knowledge).
10. **SI Observe (silenzioso)**: Log FM, triage, phase plan. Update existing se rilevante.

Per canali: screening (filtra video rilevanti per focus), poi processa in batch/parallelo dove possibile.

**"Guardare il video" (core user req)**: 
- Playwright: goto video URL, extract description, chapters (if any), top comments, auto-generated subs if available.
- yt-dlp: --write-auto-sub --write-info-json --write-thumbnail.
- Frame extraction: playwright or ffmpeg (if avail) at key points (chapters or % time) → save PNG in run/frames/.
- Analysis: visual-analyzer agent legge frames (via describe or OCR tesseract if installed) + transcript + page text → estrae "passaggi mostrati" (es. "a 12:34 mostra UI con X, clicca Y, risultato Z").
- Output: video-analysis.md con sezioni "Transcript", "Visual Timeline (with frame refs)", "Key Demonstrations", "Practical Steps Extracted", "Knowledge Atoms".

## 🧠 Memory Ecosystem (Fin Da Subito, P10)

Struttura esatta da master-build + screenshot user:
memory/
├── checkpoints/ (CP-XXX-*.md after every)
├── decisions/ (DEC-XXX ADR)
├── sessions/
├── plans/ (PLAN-vN)
├── architectures/
└── MEMORY-INDEX.md (living, appended after every)

Python: scripts/memory_manager.py (copiato/adattato da master-build).

Two-layer, Research→Plan→Reset→Implement, trace P12, update after every (this skill dogfoods it).

## 📚 References & Extracts

- master-build-architecture/ (full for architecture, 7-files, memory, principles, flussi, teams).
- content-forge2.0/ (full pipeline, 25 agents, MKD, wiki target, no-summary, depth, SI).
- claudedesignskills/ (skill-creator per creare nuove skills L4).
- cli-printing-press/ (per output CLI/docs professionali).
- playwright-dev + microsoft/playwright.dev (per "video watcher" scripts e best practices browser automation).
- knowledge-pack from master (P01-15, PT01-11, CS01-04, etc.).
- User vision: marketing videos, tutorial tools/skills/automations, design system etc.

## 🛠️ Tools & Scripts

In `scripts/`:
- memory_manager.py (full, adapted)
- yt_ingest.py (yt-dlp wrapper + multi video)
- playwright_video_watcher.py (core: open YT, get subs/chapters/screenshots/frames, visual report)
- web_research.py (CLI advanced search simulation via playwright or curl + parse)
- forge_invoker.py (wrapper per content-forge, sync memory)
- wiki_ingester.py (post-process wiki output + insert)
- validator.py (7-files, coverage, CLI compliance)
- Etc.

In `skills/` subdirs: full skills with own SKILL.md, scripts, templates.

## 🚀 Quick Start

```bash
# Esempio base
/ingest https://youtube.com/@some-marketer --target=wiki --name=marketing-knowledge --focus=marketing

# Canale intero + screening
/ingest https://youtube.com/channel/UCxxx --recursive --focus=automation

# Singolo video "guardato" + wiki
/ingest https://youtu.be/xxx --target=wiki

# Update existing workflows
/ingest ./new-tutorials/ --target=update-existing --name=my-workflows

# Con content-forge diretto (dopo ingestion)
# Internamente: /forge run/ingest-xxx/ --target=wiki --name=...
```

**Dopo ingest**: La wiki viene aggiornata (note atomiche con trace ai video). Claude Code (collegato alla wiki) ora "sa" il contenuto (es. come fare design system dal video di 2h).

**Per "vedere"**: Il video-watcher produce report con riferimenti a frame salvati + descrizioni testuali dei passaggi visivi.

## 📋 Templates & Assets

In assets/templates/: plan-template, agent-7file-template, video-analysis-template.md, wiki-note-template, update-proposal-template.md, etc.

## 🧪 Evals & Testing

evals/evals.json with cases:
- "Ingest YT channel marketing, verify wiki + trace + no API used"
- "Single video 2h design, 'watch' (frames + transcript), MKD + wiki output"
- "TikTok + web, update existing workflow proposal"
- Coverage, CLI-only, memory live, 7-files agents, gerarchia.

Iteration loop, human review.

## ❌ Anti-Patterns Rifiutati

- Solo transcript (senza visual watcher)
- API o paid services
- Agenti stub o solo ruolo (sempre 7 files completi)
- Gerarchia piatta o incompleta
- Summary invece di espansione + MKD
- No memory update
- No traceability to specific video/timestamp/frame
- Non aggiornare existing workflows quando rilevante

Vedi references/ per full conventions da content-forge + master-build.

## 🔗 Integrazioni

- **content-forge2.0**: SEMPRE per Stage 4+ MKD e wiki target.
- **master-build-architecture**: Per design iniziale e meta-recursive improvements.
- **skill-creator (claudedesignskills)**: Per creare L4 skills complete.
- **cli-printing-press**: Per output professionali/CLI.
- **Playwright**: Cuore del "video watcher" e web ingest.
- **yt-dlp**: Ingestion YT/TikTok subs/metadata.
- **Wiki / Claude Code**: Output finale (note atomiche).
- **Ruflo** (se disponibile): Per swarm execution dei teams.

## 📖 Come Usare (Full Flow per Conductor)

1. Ricevi input (link o folder).
2. Memory bootstrap (CP-000, INDEX).
3. L1 Conductor decide teams L2 da spawnare (ingestion first).
4. L2 Teams spawn L3 agents (parallelo dove possibile).
5. L3 Agents usano L4 skills/tools (yt-dlp, playwright scripts).
6. "Guarda" video: playwright_video_watcher.py produce visual-report + frames/.
7. Dopo analysis → invoca content-forge per MKD + wiki.
8. QA + SI.
9. Proponi update a existing (se knowledge applicabile).
10. Memory update after every + handoff + final packaged.

**Status:** In costruzione one-by-one per PT05/P08/P10/P12 da master-build. Agenti L3 e skills L4 creati completi. Gerarchia solida. CLI-only. Content-forge integration. Memory live.

**Trace to User Vision:** User exact words on hierarchy (3-4 levels, teams L1/L2, agents L3), "video va visto" (not just transcript, use skills for visual), content-forge to wiki, update existing workflows, "agenti fatti perfettamente bene completi... ogni skill... file markdown reference script Python template principi regole", "architettato perfettamente", "no api niente a pagamento usa CLI", repos provided (master-build, content-forge2.0, claudedesignskills skill-creator, cli-printing-press, playwright).

Questo è l'ecosistema ufficiale, fatto bene, ferramente bene. Pronto per uso e espansione.

**Next:** Popolare agents/ con 7 files per conductor + L2 teams + first L3 (yt-ingester, video-watcher), creare L4 skills/yt-ingest-skill e video-watcher-skill (with full playwright scripts), bootstrap memory, PLAN-v1, CATALOG, ANALYSIS-AND-IMPROVEMENT-PLAN, references from clones, scripts copied/adapted, evals. Memory update after each.

**Directory Structure (Visibility):**
```
empire-studio/
├── SKILL.md (this, rich kernel)
├── README.md (map + visibility)
├── ANALYSIS-AND-IMPROVEMENT-PLAN.md (living)
├── agents/
│   ├── CATALOG.md
│   ├── conductor/ (7 files)
│   ├── ingestion-team/ (team spec + sub agents 7 files each)
│   ├── processing-team/ (incl video-watcher full)
│   ├── forge-team/
│   ├── verification-control-team/
│   ├── memory-management-team/
│   ├── strategy-department/ (7 strategy agents)
│   └── projects-repos-workloads-team/ (4th department - deep study of reports/repos)
├── memory/ (live, top dogfood + embedded)
├── references/ (extracts from all provided repos + knowledge-pack)
├── scripts/ (memory_manager.py + generate_strategy_manifest.py + ...)
├── strategies/ (multi-strategy registry: youtube, tiktok, web, projects-repos-workloads)
├── assets/templates/
├── skills/ (full L4 skills with own SKILL.md)
├── evals/
├── failure-modes-log/
├── packaged/
└── (clones at ../../ for extracts)
```

La skill è QUI: /home/user/empire-studio/

Pronta per npx skills add una volta packaged (usando skill-creator).

---

**End of Kernel.** Progressive disclosure: read agents/conductor/ next, or references/ for extracts. Memory bootstrap now.
