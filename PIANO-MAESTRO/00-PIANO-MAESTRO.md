# 🏛️ EMPIRE OS — Piano Maestro di Digital Empire Group

> **Documento fondativo.** Digital Empire diventa una holding di ecosistemi di agenti AI —
> il successore multi-business di AION GROUP (Content Factory Exponium), molto più grande:
> non un solo scopo (il lancio Exponium) ma **10 ecosistemi interconnessi** che gestiscono
> un'intera azienda reale: Agency, Info Business, Content Factory, Marketing, Multi-Business,
> Platform, Forge, Intelligence, Operations, Memory.
>
> Metodo di produzione di questo piano: **Dynamic Workflow** (skeleton → swarm fan-out →
> integrazione → review) + **Swarm di agenti paralleli** (un agente specializzato per dossier).
> Versione: 1.0 · Creato: 2026-06-10 · Fonti: studio repo Content Factory Exponium
> (PLAN-05-ENTERPRISE, GRUPPO.md, ECOSISTEMA.MD), wiki Digital Empire, presentazione-empire,
> agency-empire-landing, skill Memory Empire.
>
> ⚠️ **Questo piano è la micro-base.** L'azienda finale sarà molto più grande: il piano è
> progettato per crescere — la FORGE può creare nuovi ecosistemi senza toccare l'architettura.

---

## 0. SPEC (SPARC: S)

- **COSA:** costruire **EMPIRE OS** — il sistema operativo aziendale di Digital Empire:
  una holding di 10 ecosistemi indipendenti ma connessi, su un Corporate Backbone condiviso,
  governata da una C-Suite di agenti, dove ogni reparto/workflow/funzione è gestita da
  team di agenti AI coordinati, con auto-miglioramento continuo.
- **PERCHÉ:** Digital Empire opera già su molti fronti (agency, outreach, info products,
  KDP, siti, SaaS) ma in modo frammentato: decine di workflow e 100+ skill sparsi in cartelle,
  senza gerarchia, senza coordinazione, senza memoria condivisa. AION GROUP ha dimostrato che
  il modello holding funziona — ma è mono-scopo. DE serve la versione multi-scopo.
- **DONE WHEN (criteri globali):**
  1. `company/` navigabile con 10 ecosistemi, ognuno con org interna L2→L5 documentata.
  1-bis. Ecosistema MEMORY operativo PRIMA di tutti gli altri: ogni task interroga la
     memoria prima di agire e scrive checkpoint dopo (memory-first gate).
  2. Corporate Backbone operativo (Bus, Brain, Governance, Identity-HR, Observability, Coordination).
  3. Tutti i workflow esistenti migrati e assegnati al reparto giusto (zero orfani).
  4. Agenti reali running via Ruflo (swarm + hive-mind) per almeno 3 ecosistemi.
  5. `verify.sh` Empire (gate qualità) verde; loop di auto-miglioramento attivo.
  6. Ogni ecosistema produce output reale misurabile (lead, contenuti, video, vendite).
- **OUT OF SCOPE (ora):** spese API/crediti senza ok esplicito; pubblicazione automatica
  senza review umana nelle prime fasi; assunzione che questo piano sia definitivo (è la base).

---

## 1. Identità di Digital Empire (il Mandato)

Digital Empire è una **multi-business company AI-native**:

| Pilastro | Cosa vende / fa | Stato |
|---|---|---|
| **Agency** | 3 implementazioni AI: Outreach Factory €4.000, Content Factory €3.500, Second Brain €2.500, Engine Room €8.000. Codice del cliente, €0 canoni, setup 7gg, 90gg supporto | ATTIVO (outreach + landing + presentazione live) |
| **Info Business** | Corsi (Manuale Claude Code, Skill Beast), ebook, community | ATTIVO (lanci episodici) |
| **Multi-Business** | KDP/libri, YouTube Automation, E-commerce, SaaS/App | PARZIALE (KDP + workflow libri esistono; YT/Ecomm da costruire) |
| **Posizionamento** | "L'agenzia progettata per essere licenziata" — autonomia del cliente, non dipendenza | Definito |

**Mandato Empire (equivalente del MANDATO-EXPONIUM):** brand voice diretta e provocatoria
ma trasparente ("prove non promesse"), framework APSOC come spina dorsale di ogni copy,
pricing one-time no-canoni, proprietà del codice al cliente, qualità prima della velocità,
mai contenuti generici: tutto serve uno dei 10 ecosistemi.

---

## 2. Gerarchia EMPIRE OS (modello AION GROUP esteso)

