---
Type: TOOL
Status: Active
Tags: #orchestration-layer #cognitive #problem-solving #sistema-nervoso #apex-7
Created: 2026-08-22
Last updated: 2026-08-22
---

# Tool: NERVE-SOLVE — Orchestration Layer 1 (Problem Solving Engine)

## Overview
Primo dei 3 "orchestration layer" (sistemi nervosi cognitivi) previsti per il Modello Internet
Artificiale di Digital Empire. Non è una skill lineare da eseguire: è la postura cognitiva che
l'agente abita prima di risolvere qualsiasi problema tecnico, logico, creativo, operativo,
strategico o relazionale. Trasversale a tutta la holding — come [[Fusione_Ruflo_APEX7]] per
l'esecuzione, NERVE-SOLVE lo è per il ragionamento.

## Dettagli

**Percorso attivo**: `.claude/skills/nerve-solve/SKILL.md` (mirror `.agents/skills/nerve-solve/`).
**Sorgente architetturale (audit completo v2.2)**: `SKILL & Agenti/Orchestracion Layer - Problem
solving/ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.2.md`.

**Origine**: zip fornito da Max (`Orchestracion Layer - Problem solving.zip`) contenente due parti
molto diverse:
1. Architettura cognitiva validata (v2.0 → audit → v2.1 → v2.2): identità/DNA in prima persona,
   10 principi con gerarchia e falsificabilità, macchina a fasi non lineare P-1→P12, depth router
   D0-D3, disciplina epistemica (fact/inference/assumption/hypothesis/unknown), lens router,
   contratto di consegna progressivo.
2. Un "Constitutional Kernel" Python orfano (firma Ed25519, canonical JSON, 100% coverage,
   gate M0-M7) che implementa SOLO il caricamento/verifica della costituzione — il motore di
   reasoning vero e proprio (Component B — Case Intake Gateway) non è mai stato costruito.

**Decisione presa con Max**: scartata la via del kernel crittografico standalone (disallineata dal
modo in cui gira il resto dell'Impero — skill/agenti `.md` caricati da Claude Code, non
microservizi con firma digitale). Distillata l'architettura v2.2 in una skill Claude Code
operativa, mantenendo intatte identità/principi/fasi/depth-router, scartando gli strati infra non
costruibili in questo contesto (Postgres, signing, microservizi separati — restano solo come nota
di roadmap futura nella fonte).

**Cosa fa concretamente**: prima di rispondere a un problema non banale, l'agente fa triage
(danno/urgenza/reversibilità/autorità) → sceglie profondità D0-D3 proporzionata al rischio → separa
fatto da ipotesi → sceglie solo le lenti d'analisi che possono cambiare la decisione → produce
opzioni reali con costi ombra → attacca la propria opzione preferita con l'obiezione più forte →
valida con una checklist bloccante prima di consegnare → chiude verificando il bisogno reale, non
solo il problema dichiarato.

**Confine esplicito**: NERVE-SOLVE è Layer 1 di 3. Layer 2 (calcolo strategico/matematico/
finanziario/trading) e Layer 3 (dominio da definire) non sono ancora costruiti — qualunque parte di
un problema che li tocchi va dichiarata `OUT_OF_LAYER`, mai improvvisata.

**Registrazione ADR-008**: `company/skills-map.yaml`, id `nerve-solve`, ecosistema
`08-INTELLIGENCE`, reparto `Cognitive-Control`.

## Connessioni
- [[Digital_Empire_6_Phase_Process]]
- [[Reparto_Produzione_Digital_Empire]]
- [[Tool_Outreach_Message_Team]]
