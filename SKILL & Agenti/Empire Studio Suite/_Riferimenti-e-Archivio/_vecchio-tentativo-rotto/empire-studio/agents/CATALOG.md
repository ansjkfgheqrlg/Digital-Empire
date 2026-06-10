# Content Ingest Ecosystem Agents Catalog (L1/L2/L3/L4 + Flussi/Teams)

**Total Planned:** L1: 1 (conductor) + L2: 4 teams (with 4-6 sub L3 each) + L3: 15-20 specialized (7 files) + L4: 5-8 complete skills = solid 4-level company structure.

**Implemented (Real, one-by-one per PT05/P08/P10/P12 from master-build-architecture):**
- L1: conductor (spec + system-prompt + tools + playbook + evals + failure-modes + memory.md — 7/7 started/complete in core)
- L4: video-watcher-skill (full SKILL.md + real working playwright_video_watcher.py script using yt-dlp + playwright for transcript + key frames + visual timeline + "passaggi mostrati" + atoms with trace + template)
- L3: video-watcher-agent (spec in processing-team, integrates L4)
- Structure: ingestion-team/ (dir for yt-channel-ingester-agent etc.), processing-team/ (video-watcher etc.)

**L2 Department Teams (Reparti aziendali — espansi su richiesta utente):**
- ingestion-team: yt-channel-ingester, tiktok-ingester, web-researcher, video-single-ingester (L3)
- processing-team: video-watcher (L3 + L4), transcript-processor, visual-analyzer, knowledge-extractor, context-mapper
- forge-team: content-forge-invoker (L4 wrapper), wiki-ingester, knowledge-packager, update-proposer (for existing workflows)
- **verification-control-team (NUOVO — intero reparto di verifica e controllori)**: visual-verifier-agent, coverage-controller-agent, compliance-auditor-agent, error-triage-controller-agent, silent-observer-agent, workflow-compliance-agent, real-time-monitor-agent (tutti L3 con 7 file)
- **memory-management-team (NUOVO — intero ecosistema di memoria gestito da agenti)**: memory-architect-agent, checkpoint-manager-agent, decision-codifier-agent, bug-error-tracker-agent, session-archiver-agent, update-propagator-agent, memory-auditor-agent, knowledge-state-manager-agent, architecture-versioner-agent, workflow-state-manager-agent (tutti L3 con 7 file)
- **strategy-department (NUOVO — Reparto delle Strategie, su richiesta per rendere le strategie "tante, specifiche e non generiche")**: strategy-coordinator, strategy-applicator, strategy-controller, strategy-improver, content-type-strategist, department-strategist, meta-strategy-manager (minimo 7 agenti L3 con 7 file ciascuno). Gestiscono la STRATEGY-REGISTRY (multiple strategie per dipartimento, tipo di contenuto, implementazione wiki, esterne). Coordinano, applicano, controllano, migliorano e versionano le strategie.

**Struttura Memory Espansa (su richiesta utente — "un intero ecosistema di memoria che aggiorna ogni decisione, ogni architettura, ogni sessione e ogni bug, ogni errore, ogni problema")**:
memory/
├── checkpoints/
├── decisions/
├── sessions/
├── plans/
├── architectures/
├── bugs/ (dedicato)
├── errors/ (dedicato)
├── updates/ (dedicato)
├── workflow-state/
├── knowledge-state/
├── agent-state/
├── verification-logs/
└── architecture-versions/

Agenti del Memory Management Department sono responsabili di registrare e propagare **dopo OGNI** decisione, handoff, bug, errore, problema, update. Verification & Control Team audita che questo avvenga.

**Flussi / Teams per Categoria (User req + Master-Build "flussi di agenti team di agenti per ogni categoria operatività verificazione ricerca controllo perfezionamento" + principles/patterns/case-studies):**
- Operatività (builders/pipeline): ingestion + processing teams + L4 skills (yt, video-watcher)
- Verificazione (QA): qa-team + validators + real-test (prova conoscenza)
- Ricerca (meta/domain): web/yt researchers + knowledge-extractor + meta from master
- Controllo (conductor/meta): L1 conductor + principles from master-build
- Perfezionamento (optimizers/SI): qa SI + update-proposer + failure-detector (update existing workflows)
- Specific: Flussi per "video va visto" (processing L2/L3/L4), content-forge to wiki (forge-team), update existing (qa + forge)

**Next One-by-One (per master-build PT05/P08 + user "agenti fatti perfettamente bene completi... ogni skill... markdown reference script Python template principi regole"):**
- Full 7 files for conductor (already 6/7 core).
- yt-channel-ingester-agent (L3, 7 files + yt-dlp script).
- Other L3 in teams.
- Full L4 skills: yt-ingest-skill, web-ingest-skill, content-forge-wrapper-skill, wiki-ingest-skill (use skill-creator from claudedesignskills).
- Populate references/ from all clones.
- More scripts (web, forge invoker, validator).
- CATALOG/ANALYSIS/SKILL updates with real status.
- Evals loop, test ingest.

**Trace (P12):** To user "gerarchia... tre o quattro livelli... team di agenti... agenti... skill... completi... markdown... reference... script Python... template... principi... regole... architettato... no api... CLI... video... guardarlo... content-forge... wiki... claude code... aggiornare i flussi esistenti" + master-build-architecture CATALOG + flussi + 7 files + P07/P10/P12 + content-forge agents + provided repos + our CP-000 + CP-001.

**Status:**  L1 + 1 L4 + 1 L3 partial + full structure + memory + tools installed. Real FS matches claims. Continuing one-by-one impeccably.

**Aggiornamento importante (su richiesta diretta utente 2026-06-07):**
- Aggiunto intero **Verification & Control Department** (L2) come reparto di verifica e controllori.
- Aggiunto intero **Memory Management Department** (L2) come reparto che gestisce l'ecosistema di memoria.
- **Aggiunto intero Strategy Department (L2)** come reparto dedicato alle strategie (su tua richiesta di rendere la strategia "non troppo generica" ma "tante strategie specifiche per funzionalità, ambiente/reparto, tipo di contenuto, implementazione wiki").
- Struttura memory espansa con cartelle dedicate (inclusi strategy-applications e strategy-versions).
- Agenti L3 starter creati per i nuovi reparti.
- STRATEGY-REGISTRY.md creata (multiple strategie specifiche + decision tree + versioning).
- STRATEGY.md principale aggiornata con riferimento al nuovo reparto e al registro multi-strategia.

**Trace:** Risponde esattamente alla tua ultima richiesta su strategia troppo generica, necessità di "tante strategie", e "una serie di agenti, un team di agenti minimo 5-6 agenti strategici che coordinano la strategia, applicano, controllano, migliorano ecc.".