```
👑  LX — DIPARTIMENTO EMPIRE (autorità suprema)
      Mandato Empire (posizionamento, brand voice, pricing policy, qualità)
      + Sentinelle-Empire (vigilano su OGNI livello, bloccano deliverable non conformi)
       │
L0  BOARD / C-SUITE
      CEO=Empire-Conductor · COO · CTO · CMO · CRO(revenue) · CFO · Chief-Forge
      Decisioni cross-ecosistema via hive-mind consensus (raft)
       │
L1  10 ECOSISTEMI (Business Unit indipendenti ma connesse)
   ├─ 01 AGENCY            acquisizione + delivery clienti (il pilastro revenue)
   ├─ 02 INFO-BUSINESS     lanci, prodotti informativi, vendite
   ├─ 03 CONTENT-FACTORY   produzione contenuti multi-formato multi-brand (trasversale)
   ├─ 04 MARKETING         copywriting (priorità massima), ads, email, analytics (trasversale)
   ├─ 05 MULTI-BUSINESS    YouTube Automation · E-commerce · Publishing/KDP
   ├─ 06 PLATFORM          engineering, siti, tooling, security, infra
   ├─ 07 FORGE             crea team/agenti/skill/workflow/ecosistemi (HR + R&D organizzativo)
   ├─ 08 INTELLIGENCE      ricerca, trend, second brain, Empire Studio, learning
   ├─ 09 OPERATIONS        runtime, mass-production swarm, cost guard, storage, scheduling
   └─ 10 MEMORY            memoria operativa della holding: checkpoint, decisioni (ADR),
                           piani, stato — INTERROGATA PRIMA e SCRITTA DOPO ogni task
                           (urgenza massima: si costruisce per prima)
       │
L2  REPARTI (dentro ogni ecosistema — es. AGENCY: Ricerca, Acquisizione, Preventivi,
       Operatività/Delivery, Copywriting, Marketing-interno)
L3  WORKFLOW (un team per flusso end-to-end — es. WF-OUTREACH-EMAIL, WF-YT-VIDEO)
L4  FUNZIONI (un team per singola funzionalità — es. T-thumbnail, T-voiceover)
L5  AGENTI REALI (coordinator + worker, running via Ruflo agent_spawn / Agent tool)
⊕   GUILDS (trasversali): Prompt Guild · Copy/APSOC Guild · Quality Guild · Cost Guild · Design Guild
⊕   SENTINELS (always-on): Cost · Quality · Drift · Security · Brand-Voice
```

**Regola strutturale fondamentale (ereditata da CF):** UN TEAM DI AGENTI PER OGNI SINGOLA
FUNZIONALITÀ. Ogni team: coordinator + workers, schema input/output rigoroso, acceptance
criteria misurabili, escalation protocol, shared_state.

---

## 3. I 10 Ecosistemi — sintesi e dossier

| # | Ecosistema | Missione | Priorità | Dossier |
|---|---|---|---|---|
| 01 | **AGENCY** | Acquisire e servire clienti delle 3 implementazioni AI. Reparti: Ricerca, Acquisizione (outreach), Preventivi, Operatività/Delivery, Copywriting, Marketing-interno | ALTA | `01-ECOSISTEMA-AGENCY.md` |
| 02 | **INFO-BUSINESS** | Lanci e prodotti informativi. Reparti: Lanci, Prodotto, Vendite | ALTA | `02-ECOSISTEMA-INFOBUSINESS.md` |
| 03 | **CONTENT-FACTORY** | Produzione contenuti per TUTTI gli ecosistemi (multi-brand, multi-cliente). Reparti: Strategia, Video, Testuale, Visual&Design, Pubblicazione | ALTA | `03-ECOSISTEMA-CONTENT-FACTORY.md` |
| 04 | **MARKETING** | Motore persuasione trasversale. Reparti: Copywriting (priorità assoluta), Advertising, Email, Analytics | ALTA | `04-ECOSISTEMA-MARKETING.md` |
| 05 | **MULTI-BUSINESS** | Business scalabili paralleli: YouTube Automation, E-commerce, Publishing/KDP | MEDIA-ALTA | `05-ECOSISTEMA-MULTIBUSINESS.md` |
| 06 | **PLATFORM** | Codice, siti (Crea Siti, empire-style), tooling, sicurezza, CI | TRASVERSALE | `06-ECOSISTEMI-CORE.md` |
| 07 | **FORGE** | Fabbrica organizzativa: crea skill (skill-creator, content-forge, System OMEGA), agenti, team, interi ecosistemi | TRASVERSALE | `06-ECOSISTEMI-CORE.md` |
| 08 | **INTELLIGENCE** | Second brain, wiki, Empire Studio (ingestione), Memory Empire (enrichment), ricerca e trend | TRASVERSALE | `06-ECOSISTEMI-CORE.md` |
| 09 | **OPERATIONS** | Runtime: swarm mass-production, budget guard, storage, scheduling | TRASVERSALE | `06-ECOSISTEMI-CORE.md` |
| 10 | **MEMORY** | Memoria operativa della holding: checkpoint, decisioni (ADR), piani, stato, log task. Interrogata PRIMA di ogni task, scritta DOPO ogni task | **MASSIMA (urgente, si costruisce per prima)** | `09-ECOSISTEMA-MEMORY.md` |

