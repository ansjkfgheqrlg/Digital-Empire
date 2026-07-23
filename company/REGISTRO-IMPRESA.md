# 🏛️ REGISTRO-IMPRESA — Anagrafe unica degli artefatti (ADR-008)

> **Legge:** nessun artefatto orfano. Ogni riga = proprietario + controllore + origine + governo.
> Manutentore: **Chief-Forge**. Verifica intestazioni: **MAXIMILIAN 5-bis**. Vigilanza: **Sentinelle**.
> Creato 2026-07-19 (direttiva Max). Aggiornare ad ogni creazione — è l'ultimo passo di ogni ciclo FORGE.

---

## 1. ORGANI (il nucleo e il governo)

| Artefatto | Proprietario | Controllore | Origine | Governo (Mandato) |
|---|---|---|---|---|
| ARCHITETTURA (`Genesi-Core/ARCHITETTURA/`) | Genesi Core | Pattern-Guild + 5-bis | dossier 14 | tutto il Mandato (progetta le forme) |
| FORGE (`Genesi-Core/FORGE/`) | Genesi Core | METHOD-GUARD | dossier 14→build | Art. metodo + ADR-008 (ufficio anagrafe) |
| MAXIMILIAN (`MAXIMILIAN/`) | LX (incarna Max) | corpus Maximilian (fedeltà) | dossier 12 | è il gate 5-bis di tutti |
| Mandato (`Mandato/`) | Impero intero | custodi Mandato | dossier 13 | È il governo |
| Board C-Suite (`Board-CSuite/` — CEO, COO, CTO, CMO, CRO, CFO, Chief-Forge) | Impero | 5-bis + CFO budget-guard | blueprint ARCHITETTURA (CP-010) | Art. ruoli/spesa |
| Sentinelle (`Sentinels/`) | Board/COO | MAXIMILIAN | dossier V2 | vigilanza continua |
| Guilds (`Guilds/`) | Board/CTO | 5-bis | dossier V2 | trasversale |
| Memory/Ecosistema 10 (`Memory/`) | Impero | ADR-002 memory-first | dossier 09 | Art. memoria (nessun task senza CP) |
| Ispettorato Generale (`Ispettorato/` — M1+M3 ✅ 11 agenti/5 WF, M2/M4/M5 residui) | MAX (autocritica) | Board/MAXIMILIAN (riceve i report) — indipendente da chi produce | dossier 15 (esteso 2026-07-20: revision-analyst) | Art.2 (verità su di noi, prove non promesse) |

## 2. ECOSISTEMI (STEP 5)

| Ecosistema | Stato | Direttore/Proprietario | Controllore interno | Controllore indipendente |
|---|---|---|---|---|
| 01-AGENCY (10/10 ✅) | vivo | AG-DIR | QA di reparto (ag-aN-qa) | **A10-QA-Cliente** (audita, non costruisce) |
| 02-INFO-BUSINESS (5/5 ✅) | vivo | IB-0-conductor | ib-*-qa per area | 5-bis |
| 03-CONTENT-FACTORY (9/9 ✅) | vivo | CF-R0 Director | QA per reparto | **CF-R6 QA & Gate** (indipendente) |
| 04-MARKETING (6/6 ✅) | vivo | L2-conductor | QA per reparto | 5-bis |
| 05-MULTI-BUSINESS | dossier in scrittura (Gael, Lotto 3) | [da dossier] | — | — |
| 06-CORE (split 4: Platform/Forge/Intelligence/Operations) | dossier in scrittura (Gael) | [da dossier] | — | — |
| 07-BACKBONE · 08-ROADMAP · 09-MEMORY | dossier Lotto 4 ⬜ | — | — | — |

## 3. PRODOTTI & RUNTIME VIVI (fanno soldi o lavorano ORA)

