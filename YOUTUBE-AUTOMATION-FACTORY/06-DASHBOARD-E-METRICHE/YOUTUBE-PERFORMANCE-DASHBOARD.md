# YouTube Automation Factory - Performance Dashboard

- **Ultimo Run ID**: yt-20260803-095012-1d8f7d
- **Data Aggiornamento**: 2026-08-03 09:50:16
- **Canale Target**: Dose Mentale (`@dosementale`)
- **Video Replicato**: Hai 70-80 anni? SMETTI di Camminare tanto e fai SOLO Queste 2 Cose
- **Idea Script (Fase 3)**: Dopo i 70 anni, camminare non basta più: le 2 cose che contano davvero
- **SEO Score Metadati (Fase 5)**: 100.0
- **Stato Fabbrica**: 🟢 OPERATIVA (6/6 fasi reali PASS)

## 📊 Metriche di Esecuzione (esito REALE di questa run)
| Fase | Componente | Stato | Esito Gate | Criterio |
|---|---|---|---|---|
| F1 | Canale target | Completata | 🟢 PASS | Dati reali del canale fisso @dosementale (Cash Cow Index riportato, non bloccante) |
| F2 | Selezione | Completata | 🟢 PASS | Video maturo (>=24h) con velocity reale >= 20.0 viste/ora |
| F3 | Script | Completata | 🟢 PASS | Critic score reale >= 7.5 (motore condiviso 11-APEX-7-CORE) |
| F4 | Produzione | Completata | 🟢 PASS | Schema produzione-spec valido, scene reali da script.md |
| F5 | Pubblicazione | Completata | 🟢 PASS | SEO score reale (seo_score.py) |
| F6 | Audit | Completata | 🟢 PASS | Manifest published_videos.json (video reale pubblicato) |

## 🧠 Note
Dashboard scritta da `Apex7Orchestrator.write_dashboard()` a fine `execute_workflow`, leggendo lo stato reale della run corrente — non da una pipeline separata. `run_youtube_apex7.py` (pipeline fantasma su un canale 'Dose Mentale' fisso, mai collegata alle fasi reali F1-F6) è stata ritirata in TASK-YT-005: era l'unica altra scrittrice di questo file.
