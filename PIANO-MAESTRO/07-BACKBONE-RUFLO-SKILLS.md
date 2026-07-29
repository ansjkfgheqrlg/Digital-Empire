# 🔧 07 — CORPORATE BACKBONE · INTEGRAZIONE RUFLO · REGISTRO SKILL

> Dossier tecnico del **Corporate Backbone di EMPIRE OS** (Digital Empire Group).
> Modello di riferimento: AION GROUP / Content Factory Exponium (`orchestration/company/Backbone/`,
> `PLAN-05-ENTERPRISE.md` §4-5-9). Differenza chiave: CF è **mono-scopo** (lancio Exponium),
> EMPIRE OS è **multi-business e multi-tenant** (10 ecosistemi, N brand/clienti).
> Coerente al 100% con `00-PIANO-MAESTRO.md` (§2 gerarchia, §4 backbone, §5 Ruflo, §6 pattern).
> Versione: 1.0 · Creato: 2026-06-10 · Stato: progetto esecutivo (build in F2 della roadmap)

> **⚡ Aggiornamento 2026-07-28 ([ADR-010](../company/Memory/decisions/ADR-010-fusione-ruflo-apex7.md)):**
> questo Backbone non si costruisce da zero — la sua Coordination Fabric è il motore già scritto
> e testato in `company/Ecosistemi/11-APEX-7-CORE/` (SQLite memory multi-tenant, `BaseAgent`,
> EventBus), promosso da ecosistema stand-alone a motore ufficiale del Backbone.
>
> **Fase 1 pilota (YouTube + Stream-S7-Bot) chiusa, esito misto — stato reale, non aspirazionale:**
> - **YouTube (YOUTUBE-AUTOMATION-FACTORY): ✅ in uso reale.** `Apex7Orchestrator` istanzia
>   `APEX7Memory(domain="youtube")` + `RuFLOOrchestrator(domain="youtube")`; il punteggio del
>   critic (scoring reale su lunghezza/sezioni/keyword density, invariato) persiste tramite
>   `log_critique()` sul motore condiviso invece di restare locale. Le 6 fasi della fabbrica
>   (scouting→audit) scrivono tutte dati reali, nessun hardcoded residuo, dashboard con
>   PASS/FAIL veri per run. Lotti `TASK-YT-001..005`, chiusi 2026-07-28
>   ([CP-20260728-007](../company/Memory/checkpoints/CP-20260728-007.md) →
>   [CP-20260728-011](../company/Memory/checkpoints/CP-20260728-011.md)).
> - **Stream-S7-Bot: ❌ NON migrato, decisione motivata.** Indagine (`TASK-YT-006`,
>   [CP-20260728-012](../company/Memory/checkpoints/CP-20260728-012.md)): quell'ecosistema ha
>   già un'implementazione APEX-7 Level 2 propria e più matura del motore condiviso su alcuni
>   assi (6 gate a rubrica/33 criteri, Event Bus con DLQ+replay, memory con lock/checkpoint/
>   restore, gate `L6→L7` self-giudicante). Spostarlo su `11-APEX-7-CORE` sarebbe un downgrade
>   funzionale su un sistema che esegue trade reali su Solana mainnet — non eseguito. Il motore
>   condiviso resta quindi a **1 ecosistema pilota reale su 2**, non 2/2 come pianificato:
>   prima di un rollout sui restanti 11 ecosistemi, valutare se portare le funzionalità
>   mancanti (rubrica/DLQ/replay/checkpoint) dentro `11-APEX-7-CORE` — raccomandazione aperta
>   per Max, non decisa qui.
>
> Dettaglio tecnico completo: [CP-20260728-001](../company/Memory/checkpoints/CP-20260728-001.md).

**Regola madre (ereditata da CF, ADR-005):** Ruflo COORDINA (stato, memoria, swarm, consensus),
Claude Code ESEGUE (file, codice, contenuti). Ogni componente del Backbone ha un percorso MCP
(quando il daemon è su) e un fallback bash/file (quando non lo è). Mai un single point of failure.

---

## 1. CORPORATE BACKBONE — i 6 componenti

### 1.1 BUS — Message Bus a 2 livelli

**Missione.** Il sistema nervoso di EMPIRE OS: nessuna azione isolata, ogni passaggio di lavoro
tra agenti, team, reparti ed ecosistemi è un **messaggio tracciato e append-only** (audit, replay,
apprendimento dai pattern di comunicazione).

**Design concreto per DE.**
- **Livello INTRA** (`company/orchestrator/bus.sh`): team↔team dentro un ecosistema.
  Stato: `company/runtime/bus/<ecosistema>/messages.jsonl`.
- **Livello INTER** (`company/orchestrator/gbus.sh`): ecosistema↔ecosistema e Board↔ecosistemi.
  Stato: `company/runtime/group-bus/messages.jsonl`. Mittenti/destinatari validi: i 10 ecosistemi
  + `BOARD` + `EMPIRE` (dipartimento supremo) — validati contro Identity-HR.
- **Cartelle handoffs per ecosistema**: oltre al jsonl (flusso), ogni handoff "pesante" (payload
  multi-file: copy, video, report) vive come file in
  `company/Ecosistemi/<ECO>/handoffs/{inbox,outbox,archive}/H-<id>.json` — il jsonl trasporta il
  riferimento, la cartella trasporta il contenuto. Pattern già validato da Memory Empire v3.