Backbone + integrazione Ruflo + registro skill: `07-BACKBONE-RUFLO-SKILLS.md`.
Roadmap a fasi: `08-ROADMAP-FASI.md`.

---

## 4. Corporate Backbone (servizi condivisi)

| Componente | Funzione in DE | Base esistente |
|---|---|---|
| **BUS** | Message bus 2 livelli (intra+inter ecosistema), handoff contract `{from, to, payload, acceptance_criteria}` | pattern CF (gbus.sh) da portare |
| **BRAIN** | Memoria condivisa: wiki second-brain-vault (fonte di verità umana) + AgentDB/HNSW (memoria vettoriale agenti) + ReasoningBank (impara dagli errori) + Memory Empire (enrichment skill) | wiki ATTIVA, ruflo@3.10.13 globale, Memory Empire v3 ATTIVO |
| **GOVERNANCE & QA** | Gate qualità Empire (`verify.sh` versione DE), contradiction-analyzer, brand gate (Mandato Empire), security (aidefence) | skill contradiction-analyzer installata |
| **IDENTITY-HR** | Registro unico di tutti gli agenti (ruolo, costo, performance); la Forge assume/ritira | da costruire |
| **OBSERVABILITY** | Metrics, dashboard, neural_train, autopilot, cost-attribution | da costruire |
| **COORDINATION FABRIC** | Ruflo: swarm topologies (hierarchical default) + consensus (raft/byzantine/gossip/crdt/quorum) | ruflo globale installato; init per-progetto |

---

## 5. Integrazione Ruflo (componente centrale, non secondario)

```
Ruflo = COORDINA (stato, memoria, routing, swarm, consensus)
Claude Code = ESEGUE (codice, file, contenuti, comandi)
```

| Funzione EMPIRE OS | Tool Ruflo |
|---|---|
| Coordinamento ecosistemi | `swarm_init` (topology per ecosistema), `coordination_orchestrate` |
| Decisioni cross (Board) | `hive-mind_init/propose/vote/consensus` (raft) |
| Cervello | `memory_store/search` (AgentDB HNSW), namespace per ecosistema |
| Apprendimento | `neural_train`, `reasoningbank-*`, `autopilot_*` |
| Agenti reali | `agent_spawn`, `managed_agent_*` + Agent tool Claude Code |
| Sicurezza | `aidefence_scan/is_safe/has_pii` |
| Workflow dinamici | `task_orchestrate`, `workflow_create/execute` |
| Routing costi | 3-tier model routing (WASM/Haiku/Sonnet-Opus) + Thompson Sampling |

**Azione concreta:** `ruflo init` nella root EMPIRE OS (cartella `company/` di DE) + daemon
+ memory init. Ogni ecosistema dichiara nel suo `BACKBONE.md` quali namespace di memoria
e quale topologia swarm usa.

---

## 6. I 10 Pattern architetturali non negoziabili (ereditati da CF, estesi)

1. **Team canonico a schema fisso** — coordinator, agents, I/O espliciti, acceptance criteria, failure handling, shared_state.
2. **Handoff contract** — ogni passaggio tra team è un messaggio strutturato con acceptance criteria.
3. **Dry run mode** — ogni workflow ha modalità stima-costo senza effetti reali.
4. **Gate obbligatorio** — niente esce senza QA gate + brand gate (Mandato Empire).
5. **ReasoningBank** — ogni fallimento loggato e distillato in pattern.
6. **Skill come knowledge layer separato** — una skill, molti agenti, molti reparti.
7. **Progressive disclosure** — SKILL.md kernel ≤500 righe, dettaglio in references/.
8. **Invariant cardinali espliciti** — regole non negoziabili scritte nel kernel di ogni skill/team.
9. **Cost guard** — budget guard che blocca prima di sforare; cost-attribution per agente.
10. **Sentinels always-on** — Cost, Quality, Drift, Security, Brand-Voice.

