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
| Ispettorato Generale (dossier 15) | MAX (autocritica) | sé stesso su Max | dossier 15 | Art.2 (verità su di noi) |

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
| **Copy Workflow Orchestration Layer** (`copy-workflow/`, motore APSOC 8 agenti + wrapper `.claude/skills/copy-workflow`) | 04-MARKETING / L2-1 Copywriting | gate copy L2-1-qa | pre-Impero, wrappato → **vendor ufficiale ADR-009 (2026-07-20)** | Art.2 |
| **content-forge2.0** (`content-forge2.0/`, motore `/forge` + wrapper `.claude/skills/content-forge`) | FORGE-AGENT-SKILL (06b-FORGE) | fas-qa-gate | vendor ufficiale ADR-009 | Art.2 · ADR-003 (diff vendor=0) |
| **master-build-architecture** (`master-build-architecture/`, metodo architetture + wrapper `.claude/skills/master-build-architecture`) | 06b-FORGE / L2.4 ECOSYSTEM-WORKS + L2.5 METHOD-GUARD | METHOD-GUARD | vendor (versione main, ADR-009) | Art.2 · ADR-003 |
| **Reparto FORGE-AGENT-SKILL** (officina agenti & skill: 4 agenti fas-*, WF-AGENT/SKILL-NEW) | 06b-FORGE (L2.1/L2.2) | fas-qa-gate + METHOD-GUARD | ADR-009 (2026-07-20) | ADR-001/002/006/008 |
| **Toolchain VS Code** (`.vscode/` condiviso + dossier `PIANO-MAESTRO/19-TOOLCHAIN-VSCODE.md`; Tier 1-3, agente = Claude Code unico) | 06b-FORGE / L2.4 ECOSYSTEM-WORKS | METHOD-GUARD + 5-bis campionario | ordine Max 2026-07-20 (CP-20260720-003) | ADR-002/003/006/008 (niente format-on-save, niente tool orfani) |
| **carousel-factory** (brands: mentalita-brutale, …) | 03-CONTENT-FACTORY / CF-R5 | CF-R6 QA & Gate | pre-Impero, wrappato | Art.2 |
| **Empire Studio** (ingestione video → knowledge) | 10-MEMORY (knowledge) + Reparto Competitor Research | WATCH-001 match check | suite dedicata | ADR-002 (integrale, mai riassunti) |
| **Manuale Claude Code** (prodotto S2) | 02-INFO-BUSINESS / IB-L2-PROD → VEND | ib-prod-qa + B-003 (prezzo da team-prezzi) | pre-Impero | Art.2 · ADR-005 |
| **EmpireDesk.exe** (in build OGGI, Gael) | 06-CORE/Platform (interim: Genesi-Core) | selftest 8/8 tile + 5-bis | dossier 17 | Art.2 (zero bottoni finti) · ADR-003 (solo launcher) |

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
| 17-EMPIRE-DESK-APP | Gael (build) | gate §4 dossier 17 |
| 19-TOOLCHAIN-VSCODE | L2.4 ECOSYSTEM-WORKS (FORGE) | METHOD-GUARD; gate §8 dossier 19 (verificato 2026-07-20) |

---

## Regola di chiusura (da ADR-008)

**Creato qualcosa di nuovo?** → riga QUI (se maggiore) o in `skills-map.yaml` (se skill/WF/tool)
→ poi il 5-bis può approvare. Ordine inverso = violazione.
