# 🏛️ ARCHITETTURA — ESTATE-2026 REVENUE WORKSHOP
> Prodotto con il metodo `master-build-architecture` (10 fasi, invarianti non negoziabili). Fase successiva al planning P1→P7. Memory-first dal passo zero: CP-001/002, DEC-EST-001..004 già registrati.

## 1. Invarianti architetturali (non negoziabili)
1. **Memory ecosystem dal primo passo** — ogni step scrive in `00-MEMORY/` (checkpoint/decisioni/piani/brainstorm/errori/metriche/pattern).
2. **Nessun riassunto, solo espansione operativa** — ogni documento del workshop è eseguibile da solo.
3. **Wrap, non rewrite (ADR-EST-002)** — carousel-factory, PreventivoForge, outreach A1/A2, skill content-forge: si orchestrano, non si ricostruiscono.
4. **Vendibile > perfetto (ADR-EST-005)** — DoD congelate; superarle richiede decisione registrata.
5. **Revenue-first (ADR-EST-001)** — i conflitti di risorse si risolvono per €/h (tabella P4).
6. **Tracciabilità P12** — ogni artefatto cita gli ID memoria che lo hanno prodotto (`DEC-EST-xxx`, `CP-xxx`).
7. **Zero secrets nei file** — chiavi solo in `.env` locale gitignorato.
8. **Orchestrazione degradata graziosamente** — se ruflo non è disponibile, `workflows.yaml` + protocollo memoria bastano (file-based mode).

## 2. Modello a livelli

```
┌──────────────────────────────────────────────────────────────────────┐
│ L5  SKILLS & TOOLS   content-forge2.0 · master-build-architecture    │
│                      carousel-factory · case-study-forge · site-*    │
│                      beast-preventivi · cro-copy-architect · A1/A2   │
├──────────────────────────────────────────────────────────────────────┤
│ L4  WORKFLOWS        WF-MASTER · WF-S1..S6 · WF-YT-* · WF-MEM-*      │
│                      (03-WORKFLOWS/workflows.yaml = source of truth) │
├──────────────────────────────────────────────────────────────────────┤
│ L3  AGENTS           chief-forge · forge-builder · memory-architect  │
│                      yt-* (4 nuovi) · dipartimento/team esistenti    │
│                      formato canonico 7-file                         │
├──────────────────────────────────────────────────────────────────────┤
│ L2  DEPARTMENTS      CHIEF-FORGE (build) · REVENUE · CONTENT · YT    │
│                      MEMORY MGMT · VERIFICATION & CONTROL · STRATEGY │
├──────────────────────────────────────────────────────────────────────┤
│ L1  NERVOUS SYSTEM   ruflo (swarm hierarchy, hooks, AgentDB)         │
│                      fallback: file-based orchestration              │
├──────────────────────────────────────────────────────────────────────┤
│ L0  MEMORY           00-MEMORY/ (operativa) → second-brain (long)    │
│                      MEMORY-INDEX.md vivo · ReasoningBank · P12      │
└──────────────────────────────────────────────────────────────────────┘
```

## 3. L2 — Reparti Digital Empire (responsabilità e proprietà)

| Reparto | Lead | Missione questa settimana | Output |
|---|---|---|---|
| **CHIEF-FORGE** (costruzione) | `chief-forge` | Costruisce TUTTO: funnel, kit, pipeline, wrapper skill | artefatti live + DoD rispettate |
| **REVENUE** | `pricing-cell` (beast-preventivi) | prezzi, offerta S1, script chiusura | DEC-001 attiva, script WA |
| **CONTENT** (Content Forge Dept) | `content-forge-invoker` | caroselli S3/S4, email, landing copy, case study | contenuti batch |
| **YOUTUBE** | `department-lead` | WF-YT v1: scouting→render→publish→analyze | 1 video + ReasoningBank YT |
| **MEMORY MGMT** | `memory-architect` | integrità memoria, checkpoint EOD, INDEX | memoria sempre coerente |
| **VERIFICATION & CONTROL** | `silent-observer` | gate P5, zero-stub, anti-vanity, compliance | gate 🟢🟡🔴 in dashboard |
| **STRATEGY** | `strategy-director` | planning P1→P7 (fatto), RETRO | retro + pattern |

## 4. L3 — Agenti: stato e formato
- **Formato canonico 7-file** (spec/system-prompt/playbook/tools/memory/evals/failure-modes). Pack completi: `04-AGENTS/chief-forge/`, `04-AGENTS/memory-architect/`.
- **Nuovi agenti S5** (spec completa in `04-AGENTS/YT-AGENT-PACK.md`): `yt-fliki-renderer`, `yt-seo-publisher`, `yt-performance-analyzer`, `yt-niche-scout` — si espandono in 7-file all'attivazione (24/07).
- **Esistenti (registry, si wrappano)**: yt-channel-ingester, video-single-ingester, yt-screening, visual-verifier, compliance-auditor, silent-observer, cro-copy-architect, carousel ops, case-study-forge.

