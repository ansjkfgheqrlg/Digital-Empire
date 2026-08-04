# YouTube Automation Factory - Performance Dashboard

- **Ultimo Run ID**: yt-20260804-094017-f02687
- **Data Aggiornamento**: 2026-08-04 09:40:20
- **Canale Target**: Dose Mentale (`@dosementale`)
- **Video Replicato**: Familiari Tossici? Ecco In Che Modo Dio Ti Allontana da Loro | Saggezza Biblica
- **Idea Script (Fase 3)**: Familiari tossici: i 3 segnali che Dio ti sta già allontanando da loro
- **SEO Score Metadati (Fase 5)**: 100.0
- **Stato Fabbrica**: 🟢 OPERATIVA (6/6 fasi reali PASS)

## 📊 Metriche di Esecuzione (esito REALE di questa run)
| Fase | Componente | Stato | Esito Gate | Criterio |
|---|---|---|---|---|
| F1 | Canale target | Completata | 🟢 PASS | Dati reali del canale fisso @dosementale (Cash Cow Index riportato, non bloccante) |
| F2 | Selezione | Completata | 🟢 PASS | Video maturo (>=24h), non gia' replicato, con velocity >= 3.0x la mediana del canale |
| F3 | Script | Completata | 🟢 PASS | Critic score reale >= 7.5 (motore condiviso 11-APEX-7-CORE) |
| F4 | Produzione | Completata | 🟢 PASS | Schema produzione-spec valido, scene reali da script.md |
| F5 | Pubblicazione | Completata | 🟢 PASS | SEO score reale (seo_score.py) |
| F6 | Audit | Completata | 🟢 PASS | Manifest published_videos.json (video reale pubblicato) |

## 🧠 Note
Dashboard scritta da `Apex7Orchestrator.write_dashboard()` a fine `execute_workflow`, leggendo lo stato reale della run corrente — non da una pipeline separata. `run_youtube_apex7.py` (pipeline fantasma su un canale 'Dose Mentale' fisso, mai collegata alle fasi reali F1-F6) è stata ritirata in TASK-YT-005: era l'unica altra scrittrice di questo file.
