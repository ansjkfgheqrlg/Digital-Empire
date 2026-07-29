# YouTube Automation Factory - Performance Dashboard

- **Ultimo Run ID**: yt-video-20260729-152801
- **Data Aggiornamento**: 2026-07-29 15:28:12
- **Canale Target**: Andrea Ciraolo (`@ciraolone`)
- **Video Replicato**: KIMI K3 ✨ VIBE CODING Tutorial with AI
- **Idea Script (Fase 3)**: Come installare e configurare Claude Code in 5 minuti (Tutorial Completo)
- **SEO Score Metadati (Fase 5)**: 92.5
- **Stato Fabbrica**: 🟡 PARZIALE (fermata alla fase 5, --phase limitato)

## 📊 Metriche di Esecuzione (esito REALE di questa run)
| Fase | Componente | Stato | Esito Gate | Criterio |
|---|---|---|---|---|
| F1 | Scouting | Completata | 🟢 PASS | Niche-gate reale (Cash Cow Index >= 60, cashcow_check.py) |
| F2 | Selezione | Completata | 🟢 PASS | Video maturo (>=24h) con velocity views/ora reale |
| F3 | Script | Completata | 🟢 PASS | Critic score reale >= 7.5 (motore condiviso 11-APEX-7-CORE) |
| F4 | Produzione | Completata | 🟢 PASS | Schema produzione-spec valido, scene reali da script.md |
| F5 | Pubblicazione | Completata | 🟢 PASS | SEO score reale (seo_score.py) |
| F6 | Audit | Non eseguita | ⚪ N/D | Manifest published_videos.json (video reale pubblicato) |

## 🧠 Note
Dashboard scritta da `Apex7Orchestrator.write_dashboard()` a fine `execute_workflow`, leggendo lo stato reale della run corrente — non da una pipeline separata. `run_youtube_apex7.py` (pipeline fantasma su un canale 'Dose Mentale' fisso, mai collegata alle fasi reali F1-F6) è stata ritirata in TASK-YT-005: era l'unica altra scrittrice di questo file.
