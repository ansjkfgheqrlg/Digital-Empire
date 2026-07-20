# 18 — ARCHITETTURA IMPERO: REVISIONE CON MASTER-BUILD-ARCHITECTURE

> Revisione architetturale trasversale di Digital Empire applicando la skill
> `master-build-architecture` (motore: `master-build-architecture/`, ADR-009).
> Data: 2026-07-20 · Autore: sessione Claude · Committente: Max.
> **Premessa vincolante (direttiva Max):** Digital Empire NON è un workflow. È un IMPERO CON PIÙ WORKFLOW.
> Ogni valutazione qui sotto tratta quindi i workflow come unità VIVE dentro reparti → ecosistemi → holding
> (EMPIRE OS v1/V2, ADR-001). Nessun workflow orfano; ogni miglioria ha intestazione ADR-008.
> Metodo applicato: 10 invarianti della skill come CHECKLIST di audit + failure-modes-first + MKD.

---

## 0. SINTESESE (MKD ridotta della revisione)

L'impero ha già le tre gambe portanti che la skill prescrive: **memory-first** (`company/Memory/`, ADR-002 ✅),
**ciclo di fase a 9 passi con gate** (ADR-006 ✅), **wrap non riscrittura** (ADR-003 ✅).
I gap sistemici trovati sono quattro: (1) gli agenti dei workflow storici NON seguono tutti lo standard
7-file canonici; (2) failure-modes non è di prima classe ovunque (c'è dove dominate dagli errori: REGISTRO-ERRORI
solo in PreventivoForge/EmpireDesk); (3) traceability sorgente→output non uniforme fuori da Empire Studio;
(4) finora mancava un'officina permanente che producesse agenti/skill → **chiusa oggi con FORGE-AGENT-SKILL**.
Ogni gap diventa miglioria MIR-w (Miglioria Impero Workflow) con owner e gate, non "note sparse".

---

## 1. AUDIT PER INVARIANTE (le 10 gambe della skill sull'impero)

| # | Invariante | Stato impero | Miglioria |
|---|---|---|---|
| 1 | Memory-first dal passo zero | ✅ ADR-002 + Memory ecosystem (checkpoint/ADR/BACKLOG) | MIR-1: estendere memory/ locale ai runtime che non ce l'hanno (outreach, carousel-factory): INDEX.md + 1 riga per run |
| 2 | MKD + mai riassunti | ✅ solo Empire Studio (videos→pagine complete) | MIR-2: adottare `/forge` (MKD) per ogni nuova ingestione; candidata: `Materiale Agency - Diglital Empire.txt` → MKD brand-offer |
| 3 | PLAN→ASK→BUILD→CRITIQUE→ITERATE | ✅ **closed 2026-07-20 (MIR-3, CP-20260720-009)**: ASK formale obbligatorio in ogni FORGE-PLAN del reparto — `FORGE-AGENT-SKILL/workflows/ASK-PROTOCOL.md` + step ASK nelle 2 WF + qa-gate punto 7 | (chiuso) |
| 4 | Tre livelli: kernel/specialisti/tools | ✅ su copy-workflow (8 agenti A1-A8) e content-forge | MIR-4: mappare i runtime "monolitici" (app.py EmpireDesk) verso kernel+moduli (già avviato da §5 dossier 17: seam modules/) |
| 5 | 7 file canonici per agente | ⚠️ 01-AGENCY/02/03/04 li hanno (CF-grade); i runtime pre-impero NO | MIR-5: via FORGE-AGENT-SKILL, retrofit progressivo (1 reparto-figlio per sprint) — backorder, nessuna fretta (ADR-003) |
| 6 | Failure-modes di prima classe | ⚠️ solo PreventivoForge/EmpireDesk hanno REGISTRO-ERRORI | MIR-6: REGISTRO-ERRORI.md obbligatorio in ogni runtime attivo (outreach, carousel, YouTube kit) — regola già Max 07-05, ora standardizzata |
| 7 | Traceability sorgente→output | ✅ Empire Studio (P12); ⚠️ altrove manuale | MIR-7: ogni FORGE-PLAN dichiara sorgenti; coverage-check nei gate (fas-qa-gate lo fa) |
| 8 | Research→Plan→Reset→Implement | ✅ praticato (swarm fresh per fasi) | MIR-8: codificarlo nel ciclo a 9 passi come nota metodo (no ADR nuovo) |
| 9 | Swarm (hier/mesh/pipeline) | ✅ **closed 2026-07-20 (MIR-9, CP-20260720-013)**: `topology.md` obbligatorio per team ≥2 agenti (R2-bis + template + gate) — dogfooding: `FORGE-AGENT-SKILL/TOPOLOGY.md` | (chiuso) |
| 10 | Meta-ricorsione (skill che fa skill) | ✅ OGGI: FORGE-AGENT-SKILL + content-forge + master-build-architecture | MIR-10: prima auto-applicazione: retrofit MIR-5 guidato dal reparto stesso |

---

## 2. I WORKFLOW DELL'IMPERO COM'È OGGI (mappa viva, con miglioria prioritaria)