| Artefatto | Proprietario | Controllore | Origine | Governo |
|---|---|---|---|---|
| **PreventivoForge** (+ fabbrica `/nuovo-concessionario`, kill-switch licenze) | 01-AGENCY / A4-Delivery (delivery cliente) + S1/S6 dossier 16 | Gate IMG/R + regole-check + A10 | build Max+Gael (CP-2026070x) | Art.2 (prezzo reale, no invenzioni) · ADR-003 |
| **Outreach Runtime** (email/LinkedIn/IG, 300+/gg) | 01-AGENCY / A2-Acquisizione | **Gate Bibbia** (ag-a2-qa) + rate caps | pre-Impero, wrappato ADR-003 | Art.2 + PII Art.7.2 |
| **Copy Workflow Orchestration Layer** | 04-MARKETING / L2-1 Copywriting | gate copy L2-1-qa | pre-Impero, wrappato | Art.2 |
| **carousel-factory** (brands: mentalita-brutale, …) | 03-CONTENT-FACTORY / CF-R5 | CF-R6 QA & Gate | pre-Impero, wrappato | Art.2 |
| **Empire Studio** (ingestione video → knowledge) | 10-MEMORY (knowledge) + Reparto Competitor Research | WATCH-001 match check | suite dedicata | ADR-002 (integrale, mai riassunti) |
| **Andrei Pascu System** (Playbook + Checklist APSOC 25 item) | 10-MEMORY / 04-MARKETING (knowledge & copy) | Checklist APSOC (score ≥92%) | import da Arena zip 2026-07-22 (ADR-008) | Art.2 (dati reali, zero fuffa) |
| **Manuale Claude Code** (prodotto S2) | 02-INFO-BUSINESS / IB-L2-PROD → VEND | ib-prod-qa + B-003 (prezzo da team-prezzi) | pre-Impero | Art.2 · ADR-005 |
| **EmpireDesk.exe** (in build OGGI, Gael) | 06-CORE/Platform (interim: Genesi-Core) | selftest 8/8 tile + 5-bis | dossier 17 | Art.2 (zero bottoni finti) · ADR-003 (solo launcher) |
| **preventa-maps-scraper** (Playwright Maps Scraper + Sheets) | 01-AGENCY / A2-Acquisizione | A2-QA (ag-a2-qa) | build Arena (19-ARENA-BUILD-LIST) | Art.2 + PII Art.7.2 · ADR-008 |
| **preventa-outreach-pack** (script freddo APSOC concessionari) | 01-AGENCY / A5-Copywriting + S1/S6 | A5-QA (ag-a5-qa) | build Arena (19-ARENA-BUILD-LIST) | Art.2 · ADR-008 |
| **preventa-launch-kit** (Naming + kit lancio B2B concessionari) | 01-AGENCY / A5-Copywriting + S1/S6 | A5-QA (ag-a5-qa) | build Arena (19-ARENA-BUILD-LIST) | Art.2 · ADR-008 |
| **youtube-niche-scout-analysis** (Data-pack canali, pattern, idee e SEO) | 03-CONTENT-FACTORY + 04-MARKETING | checklist_APSOC + niche-gate | build AI/Claude ITA (19-ARENA-BUILD-LIST) | Art.2 + Art.8 · ADR-008 |


## 4. CANALI & PAGINE (dossier 16)

| Canale | Proprietario | Controllore | Stream |
|---|---|---|---|
| pagina IG `mentalita.brutale` | 03-CF / CF-R7 Pubblicazione (pipeline) + 05-MB (P&L) | CF-R6 gate + condizione Max "solo se auto 100%" | S4 |
| pagina IG `crea.illtuo_impero` (+ pagine lancio CCM) | 04-MARKETING (funnel) + 02-INFO (prodotto) | gate copy + audit P0.2 | S3 |
| canali YouTube Fliki (da creare) | 03-CF / WF-YT-* | WF-YT-ANALYZE + gate anti-copia | S5 |
| 7 concessionari (relazioni) | MAX in persona + A7-Account-Management | A10-QA-Cliente | S1 |

## 5. DOSSIER & PIANI ATTIVI

| Dossier | Proprietario | Controllore |
|---|---|---|
| PIANO-MAESTRO 01-15 + V2 | Board/CEO | MAXIMILIAN (fedeltà alla direttiva) |
| 16-PIANO-ESTATE-REVENUE | MAX (business) + CFO (numeri) | metriche §4 misurate, RETRO settimanale |
| 17-EMPIRE-DESK-APP | **MAX** (ownership totale dal 2026-07-21, superata divisione Half A/Half B) | gate §4 dossier 17 |
| `DIGITAL-EMPIRE/` (workflow estate NUOVO, sostituisce planning-workshop+workflows+ESTATE-WORKSHOP*) | MAX (import) → Chief-Forge (build originale) | `DIGITAL-EMPIRE/07-CONTROL/` gates + RETRO-PROTOCOLLO, memory_manager.py |
| `WORKFLOW-ESTATE/` (riorganizzazione 6 pilastri Art.8 del sistema estate) | MAX | ⚠️ **NON CONFORME al 2026-07-22**: pilastri 05/06 vuoti + 26 path rotti (CP-20260722-005) → risanamento assegnato a GEM-04 |
| `company/Antigravity-Briefs/` (GEM-00…GEM-06: pacchetti di lavoro per Gemini/Antigravity) | MAX (committente) | **Claude** (gate 5-bis su ogni consegna in `consegne/`) · Origine: FORGE via Claude, CP-20260722-005 · Governo: MANDATO Art.8 + ADR-002/003/006/008 |
| `empire/` (core runtime Python — **da costruire**, GEM-01) | MAX | Claude (gate) · esecutore GEMINI/Antigravity · Governo: ADR-003 wrap + ADR-008 |

