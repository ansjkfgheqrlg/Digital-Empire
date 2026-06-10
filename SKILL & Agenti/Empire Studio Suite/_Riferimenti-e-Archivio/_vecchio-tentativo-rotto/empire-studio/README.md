# Empire Studio

**Nome ufficiale:** Empire Studio (deciso dall'utente 2026-06-07)

**Cosa è:** Workflow completo, gerarchico, professionale (struttura aziendale con 4 livelli e 4 reparti simmetrici) per ingerire e studiare profondamente conoscenza da:
- YouTube (video e canali)
- TikTok
- Siti web / ricerche avanzate
- **Progetti, repo e altri workload interni** (NUOVO quarto reparto)

**Il quarto reparto (Projects, Repos & Workloads Department):**
- Quando l'utente fornisce un "report" di un altro workflow, una repo, o un progetto, il reparto lo studia nei minimi dettagli:
  - Architettura
  - Decisioni e "perché è stato fatto così"
  - Come funziona
  - Quanto funziona bene (punti di forza, debolezze, anti-pattern)
  - Pattern e principi (usando master-build-architecture, content-forge, ecc.)
- **Non modifica mai l'originale** (solo lettura e analisi via CLI).
- Estrae knowledge atoms con trace preciso (a file/sezione specifica del report/repo).
- Poi la stessa pipeline degli altri reparti: content-forge → MKD → note atomiche nella wiki (con trace).
- Può generare update proposal per workflow esistenti (inclusi gli altri reparti di Empire Studio).

**Come usarlo:**
- Per contenuti video/web: /empire <link> --dept=youtube|tiktok|web
- Per progetti/repo: fornisci il path al report o alla repo. Il quarto reparto lo "studia profondamente" come i video vengono "guardati".

**Struttura:**
- L1: Conductor
- L2: 4 Department Teams (YouTube/Ingestion, TikTok, Web, **Projects-Repos-Workloads**)
- L3: Agenti specializzati (7 file ciascuno)
- L4: Skills complete (SKILL.md + script + template + principles + rules) — ora decine di skills

**Memory, Strategy, Verification:** Pieno supporto (multi-strategie per dept e tipo di contenuto, inclusi progetti; memory ecosystem gestito da agenti; verification & control costanti).

**Stato attuale:** Gerarchia completa + quarto reparto con 8 agenti (workflow-deep-analyzer-agent ha full 7 files; altri specs). Strategy Department full 7 files per Coordinator/Controller/Improver. 15+ skills (frame-extractor, repo-parser, atomic-note-creator, memory-checkpoint, visual-analyzer, etc.). Multi-strategie + generate_strategy_manifest.py. 4 depts simmetrici. CLI-only, Playwright per "visione" video + "passaggi mostrati".

Forniscimi il primo "report di un altro workflow" (path o contenuto) e il quarto reparto lo studierà nei minimi dettagli, estraendo tutto, senza modificare l'originale, e lo porterà nella wiki via content-forge.

Tutto CLI-only, memory-first, 7-file agents, multi-strategie, come richiesto.

**Directory canonica:** /home/user/empire-studio/

**Download per edit locale con Claude Code (importante per evitare errori Windows):**
- Scarica SOLO dalla lista file della piattaforma: `empire-studio-clean.zip` (o empire-studio-clean.tar.gz o empire-studio-super-clean.tar.gz che esclude memory/checkpoints).
- **NON** scaricare o zippare l'intero /home/user/ (contiene altre dir di riferimento come master-build-architecture/ con vecchi file che potevano causare problemi).
- Su Windows: usa **7-Zip** per estrarre in un percorso corto tipo `C:\EmpireStudio` (evita path lunghi + nomi strani).
- Dopo estrazione: `cd EmpireStudio\empire-studio` e apri con Claude Code. Tutti gli agenti, skills (decine), flussi, memory, strategie, 4 reparti sono lì, puliti, pronti per editing locale.
- Se problemi residui: usa la super-clean version (senza checkpoints) o dimmi e preparo versione ancora più minimal.

**Install CLI tools (minimo, ma la struttura è il package):**
- yt-dlp (per download video/metadata)
- playwright (chromium) + python (per "guardare" video via frame extraction + visual analysis "passaggi mostrati")
- python3 + pip (per scripts e parsers)
- (opzionale) ffmpeg per frame extraction avanzata, tesseract per OCR

**Esempio comando base (dopo estrazione locale):**
python scripts/generate_strategy_manifest.py --input-type=projects-report --focus=deep-study --dept=projects

**Riferimenti esterni (non modificare, solo studio):** master-build-architecture/, content-forge2.0/, claudedesignskills/, cli-printing-press/, playwright.dev

**Prossimi passi per utente:**
1. Scarica clean.zip come sopra.
2. Estrai localmente.
3. Invia primo report/repo per deep study con 4th dept (workflow-deep-analyzer full 7 files pronto).
4. Tutto sarà tracciato, memory aggiornato, wiki via forge.

*Crafted with master-build rigor, content-forge pipeline, Playwright for vision, CLI purity, and user exact specs — to deliver production knowledge ingestion.*