**Handoff contract standard (obbligatorio, pattern #2 del Piano Maestro):**
```json
{
  "id": "H-20260610-0042",
  "ts": "2026-06-10T15:30:00Z",
  "scope": "inter|intra",
  "from": "AGENCY/Acquisizione/WF-OUTREACH-EMAIL",
  "to": "MARKETING/Copywriting/T-email-writer",
  "priority": "CRITICAL|HIGH|NORMAL|LOW",
  "type": "directive|handoff|result|escalation",
  "payload": { "task": "...", "files": ["..."], "brand_kit": "DE|<cliente>", "icp": "..." },
  "acceptance_criteria": ["max 150 parole", "APSOC completo", "zero claim non provabili"],
  "status": "pending|accepted|in_progress|done|rejected|escalated"
}
```
Regole: (a) un handoff senza `acceptance_criteria` misurabili è INVALIDO e il coordinator lo
rifiuta; (b) `status=rejected` DEVE includere note correttive; (c) 2 reject consecutivi → `type:
escalation` automatica al reparto superiore via gbus.

**Differenza vs CF Exponium.** CF ha 6 ecosistemi validi e payload mono-brand; DE ne ha 9 + il
campo `brand_kit`/`icp` obbligatorio nel payload (pattern #11 multi-tenant: stesso bus per DE,
clienti agency, canali YT, libri KDP). CF non ha cartelle handoffs per ecosistema (solo jsonl);
DE le aggiunge per i deliverable multi-file.

**Fasi di build.** B2.1 script bus.sh/gbus.sh portati da CF e adattati (10 ecosistemi) → B2.2
cartelle handoffs + schema JSON validato (script `validate-handoff.sh`) → B2.3 wiring nei primi
workflow reali (outreach AGENCY, F4).

---

### 1.2 BRAIN — Memoria a 3 strati

**Missione.** Il cervello aziendale: una sola verità, tre rappresentazioni — leggibile dagli
umani, ricercabile semanticamente dagli agenti, distillata in pattern dagli errori.

**Architettura a 3 strati (design DE):**

| Strato | Per chi | Tecnologia | Dove |
|---|---|---|---|
| **1. Wiki** (fonte di verità) | Umani + Claude in sessione | Markdown Obsidian, regola wiki-first | `second-brain-vault/wiki/` (index.md + log.md) |
| **2. AgentDB** (indice semantico) | Agenti running | Ruflo `memory_store/search`, HNSW 384-dim, 150x-12500x speedup | namespace per ecosistema (sotto) |
| **3. ReasoningBank** (errori→pattern) | Loop di auto-miglioramento | `reasoningbank-*`: trajectory → verdict → distill | namespace `patterns/` |

**Namespace AgentDB per ecosistema** (ogni `BACKBONE.md` di ecosistema li dichiara):
`agency/` (lead, clienti, preventivi) · `infobusiness/` (lanci, offerte) · `contentfactory/`
(hook, format vincenti) · `marketing/` (copy APSOC validati, angle) · `multibusiness/` (KDP,
YT, ecomm) · `platform/` (decisioni tecniche, ADR) · `forge/` (template agenti/skill) ·
`intelligence/` (ricerche, trend) · `operations/` (run, costi) · `memory/` (checkpoints,
decisions, state, sessions — indice semantico dell'ecosistema 10 MEMORY, vedi
09-ECOSISTEMA-MEMORY.md §9) · trasversali: `identity/`, `decisions/board/`, `patterns/`,
`mandato/`.

**Regole di sincronizzazione (wiki ↔ AgentDB), eseguite dal wiki-syncer di Memory Empire:**
1. Ogni pagina wiki nuova/modificata → `memory_store` dell'abstract + path nel namespace giusto
   (la wiki resta il contenuto integrale; AgentDB indicizza, non duplica).
2. Ogni pattern distillato dal ReasoningBank con ≥3 conferme → promosso a pagina wiki in
   `concepts/` o `synthesis/` (gli umani devono poter leggere ciò che gli agenti imparano).
3. Ogni operazione (ingest, decisione board, hire/retire) → entry obbligatoria in `wiki/log.md`
   (pattern #12 wiki-first). Il Drift-Sentinel verifica il lag di sync (KPI: < 24h).
4. Conflitto wiki vs AgentDB → **vince la wiki** (fonte di verità umana); AgentDB si reindicizza.
- Fallback senza daemon: mirror locale `company/runtime/brain/<ns>.jsonl` + `brain.sh recall`
  (grep sul mirror) — modello ibrido ADR-005 di CF, portato pari pari.

**Differenza vs CF Exponium.** CF ha 2 strati (AgentDB + mirror) e la conoscenza vive nei file
orchestration; DE ha la wiki second-brain come strato sovrano + Memory Empire v3 come router e
arricchitore (CF non ha equivalente). La regola "vince la wiki" è nuova ed è il guard-rail
contro la divergenza (rischio §9 del Piano Maestro).

**Fasi di build.** B2.4 `ruflo init` + memory init in `company/` → B2.5 brain.sh + mirror →
B2.6 wiki-syncer attivo (estensione skill memory-empire) → B2.7 ReasoningBank wired sui primi
fallimenti reali (F4+).

---

### 1.3 GOVERNANCE & QA — il gate unico

**Missione.** Niente esce senza controllo: un solo cancello componibile che blocca deliverable
non conformi PRIMA della consegna/pubblicazione. Exit 0 = APPROVATO, exit 1 = BLOCCATO con note
correttive precise. **I gate non sono bypassabili**: nessun flag `--skip`, nessuna eccezione
inline; l'unica via è correggere o ottenere deroga registrata dal Board (hive-mind raft,
depositata in `decisions/board/`).

**Design concreto: `company/orchestrator/verify.sh` Empire — 5 categorie di check:**

| Categoria | Check (esempi) | Strumento |
|---|---|---|
| **1. Struttura** | albero company/ integro, ogni team ha i 7 file canonici, YAML/JSON validi, zero workflow orfani, link wiki non rotti | bash + python lint |
| **2. Brand / Mandato Empire** | voce diretta-provocatoria-trasparente, "prove non promesse" (zero claim senza evidenza), pricing one-time no-canoni, posizionamento "agenzia progettata per essere licenziata" rispettato | checklist + agente Brand-Voice (Haiku) |
| **3. Qualità copy APSOC** | tutti i 6 blocchi presenti (Attenzione-Problema-Promessa-Social Proof-Obiezioni-CTA), hook nei primi 2 righi, una sola CTA primaria, lunghezza nei limiti del format | skill cro-copy-architect in modalità audit |
| **4. Costi** | dry-run eseguito prima del run reale (pattern #3), stima ≤ envelope del reparto, tier modello coerente con la routing policy (§2.3), nessun Opus su task Tier 0/1 | cost-estimator + log routing |
| **5. Sicurezza** | zero segreti tracciati (.env, token, credenziali), scan PII su output destinati all'esterno, supply-chain skill/vendor | `aidefence_scan/is_safe/has_pii` + git-secrets |

In più, come in CF: **contradiction gate** — `skill-contradiction-analyzer` (già installata) gira
su ogni nuova skill/SOP/pagina Mandato: zero contraddizioni bloccanti tra documenti normativi.

**Differenza vs CF Exponium.** Il verify.sh di CF (68 check) è centrato su spec video (ffprobe,
aspect 9:16, durata, caption); quello DE è **multi-dominio**: copy, brand, preventivi, siti,
libri, video. La categoria 2 (Mandato Empire) e la 3 (APSOC) non esistono in CF. La CI GitHub
esegue lo stesso gate su ogni push (come CF).

**Fasi di build.** B2.8 verify.sh categorie 1+5 (struttura+sicurezza, deterministiche) → B3
categorie 2+3 (brand+APSOC, richiedono agente giudice) → B4 categoria 4 (costi, richiede
observability). Gate "verify verde" = condizione di chiusura della fase F2 della roadmap.

---

### 1.4 IDENTITY-HR — il registro unico degli agenti

**Missione.** La fonte di verità su "chi lavora qui": ogni agente (di ruolo e reale/running)
anagrafato con ruolo, costo, performance. La **FORGE assume** (registra alla creazione) e
**ritira** (su segnalazione di Cost-Sentinel/evolve quando inefficace).

**Design concreto:** `company/Backbone/Identity-HR/registro-agenti.yaml` (+ vista generata
`registro-agenti.md`, NON modificare a mano) + persistenza `company/runtime/identity/agents.jsonl`
+ roster nel Brain (namespace `identity/`). Schema record:

```yaml
- id: AGY-ACQ-email-writer-01        # <ECO>-<REPARTO>-<ruolo>-<seq>
  ecosistema: AGENCY
  reparto: Acquisizione
  team: WF-OUTREACH-EMAIL
  ruolo: worker                       # coordinator | worker | sentinel | guild-lead
  tier_modello: 2                     # 0=WASM 1=Haiku 2=Sonnet 3=Opus (policy §2.3)
  costo: { stimato_run: 0.04, cumulativo_30g: 1.20 }   # USD
  performance: { task_done: 87, pass_rate_gate: 0.94, reject_rate: 0.03 }
  stato: active                       # active | idle | retired
  assunto: 2026-06-15  da: FORGE
```

Ciclo di vita: FORGE `agent_spawn` → record creato → Observability aggiorna costo/performance →
pass_rate < soglia o idle > 14g → segnalazione → FORGE ritira (`agent_terminate`) →
`stato: retired` (mai cancellato: storia = apprendimento). Query operative: "chi può fare X?",
"chi costa troppo?", "chi è idle?" via `agent_list` o grep sul yaml.

**Differenza vs CF Exponium.** CF usa registro md + jsonl senza tier modello né performance
strutturata; DE impone YAML tipato con `tier_modello`, `pass_rate_gate` e costo cumulativo —
necessari perché i 10 ecosistemi condividono budget e il routing 3-tier è policy (non scelta
del singolo team).

**Fasi di build.** B2.9 schema yaml + generatore vista md → B4 (roadmap F4) primi agenti reali
AGENCY anagrafati → F8 ciclo hire/retire automatico con la FORGE.

---

### 1.5 OBSERVABILITY — occhi, costi, dashboard

**Missione.** Misurare tutto, attribuire i costi, alimentare l'apprendimento, predire i colli
di bottiglia prima che blocchino.

**Design concreto per DE:**
- **Metrics**: `company/metrics/runs.jsonl` — eventi standard: `run_done`, `gate_passed`,
  `gate_failed`, `handoff_rejected`, `swarm_done`, `lead_generated`, `content_published`,
  `sale_closed`, `evolution`. Ogni evento porta `{eco, reparto, team, agente, brand_kit, costo}`.
- **Cost-attribution multi-tenant**: aggregazioni per agente, per team, per ecosistema E per
  `brand_kit` (quanto costa servire il cliente X? quanto costa il canale YT Y?) →
  `company/metrics/cost/by-{agent,team,eco,brand}.json` rigenerati da `costs.sh`.
- **Dashboard**: `company/orchestrator/dashboard.sh` — vista unica: stato 10 ecosistemi, agenti
  attivi/idle, backlog bus, ultimi gate, costo giornaliero vs envelope, alert Sentinels.
- **Learning**: le metriche alimentano `neural_train` (pattern), `autopilot_predict`
  (bottleneck), `evolve` (FORGE crea/ritira). Fallback senza MCP: i jsonl locali bastano per
  dashboard ed evolve (come in CF).

**Differenza vs CF Exponium.** CF misura produzioni video e swarm; DE aggiunge (a) eventi di
**revenue** (lead, vendite — i criteri "output reale misurabile" del DONE WHEN §0) e (b)
cost-attribution **per brand/cliente** (multi-tenant), che in CF non esiste.

**Fasi di build.** B2.10 runs.jsonl + emettitori negli script → B4 dashboard.sh → F8
neural/autopilot wired.

---

### 1.6 COORDINATION FABRIC — topologie e consenso

**Missione.** Decidere COME gli agenti lavorano insieme (topologia swarm) e COME si decide
collettivamente (consenso hive-mind). 100 agenti in parallelo senza caos.

**Mappa topologia → ecosistema (design DE, hierarchical = default Ruflo):**

| Ecosistema | Topologia | Perché |
|---|---|---|
| 01 AGENCY | hierarchical | catena di comando: delivery clienti = anti-drift, responsabilità chiare per SLA |
| 02 INFO-BUSINESS | ring | un lancio è una pipeline sequenziale (pre-lancio→cart open→close): ogni fase passa il testimone |
| 03 CONTENT-FACTORY | hierarchical + mesh nei batch | strategia top-down, ma la produzione multi-formato (20 post, 10 caroselli) è fan-out mesh |
| 04 MARKETING | star | hub centrale = copy engine APSOC (cro-copy-architect): ogni output copy passa dal hub per coerenza di voce |
| 05 MULTI-BUSINESS | mesh | 3 business indipendenti (YT, Ecomm, KDP) senza dipendenze reciproche: massimo parallelismo |
| 06 PLATFORM | hierarchical | engineering SPARC: spec→pseudocode→architecture→code, sequenza gateata |
| 07 FORGE | star | hub = skill-creator/omega-create; ogni nuovo asset organizzativo nasce dal centro e viene validato lì |
| 08 INTELLIGENCE | mesh | ricerche e ingest paralleli e indipendenti (Empire Studio multi-fonte) |
| 09 OPERATIONS | mesh | mass-production: N job identici indipendenti (pattern CF OPERATIONS) |
| 10 MEMORY | hierarchical | ME-Conductor root (recall/checkpoint sono flussi gateati); sync-agent in mesh col Backbone Brain |
| BOARD (L0) | hive-mind **raft** | decisioni cross-ecosistema leader-based anti-drift (default CF, confermato) |
| Decisioni critiche/sicurezza | hive-mind **byzantine** | tollera guasti/attori anomali (es. deroghe gate, spese straordinarie) |
| Membership swarm | **quorum** | ingresso/uscita agenti dagli swarm |
| Stato condiviso eventually-consistent | **crdt** / **gossip** | merge metriche e propagazione stato su molti nodi |

**Differenza vs CF Exponium.** CF usa di fatto 3 configurazioni (hierarchical, mesh,
hierarchical-mesh di gruppo) per 6 ecosistemi mono-scopo; DE mappa **tutte e 4 le topologie**
Ruflo (hierarchical/mesh/ring/star) su 10 ecosistemi con razionale per ciascuno, e formalizza
ring (lanci) e star (copy hub, forge hub) che CF non usa.

**Fasi di build.** B2.11 `swarm_init` di gruppo (hierarchical) + hive-mind raft Board →
F4 swarm AGENCY → F5 star MARKETING + mesh CONTENT-FACTORY → F8 tutte le topologie attive.

---

## 2. INTEGRAZIONE RUFLO OPERATIVA

### 2.1 Piano di rollout

Ruflo@3.10.13 è installato **globale** (npm -g): il comando esiste ovunque, ma l'init è
**per-cartella**. Sequenza (fase F2 della roadmap):

| # | Azione | Comando / dove | Verifica |
|---|---|---|---|
| 1 | Init nella root di EMPIRE OS | `ruflo init` in `Digital Empire/company/` | `.ruflo/` creato |
| 2 | Daemon attivo | `ruflo daemon start` (+ task pianificata Windows per restart al boot — rischio daemon non persistente, §9 Piano Maestro) | `ruflo daemon status` |
| 3 | Memoria inizializzata | `ruflo memory init` + creazione namespace §1.2 | `memory_search` risponde |
| 4 | MCP registrato per Claude Code | `claude mcp add ruflo -- ruflo mcp start` (scope project su `company/`) | tools `mcp__ruflo__*` visibili |
| 5 | Hooks attivi | hooks pre/post-task (27+12 workers) per checkpoint memoria + metriche | `hooks_metrics` |
| 6 | Swarm+hive di gruppo | `swarm_init` (hierarchical) + `hive-mind_init` (raft, queen=Empire-Conductor) | id persistiti in `Coordination/README` |

Bootstrap auto-riparante: `company/orchestrator/bootstrap.sh` controlla daemon→memoria→swarm
e ripara ciò che manca (pattern CF). Ogni `BACKBONE.md` di ecosistema dichiara namespace e
topologia che usa (azione concreta §5 del Piano Maestro).

### 2.2 Tabella funzione → tool MCP (estende PLAN-05 §9 di CF)

| Funzione EMPIRE OS | Tool Ruflo MCP | Fallback bash (ADR-005) |
|---|---|---|
| Coordinamento ecosistemi | `swarm_init`, `swarm_status`, `coordination_orchestrate`, `coordination_topology` | `fabric.sh status` + registri jsonl |
| Decisioni Board | `hive-mind_init/propose/vote/consensus` | decisione manuale loggata in `decisions/board/` |
| Cervello | `memory_store/search/search_unified`, `agentdb_*` | `brain.sh store/recall` su mirror jsonl |
| Apprendimento | `neural_train/predict`, `reasoningbank-*`, `autopilot_*` | `evolve.sh cycle` sui metrics locali |
| Agenti reali | `agent_spawn`, `managed_agent_*`, `agent_list/terminate` + Agent tool Claude Code | Agent tool puro + registro yaml a mano |
| Sicurezza | `aidefence_scan/is_safe/has_pii` | git-secrets + checklist PII in verify.sh |
| Workflow dinamici | `task_orchestrate`, `workflow_create/execute` | skill copy-workflow / workflow-automation |
| Osservabilità | `performance_*`, `system_health`, `hooks_metrics` | `dashboard.sh` sui jsonl |
| Routing modelli | 3-tier router + Thompson Sampling | tabella statica §2.3 applicata dal coordinator |

### 2.3 Routing policy 3-tier per tipo di task DE

| Tier | Modello | Task DE tipici | Regola |
|---|---|---|---|
| 0 | WASM (gratis) | validazione JSON/YAML handoff, routing bus, aggregazione metriche, rename/file ops | tutto ciò che è deterministico NON tocca un LLM |
| 1 | Haiku | qualifica lead, tagging, estrazione dati, meta description, alt-text, QA checklist semplici, classificazione messaggi bus | default per classificazione/estrazione |
| 2 | Sonnet | copy standard (email, post, caroselli), codice, ricerca, report, qualifica complessa, draft preventivi | default produzione |
| 3 | Opus | sales page APSOC, preventivi finali (beast-preventivi), architettura sistemi, decisioni Board, debugging difficile | SOLO con giustificazione; il Cost-Sentinel segnala Opus su task Tier ≤1 |

Thompson Sampling di Ruflo ottimizza nel tempo dentro questi vincoli; la tabella è il prior e
il limite. Ogni run logga `tier_usato` per la cost-attribution.

### 2.4 Pattern ibrido (se MCP cade)

Identico ad ADR-005 di CF: ogni script ha doppio percorso — prova MCP/CLI ruflo, se assente
scrive/legge il mirror locale (`runtime/brain/`, `runtime/bus/`, `metrics/`). Il sistema
**degrada, non si ferma**: il bus resta jsonl append-only, il brain resta grep-abile, il gate
resta bash puro. Al ritorno del daemon, `bootstrap.sh` riallinea i mirror in AgentDB.

---

## 3. REGISTRO SKILL

### 3.1 Censimento reale

`C:\Users\Utente\.claude\skills\` contiene **121 skill globali** (censite via listing directory,
2026-06-10). Mappa per ecosistema (famiglie raggruppate, conteggi reali):

| Skill / famiglia | n | Ecosistema | Reparto |
|---|---|---|---|
| `avvia-email/-ig/-linkedin/-parallel/-scraper` | 5 | AGENCY | Acquisizione (runtime in OPERATIONS) |
| `cold-email`, `agency-scalping`, `sales-enablement`, `revops` | 4 | AGENCY | Acquisizione |
| `beast-preventivi` | 1 | AGENCY | Preventivi |
| `cro`, `onboarding` | 2 | AGENCY | Operatività/Delivery |
| `launch`, `community-marketing`, `lead-magnets` | 3 | INFO-BUSINESS | Lanci · Prodotto |
| `content-strategy`, `social`, `video`, `image`, `canvas-design`, `theme-factory`, `brand-guidelines` | 7 | CONTENT-FACTORY | Strategia · Video · Visual&Design |
| `market` + `market-*` (suite completa) | 15 | MARKETING | tutti i reparti (orchestratore + verticali) |
| `copywriting`, `copy-workflow`, `copy-editing`, `cro-copy-architect`, `emails`, `sms` | 6 | MARKETING | Copywriting · Email |
| `ads`, `ad-creative`, `co-marketing`, `referrals`, `popups`, `free-tools`, `directory-submissions` | 7 | MARKETING | Advertising · Growth |
| `seo-audit`, `ai-seo`, `programmatic-seo`, `schema`, `competitors` | 5 | MARKETING | SEO |
| `analytics`, `ab-testing`, `pricing`, `product-marketing`, `marketing-ideas`, `marketing-psychology` | 6 | MARKETING | Analytics · Strategy |
| `printing-press` + 9 sub-skill | 10 | MULTI-BUSINESS | Publishing/KDP |
| `aso`, `paywalls`, `signup`, `churn-prevention` | 4 | MULTI-BUSINESS | SaaS/App |
| `site` + 15 sub-skill (`site-3d`…`site-stack`) | 16 | PLATFORM | Siti (Crea Siti) |
| `empire-premium-style`, `frontend-design`, `playwright-dev`, `github-automation`, `pair-programming`, `impeccable`, `opus`, `prd-architect-os`, `sparc-methodology` | 9 | PLATFORM | Engineering |
| `agent-architecture/-coder/-planner/-researcher/-reviewer/-specification/-tester` | 7 | PLATFORM | Engineering (pipeline SPARC; la FORGE li riusa) |
| `skill-creator`, `omega-create`, `content-forge`, `book-to-skill` | 4 | FORGE | Builder skill/agenti |
| `memory-empire`, `wiki-context`, `memory-management`, `customer-research`, `competitor-profiling` | 5 | INTELLIGENCE | Second Brain · Ricerca |
| `swarm-orchestration`, `workflow-automation`, `hooks-automation` | 3 | OPERATIONS | Runtime/Coordinamento |
| `verification-quality`, `skill-contradiction-analyzer` | 2 | BACKBONE | Governance & QA |
| **Totale** | **121** | | |

La mappa completa skill→reparto vive (e si mantiene) in `company/skills-map.yaml` (come in CF):
questa tabella è la vista; il yaml è il dato. Zero orfani = gate della fase F3.

### 3.2 Nuove skill trasversali da creare (in ordine di build)

| # | Skill | Cosa fa | Equivalente CF |
|---|---|---|---|
| 1 | **`empire-context`** | knowledge base DE per agenti (sotto) | `exponium-context` |
| 2 | `empire-brand-kit` | carica il brand kit attivo (DE o cliente/canale): voce, palette, ICP, offerta, vincoli — input del pattern multi-tenant #11 | MANDATO (parziale) |
| 3 | `empire-handoff` | crea/valida/instrada handoff conformi al contract §1.1 (wrapper di bus.sh/gbus.sh) | gbus.sh (solo script) |
| 4 | `empire-verify` | invoca il gate §1.3 e spiega i blocchi con note correttive | verify.sh (solo script) |
| 5 | `empire-hr` | interroga/aggiorna il registro agenti (chi può fare X, costi, hire/retire con FORGE) | registro-agenti.md |
| 6 | `empire-dashboard` | stato del gruppo in linguaggio naturale (wrapping dashboard.sh + metrics) | dashboard.sh |
| 7 | `empire-cost` | stima dry-run di un workflow + verifica envelope prima del run reale | (parte di evolve) |
| 8 | `empire-sentinel` | definizione/runbook dei 5 Sentinels, usata per spawnarli always-on | Sentinels/*.md |
| 9 | `empire-memory-gate` | pre-task gate ecosistema 10 MEMORY: carica INDEX+STATO+CP/ADR rilevanti (context-pack) | — (nuovo, 09 §8) |
| 10 | `empire-checkpoint` | post-task commit: scrive CP da template + sync wiki/AgentDB | — (nuovo, 09 §8) |
| 11 | `empire-adr` | registra ADR + contradiction-check contro decisioni attive | — (nuovo, 09 §8) |
| 12 | `empire-stato` | legge/aggiorna STATO-EMPIRE dal filesystem reale (mai dichiarato) | catalog_status.py (pattern) |

#### 3.2.1 `empire-context` — la PRIMA skill da creare

**Missione.** L'equivalente DE di `exponium-context`: il **contesto aziendale compresso** che
ogni agente carica prima di lavorare. Senza, ogni agente reinventa chi è Digital Empire; con,
ogni output nasce già dentro il Mandato.

**Contenuto del kernel (SKILL.md ≤500 righe, pattern #7 progressive disclosure):**
1. **Identità e Mandato Empire** — posizionamento ("l'agenzia progettata per essere licenziata"),
   brand voice (diretta, provocatoria, trasparente, "prove non promesse"), pricing one-time.
2. **I 10 ecosistemi** — missione di ciascuno in 1 riga + a chi chiedere cosa (routing).
3. **Offerta attuale** — 3 implementazioni AI: Outreach Factory €4.000, Content Factory €3.500,
   Second Brain €2.500, Engine Room €8.000 (codice del cliente, €0 canoni, setup 7gg).
4. **Regole non negoziabili** — i 13 pattern del Piano Maestro §6 in forma di invariant
   (incluso #13 memory-first: interroga `company/Memory/` prima, checkpoint dopo).
5. **Dove sta la conoscenza** — wiki (verità), AgentDB namespace (ricerca), come loggare.
6. `references/` — Mandato esteso, brand voice guide v2.0, APSOC, listino, casi studio.

**Trigger:** caricata da OGNI agente spawned in `company/` (hook pre-task) e da ogni skill
`empire-*`. **Build:** con `skill-creator`, sorgenti = Mandato + wiki index + Piano Maestro;
gate = contradiction-analyzer su kernel vs Mandato. È il primo deliverable della fase B3.

---

## 4. SENTINELS & GUILDS

### 4.1 I 5 Sentinels (agenti autonomi always-on — pattern #10)

Formato ereditato da CF (trigger→azione→escalation, runbook in `company/Sentinels/<nome>.md`):

| Sentinel | Vigila su | Trigger (soglie) | Azioni autonome | Escalation |
|---|---|---|---|---|
| **Cost** | crediti per eco/agente/brand | 60% envelope=log · 80%=warning · 95%=blocco task non urgenti · 100%+accelerazione=crisi; Opus su task Tier≤1; agente in loop (velocità >20x per >2min) | notifica C-level+CFO, blocco preventivo, sospensione agente in loop, raccomandazione downgrade | CFO → CEO-Conductor (crisi) |
| **Quality** | pass-rate gate, reject handoff | pass_rate < 90% su 10 run · 2 reject consecutivi stesso team · trend qualità in calo 3 cicli | blocco consegna, richiesta rework con note, segnala team alla Quality-Guild | CTO → Board |
| **Drift** | coerenza architetturale e wiki-sync | contraddizione bloccante (contradiction-analyzer) · wiki/AgentDB lag >24h · team che opera fuori dal proprio reparto · doc normativo modificato senza log | blocco merge, forza sync wiki-syncer, apre issue di riallineamento | CTO + Chief-Forge → Board (raft) |
| **Security** | segreti, PII, supply-chain | secret in commit · PII in output esterno (aidefence) · skill/vendor non verificati · permessi anomali | blocco push/invio immediato, quarantena artefatto, scan completo | CTO → CEO (byzantine se compromissione sospetta) |
| **Brand-Voice** | Mandato Empire su ogni output esterno | claim senza prova · tono fuori voce · canoni/pricing non conformi · APSOC incompleto su asset di conversione | blocco pubblicazione, rewrite request al copy hub (MARKETING star) | CMO → Dipartimento Empire (LX, autorità suprema) |

Regole comuni: ogni intervento è depositato nel Brain (`patterns/incidents/`) per
auto-calibrazione; le soglie le configura la Guild competente e le approva il C-level; nessun
Sentinel può essere spento senza decisione Board registrata.

### 4.2 Le 5 Guilds (comunità di pratica trasversali)

| Guild | Standardizza | Deliverable | Sponsor C-level |
|---|---|---|---|
| **Prompt** | struttura prompt, context engineering, template per task/modello, anti-pattern, chaining | Prompt Library nel Brain (`patterns/prompt/`) | CTO |
| **Copy/APSOC** | il framework APSOC come spina dorsale, tone of voice per brand_kit, swipe file validati, regole per formato (email/sales page/ads/DM) | APSOC Playbook + libreria copy validati (`marketing/`) | CMO |
| **Quality** | acceptance criteria standard, rubriche di valutazione, definizione di "done" per tipo di deliverable | rubriche per verify.sh cat.3, benchmark interni | CTO |
| **Cost** | routing table 3-tier (§2.3), envelope per reparto, soglie Cost-Sentinel, regole dry-run | routing policy + envelope yaml | CFO |
| **Design** | design system Empire (empire-premium-style: ink/paper/orange #fb4604), template visual, regole brand kit per cliente | DE Design System + template library | CMO |

Funzionamento (come Prompt-Guild CF): raccolta pattern dagli ecosistemi via ReasoningBank →
validazione su benchmark → pubblicazione nel Brain → notifica via Bus. Ingaggio passivo
(`memory_search` sul namespace) o attivo (richiesta via gbus `new-template-request`).
Differenza vs CF: CF ha Security-Guild e Data-Memory-Guild; in DE la sicurezza è assorbita dal
Security-Sentinel + PLATFORM, e la memoria dal componente Brain + INTELLIGENCE — al loro posto
entrano **Copy/APSOC** (il copy è priorità assoluta del Piano Maestro) e **Design**.

---

## 5. STRUTTURA FILESYSTEM — `Digital Empire/company/`

```
company/
├── GRUPPO.md                          # org chart EMPIRE OS + indice (come GRUPPO.md di CF)
├── skills-map.yaml                    # mappa 121+ skill → ecosistema/reparto (§3.1)
├── Mandato/                           # LX — DIPARTIMENTO EMPIRE (autorità suprema)
│   ├── MANDATO-EMPIRE.md              # posizionamento, voce, pricing, qualità (≈ MANDATO-EXPONIUM)
│   └── README.md                      # come il Mandato vincola Board ed ecosistemi
├── Board-CSuite/                      # L0
│   ├── README.md  Council.md
│   ├── CEO-Conductor.md  COO.md  CTO.md  CMO.md  CRO-Revenue.md  CFO.md  Chief-Forge.md
├── Ecosistemi/                        # L1 — ognuno: {ECOSISTEMA.md, BACKBONE.md,
│   │                                  #   Reparti/, Workflow/, Funzioni/, Agenti/, handoffs/}
│   ├── 01-AGENCY/        02-INFO-BUSINESS/   03-CONTENT-FACTORY/
│   ├── 04-MARKETING/     05-MULTI-BUSINESS/  06-PLATFORM/
│   ├── 07-FORGE/         08-INTELLIGENCE/    09-OPERATIONS/
│   └── 10-MEMORY/                     # org dell'ecosistema; i DATI vivono in company/Memory/
├── Memory/                            # ✅ GIÀ COSTRUITA (ME-0/ME-1, 2026-06-10): INDEX.md,
│   │                                  #   STATO-EMPIRE.md, checkpoints/, decisions/, plans/,
│   │                                  #   sessions/, tasks/<eco>/, state/, audit/, templates/
│   │                                  #   → dossier 09-ECOSISTEMA-MEMORY.md
├── Backbone/                          # servizi condivisi (§1) — README per componente
│   ├── Bus/  Brain/  Governance/  Identity-HR/  Observability/  Coordination/
│   └── Identity-HR/registro-agenti.yaml
├── Guilds/                            # §4.2
│   ├── README.md  Prompt-Guild.md  Copy-APSOC-Guild.md  Quality-Guild.md
│   ├── Cost-Guild.md  Design-Guild.md
├── Sentinels/                         # §4.1
│   ├── README.md  Cost-Sentinel.md  Quality-Sentinel.md  Drift-Sentinel.md
│   ├── Security-Sentinel.md  Brand-Voice-Sentinel.md
├── Gerarchia/                         # spiegazione livelli LX/L0..L5 + cross-cutting
│   ├── README.md  L2-Reparti.md  L3-Workflow.md  L4-Funzioni.md  L5-Agenti.md
├── orchestrator/                      # script eseguibili (bash, doppio percorso MCP/file)
│   ├── bootstrap.sh  bus.sh  gbus.sh  brain.sh  verify.sh  governance.sh
│   ├── dashboard.sh  costs.sh  evolve.sh  fabric.sh  validate-handoff.sh
├── runtime/                           # stato vivo (gitignore parziale)
│   ├── bus/<eco>/messages.jsonl  group-bus/messages.jsonl
│   ├── brain/<ns>.jsonl  identity/agents.jsonl
└── metrics/                           # runs.jsonl, cost/, improvements/, evolutions/
```

Convenzione (da CF): ogni nodo ha un README "cosa fa · come si collega · come ragiona quando si
attiva". Differenze vs CF: cartella `Mandato/` esplicita (in CF è dentro `Exponium/`), ecosistemi
numerati 01-09, cartelle `handoffs/` per ecosistema, registro HR in YAML.

---

## 6. KPI DEL BACKBONE + FASI DI BUILD

### 6.1 KPI (misurati da Observability, vigilati dai Sentinels)

| KPI | Target | Componente |
|---|---|---|
| Backlog bus (messaggi pending > 24h) | 0 | Bus |
| Handoff invalidi (senza acceptance criteria) | 0% | Bus / Governance |
| Lag sync wiki ↔ AgentDB | < 24h | Brain (Drift-Sentinel) |
| Pattern distillati promossi a wiki / mese | ≥ 4 | Brain / ReasoningBank |
| Pass-rate verify.sh al primo colpo | ≥ 90% | Governance |
| Gate bypassati | 0 (per definizione) | Governance |
| Copertura registro agenti (agenti running anagrafati) | 100% | Identity-HR |
| Costo attribuito (eventi con costo e brand_kit) | ≥ 95% | Observability |
| Quota task su tier corretto (vs policy §2.3) | ≥ 90% | Coordination / Cost |
| Skill orfane (non mappate in skills-map.yaml) | 0 | Registro skill |
| Interventi Sentinel depositati nel Brain | 100% | Sentinels |

### 6.2 Fasi di build con gate (dettaglio della F2 roadmap + aggancio F3-F8)

| Build | Cosa | Gate (non bypassabile) |
|---|---|---|
| **B1** | Scaffolding `company/` completo (§5) + GRUPPO.md + Mandato/ | albero navigabile, README ovunque, contradiction-analyzer verde sul Mandato |
| **B2** | Bus (bus.sh/gbus.sh + handoffs/) · Brain (ruflo init, namespace, mirror) · Coordination (swarm+hive di gruppo) | handoff di test attraversa 2 ecosistemi e torna `done`; `memory_search` risponde; fallback testato a daemon spento |
| **B3** | Governance: verify.sh 5 categorie + `empire-context` + `empire-brand-kit`/`empire-handoff`/`empire-verify` | verify.sh verde sull'intero `company/`; empire-context passa il contradiction gate |
| **B4** | Identity-HR (yaml + primi agenti reali AGENCY) + Observability (metrics, dashboard, cost-attribution) | 100% agenti running anagrafati; dashboard mostra costo reale di un run |
| **B5** | Sentinels always-on (5) + Guilds documentate + soglie approvate | ogni Sentinel ha runbook + un intervento simulato end-to-end loggato nel Brain |
| **B6** | Auto-miglioramento: ReasoningBank + neural_train + evolve + ciclo hire/retire FORGE | primo pattern distillato da fallimento reale promosso in wiki (≈ F8 roadmap) |

Regola di costruzione (metodo §7 Piano Maestro): una build per ciclo, verify ad ogni step,
checkpoint memoria, output REALE prima di passare oltre — il Backbone esiste per servire i
flussi di F4-F7 (lead, contenuti, lanci, video), non per essere una cattedrale.

---

## Connessioni

- [[00-PIANO-MAESTRO]] — §2 gerarchia, §4 backbone, §5 Ruflo, §6 pattern (questo dossier li rende esecutivi)
- [[projects/Exponium/Exponium_Content_Factory_Studio]] — modello AION GROUP (Backbone/, PLAN-05 §4-5-9)
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo 3.10.13 globale: swarm, AgentDB, hive-mind, 3-tier routing
- [[Memory_Empire]] — wiki-syncer e router del Brain (strato 1↔2)
- [[Tool_Copy_Workflow_Orchestration]] + [[Framework_Cold_Outreach_APSOC]] — il copy hub (star) di MARKETING
- `08-ROADMAP-FASI.md` — collocazione temporale delle build B1-B6 dentro F2/F3/F8
