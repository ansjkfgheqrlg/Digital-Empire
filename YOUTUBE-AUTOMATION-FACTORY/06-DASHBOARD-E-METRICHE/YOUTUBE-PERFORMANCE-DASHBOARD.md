# YouTube Automation Factory - Performance Dashboard

- **Ultimo Run ID**: yt-20260914-173159-de40af
- **Data Aggiornamento**: 2026-09-14 17:32:58
- **Canale Target**: N/D (Fase 1 non raggiunta)
- **Video Replicato**: N/D (Fase 2 non raggiunta)
- **Idea Script (Fase 3)**: N/D (Fase 3 non raggiunta)
- **SEO Score Metadati (Fase 5)**: 100.0
- **Stato Fabbrica**: 🔴 BLOCCATA ALLA FASE 5

## 📊 Metriche di Esecuzione (esito REALE di questa run)
| Fase | Componente | Stato | Esito Gate | Criterio |
|---|---|---|---|---|
| F1 | Canale target | Non eseguita | ⚪ N/D | Dati reali del canale fisso @dosementale (Cash Cow Index riportato, non bloccante) |
| F2 | Selezione | Non eseguita | ⚪ N/D | Video maturo (>=24h), non gia' replicato, con velocity >= 3.0x la mediana del canale |
| F3 | Script | Non eseguita | ⚪ N/D | Critic score reale >= 7.5 (motore condiviso 11-APEX-7-CORE) |
| F4 | Produzione | Non eseguita | ⚪ N/D | Schema produzione-spec valido, scene reali da script.md |
| F5 | Pubblicazione | Fallita | 🔴 FAIL | SEO score reale (seo_score.py); upload reale via --upload (opt-in, altrimenti solo preparazione metadati) |
| F6 | Audit | Non eseguita | ⚪ N/D | Manifest published_videos.json (video reale pubblicato) |

## 🧠 Note
Dashboard scritta da `Apex7Orchestrator.write_dashboard()` a fine `execute_workflow`, leggendo lo stato reale della run corrente — non da una pipeline separata. `run_youtube_apex7.py` (pipeline fantasma su un canale 'Dose Mentale' fisso, mai collegata alle fasi reali F1-F6) è stata ritirata in TASK-YT-005: era l'unica altra scrittrice di questo file.
