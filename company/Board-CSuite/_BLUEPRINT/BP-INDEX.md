# 📐 BLUEPRINT BOARD C-SUITE V2 — prodotti da ARCHITETTURA per la FORGE

> **Bootstrap del Genesi Core (2026-06-16).** Primo uso reale di WF-ARCH-DESIGN dell'organo
> ARCHITETTURA: progettare la STRUTTURA delle 7 figure Board prima che la FORGE costruisca il contenuto.
> Confine: questi file sono STRUTTURA (blueprint), NON la figura finale. La FORGE (STEP 4-heavy)
> costruisce il contenuto dentro questi blueprint, poi MAXIMILIAN giudica, Mandato verifica, si registra.

## Perché esistono
La direttiva V2 (§1) marca INACCETTABILE la v1 (CEO = 1 file .md). Standard V2: ogni figura C-level =
**cartella-workflow CF-grade** con ≥10 agenti, principi, skill proprie, workflow ≥2, scripts, kpi, state.
La §8 impone: progettata PRIMA con le skill di architettura → qui ARCHITETTURA fa esattamente questo.

## Record WF-ARCH-DESIGN
- `request_id`: ARCH-BOARD-20260616
- `tipo`: 7× "figura C-level" (forma = workflow CF-grade, peso PESANTE)
- `committente`: Board / Max (direttiva V2 §1)
- `forma_scelta`: ogni figura = cartella-workflow (NON file, NON semplice reparto) — motivata §1
- `validazione strutturale`: ogni BP include la checklist struct-gate per la verifica post-build
- `handoff_to`: FORGE (WF-ECOSYSTEM-NEW / WF-TEAM-NEW per gli agenti di figura)

## Le 7 figure (blueprint)
| Figura | Governa | Blueprint | Agenti |
|---|---|---|---|
| **CEO** Empire-Conductor | orchestrazione, consenso, Mandato gate | [BP-CEO](BP-CEO.md) | 10 |
| **COO** | operations, backbone health, sync, runtime | [BP-COO](BP-COO.md) | 10 |
| **CTO** | architettura, Platform, Forge, sicurezza | [BP-CTO](BP-CTO.md) | 10 |
| **CMO** | marketing, content, brand voice, APSOC | [BP-CMO](BP-CMO.md) | 10 |
| **CRO** | revenue, Agency pipeline, InfoBusiness lanci | [BP-CRO](BP-CRO.md) | 10 |
| **CFO** | budget, cost guard, 3-tier routing | [BP-CFO](BP-CFO.md) | 10 |
| **Chief-Forge** | skill, agenti, team, nuovi ecosistemi | [BP-Chief-Forge](BP-Chief-Forge.md) | 10 |

= **70 agenti** progettati a livello di roster + struttura. Build contenuto = STEP 4-heavy (FORGE).

## Struttura che la FORGE costruirà per OGNI figura (template V2 §1)
```
Board-CSuite/<FIGURA>/
├── README.md            # architettura della figura (da ARCHITETTURA.md del BP)
├── ARCHITETTURA.md      # questo blueprint, espanso
├── agenti/              # ≥10 schede (roster nel BP)
├── principi/  regole/   # come ragiona, cosa NON può fare
├── skills/              # skill proprie (elencate nel BP)
├── scripts/             # .py/.ps1: raccolta dati, report, dispatch
├── workflow/            # ≥2 flussi CF-grade (elencati nel BP)
└── kpi/  state/
```

## Connessioni
- [[14-DOSSIER-ARCHITETTURA]] — l'organo che ha prodotto questi blueprint (WF-ARCH-DESIGN)
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §1 (Board V2) · §8 (obbligo skill architettura)
- [[12-DOSSIER-MAXIMILIAN]] — giudica le figure dopo il build (review 5-bis)
- Genesi-Core/FORGE — costruirà il contenuto da questi blueprint
