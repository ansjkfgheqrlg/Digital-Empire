---
Type: PROJECT
Status: Active
Tags: #empire-os #piano-maestro #holding #ecosistemi #agenti #memory-first
Created: 2026-06-10
Last updated: 2026-08-24
---

# Piano Maestro EMPIRE OS — Digital Empire Group

## Overview
Il piano fondativo che trasforma Digital Empire in una **holding di 10 ecosistemi di agenti AI**
(EMPIRE OS), successore multi-business di [[projects/Exponium/Exponium_Content_Factory_Studio|AION GROUP]].
10 dossier esecutivi in `Digital Empire/PIANO-MAESTRO/`, prodotti con metodo Dynamic Workflow +
swarm di 7 agenti paralleli (2026-06-10). Versione 1.0 — dichiarata esplicitamente "micro-base":
progettata per crescere oltre questo orizzonte via FORGE.

## I 10 Ecosistemi

| # | Ecosistema | Missione | Dossier |
|---|---|---|---|
| 01 | AGENCY | acquisizione + delivery 3 implementazioni AI (€4k/€3.5k/€2.5k, Engine Room €8k) | 01 (379 r., 6 reparti, ~37 agenti, 16 handoff) |
| 02 | INFO-BUSINESS | lanci, corsi, ebook, community | 02 (391 r., 4 reparti, 26 agenti) |
| 03 | CONTENT-FACTORY | contenuti multi-formato **multi-tenant** (brand_kit+icp come input — supera CF Exponium) | 03 (434 r., 5 reparti, engine layer multi-motore) |
| 04 | MARKETING | copywriting priorità assoluta (Copy Workflow A1-A8+S1-S3 inglobato), ads, email, analytics | 04 (387 r., gate score ≥80/100) |
| 05 | MULTI-BUSINESS | YouTube Automation · Publishing/KDP · E-comm | 05 (446 r., pipeline YT 16 step, 4 QA gate/video) |
| 06 | PLATFORM | engineering, Crea Siti, security, deploy | 06 (4 core in un dossier, 41 agenti) |
| 07 | FORGE | crea skill/agenti/team/ecosistemi (content-forge + skill-creator come motori) | 06 |
| 08 | INTELLIGENCE | wiki, Empire Studio, Memory Empire (inglobati così come sono), ricerca | 06 |
| 09 | OPERATIONS | runtime swarm, budget guard, scheduling, dashboard | 06 |
| 10 | **MEMORY** | memoria operativa: checkpoint, ADR, piani, stato — **interrogata PRIMA, scritta DOPO ogni task** (pattern #13, urgenza massima) | 09 (209 r.) — **GIÀ COSTRUITA ME-0/ME-1** |

+ `07-BACKBONE-RUFLO-SKILLS.md`: Backbone 6 componenti (Bus, Brain 3 strati, Governance/verify
5 categorie, Identity-HR, Observability, Coordination con mappa topologie), rollout Ruflo,
censimento **121 skill** mappate, 12 skill `empire-*` nuove (prima: `empire-context`),
5 Sentinels + 5 Guilds, struttura `company/`.
+ `08-ROADMAP-FASI.md`: 12 fasi con gate (F1 parte da MEMORY → F12 dashboard).

## Architettura (ereditata da AION GROUP, estesa)
- Gerarchia **LX→L5**: Mandato Empire → Board/C-Suite → 10 Ecosistemi → Reparti → Workflow → Funzioni → Agenti. + Guilds e Sentinels.
- **13 pattern non negoziabili** (10 da CF + multi-tenant #11, wiki-first #12, **memory-first #13**).
- Ruflo = coordina (swarm, AgentDB, hive-mind raft, 3-tier routing); Claude Code = esegue.

## Ecosistema MEMORY — già operativo
`Digital Empire/company/Memory/`: INDEX.md, STATO-EMPIRE.md, checkpoints/ (CP-20260610-001),
decisions/ (ADR-001 EMPIRE OS, ADR-002 memory-first, ADR-003 wrap-non-riscrittura), plans/,
sessions/, tasks/<10 eco>/, state/, audit/, templates/. REGOLA ZERO MEMORY-FIRST aggiunta al
CLAUDE.md di Digital Empire.

## Decisioni chiave (ADR in company/Memory/decisions/)
1. **ADR-001** — EMPIRE OS: holding 10 ecosistemi su modello AION GROUP.
2. **ADR-002** — memory-first: nessun task chiuso senza CP; nessun task parte senza interrogare Memory.
3. **ADR-003** — migrazione = wrap, mai riscrittura; sistemi attivi (outreach) intoccabili.

## Evoluzione V2 (2026-06-11 → 06-30) — pivot di scala (ADR-007)
Dopo F1 (scaffolding `company/` completo, 92 check) e F2 (Backbone/ruflo operativo), Max ha
dato una **direttiva di scala** ([[Concept_Decisioni_Architetturali_ADR|ADR-007]]): i
reparti diventano team CF-grade da 6-10 agenti con workflow propri, i mega-reparti "aziende
dentro l'azienda", e nascono due nuove strutture di governo:
- **Genesi Core** (`company/Genesi-Core/`) — organo **ARCHITETTURA** (progetta la forma
  giusta di ogni artefatto, dossier 14) + organo **FORGE** (costruisce il contenuto attorno
  al blueprint, gemello di ARCHITETTURA), confine ferreo struttura/contenuto.
- **MAXIMILIAN** (`company/MAXIMILIAN/`, dossier 12) — organo LX che incarna il giudizio di
  Max: 8 agenti MX-*, gate **5-bis** ("Max approverebbe?") innestato nel ciclo a 9 passi
  ([[Concept_Decisioni_Architetturali_ADR|ADR-006]]) dopo ogni BUILD, skill
  `maximilian-standard-gate` (8 test binari deterministici).
- **Board C-Suite V2 completo**: le 7 figure (CEO, Chief-Forge, CTO, COO, CMO, CRO, CFO)
  ricostruite come cartelle-workflow CF-grade (10 agenti + ≥2 workflow ciascuna, ~70 agenti
  totali), progettate da ARCHITETTURA e costruite da FORGE — prima prova che il Genesi Core
  funziona davvero, ogni figura passata dal gate 5-bis.
- **Ecosistemi V2 costruiti reparto-per-reparto (STEP 5)**: **04-MARKETING completo 6/6**
  (114 file/44 agenti/22 workflow, incl. il wrap del Copy Workflow Orchestration Layer
  attivo — [[Tool_Copy_Workflow_Orchestration]]), **02-INFO-BUSINESS completo 5/5**,
  **03-CONTENT-FACTORY completo 9/9** (CF-R0 Director → CF-R8 Apprendimento, mega-reparto a
  5 livelli gerarchici), **01-AGENCY 6/10** (A1-A6: Ricerca/Acquisizione/Preventivi/Delivery/
  Copy interno/Marketing interno — A2 wrappa il runtime outreach LIVE per ADR-003, A7-A10
  non confermati completi in questo backfill).

Ogni build ha rispettato [[Concept_Decisioni_Architetturali_ADR|ADR-003]] (wrap, non
riscrittura — verificato con `git diff` sui file v1/motori attivi ad ogni checkpoint) e ha
attraversato struct-gate + review 5-bis MAXIMILIAN prima del commit.

## Ecosistema 11 — APEX-7-CORE (motore di orchestrazione condiviso)
Vedi [[Tool_APEX7_Core_Motore_Condiviso]]: motore comune di quality-gate/orchestrazione
nato per curare la frammentazione di 6 implementazioni APEX-7 divergenti trovate nel repo
([[Concept_Decisioni_Architetturali_ADR|ADR-010]], [[Concept_Decisioni_Architetturali_ADR|ADR-011]]).
Pilota riuscito su [[Concept_YouTube_Automation_Factory]]; Stream-S7-Bot valutato e non
migrato per non fare un downgrade funzionale su un sistema con soldi reali.

## Pending noti
- Token FB scaduto (scraper outreach) — fase B0 dossier 01.
- Catalogo InfoBusiness: prezzo Manuale Claude Code "NON LO SO" + doppio ruolo contraddittorio — bloccante B1 dossier 02.
- Ingestione Empire Studio canali YouTube riferimento (@Legamidiamore, @dosementale) — task 7.0/F-MB1, sessione dedicata (vincolo: il video VA VISTO).

## Connessioni
- [[projects/Exponium/Exponium_Content_Factory_Studio]] — modello architettonico
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo
- [[Concept_Pivot_Implementazioni_AI]] — offerta agency
- [[Tool_Copy_Workflow_Orchestration]] — motore copy (wrappato in 04-MARKETING/L2.1)
- [[Empire_Studio]] · [[Memory_Empire]] — ecosistema INTELLIGENCE
- [[Agency_Empire_Landing]] — vetrina
- [[Concept_Decisioni_Architetturali_ADR]] — tutte le decisioni ADR-001..012 di governo del piano
- [[Tool_APEX7_Core_Motore_Condiviso]] — ecosistema 11, motore di orchestrazione condiviso

## 📍 Status
- Created: 2026-06-10 · Aggiornato: 2026-08-24 (backfill storico 06-08/2026, permesso
  esplicito Max) · Fase: V2 in costruzione reparto-per-reparto (STEP 5), Genesi Core e Board
  C-Suite V2 completi, 3 ecosistemi V2 chiusi (04-MARKETING, 02-INFO-BUSINESS,
  03-CONTENT-FACTORY), 01-AGENCY 6/10 — stato dei restanti ecosistemi (05, 06-split, 07, 08,
  09) non verificato in questo backfill, richiede lettura diretta di STATO-EMPIRE.md corrente