## 5. L4 — Workflow (mappa completa in `03-WORKFLOWS/workflows.yaml`)

| WF | Scopo | Stream | Finestra |
|---|---|---|---|
| WF-MASTER | orchestratore di settimana: gates, coda swarm, EOD loop | tutti | continuo |
| WF-S1-CONCESSIONARI | lista→script→WA msg1-2-3→obiezioni→chiusura→clone app→incasso | S1 | 21→26/07 |
| WF-S2-MANUALE | DEC-001→landing→checkout→3 email→push→vendite | S2 | 21→26/07 |
| WF-S3-PAGINE | audit→bio→batch caroselli→pubblicazione→traffico→S2 | S3 | 22→26/07 |
| WF-S4-MENTALITA | gate 100% auto: batch→QA→scheduler→report | S4 | 23→25/07 |
| WF-S5-YOUTUBE | scout→script→render(Fliki/ladder)→thumb→publish→analyze→improve | S5 | 24→25/07 |
| WF-S6-REBRAND | DEC-002→dominio→case study→landing Preventa→demo→outreach A1/A2 | S6 | 22→26/07 |
| WF-MEM-EOD | chiusura giornata: metriche, checkpoint, dashboard | memoria | h19:00 |
| WF-MEM-RETRO | RETRO domenica: numeri veri→pattern ReasoningBank | memoria | 26/07 |

## 6. L0 — Topologia memoria (due livelli)
- **Operativa**: `00-MEMORY/` — atomi ID-numerati, MEMORY-INDEX.md per ricerca, ReasoningBank per pattern. CLI: `memory_manager.py` (init/checkpoint/decision/plan/brainstorm/error/metric/pattern/retro/search/status).
- **Long-term**: second-brain vault esistente (Obsidian) — sync manuale in RETRO: i pattern e i CP settimanali vengono copiati come note permanenti.
- **P12 trace**: frontmatter `id`+`trace` in ogni atomo; gli artefatti citano gli ID.

## 7. L1 — Sistema nervoso (ruflo)
- Topologia: **hierarchical queen-led** → `chief-forge` = orchestratore, reparti = worker swarm. Dettagli e config: `06-NERVOUS-SYSTEM/RUFLO-INTEGRATION.md` + `swarm.estate.yaml`.
- Hooks: pre-task → carica contesto memoria; post-task → `checkpoint`; on-failure → `error`; EOD → `WF-MEM-EOD`.
- AgentDB/memoria vettoriale ruflo = cache semantica; **source of truth resta `00-MEMORY/`** (file, diffabile, umano-leggibile).

## 8. ADR emesse
| ADR | Decisione |
|---|---|
| ADR-EST-001 | Revenue-first: conflitti risolti per €/h |
| ADR-EST-002 | Wrap-don't-rewrite per tutti i motori attivi |
| ADR-EST-003 | Memory-first: nessun task è "chiuso" senza checkpoint |
| ADR-EST-004 | Un solo swarm pesante alla volta (coda priorità S1>S2>S6>S5) |
| ADR-EST-005 | DoD "vendibile" congelata per ogni deliverable |
| ADR-EST-006 | Decisioni per default + veto window (anti-bottiglia Max) |

## 9. Mappa directory (build completata)
```
DIGITAL-EMPIRE/
├── 00-MEMORY/        L0 — ecosistema memoria + memory_manager.py + INDEX
├── 01-PLANNING/      PLANNING-P1..P7 (master plan = P7, plan of record)
├── 02-ARCHITECTURE/  questo documento
├── 03-WORKFLOWS/     workflows.yaml + WF-MASTER + WF-S1..S6
├── 04-AGENTS/        registry + chief-forge (7 file) + memory-architect (7) + YT pack
├── 05-SKILLS/        content-forge2.0 · master-build-architecture · ruflo (clonati 21/07)
├── 06-NERVOUS-SYSTEM/ ruflo integration + swarm.estate.yaml
└── 07-CONTROL/       dashboard + protocollo RETRO
```

## 10. Runbook di attivazione (da qui all'esecuzione)
1. Max apre P7 §1 → conferma/veta DEC-001 entro h20:00 (OGGI).
2. Claude esegue batch copy 21/07 sera (WF-S1 §script + WF-S2 §copy).
3. Gael segue P7 §2 corsia 🟣 — ogni task chiuso → checkpoint.
4. Ogni h19:00 → WF-MEM-EOD. Gate al loro orario → 🟢/🔴 in dashboard.
5. 26/07 → WF-MEM-RETRO: numeri veri, pattern → ReasoningBank, sync second-brain.

---
⛓️ Trace P12: `ARCH-ESTATE-2026#estate-2026` · input: PLANNING-P1..P7 · metodo: 05-SKILLS/master-build-architecture · memory: CP-001/002, DEC-EST-001..004
