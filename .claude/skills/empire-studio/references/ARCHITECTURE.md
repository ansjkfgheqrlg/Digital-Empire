# Empire Studio - Architettura Canonica (MKD)

> Workflow gerarchico per ingerire conoscenza da YouTube / TikTok / Web /
> Progetti-Repo, "guardare" davvero i video, forgiarla via content-forge e
> versarla nella wiki di Digital Empire (che alimenta Claude Code).
> Tutto CLI-only, no API, no paid. La visione la fa Claude.

## 0. Cos'e' (e cosa NON e')
- **E'** un *workflow / ecosistema*: organizzazione gerarchica con reparti,
  agenti che usano skill, skill di calibro diverso, controllori.
- **Non e'** una singola skill ne' un singolo agente. L'entrypoint `/empire`
  e' solo la porta: dietro c'e' lo swarm.

## 1. I 4 livelli
```
L1  Conductor (Director / queen ruflo)         orchestra, parla con l'utente, stato+memory
L2  Reparti (Department Teams)                  ognuno con un Lead + skill di reparto
L3  Agenti specialisti (30+, 7 file ciascuno)   i lavoratori
L4  Skill (a tier di calibro)                   gli strumenti che gli agenti impugnano
```

## 2. I 9 reparti (L2)
**Ricerca / Ingestion (4 simmetrici):**
1. YouTube Department
2. TikTok Department
3. Web Department
4. Projects/Repos/Workloads Department (deep study, MAI modifica l'originale)

**Servizi & governance (motore + controllori):**
5. Processing & Vision Department (servizio condiviso: frame + Claude-vision)
6. Forge & Wiki Department (orchestrazione content-forge -> wiki + update proposals)
7. Strategy Department (multi-strategia)
8. Verification & Control Department (controllori)
9. Memory Management Department (gestione ecosistema di memoria)

## 3. Roster agenti L3 (target >= 30, tutti 7-file reali)
- **conductor/**: conductor
- **youtube-department/**: department-lead, yt-channel-ingester, yt-screening, video-single-ingester
- **tiktok-department/**: department-lead, tiktok-ingester, tiktok-trend-scout
- **web-department/**: department-lead, web-researcher, site-crawler, doc-extractor
- **projects-repos-workloads-department/**: department-lead, workflow-deep-analyzer, repo-deep-study, project-knowledge-extractor, workload-comparator
- **processing-vision-department/**: department-lead, frame-extractor, video-watcher (Claude-vision), transcript-processor, knowledge-extractor, context-mapper
- **forge-wiki-department/**: department-lead, content-forge-invoker, wiki-writer, knowledge-packager, update-proposer
- **strategy-department/**: coordinator, applicator, controller, improver, department-strategist, content-type-strategist, meta-strategy-manager
- **verification-control-department/**: lead, visual-verifier, coverage-controller, compliance-auditor, error-triage-controller, silent-observer, real-tester
- **memory-management-department/**: lead, memory-architect, checkpoint-manager, decision-codifier, bug-error-tracker, session-archiver, update-propagator, memory-auditor
Totale pianificato: ~45 agenti. (Costruiti depth-first, reparto per reparto.)

## 4. Tier delle skill (L4)
- **Tier-0 (orchestrazione, governano altre skill):** empire-orchestration,
  strategy-manifest, memory-ecosystem, verification.
- **Tier-1 (di reparto):** youtube-pipeline, tiktok-pipeline, web-pipeline,
  projects-study, forge-wiki.
- **Tier-2 (funzionali, con script reale):** yt-ingest, tiktok-ingest,
  web-research, repo-study, frame-extractor, video-vision, transcript-clean,
  content-forge-bridge, wiki-writer, update-proposer, cli-doc.

## 5. La pipeline (per reparto, simmetrica)
```
INPUT (/empire <link|path> --dept=...)
  -> Stage 0  Memory bootstrap (CP-000 run) + Strategy Manifest
  -> Stage 1  Ingestion        (yt_ingest.py / web_research / repo reader)
  -> Stage 2  Frame extraction  (frame_extractor.py, ffmpeg)  [solo video]
  -> Stage 3  VISIONE           Claude legge i PNG -> video-analysis.md reale
  -> Stage 4  Knowledge atoms   (con trace P12) + KG
  -> Stage 5  Verifica          (visual-verifier: frame reali? descrizioni vere?)
  -> Stage 6  Forge             /forge <material> --target=wiki  (content-forge)
  -> Stage 7  Wiki write        wiki_writer.py -> second-brain-vault/wiki/
  -> Stage 8  Update proposals  update_proposer.py (vs workflow esistenti)
  -> Stage 9  Memory close      CP finale + INDEX + agent/knowledge-state
```

## 6. Il "video va visto" - protocollo reale (la correzione)
Errore del primo tentativo: uno script che rifaceva lo stesso screenshot e
scriveva descrizioni inventate. Correzione:
1. `frame_extractor.py`: yt-dlp scarica il video; ffmpeg estrae frame a
   capitoli (da `info.json`) o a intervalli/% / scene-change -> `frames/frame-NNN.png`
   con `frames/manifest.json` (frame -> timestamp).
2. **Claude (agente video-watcher) legge i PNG** con lo strumento Read (visione
   nativa) e descrive cosa si vede DAVVERO: UI, click, demo, risultati a schermo,
   "passaggi che dal transcript non si capiscono".
3. Output `video-analysis.md`: Transcript | Visual Timeline (frame+desc reali) |
   Key Visual Passages | Knowledge Atoms (trace `video-id#ts + frame-NNN.png`).
Nessuna API. Costo: zero (la visione e' inclusa in Claude Code).

## 7. Orchestrazione (ruflo / swarm)
- Topologie: **hierarchical** (queen=Conductor, comando), **pipeline** (gli stage
  1->9), **mesh** (verification <-> memory). Principi ruflo.
- Quando i tool MCP ruflo sono presenti: `swarm_init`, `agent_spawn`,
  `memory_store`. `ruflo_bridge.py` emette i comandi.
- Fallback (ambiente attuale, ruflo non attivo): il Conductor orchestra gli
  agenti via il tool Task/Agent di Claude Code + `memory_manager.py`. Stesso
  organigramma, stessa pipeline.

## 8. Repo fornite -> ruolo nell'architettura
- master-build-architecture -> principi P01-P15 / pattern / anti-pattern / 7-file / memory.
- content-forge2.0           -> motore forging -> wiki (/forge --target=wiki).
- claudedesignskills/skill-creator -> formato/creazione skill L4.
- cli-printing-press         -> output CLI/docs (cli-doc-skill).
- playwright.dev             -> browser per web-research + fallback frame.
- ruflo                      -> swarm topologie + memory_store.

## 9. Stato di costruzione
Vedi `agents/CATALOG.md` per lo stato REALE (costruito vs pianificato) di ogni
agente e skill. Nessun "fatto" senza che `validator.py` dia 0 violazioni.
