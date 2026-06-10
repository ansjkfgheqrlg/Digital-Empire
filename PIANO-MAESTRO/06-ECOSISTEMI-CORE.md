# ⚙️ 06 — ECOSISTEMI CORE: PLATFORM · FORGE · INTELLIGENCE · OPERATIONS

> **Dossier dei 4 ecosistemi trasversali di EMPIRE OS.** Riferimento: [[00-PIANO-MAESTRO]].
> Versione 1.0 · 2026-06-10 · Architettura: modello AION GROUP esteso (L2 reparti → L3 workflow → L4 funzioni → L5 agenti).
> Regola madre ereditata da CF: **un team di agenti per ogni singola funzionalità** — coordinator + workers, I/O espliciti, acceptance criteria, escalation, shared_state.

---

## 0. Panoramica — perché questi 4 sono il sistema operativo

I 5 ecosistemi business (AGENCY, INFO-BUSINESS, CONTENT-FACTORY, MARKETING, MULTI-BUSINESS) **vendono e producono**. I 4 ecosistemi core **rendono possibile vendere e produrre**. (Decimo ecosistema, aggiunto dopo questo dossier: **10 MEMORY** — memoria operativa della holding: checkpoint, ADR, piani, stato; dossier `09-ECOSISTEMA-MEMORY.md`. Non duplica INTELLIGENCE: vedi confini sotto.) Nessun ecosistema business tocca direttamente codice, creazione di agenti, memoria o runtime: lo chiede ai core via handoff contract.

| Core | Metafora OS | Cosa fornisce agli altri 5 | Senza di lui... |
|---|---|---|---|
| **PLATFORM** | Kernel + driver | Codice, siti, deploy, sicurezza, CI/CD | nessun sito, nessun tool, nessuna delivery tecnica Agency |
| **FORGE** | Compilatore + HR | Skill, agenti, team, workflow, interi ecosistemi nuovi | l'organizzazione non cresce né si ripara |
| **INTELLIGENCE** | File system + RAM | Verità (wiki), memoria (AgentDB), ingestione (Empire Studio), enrichment (Memory Empire), ricerca | gli agenti lavorano ciechi e ri-imparano tutto ogni volta |
| **OPERATIONS** | Scheduler + power management | Runtime swarm, cron, budget guard, storage, monitoraggio, dashboard | costi fuori controllo, run manuali, zero osservabilità |

**Tre proprietà che li distinguono dai business:**

