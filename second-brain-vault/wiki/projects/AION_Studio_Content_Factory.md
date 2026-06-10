---
Type: PROJECT
Status: Active
Tags: #content-factory #agenti #orchestration #ugc #higgsfield #aion-studio
Created: 2026-05-29
Last updated: 2026-05-29
---

# AION Studio — Content Factory (Ecosistema di Agenti)

## Overview
**AION Studio** (*Agentic Intelligent Orchestration Network*) è l'azienda-di-agenti di
Digital Empire per la produzione automatizzata di **video UGC, immagini 4K, motion e
contenuti marketing**. È un orchestration layer gerarchico: un "capo" (Conductor) riceve
un brief, lo scompone e lo instrada a reparti di agenti che producono l'output usando il
motore **Higgsfield** (via `hf-studio`). Vive in `SKILL & Agenti/Ecosistema - Content Factory/`.

## Dettagli

### Architettura (8 reparti, ~24 team, gerarchia a 3 livelli)
- **L3 Reparti/Direzioni:** D1 Strategy · D2 Creative/Production · D3 Operations ·
  D4 Marketing · D5 Quality · D6 Orchestration · D7 Research · D8 Code.
- **L2 Team-Workflow:** un team per workflow (es. "Video UGC").
- **L1 Team-Funzione:** un team per funzione (Soul ID, Image 4K, Motion, Editing…).
- Coordinamento via **message bus** (JSONL) + **project-state** + **handoff** registrati.
- Costruita con metodo [[SPARC_Methodology]] e pattern [[Swarm_Orchestration_Pattern]]
  (Queen→Workers), ispirati a [[Tool_ClaudeFlow_Orchestration]] (Ruflo).

### Cosa è stato costruito (BUILD-1→4 + verificatori)
- `company/org/` (hierarchy, directions, roster YAML) — l'azienda su file.
- `orchestrator/` — 9 script bash: conductor, dispatch, state, bus, agents, mem, verify,
  bootstrap, lib-orch. **Ha prodotto 1 video UGC reale end-to-end** (Soul→Img4K→Motion→Edit).
- `memory/` — ecosistema di memoria persistente (checkpoint CP-001→006, ADR-001→005).
- 3 **agenti verificatori** (gate post-step): integrità codice, output QA, memory auditor.
- `vendor/` — 7 asset: ruflo, content-forge2.0, [[Tool_Copy_Workflow_Orchestration|copy-workflow]],
  marketingskills, product-manager-skills, skill-contradiction-analyzer, cli-printing-press.
- `hf-studio/` — suite Higgsfield: img, video, pipeline, soul, product, batch.

### Stato attuale (resume 2026-05-29)
⚠️ Ecosistema **migrato da sandbox Linux cloud → Windows** (estratto da zip). Codice integro,
ma il motore Higgsfield è **scollegato** (CLI/credenziali/ffmpeg assenti). Prossimo step =
**FASE PORT** (bootstrap ambiente + re-login Higgsfield), poi BUILD-5→8.
Piano completo: `orchestration/PLAN-03-CONTINUATION.md`. Memoria: `orchestration/memory/`.

### Principi non negoziabili (dall'utente)
- Un team di agenti per **ogni singola funzionalità**; team-capo (Queen) sopra ogni reparto.
- Gerarchia esplicita a 3 livelli; tutto coordinato, tracciato, auto-migliorante (SOP vive).
- Riuso totale degli asset installati; costi crediti sotto controllo (budget guard).
- Focus prioritario: **Social/UGC con personaggio ricorrente**.
- Memoria sempre aggiornata: leggere prima di ogni step, scrivere checkpoint dopo.

## Connessioni
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo: i pattern swarm/hive-mind/SPARC che AION incarna.
- [[SPARC_Methodology]] — metodo di pianificazione e build usato in tutto il progetto.
- [[Swarm_Orchestration_Pattern]] — topologia multi-agente (Queen→Workers, mesh).
- [[Tool_Copy_Workflow_Orchestration]] — sistema copy APSOC, reparto D4 Marketing di AION.
