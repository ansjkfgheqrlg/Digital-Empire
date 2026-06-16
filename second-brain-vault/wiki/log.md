# Wiki Log

## [2026-06-11] — 🚨 PIANO V2: Direttiva di Scala di Max (ADR-007) + corpus MAXIMILIAN

- DIRETTIVA (Max, analisi completa workspace): la scala v1 è superata — "stiamo costruendo un'AZIENDA". Nuova unità di misura: **1 workflow fatto bene = il Content Factory di Exponium intero**. Board C-Suite: ogni figura (CEO, CFO, CTO, CMO, CRO, COO, Chief-Forge) = workflow CF-grade con ≥10 agenti, principi, regole, script .py, skill proprie (~70 agenti). Ogni reparto = team 6-10 agenti con gerarchia + 1-5 workflow CF-grade; reparti Agency da ampliare; mega-reparti (Info Business, Content Factory) = aziende interne. Mandato → ecosistema di governo (team custodi + multi-workflow, comanda le Sentinelle). Sentinelle multi-workflow. Guilds drasticamente migliorate. Memory promossa ma da potenziare per la scala. Knowledge ingestion: tutte le cartelle formazione del workspace (Formazzione/, Marketing & Ai/, SKILL & Agenti/, InfoBusiness/...) si trasformano in organi interni.
- NUOVO ORGANO **MAXIMILIAN** (LX, sopra il Board): ≥8 agenti che incarnano carattere/standard/decisioni di Max, addestrati sul corpus integrale (`company/Memory/maximilian-corpus/` — prima entry: direttiva di oggi, parole integrali). Nuovo passo 5-bis del metodo: review "Max approverebbe?".
- CODIFICATO: `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md` (incl. roadmap V2-0…V2-8 + obbligo skill-architettura) + ADR-007 + CP-20260611-008. STATO-EMPIRE con banner pivot per Gael (F1-bis in corso vale come base; poi V2-2 dossier v2 → V2-3 organo Maximilian). Zero collisioni: lavorato solo in PIANO-MAESTRO/ e Memory/ (company/ lockata dallo swarm di Gael); nessun secondo swarm (budget account condiviso). → 4 file creati, 4 aggiornati.

## [2026-06-11] — METODO: Ciclo di Fase Empire a 9 passi (ADR-006) + handover Max→Gael

- CREATO: `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` — il metodo "fase→controllo→avanti" arricchito a 9 passi chirurgici (RECALL→SPEC→PRE-MORTEM→BUILD con swarm obbligatorio→GATE deterministico→REVIEW indipendente→TEST funzionale/amnesia→COMMIT→RETRO) + regole trasversali (idempotenza, coordinamento via STATO, budget-guard 20%, una fase per ciclo) + checklist per CP. Origine: direttiva Max + lezioni reali (CP-001 scritture concorrenti, CP-005 swarm morto su session limit).
- CODIFICATO in: ADR-006, CLAUDE.md progetto (REGOLA UNO — Gael la eredita via repo), 08-ROADMAP regole, skill empire-context. Chiarito: Gael ha capacità swarm IDENTICHE a Max (stesso account/skill) — ora obbligo per entrambi.
- HANDOVER: Max si ferma; F1-bis (arricchimento massivo company/, interrotto a metà dal session limit 19:50 con 6 agenti morti) riprende GAEL con istruzioni passo-passo in STATO-EMPIRE. CP-20260611-005.

## [2026-06-11] — BUILD: F1 Scaffolding EMPIRE OS completato (Gael, CP-20260611-001)

- BUILD: `company/` ora navigabile con struttura completa — task 1.1–1.7 di F1 tutti completati.
- CREATO: `company/GRUPPO.md` (organigramma holding, LX→L5, 10 ecosistemi, Backbone, Guilds, Sentinels).
- CREATO: `company/Mandato/MANDATO-EMPIRE.md` (documento costituzionale LX: identità, brand voice, pricing policy, gate APSOC, 13 pattern, governance, checklist brand gate).
- CREATO: `company/Board-CSuite/` — 7 schede agente complete (CEO/COO/CTO/CMO/CRO/CFO/Chief-Forge): identità, responsabilità, I/O JSON, processo decisionale, KPI, escalation. + README Board.
- CREATO: `company/Ecosistemi/` — 10 ecosistemi (01-AGENCY…10-MEMORY): ECOSISTEMA.md + BACKBONE.md + 4 sottocartelle (Reparti/, Workflow/, Funzioni/, Agenti/) per ognuno. Contenuto: missione, reparti L2, workflow principali, asset esistenti, collegamento backbone.
- CREATO: `company/Backbone/` — 6 componenti (Bus, Brain, Governance, Identity-HR, Observability, Coordination) + README master: funzione, struttura, stato build, dipendenze.
- CREATO: `company/Guilds/` — 5 Guild (Prompt, Copy/APSOC, Quality, Cost, Design) con README per ognuna.
- CREATO: `company/Sentinels/` — 5 Sentinel (Cost, Quality, Drift, Security, BrandVoice) con README per ognuno.
- CREATO: `company/Gerarchia/README.md` — schema LX→L5 con albero completo e schema canonico team.
- CREATO: `scripts/gen-empire.py` — generatore/verifier struttura; gate F1: PASS 92/92.
- RISOLTO: staging anomalo all'inizio sessione (~10.639 file staged per deletion) — annullato con `git restore --staged .`, nessun dato perso.
- MEMORY: CP-20260611-001 + STATO-EMPIRE + INDEX aggiornati. → ~70 file/cartelle creati.

## [2026-06-10] — SKILL: `empire-context` creata e installata (project-level, per Max + Gael)

- CREATA: `.claude/skills/empire-context/SKILL.md` — la knowledge base aziendale per agenti/sessioni (equivalente DE di exponium-context, deliverable anticipato del dossier 07 §3.2.1): identità+offerta+prezzi, mappa 10 ecosistemi→dossier, top-5 pattern operativi (memory-first, wiki-first, wrap-non-riscrittura, dry-run, gate), sistema sync ADR-004, sezione "se l'utente è Gael" (guida passo-passo + coordinamento anti-collisione via STATO-EMPIRE), mappa file di verità, storia del progetto.
- INSTALLAZIONE: livello PROGETTO (viaggia col repo) — le skill non si sincronizzano via account Claude; il monorepo è il canale: Gael la riceve attiva col primo pull. Memory: CP-20260610-003. → 1 skill creata.

## [2026-06-10] — INFRA: Monorepo GitHub `digital-empire` + sync automatico Max↔Gael (ADR-004)

- BUILD: repo git nella root di `Digital Empire/` — branch main, commit iniziale **10.634 file / 967 MiB**, destinazione repo privato `ansjkfgheqrlg/digital-empire` (scelta esplicita Max; token in rinnovo via device flow).
- SYNC ENGINE: `scripts/empire-sync.ps1` (pull a inizio sessione, commit+rebase+push dopo ogni blocco, lock, rate-limit 90s, conflitti → `SYNC-CONFLICT.txt` senza mai perdere lavoro) + hook SessionStart/Stop pronti in `scripts/hooks-sync.json` + `SETUP-GAEL.md` (onboarding: clone → zero comandi git per sempre).
- SICUREZZA: `.gitignore` blindato in 4 iterazioni — rimossi dallo staging 3 file di sessione VIVI (instagram/linkedin_session.json), 6.491 file di profili browser (session_data/, maps_session/), 2 GiB di PNG copertine KDP, tutti i .env/DB lead/video/zip. Scan segreti finale: pulito.
- REPO ANNIDATI (decisione Max): 7 inclusi nel monorepo (`.git`→`.git.bak` reversibile: Crea siti, copy-workflow, outreach-dashboard, preventivo-exponium, ccm-premium, app-landing, email-agent, empire-style-skill); `Clienti/EXPONIUM` resta indipendente (repo cliente).
- MEMORY: ADR-004 + CP-20260610-002 + STATO-EMPIRE aggiornato.
- ✅ ESITO FINALE: push iniziale **966.63 MiB completato** su repo privato `ansjkfgheqrlg/Digital-Empire` (eseguito da Max — il classifier auto-mode blocca i push massivi di Claude); motore sync TESTATO end-to-end (commit `sync(Max)` arrivato su GitHub in automatico, 0 conflitti). Pendenze: Max incolla blocco hooks in `.claude/settings.json` (Claude non può editarlo per policy), invito Gael come collaborator.

## [2026-06-10] — COPY: Script cold outreach definitivo (call + email APSOC+V)

- CREATO: `SKILL & Agenti/Copy-Workflow-manuale/script-cold-outreach-digital-empire.md` — script chiamata a freddo completo (apertura trasparenza radicale, Barnum, gestione gatekeeper + 5 obiezioni CPB), email APSOC+V ~300 parole, 3 follow-up (giorno 3/7/12, breakup onesto), varianti A/B e regole d'uso. Vende: Outreach Factory, Content Factory, Second Brain + formazione aziendale in presenza. Basato su [[Framework_Cold_Outreach_APSOC]], contenuto integrale di presentazione-empire.vercel.app (€0 canoni, codice proprietà cliente, setup 7-10gg, 300+ email/gg), skill: copy-workflow, cro-copy-architect, cold-email, marketing-psychology. Audit APSOC 34/40 (manca solo case study nominale). → 1 file creato.

## [2026-06-10] — ✅ COMPLETATO: PIANO MAESTRO EMPIRE OS + ECOSISTEMA MEMORY (operazione master)

- PRODOTTO: `Digital Empire/PIANO-MAESTRO/` — 10 dossier esecutivi (~3.100 righe totali): 00 master (EMPIRE OS, holding 10 ecosistemi, gerarchia LX→L5, 13 pattern), 01 AGENCY, 02 INFO-BUSINESS, 03 CONTENT-FACTORY (434 r., multi-tenant, engine layer — entry mancante per scrittura concorrente, registrato qui), 04 MARKETING, 05 MULTI-BUSINESS (446 r., YouTube 16-step + KDP + Ecomm — idem), 06 CORE (Platform/Forge/Intelligence/Operations), 07 BACKBONE-RUFLO-SKILLS (387 r., Bus/Brain/Governance/HR/Observability/Coordination, 121 skill censite e mappate, 12 skill empire-* da creare, 5 Sentinels + 5 Guilds — idem), 08 ROADMAP (12 fasi con gate), 09 MEMORY.
- METODO: Dynamic Workflow (skeleton → swarm fan-out → integrazione → review) + **swarm di 7 agenti paralleli** (uno per dossier) + conductor. Fase 0 preliminare: studio repo CF Exponium (AION GROUP), wiki DE, presentazione-empire e agency-empire-landing via fetch.
- NUOVO ECOSISTEMA 10 — MEMORY (richiesta Max, urgenza massima): memoria operativa della holding. Pattern #13 memory-first: interrogare `company/Memory/` PRIMA di ogni task, checkpoint DOPO ogni task. **GIÀ COSTRUITO (ME-0/ME-1):** `company/Memory/` con INDEX.md, STATO-EMPIRE.md, CP-20260610-001, ADR-001/002/003, plans/, sessions/, tasks/, state/, audit/, templates/. REGOLA ZERO MEMORY-FIRST aggiunta al CLAUDE.md di Digital Empire.
- REVIEW COERENZA: fix 9→10 ecosistemi in 00/07/08, 12→13 pattern in 01/02/03, topologia + namespace + 4 skill memory in 07, confine INTELLIGENCE↔MEMORY chiarito in 06.
- WIKI: creata [[Piano_Maestro_EMPIRE_OS]] + index aggiornato. → 1 pagina creata, 10 dossier + 12 file Memory prodotti.
- VINCOLO RISPETTATO: canali YouTube riferimento NON analizzati superficialmente — ingestione Empire Studio pianificata come task 7.0/F-MB1 (sessione dedicata).

## [2026-06-10] — PIANO MAESTRO: Dossier Ecosistemi CORE (EMPIRE OS)

- CREATO: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` (~480 righe) — dossier unico dei 4 ecosistemi trasversali L1 #06-09 (coerente con `00-PIANO-MAESTRO.md`): PLATFORM, FORGE, INTELLIGENCE, OPERATIONS. Per ciascuno: missione+DONE WHEN, handoff contract con gli altri ecosistemi, org L2→L3→L4, roster L5 con tier modello (41 agenti totali: 11 PLATFORM, 10 FORGE, 10 INTELLIGENCE, 10 OPERATIONS), mappatura asset path→reparto→azione (usa/wrappa/evolvi/porta), skill esistenti + 18 nuove da forgiare (P0: empire-verify, forge-intake, ecosystem-scaffold, team-canonical-template, context-pack, wiki-sync-guard, empire-swarm, cost-ledger, budget-guard), KPI+quality gates, fasi di build con gate.
- DECISIONI ARCHITETTONICHE: (1) FORGE usa content-forge + skill-creator come motori reali (MKD intermedio obbligatorio, eval gate); (2) Empire Studio e Memory Empire inglobati COSÌ COME SONO come reparti L2 INGESTION e MEMORY di INTELLIGENCE — zero riscritture; (3) OPERATIONS è il guardiano dei costi dell'intera holding (ledger + budget guard pre-sforo + 3-tier routing); (4) Crea Siti diventa il reparto L2 WEB-ENGINEERING di PLATFORM senza riscrittura; (5) pattern CF da portare: swarm.sh --parallel/--budget, render queue, cost attribution.
- CHIUSURA: matrice di dipendenza Core×Business + ordine di costruzione (INTELLIGENCE→OPERATIONS→FORGE→PLATFORM, allineato a F1-F9). → 1 pagina creata.

## [2026-06-10] — PIANO MAESTRO: Dossier Ecosistema MARKETING (EMPIRE OS)

- CREATO: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` (387 righe) — dossier L1 #04 di EMPIRE OS (coerente con `00-PIANO-MAESTRO.md`). 4 reparti L2 (Copywriting PRIORITÀ ASSOLUTA, Advertising, Email Marketing, Analytics & Ottimizzazione) con org L3/L4; roster L5: 13 agenti esistenti del Copy Workflow inglobati senza duplicazione (copy-master + A1-A8 + S1-S3) + 13 nuovi (AD1-4, E1-3, AN1-4, MKT-Conductor, Brand-Voice Sentinel); contratto richiesta copy `{committente, formato, awareness_level, icp, obiettivo, deadline}` con routing per formato; 4 workflow chiave (richiesta cross-ecosistema, campagna ads end-to-end, email lancio/nurture/post-cancel, loop ottimizzazione data-driven → reasoningbank); mappatura completa skill→reparto (cro-copy-architect, market-* ×15, emails, ads, ab-testing, analytics... zero orfane); 7 skill nuove (P0: empire-brand-gate, copy-request-router); namespace Ruflo `marketing/copy/patterns/{icp}`; gates G1-G4 (score A8 ≥80 / ≥85 sales page + brand gate Mandato Empire bloccante); fasi build M1-M6 dentro F5. → 1 pagina creata.
- DECISIONE ARCHITETTONICA: il Copy Workflow Orchestration Layer NON si riscrive — si ingloba come motore del reparto Copywriting via wrapper di handoff. Riferimenti: [[Tool_Copy_Workflow_Orchestration]], [[Framework_Cold_Outreach_APSOC]].

