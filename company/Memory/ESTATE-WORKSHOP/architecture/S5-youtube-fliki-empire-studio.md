# ARC-001 — Architettura Workflow S5: YouTube Fliki + Empire Studio

**Data:** 2026-07-20  
**Owner:** Chief Forge Department  
**Stream:** S5  
**Status:** ATTIVO

---

## 1. Visione

Trasformare S5 in un **workflow Empire Studio completo** (9 stage) con integrazione **content-forge2.0**, **ruflo** e **Memory Ecosystem**.

---

## 2. Reparti Coinvolti

- YouTube Department
- Processing & Vision Department
- Forge & Wiki Department
- Strategy Department
- Verification & Control Department
- Memory Management Department

---

## 3. Pipeline a 9 Stage (Empire Studio)

| Stage | Nome | Agente Principale | Output | Memory |
|-------|------|-------------------|--------|--------|
| 0 | Memory Bootstrap + Strategy | memory-architect | Strategy Manifest + Nicchia | ✓ |
| 1 | Ingestion | yt-channel-ingester / yt-screening | videos.json | ✓ |
| 2 | Frame Extraction | frame_extractor | frames/*.png | ✓ |
| 3 | Visione Reale | video-watcher | video-analysis.md | ✓ |
| 4 | Knowledge Atoms | knowledge-extractor | atoms/ | ✓ |
| 5 | Verifica | visual-verifier | verification-report | ✓ |
| 6 | Forge + Render | content-forge2.0 + yt-fliki-renderer | video.mp4 | ✓ |
| 7 | Wiki + Publish | wiki-writer + yt-seo-publisher | YouTube live + wiki | ✓ |
| 8 | Improve | WF-YT-IMPROVE | ReasoningBank update | ✓ |
| 9 | Memory Close | checkpoint-manager | CP finale | ✓ |

---

## 4. Agenti da Forgiare (G4-G5)

Usando **content-forge2.0** + **master-build-architecture**:

- `yt-fliki-renderer` (7 file)
- `yt-seo-publisher` (7 file)
- `yt-performance-analyzer` (7 file)
- `yt-niche-scout` (7 file)

---

## 5. Ruflo Orchestration

- **Queen:** department-lead (YouTube)
- **Swarm:** hierarchical + pipeline
- **Memory Store:** ruflo memory_store per ogni stage

---

## 6. Memory Path

`company/Memory/ESTATE-WORKSHOP/stream-S5/youtube-runs/<run-id>/`

---

**Creato da:** Chief Forge Department — 20 Luglio 2026