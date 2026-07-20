---
Type: TOOL
Status: Active
Tags: #skill #ricerca #cro #intelligence #retrofit #mir-5
Created: 2026-07-20
Last updated: 2026-07-20
---

# Skill CRO Ricerca — Client Research Engine

## Overview
Il **sistema di intelligence prima di ogni copy e di ogni video**: ricerca profonda nelle conversazioni
REALI del target (commenti YouTube, Reddit, X, recensioni, forum). Estrae le ESATTE PAROLE, i VERI
PROBLEMI, le REALI OBIEZIONI e il TOV autentico — e li compila in un **Report Ricerca a 10 sezioni**
con scoring (pain I×F×A · obiezioni F×I) che è il prerequisito non negoziabile del CRO Copy Architect.
Regola d'oro: *"Se non trovi le parole esatte del target, non hai cercato abbastanza."* — 90% delle
agenzie salta la ricerca e produce copy generico; questa skill è la fase che separa il 10%.

## Dove sta / come si usa
- **Master:** `SKILL & Agenti/SKILL/Skill CRO - Ricerca/SKILL.md` (1.625 righe, vincolo ADR-003: intoccato)
  + 7 knowledge reali (890 righe: FILOSOFIA, masterclass YouTube/Reddit/X, pain 3 livelli, TOV 6 dimensioni,
  obiezioni implicite, cross-platform pattern).
- **Wrap canonico (retrofit MIR-5 sprint 2, CP-20260720-015):** `spec.md` (mappa righe + debiti D1-D3) ·
  `tools.md` (nessun tool: `tools: []` by design — guida/raccogli/analizza) · `playbook.md` (4 scenari:
  avvio cliente, ciclo analisi dati grezzi, compilazione report, fuori-perimetro/parziale 2.5h) ·
  `evals.md` (E1-E7) · `failure-modes.md` (F1-F7) · `memory/INDEX.md`.
- **⚠️ Manifest fantasma:** non cercare i 5 template del §KNOWLEDGE_FILES come file — non esistono;
  i contenuti sono INLINE nel master (regola del wrap: **il corpo vince sul manifest**).

## Metodo in sintesi (5 fasi)
R1 Audience (min 20 frasi esatte, commenti > contenuti) → R2 Competitor (3 diretti + 2 indiretti, scheda
completa) → R3 TOV (in parallelo a R1; tabella USA/EVITA 10+ coppie) → R4 Pain points (4 categorie,
scoring Intensità×Frequenza×Actionability, top 5-7 + leve emotive) → R5 Obiezioni (5 categorie, scoring
F×I, top 5-7, RACCOGLI non gestire) → Report 10 sezioni. Tempi: full 5-10h · minima 2.5h (dichiarando
cosa manca e impatto). Gate qualità: 13 standard completi / 7 minimum (tools.md).

## Relazioni
- **A valle:** CRO Copy Architect (consuma il Report; knowledge dir non censita → candidata MIR-5 sprint 3).
- **A monte:** Briefing Master Pro (citata dal master, NON presente nel repo al 2026-07-20 — STEP 0 gestisce).
- **W7 YouTube:** frasi esatte/obiezioni/TOV alimentano [[tools/Tool_Youtube_Script_Factory|Script Factory]]
  e la strategia [[tools/Tool_Youtube_Lead_Machine_Skill|/youtube-lead-machine]] (playbook S4).
- **Confine:** NON scrive copy, NON gestisce obiezioni, NON inventa dati (evals E5/E2).

## Registro
- Retrofit MIR-5 sprint 2 (2026-07-20): wrap satelliti + debiti manifest/gate dichiarati · GATE retro PASS
  7/7 (verbale in `FORGE-AGENT-SKILL/memory/checkpoints/`) · skills-map v1.6 (entry esistente aggiornata,
  stats invariate 63) · REGISTRO-IMPRESA §3.