## [2026-06-10] — PIANO MAESTRO: Dossier Ecosistema INFO-BUSINESS (EMPIRE OS)

- CREATO: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md` — dossier L1 #02 di EMPIRE OS (coerente con `00-PIANO-MAESTRO.md`). 4 reparti L2 (Prodotto, Lanci, Vendite/Funnel, Community&Retention), roster 26 agenti L5 (5 agenti formazione-* esistenti arruolati as-is + 21 da creare via FORGE), 3 workflow end-to-end (WF-CORSO: raw→content-forge MKD→curriculum→piattaforma Supabase; WF-LANCIO: T-30→T+7 con dry-run e go/no-go hive-mind; WF-FUNNEL-EVERGREEN), mappatura completa asset (Formazzione/, Lancio corso skill beast/, Lanco ebook/, InfoBusiness/), 15 skill esistenti assegnate + 7 nuove da forgiare (course-architect, launch-runbook, offer-stack, webinar-funnel, student-success, launch-debrief, crosssell-bridge), 6 namespace Ruflo `infobusiness/*`, 7 quality gate (copy APSOC ≥80/100, validazione idea ≥60/100), fasi build B0→B6 (B4 = gate F6 del Piano Maestro), 9 rischi con mitigazioni. → 1 pagina creata.
- GAP RILEVATI nel catalogo prodotti: Manuale Claude Code con prezzo "NON LO SO" e doppio ruolo lead-magnet-gratuito/prodotto-a-pagamento → risoluzione resa bloccante in fase B1 del dossier.

## [2026-06-10] — PIANO MAESTRO: Dossier Ecosistema AGENCY (EMPIRE OS)

- CREATO: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` — dossier completo dell'ecosistema L1 #01 di EMPIRE OS (coerente con `00-PIANO-MAESTRO.md`). 6 reparti L2 (Ricerca, Acquisizione/Outreach, Preventivi, Delivery, Copywriting-interno, Marketing-interno), 20 team L3/L4, roster ~37 agenti L5 con tier modello, 16 handoff contract verso gli altri 8 ecosistemi, pipeline revenue end-to-end (lead→outreach→call→preventivo→contratto→delivery 7gg→supporto 90gg→testimonianza/upsell), mappatura asset esistenti (wrap mai riscrittura — pipeline outreach attiva intoccabile), 9 skill nuove da forgiare, topologie swarm Ruflo + 8 namespace `agency/*`, 3 quality gate (Bibbia esistente, Preventivo, Delivery), 8 fasi build B0→B7 (B6 = gate F4 del Piano Maestro), 11 rischi con mitigazioni. → 1 pagina creata.

## [2026-06-09] — INGEST: Claude Design È PAZZESCO (Giovanni Beggiato, Avanguardia+)

- INGEST COMPLETO (Empire Studio): Video YouTube B4i1qV0LiMw — "Claude Design È PAZZESCO: Ti Insegno A Usarlo Bene" — 707 frame estratti a 2s, visione nativa su tutti i frame, video-analysis.md completato.
- CONTENUTO: Metodo in 4 passi — (1) Design System in claude.ai/design, (2) Template library, (3) Skills Claude Code via skill-creator, (4) Lead Magnet automatizzato. Anti-pattern "vibe design": 490.849 token → 0 risultati; con sistema → 90%. Dimostrazione live: featuresheet:cheat-skill (PNG+PDF 1080×1350 branded con self-check), The Thought Leader Funnel (5 stadi), The Founder Authority Stack (7 layers), Social Media Manager 25+ skills (lista completa estratta).
- KNOWLEDGE ARCHIVE: 16 atomi archiviati in `~/.claude/skills/memory-empire/knowledge/B4i1qV0LiMw/` (ingest-manifest.json + atoms.json + contenuto-integrale.md + enrichment-report.md).
- ENRICHMENT: 4 skill con modifiche proposte: `lead-magnets` (keyword-matching rule + workflow integrato + scarcity XX/100), `image` (featuresheet workflow + self-check step), `skill-creator` (self-check best practice), `social` (Thought Leader Funnel + Founder Authority Stack). 4 nuovi asset DE identificati: social-media-manager-de, featuresheet:cheat-skill, DE Design System, LinkedIn Authority Playbook.
- WIKI: aggiunto entry in index.md → Modelli AI — Aggiornamenti.

## [2026-06-08] — STUDIO REPO: Exponium Content Factory (AION GROUP)

- STUDIO APPROFONDITO: letta repo `Lavoro/Exponium/second-brain-exponium/Ecosistema - Content Factory` nei minimi dettagli — CLAUDE.md, ECOSISTEMA.MD, GUIDA.md, PLAN-01-ARCHITECTURE.md, PLAN-05-ENTERPRISE.md, BUILD-STATUS.md, skill exponium-context, struttura company/ completa.
- ANALISI: holding AI enterprise (AION GROUP) a 6 livelli (L0-L5 + Guilds + Sentinels), 6 ecosistemi (STUDIO/INTELLIGENCE/GROWTH/PLATFORM/FORGE/OPERATIONS), Corporate Backbone (BUS/BRAIN/GOVERNANCE/IDENTITY/OBSERVABILITY/COORDINATION), 8 reparti, ~24 team, pipeline UGC reale testata (video mp4 2MB, 12 crediti, 2026-05-29), 68 quality check via verify.sh, dry run mode, ReasoningBank.
- WIKI: creata pagina [[projects/Exponium/Exponium_Content_Factory_Studio]] con analisi completa + confronto DE + 10 pattern architettonici chiave da replicare. Aggiunto in index.md come riferimento architettonico master.
- CONTESTO: lo studio serve per costruire la versione Digital Empire — molto più grande (multi-scopo: agency + info products + SaaS) con 3 ecosistemi aggiuntivi rispetto a CF (CLIENT DELIVERY, SALES, PRODUCT).

## [2026-06-08] — RE-INGEST DENSO + ENRICHMENT: Video Opus 4.8

- RE-INGEST COMPLETO (Empire Studio, fix pipeline): Video YouTube "Claude Opus 4.8 è una Follia: 7 Casi d'Uso Reali (+ Prompt)" — **466 frame estratti a 2 secondi** (da 17 frame sparsi a visione densa reale). video-analysis.md riscritto da zero con timeline completa, 5 lezioni complete, 7 prompt live esatti, Pro/Contro lista completa da slides.
- KNOWLEDGE ARCHIVE: contenuto archiviato integralmente in `~/.claude/skills/memory-empire/knowledge/uU3M_NJ70XE/` (contenuto-integrale.md + atoms.json 16 atomi + ingest-manifest.json + enrichment-report.md).
- ENRICHMENT: 3 skill arricchite con pattern estratti dal video:
  1. `pair-programming` → tabella effort level calibration + plan-before-act + human-in-the-loop stop points
  2. `copywriting` → Voice Matching with Style Sample (pattern style-sample Opus 4.8)
  3. `workflow-automation` → Outline-First Pattern per deliverable strutturati
- SYSTEM FIX: hook UserPromptSubmit aggiornato per attivazione meccanica Empire Studio + Memory Empire. Memory Empire ridisegnato con architettura 5-reparti 25+ agenti con handoff protocol JSON. frame_extractor.py aggiornato con --interval N per estrazione densa.


## [2026-06-04] — PIVOT: Outreach da "Landing Page" a "Implementazioni AI" (3 prodotti)

- DECISIONE STRATEGICA: l'outreach (Email + LinkedIn + Instagram) smette di vendere landing page/CRO e vende 3 IMPLEMENTAZIONI AI: **Outreach Factory**, **Content Factory**, **Second Brain** (workflow sui server del cliente, codice incluso, €0 canoni, setup 7gg). Leva = operatività, non conversioni. Obiezione = solo fiducia (demo live + presentazione).
- TARGET cambiato: Agency + Info Business + Marketing pros (SMM/copy/ads) + ecommerce. Eliminati i professionisti locali da scraper SETTORI, hashtag IG, ricerche LinkedIn, keyword bio (incl. `Instagram Automation/agents/profile_qualifier.py`).
- FRAMEWORK APSOC ricalibrato (A=hype → P=1 problema operativo → S=workflow 100% → O=solo fiducia → C=guarda presentazione + prenota call, con sconto). Match prodotto↔target nel qualifier (`prodotto_guida`; template A=Outreach, B=Content, C=Second Brain).
- LINK NEL PRIMO MESSAGGIO su tutti i canali: `presentazione-empire.vercel.app` nel CTA + `agency-empire-kohl.vercel.app` in firma. Rimosso l'HARD-BLOCK anti-link in `bibbia_team.py` e la regola "link=FAIL" nella Bibbia. VOLUME email aggiornato a fino a 1000/giorno con CAP 100/ora (drip throttle in `sender.py`, env `EMAIL_DAILY_LIMIT`/`EMAIL_HOURLY_LIMIT`/`EMAIL_DELAY_SECONDS`); Gmail personale ~500/gg, per 1000 serve Workspace o più mailbox. CONFIG OPERATIVA scelta dall'utente: email 500/gg (cap 100/h), Instagram 30 DM/gg, LinkedIn 20 connect + 20 msg + 30 commenti/gg. I limiti DM restano bassi per rischio ban (NON scalabili come l'email).
- FILE: knowledge/{apsoc,brand_voice,copy_training}.py + bibbia_outreach.md; agents/{scraper,qualifier,strategist,copy_knowledge,writer,bibbia_team,humanizer,followup_writer,conversation_manager}.py; LinkedIn+Instagram {config,personalize}.py; profile_qualifier.py; .env.example. Eseguiti via team di agenti paralleli (Wave 1-3). `py_compile` OK su tutti.
- WIKI: creata [[Concept_Pivot_Implementazioni_AI]]. NB residuo (non bloccante): agenti DEEP-INTEL dormienti (cro_audit/competitor/insight) e `SISTEMA_OUTREACH_COMPLETO.md` da aggiornare in una sessione futura.

## [2026-06-03] — INSTALL: skill `agency-scalping` v2.0.0 + push repo dedicato

- INSTALL UFFICIALE: estratta la cartella `agency-scalping/` (129 file) dal workspace zip `SKILL & Agenti/Skill scalping agency/workspace-019e8de1-...zip` → `C:\Users\Utente\.claude\skills\agency-scalping\`. Skill ora attiva globalmente (`/agency-scalp` o trigger naturale "voglio aprire un'agenzia / SMMA / scalare l'agenzia").
- ESCLUSI dall'install i vendor di build presenti nello zip (ruflo 62MB, content-forge2.0, product-manager-skills, uploads) — non fanno parte della skill.
- GITHUB: creato repo **privato dedicato** `ansjkfgheqrlg/agency-scalping` (branch `main`, 129 file, SKILL.md incluso). **Solo questo account** per richiesta esplicita di Max — NON sui due repo abituali. La cartella skill installata è anche il repo locale (`origin` → agency-scalping.git) per update futuri.
- WIKI: creata pagina [[Tool_Agency_Scalping_Skill]].

## [2026-06-01] — DOC: AION GROUP — creata `GUIDA.md` (spiegazione semplice)

- Creato `GUIDA.md` alla radice di Content Factory: spiega in parole semplici cosa fa l'ecosistema, cosa può fare, come funziona (flusso + struttura holding 6 ecosistemi), come si usa (comandi), e una roadmap di 14 cose da aggiungere/implementare (priorità alta/media/evoluzione). Push su 2 GitHub (11f180f).

## [2026-06-01] — QUALITÀ: AION GROUP — arricchimento massivo (7 agenti coordinati)

- Problema: ecosistemi non finiti (cartelle vuote: Agenti/Funzioni) + ~44 file .md "magri" (template generici ~16 righe) — sistemico.
- Operazione: 7 agenti-team REALI in background (Agent tool, sonnet), cartelle disgiunte → 6 ecosistemi + 1 cross-cutting. ~127 file da magri a completi (agenti 140-170 righe: identità, responsabilità, input/output, strumenti, "come ragiona", interazioni, KPI, escalation, esempi).
- Gap-closer fallito (errore server 529) → ultime 15 lacune chiuse a mano (STUDIO Agenti/Funzioni, 2 Sentinel, 3 Gerarchia, 6 Backbone, 2 indici).
- Risultato: **0 cartelle vuote, 0 file magri**, 165 .md / **17.247 righe**. `verify.sh` **68 PASS**. Memory CP-024. Push 2 GitHub.
- NB: i markdown curati sono la fonte di verità → NON rigenerare con gen-company/gen-group.

## [2026-05-31] — ✅ COMPLETATO: AION GROUP (BUILD-14→16) — holding enterprise operativa

- BUILD-14: 10 agenti REALI via claude-flow agent_spawn (Conductor + 6 coordinatori ecosistema + 3 Sentinel) nello swarm; roster in AgentDB + Identity-HR; fabric.sh.
- BUILD-15: auto-miglioramento di gruppo `evolve.sh` (osserva→giudica→distilla in Brain→FORGE hire/retire→predice).
- BUILD-16: `group-conductor.sh` (orchestrazione CROSS-ECOSISTEMA via gbus + governance) + `dashboard.sh` (vista gruppo).
- **AION GROUP completo:** L0 C-Suite + 6 ecosistemi (29 team/47 agenti/11 wf) + Backbone (bus/brain/governance/identity/fabric) + 10 agenti reali + auto-miglioramento + dashboard. Gate **68 PASS**. CP-021/022/023. Su 2 GitHub.
- Nota: MCP claude-flow disconnessa nelle ultime fasi → realizzate in bash + CLI ruflo + fallback (ibrido ADR-005). Loop dinamico CHIUSO.

## [2026-05-30] — BUILD: AION GROUP 11→13 (scaffolding + migrazione + Backbone) [Dynamic Workflow]

- BUILD-11: scaffolding holding (GRUPPO.md, Board-CSuite 7+Council, 6 Ecosistemi, Backbone 6, Guilds 5, Sentinels 5) via gen-group.py.
- BUILD-12: migrazione org dentro gli ecosistemi (19 mv per mappatura) — 29 team/11 wf/47 agenti in Ecosistemi/<ECO>/. Generatori resi ecosystem-aware (rigenerabile).
- BUILD-13: Corporate Backbone operativo — gbus.sh (bus inter-ecosistema), brain.sh (AgentDB+mirror), governance.sh (gate gruppo). verify.sh **61 PASS**.
- Calibrazione utente: struttura prima, agenti reali da BUILD-14. Memory CP-018/019/020. Push su 2 GitHub a ogni fase.

## [2026-05-30] — PLAN: AION GROUP — architettura enterprise di nuova generazione (PLAN-05)

- MCP di Ruflo (claude-flow v3.10.16) ATTIVA → usata dal vivo per pianificare: swarm_init, hive-mind_init (raft), memory_store (AgentDB HNSW), guidance_recommend.
- `PLAN-05-ENTERPRISE.md`: AION GROUP = holding di 6 ecosistemi indipendenti ma connessi (STUDIO/INTELLIGENCE/GROWTH/PLATFORM/FORGE/OPERATIONS) + Corporate Backbone (Bus/Brain-AgentDB/Governance/Identity-HR/Observability/Coordination) + C-Suite L0 + Guilds + Sentinels. Agenti reali via MCP. Auto-miglioramento continuo (reasoningbank+neural+autopilot+Forge).
- Gerarchia estesa L0→L5 + cross-cutting. Roadmap Dynamic Workflow BUILD-11→16. ADR-007 + CP-017. Push 2 GitHub.

## [2026-05-30] — INFRA: Ruflo `init` in Content Factory + agency-empire

- INIT: `ruflo init` (config default, senza `--force` → no overwrite) eseguito in 2 cartelle: `SKILL & Agenti/Ecosistema - Content Factory/` (106 file) e `agency-empire/` (105 file).
- Creato per cartella: `CLAUDE.md` (guida swarm), `.mcp.json` (server MCP ruflo), `.claude/` con 30 skill + 16 comandi + 17 agenti + 7 hook (override cross-platform Windows auto-rilevati), runtime `.claude-flow/`. `ruflo init check` → `[OK] initialized` in entrambe.
- CHIARITO: l'**init è per-cartella** (non esiste "init globale"). L'install è globale (comando ovunque), l'init no → va ripetuto in ogni progetto dove serve ruflo. Per i background worker: `ruflo daemon start` + `ruflo memory init`.
- ⚠️ EFFETTO GLOBALE: l'init ha aggiunto un blocco "Ruflo Integration (auto-generated)" in cima a `~/.claude/CLAUDE.md` → nudge verso i tool MCP ruflo in **tutti** i progetti della macchina. Rimovibile a mano o con `ruflo init --no-global` in futuro.

## [2026-05-30] — INFRA: Ruflo installato in GLOBALE (npm -g)

- INSTALL: `npm install -g ruflo` → `ruflo@3.10.13` su macchina Max. Comando `ruflo` ora su PATH (`C:\Users\Utente\AppData\Roaming\npm\ruflo.ps1`), disponibile da qualsiasi cartella/progetto.
- CHIARIMENTO: la copia in `orchestration/vendor/ruflo/` (v3.10.10, ~6800 file) era **vendoring per archivio**, non installazione → nessun comando, agenti non caricati (sottocartella annidata fuori dagli scope `.claude/` letti da Claude Code). Per questo non era usabile in altri progetti.
- AGGIORNATO: `tools/Tool_ClaudeFlow_Orchestration.md` (sezione "Stato installazione locale") + index.md. Prossimo step per usarlo in un progetto: `ruflo init` lì dentro.

## [2026-05-30] — ORG: AION Studio — Azienda NAVIGABILE nell'Explorer

- Riorganizzata `company/` come azienda vera esplorabile: `Organigramma.md`, `Gerarchia/`, `Reparti/Dx-<nome>/Tx.y-<nome>/{README, team.yaml, agenti/}`, `Workflow/{Engine,Produzione}/WF-*/`, `Personaggi/`, `org/`.
- Ogni team ha README con sezione "🧠 Come si ATTIVA e RAGIONA" (trigger→decomposizione→esecuzione→handoff→failure). Ogni agente = un file.
- `scripts/gen-company.py` genera l'albero; gen-teams/gen-workflows scrivono nell'albero. verify.sh + CI aggiornati. **55 PASS**. 8 reparti·29 team·47 agenti·11 workflow. Memory CP-016. Push su 2 GitHub.

## [2026-05-30] — BUILD-10: AION Studio — Vendor=Workflow L2 + Produzione di Massa (Swarm)

- CORREZIONE ARCHITETTURALE (ADR-006): ogni asset vendor È un workflow L2 operato da un team dedicato. Ruflo = motore di produzione di massa (108 agenti/swarm), non reference passiva.
- CREATI 11 team-workflow L2 (`company/workflows/`): 8 engine (WF-RUFLO/MARKETING/COPY/FORGE/PM/TOOLING/COHERENCE/CONTEXT) + 3 produzione (WF-UGC/PRODUCT/LAUNCH). `hierarchy.yaml` aggiornato.
- `orchestrator/swarm.sh`: produzione di massa (mesh/queen) — N video in parallelo da batch, budget guard. Fix id concorrenza (PID+random).
- TEST: 5 produzioni parallele dry → 5 ok, budget guard blocca 60>40. `verify.sh` **53 PASS**. Memory CP-015.
- PUSH su ENTRAMBI i GitHub (ansjkfgheqrlg + fragolina97), snapshot completo (vendor incluso, 6973+ file, segreti esclusi).

## [2026-05-30] — BUILD-9: AION Studio — Skill native ibride [Dynamic Workflow iter.4]

- Modello ibrido (ADR-005) come contratto agente↔skill: `company/skills-map.yaml` (team→skill native reali) + `orchestrator/skill-bridge.sh` (request/pending/fulfill). `agents.sh` emette le richieste-skill.
- Il bash non può chiamare le skill Claude → gli step di conoscenza (brief/copy/research) li esegue l'AGENTE via skill native; template statico = fallback.
- TEST: ciclo bridge + copy APSOC reale prodotta dall'agente → fulfill → copy.md sostituita. `verify.sh` **51 PASS**. Memory CP-013.
- PROSSIMO (loop): BUILD-8 GitHub (ultima fase).

## [2026-05-30] — BUILD-7: AION Studio — Produzione avanzata (editing reale) [Dynamic Workflow iter.3]

- `editing.sh` (T2.4): montaggio reale ffmpeg → normalizza a 9:16 (1080x1920), concat multi-clip, caption opzionale. TEST: 2 clip → master 9:16 + caption → QA PASS.
- `dispatch.sh`: riuso keyframe in T2.3 (`video -i <id>`, niente doppia generazione = risparmio crediti) + montaggio reale T2.4. t2v/product via hf-studio.sh.
- LINT 24 bash, `verify.sh` **50 PASS**. Memory CP-012. PROSSIMO (loop): BUILD-9 skill native ibride.

## [2026-05-30] — BUILD-6: AION Studio — Self-Improvement (D6) [Dynamic Workflow loop iter.2]

- `improve.sh` (D6): failure-detector → triage → phase-planner. Legge metrics/escalation, genera note di miglioramento + proposta diff SOP. Loop chiuso: `dispatch.sh` qa-failed → `improve.sh scan` automatico.
- TEST: fallimento render iniettato → nota con azione corretta ("D3: retry+fallback"). `verify.sh` **49 PASS**. Memory CP-011.
- PROSSIMO (loop): BUILD-7 produzione avanzata (editing ffmpeg, riuso keyframe, t2v/product).

## [2026-05-30] — BUILD-5: AION Studio — Qualità (D5) + Codice (D8) [Dynamic Workflow loop]

- Attivata modalità **Dynamic Workflow** (loop self-paced) per costruire BUILD-5→8 in autonomia.
- D5 `qa.sh`: gate qualità reale via **ffprobe** (aspect 9:16, durata, orientamento) → blocca output non conforme. Integrato in `dispatch.sh` (review solo se QA pass, altrimenti qa-failed + escalation D6).
- D8 `code.sh`: lint bash+python, dedup, inventory. ffmpeg 8.1.1 wired in PATH (lib-orch autodetect).
- TEST (0 crediti): clip 16:9 → BLOCCATO; 9:16 → PASS. `verify.sh` **48 PASS / 0 FAIL**. Memory CP-010.
- PROSSIMO (loop): BUILD-6 Self-Improvement.

## [2026-05-30] — BUILD: AION Studio Content Factory — FASE PORT completa (gira su Windows)

- FIX PORTABILITÀ: aggiunto `pypath()` (cygpath) in lib-orch + fixate tutte le chiamate Python (sys.argv + utf-8) in verify/state/conductor/dispatch/agents → risolti i 4 falsi-FAIL
- `verify.sh` ora 43 PASS / 0 FAIL su Windows; smoke test `dispatch ugc --dry` end-to-end OK
- HIGGSFIELD CLI: install npm fallisce (GNU tar + path C:\) → scaricato binario + estratto con System32 bsdtar + shim `higgsfield.exe`. bootstrap.sh reso Windows-aware (auto-riparante)
- LOGIN OK: account monicaesposito1797@gmail.com — 83 crediti
- config.sh `HF_ROOT` portabile. Memory CP-008 + MEMORY-INDEX aggiornati.
- FASE GAP (CP-009): generati 29 team YAML (`scripts/gen-teams.py` da roster.yaml) + `sop/SOP-ugc-video.md` + `company/characters/_schema.md`. verify.sh esteso → **46 PASS / 0 FAIL**. ffmpeg 8.1.1 installato.
- FINE SESSIONE (riprende domani). ▶️ RIPRESA DA: **BUILD-5** (D5 Output QA `qa.sh`+ffprobe+contradiction-analyzer gate, D8 Code `code.sh` lint). Dettaglio in `orchestration/PLAN-04-EXECUTION.md` §5 e `memory/sessions/session-20260530.md`.

## [2026-05-29] — INGEST: AION Studio Content Factory — ecosistema agenti studiato + piano continuazione

- ESTRATTO: `workspace-...zip` → ecosistema completo in `SKILL & Agenti/Ecosistema - Content Factory/`
- STUDIATO: Cronologia chat completa (2311 righe), memoria AION (CP-001→005, ADR-001→004), piani PLAN-00/01/02, tutti gli script orchestrator + hf-studio + vendor (7 asset)
- SCOPERTO: migrazione sandbox Linux → Windows; motore Higgsfield scollegato (no CLI/creds/ffmpeg)
- CREATO: `projects/AION_Studio_Content_Factory.md` — pagina progetto wiki
- CREATO (in orchestration/): `PLAN-03-CONTINUATION.md`, memory `CP-006`, `ADR-005` (portabilità Windows + modello ibrido bash+skill native)
- INSTALLAZIONI UFFICIALI (richiesta utente): ri-clonati 8 asset vendor (ruflo, marketingskills, content-forge2.0, copy-workflow, product-manager-skills, skill-contradiction-analyzer + cli-printing-press + context-engineering-commands ora esistente). context-engineering-advisor già in skills-lock.
- FIX PORT: rimosso `.npmrc` prefix Linux, abilitato git core.longpaths. Trovato bug path MSYS→Windows Python (fix: cygpath) → 4 falsi-FAIL in verify.sh.
- CREATO: `PLAN-04-EXECUTION.md` (piano dettagliato SPARC+swarm, task-by-task) + memory `CP-007`. Usata skill nativa `sparc-methodology`.
- PROSSIMO: FASE PORT P1 (fix cygpath negli script) → verify 0 FAIL → install higgsfield CLI+ffmpeg → login

## [2026-05-29] — UPDATE: agency-empire-landing — 7 modifiche UI completate

- Mod 1 hero.tsx: H1 riscritto "Da lavoro manuale / a macchina che produce." + subtitle migliorato con pain point e numeri specifici
- Mod 2 audience.tsx: Fix wrap "Business Owner." — white-space nowrap
- Mod 3 audience.tsx: Card YES/NO riempite con colori solidi (crimson-orange vs dark steel-blue) + silver border 2px
- Mod 4 hierarchy.tsx: Eyebrow label ridesignato con pill + dot indicator + step badge premium (orange per Target Empire)
- Mod 5 roadmap.tsx: Annotation colors scuriti per visibilità su bg-paper (#c41818, #b84400, #1a7a38, #1a44b0) + opacity 1
- Mod 6 no-fluff.tsx: Fix wrap "Vendiamo asset." — white-space nowrap
- Mod 7 pricing-roi.tsx: Sezione completamente ridisegnata con 3 card servizi individuali (Outreach €4k, Second Brain €2.5k, Content Factory €3.5k) + Engine Room combo (€8k/€10k) + ROI box

## [2026-05-29] — UPDATE: Tool_ClaudeFlow_Orchestration.md — analisi completa da zip ruflo-main

- ANALIZZATO: `ruflo-main.zip` — Ruflo v3.7.0-alpha.8 (ex claude-flow) by ruvnet
- AGGIORNATA: pagina wiki con dati reali: 314 MCP tools, 100+ agenti, 33 plugin, 27 hooks+12 workers
- DOCUMENTATI: 3-tier model routing, Thompson Sampling, HNSW 150x-12,500x speedup, Agent Federation, SONA learning
- AGGIORNATO: numeri ecosistema reali — 22M+ download, 115k clone/14gg, 6,000+ commit

## [2026-05-29] — INGEST: Claude-Flow V3 (Ruflo) — 15 skill installate + 4 pagine wiki + Exponium aggiornato

- ANALIZZATO: `ruflo-main.zip` — Claude-Flow V3 by ruvnet (138 skill, framework multi-agent)
- INSTALLATO: 15 skill adattate in `~/.claude/skills/`:
  - `sparc-methodology`, `swarm-orchestration`, `memory-management`
  - `verification-quality`, `github-automation`, `pair-programming`, `workflow-automation`, `hooks-automation`
  - `agent-specification`, `agent-architecture`, `agent-researcher`, `agent-planner`
  - `agent-reviewer`, `agent-tester`, `agent-coder`
- CREATO: `tools/Tool_ClaudeFlow_Orchestration.md` — panoramica completa framework
- CREATO: `concepts/SPARC_Methodology.md` — workflow 5 fasi per sviluppo strutturato
- CREATO: `concepts/AgentDB_Memory_System.md` — architettura memoria vettoriale HNSW (Cap.9 Exponium)
- CREATO: `concepts/Swarm_Orchestration_Pattern.md` — multi-agent topology (Cap.6+ Exponium)
- CREATO: `synthesis/ClaudeFlow_Exponium_Applications.md` — mapping completo applicazioni
- AGGIORNATO: `Clienti/EXPONIUM/CLAUDE_CODE_SESSIONS.md` — aggiunto Protocollo SPARC obbligatorio
- AGGIORNATO: `Clienti/EXPONIUM/CLAUDE.md` — aggiunta sezione SPARC Workflow
- AGGIORNATO: `Clienti/EXPONIUM/MASTER_PLAN.md` — Cap.9 ora include architettura AgentDB completa

## [2026-05-28] — PUSHED: CLAUDE.md + GIORNATA.md — workflow automatico sessioni Exponium

- CREATO: `CLAUDE.md` nella cartella Exponium — istruzioni complete per Claude Code:
  - All'inizio di ogni sessione: legge git log, legge MASTER_PLAN, identifica utente (Max vs Gael), scrive piano del giorno
  - Quando utente dice "finito/done/chiudiamo/pusha": esegue automaticamente git add+commit+push, aggiorna GIORNATA.md
  - Né Max né Gael devono ricordare comandi git — li esegue sempre Claude Code
- CREATO: `GIORNATA.md` — log sessioni aggiornato automaticamente da Claude dopo ogni sessione
- PUSHED: commit 72e765f su `https://github.com/ansjkfgheqrlg/exponium-client`

