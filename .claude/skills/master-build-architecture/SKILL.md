---
name: master-build-architecture
description: "Skill di architettura madre per progettare architetture complete, swarm di agenti, ecosistemi di memoria, piani e workflow a prova di errore. Usa /master-architect per architettare sistemi multi-agente, creare skill/agenti/team production-ready da una visione grezza, o revisionare/migliorare l'architettura dell'impero. MKD sempre; memory-first dal passo zero; 7 file canonici per agente; failure modes di prima classe; traceability sorgente→output. Motore vendored in master-build-architecture/ (ADR-003 wrap; ADR-009 adozione)."
---

# Master-Build-Architecture — Skill di architettura madre (wrapper)

> **Reparto proprietario:** `06b-FORGE / L2.4 ECOSYSTEM-WORKS` (architetture) con custodia
> `L2.5 METHOD-GUARD` (pattern). Uso trasversale su tutto l'impero.
> **Motore (sorgente eseguibile):** `master-build-architecture/` alla root del repo (origin:
> `gh repo clone ansjkfgheqrlg/master-build-architecture`; versione di riferimento = quella già
> presente su `main`, NON sovrascrivere con il clone freso — vedi CP-20260720-002).
> Kernel: `master-build-architecture/SKILL.md` (10 invarianti, processo 10 fasi, catalogo 25+ agenti).
> Knowledge pack: `master-build-architecture/references/knowledge-pack/`.

## REGOLA D'ORO per Digital Empire (direttiva Max 2026-07-20)
**Quello che architetti NON è "un workflow": è un IMPERO con PIÙ workflow.**
Ogni architettura deve rispettare la mappa a 10 ecosistemi (EMPIRE OS, ADR-001) e il ciclo di fase
a 9 passi (ADR-006): un singolo workflow vive DENTRO un reparto, dentro un ecosistema, dentro la holding.
Mai progettare workflow orfani: ogni artefatto ha intestazione ADR-008 (proprietario/controllore/origine/governo).

## Le 10 invarianti applicate all'impero
1. Memory-first dal passo zero → `company/Memory/` (ADR-002) + memory/ locale per progetto.
2. MKD + mai riassunti (espansione; invenzioni `➕`).
3. PLAN → ASK → BUILD → CRITIQUE → ITERATE (nessun output diretto su target complessi).
4. Tre livelli: kernel + specialisti + tools.
5. 7 file canonici per agente (spec/system-prompt/tools/playbook/evals/failure-modes/memory).
6. Failure modes di prima classe (tabella failure|sintomo|prevenzione|rilevamento|recupero).
7. Traceability sorgente→output (KG; coverage check).
8. Research → Plan → RESET → Implement.
9. Swarm Ruflo (hierarchical/mesh/pipeline) dove≥2 aree disgiunte (già ADR-006).
10. Meta-ricorsione: questa skill migliora le skill (via FORGE-AGENT-SKILL + content-forge).

## Uso nell'impero
- Revisioni architetturali complete → `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md` (baseline 2026-07-20).
- Architettura di nuovi ecosistemi/reparti/workflow → processo 10 fasi del kernel + registrazione ADR-008.