**+ 2 pattern nuovi per DE:**

11. **Multi-tenant by design** — ogni workflow accetta `brand_kit` + `icp` come input: lo stesso
    motore serve DE stessa, i clienti agency, i canali YouTube, i libri KDP.
12. **Wiki-first** — la wiki è la fonte di verità leggibile dall'uomo; AgentDB è l'indice
    semantico per gli agenti. Ogni operazione logga in `wiki/log.md`.

13. **Memory-first (non negoziabile)** — PRIMA di qualsiasi task: interrogare l'ecosistema
    MEMORY (stato, checkpoint, decisioni, piani rilevanti). DOPO ogni task: scrivere
    checkpoint con esito. Nessun task è "fatto" finché non è salvato in MEMORY.
    Dettaglio: `09-ECOSISTEMA-MEMORY.md`.

---

## 7. Metodo: Dynamic Workflows + Swarm

- **Costruzione a iterazioni self-paced** (come BUILD-11→16 di CF): una fase per ciclo,
  gate verify ad ogni step, checkpoint memoria, push GitHub.
- **Swarm per la produzione di massa**: mai un agente solo quando più agenti coordinati
  possono lavorare in parallelo (fan-out su reparti disgiunti, pipeline su flussi sequenziali,
  supervisor per refactor complessi).
- **Workflow adattivi**: ogni workflow legge memoria/pattern prima di agire
  (`memory_search`), si auto-corregge dopo (`hooks post-task`), e la FORGE lo fa evolvere
  quando i KPI calano.

---

## 8. Roadmap (sintesi — dettaglio in 08-ROADMAP-FASI.md)

| Fase | Cosa | Gate |
|---|---|---|
| **F1** | Scaffolding EMPIRE OS: parte da MEMORY (task 1.0, urgenza massima — ME-0→ME-5), poi `company/` con LX/L0/L1, 10 ecosistemi, Backbone, Guilds, Sentinels + Mandato Empire | memory-first attivo + struttura navigabile |
| **F2** | Backbone operativo: ruflo init, Bus, Brain (AgentDB+wiki bridge), verify.sh Empire | verify verde |
| **F3** | Migrazione asset: ogni workflow/skill esistente assegnato al suo reparto (zero orfani) | inventario 100% mappato |
| **F4** | AGENCY ecosystem live: outreach + preventivi + delivery come team L3 coordinati | primo flusso end-to-end |
| **F5** | MARKETING + CONTENT-FACTORY live (copy engine + produzione multi-formato) | contenuti reali prodotti |
| **F6** | INFO-BUSINESS: lancio orchestrato dal sistema | primo lancio assistito |
| **F7** | YOUTUBE AUTOMATION: ingestione Empire Studio dei 2 canali riferimento + build pipeline | primo video pubblicato |
| **F8** | Agenti reali + Sentinels + auto-miglioramento (reasoningbank+neural+autopilot) | loop attivo |
| **F9+** | E-commerce, espansione FORGE (nuovi ecosistemi), dashboard, scaling | continuo |

---

## 9. Rischi & mitigazioni

| Rischio | Mitigazione |
|---|---|
| Complessità eccessiva / sistema cattedrale mai usato | costruzione a fasi con output REALE ad ogni fase (F4 = lead veri, F5 = contenuti veri) |
| Drift architetturale tra 10 ecosistemi | Mandato Empire + Drift-Sentinel + hive-mind raft + contradiction gate |
| Costi API/agenti reali | 3-tier routing, Cost-Sentinel, dry-run default, spawn on-demand |
| Asset esistenti rotti dalla migrazione | migrazione = mappatura + wrapper, mai riscrittura; i workflow attivi (outreach) non si toccano finché il sostituto non è validato |
| Daemon Ruflo non persistente su Windows | bootstrap auto-riparante + fallback pattern bash (ibrido ADR-005 CF) |
| Wiki/AgentDB divergono | wiki-syncer di Memory Empire + log obbligatorio |

---

## 10. Connessioni

- [[projects/Exponium/Exponium_Content_Factory_Studio]] — modello architettonico di riferimento
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo
- [[Concept_Pivot_Implementazioni_AI]] — offerta agency attuale
- [[Tool_Copy_Workflow_Orchestration]] — motore copy APSOC
- [[Empire_Studio]] + [[Memory_Empire]] — ecosistema INTELLIGENCE
- [[Agency_Empire_Landing]] — vetrina agency