## [2026-05-28] — PUSHED TO GITHUB: Piano Operativo Exponium — commit d4b10a1

- PUSHED: `https://github.com/ansjkfgheqrlg/exponium-client` (branch master)
- 4 file caricati: MASTER_PLAN.md, CLAUDE_CODE_SESSIONS.md, GAEL_TASKS.md (aggiornato), sync.ps1
- GAEL_TASKS.md ora include sezione GitHub completa: link repo, come clonare, git pull, sync.ps1
- MASTER_PLAN.md ora include sezione GitHub con link repo e istruzioni push per Max

## [2026-05-28] — UPDATE: EXPONIUM Piano — Aggiunto CLAUDE_CODE_SESSIONS.md + sync.ps1

- CREATO: `CLAUDE_CODE_SESSIONS.md` — prompt pronti da incollare in Claude Code per ogni capitolo (Cap.1, 2A/B/C/D, 3, 4, 6, 9)
  - Ogni prompt è self-contained: include contesto, tech stack, codice skeleton, criteri di completamento
  - Pensato per essere eseguito autonomamente da Claude Code senza domande
- AGGIORNATO: `sync.ps1` — script PowerShell per pushare su GitHub con messaggio custom
  - Uso: `.\sync.ps1 "Cap.2 - Google Maps scraper"` — fa add+commit+push automaticamente
