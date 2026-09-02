# Empire Studio - CATALOG agenti & skill (STATO REALE)

> Questo file dice la verita': cosa e' COSTRUITO (7 file reali, validator-pass) e
> cosa e' PIANIFICATO. Nessun "fatto" senza riscontro sul filesystem.
> Legenda: ✅ costruito e validato · 🟡 in lavorazione · ⬜ pianificato

_Ultimo aggiornamento: Fase 1 in corso — MOTORE PROVATO end-to-end su video reale._

> ✅ **Milestone reale:** la pipeline ingest → frame veri (ffmpeg) → visione di
> Claude → `video-analysis.md` reale è stata eseguita su un video YouTube vero
> (jNQXAC9IVRw) e il `validator.py` dà 0 violazioni. Vedi `runs/test-youtube-001/`.

## L1 Conductor
- ⬜ conductor (7 file) — Fase 1

## L2/L3 Reparti di ricerca
### YouTube Department
- ⬜ department-lead · ⬜ yt-channel-ingester · ⬜ yt-screening · ⬜ video-single-ingester  (Fase 1)
### TikTok Department
- ⬜ department-lead · ⬜ tiktok-ingester · ⬜ tiktok-trend-scout  (Fase 2)
### Web Department
- ⬜ department-lead · ⬜ web-researcher · ⬜ site-crawler · ⬜ doc-extractor  (Fase 2)
### Projects/Repos/Workloads Department
- ⬜ department-lead · ⬜ workflow-deep-analyzer · ⬜ repo-deep-study · ⬜ project-knowledge-extractor · ⬜ workload-comparator  (Fase 2)

## L2/L3 Servizi & governance
### Processing & Vision Department
- ⬜ department-lead · ⬜ frame-extractor · ✅ **video-watcher (Claude-vision, 7 file, validato)** · ⬜ transcript-processor · ⬜ knowledge-extractor · ⬜ context-mapper  (Fase 1)
### Forge & Wiki Department
- ⬜ department-lead · ⬜ content-forge-invoker · ⬜ wiki-writer · ⬜ knowledge-packager · ⬜ update-proposer  (Fase 1)
### Strategy Department
- ⬜ coordinator · ⬜ applicator · ⬜ controller · ⬜ improver · ⬜ department-strategist · ⬜ content-type-strategist · ⬜ meta-strategy-manager  (Fase 3)
### Verification & Control Department
- ⬜ lead · ⬜ visual-verifier · ⬜ coverage-controller · ⬜ compliance-auditor · ⬜ error-triage-controller · ⬜ silent-observer · ⬜ real-tester  (Fase 3)
### Memory Management Department
- ⬜ lead · ⬜ memory-architect · ⬜ checkpoint-manager · ⬜ decision-codifier · ⬜ bug-error-tracker · ⬜ session-archiver · ⬜ update-propagator · ⬜ memory-auditor  (Fase 3)

**Totale agenti pianificati: ~45 · Costruiti & validati: 0 (Fase 0 = fondazione/motore)**

## Skill (L4)
### Tier-0 orchestrazione
- ⬜ empire-orchestration · ⬜ strategy-manifest · ⬜ memory-ecosystem · ⬜ verification
### Tier-1 di reparto
- ⬜ youtube-pipeline · ⬜ tiktok-pipeline · ⬜ web-pipeline · ⬜ projects-study · ⬜ forge-wiki
### Tier-2 funzionali (con script reale)
- ✅ **video-vision (script assemble_analysis.py, validato)** · ⬜ yt-ingest · ⬜ frame-extractor · ⬜ transcript-clean · ⬜ web-research · ⬜ repo-study · ⬜ content-forge-bridge · ⬜ wiki-writer · ⬜ update-proposer · ⬜ cli-doc

## Script motore (scripts/)
- ✅ memory_manager.py    (Windows-safe, 16 categorie, testato)
- ✅ validator.py         (cancello anti-stub, testato)
- ✅ setup_check.py       (prerequisiti, testato)
- ✅ yt_ingest.py         (yt-dlp ingest + screening canali, testato su video reale)
- ✅ frame_extractor.py   (ffmpeg, frame VERI ai capitoli, testato: 6 frame estratti)
- ✅ wiki_writer.py       (scrive in second-brain-vault/wiki + log.md)
- ⬜ update_proposer.py · ⬜ ruflo_bridge.py · ⬜ generate_strategy_manifest.py  (Fase 1+)
