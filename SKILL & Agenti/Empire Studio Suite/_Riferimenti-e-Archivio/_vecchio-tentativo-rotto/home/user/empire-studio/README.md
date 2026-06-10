# Empire Studio

**Nome ufficiale:** Empire Studio (deciso dall'utente 2026-06-07)

**Cosa è:** Workflow completo, gerarchico, professionale (struttura aziendale con 4 livelli e 4 reparti) per ingerire e studiare profondamente conoscenza da:
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
- L2: 4 Department Teams (Ingestion, Processing/Analysis, Forge&Wiki+Verification+Memory, **Projects-Repos-Workloads**)
- L3: Agenti specializzati (7 file ciascuno)
- L4: Skills complete (SKILL.md + script + template + principles + rules)

**Memory, Strategy, Verification:** Pieno supporto (multi-strategie per dept e tipo di contenuto, inclusi progetti; memory ecosystem gestito da agenti; verification & control costanti).

**Stato:** Base completa + quarto reparto aggiunto con agenti iniziali (workflow-deep-analyzer, repo-deep-study, project-knowledge-extractor, workload-comparator, empire-projects-strategist). Pronti per il primo report di workflow da studiare in dettaglio.

Forniscimi il primo "report di un altro workflow" (path o contenuto) e il quarto reparto lo studierà nei minimi dettagli, estraendo tutto, senza modificare l'originale, e lo porterà nella wiki via content-forge.

Tutto CLI-only, memory-first, 7-file agents, multi-strategie, come richiesto.

**Directory:** /home/user/empire-studio/