- Gael ha accesso solo tramite GitHub clone — tutto il coordinamento via repo condiviso

## [2026-05-28] — INGEST: EXPONIUM Piano Operativo Maestro — 3 Prodotti

- CREATO: `Clienti/EXPONIUM/MASTER_PLAN.md` — piano operativo completo in 15 capitoli
  - Prodotto 1: Outreach Platform (Cap. 1-7) — pipeline scraping→qualifica→Bibbia→umanizzazione→invio, 500 lead/giorno, dashboard grafica
  - Prodotto 2: Content Factory (Cap. 8A-8F) — Canva automation via Playwright (delegato a Gael) + AI copy generator + Hitsfield CLI
  - Prodotto 3: Second Brain Exponium (Cap. 9-10) — wiki strutturata + guide operative + 3 skill Claude custom
- AGGIORNATO: `Clienti/EXPONIUM/GAEL_TASKS.md` — aggiunti 7 task Canva (Canva-A→G) per automazione Playwright caroselli
  - Task: account dedicato, mapping UI, login script, crea design, modifica testi, flussi alternativi, test e2e
- Piano organizzato a "capitoli" autonomi: Max porta un capitolo per sessione, Claude guida l'esecuzione

## [2026-05-28] — UPDATE: Preventivo + Presentazione EXPONIUM — aggiunto servizio Second Brain

- MODIFICATO: `preventivo-exponium/app/page.tsx` — aggiunto 3° prodotto Second Brain
  - Cover: tag SECOND BRAIN aggiunto + intro aggiornata ("tre sistemi AI")
  - Section 3: 4° blocco problema "L'AI non ha memoria del business di EXPONIUM" (metrica 0%)
  - Section 4: 2 nuove before/after card su briefing ripetuti e contesto applicato
  - Section 8 ristrutturata: 3 card individuali (Outreach €3.200 | Second Brain €2.500 | Content €2.800) + Engine Room full-width bundle €6.500 (vs €8.500, risparmio €2.000)
  - BOOKING_URL aggiornato → https://presentazione-empire.vercel.app/#prenota
  - DEPLOYED: https://preventivo-exponium.vercel.app/
- MODIFICATO: `presentazione-empire/src/app/page.tsx` — aggiunto 3° sistema Second Brain
  - totalSlides 17 → 19, tutti e 3 gli array slide aggiornati
  - Section 2: griglia 2-col → 3-col, 3° card Second Brain (Knowledge Graph · Context Engineering · Memoria Permanente)
  - Section 14 NUOVA (bg-ink): Second Brain Service — storia RAG→Second Brain, Andrej Karpathy/Context Engineering, 3 feature bullets, workflow 4 step
  - Section 15 NUOVA (bg-grey): Second Brain Kit — 3 card (Knowledge Base a Grafo, Integrazione LLM, Workflow Aggiornamento)
  - Pricing: grid 3 card (Outreach | Content | Second Brain ENGINE 03) + Engine Room full-width bundle
  - DEPLOYED: https://presentazione-empire.vercel.app/

## [2026-05-28] — INGEST: Agency Empire Landing — copia completa sito CCM con copy agency

- CREATO: `agency-empire-landing` in `C:\...\Digital Empire\agency-empire-landing`
- Stack: Next.js 15 + Tailwind v4 + Framer Motion + Lenis (identico a index_backup-empire)
- 25 sezioni riscritte con copy agenzia (3 prodotti: Outreach Factory, Content Factory, Second Brain)
- Copy pillars: €0 canoni, codice tuo, 7 giorni setup, 90gg supporto, APSOC Framework
- 4 obiezioni CPB: ChatGPT, ban Instagram, copy robotico, dipendenza
- CTA: #prenota → CallCTA con label "Prenota una Chiamata Strategica"
- Pagina wiki creata: [[Agency_Empire_Landing]]

## [2026-05-27] — UPGRADE #3: Agency Empire — Empire Premium Style · Grain + Marquee + 2 Nuove Sezioni

- SKILL USATA: `/empire-premium-style` — processo a 8 step con sito CCM come reference
- CCM ANALISI: Lette tutte le 28 sezioni CCM (`src/components/sections/`). Sezioni mancanti in agency identificate: `chi-siamo`, `stack`, `competitors` (non aggiunto), `about-story`
- GLOBALS.CSS — Grain System Upgrade:
  - Layer 1: `screen` → `overlay` (opacity 0.65 → 0.55) — grain visibile su ENTRAMBI sfondo scuro e chiaro
  - Layer 2: `soft-light` → `hard-light` (opacity 0.30 → 0.30, alpha SVG 0.40 → 0.50) — texture intensa
  - `fiber-layer`: opacity 0.10 → 0.18, blend `soft-light` → `overlay` — fibra visibile
  - `bg-ink`: `#0d0d0d` → `#080808`, aggiunto 3° radial (blue ambient), gradient più saturo
  - `bg-ink-2`: più profondo `#050505→#020202`, aggiunto radial blue laterale
  - `stat-card-silver`: aggiunto cream-brand highlight in alto-destra `rgba(237,238,190,0.24)`
  - `card-silver-gold`: aggiunto cream-brand highlight in alto-destra `rgba(237,238,190,0.20)`
  - Safari fallback: `@supports not (mix-blend-mode: overlay)` — graceful degradation
- HERO (01-hero.tsx): Aggiunto marquee bar CCM-style DENTRO la sezione hero
  - Gradient silver/white/cream-gold come il CCM original
  - Testo: "AI Workflow Agency · Outreach Workflow · Content Workflow · by Digital Empire"
  - Dots in electric blue `#3a6bc0` (brand) invece di orange
- NUOVA SEZIONE 16-chi-siamo.tsx: "Chi siamo / Team"
  - 3 sub-sezioni: Intro (bg-paper) + Team cards (bg-ink-2) + Mission (bg-paper)
  - Team: Maximilian (founder), Gael (socio), Leonardo (team)
  - Mission card: "L'agenzia progettata per essere licenziata"
  - Adattato da CCM about-story con colori navy/cream
- NUOVA SEZIONE 17-stack.tsx: "Stack strumenti"
  - 12 tool: Make, n8n, Clay, Apollo, Claude AI, Instantly, HeyReach, Airtable, Notion, PhantomBuster, Buffer, ElevenLabs
  - Gradient card: silver/cream → electric blue navy (equivalente navy del card-silver-orange CCM)
  - Radial glow navy in basso-destra (pattern CCM identico ma con navy)
- PAGE.TSX: Stack dopo Processo, ChiSiamo dopo Portfolio
- BUILD: ✅ Compiled 2.3s, TypeScript OK, 4 route statiche
- DEPLOY: `https://agency-empire-kohl.vercel.app` (production)

## [2026-05-27] — UPGRADE #2: Agency Empire — CCM-Level Visual Redesign (Deep)

- ANALISI: Letto codice sorgente CCM icro-empire (`globals.css`, `page.tsx`) — estratta ricetta esatta card premium
- PRINCIPIO CCM: card chiare → gradiente radiale puro `#ffffff → #f4f1f7 → #d9d4e1`, NO grain, shadow 4-layer
- FIXES globals.css:
  - `stat-card-silver` → gradiente puro CCM, shadow 4-strati con navy (rimosso grain/multiply)
  - `card-silver-gold` → gradiente puro CCM, shadow 4-strati (rimosso grain/multiply)  
  - `card-dark-red` → più scuro/saturo `#380c0e → #180404`, border 1.5px, inner red glow, drop shadow più forte
  - `silver-chip` → REDESIGN: da dark blue `#4a6da3` a LIGHT silver/bianco con testo navy — identico CCM
  - `corner-bracket` → abilitato (era `display: none !important`)
- FIXES sezioni:
  - `08-processo.tsx`: `bg-paper` → `bg-ink` + testi per sfondo scuro + glow ambientale blue
  - `10-per-chi.tsx`: card-dark → card-dark-red per "non lavoriamo" card
  - `01-hero.tsx`: silver chips spostati a livello section (fix overflow-hidden clip)
  - `03-servizi.tsx`: landing card gradient da `#f5eefe` (bianco) a `#c090f0` (viola medio)
- BUILD: ✅ zero errori TypeScript
- DEPLOY: `https://agency-empire-kohl.vercel.app` (production)

## [2026-05-27] — UPGRADE: Agency Empire Site — Design Quality Lift

