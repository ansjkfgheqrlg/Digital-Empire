---
Type: TOOL
Status: Active
Tags: #workflow #agenti #ingestion #knowledge #cli #ricostruzione
Created: 2026-06-08
Last updated: 2026-06-08
---

# Empire Studio

## Overview
Workflow gerarchico (non una singola skill) che trasforma link grezzi — YouTube,
TikTok, siti web, progetti/repo — in conoscenza operativa dentro la wiki di
Digital Empire. Caratteristica distintiva: **"guarda" davvero i video** (frame
estratti con yt-dlp+ffmpeg e analizzati dalla visione nativa di Claude — niente
API, niente costi). Forgia il materiale via content-forge e lo versa nella wiki.

## Dettagli
- **Posizione:** `SKILL & Agenti/Empire Studio Suite/empire-studio/` ·
  pacchetto pulito Windows-safe in `packaged/empire-studio-clean.zip`.
- **Architettura:** 4 livelli (L1 Conductor → L2 9 reparti → L3 50 agenti a 7
  file reali → L4 20 skill su 3 tier di calibro). Entrypoint `/empire <link|path>
  [--dept=youtube|tiktok|web|projects]`.
- **9 reparti:** YouTube, TikTok, Web, Projects/Repos (ricerca, simmetrici) +
  Processing&Vision, Forge&Wiki, Strategy, Verification&Control, Memory Management.
- **Motore reale (14 script CLI):** ingest (yt-dlp), frame extraction (ffmpeg),
  visione (Claude legge i PNG), forge-bridge (/forge), wiki-writer (scrive in
  `second-brain-vault/wiki/`), memory manager (16 categorie, nomi Windows-safe),
  validator anti-stub, strategy manifest, ruflo_bridge (swarm), packaging.
- **Garanzie anti-errore:** `validator.py` (cancello anti-stub, 0 violazioni) +
  `catalog_status.py` (stato letto dal filesystem, non dichiarato). Risolve i
  problemi del primo tentativo cloud (stub spacciati per "fatti", video-watcher
  finto, nomi file non estraibili su Windows → errore 0x80070057).
- **Origine:** ricostruzione drastica (v2.0, 2026-06-08) del workflow generato da
  un agente cloud, dopo audit completo della cronologia chat.

## Connessioni
- [[Map - Agenti]]
- [[Map - Skill_And_Agenti]]
- [[Map - Progetti_Claude]]
- [[Map - System_Omega_-_Creazione_Proggetti_E_Skill_Per_Claude]]