1. **Sono multi-tenant per definizione** (pattern #11): PLATFORM costruisce siti per DE *e* per i clienti Agency; FORGE crea team per qualsiasi ecosistema; INTELLIGENCE memorizza per tutti; OPERATIONS misura i costi di tutti.
2. **Sono i custodi dei pattern non negoziabili**: PLATFORM custodisce il codice (#3 dry-run, security), FORGE custodisce lo schema team canonico (#1, #6, #7, #8), INTELLIGENCE custodisce wiki-first e ReasoningBank (#5, #12), OPERATIONS custodisce cost guard e sentinels (#9, #10).
3. **Si costruiscono PRIMA o INSIEME ai business**: la roadmap F1–F3 del Piano Maestro è quasi interamente lavoro dei core (scaffolding, backbone, migrazione asset).

**Flusso tipo end-to-end** — "Agency vende un sito a un cliente":
`AGENCY` (chiude il deal) → `INTELLIGENCE` (carica ICP + brand kit + ricerca competitor) → `MARKETING` (copy APSOC) → `PLATFORM` (build sito via Crea Siti + empire-premium-style + deploy Vercel) → `OPERATIONS` (cost attribution della commessa, scheduling QA ricorrente) → `INTELLIGENCE` (archivia caso studio in wiki). Se nel flusso manca una capacità → `FORGE` la crea.

---

# 06 · PLATFORM — Engineering & Code Custody

## 1. Missione + DONE WHEN

**Missione:** essere il reparto engineering della holding: produrre e mantenere TUTTO il codice di Digital Empire — siti premium (DE e clienti), SaaS/App, tooling interno — con custodia del codice, sicurezza, CI/CD e deploy. PLATFORM è l'unico ecosistema autorizzato a scrivere codice di produzione.

**DONE WHEN:**
1. Il sistema **Crea Siti** (orchestrators + agenti + 20+ skill site-*) è formalizzato come reparto L2 con team L3 documentati, e produce un sito cliente end-to-end senza intervento manuale fuori dai gate.
2. Ogni repo/progetto (`agency-empire-landing`, `SaaS/`, `App/`, siti clienti) ha owner, pipeline di verify e procedura di deploy Vercel documentata.
3. `verify.sh` Empire (gate qualità codice) gira verde su ogni deliverable prima del deploy.
4. Zero codice orfano: ogni script attivo (incl. quelli di Outreach) è censito nel registry PLATFORM con owner e stato.

## 2. Posizione nella holding — handoff

| Da → A | Contratto di handoff |
|---|---|
| AGENCY → PLATFORM | `{brief cliente, brand_kit, icp, scope, deadline}` → sito/implementazione consegnata + codice in custodia cliente |
| MARKETING → PLATFORM | copy APSOC validato → integrato nelle pagine (PLATFORM non scrive copy: lo monta) |
| CONTENT-FACTORY → PLATFORM | asset visual/video → embed e ottimizzazione performance |
| PLATFORM → OPERATIONS | ogni build/deploy emette evento `{commessa, costo, durata, esito}` per cost attribution |
| PLATFORM → INTELLIGENCE | post-mortem tecnici, decisioni d'architettura (ADR) → wiki `tools/` e ReasoningBank |
| FORGE → PLATFORM | nuovi agenti/skill engineering (es. nuova skill site-*) consegnati e installati |
| INTELLIGENCE → PLATFORM | ricerca tecnica (stack, librerie, competitor tecnici) prima di ogni scelta d'architettura |

## 3. Reparti L2 → Workflow L3 → Funzioni L4

```
PLATFORM
├─ L2 WEB-ENGINEERING (il reparto "Crea Siti")
│   ├─ L3 WF-SITE-FULL      brief → plan → design → copy-merge → build → qa → deploy
│   │     L4: T-site-brief · T-site-architecture · T-site-design · T-site-components ·
│   │         T-site-animate · T-site-3d · T-site-seo · T-site-qa · T-site-report
│   ├─ L3 WF-EMPIRE-RESTYLE  sito esistente → stile premium DE (empire-premium-style)
│   │     L4: T-audit-sorgente · T-rebuild-next15 · T-token-design (palette ink/orange/silver) · T-motion (Lenis/GSAP)
│   └─ L3 WF-LANDING-RAPIDA  landing singola < 48h (market-landing + site-premium-stack)
├─ L2 PRODUCT-ENGINEERING (SaaS & App)
│   ├─ L3 WF-SAAS-BUILD      PRD (da FORGE/prd-architect-os) → MVP → iterazioni
│   └─ L3 WF-APP-MAINTAIN    manutenzione App/ e book-factory automation
├─ L2 TOOLING & AUTOMATION (codice interno)
│   ├─ L3 WF-TOOL-BUILD      script/CLI interni (es. pipeline outreach, dashboard) — build-implementation
│   └─ L3 WF-CODE-CUSTODY    repo hygiene, ownership, handover codice ai clienti (€0 canoni = codice loro)
├─ L2 SECURITY & QUALITY
│   ├─ L3 WF-SEC-SCAN        aidefence scan + security-review su ogni deliverable
│   └─ L3 WF-VERIFY          verify.sh Empire + playwright-dev (test browser reali)
└─ L2 DEPLOY & CI/CD
    └─ L3 WF-DEPLOY          vercel:deploy + vercel:logs + rollback + post-deploy smoke
```

## 4. Roster agenti L5

| ID | Ruolo | Tier modello |
|---|---|---|
| `plt-director` | Direttore PLATFORM (era "opus-director" di Crea Siti) — arbitra scope, approva architetture | Opus |
| `plt-cc-master` | Orchestratore esecutivo build (era "cc-master") — coordina i team L4 | Sonnet |
| `plt-site-architect` | Architettura informativa + stack (site-architecture, site-stack) | Sonnet |
| `plt-site-builder` | Implementazione Next.js 15/16 + Tailwind v4 (agente site-build) | Sonnet |
| `plt-site-copy-merger` | Integra il copy di MARKETING nei componenti (agente site-copy) | Haiku |
| `plt-motion-eng` | Animazioni Lenis/Framer/GSAP (site-animate, site-3d) | Sonnet |
| `plt-qa-runner` | QA browser con playwright-dev + verify (agente site-qa) | Haiku |
| `plt-seo-tech` | SEO tecnico on-build (site-seo, schema) | Haiku |
| `plt-sec-sentinel` | Security always-on: aidefence, security-review, has_pii | Sonnet |
| `plt-deploy-op` | Deploy Vercel + logs + rollback | Haiku |
| `plt-custodian` | Code custody: registry repo, handover clienti, .gitignore/licenze | Haiku |

## 5. Asset esistenti → reparto

| Path | Reparto L2 | Azione |
|---|---|---|
| `Digital Empire/Crea siti/` (agents/orchestrators, site-build, site-copy, site-qa; system/SOP-SITE, SOP-OPUS, ARCHITETTURA-SISTEMA-SITE) | WEB-ENGINEERING | **USA** — è già il reparto: formalizzare nomi L3/L4, non riscrivere |
| `Crea siti/skills/site-*` (20+ skill) + `theme-factory`, `frontend-design`, `canvas-design` | WEB-ENGINEERING | **USA** |
| skill `empire-premium-style` / `empire-style` (`SKILL & Agenti/empire-style`) | WEB-ENGINEERING / WF-EMPIRE-RESTYLE | **USA** — motore del restyle premium |
| `Digital Empire/agency-empire-landing/` | WEB-ENGINEERING | **USA** (vetrina viva) + **EVOLVI** (CI verify pre-deploy) |
| `Digital Empire/Crea siti/Siti CCM/` | WEB-ENGINEERING | **USA** come reference design system (ccm-premium) |
| `Digital Empire/SaaS/` | PRODUCT-ENGINEERING | **EVOLVI** — censire, dare owner e pipeline |
| `Digital Empire/App/` | PRODUCT-ENGINEERING | **EVOLVI** — idem |
| `Digital Empire/Outreach/*.py`, `*.bat` (codice, non i run) | TOOLING & AUTOMATION | **WRAPPA** — registry + verify, NON toccare i flussi attivi (rischio #4 Piano Maestro) |
| skill `playwright-dev`, `verify`, `build-implementation`, `review-and-heal` | SECURITY & QUALITY | **USA** |
| skill `vercel:deploy/logs/setup` | DEPLOY & CI/CD | **USA** |

## 6. Skill esistenti + nuove

**Esistenti (si usano così):** site, site-plan, site-brief, site-architecture, site-design, site-components, site-build, site-copy, site-animate, site-3d, site-seo, site-qa, site-deploy, site-report, site-stack, site-premium-stack, empire-premium-style, frontend-design, theme-factory, playwright-dev, verify, vercel:deploy, security-review, github-automation.

**NUOVE da creare (via FORGE):**

| Skill nuova | Scopo | Priorità |
|---|---|---|
| `empire-verify` | verify.sh versione DE: lint+build+playwright+brand gate in un comando | ALTA |
| `code-custody` | checklist handover codice cliente (repo transfer, env, docs, 90gg supporto) | ALTA |
| `site-cost-report` | emette evento costi per OPERATIONS a fine build | MEDIA |
| `stack-radar` | watch trimestrale su stack (Next, Tailwind, Vercel) con proposta upgrade | BASSA |

## 7. KPI + quality gates

| KPI | Target |
|---|---|
| Lead time sito cliente (brief→deploy) | ≤ 10 giorni lavorativi |
| First-pass QA (deliverable passa site-qa al primo giro) | ≥ 80% |
| Lighthouse performance siti consegnati | ≥ 90 |
| Incidenti security post-deploy | 0 |
| Repo censiti nel registry / repo totali | 100% |

**Gates:** G-SEC (aidefence + security-review verde) → G-QA (site-qa + playwright verde) → G-BRAND (stile conforme a empire-premium-style / brand kit cliente) → G-DEPLOY (verify + smoke post-deploy). Nessun deploy salta un gate.

## 8. Fasi di build

| Fase | Cosa | Gate |
|---|---|---|
| P1 | Censimento: registry di tutti i repo/script con owner e stato | inventario 100% |
| P2 | Formalizzare Crea Siti come L2 WEB-ENGINEERING (rinominare ruoli, documentare L3/L4) | un sito demo prodotto col flusso formale |
| P3 | `empire-verify` + pipeline gates su agency-empire-landing | verify verde su landing live |
| P4 | Code custody: procedura handover cliente testata su una commessa reale | handover completato |
| P5 | Agenti reali via Ruflo (plt-cc-master come swarm coordinator) | build sito orchestrata da swarm |

---

# 07 · FORGE — La Fabbrica Organizzativa

## 1. Missione + DONE WHEN

**Missione:** essere HR + R&D organizzativo della holding: creare, valutare, migliorare e ritirare **skill, agenti, team, workflow e interi ecosistemi**. La FORGE è il motivo per cui EMPIRE OS può crescere senza toccare l'architettura (⚠️ premessa del Piano Maestro: "il piano è la micro-base"). I suoi due motori reali sono **content-forge** (materia prima → artefatto, con MKD obbligatorio) e **skill-creator** (creazione/miglioramento/eval di skill).

**DONE WHEN:**
1. Esiste una **pipeline di forgiatura standard**: richiesta → spec (agent-specification) → MKD/PRD → costruzione (content-forge o skill-creator) → eval → consegna all'ecosistema richiedente → registro Identity-HR aggiornato.
2. Ogni nuovo artefatto rispetta lo schema team canonico (pattern #1) e progressive disclosure (#7: kernel ≤500 righe).
3. Il registro Identity-HR (Backbone) elenca il 100% degli agenti con ruolo, costo, performance.
4. La FORGE ha creato almeno: 1 skill nuova con eval ≥ soglia, 1 team L4 completo, 1 reparto L2 per un ecosistema business.

## 2. Posizione nella holding — handoff

| Da → A | Contratto di handoff |
|---|---|
| QUALSIASI ecosistema → FORGE | `{capability mancante, contesto, KPI attesi, budget}` → artefatto consegnato + eval report |
| INTELLIGENCE → FORGE | materiale raw ingerito (Empire Studio) + pattern ReasoningBank → input per forgiare/arricchire skill |
| FORGE → INTELLIGENCE | ogni artefatto creato → pagina wiki `tools/` + log; enrichment skill esistenti passa per Memory Empire |
| FORGE → OPERATIONS | ogni nuovo agente dichiara tier modello + costo stimato → budget guard pre-approvazione |
| FORGE → Backbone Identity-HR | assunzione/ritiro agenti: registro unico aggiornato a ogni forgiatura |
| LX/Board → FORGE | mandato per nuovi ecosistemi interi (es. F9+: E-commerce) |

## 3. Reparti L2 → Workflow L3 → Funzioni L4

```
FORGE
├─ L2 SKILL-WORKS (forgia skill)
│   ├─ L3 WF-SKILL-NEW       richiesta → spec → skill-creator init → draft → eval → package
│   │     L4: T-spec (agent-specification) · T-draft · T-eval-runner · T-description-optimizer
│   ├─ L3 WF-SKILL-IMPROVE   skill esistente + nuova conoscenza → versione migliorata (eval prima/dopo)
│   └─ L3 WF-SKILL-AUDIT     skill-contradiction-analyzer su coppie/set di skill (gate anti-drift)
├─ L2 AGENT-WORKS (forgia agenti e team)
│   ├─ L3 WF-AGENT-NEW       architect-agent → 7-file structure → smoke test → registro HR
│   └─ L3 WF-TEAM-NEW        team L3/L4 canonico: coordinator+workers, I/O, acceptance, escalation
│         L4: T-org-design · T-handoff-contracts · T-shared-state-schema
├─ L2 WORKFLOW-WORKS (forgia workflow e orchestrazioni)
│   ├─ L3 WF-FORGE-PIPELINE  content-forge: raw → MKD → target (doc/agent/team/skill/workflow/orchestration/wiki/custom)
│   └─ L3 WF-PRD             prd-architect-os: PRD tipo A-E con quality score (gate: context score ≥60)
├─ L2 ECOSYSTEM-WORKS (forgia interi ecosistemi — il livello massimo)
│   └─ L3 WF-ECOSYSTEM-NEW   mandato Board → org L2-L5 completa + BACKBONE.md + namespace memoria + dossier
└─ L2 METHOD-GUARD (custode dei pattern)
    └─ L3 WF-SPARC-ENFORCE   sparc-methodology su ogni build non banale; omega-create per progetti Claude Browser
```

**Regola operativa:** la FORGE non inventa da zero quando esiste materia prima — prima chiede a INTELLIGENCE se Empire Studio ha già ingerito materiale sul tema; se sì, content-forge parte da quello (MKD intermedio obbligatorio, mai riassumere: espandere).

## 4. Roster agenti L5

| ID | Ruolo | Tier modello |
|---|---|---|
| `frg-chief` | Chief-Forge (siede in C-Suite L0) — approva forgiature, gestisce coda richieste | Opus |
| `frg-spec-writer` | Specification (SPARC fase 1): requisiti, acceptance, out-of-scope | Sonnet |
| `frg-org-designer` | Disegna org chart team/reparti/ecosistemi (schema canonico CF) | Opus |
| `frg-skill-smith` | Operatore skill-creator: init, draft, package | Sonnet |
| `frg-mkd-forger` | Operatore content-forge: raw → MKD → artefatto target | Sonnet |
| `frg-prd-architect` | Operatore prd-architect-os: PRD tipo A–E con quality score | Sonnet |
| `frg-eval-runner` | Esegue eval skill, benchmark, variance analysis | Haiku |
| `frg-contradiction-gate` | skill-contradiction-analyzer su ogni rilascio (anti-drift) | Sonnet |
| `frg-hr-registrar` | Aggiorna Identity-HR: assume/ritira agenti, traccia costo/performance | Haiku |
| `frg-sparc-warden` | Verifica che ogni build segua SPARC (S→P→A→R→C), blocca salti di fase | Haiku |

## 5. Asset esistenti → reparto

| Path | Reparto L2 | Azione |
|---|---|---|
| skill `skill-creator` (anche in `Crea siti/skills/skill-creator`) | SKILL-WORKS | **USA** — motore reale #1 |
| `SKILL & Agenti/Content-forge/skill - FINALE/` (content-forge, 433 file) | WORKFLOW-WORKS | **USA** — motore reale #2; MKD obbligatorio |
| `Digital Empire/System OMEGA - Creazione proggetti e skill per Claude/` + skill `omega-create` | METHOD-GUARD | **USA** per progetti Claude Browser; **WRAPPA** nel flusso WF-SKILL-NEW come variante target |
| skill `prd-architect-os` | WORKFLOW-WORKS / WF-PRD | **USA** |
| skill `architect-agent` | AGENT-WORKS | **USA** |
| `SKILL & Agenti/Skill Master Architecture/` | SKILL-WORKS | **USA** come reference di metodo (Three-Level Architecture) |
| Agenti SPARC: `agent-specification`, `agent-planner`, `agent-researcher`, `agent-coder`, `agent-tester`, `agent-reviewer`, `agent-architecture` | METHOD-GUARD | **USA** — pipeline SPARC standard |
| skill `sparc-methodology`, `swarm-orchestration` | METHOD-GUARD | **USA** |
| skill `skill-contradiction-analyzer` | SKILL-WORKS / WF-SKILL-AUDIT | **USA** — gate obbligatorio |
| `SKILL & Agenti/agent-factory/` | AGENT-WORKS | **EVOLVI** — valutare merge con WF-AGENT-NEW |

## 6. Skill esistenti + nuove

**Esistenti:** skill-creator, content-forge, omega-create, prd-architect-os, architect-agent, sparc-methodology, swarm-orchestration, skill-contradiction-analyzer, agent-* (7 SPARC).

**NUOVE da creare:**

| Skill nuova | Scopo | Priorità |
|---|---|---|
| `forge-intake` | Form unico di richiesta capability: cattura `{ecosistema, gap, KPI, budget}` e instrada al L3 giusto | ALTA |
| `ecosystem-scaffold` | Genera struttura completa L2-L5 + BACKBONE.md per un ecosistema nuovo (template da questo dossier) | ALTA |
| `team-canonical-template` | Genera team a schema fisso CF (coordinator, workers, I/O, acceptance, escalation, shared_state) | ALTA |
| `agent-retire` | Procedura di ritiro agente: deprecazione, archivio, aggiornamento registro HR | MEDIA |
| `forge-metrics` | Report trimestrale: skill create/migliorate, eval score medi, tempo di forgiatura | BASSA |

## 7. KPI + quality gates

| KPI | Target |
|---|---|
| Tempo richiesta → artefatto consegnato (skill semplice) | ≤ 2 giorni |
| Eval score nuove skill (skill-creator evals) | ≥ 85% pass |
| Artefatti conformi a schema canonico al primo audit | ≥ 90% |
| Copertura registro Identity-HR | 100% agenti |
| PRD quality score (prd-architect-os) | ≥ 75/100 |

**Gates:** G-SPEC (spec approvata prima di costruire) → G-MKD/PRD (documento intermedio completo — content-forge non salta MAI l'MKD; PRD bloccato se context score <60) → G-EVAL (eval ≥ soglia) → G-CONTRADICTION (analyzer verde vs skill esistenti) → G-REGISTRY (HR aggiornato). 

## 8. Fasi di build

| Fase | Cosa | Gate |
|---|---|---|
| F1 | Pipeline WF-SKILL-NEW formalizzata su skill-creator; prima skill nuova = `empire-verify` (per PLATFORM) | skill consegnata con eval verde |
| F2 | WF-FORGE-PIPELINE: content-forge collegato a Empire Studio (input = materiale ingerito) | un MKD→artefatto da materiale reale |
| F3 | Identity-HR: registro agenti popolato (censimento da tutti gli ecosistemi) | 100% censito |
| F4 | WF-TEAM-NEW: forgiare un team L4 reale per un business (es. T-thumbnail per MULTI-BUSINESS/YT) | team operativo |
| F5 | WF-ECOSYSTEM-NEW: dry-run sulla creazione ecosistema E-commerce (F9+ roadmap) | scaffold completo validato |

---

# 08 · INTELLIGENCE — Ricerca, Memoria, Learning

## 1. Missione + DONE WHEN

**Missione:** essere il cervello della holding: la **wiki second-brain-vault è la fonte di verità umana** (pattern #12), AgentDB/ReasoningBank la memoria semantica degli agenti, **Empire Studio** il sistema di ingestione (link/video con frame reali + visione Claude, 9 reparti, 50 agenti), **Memory Empire v3** il router + archivio + enrichment pipeline. INTELLIGENCE fornisce a tutti gli ecosistemi contesto prima di agire e apprendimento dopo aver agito.

**Vincolo cardinale:** Empire Studio e Memory Empire si inglobano **COSÌ COME SONO** — sono attivi e testati. INTELLIGENCE li *organizza* sotto di sé, non li riscrive. Qualsiasi evoluzione passa per la FORGE con eval prima/dopo.

**Confine con l'ecosistema 10 MEMORY (ADR-002):** INTELLIGENCE custodisce la **conoscenza** (esterna ingerita + wiki + pattern appresi); l'ecosistema 10 MEMORY custodisce la **memoria operativa** (checkpoint CP, decisioni ADR, piani, stato, sessioni in `company/Memory/`). Il reparto L2 qui sotto chiamato "MEMORY (= Memory Empire v3)" è il motore di *knowledge routing/enrichment* — NON è l'ecosistema 10. Regola memory-first (#13): ogni team di INTELLIGENCE interroga `company/Memory/` prima di agire e scrive CP dopo, come tutti.

**DONE WHEN:**
1. Ogni ecosistema, prima di un task non banale, ottiene un context pack (`wiki-context` + `memory_search`) e dopo logga l'esito (wiki/log.md + ReasoningBank).
2. Empire Studio risponde come servizio: qualsiasi link/video/repo passato da qualsiasi ecosistema viene ingerito e archiviato integrale in knowledge/ + wiki.
3. Memory Empire instrada il 100% delle richieste DE al workflow giusto (rete di sicurezza) e arricchisce skill esistenti senza romperle.
4. Wiki e AgentDB non divergono: wiki-syncer attivo, log obbligatorio rispettato (mitigazione rischio #6 Piano Maestro).

## 2. Posizione nella holding — handoff

| Da → A | Contratto di handoff |
|---|---|
| QUALSIASI → INTELLIGENCE | `{link/video/file/domanda}` → ingestione integrale o context pack `{pagine wiki, memorie, pattern, fonti}` |
| INTELLIGENCE → FORGE | conoscenza distillata (MKD-ready) per forgiare/arricchire skill; pattern ReasoningBank sui fallimenti |
| INTELLIGENCE → MARKETING/AGENCY | ricerca cliente (customer-research), profili competitor (competitor-profiling), trend |
| INTELLIGENCE → CONTENT-FACTORY/MULTI-BUSINESS | analisi canali riferimento (es. F7: ingestione 2 canali YouTube via Empire Studio) |
| OPERATIONS → INTELLIGENCE | log run, metriche, costi → distillati in pattern e pagine wiki |
| INTELLIGENCE → Backbone BRAIN | è l'ecosistema che OPERA il Brain del backbone (wiki + AgentDB + ReasoningBank) |

## 3. Reparti L2 → Workflow L3 → Funzioni L4

```
INTELLIGENCE
├─ L2 INGESTION (= Empire Studio, così com'è: 9 reparti interni, 50 agenti)
│   ├─ L3 WF-INGEST-VIDEO    video/canale → frame reali + visione → knowledge integrale + wiki
│   ├─ L3 WF-INGEST-WEB      link/sito/repo → estrazione → knowledge + wiki
│   └─ L3 WF-INGEST-DOC      file/cartelle (book-to-skill come variante per libri)
├─ L2 MEMORY (= Memory Empire v3, così com'è: 5 reparti, agenti 7-file con handoff)
│   ├─ L3 WF-ROUTE           router: ogni richiesta DE → workflow giusto, attivazione di sicurezza
│   ├─ L3 WF-ARCHIVE         archivio integrale in knowledge/ + wiki
│   └─ L3 WF-ENRICH          enrichment pipeline: nuova conoscenza → skill/workflow esistenti (safe)
├─ L2 SECOND-BRAIN (wiki ops)
│   ├─ L3 WF-WIKI-CONTEXT    wiki-context loader: context pack pre-task per ogni ecosistema
│   ├─ L3 WF-WIKI-SYNC       wiki ↔ AgentDB bridge (anti-divergenza) + log.md enforcement
│   └─ L3 WF-WIKI-GARDEN     manutenzione: cross-link (≥2-3 per pagina), index.md, pagine orfane
├─ L2 RESEARCH
│   ├─ L3 WF-CUSTOMER        customer-research: ICP, interviste, JTBD
│   ├─ L3 WF-COMPETITOR      competitor-profiling + market-competitors: dossier da URL
│   └─ L3 WF-TREND           radar trend (mercato, AI, piattaforme) → brief mensile alla Board
└─ L2 LEARNING (memoria vettoriale agenti via Ruflo)
    ├─ L3 WF-REASONINGBANK   ogni fallimento loggato → distillato in pattern (pattern #5)
    └─ L3 WF-NEURAL          neural_train + autopilot: i workflow leggono pattern prima di agire
```

## 4. Roster agenti L5

| ID | Ruolo | Tier modello |
|---|---|---|
| `int-director` | Direttore INTELLIGENCE — prioritizza ingestioni e ricerche, risponde alla Board | Opus |
| `int-studio-conductor` | Punto di contatto con Empire Studio (che mantiene i SUOI 50 agenti interni) | Sonnet |
| `int-memory-router` | Punto di contatto con Memory Empire router (WF-ROUTE) | Sonnet |
| `int-librarian` | Wiki gardener: index, cross-link, log, pagine orfane | Haiku |
| `int-sync-keeper` | wiki ↔ AgentDB sync, controllo divergenze | Haiku |
| `int-customer-researcher` | Ricerca clienti/ICP per Agency e Marketing | Sonnet |
| `int-competitor-analyst` | Dossier competitor da URL | Sonnet |
| `int-trend-scout` | Radar trend, brief mensile | Haiku |
| `int-pattern-distiller` | ReasoningBank: da fallimenti a pattern riusabili | Sonnet |
| `int-context-packer` | Compone context pack pre-task (wiki + memoria + pattern) | Haiku |

## 5. Asset esistenti → reparto

| Path | Reparto L2 | Azione |
|---|---|---|
| `second-brain-vault/wiki/` (index.md, log.md, concepts/, entities/, projects/, tools/, sources/, synthesis/) | SECOND-BRAIN | **USA** — fonte di verità, struttura intoccabile |
| `SKILL & Agenti/Empire Studio Suite/empire-studio/` (agents, skills, strategies, runs, memory, evals, packaged) | INGESTION | **USA COSÌ COM'È** — non riscrivere; esporre come servizio |
| `~/.claude/skills/memory-empire/` v3 (agents, departments, knowledge, scripts, routing-map.md) | MEMORY | **USA COSÌ COM'È** — router + archivio + enrichment già attivi |
| skill `wiki-context` | SECOND-BRAIN / WF-WIKI-CONTEXT | **USA** |
| skill `memory-management` | MEMORY | **USA** |
| skill `customer-research`, `competitor-profiling`, `market-competitors` | RESEARCH | **USA** |
| skill `book-to-skill` | INGESTION / WF-INGEST-DOC | **USA** (ponte verso FORGE quando il target è una skill) |
| Ruflo `memory_store/search`, ReasoningBank, AgentDB HNSW, `neural_train` | LEARNING | **USA** — namespace per ecosistema (vedi 07-BACKBONE) |
| `SKILL & Agenti/Orchestracion layer - databese RAG/` | LEARNING | **EVOLVI** — valutare integrazione con AgentDB |
| `~/.claude/projects/...Digital-Empire/memory/MEMORY.md` (auto-memory) | MEMORY | **WRAPPA** — sync periodico verso wiki |

## 6. Skill esistenti + nuove

**Esistenti:** memory-empire, wiki-context, memory-management, customer-research, competitor-profiling, market-competitors, book-to-skill, Empire Studio (SKILL.md propria).

**NUOVE da creare (via FORGE):**

| Skill nuova | Scopo | Priorità |
|---|---|---|
| `context-pack` | Output standard pre-task: 1 comando → `{pagine wiki rilevanti, memorie, pattern, fonti}` per qualsiasi ecosistema | ALTA |
| `wiki-sync-guard` | Check periodico divergenza wiki/AgentDB + report pagine orfane e log mancanti | ALTA |
| `trend-radar` | Brief mensile trend per la Board (formato fisso, fonti tracciate) | MEDIA |
| `ingest-router` | Front-door unica: classifica `{link|video|file|domanda}` e instrada a Empire Studio / Memory Empire / Research | MEDIA |

## 7. KPI + quality gates

| KPI | Target |
|---|---|
| Copertura context pack (task non banali preceduti da contesto) | ≥ 95% |
| Ingestioni Empire Studio completate senza intervento manuale | ≥ 90% |
| Divergenze wiki/AgentDB rilevate al check | 0 aperte > 7gg |
| Pagine wiki nuove con ≥2 cross-link | 100% |
| Pattern ReasoningBank riusati (memory_search hit nei workflow) | trend crescente mese/mese |

**Gates:** G-INTEGRAL (contenuto archiviato INTEGRALE, mai solo riassunto) → G-LOG (ogni operazione in wiki/log.md) → G-LINK (≥2-3 cross-link per pagina nuova) → G-SAFE-ENRICH (enrichment skill: backup + diff + verifica non-regressione prima di toccare skill attive).

## 8. Fasi di build

| Fase | Cosa | Gate |
|---|---|---|
| I1 | Formalizzare la mappa: Empire Studio e Memory Empire dichiarati reparti L2 (zero modifiche al loro interno) | routing-map aggiornata |
| I2 | `context-pack`: ogni ecosistema parte col contesto | usato in un flusso AGENCY reale |
| I3 | `wiki-sync-guard` + WF-WIKI-GARDEN schedulato (via OPERATIONS) | primo report sync pulito |
| I4 | LEARNING attivo: ReasoningBank logga i fallimenti dei primi workflow live (outreach) | primi pattern distillati |
| I5 | WF-TREND + RESEARCH a regime per F7 (ingestione 2 canali YouTube riferimento) | dossier canali completo |

---

# 09 · OPERATIONS — Runtime & Cost Guard

## 1. Missione + DONE WHEN

**Missione:** essere il runtime della holding: eseguire la produzione di massa (swarm), schedulare i flussi ricorrenti (cron/loop), **fare da guardiano dei costi di TUTTA la holding** (budget guard + cost attribution per agente/ecosistema/commessa), gestire storage e asset, monitorare i processi e dare alla Board una dashboard unica. OPERATIONS non decide COSA produrre (lo decidono i business) ma COME gira e QUANTO costa.

**DONE WHEN:**
1. Ogni run (outreach, build siti, ingestioni, content) emette evento standard `{ecosistema, workflow, costo, durata, esito}` raccolto in un ledger unico.
2. Budget guard attivo: nessun workflow può sforare il budget dichiarato — blocco PRIMA dello sforo (pattern #9), dry-run default (pattern #3).
3. Le run outreach giornaliere (avvia-email, avvia-ig, avvia-parallel) girano schedulate e monitorate, non più lanciate a mano.
4. Dashboard unica: stato run, costi per ecosistema, alert sentinels — leggibile in 30 secondi.

## 2. Posizione nella holding — handoff

| Da → A | Contratto di handoff |
|---|---|
| QUALSIASI → OPERATIONS | `{workflow, parametri, budget_max, schedule}` → run eseguita/schedulata + report `{esito, costo, durata}` |
| OPERATIONS → QUALSIASI | alert: budget all'80%, run fallita, drift di costo, processo zombie |
| OPERATIONS → INTELLIGENCE | log e metriche delle run → ReasoningBank + wiki (post-mortem) |
| OPERATIONS → Board (L0) | report costi settimanale per ecosistema + dashboard |
| FORGE → OPERATIONS | nuovo agente/team → registrazione nel cost model (tier, costo stimato/run) |
| OPERATIONS → PLATFORM | richieste tooling (script scheduling, dashboard) — OPERATIONS le usa, PLATFORM le scrive |

## 3. Reparti L2 → Workflow L3 → Funzioni L4

```
OPERATIONS
├─ L2 RUNTIME (esecuzione swarm)
│   ├─ L3 WF-SWARM-RUN       produzione di massa: pattern CF swarm.sh --parallel N --budget N
│   │     L4: T-fanout (sharding lavoro) · T-worker-pool · T-merge-results · T-retry-failed
│   └─ L3 WF-QUEUE           render/job queue (pattern render queue CF): priorità, concorrenza, backpressure
├─ L2 SCHEDULING
│   ├─ L3 WF-CRON            run ricorrenti: outreach giornaliero (avvia-email/ig/parallel), wiki-garden, trend-radar
│   └─ L3 WF-LOOP            loop self-paced su condizione (skill loop / schedule)
├─ L2 COST GUARD (il guardiano della holding intera)
│   ├─ L3 WF-BUDGET          budget per workflow/ecosistema; blocco pre-sforo; approvazione spese (OUT-OF-SCOPE #1: zero spese API senza ok)
│   ├─ L3 WF-ATTRIBUTION     cost attribution per agente/run/commessa → ledger
│   └─ L3 WF-TIER-ROUTING    enforcement 3-tier (WASM/Haiku/Sonnet-Opus): il modello giusto per il task giusto
├─ L2 STORAGE & ASSETS
│   ├─ L3 WF-ASSET-MGMT      asset (immagini, video, export) con naming, dedup, retention
│   └─ L3 WF-BACKUP          backup wiki/knowledge/registry + restore testato
└─ L2 MONITORING & DASHBOARD
    ├─ L3 WF-WATCH           health check processi (run attive, daemon Ruflo, token in scadenza — es. token FB)
    └─ L3 WF-DASHBOARD       dashboard unica Board (estende outreach-dashboard-premium)
```

## 4. Roster agenti L5

| ID | Ruolo | Tier modello |
|---|---|---|
| `ops-director` | Direttore OPERATIONS — SLA run, priorità code, report Board | Opus |
| `ops-swarm-marshal` | Orchestrazione swarm: fan-out, parallel N, merge | Sonnet |
| `ops-scheduler` | Cron/loop: pianifica e lancia run ricorrenti | Haiku |
| `ops-cost-sentinel` | Sentinel always-on: budget guard, blocco pre-sforo, alert 80% | Sonnet |
| `ops-cost-accountant` | Ledger: attribution per agente/run/commessa/ecosistema | Haiku |
| `ops-tier-router` | Enforcement 3-tier routing + Thompson Sampling (via Ruflo) | Haiku |
| `ops-asset-keeper` | Storage, naming, dedup, retention asset | Haiku |
| `ops-backup-op` | Backup + restore test periodico | Haiku |
| `ops-watchdog` | Health check: run, daemon, token, processi zombie | Haiku |
| `ops-dashboard-builder` | Mantiene dashboard (con PLATFORM per il codice) | Sonnet |

Nota tier: OPERATIONS è l'ecosistema più Haiku-heavy della holding — lavoro ripetitivo e schematico, deve costare poco per definizione (predica col proprio esempio).

## 5. Asset esistenti → reparto

| Path | Reparto L2 | Azione |
|---|---|---|
| `Digital Empire/Outreach/` run scripts (`run_parallel.py`, `run_ig_email.py`, `run_all.bat`, `AVVIA-*.bat`) | SCHEDULING | **WRAPPA** — schedulare e monitorare SENZA modificare (workflow attivi: 6 team Nemotron $0/giorno) |
| skill `avvia-email`, `avvia-ig`, `avvia-linkedin`, `avvia-parallel`, `avvia-scraper` | SCHEDULING / WF-CRON | **USA** — trigger ufficiali delle run |
| `Outreach/outreach-dashboard-premium/` + `start-dashboard.bat` | MONITORING / WF-DASHBOARD | **EVOLVI** — da dashboard outreach a dashboard holding |
| Pattern CF `swarm.sh --parallel N --budget N` (repo Content Factory Exponium) | RUNTIME | **PORTA** — riscrivere versione DE (è l'unico "porta da fuori": il pattern, non il file) |
| Pattern CF render queue + cost attribution | RUNTIME / COST GUARD | **PORTA** — idem |
| Ruflo: `task_orchestrate`, `swarm_init`, 3-tier routing, daemon | RUNTIME / COST GUARD | **USA** — con fallback bash auto-riparante (rischio #5: daemon Windows) |
| skill `loop`, `schedule` (cloud agents cron) | SCHEDULING | **USA** |
| skill `hooks-automation`, `workflow-automation`, `update-config` | SCHEDULING / MONITORING | **USA** |
| `Outreach/SISTEMA_OUTREACH_COMPLETO.md` | MONITORING | **USA** come runbook di riferimento |

## 6. Skill esistenti + nuove

**Esistenti:** avvia-email, avvia-ig, avvia-linkedin, avvia-parallel, avvia-scraper, loop, schedule, hooks-automation, workflow-automation.

**NUOVE da creare (via FORGE):**

| Skill nuova | Scopo | Priorità |
|---|---|---|
| `empire-swarm` | swarm.sh versione DE: `--parallel N --budget N --dry-run`, fan-out + merge + retry | ALTA |
| `cost-ledger` | Ledger eventi costo + report settimanale per ecosistema | ALTA |
| `budget-guard` | Dichiarazione budget per workflow + blocco pre-sforo + richiesta ok umano per spese API | ALTA |
| `empire-watchdog` | Health check schedulato: run, daemon Ruflo, token (es. FB scaduto), disco | MEDIA |
| `asset-vault` | Convenzioni storage + dedup + retention per asset multi-ecosistema | MEDIA |

## 7. KPI + quality gates

| KPI | Target |
|---|---|
| Sforamenti budget | 0 (blocco pre-sforo funziona) |
| Run schedulate completate senza intervento | ≥ 95% |
| Costo attribuito / costo totale (copertura ledger) | ≥ 98% |
| Tempo rilevazione run fallita (watchdog) | ≤ 15 min |
| Quota task su tier economico (WASM/Haiku) | ≥ 70% |
| Restore backup testato | 1/mese, verde |

**Gates:** G-DRYRUN (ogni workflow nuovo gira prima in dry-run con stima costi) → G-BUDGET (budget dichiarato e approvato prima della run reale) → G-ATTRIBUTION (run senza evento costo = run non valida) → G-RUNBOOK (ogni workflow schedulato ha runbook e procedura di rollback).

## 8. Fasi di build

| Fase | Cosa | Gate |
|---|---|---|
| O1 | `cost-ledger` + eventi costo dai flussi esistenti (outreach, build siti) | primo report settimanale reale |
| O2 | `budget-guard` su tutti i workflow censiti; dry-run default | un blocco pre-sforo testato |
| O3 | Scheduling outreach: avvia-* sotto WF-CRON + `empire-watchdog` (incl. alert token FB) | 7 giorni di run senza lancio manuale |
| O4 | `empire-swarm` (pattern CF portato): prima produzione di massa reale (es. batch contenuti CONTENT-FACTORY) | batch completato entro budget |
| O5 | Dashboard holding (evoluzione outreach-dashboard-premium) + report Board automatico | dashboard live |

---

# Chiusura — Matrice di dipendenza Core × Business

## Chi serve chi

| Fornisce ↓ / Riceve → | AGENCY | INFO-BUSINESS | CONTENT-FACTORY | MARKETING | MULTI-BUSINESS |
|---|---|---|---|---|---|
| **PLATFORM** | siti clienti, implementazioni, code custody | sales page, piattaforma corsi | tooling pubblicazione | landing/funnel tecnici | SaaS/App, automazioni KDP/YT |
| **FORGE** | team delivery, skill preventivi | team lancio, skill prodotto | team per formato/canale | skill copy/ads nuove | interi rami nuovi (YT, Ecomm) |
| **INTELLIGENCE** | ricerca lead/ICP, dossier competitor | ricerca audience, materiale corsi (Empire Studio) | ingestione fonti, trend contenuti | customer insight, pattern copy vincenti | analisi canali YT riferimento, nicchie KDP |
| **OPERATIONS** | run outreach schedulate, costi per commessa | costi lancio, scheduling email | mass-production swarm, render queue | budget ads guard, attribution | batch produzione libri/video, cron |

## Dipendenze tra i 4 core (ordine interno)

```
INTELLIGENCE ──(contesto, materia prima)──▶ FORGE ──(skill/agenti/team)──▶ PLATFORM
     ▲                                        │                              │
     │                                        ▼                              ▼
     └──(log, pattern, post-mortem)──── OPERATIONS ◀──(eventi costo/run da TUTTI)──┘
```

- **INTELLIGENCE è prima**: già attiva (wiki, Empire Studio, Memory Empire) — si formalizza, non si costruisce.
- **OPERATIONS subito dopo**: il cost guard deve esistere PRIMA di moltiplicare gli agenti (out-of-scope #1: zero spese senza ok).
- **FORGE terza**: forgia ciò che serve, con contesto (da INTELLIGENCE) e budget (da OPERATIONS).
- **PLATFORM in parallelo continuo**: Crea Siti è già operativo; si formalizza mentre serve AGENCY.

## Ordine di costruzione (allineato a roadmap 00-PIANO-MAESTRO)

| Step | Cosa si costruisce | Fase roadmap | Sblocca |
|---|---|---|---|
| 1 | INTELLIGENCE I1-I2 (formalizzazione + context-pack) | F1-F2 | tutti: contesto pre-task |
| 2 | OPERATIONS O1-O2 (ledger + budget guard) | F2 | spawn agenti in sicurezza economica |
| 3 | FORGE F1-F3 (pipeline skill + registro HR) | F2-F3 | creazione capability mancanti |
| 4 | PLATFORM P1-P3 (registry + Crea Siti formale + empire-verify) | F3-F4 | delivery AGENCY (F4) |
| 5 | OPERATIONS O3 (scheduling outreach) | F4 | AGENCY live senza run manuali |
| 6 | FORGE F4 + OPERATIONS O4 (team L4 + empire-swarm) | F5 | CONTENT-FACTORY/MARKETING in produzione di massa |
| 7 | INTELLIGENCE I4-I5 (learning + ricerca canali) | F7-F8 | YouTube Automation + auto-miglioramento |
| 8 | FORGE F5 (ecosystem-scaffold) | F9+ | E-commerce e qualsiasi ecosistema futuro |

**Invariante finale:** i 4 core non generano revenue diretta — il loro KPI ultimo è il KPI degli altri 5. Se AGENCY consegna più in fretta, INFO-BUSINESS lancia meglio, CONTENT-FACTORY produce di più a costo minore, allora PLATFORM, FORGE, INTELLIGENCE e OPERATIONS stanno funzionando.

## Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia, backbone, pattern, roadmap
- [[07-BACKBONE-RUFLO-SKILLS]] — Bus, Brain, namespace memoria, registro skill
- [[08-ROADMAP-FASI]] — fasi F1-F9 dettagliate
- [[Empire_Studio]] · [[Memory_Empire]] — motori INTELLIGENCE (inglobati così come sono)
- [[Tool_ClaudeFlow_Orchestration]] — Ruflo (coordination fabric)
- [[projects/Exponium/Exponium_Content_Factory_Studio]] — origine dei pattern swarm/cost/queue