---

<!-- EMPIRE-CENSUS:BEGIN (rigenerato, non modificare a mano) -->
## 6. CENSIMENTO AUTOMATICO DEGLI ARTEFATTI MAGGIORI (FORGE / census.py)

| Tipo | Path | Proprietario (Owner) | Controllore | Origine | Governo | CF-Grade |
|---|---|---|---|---|---|---|
| `agent` | `DIGITAL-EMPIRE/04-AGENTS/YT-AGENT-PACK.md` | — | — | — | — | — |
| `agent` | `DIGITAL-EMPIRE/04-AGENTS/chief-forge/tools.md` | — | — | — | — | — |
| `agent` | `DIGITAL-EMPIRE/04-AGENTS/memory-architect/tools.md` | — | — | — | — | — |
| `agent` | `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/AGENTE-MAX.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A1-Ricerca/agenti/ag-a1-scrape.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A10-QA-Cliente/agenti/ag-a10-uat.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A2-Acquisizione/agenti/ag-a2-write.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A3-Preventivi/agenti/ag-a3-qa.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A4-Delivery/agenti/ag-a4-uat.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A5-Copywriting-Interno/agenti/ag-a5-write.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A6-Marketing-Interno/agenti/ag-a6-upsell.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A7-Account-Management/agenti/ag-a7-qa.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A8-Closing/agenti/ag-a8-script.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/01-AGENCY/Reparti/A9-Partnership-Referral/agenti/ag-a9-qualify.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-WEBINAR-host.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-COMM-Community-Retention/agenti/ib-coord-community.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/agenti/IB-LANC-WEBINAR.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-PROD-Produzione-Prodotti/agenti/ib-prod-writer.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-STRA-Strategia-Intelligence/agenti/ib-stra-roadmap-builder.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-VEND-Vendite-Funnel/agenti/ib-vend-track.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Agenti/CF-R2-A07-voiceover.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R0-Director/agenti/cf-d-status.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R1-Strategia-Brief/agenti/cf-r1-trend.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R2-Brand-Kit-Registry/agenti/cf-r2-qa.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R3-Produzione-Video/agenti/cf-r3-vo.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R4-Produzione-Testuale/agenti/cf-r4-write.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R5-Visual-Design-Caroselli/agenti/cf-r5-slidecopy.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R6-QA-Gate/agenti/cf-r6-rework.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R7-Pubblicazione/agenti/cf-r7-yt.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R8-Apprendimento/agenti/cf-r8-reasoning.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Agenti/SEN-BV-brand-voice-sentinel.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting/agenti/copy-qa-lead.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Reparti/L2-2-Advertising/agenti/ads-lead.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Reparti/L2-3-Email-Lifecycle/agenti/email-lead.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Reparti/L2-4-Analytics/agenti/an5-funnel-analyst.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Reparti/L2-5-Brand-Creative-Strategy/agenti/brand-lead.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/04-MARKETING/Reparti/L2-6-Conversion-Architecture/agenti/conv-lead.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/05-MULTI-BUSINESS/Agenti/MB-YT-A09-opt-coord.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ecosistemi/06-PLATFORM/Agenti/plt-site-copy-merger.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/07-FORGE/Agenti/frg-spec-writer.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/08-INTELLIGENCE/Agenti/INT-A03-int-librarian.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/09-OPERATIONS/Agenti/ops-watchdog.md` | — | — | — | — | — |
| `agent` | `company/Ecosistemi/10-MEMORY/Agenti/ME-A10-memory-sentinel.md` | — | — | — | — | — |
| `agent` | `company/Genesi-Core/ARCHITETTURA/Agenti/arch-validator.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Genesi-Core/FORGE/Agenti/frg-spec-writer.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `company/Ispettorato/agenti/isp-verifier.md` | — | — | — | — | — |
| `agent` | `company/MAXIMILIAN/Agenti/MX-VISION.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `agent` | `second-brain-vault/raw/Agenti/2026-05-06-struttura.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/2026-05-06-requirements.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/agents/2026-05-06-market-technical.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/orchestrator/2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/output/2026-05-06-test-pdf.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/outreach/2026-05-06-script-chiamata-freddo.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/outreach/rules/2026-05-06-06-ricerca-ai-prospects.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/outreach/rules/2026-05-06-06-ricerca-ai-prospects.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/sub-agents/ai-implementation/2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/sub-agents/cro-funnel/2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/raw/Agenti/Agency/sub-agents/no-website/2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/(Agenti) 2026-05-06-struttura.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/(Agency) 2026-05-06-requirements.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/agents/(agents) 2026-05-06-market-technical.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/orchestrator/(orchestrator) 2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/output/(output) 2026-05-06-test-pdf.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/outreach/(outreach) 2026-05-06-script-chiamata-freddo.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/outreach/rules/(rules) 2026-05-06-06-ricerca-ai-prospects.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/outreach/rules/(rules) 2026-05-06-06-ricerca-ai-prospects.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/sub-agents/ai-implementation/(ai-implementation) 2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/sub-agents/cro-funnel/(cro-funnel) 2026-05-06-agent.md` | — | — | — | — | — |
| `agent` | `second-brain-vault/wiki/03 - Resources/Knowledge_Base/Agenti/Agency/sub-agents/no-website/(no-website) 2026-05-06-agent.md` | — | — | — | — | — |
| `dashboard` | `Clienti/Prof Autocad/preventivo-forge/dist/PreventivoForge/_internal/playwright/driver/package/lib/vite/dashboard/index.html` | — | — | — | — | — |
| `dashboard` | `DIGITAL-EMPIRE/07-CONTROL/DASHBOARD-E-RETRO.md` | — | — | — | — | — |
| `dashboard` | `DIGITAL-EMPIRE/07-CONTROL/DASHBOARD-E-RETRO.md` | — | — | — | — | — |
| `dashboard` | `DIGITAL-EMPIRE/07-CONTROL/DASHBOARD-E-RETRO.md` | — | — | — | — | — |
| `dashboard` | `DIGITAL-EMPIRE/07-CONTROL/DASHBOARD-E-RETRO.md` | — | — | — | — | — |
| `dashboard` | `SKILL & Agenti/Workflow agency creative/caroselli - agency/dashboard. Produzione caroselli Agency/tsconfig.json` | — | — | — | — | — |
| `dashboard` | `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/KPI-SISTEMA.md` | Max | Claude | FORGE (GEM-04) | MANDATO Art.8 + ADR-008 | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/README.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/agenti/ceo-verificatore.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/kpi/KPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/principi/PRINCIPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/regole/REGOLE.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/scripts/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/skills/SKILLS.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CEO-Empire-Conductor/workflow/WF-REVIEW-TRIMESTRALE.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CFO/README.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CFO/agenti/cfo-tier-router.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CFO/kpi/KPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CFO/principi/PRINCIPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CFO/regole/REGOLE.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CFO/scripts/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CFO/skills/SKILLS.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CFO/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CFO/workflow/WF-SPEND-APPROVAL.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/README.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/agenti/cmo-performance-analyst.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/kpi/KPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/principi/PRINCIPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/regole/REGOLE.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/scripts/README.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/skills/SKILLS.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CMO/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CMO/workflow/WF-LANCIO-COORD.md` | ** cmo-launch-coordinator | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/COO/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/agenti/coo-sync-keeper.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/kpi/KPI.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/principi/PRINCIPI.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/regole/REGOLE.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/scripts/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/skills/SKILLS.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/COO/workflow/WF-OPS-DAILY.md` | ** coo-conductor | — | — | — | — |
| `department` | `company/Board-CSuite/CRO/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CRO/agenti/cro-retention-revenue.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CRO/kpi/KPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CRO/principi/PRINCIPI.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CRO/regole/REGOLE.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CRO/scripts/README.md` | ** `cro-pipeline-health` | — | — | — | — |
| `department` | `company/Board-CSuite/CRO/skills/SKILLS.md` | ** `cro-deal-desk` | — | — | — | — |
| `department` | `company/Board-CSuite/CRO/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CRO/workflow/WF-PRICING.md` | ** `cro-conductor` | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/agenti/cto-tech-debt-tracker.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/CTO/kpi/KPI.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/principi/PRINCIPI.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/regole/REGOLE.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/scripts/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/skills/SKILLS.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/CTO/workflow/WF-TECH-REVIEW.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/README.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/Chief-Forge/agenti/cf-skill-portfolio.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/kpi/KPI.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/principi/PRINCIPI.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/regole/REGOLE.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/Chief-Forge/scripts/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/skills/SKILLS.md` | ** `cf-intake-router` | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/state/README.md` | — | — | — | — | — |
| `department` | `company/Board-CSuite/Chief-Forge/workflow/WF-HR-REGISTRY.md` | `cf-conductor` + `cf-agent-registry` | — | — | — | — |
| `department` | `company/Board-CSuite/README.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/_BLUEPRINT/BP-INDEX.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `department` | `company/Board-CSuite/_BLUEPRINT/BP-INDEX.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `ecosystem` | `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Ecosistemi/05-MULTI-BUSINESS/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md` | — | — | — | ** Security Sentinel supervisiona ogni build; zero segreti in git | — |
| `ecosystem` | `company/Ecosistemi/07-FORGE/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Ecosistemi/08-INTELLIGENCE/ECOSISTEMA.md` | — | — | — | ** wiki-sync-guard garantisce che ogni operazione loggi in wiki/log.md | — |
| `ecosystem` | `company/Ecosistemi/09-OPERATIONS/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Ecosistemi/10-MEMORY/ECOSISTEMA.md` | — | — | — | — | — |
| `ecosystem` | `company/Genesi-Core/ARCHITETTURA/ECOSISTEMA.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `ecosystem` | `company/Genesi-Core/FORGE/ECOSISTEMA.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `ecosystem` | `company/MAXIMILIAN/ECOSISTEMA.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `Agenti/Agency/skills/market-ads/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-audit/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-brand/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-competitors/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-copy/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-emails/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-funnel/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-landing/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-launch/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-proposal/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-report-pdf/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-report/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-seo/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-social/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market-social/SKILL.md` | — | — | — | — | — |
| `skill` | `Agenti/Agency/skills/market/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/Prof Autocad/preventivo-forge/dist/PreventivoForge/_internal/playwright/driver/package/lib/tools/cli-client/skill/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ab-testing/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ab-testing/references/test-templates.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ad-creative/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ad-creative/references/platform-specs.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ads/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ads/references/platform-setup-checklists.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ai-seo/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/ai-seo/references/platform-ranking-factors.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/analytics/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/analytics/references/gtm-implementation.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/aso/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/aso/references/scoring-criteria.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/churn-prevention/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/churn-prevention/references/dunning-playbook.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/co-marketing/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/cold-email/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/cold-email/references/subject-lines.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/community-marketing/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/competitor-profiling/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/competitor-profiling/references/tool-reference.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/competitors/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/competitors/references/templates.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/content-strategy/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/content-strategy/references/headless-cms.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/copy-editing/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/copy-editing/references/plain-english-alternatives.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/copywriting/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/copywriting/references/natural-transitions.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/cro/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/cro/references/form.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/customer-research/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/customer-research/references/source-guides.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/directory-submissions/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/emails/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/emails/references/sequence-templates.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/free-tools/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/free-tools/references/tool-types.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/image/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/image/references/ai-image-prompting.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/launch/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/lead-magnets/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/lead-magnets/references/format-guide.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/marketing-ideas/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/marketing-ideas/references/ideas-by-category.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/marketing-psychology/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/onboarding/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/onboarding/references/experiments.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/paywalls/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/paywalls/references/experiments.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/popups/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/pricing/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/pricing/references/tier-structure.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/product-marketing/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/programmatic-seo/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/programmatic-seo/references/playbooks.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/referrals/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/referrals/references/program-examples.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/revops/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/revops/references/scoring-models.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/sales-enablement/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/sales-enablement/references/one-pager-templates.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/schema/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/schema/references/schema-examples.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/seo-audit/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/seo-audit/references/international-seo.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/signup/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/site-architecture/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/site-architecture/references/site-type-templates.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/sms/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/sms/references/sequence-templates.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/social/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/social/references/short-form-video.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/video/SKILL.md` | — | — | — | — | — |
| `skill` | `Clienti/marketingskills-main/skills/video/references/ai-video-prompting.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/_INDEX.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/brand-guidelines/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/canvas-design/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/frontend-design/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-ads/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-audit/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-brand/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-competitors/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-copy/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-emails/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-funnel/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-landing/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-launch/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-proposal/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-report-pdf/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-report/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-seo/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market-social/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/market/scripts/social_calendar.py` | — | — | — | — | — |
| `skill` | `Crea siti/skills/omega-create/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/opus/TYPOGRAPHY-SYSTEM.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-3d/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-animate/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-brief/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-build/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-components/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-copy/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-deploy/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-design/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-plan/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-qa/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-report/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-seo/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site-stack/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/site/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/skill-creator/SKILL.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/skill-creator/agents/grader.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/skill-creator/references/schemas.md` | — | — | — | — | — |
| `skill` | `Crea siti/skills/skill-creator/scripts/__init__.py` | — | — | — | — | — |
| `skill` | `Crea siti/skills/theme-factory/themes/tech-innovation.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/SKILL-REGISTRY.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/SKILL.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/builders/workflow-builder-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/conductor.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/meta/question-designer-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/optimizers/skill-depth-agent.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/pipeline/target-advisor-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/qa/target-schema-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/self-improvement/triage-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/agents/self-improvement/triage-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/_shared/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/_shared/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/custom/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/doc/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/orchestration/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/skill/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/team/topology.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/wiki/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/wiki/_meta/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/wiki/concepts/structured-output.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/wiki/frameworks/istruzioni-vaghe.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/examples/workflow/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/failure-modes-log/TEMPLATE.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/HANDOFF.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/SKILL.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/builders/workflow-builder-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/conductor.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/meta/question-designer-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/optimizers/skill-depth-agent.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/pipeline/target-advisor-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/qa/target-schema-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/agents/qa/target-schema-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/_shared/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/_shared/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/custom/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/doc/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/orchestration/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/skill/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/team/topology.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/wiki/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/wiki/_meta/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/wiki/concepts/structured-output.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/wiki/frameworks/istruzioni-vaghe.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/assets/examples/workflow/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/references/conventions/naming.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/references/external/skill-creator.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/references/patterns/P9-target-shape-mapping.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/references/processes/workflow.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/references/schemas/workflow.schema.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/references/stages/09-packaging.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/scripts/lib/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/scripts/tests/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.1/content-forge/scripts/validate_dag.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/HANDOFF.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/SKILL.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/builders/workflow-builder-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/conductor.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/meta/question-designer-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/optimizers/skill-depth-agent.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/pipeline/target-advisor-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/qa/target-schema-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/self-improvement/triage-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/agents/self-improvement/triage-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/_shared/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/_shared/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/custom/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/doc/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/orchestration/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/skill/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/team/topology.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/wiki/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/wiki/_meta/source.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/wiki/concepts/structured-output.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/wiki/frameworks/istruzioni-vaghe.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/assets/examples/workflow/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/failure-modes-log/TEMPLATE.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/failure-modes-log/TEMPLATE.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/failure-modes-log/TEMPLATE.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/failure-modes-log/TEMPLATE.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/failure-modes-log/TEMPLATE.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/references/conventions/naming.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/references/external/skill-creator.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/references/patterns/P9-target-shape-mapping.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/references/processes/workflow.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/references/schemas/workflow.schema.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/references/stages/10-self-improvement.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/scripts/lib/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/scripts/tests/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/scripts/tests/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/packaged-final-v1.2/content-forge/scripts/validate_dag.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/references/conventions/naming.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/references/external/skill-creator.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/references/patterns/P9-target-shape-mapping.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/references/processes/workflow.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/references/schemas/workflow.schema.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/references/stages/10-self-improvement.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/scripts/lib/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/scripts/tests/__init__.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/scripts/validate_dag.py` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/SKILL.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/CATALOG.md` | — | ** | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/CATALOG.md` | — | ** | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/builders/agent-spec-builder/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/builders/memory-ecosystem-builder/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/builders/plan-builder/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/builders/swarm-builder/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/conductor/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/conductor/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/anti-pattern-hunter/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/case-study-analyst/tools.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/context-boundary-architect/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/patterns-manager/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/principle-codifier/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/principles-manager/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/ruflo-swarm-extractor/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/topology-designer/topology-designer.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/domain/topology-designer/topology-designer.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/optimizers/skill-depth-agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/optimizers/skill-depth-agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/pipeline/ingestion-agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/pipeline/ingestion-agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/qa/coverage-verifier-agent/coverage-verifier-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/qa/failure-mode-validator-agent/failure-mode-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/qa/target-schema-validator-agent/target-schema-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/qa/target-schema-validator-agent/target-schema-validator-agent.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/self-improvement/failure-detector-agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/agents/self-improvement/failure-detector-agent/tools.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/memory/MEMORY-INDEX.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/memory/checkpoints/CP-025-cp-025_-autonomous-turn-complete.-priority-1-done,-2026-06-03T170542.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/memory/decisions/DEC-updated-analysis-and-catalog-with-real-fs-audit-2026-06-04T102215.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/memory/plans/PLAN-v1-master-architect-creation.md` | ** Conductor + Plan-Builder (this process). | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/memory/sessions/SES-001-initial-setup-2026-06-03.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/packaged/README.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/references/KP-PLAN.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/references/knowledge-pack/01-principles/P15-trigger-design-as-product-design.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/references/knowledge-pack/02-patterns/PT11-validation-with-auto-fix.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/references/knowledge-pack/06-case-studies/CS04-bugs-found-in-real-test.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/references/knowledge-pack/08-glossary/glossary.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/references/knowledge-pack/KP-PLAN.md` | — | — | — | — | — |
| `skill` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/scripts/memory_manager.py` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `KDP - prodottti digitali/Progetto KDP su Claude Code/SKILL/skill.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/apsoc-builder/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/apsoc-builder/agents/apsoc-conductor.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/apsoc-builder/agents/apsoc-conductor.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/apsoc-builder/references/sezione-per-sezione.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/copy-review/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/copy-review/agents/reviewer-agent.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/copy-review/agents/reviewer-agent.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/copy-review/references/scoring-guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/funnel-designer/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/funnel-designer/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/funnel-designer/references/funnel-economics.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/headline-forge/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/headline-forge/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/headline-forge/references/headline-per-contesto.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/objections-forge/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/objections-forge/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/objections-forge/assets/examples/cpb-ho-gia-provato.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/objections-forge/references/obiezioni-per-settore.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/target-avatar/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/target-avatar/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/target-avatar/assets/examples/avatar-giulia.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/skills/target-avatar/references/research-methods.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/content-ingest-ecosystem/skills/content-forge-wrapper-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/content-ingest-ecosystem/skills/video-watcher-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/content-ingest-ecosystem/skills/video-watcher-skill/scripts/playwright_video_watcher.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/content-ingest-ecosystem/skills/yt-ingest-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/empire-studio/skills/content-forge-wrapper-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/empire-studio/skills/video-watcher-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/empire-studio/skills/video-watcher-skill/scripts/playwright_video_watcher.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/empire-studio/skills/yt-ingest-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/home/user/empire-studio/skills/atomic-note-creator-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/home/user/empire-studio/skills/frame-extractor-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/home/user/empire-studio/skills/memory-checkpoint-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/home/user/empire-studio/skills/repo-parser-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/home/user/empire-studio/skills/strategy-manifest-applicator-skill/SKILL.md` | — | — | — | MANDATO-EMPIRE.md | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/home/user/empire-studio/skills/visual-analyzer-skill/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animated-component-libraries/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animated-component-libraries/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animated-component-libraries/references/react_bits_components.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animated-component-libraries/scripts/props_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animejs/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animejs/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animejs/references/timeline_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/animejs/scripts/timeline_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/lottie-animations/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/lottie-animations/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/lottie-animations/assets/starter_lottie/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/lottie-animations/references/performance_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/lottie-animations/scripts/optimize_lottie.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/react-spring-physics/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/react-spring-physics/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/react-spring-physics/references/react_spring_api.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/react-spring-physics/scripts/spring_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/scroll-reveal-libraries/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/scroll-reveal-libraries/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/scroll-reveal-libraries/references/aos_api.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/scroll-reveal-libraries/scripts/config_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/animation-components/skills/scroll-reveal-libraries/scripts/config_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/blender-web-pipeline/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/blender-web-pipeline/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/blender-web-pipeline/references/optimization_strategies.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/blender-web-pipeline/scripts/optimize_model.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/rive-interactive/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/rive-interactive/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/rive-interactive/references/api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/rive-interactive/scripts/viewmodel_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/spline-interactive/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/spline-interactive/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/spline-interactive/references/api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/spline-interactive/scripts/project_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/substance-3d-texturing/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/substance-3d-texturing/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/substance-3d-texturing/references/python_api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/substance-3d-texturing/scripts/web_optimizer.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/authoring-motion/skills/substance-3d-texturing/scripts/web_optimizer.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/babylonjs-engine/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/babylonjs-engine/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/babylonjs-engine/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/babylonjs-engine/references/api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/babylonjs-engine/scripts/scene_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/gsap-scrolltrigger/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/gsap-scrolltrigger/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/gsap-scrolltrigger/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/gsap-scrolltrigger/references/easing_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/gsap-scrolltrigger/scripts/timeline_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/motion-framer/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/motion-framer/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/motion-framer/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/motion-framer/references/api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/motion-framer/scripts/variant_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/react-three-fiber/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/react-three-fiber/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/react-three-fiber/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/react-three-fiber/references/api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/react-three-fiber/scripts/scene_setup.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/threejs-webgl/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/threejs-webgl/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/threejs-webgl/assets/starter_scene/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/threejs-webgl/references/optimization_checklist.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/threejs-webgl/scripts/setup_scene.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/core-3d-animation/skills/threejs-webgl/scripts/setup_scene.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/aframe-webxr/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/aframe-webxr/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/aframe-webxr/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/aframe-webxr/references/webxr_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/aframe-webxr/scripts/scene_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/barba-js/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/barba-js/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/barba-js/references/transition_patterns.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/barba-js/scripts/transition_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/lightweight-3d-effects/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/lightweight-3d-effects/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/lightweight-3d-effects/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/lightweight-3d-effects/references/zdog_api.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/lightweight-3d-effects/scripts/setup_vanta.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/locomotive-scroll/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/locomotive-scroll/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/locomotive-scroll/references/gsap_integration.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/locomotive-scroll/scripts/integration_helper.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/pixijs-2d/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/pixijs-2d/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/pixijs-2d/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/pixijs-2d/references/performance_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/pixijs-2d/scripts/sprite_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/playcanvas-engine/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/playcanvas-engine/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/playcanvas-engine/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/playcanvas-engine/references/optimization_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/playcanvas-engine/scripts/project_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/extended-3d-scroll/skills/playcanvas-engine/scripts/project_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/modern-web-design/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/modern-web-design/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/modern-web-design/references/performance_checklist.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/modern-web-design/scripts/pattern_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/web3d-integration-patterns/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/web3d-integration-patterns/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/bundles/meta-skills/skills/web3d-integration-patterns/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/aframe-webxr/skills/aframe-webxr/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/aframe-webxr/skills/aframe-webxr/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/aframe-webxr/skills/aframe-webxr/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/aframe-webxr/skills/aframe-webxr/references/webxr_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/aframe-webxr/skills/aframe-webxr/scripts/scene_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/aframe-webxr/skills/aframe-webxr/scripts/scene_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animated-component-libraries/skills/animated-component-libraries/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animated-component-libraries/skills/animated-component-libraries/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animated-component-libraries/skills/animated-component-libraries/references/react_bits_components.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animated-component-libraries/skills/animated-component-libraries/scripts/props_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animated-component-libraries/skills/animated-component-libraries/scripts/props_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animejs/skills/animejs/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animejs/skills/animejs/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animejs/skills/animejs/references/timeline_guide.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animejs/skills/animejs/scripts/timeline_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/animejs/skills/animejs/scripts/timeline_builder.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/babylonjs-engine/skills/babylonjs-engine/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/babylonjs-engine/skills/babylonjs-engine/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/babylonjs-engine/skills/babylonjs-engine/assets/examples/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/babylonjs-engine/skills/babylonjs-engine/references/api_reference.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/babylonjs-engine/skills/babylonjs-engine/scripts/scene_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/babylonjs-engine/skills/babylonjs-engine/scripts/scene_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/barba-js/skills/barba-js/SKILL.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/barba-js/skills/barba-js/assets/README.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/barba-js/skills/barba-js/references/transition_patterns.md` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/barba-js/skills/barba-js/scripts/transition_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/barba-js/skills/barba-js/scripts/transition_generator.py` | — | — | — | — | — |
| `skill` | `SKILL & Agenti/Empire Studio Suite/_Riferimenti-e-Archivio/claudedesignskills/plugins/individual/blender-web-pipeline/skills/blender-web-pipeline/SKILL.md` | — | — | — | — | — |
<!-- EMPIRE-CENSUS:END -->

## Regola di chiusura (da ADR-008)

**Creato qualcosa di nuovo?** → riga QUI (se maggiore) o in `skills-map.yaml` (se skill/WF/tool)
→ poi il 5-bis può approvare. Ordine inverso = violazione.
