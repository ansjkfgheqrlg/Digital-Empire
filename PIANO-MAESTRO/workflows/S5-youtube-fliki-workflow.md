# WORKFLOW S5 — YouTube Fliki Empire Studio (Versione Operativa Completa)

**Owner:** Chief Forge Department + YouTube Department  
**Goal:** Costruire un canale YouTube completamente automatico con 1 video end-to-end + architettura scalabile  
**Metodo:** Empire Studio 9 Stage + content-forge2.0 + ruflo + Memory Ecosystem

---

## 1. Obiettivo

- Generare video in italiano da competitor stranieri performanti
- Pubblicare automaticamente su YouTube
- Inserire link al Manuale Claude Code per lead generation
- Costruire un sistema che migliora da solo (ReasoningBank)

---

## 2. Pipeline a 9 Stage (Empire Studio)

| Stage | Nome | Agente Principale | Output | Memory Hook |
|-------|------|-------------------|--------|-------------|
| **0** | Memory Bootstrap + Strategy | memory-architect + department-lead | Strategy Manifest + Nicchia | ✓ |
| **1** | Ingestion | yt-channel-ingester + yt-screening | videos.json | ✓ |
| **2** | Frame Extraction | frame_extractor | frames/*.png | ✓ |
| **3** | Visione Reale | video-watcher (Claude) | video-analysis.md | ✓ |
| **4** | Knowledge Atoms | knowledge-extractor | atoms/ | ✓ |
| **5** | Verifica | visual-verifier | verification-report | ✓ |
| **6** | Forge + Render | **yt-fliki-renderer** | video.mp4 + render.json | ✓ |
| **7** | Wiki + Publish | **yt-seo-publisher** | YouTube URL + publish.json | ✓ |
| **8** | Improve | **yt-performance-analyzer** | performance-report + ReasoningBank | ✓ |
| **9** | Memory Close | checkpoint-manager | CP finale | ✓ |

---

## 3. Agenti Forgiati (Fase 1)

- ✅ `yt-fliki-renderer` (7 file)
- ✅ `yt-seo-publisher` (7 file)
- ✅ `yt-performance-analyzer` (7 file)
- ✅ `yt-niche-scout` (7 file)

---

## 4. Ruflo Orchestration

- **Queen:** department-lead (YouTube Department)
- **Topology:** Hierarchical + Pipeline
- **Memory:** ruflo `memory_store` su ogni stage

---

## 5. Memory Path

```
company/Memory/ESTATE-WORKSHOP/stream-S5/
├── youtube-runs/<run-id>/
├── ReasoningBank/
└── checkpoints/
```

---

## 6. Regole Non Negoziabili

- Chiave Fliki e YouTube API solo in `.env`
- Ogni video deve contenere link al Manuale
- Memory checkpoint dopo ogni stage
- Zero stub

---

**Creato da Chief Forge Department** — 20 Luglio 2026