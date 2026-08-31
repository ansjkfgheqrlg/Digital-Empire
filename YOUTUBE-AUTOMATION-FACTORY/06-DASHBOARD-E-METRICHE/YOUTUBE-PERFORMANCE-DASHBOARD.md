# YouTube Automation Factory - Performance Dashboard

- **Ultimo Run ID**: yt-20260829-173247-26140f
- **Data Aggiornamento**: 2026-08-29 17:33:50
- **Canale Target**: Legami d'Amore (`@Legamidiamore`)
- **Video Replicato**: 7 tocchi che faranno innamorare perdutamente una donna matura di te #psicologia  #relazioni
- **Idea Script (Fase 3)**: 7 Tocchi Che Fanno Innamorare Una Donna Di Te (Funzionano Davvero)
- **SEO Score Metadati (Fase 5)**: 100.0
- **Stato Fabbrica**: 🔴 BLOCCATA ALLA FASE 5

## 📊 Metriche di Esecuzione (esito REALE di questa run)
| Fase | Componente | Stato | Esito Gate | Criterio |
|---|---|---|---|---|
| F1 | Canale target | Completata | 🟢 PASS | Dati reali del canale fisso @dosementale (Cash Cow Index riportato, non bloccante) |
| F2 | Selezione | Completata | 🟢 PASS | Video maturo (>=24h), non gia' replicato, con velocity >= 3.0x la mediana del canale |
| F3 | Script | Completata | 🟢 PASS | Critic score reale >= 7.5 (motore condiviso 11-APEX-7-CORE) |
| F4 | Produzione | Completata | 🟢 PASS | Schema produzione-spec valido, scene reali da script.md |
| F5 | Pubblicazione | Fallita | 🔴 FAIL | SEO score reale (seo_score.py); upload reale via --upload (opt-in, altrimenti solo preparazione metadati) |
| F6 | Audit | Non eseguita | ⚪ N/D | Manifest published_videos.json (video reale pubblicato) |

## 🧠 Note
Dashboard scritta da `Apex7Orchestrator.write_dashboard()` a fine `execute_workflow`, leggendo lo stato reale della run corrente — non da una pipeline separata. `run_youtube_apex7.py` (pipeline fantasma su un canale 'Dose Mentale' fisso, mai collegata alle fasi reali F1-F6) è stata ritirata in TASK-YT-005: era l'unica altra scrittrice di questo file.