- ROOT: bg troppo chiaro (#131313), stat cards flat (dark su dark), hero senza silver chips, card-silver-purple slavata
- FIX globals.css (6 modifiche):
  - `--color-ink: #0d0d0d` (da #131313) — sfondo più scuro
  - `bg-ink` base: `#0d0d0d → #080808`, `bg-ink-2`: `#060606 → #030303`
  - Grain layer 1 opacity: `0.65` (da 0.55) — più visibile su dark
  - `btn-gold` — gradiente più brillante `#2558c0 → #051844`, border cream più opaco, double glow (navy + blue)
  - `card-silver-purple` — gradiente metallico viola da `#c8b0e8 → #1e0850` (no più lavanda slavata `#f6f1fb`)
  - `stat-card-silver` — fill bianco/silver puro per contrasto masssimo su dark bg
  - `card-dark` — texture grana più visibile, border leggermente più chiaro
  - `step-num` — glow più intenso con double shadow
- FIX 02-stats.tsx — dark gradient inline → `stat-card-silver` CSS class; numeri navy su card bianca (contrasto CCM-level)
- FIX 01-hero.tsx — aggiunto 3 glow radiali, 4 silver chips flottanti (40+ automazioni, H24, 100%, Demo gratuita)
- FIX 05-diagnosi-cro.tsx — icon box con boxShadow, label testo bianco con text-shadow
- BUILD: ✅ zero errori TypeScript, 3 route statiche generate
- PATH: `agency-empire/`
- ISPIRAZIONE: icro-empire CCM site (stat-card-silver white on dark, silver chips)

## [2026-05-27] — FIX: Outreach Dashboard — crash risolto + 9 file creati/aggiornati

- ROOT CAUSE: `globals.css` e `src/lib/utils.ts` mancanti → pagina bianca, zero stili
- FIX CRITICO: creati entrambi i file + full Empire design system (bg-ink, card-dark, grain-fine, bubbles, marquee, btn-orange, ecc.)
- BUILD: 5 API routes create da zero:
  - `GET /api/status` — legge process-state.json + parsing stats da log file
  - `POST /api/launch` — spawna Python subprocess (run.py/run_parallel.py) con demo mode fallback
  - `POST /api/stop` — taskkill python.exe + aggiorna stato
  - `GET /api/logs` — SSE streaming live da outreach-live.log (polling 200ms)
  - `GET /api/leads` — legge emails_ready.json reali (250 lead), search + paginazione
- UPDATE: Lead Explorer → dati reali (250 lead), paginazione funzionante, export CSV
- UPDATE: Dashboard page.tsx → stat chips da `/api/status` (dinamiche)
- UPDATE: Accounts page.tsx → Global Cluster Health dinamico
- BUILD: `mobile-nav.tsx` — hamburger drawer per mobile
- BUILD: `not-found.tsx` — pagina 404 Empire style
- FIX: `chat.tsx` — rimossi CSS obsoleti (card-premium, bg-premium-gradient)
- UPDATE: `layout.tsx` — aggiunto `<MobileNav />` + import
- PATH: `Outreach/outreach-dashboard-premium/`
- RESULT: HTTP 200, /api/leads → 250 real leads, search operativa, SSE logs live

## [2026-05-26] — ADD: Copy Workflow — 3 agenti strategy layer creati

- ADD: cartella `agents/strategy/` popolata con 3 agenti strategici (era vuota)
- S1 `funnel-strategist.md` — architettura funnel: tipo (corto/medio/lungo/social), distribuzione APSOC per step, lunghezze benchmark, follow-up non-convertiti, KPI target
- S2 `positioning-strategist.md` — USP reale/finto/costruito, mappa competitiva (Opposto vs Superiore), awareness scale Schwartz, brand voice codificato per sezione APSOC
- S3 `campaign-strategist.md` — inventario asset con Tier 1/2/3, framework A/B test (single variable + hypothesis), timeline produzione, KPI dashboard con soglie di allarme
- POSIZIONE nel workflow: dopo A2 (Target Analyst), prima degli agenti APSOC A3-A7
- PATH: `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/agents/strategy/`

## [2026-05-26] — EXPAND: Copy Workflow — tutte le 6 sub-skill espanse a struttura professionale

- EXPAND: 6 sub-skill di `copy-workflow` portate da singolo SKILL.md a struttura completa (references/ + assets/templates/ + agents/)
- SKILL objections-forge: +4 file — `cpb-deep.md`, `obiezioni-per-settore.md`, `cpb-worksheet.md`, `cpb-ho-gia-provato.md` (esempio annotato)
- SKILL headline-forge: +3 file — `formule-espanse.md` (10 formule F1-F10), `headline-per-contesto.md` (awareness/formato/tier), `headline-batch.md` (template 10 headline)
- SKILL target-avatar: +3 file — `research-methods.md` (6 fonti), `avatar-canvas.md` (10 sezioni), `avatar-giulia.md` (esempio annotato)
- SKILL funnel-designer: +2 file — `funnel-economics.md` (CAC/LTV/KPI/diagnosi), `funnel-canvas.md` (8 sezioni con math validation)
- SKILL copy-review: +4 file — `scoring-guide.md` (criteri/penalizzatori/benchmark), `riscrittura-patterns.md` (7 pattern chirurgici), `review-template.md` (5-step template), `reviewer-agent.md` (A8 system prompt)
- SKILL apsoc-builder: +3 file — `sezione-per-sezione.md` (guida operativa A/P/S/O/C), `apsoc-canvas.md` (pre-scrittura canvas), `apsoc-conductor.md` (orchestratore 6 fasi)
- TOTAL: +22 file aggiunti in questa sessione
- PATH: `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/`

## [2026-05-26] — BUILD: Copy Workflow Orchestration Layer creato con content-forge

- BUILD: `copy-workflow` orchestration layer costruito via content-forge (target=orchestration) da "Il Manuale del Copywriting v1.1" (115 pagine, ~22.700 parole)
- PATH: `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` — 22 file
- ARCHITETTURA: orchestratore master (copy-master.md) + 8 agenti specializzati (A1-A8) + 6 sub-skill + 4 workflow + 4 template
- FRAMEWORK CORE: APSOC (Attention→Problem→Solution→Objections→CTA) + CPB (Claim→Proof→Benefit)
- COMANDI: `/copywriting full|ad|sales-page|email|headline|objections|avatar|funnel|review`
- QA: sistema score 100 punti con gate automatici (≥80 standard, ≥85 sales page)
- WIKI: pagina tool creata → `tools/Tool_Copy_Workflow_Orchestration.md`

## [2026-05-24] — BUILD: beast-preventivi skill creata con content-forge

- BUILD: skill `beast-preventivi` costruita via content-forge (target=skill) da PREVENTIVI.md (7 fonti, 66 atomi KG)
- PATH: `C:\Users\Utente\.claude\skills\beast-preventivi\` — 12 file
- ARCHITETTURA: SKILL.md kernel + 6 references (concepts/stages/patterns/conventions) + template + esempio + evals
- PRINCIPIO CORE: problem-centric selling — tutto gira intorno al problema del cliente
- CONTESTO: specializzata per landing page agency, adatta a cliente aware/unaware
- STRUTTURA: discovery → pricing 3 opzioni → documento 8 sezioni → call presentation + gestione obiezioni
- EVALS: 6 prompt realistici in evals.json

## [2026-05-24] — INSTALL: content-forge skill installata ufficialmente in Claude Code

- INSTALL: `content-forge` v1.0 estratta da zip (438 entries) → `C:\Users\Utente\.claude\skills\content-forge\` (433 file)
- SOURCE: `SKILL & Agenti/Content-forge/skill - FINALE/workspace-*.zip`
- STATUS: Skill attiva globalmente — disponibile come `/content-forge` o trigger naturale in tutte le sessioni Claude Code
- STRUTTURA: agents/ + assets/ + references/ + scripts/ + SKILL.md (kernel) + ARCHITECTURE.md
- CAPACITA': Trasforma transcript/documenti raw → 8 target (doc, agent, team, skill, workflow, orchestration, wiki, custom) + MKD obbligatorio intermedio

## [2026-05-24] — CLEANUP COMPLETO: Exponium — Rimozione completa identità Digital Empire

- COMPLETATO: pulizia blocco-DE su tutti i file Python del sistema outreach Exponium
  - Zero riferimenti a "Digital Empire", "Max Ricci", "Andrei Pascu", "agency-empire" nei prompt AI
  - Unica eccezione intenzionale: `brand_voice.py` BANNED_VOCABULARY (penalizza le email che li contengono)

- REWRITE critico — `outreach/knowledge/apsoc.py`:
  - TEMPLATE_A/B/C → da PMI locale (ristorante/palestra/dentista) a SaaS B2B
  - APSOC_FULL_FRAMEWORK → esempi reali per VP Sales, Head of Growth, Founder, RevOps
  - DR_PRINCIPLES → benchmark SaaS (reply rate, MQL-to-SQL, close rate)
  - APPROVED_OPENERS → segnali LinkedIn (hiring SDR, funding, expansion)
  - CPB_FRAMEWORK → esempi Template A/B/C SaaS
  - FOLLOW_UP_SEQUENCE → link `agency-empire-kohl.vercel.app` → `[LINK_CASE_STUDY]`
  - LINKEDIN_AUTOMATION_RULES → rimosso "Digital Empire" dall'header

- REWRITE critico — `outreach/knowledge/copy_training.py` (già fatto 2026-05-23):
  - 21 riferimenti DE rimossi, 14 esempi email (fisioterapisti/ristoranti) → esempi SaaS B2B
  - FIRM → env vars SENDER_NAME / COMPANY_NAME
  - SECTOR_MICRO_RULES → ROLE_MICRO_RULES per ruoli SaaS (vp_sales, head_of_growth, founder, revops)

- FIX critico — `agents/qualifier.py`:
  - QUALIFIER_SYSTEM_PROMPT completo rewrite: ICP info-product/coach → ICP VP Sales/Head of Growth/Founder SaaS
  - Scoring: hiring SDR, funding recente, ruolo sales/growth → +15-20 punti
  - Template logic: A=founder-led, B=outbound deludente, C=post-Series A scaling
  - `_qualifica()` → usa `call_ai()` invece di rotation openai, campi lead aggiornati (ruolo, funding, trigger)

- FIX critico — `agents/followup_writer.py`:
  - `_NICCHIE_FOLLOWUP` (7 nicchie PMI) → `_ICP_FOLLOWUP` (5 ruoli SaaS: vp_sales, growth, founder, revops, sdr_manager)
  - `_get_nicchia()` → `_get_icp_role()` — mappa titoli B2B SaaS
  - F1/F2 system prompts → sender da env var, rimosso "Max Ricci / Digital Empire"
  - CTA_LINK → env var `CTA_LINK` con fallback `[LINK_CASE_STUDY]`
  - Imports → `call_ai()` da ai_client, rimosso `openai`/`build_rotation`

- FIX critico — `agents/conversation_manager.py`:
  - `_RISPOSTA_SYSTEM` → sender da env var, rimosso "Max Ricci, consulente di Digital Empire"
  - CTA_LINK → env var
  - Imports → `call_ai()`, rimosso `openai`/`build_rotation`

- FIX — `agents/bibbia_team.py`:
  - Checker prompts → rimosso "Digital Empire" e "Max Ricci in persona"
  - `_chiama_checker()` → usa `call_ai(qa_mode=True)`, rimosso `openai` import
  - `BibbiaTeam.__init__` → non richiede più `openrouter_api_key`

- FIX — `agents/writer.py`:
  - Replacement pair: `("La nostra agenzia", "Digital Empire")` → `"La mia esperienza"`
  - Docstring: "Andrei Pascu" → "B2B SaaS peer-to-peer"

- FIX batch — docstrings di 11 file module header → "Exponium Outreach"
  - apify_leads_finder, apify_scraper, extractor, google_scraper, maps_browser_scraper,
    orchestrator, outscraper_scraper, reply_monitor, scraper, sender, knowledge/__init__, utils/printer

- FIX minimal — competitor.py, cro_audit.py, insight.py → rimosso DE dalle system prompt (agents non-core per B2B SaaS, da sostituire con research.py)

## [2026-05-23] — FIX CRITICO: Exponium — QA reale + modelli produzione + prompt caching

- FIX: `humanizer.py` → `controlla()` ora chiama i 3 checker AI reali (era hardcoded a 8/10)
  - TIER 1: hard block deterministico (agency tone → fail immediato, zero API cost)
  - TIER 2: soft block deterministico (clichés → penalità -0.5/frase, max -2)
  - TIER 3: 3 checker AI in sequenza con qa_mode=True (usa QA_MODEL più economico)
  - Feedback granulare per writer retry: humanness + APSOC + brand + clichés
  - sleep(1) → sleep(0.3) (meno blocco, retry gestito da call_ai)
- FIX: `ai_client.py` default models corretti per produzione
  - openai: gpt-4o-mini → gpt-4o
  - anthropic: claude-haiku → claude-sonnet-4-6
- NEW: Anthropic prompt caching automatico in `_call_anthropic()`
  - System prompt > 200 parole → cache_control ephemeral automatico
  - Risparmio stimato: -80% costo input token dalla seconda call in poi
  - Per 300 email/giorno con claude-sonnet: ~€150/mese → ~€50/mese
- NEW: parametro `QA_MODEL` in .env — modello separato per QA checker (haiku/mini)
  - `call_ai(qa_mode=True)` usa QA_MODEL se configurato
  - `QA_MODEL=claude-haiku-4-5-20251001` → risparmio ~40% sul costo QA
- UPDATE: `.env.example` — documentazione modelli aggiornata con raccomandazioni reali

## [2026-05-22] — UPDATE: Exponium — Installazione ufficiale marketingskills + skill_loader

- INSTALL: 41 marketing skills da `marketingskills-main/` installate in:
  1. `EXPONIUM/.agents/skills/` — standard Agent Skills spec (project-level)
  2. `~/.claude/skills/` — user-level Claude Code (disponibili globalmente con /cold-email ecc.)
  3. `~/.claude/plugins/marketplaces/` — plugin marketplace manifest
- BUILD: `EXPONIUM/shared/skill_loader.py` — utility condivisa tra outreach + content-factory
  - `load_skill(name)` — carica SKILL.md da .agents/skills/
  - `build_context_block(skill_names)` — blocco context pronto per system prompt AI
  - `load_product_context()` — carica .agents/product-marketing.md
  - Auto-discovery: risale la directory tree per trovare .agents/
- UPDATE: content-factory agents (`brief_agent.py`, `video_script_agent.py`, `qa_agent.py`) → ora usano skill_loader ufficiale invece del path hardcoded a marketingskills-main/
- UPDATE: `outreach/agents/writer.py` → skill_loader importato come utility opzionale
- ARCHITECTURE CHIARITA: skills usate in 3 modi distinti:
  1. Claude Code interattivo → /cold-email, /copywriting, /cro (slash commands)
  2. Python agents runtime → load_skill() inietta SKILL.md nel system prompt
  3. .agents/skills/ → standard multi-agent per future integrazioni

## [2026-05-22] — INGEST: Progetto Exponium — Client Infrastructure Setup

- PROJECT: Nuovo cliente Exponium (SaaS/Software company) — servizi: Outreach Engine + Content Factory + Dashboard
- BUILD AVVIATO: `Clienti/EXPONIUM/` — struttura progetto completa creata
- ARCHITECTURE: 3 sistemi in parallelo:
  1. **Outreach Engine** — clone customizzato del workflow email (8 team agenti, LinkedIn scraper, multi-provider AI)
  2. **Content Factory** — NUOVO sistema multi-formato: carousel, video (HeyGen/Runway), email sequence, social post
  3. **Dashboard** — Next.js 16 app unificata (modulare, splittabile)
- BUILD: `ai_client.py` refactored → multi-provider factory (openai/anthropic/azure/openrouter/groq via .env)
- BUILD: `.agents/product-marketing.md` — template fondante (da completare con info cliente)
- BUILD: `knowledge/icp_profile.py` — ICP scorer con tier A/B/C (template, da compilare post-call)
- BUILD: `content-factory/agents/brief_agent.py` — genera content brief strutturato
- BUILD: `content-factory/agents/video_script_agent.py` — script Reels/VSL/YT Shorts + HeyGen payload
- BUILD: `content-factory/agents/qa_agent.py` — CRO check su ogni output (usa marketingskills/cro skill)
- INTEGRATION: `marketingskills-main/` (46 skill Corey Haines) referenziate negli agenti content factory
- DOC: `GAEL_TASKS.md` — 13 task dettagliati per il team member Gael
- TEAM: Max (architettura + strategia) + Gael (scaffolding + componenti + testing)
- STATUS: Giorno 1 completato — scaffolding + agenti core. Pending: LinkedIn scraper, email_sequence_agent, dashboard API routes
- NOTA CRITICA: product-marketing.md incompleto — richede call con Exponium prima di procedere con knowledge base

## [2026-05-19] — BUILD: Team BIBBIA OUTREACH — QA reale con 3 agenti AI paralleli

- DECISION: il vecchio HumanizerAgent aveva punteggi hardcoded a 8/10 — i checker AI non venivano mai chiamati
- BUILD: `knowledge/bibbia_outreach.md` — documento canonico esterno (editabile senza toccare codice)
  - Sezioni: rubrica CheckerUmano, rubrica CheckerStruttura, rubrica CheckerConversione
  - 3 esempi gold completi (fisioterapista, coach, estetica)
  - 6 anti-esempi commentati con spiegazione del perché falliscono
  - Glossario termini tecnici per nicchia (anti-AI-slop)
- BUILD: `agents/bibbia_team.py` — Team BIBBIA con 3 checker in parallelo (ThreadPoolExecutor)
  - CheckerUmano: tono umano, prima persona, zero AI slop
  - CheckerStruttura: APSOC+V completo, 3 livelli agitazione, Barnum specifico
  - CheckerConversione: oggetto con dato reale, zero link, CTA corretta, lunghezza 200-340 parole
  - Soglia reale: tutti e 3 i checker devono essere >= 7.0 (non 5.5 hard fail)
  - Hard block deterministici pre-AI: frasi agenzia + link nel corpo
  - Feedback specifico per checker → Writer.revise() con istruzioni precise
- MODIFY: `agents/orchestrator.py` — FASE 5 usa BibbiaTeam invece di Humanizer
  - Hard block (frasi agenzia, link) → scartata direttamente, nessun retry
  - Soft fail → Writer riscrive con feedback Bibbia → secondo check Bibbia
  - Report qualità mostra score Bibbia (non più valore fisso)

---

## [2026-05-18] — INGEST: Framework Cold Outreach APSOC (Bibbia Messaggi)

- INGEST: Formazione avanzata cold outreach (video) → 1 pagina creata: `concepts/Framework_Cold_Outreach_APSOC.md`
- Codifica: Effetto Barnum, Inganno Arcobaleno, 5 pilastri, matematica follow-up, checklist pre-invio
- Verifica: framework già encodato nel WRITER_SYSTEM_PROMPT del writer.py (confermato in code review)

---

## [2026-05-15] — UPGRADE v5.0: Team DEEP-INTEL — 5 nuovi agenti email pipeline

### NUOVI AGENTI CREATI (5 file Python + 5 definizioni Claude Code)
- **research.py**: visita sito lead, estrae CRO intelligence rule-based (no AI)
- **cro_audit.py**: AI → 3 problemi CRO specifici con evidenza reale + score 0-10
- **competitor.py**: query SQLite DB → 2-3 competitor stessa nicchia/città
- **insight.py**: sintetizza tutto → insight_brief con apertura_email verificata
- **lead_analyzer.py**: orchestratore — 3 sub-agent paralleli + 1 synthesis

### IMPATTO DIRETTO
Email ora inizia con osservazioni VERIFICATE dal sito reale invece di Barnum generico.

### FILE MODIFICATI
- orchestrator.py: aggiunta FASE 1.5 DEEP-INTEL
- strategist.py: usa insight_brief come angolo primario
- writer.py: apertura_email reale sostituisce Barnum quando disponibile
- SISTEMA_OUTREACH_COMPLETO.md: aggiornato a v5.0

## [2026-05-15] — ARCHITETTURA SUB-AGENTS Instagram: 3 agenti specializzati

### ROOT CAUSE 2 DM invece di 15
- FASE 1 trovava max 20 candidati (4 hashtag × 5 profili)
- 18/20 scartati come "non target" dal filtro bio troppo stretto
- API già trovava 70-103 username per hashtag ma ne prendeva solo 5

### SOLUZIONE: 3 Sub-Agents + FASE 0

**Nuovi file creati:**
- `Instagram Automation/agents/hashtag_scout.py`: scansiona 10 hashtag × 25 profili = 250 candidati. Usa scroll aggressivo (10 round) + API intercept. Restituisce pool massivo.
- `Instagram Automation/agents/profile_qualifier.py`: visita profili in bulk, analizza bio con keyword estese (anche forme femminili), verifica bottone DM. Marca come "qualified". Stop anticipato a 30 qualificati.
- `Instagram Automation/agents/similar_accounts_scout.py`: da lead qualificati, estrae "Profili simili" / account suggeriti da Instagram. Lead ad altissima qualità algoritmica.

**File modificati:**
- `run_today.py`: aggiunta FASE 0 che orchestra i 3 sub-agents prima del DM. max_profiles 5→20, hashtags[:4]→[:8]. Lead "qualified" saltano il filtro bio in FASE 2.
- `config.py`: TARGET_KEYWORDS espanso — aggiunte forme femminili (formatrice, imprenditrice), freelancer, content creator, professioni con alta spesa (fotografo, psicologo, avvocato, ecc.)

### MATEMATICA GARANTITA
- Scout: 10 hashtag × 25 = 250 candidati
- Qualifier: visita max 60, con tasso 15-20% → 9-12 qualificati
- Similar Scout: da 5 profili top → 30-50 candidati bonus
- Totale pool qualificato: 30+ → garantisce 15 DM/giorno

---

## [2026-05-14] — FIX CRITICO Sistema Outreach: Instagram + Email + DB

### BUG RISOLTI
- **Instagram 0 DMs**: `scrape_hashtag()` ora usa fast-path URL parsing (instagram.com/USER/p/ID) + JSON-LD + article header + debug logging. Prima 4 metodi JS fallivano tutti.
- **settore_calibrato missing**: colonna aggiunta al DB via ALTER TABLE + COALESCE fallback nelle query di `run_followup.py` + migration in `orchestrator._init_db()`.
- **Email 0 inviati (old targets)**: SETTORI in `scraper.py` aggiornati da fisioterapista/avvocato/dentista → business coach/life coach/social media manager/agenzia marketing/consulente ecommerce/shopify expert/consulente aziendale.
- **Unicode crash su Windows cp1252**: `sys.stdout.reconfigure(encoding="utf-8")` aggiunto a `run_parallel.py`, `rerun_partial.py`, `Instagram Automation/run_today.py`.
- **run_parallel.py EMAIL-GEN**: rimosso `--csv leads_freschi_validated.csv` (aveva 52 lead OLD già nel DB) → ora usa scraper Apify direttamente con nuovi SETTORI.

### TARGET AUDIENCE DEFINITIVO
Email, LinkedIn, Instagram puntano tutti allo stesso segmento: coach, formatori, info product creator, SMM freelance, agenzie marketing, ecommerce/dropshipping, consulenti B2B italiani.

## [2026-05-13] — CATENA INSTAGRAM aggiunta al Sistema Outreach

### NUOVI FILE CREATI
- **`Instagram Automation/config.py`**: credenziali (da .env), limiti giornalieri (15 DM/giorno), hashtag target, keyword bio
- **`Instagram Automation/personalize.py`**: generatore messaggi AI adattato per Instagram — stessa pipeline Strategist→Writer→Humanizer di LinkedIn ma messaggi ≤50 parole, zero link nel primo DM, tono più diretto
- **`Instagram Automation/refresh_session.py`**: apre browser, utente fa login, salva `instagram_session.json`
- **`Instagram Automation/run_today.py`**: flusso completo — FASE 1 (scoperta lead da hashtag), FASE 2 (DM primo contatto), FASE 3 (F1 giorno 2-3), FASE 4 (F2 giorno 6-7 break-up)
- **`Instagram Automation/check_replies.py`**: legge DM non letti dall'inbox, genera suggerimenti risposta, modalità `--autoinvia` disponibile
- **`Instagram Automation/instagram_leads.json`**: DB lead Instagram (JSON, analogo a linkedin_leads.json)

### MODIFICHE FILES ESISTENTI
- **`run_parallel.py`** → v4.0: aggiunta CATENA INSTAGRAM (IG-DM → IG-REPLIES sequenziale, parte in parallelo con LI+EMAIL con stagger 5s). Instagram è non-bloccante: se sessione non trovata, le altre catene girano normalmente.
- **`SISTEMA_OUTREACH_COMPLETO.md`** → v4.0: documenta catena Instagram, differenze vs LinkedIn, stati lead, comandi separati

### DIFFERENZE CHIAVE INSTAGRAM vs LINKEDIN
- No connection request — DM diretto a profili pubblici
- Limite 15 DM/giorno (vs 20 connessioni LinkedIn) — Instagram più sensibile
- Max 50 parole primo DM (vs 75 LinkedIn)
- Zero link nel primo DM (Instagram penalizza)
- F1 dopo 2-3 giorni (vs 3-4 LinkedIn) — attività più veloce su IG
- Lead discovery: hashtag scraping (vs keyword search LinkedIn)

---

## [2026-05-12] — SISTEMA COMPLETO: Follow-up + Reply Monitor + Conversation Manager

### NUOVI MODULI COSTRUITI
- **`Outreach Workflow/agents/followup_writer.py`**: genera F1 (giorno 3) e F2 (giorno 7) con stesso framework Barnum/Rainbow/anti-AI-slop della prima email. QA automatico >= 7.0. Opener Rainbow DIVERSO dall'originale, angolo pain alternativo per nicchia.
- **`Outreach Workflow/agents/reply_monitor.py`**: controlla Gmail IMAP per risposte dai lead nel DB. Estrae testo pulito (rimuove quoted text). Dedup per lead.
- **`Outreach Workflow/agents/conversation_manager.py`**: classifica la risposta (POSITIVO/OBIEZIONE/DOMANDA/NON_INTERESSATO), genera risposta appropriata per portare verso la chiamata di 20 minuti. Stesse regole qualità della prima email.
- **`Outreach Workflow/run_followup.py`**: orchestratore giornaliero. Carica lead eligibili F1 (3+ giorni senza risposta) e F2 (4+ giorni da F1). Genera + invia + aggiorna DB.
- **`Outreach Workflow/run_reply_manager.py`**: IMAP scan → classifica risposta → genera replica → invia → aggiorna DB (conversazione_stato).
- **`LinkedIn Automation/check_replies.py`**: Playwright read-only su LinkedIn messaging. Rileva risposte non lette dai lead. Genera suggerimenti risposta via AI. Modalità --autoinvia disponibile.
- **`run_parallel.py`** → v2.0: aggiunge FASE 3 (FOLLOWUP + REPLY-MGR parallelo) e FASE 4 (LI-REPLIES).

### SCHEMA DB AGGIORNATO
Nuove colonne in `leads_contattati`: f1_inviata, f1_oggetto, f1_corpo, f2_inviata, f2_oggetto, f2_corpo, risposta_ricevuta, risposta_testo, risposta_oggetto, conversazione_stato.

### FLUSSO COMPLETO GIORNALIERO
FASE 1 (parallelo): commenti + connessioni + genera email
FASE 2: invia email
FASE 3 (parallelo): followup F1/F2 + reply manager email
FASE 4: check DM LinkedIn (suggerimenti)

---

## [2026-05-12] — PIANO OUTREACH DEFINITIVO: LinkedIn + Email Full Python

### DECISIONE STRATEGICA
- **Drop**: Chrome Extension approach — abbandonata definitivamente
- **LinkedIn**: 40 commenti/giorno (warming) + 20 connection requests CON NOTA (Barnum/Rainbow 300 char) + DM automatico post-accettazione con 5-pillar + F1/F2 follow-up
- **Email**: ripartenza con 150 email/giorno, stesso framework Barnum/Rainbow/5-Pillar iniettato nel writer email (APSOC+V)
- **Team agenti**: Strategist → Writer → Humanizer per entrambi i canali, framework "ultima formazione" come bibbia

### FILE MODIFICATI
- `LinkedIn Automation/config.py`: `DAILY_COMMENT_LIMIT = 40`
- `LinkedIn Automation/personalize.py`: aggiunta `generate_connection_note()` — 300 char per nicchia, Barnum/Rainbow compresso
- `LinkedIn Automation/run_today.py`: `send_connection()` ora invia richiesta CON NOTA; fallback a "senza nota" se LinkedIn non supporta
- `Outreach Workflow/agents/strategist.py`: sistema prompt arricchito con Effetto Barnum/Rainbow + dict niche_term + output JSON esteso con `barnum_opener` e `niche_term`
- `Outreach Workflow/agents/writer.py`: `[A] ATTENZIONE` aggiornato per usare Barnum/Rainbow come tecnica primaria; `_formatta_strategy_brief()` passa i nuovi campi al modello
- `Outreach Workflow/run.py`: target default 150 (da 300)
- `Outreach/run_all.bat`: nuovo — lancia tutta la sequenza daily in ordine: commenti → connessioni → genera email → invia email

---

## [2026-05-12] — Claude Chrome Prompt AUTONOMO: Phase 2 Self-Directing

### PIVOT CRITICO: 3° GRADO NON MESSAGGIABILE
- **Problema scoperto**: tutti i 10 lead della Phase 1 erano 3° grado → LinkedIn blocca con paywall
- **Soluzione**: Phase 2 — Claude Chrome cerca autonomamente, filtra SOLO 1° grado
- **File creato**: `chrome_prompt_autonomo.md`
- **Logica**: URL con `?network=%5B%22F%22%5D` filtra 1° grado direttamente da LinkedIn Search
- **Workflow autonomo**: Search → valuta grado → analizza profilo → Barnum/Rainbow → 5 Pilastri → checklist 6 punti → invia → 35-50sec → ripeti (max 15 DM/sessione)
- **Framework embedded**: Barnum + Rainbow opener per ogni nicchia, prova con numeri, valore gratuito concreto, CTA binaria, termine tecnico anti-AI-slop per nicchia

---

## [2026-05-12] — Claude Chrome Prompt v2: 10 Messaggi con Framework 5 Pilastri

### UPGRADE SYSTEM PROMPT claude_chrome_prompt.md
- **Problema**: prima versione usava template fallback generici, nessun Barnum/Rainbow, nessun anti-AI-slop
- **Soluzione**: rewrite completo con 3-pass validation (Draft → 6-point checklist → Polish)
- **Framework applicato**: Barnum opener OPPURE Rainbow opener (mai entrambi), niche_term hard-coded, proof_hint concreto, micro-commitment CTA binaria, max 75 parole
- **Varietà fisioterapisti** (5/10 leads): 3 angoli diversi — Barnum (passaparola), Rainbow (slot vuoti), Urgenza (dolore adesso), Barnum-trust (fiducia passaparola≠online)
- **Dentisti**: Lead 1 Barnum (segreteria occupata) vs Lead 9 Rainbow (qualità clinica) — stesso proof, opener diverso
- **File aggiornato**: `LinkedIn Automation/claude_chrome_prompt.md`

---

## [2026-05-12] — INSIGHT: Claude Chrome Extension per LinkedIn Automation

### POTENZIALE GAME-CHANGER
- **Insight utente**: usare l'estensione Claude in Chrome (sidebar) come automazione LinkedIn
- **Vantaggio chiave**: Claude vede l'UI semanticamente (non via CSS selectors) → immune ai cambi DOM
- **Approccio**: system prompt dettagliato con target, template messaggi, workflow, anti-ban rules
- **Sostituisce**: tutta la pipeline Playwright (comment_posts.py, direct_dm.py, run_today.py)
- **Domanda aperta**: autonoma (unattended) vs. supervisione per ogni click?
- **Se autonoma**: rivoluziona il setup — zero manutenzione codice, zero ban detection issues
- **Prossimo step**: testare se può fare azioni senza approvazione manuale

---

## [2026-05-12] — Strategia LinkedIn: Direct DM + Comment Warmer (no connection requests)

### PIVOT STRATEGICO
- **Decisione utente**: stop connection requests — troppo lenti su account nuovo, nessun risultato
- **Nuova strategia**: Direct DM su Open Profile + Comment Warmer per warm-up

### NUOVO SCRIPT: `direct_dm.py`
- Cerca profili via People Search (35 keyword variazioni)
- Strategia 1: tasto "Message" inline nelle card dei risultati (Open Profile)
- Strategia 2: visita profilo singolo, cerca tasto Message
- Genera DM con framework 5 Pilastri (generate_message da personalize.py)
- Limite: 25 DM/giorno

### `comment_posts.py` RISCRITTO
- Abbandonato Content Search (0 risultati, selettori CSS instabili)
- Nuova strategia: People Search → visita /recent-activity/all/ → commenta
- Limite: 30 commenti/giorno
- **Risultato oggi**: funziona, 7/30 commenti inviati

### BLOCCHI TECNICI RISOLTI OGGI
- JS SyntaxError su multi-line selectors → single-string selectors
- Content Search LinkedIn → 0 risultati (cambi DOM) → rimpiazzato con People Search
- PYMK → 0 target (account nuovo) → rimpiazzato con keyword search
- Class-based CSS selectors per profili → rotto → sostituito con approccio DOM-agnostic (h1, text scan)
- People Search: ~2-4 risultati per ricerca su account nuovo (limite LinkedIn)

### LIMITAZIONE LINKEDIN NUOVI ACCOUNT
- People Search: max 2-4 profili per ricerca
- Profile view: spesso ristretta → no Message button visibile
- DM diretti: solo su Open Profile (LinkedIn Premium) o 1° grado
- **Impact**: direct_dm trova profili ma raramente trova Open Profile → bassa conversione oggi

---

## [2026-05-12] — Cold DM Framework v2: 5 Pilastri ✅

### UPGRADE MESSAGGI LINKEDIN — Framework da video Giovanni (Lussemburgo #1 Tech)

**Fonte**: creator italiano >$100k in 1 anno, <5% da content, 95% da outbound (600 commenti/settimana + 100 DM/settimana)

**5 Pilastri implementati in personalize.py**:
1. **Barnum/Rainbow opener** — frase universale-specifica per ogni nicchia (sembra personale, si applica al 99%)
2. **Identità + Prova** — "Sono Max — [risultato concreto per nicchia]" in 1 frase
3. **Valore Gratuito** — offerta analisi gratuita PRIMA di qualsiasi richiesta
4. **Micro-Commitment** — CTA binaria sì/no a basso attrito (non "call di 30 minuti")
5. **Anti-AI-Slop** — termine tecnico hard-coded per nicchia (tasso di abbandono booking, prenotazioni H24, ecc.)

**Matematica follow-up** (ora nel prompt):
- M1: ~20% risposta | F1 (gg3): ~40% cumulativo | F2 (gg7): ~50% cumulativo

**FILE AGGIORNATI**:
- `personalize.py` — completo rewrite, nuovi campi NICCHIE (barnum, rainbow, niche_term, free_value, proof_hint), nuovi prompt Writer+Strategist, fallback template con struttura v2
- `second-brain-vault/wiki/sources/Source_Cold_DM_5_Pillar_Framework.md` — pagina wiki con framework completo

---

## [2026-05-11] — LinkedIn Automation: Sistema 50 Contatti/Giorno ✅

### UPGRADE SISTEMA: DA 20 A 50 INTERAZIONI/GIORNO
- **Problema**: primo run aveva inviato 20 connessioni a persone sbagliate (film maker, politici, non professionisti target)
- **Root cause**: PYMK è casuale, non filtra per professione; il vecchio codice non visitava i profili prima di connettere
- **Soluzione implementata**: sistema a 2 step

**Step 1 — comment_posts.py (NUOVO)** — 30 commenti warming/giorno
- Cerca post LinkedIn con keywords per nicchia (avvocato, commercialista, fisioterapista, ecc.)
- Visita la pagina attività di ogni autore, commenta il post più recente
- Commento AI contextual (max 25 parole) via Groq llama-3.3-70b
- Effetto: l'autore vede il nostro nome → riconosce chi siamo quando arriva la conn request → acceptance rate +40%

**Step 2 — run_today.py (AGGIORNATO)** — 20 connessioni target/giorno
- PYMK: 2 visite con 10 scroll ciascuna → pool 100-150 profili
- People Also Viewed: da ogni profilo visitato, raccoglie 8-10 profili stessa nicchia (qualità alta)
- Filtra per professione target PRIMA di connettere (keyword check sul titolo live)
- Verifica "In sospeso" dopo click → connessione confermata

**Totale: 50 interazioni/giorno** — metodologia dai professionisti NotebookLM (600 commenti/settimana + 100 DM/settimana)

### FILE AGGIORNATI
- `comment_posts.py` — nuovo, warming via commenti su post target
- `run_today.py` — PYMK x2 visits + People Also Viewed discovery
- `personalize.py` — aggiunta `generate_comment()` per commenti AI
- `config.py` — aggiunto `DAILY_COMMENT_LIMIT = 30`
- `run_daily.bat` — rimosso groups_outreach, aggiunto comment_posts.py step 1
- `C:\LinkedIn_Bot\run.bat` — aggiornato per Task Scheduler (no spaces path)

### CLEANUP: RICHIESTE SBAGLIATE RITIRATE
- 20 connessioni inviate oggi a wrong_target ritirate via `withdraw_pending.py`
- Status aggiornato da `wrong_target_sent` a `withdrawn` nel DB
- LinkedIn "Gestisci inviti": profili non-target rimossi da pending

### TASK SCHEDULER
- `DigitalEmpire_LinkedIn_Daily` — DISABILITATO (era duplicato, path con spazi)
- `LinkedIn Daily Outreach` — ATTIVO, ore 09:00, runs `C:\LinkedIn_Bot\run.bat`

---

## [2026-05-11] — LinkedIn Automation: Primo Run Completo ✅

### PRIMO RUN GIORNALIERO COMPLETATO CON SUCCESSO
- **20/20 connessioni inviate** (18:34 → 18:43, ~9 minuti)
- Ritmo: 1 connessione ogni ~27 secondi con delays randomizzati anti-ban
- Lead source: 60 lead salvati in `linkedin_leads.json` con status "new" (scoperti via PYMK)
- Tutte le connessioni inviate SENZA nota (tecnica Oleg Melnikov, +30% acceptance rate)

### BUG CRITICO TROVATO E RISOLTO
- **Root cause del fallimento precedente**: il bottone Connect di LinkedIn italiano è un tag `<a>` (non `<button>`) con `aria-label="Invita [Nome] a collegarsi"` — tutti i selettori precedenti erano sbagliati
- **Fix**: `page.evaluate()` cerca `a` o `button` con `aria.includes('a collegarsi')` filtrato per primo nome dall'H1
- **Modal "Invia senza nota"**: richiede `page.click()` nativo Playwright (non JS .click())
- Il fix è stato confermato manualmente con `test_send_one.py` su Antonio Crapanzano (Personal Trainer, FitActive, Bergamo)

### FILE SISTEMA ATTUALE
- `run_today.py` — runner giornaliero unificato con PYMK + saved leads + messaggi + follow-up
- `linkedin_leads.json` — 60+ lead, ora aggiornati a status "connect_sent"
- `run_today_log.txt` — log completo delle operazioni

### PROSSIMI PASSI
- Domani/dopodomani: controllare accettazioni → FASE 2 messaggi AI personalizzati
- Setup Task Scheduler 9:00 AM per run automatico giornaliero

---

## [2026-05-11] — LinkedIn Automation System Costruito

### KNOWLEDGE ESTRATTA DA 3 NOTEBOOK IN PARALLELO
- Notebook 1: "Mastering the Art of Cold Outreach on LinkedIn" (52b88862)
- Notebook 2: "Outreach + Claude Code" (0f77f03e) — 3 professionisti documentati
- Notebook 3: "Multi-AI Outreach and CRO Funnel Optimization System" (11b95def)

### PROFESSIONISTI STUDIATI E WORKFLOW DOCUMENTATI
- **Oleg Melnikov**: Claude Cowork + Apify + Kai AI → 35% response rate
  - Connessioni SENZA nota → acceptance rate +30%
  - Lead scoring con Claude Code (1-10 per priorità)
  - Lead magnet: banner LinkedIn + foto profilo generata con AI gratis
- **Ben AI**: skills .md + Apify post engagers + Uniflow multi-channel
- **Zubair Trabzada**: 14 skills VS Code, /sales-prospect lancia 5 sub-agenti paralleli

## 2026-06-16
- F1-bis COMPLETATO (Gael, CP-20260616-002): arricchimento massivo `company/` chiuso. Gate verde (0 cartelle vuote su 26 iniziali, 0 file <15 righe, 317 file totali), review indipendente PASS su 5 file a campione. I 10 ecosistemi hanno ora Reparti/Funzioni/Workflow/Agenti popolati con schede stile CF (identita, I/O, decision tree, KPI, escalation) ancorate ai dossier PIANO-MAESTRO. Prossima fase = V2-2 (dossier a scala v2, ADR-007), NON F5.
- FIX integrita repo (Gael, CP-20260616-001): risolta collisione case-insensitive in `company/Ecosistemi/06-PLATFORM/Reparti/` (5 doppioni MAIUSCOLO/Title-Case che bloccavano i commit su Windows). Voci fantasma rimosse dall'indice, contenuto arricchito preservato. Regola naming swarm aggiunta in STATO-EMPIRE.
- V2-2 AVVIATA (Gael, CP-20260616-003): creato `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`, blueprint dell'organo MAXIMILIAN (team LX che incarna Max). Ancorato al corpus reale di Max. Definisce 8 agenti MX-*, il review-gate 5-bis (\"Max approverebbe?\" — blocca le fasi da V2-3), 2 workflow CF-grade, 2 skill proprie, deleghe, addestramento sul corpus. Da costruire in V2-3 (priorita alta). Prossimo dossier V2-2: MANDATO-ecosistema.
- V2-2 (Gael, CP-20260616-004): creato `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`, blueprint del Mandato che da documento diventa ecosistema di governo. Gli Articoli 1-7 restano INVARIATI come cuore (wrap ADR-003), avvolti da 6 agenti custodi MND-*, 3 workflow (enforcement/evoluzione/audit), comando sulle 5 Sentinelle, contradiction-check automatico. Confine netto con MAXIMILIAN: Mandato=la LEGGE, Maximilian=lo STANDARD. Da costruire in V2-5. I 2 dossier NUOVI di V2-2 sono ora completi; resta la riscrittura swarm dei dossier 01-09.

### TOOL STACK COMPLETO DOCUMENTATO
- Apify: standard industry per LinkedIn scraping (no ban)
- Claude Cowork: sostituisce Selenium, agisce come umano
- Uniflow: multi-channel (LinkedIn + WhatsApp + X)
- Supabase: database lead
- Make.com / n8n: orchestrazione API
- Sistema Multi-AI: ChatGPT parse → Perplexity research → NotebookLM brief → Claude write

### SISTEMA COSTRUITO
- `LinkedIn Automation/config.py` — configurazione centrale
- `LinkedIn Automation/linkedin_session.py` — login e salvataggio sessione
- `LinkedIn Automation/01_scrape_leads.py` — scraping LinkedIn search
- `LinkedIn Automation/02_send_connections.py` — invio connection requests (no nota, 20/day)
- `LinkedIn Automation/03_check_accepted.py` — controlla accettazioni
- `LinkedIn Automation/04_send_messages.py` — primo messaggio (Claude API)
- `LinkedIn Automation/05_send_followups.py` — follow-up giorno 3-4 + giorno 7
- `LinkedIn Automation/run_daily.py` — runner giornaliero completo
- `LinkedIn Automation/personalize.py` — generazione messaggi con Claude API
- Skill Claude Code: `.agents/skills/linkedin/skill.md`

### APSOC.PY AGGIORNATO
- Aggiunto LINKEDIN_AUTOMATION_PROFESSIONALS con workflow esatti dei 3 pro
- Aggiunto LINKEDIN_AUTOMATION_RULES con regole operative safety

### SKILL NOTEBOOKLM REINSTALLATA UFFICIALMENTE
- `npx skills add https://github.com/teng-lin/notebooklm-py --skill notebooklm` ✓
- Installata per: Claude Code, Antigravity, Codex, Cursor, Gemini CLI + altri

## [2026-05-11] — Knowledge Extraction NotebookLM + Workflow Update Completo

### NUOVI FRAMEWORK ESTRATTI DA NOTEBOOKLM (4 notebook paralleli)
- TRIPLE TAP: Get the Open → Get the Read → Get the Action (framework da "Outreach + Claude Code")
- DELIVERABILITY RULES: max 25-50 email/giorno/mailbox, ZERO link prima email, warm-up 2-4 settimane
- LINKEDIN DM: 5-step (Personalizzazione Barnum, Chiarezza, Valore gratis, Micro-commitment, Basso attrito)
  - Tasso risposta: 1° msg 20%, 2° msg 40%, 3° msg 30%
- FOLLOW-UP OTTIMALE: giorno 3-4 (nudge), giorno 7 (info dump + link), giorno 14 (finale binario)
- APSOC aggiornato: link CTA solo in follow-up #2, non prima email

### MODIFICHE WORKFLOW APPLICATE
- apsoc.py: aggiunti DELIVERABILITY_RULES, TRIPLE_TAP_FRAMEWORK, LINKEDIN_DM_FRAMEWORK, FOLLOW_UP_SEQUENCE
- prepare_emails.py: _aggiungi_cta() disabilitata → ZERO link nella prima email fredda
- send_ready.py: DELAY 45s→90s, DAILY_LIMIT_PER_ACCOUNT = 50 (era 500!)
- fix_b6_remove_links.py: rimosse link da 78/182 email B6 e 105/208 email B5 già preparate
- REGOLA AGGIORNATA: link https://agency-empire-kohl.vercel.app → solo follow-up #2 (giorno 7)

### ROOT CAUSE BOUNCES IDENTIFICATA E CORRETTA
- Causa principale: link nella prima email fredda + volume 500/giorno su singolo account
- Fix applicato: cap 50/giorno + zero link prima email + delay 90s

### NOTEBOOKLM CONNESSO
- notebooklm-py v0.4.0 installato + autenticato
- Skill installata in .agents/skills/notebooklm
- Notebook "Outreach + Claude Code" ID: 0f77f03e-b2c1-415b-b60b-4244446f32a3
- Altri notebook rilevanti: Outreach Coach, LinkedIn Outreach, Multi-AI CRO, Cold Email Claude Code

## [2026-05-11] — Status Audit Completo + NotebookLM Skill

### STATO EMAIL (oggi 2026-05-11)
- STORICO INVIATO: 170 email totali (B1:30 + B2:72 + B3:37 + B4:31)
- B5: emails_b5_ready.json esiste (encoding error, lead dentisti 208)
- B6: 182 email PRONTE, non ancora inviate (nicchie: avvocato:29, palestra:28, psicologo:27, estetica:27, commercialista:26, fisioterapista:24, medico:21)
- RISPOSTE POSITIVE DA PROSPECT: 0 (ZERO su 170 email inviate)

### CRITICO — PROBLEMA DELIVERABILITY (10 maggio)
- PATTERN: OGNI email inviata il 10/05 ha ricevuto bounce "Message blocked" / "Message rejected" dai server destinatari
- Gmail account ha raggiunto il limite 500/day l'08/05 (segnale di reputazione danneggiata)
- Alcune email inviate 2-3 volte stesso indirizzo (spam pattern)
- Lead placeholder identificati: info@studiorossi.it, info@studiomedicomilano.it, info@studiolegalenapoli.it, info@fitnessroma.it → email fake che danneggiano la reputazione
- ROOT CAUSE: troppo volume in poco tempo (170 email in 2 giorni) + lead di bassa qualità + stesso account sender

### FOLLOW-UP STATUS
- B1 follow-up: schedulato 2026-05-09 09:00 (dovrebbe aver girato 2 giorni fa)
- B2 follow-up: schedulato 2026-05-12 09:00 (domani)
- B3 follow-up: schedulato 2026-05-10 09:00 (dovrebbe aver girato ieri)

### NOTEBOOKLM SKILL
- INSTALLATA: npx skills add teng-lin/notebooklm-py → symlink Claude Code + locale .agents/skills/notebooklm
- PACKAGE: notebooklm-py v0.4.0 installato via pip
- STATUS AUTH: NON autenticato → richiede `python -m notebooklm login` (apre browser Google)
- USO: `python -m notebooklm list` → lista notebook → trovare "Outreach + Claude Code"

### AZIONI STRATEGICHE NECESSARIE
- STOP invii per 48-72h per recupero reputazione account Gmail
- Creare secondo account Gmail (gratuito) per round-robin
- Pulire lead da email placeholder prima di ogni batch
- Ridurre volume a max 100-150/giorno per account nuovo
- Attivare LinkedIn DM outreach (nessun problema deliverability)

## [2026-05-08] — Batch 6 (765 lead multi-nicchia) + Catena Invio 500/day
- INGEST: lead-freschi.csv aggiornato a 1104 righe (formato markdown table) → convertito a leads_b6.csv
- PROCESS: 1104 righe → 1001 dedup → 800 unici → 765 freschi (escluse 68 email già inviate storico JSON)
- NICCHIE B6: palestra(133), estetica(130), fisioterapista(127), medico(121), psicologo(85), avvocato(85), commercialista(84)
- PIPELINE: prepare_emails.py --csv leads_b6.csv --output emails_b6_ready.json → in corso (background)
- CHAIN: send_chain_b6.py — aspetta fine B5, aspetta fine generazione B6, invia 472 email (limite 500/day − 28 B5)
- DELAY: ridotto da 90s a 45s in send_ready.py (~80 email/ora con email 100% personalizzate)
- ETA COMPLETAMENTO: B5 (~35 min), B6 gen (~15 min), B6 send (~6h), totale oggi: 500 email
- DECISIONE: utente non vuole creare account Gmail aggiuntivi → strategia 1 account 500/day

## [2026-05-08] — Batch 5 Lead Dentisti Preparati
- INGEST: Creato leads_dentisti_b5.csv → 208 lead dentisti non ancora contattati
- SOURCE: Filtrato da leads_trovati.csv (300 righe) escludendo: 1 blacklisted (studiobittante), 3 email non valide (flags@2x.webp, utente@dominio.com, info@website.com), righe non-dentista (palestre, attività locali varie)
- OVERLAP: 0 email già inviate trovate in leads_trovati.csv (il file contiene lead dentisti completamente nuovi vs batch precedenti che erano fisioterapisti/avvocati/etc)
- COVERAGE: Città coperte — Milano, Roma, Napoli, Bologna, Firenze, Bari, Verona, Genova, Catania, Padova, Brescia, Bergamo, Parma, Modena, Reggio Emilia, Perugia, Trieste, Taranto, Messina, Prato, Reggio Calabria, Cagliari, Venezia, Palermo
- STATUS: Pronto per batch invio B5

## [2026-05-08] — Audit Lead & Capacita' Gmail
- AUDIT: Email inviate oggi (2026-05-08): 0 — nessun invio ancora eseguito oggi
- AUDIT: Limite Gmail residuo oggi: 500/500
- AUDIT: Email cumulative inviate (storico): ~168 (B1:30 + B2:72 + B3:37 + B4:29)
- AUDIT: JSON state — emails_ready.json: 37 sent + 1 ready (B3); emails_b4_ready.json: 30 sent + 1 ready (B4)
- AUDIT: CSV files trovati: 5 file (leads_trovati.csv 300 righe, leads_100.csv 100 righe, leads_nuove_nicchie.csv 37 righe, leads_freschi_clean.csv 31 righe, lead-freschi.csv 100 righe di cui solo 31-32 reali)
- AUDIT: Lead unici non contattati stimati: ~240 (leads_trovati.csv dentisti non ancora usati in bulk) + overlap da verificare con B2
- BOTTLENECK confermato: lead reali freschi esauriti (B4 resto = 1). Servono nuovi lead via Outscraper/Apollo.

## [2026-05-08] — Piano Outreach 1000 Contatti
- ANALYSIS: Diagnosi dataset — lead reali disponibili oggi: 2 (resto di B4). Lead 33-100 in lead-freschi.csv sono placeholder non reali.
- STRATEGY: Piano multi-canale definito — 3 leve: multi-account Gmail (round-robin), Outscraper $4 per 1000 lead, Apollo.io free tier
- ACTION: Round-robin 3 account Gmail porta limite a 1500/giorno; con 3 account + lead Outscraper → ~600-700 email/giorno raggiungibili
- BOTTLENECK: Lead freschi = unico collo di bottiglia. Soluzione immediata: Outscraper.com query "fisioterapista/dentista italia" 1000 righe ($4)
- CHANNELS: Email (principale), LinkedIn DM (~50/giorno), Cold call (~80 in 2h), WhatsApp (solo follow-up, max 20-30/giorno)
- TARGET REALISTICO: 700-800 contatti totali in 8h con infrastruttura completa; 1000 richiede anche LinkedIn attivo + cold call

## [2026-05-07] — Batch 4 inviato (parziale)
- SENT: B4 — 29/31 email inviate (2 rimaste, da inviare domani con send_ready.py --input emails_b4_ready.json --auto)
- TOTALE CUMULATIVO: 30 (B1) + 72 (B2) + 37 (B3) + 29 (B4) = 168 email inviate totali
- UPDATE: send_ready.py — aggiunto flag --input per scegliere file JSON sorgente

## [2026-05-07] — Batch 4 pronto + follow-up schedulati
- CREATE: leads_freschi_clean.csv — 31 lead reali da lead-freschi.csv (righe 1-32, esclusi placeholder 33-100 e dup)
- CREATE: emails_b4_ready.json — 31 email pronte, 0 errori, link CTA in tutte
- CREATE: send_followup_b3.py — follow-up per 37 email B3 multi-nicchia (pazienti/clienti/iscritti per nicchia)
- SCHEDULED: Windows Task "DigitalEmpire_FollowupB3" — esecuzione 2026-05-10 09:00
- UPDATE: prepare_emails.py — aggiunto _aggiungi_cta() + argomenti --csv/--output
- RULE: link CTA obbligatorio in ogni email → https://agency-empire-kohl.vercel.app
- TOTALE OGGI (2026-05-07): 37 email inviate (B3) | 31 pronte per invio (B4)

## [2026-05-07] — Batch 3 multi-nicchia inviato
- SENT: Batch 3 completato — 37/37 email inviate (0 errori) a professionisti italiani multi-nicchia
- NICCHIE: fisioterapista(5), avvocato(8), psicologo(4), palestra(3), yoga(1), estetica(3), spa(1), commercialista(4), medico(7), dentista(1)
- QA: fix triple-newline (4 email), rimozione hallucination "sito si carica lentamente" (4 email), 2 email ricostruite sotto soglia parole
- TOTALE CUMULATIVO: 30 (B1) + 72 (B2) + 37 (B3) = 139 email inviate totali
- UPDATE: send_ready.py — aggiunto flag --auto per invio non-interattivo da background

## [2026-05-07] — Espansione multi-nicchia
- EXPAND: Outreach espanso da dentisti a 8 nicchie (fisioterapisti, avvocati, psicologi, commercialisti, palestre, estetica, studi medici, dentisti)
- CREATE: leads_nuove_nicchie.csv — 37 lead unici estratti da batch 100 righe (63 duplicati rimossi)
- CREATE: prepare_emails.py — generatore AI APSOC+V con mini-dettagli per lead (sito datato, trovato su Instagram, solo WhatsApp, trovato in PDF, ecc.)
- CREATE: send_ready.py — sender da emails_ready.json con conferma interattiva + blacklist
- CREATE: review_emails.py — viewer terminale per revisione pre-invio
- PIPELINE: prepare_emails.py → emails_ready.json → review_emails.py → send_ready.py
- NOTE: email personalizzate al 100%, ogni email è unica — nessun template generico

## [2026-05-07]
- SCHEDULED: Windows Task "DigitalEmpire_FollowupB1" — esecuzione automatica 2026-05-09 09:00 (send_followup_b1.py --auto)
- CREATE: send_followup_b1.py — follow-up batch 1 (29 email, da inviare 2026-05-09/10/11)
- SCHEDULED: Windows Task "DigitalEmpire_FollowupB2" — esecuzione automatica 2026-05-12 09:00 (send_followup_b2.py --auto)
- CREATE: send_followup_b2.py — follow-up batch 2 (72 email, da inviare 2026-05-11/12)
- COPY: Follow-up strategy — ultra-short (<60 parole), domanda binaria, "smetto se risposta è no", stesso oggetto = thread Gmail
- SENT: Batch 2 completato — 72/72 email inviate (0 errori) a studi dentistici italiani
- INGEST: leads_100.csv — 100 lead caricati, 72 unici validi (27 dup rimossi, 1 Doctolib skip)
- CREATE: send_batch2.py — script invio batch 2 (citta da CSV, dedup, blacklist)
- TOTALE CUMULATIVO: 30 (batch 1) + 72 (batch 2) = 102 email dentisti inviate

## [2026-05-07] — precedente
- AUDIT: Email template v1 dentisti analizzato contro APSOC/CPB/Brand Voice → 8 errori identificati
- UPDATE: Template v2 prodotto e deployato in send_now.py (identità mittente + valore educativo + rimozione frasi difensive)
- CREATE: `projects/Outreach/Email_Audit_v1_v2.md` — documentazione completa audit
- CREATE: `agents/apify_leads_finder.py` — nuovo scraper Apollo-alternative (code_crafter/leads-finder, email verificate)
- UPDATE: orchestratore aggiornato con priorità `ApifyLeadsFinder` quando `APIFY_LEADS_FINDER=1`
- NOTE: Account Apify in monthly limit fino a 2026-06-01 — attivare Leads Finder dopo reset

## [2026-05-06] Massive Ingestion & Compilation
- Processed 1283 files across 24 topics.
- Mode: Full Extraction (No synthesis, per user request).
- Ingested & Compiled: index (topic: agency-empire)
- Ingested & Compiled: manifest (topic: agency-empire)
- Ingested & Compiled: manifest (topic: agency-empire)
- Ingested & Compiled: ___netlify-server-handler (topic: agency-empire)
- Ingested & Compiled: __next._full (topic: agency-empire)
- Ingested & Compiled: __next._full (topic: agency-empire)
- Ingested & Compiled: __next._head (topic: agency-empire)
- Ingested & Compiled: __next._head (topic: agency-empire)
- Ingested & Compiled: __next._index (topic: agency-empire)
- Ingested & Compiled: __next._index (topic: agency-empire)
- ... and 1273 more articles.

## [2026-05-06] Massive Ingestion & Compilation
- Processed 1283 files across 24 topics.
- Mode: Full Extraction (No synthesis, per user request).
- Ingested & Compiled: index (topic: agency-empire)
- Ingested & Compiled: manifest (topic: agency-empire)
- Ingested & Compiled: manifest (topic: agency-empire)
- Ingested & Compiled: ___netlify-server-handler (topic: agency-empire)
- Ingested & Compiled: __next._full (topic: agency-empire)
- Ingested & Compiled: __next._full (topic: agency-empire)
- Ingested & Compiled: __next._head (topic: agency-empire)
- Ingested & Compiled: __next._head (topic: agency-empire)
- Ingested & Compiled: __next._index (topic: agency-empire)
- Ingested & Compiled: __next._index (topic: agency-empire)
- ... and 1273 more articles.

## 2026-06-05
- FIX (Instagram Outreach): i DM inviati il 2026-06-04 erano corti/telegrafici, senza link agency e con accenti rotti ("gi�"). Causa: `Instagram Automation/personalize.py` non aggiungeva mai AGENCY_URL (prompt step 6 = solo "Max") e `_pulisci` tagliava tutto dopo "Max"; followup1/2 non passavano nemmeno da `_pulisci`; nessuna normalizzazione accenti prima della digitazione Playwright.
- RISOLTO: aggiunte `_no_accenti()` + `_enforce_chiusura()` (firma "Max" + link agency sotto, deterministico su primo+followup); prompt primo DM riscritto (struttura piena, 55-85 parole, valore, no telegrafico, no accenti, no firma manuale); followup1/2 ora passano da `_pulisci`+`_enforce_chiusura`; fallback e retry-humanizer allineati. Verificato: agency+presentazione+firma presenti, 0 accenti rotti, ~110 parole. → 1 file modificato.
- FIX (Skill /avvia-*): rimosso il flag `--csv leads_verificati.csv` da `/avvia-email` e `/avvia-parallel` (caricava 500 lead già contattati → 0 email nuove). Ora `python run.py --target 500 --mode completo` fa scraping live. Allineati i banner: IG max 30 DM/giorno, LinkedIn 20 connessioni + 20 messaggi + 30 commenti. Verificati tutti gli entrypoint (run.py, scrape_only.py, run_today.py IG/LinkedIn) + compile OK. → 4 skill modificati.

## 2026-06-05 (continuazione)
- FIX CRITICO (Agency URL + Pattern firma IG): l'URL agency era sbagliato (agency-empire-kohl → agency-empire-landing.vercel.app). Aggiornato globalmente in 32 file. INOLTRE: refactor completo della struttura firma Instagram — adesso i DM sono SEPARATI in 2 messaggi: (1) corpo pitch senza firma, (2) link agency nudo (NO "Max", NO struttura firma). `generate_dm/followup1/followup2()` ritornano dict {"corpo": "...", "link_msg": "..."} anziché string. `run_today.py` updated per mandare i 2 messaggi in sequenza. Compile OK, verified. Impatto: Email + LinkedIn rimangono invariati per ora (toccarli dopo). → 2 file refactored (personalize.py, run_today.py).
- COMPLETED: Firma formattata con nome reale (Maximilian - Agency | Digital Empire) + link sito web separato. Pattern finale:
  - IG + LinkedIn: 2 messaggi separati (corpo pitch + firma con link)
  - Email: corpo email classico + firma al fondo nello stesso messaggio
  - Compile OK, test OK → 5 file completi (writer.py, personalize.py IG, run_today.py IG, personalize.py LinkedIn, run_today.py LinkedIn)

## 2026-06-08
- INGEST: nuovo workflow **Empire Studio** (ricostruzione drastica v2.0) → 1 pagina tool creata ([[Empire_Studio]]). Workflow gerarchico per ingerire conoscenza da YouTube/TikTok/Web/Repo, "guardare" davvero i video (frame ffmpeg + visione Claude, no API), forgiare via content-forge e versare nella wiki. 50 agenti a 7 file reali, 20 skill (3 tier), 14 script CLI, validator anti-stub a 0 violazioni, pacchetto Windows-safe estraibile. Nasce dall'audit della chat con l'agente cloud che aveva consegnato in gran parte stub/finto. Posizione: `SKILL & Agenti/Empire Studio Suite/empire-studio/`.
- NUOVA SKILL: **Memory Empire** (always-on) → 1 pagina tool ([[Memory_Empire]]). Memoria viva + router di Digital Empire: carica il contesto, instrada e ATTIVA il workflow giusto (es. Empire Studio quando arriva un link, anche se non parte da solo), archivia ogni contenuto INTEGRALE (mai riassunti) in `~/.claude/skills/memory-empire/knowledge/` + wiki (doppio salvataggio reale via `save_to_memory_empire.py`). Attivazione naturale, nessun comando. 3 agenti: workflow-router, knowledge-keeper, digital-empire-context.
- RIORDINO: Explorer di "Empire Studio Suite" pulito — solo `empire-studio/` (workflow) + `_Riferimenti-e-Archivio/` (repo di riferimento + `_vecchio-tentativo-rotto/`). Attivazione di Empire Studio resa naturale (rimosso `/empire`).
- POTENZIAMENTO [[Memory_Empire]] (v2.0): da 3 a **11 agenti in 4 categorie** (operativi/analizzatori/studiosi/controllori) + nuova capacità reale di **arricchire altre skill** con la conoscenza nuova (es. principi marketing da un video → skill `market-*`), in sicurezza (backup+append+log+rollback). 4 script reali testati (enrich_skill, relevance_scan, audit_log, me_agent_factory). Ciclo arricchimento+rollback provato end-to-end. Registrata ufficialmente come skill always-on.

## 2026-06-10
- INGEST (PIANO MAESTRO): creato dossier **05-ECOSISTEMA-MULTIBUSINESS.md** (446 righe) in `PIANO-MAESTRO/` → 1 pagina creata. Ecosistema L1 #05 di EMPIRE OS: 3 sotto-ecosistemi (YouTube Automation MB-YT prioritario, Publishing/KDP MB-PUB, E-commerce MB-ECOM dormiente). Org L2→L5 completa, roster 28 agenti, pipeline YouTube end-to-end con 4 QA gate per video (script/audio/visual/SEO) + policy gate, multi-canale via swarm (1 canale = 1 brand_kit), pipeline libro KDP che wrappa `Workflow-libri/` (book-factory) senza riscriverlo, 11 skill nuove ordinate alla Forge (yt-niche-research, yt-script-engine, yt-seo-optimizer, thumbnail-factory...), namespace memoria Ruflo `mb/*`, roadmap F-MB1→F-MB7. VINCOLO: F-MB1 = ingestione Empire Studio di @Legamidiamore e @dosementale (non ancora analizzati — zero dati inventati, segnaposto `[da ingestione F-MB1]`).