| # | Workflow/Ecosistema parallelo | Sede | Qualità architetturale | Miglioria #1 |
|---|---|---|---|---|
| W1 | Outreach (email/LinkedIn/IG, 300+/gg) | `Outreach/` | runtime legacy wrappato ✅ | MIR-1+6: memory/ locale + REGISTRO-ERRORI |
| W2 | **Copy** (APSOC 8 agenti) | `copy-workflow/` (OGGI ufficiale) | CF-grade ⭐ | MIR-2: usarlo su OGNI copy (regola attiva) |
| W3 | PreventivoForge (cliente) | `Clienti/Prof Autocad/` | CF-grade + gate + registro errori ⭐ | pattern di riferimento per gli altri |
| W4 | Content / carousel-factory | `Workfolw crea caroselli à/` | runtime wrappato | MIR-6: registro errori + selftest tile EmpireDesk |
| W5 | Empire Studio (ingest video) | `SKILL & Agenti/` | CF-grade + WATCH-001 ⭐ | — |
| W6 | EmpireDesk (launcher) | `EmpireDesk/` | in build (B0/B1 da ordine Max) | seam modules/ = gambino 4 ✅ in corso (governance altro owner) |
| W7 | **YouTube Lead Machine** | `Formazzione/Youtube/` | strategia+kit ✅ (CP-20260719-009, CP-20260720-011) | MIR-11: ✅ skill `/youtube-lead-machine` FORGIATA (CP-20260720-005, GATE 7/7); agenti yt-* in valutazione superfluità (deleghe attive) |
| W8 | **FORGE-AGENT-SKILL** (OGGI) | `FORGE-AGENT-SKILL/` | reparto nuovo CF-grade | — (è il MIR-maker degli altri) |
| W9 | Manuale CC (prodotto S2) | `02-INFO-BUSINESS` | CF-grade | vendita: copy review via copy-workflow |
| W10 | Pagine lancio / agency sites | `Agency page*/`, `agency-empire*/` | siti statici | MIR-12: ✅ review APSOC fatta 2026-07-20 (`COPY-REVIEW-APSOC-SITO.md`, 78/100; patch P0 = corsia Max) |

**Nota coordination:** W6 ha owner divisione Max/Gael (ordine in STATO-EMPIRE). Questa revisione NON tocca
codice/cantiere aperto di altri owner — produce solo le migliorie MIR su asset non in cantiere altrui.

---

## 3. LE 12 MIGLIORIE (azioni, owner, gate)

| ID | Azione | Owner | Gate | Priorità |
|---|---|---|---|---|
| MIR-1 | memory/ locale (INDEX.md) nei runtime W1, W4 | FORGE-AGENT-SKILL (via richiesta eco) | fas-qa-gate | P2 — ✅ FATTA 2026-07-20 (Outreach/ + carousel-factory/ memory/INDEX.md) |
| MIR-2 | Copy obbligatorio via copy-workflow (regola attiva da oggi) + MKD brand-offer da `Materiale Agency` | 04-MARKETING/L2-1 | A8 review ≥85 | **P0 ✅ entrambe 2026-07-20: kit YouTube review + MKD-brand-offer-DE.md** |
| MIR-3 | ASK formale nei FORGE-PLAN (max 3 domande mirate) | FORGE-AGENT-SKILL | conductor checklist | P1 — ✅ FATTA 2026-07-20: `workflows/ASK-PROTOCOL.md` + step ASK in WF-SKILL/AGENT-NEW + qa-gate p.7 (CP-20260720-009) |
| MIR-4 | EmpireDesk seam modules (già ordine Max B1 — solo annotato, owner altrui) | (Gael) | selftest 8/8 | — |
| MIR-5 | Retrofit 7-file su reparti pre-impero, 1 figlio/sprint | FORGE-AGENT-SKILL | fas-qa-gate | P3 |
| MIR-6 | REGISTRO-ERRORI.md in ogni runtime attivo | ogni reparto owner | METHOD-GUARD | P1 — ✅ outreach+carousel+youtube-kit 2026-07-20 (PreventivoForge/EmpireDesk ce l'avevano già) |
| MIR-7 | FORGE-PLAN con sorgenti dichiarate (traceability) | FORGE-AGENT-SKILL | qa-gate | P1 |
| MIR-8 | Nota metodo Research→Plan→Reset→Implement in `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` | Max (approva) | — | P3 |
| MIR-9 | topology.md obbligatorio per team nuovi | FORGE-AGENT-SKILL | qa-gate | P2 — ✅ FATTA 2026-07-20: `templates/TOPOLOGY-TEMPLATE.md` + R2-bis + WF-AGENT-NEW step 6 + gate p.1 + `FORGE-AGENT-SKILL/TOPOLOGY.md` (dogfooding) |
| MIR-10 | Auto-applicazione: retrofit guidato dal reparto | FORGE-AGENT-SKILL | — | P3 |
| MIR-11 | Skill `/youtube-lead-machine` + agenti yt-* (backlog reparto) | FORGE-AGENT-SKILL → 04-MARKETING | fas-qa-gate | **P0 candidato prossimo passo** |
| MIR-12 | Copy review APSOC su `Agency page*-` + eventi tracking uniformi | 04-MARKETING | A8 ≥85 | P2 — ✅ REVIEW 2026-07-20: 78/100, 5 P0 consegnati + schema eventi uniforme; ⏳ applicazione patch = corsia Max (CP-20260720-012) |

**Regola P0/P1:** chiusura via workflow repo (edit + CP + ADR se serve), niente maghe in chat.

---

## 4. DECISIONI ARCHITETTURALI PRESE OGGI (→ ADR-009)

1. **3 toolkit esterni ufficiali dell'impero**, vendored alla root: `copy-workflow/` (motore copy),
   `content-forge2.0/` (motore di forgia), `master-build-architecture/` (metodo architetture) — wrap, mai riscrittura (ADR-003).
2. **Nuovo reparto operativo `FORGE-AGENT-SKILL`** (officina agenti & skill, roster v1: 4 agenti) sotto 06b-FORGE.
3. Wrapper skill in `.claude/skills/` per i 3 motori (invocabili: `/copywriting`, `/forge`, `/master-architect`).

## 5. GOVERNO
Controllore di questo documento: METHOD-GUARD (pattern) + Ispettorato Generale (audit su adozione MIR).
Retro: chiusura MIR rivista nel RETRO settimanale (dossier 16 G7).
