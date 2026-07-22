# WF-S5 — YOUTUBE FLIKI: canale auto-producente (Empire Studio integrato)
> Stream: S5 · Window: 24→25/07 · Owner: YouTube Department · **Scope questa settimana: UN video end-to-end** (P4: niente scaling)
> Metodo: competitor in ALTRA lingua che performano → rifatti in ITALIANO → pubblicati con link Manuale in descrizione.
> Dipendenze: DEC-EST-004 (nicchia, veto 24/07) · Gate-S5 (test chiave Fliki 23/07).

## 1. Pipeline 9-stage ( Empire Studio )
| Stage | Nome | Agente | Output |
|---|---|---|---|
| 0 | Memory bootstrap + Strategy Manifest | strategy-dept + memory-architect | nicchia (DEC-004) + focus salvati |
| 1 | Ingestion | yt-channel-ingester / video-single-ingester | 1 video competitor scelto (prova: view/outlier) |
| 2 | Frame extraction | script ffmpeg | frame-NNN.png campionati |
| 3 | Visione reale | video-watcher | struttura narrativa del video |
| 4 | Knowledge atoms | knowledge-extractor | atomi con trace `video-id#ts + frame-NNN` |
| 5 | Verifica | visual-verifier + compliance-auditor | **gate anti-copia**: riformulato, non tradotto letteralmente |
| 6 | Forge + Render | content-forge-invoker → **yt-fliki-renderer** | script IT + video renderizzato (o ladder fallback) |
| 7 | Wiki + Publish | wiki-writer → **yt-seo-publisher** | video live: titolo/desc/tag SEO + **link Manuale in descrizione** |
| 8 | Improve | update-proposer | pattern → ReasoningBank (`youtube/`) |
| 9 | Memory close | checkpoint-manager + memory-architect | `memory/youtube-runs/<run-id>/` + CP |

## 2. Render ladder (se Gate-S5 🔴)
1. **Fliki API** (chiave in `.env` — regola 4 dossier).
2. **Fallback**: script + stock footage (Pexels) + TTS + montaggio ffmpeg.
3. **Defer**: S5 slitta alla settimana prox con `error --wf WF-YT-RENDER`. **Mai** sottrarre ore a S1/S2.

## 3. Struttura directory di run (memory-first)
```
00-MEMORY/  (operativa)
memory/youtube-runs/<run-id>/    checkpoint P10 + log API
memory/knowledge/<video-id>/     atomi + trace P12
memory/workflow-state/youtube/   stato canali + ReasoningBank YT
memory/errors/youtube/           video saltati, errori Fliki, gate anti-copia
```
(questa sottostruttura si crea nel vault second-brain alla prima run; l'operativa resta in 00-MEMORY con `checkpoint --task WF-YT-*`)

## 4. SEO pack pubblicazione (yt-seo-publisher)
- Titolo: pattern competitor + keyword IT ("Claude Code", "AI per lavorare", "automazione").
- Descrizione: 2 righe valore → **link Manuale (S2)** → capitoli → tag.
- CTA verbale nel primo 10%: "risorsa gratuita in descrizione" (Parte 1 del Manuale).

## 5. Revenue path (verità, da P6)
Questa settimana: **0 € diretti** — il video porta lead verso S2 (lead-gen). AdSense/compounding: agosto-settembre. Chi dice altro, mente.

## 6. Regole non negoziabili
chiave solo `.env` · zero stub (validator 0 violazioni) · memory-first dopo OGNI run · tracciabilità P12 su ogni atomo · revenue-before-perfection (ogni video porta al Manuale) · 1 video basta questa settimana.

---
⛓️ P12: `WF-S5#estate-2026` · trace: DEC-EST-004, F-05, R-05, R-07 · gates: Gate-S5 23/07, checkpoint stage 9
