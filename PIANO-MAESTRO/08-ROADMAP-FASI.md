# 🗺️ EMPIRE OS — Roadmap a Fasi (Dynamic Workflow)

> Esecuzione a iterazioni self-paced, modello BUILD-11→16 di AION GROUP esteso.
> Regola: **una fase per ciclo, gate di validazione prima della successiva, checkpoint
> memoria + log wiki + push GitHub ad ogni fase.** Nessuna fase parte se la precedente
> non ha passato il gate. Le fasi parallele sono marcate ∥.
>
> ⚠️ Questo piano è la micro-base: la roadmap arriva a F12 ma la FORGE è progettata per
> generare nuove fasi/ecosistemi oltre questo orizzonte.

---

## Quadro generale

```
F1 Scaffolding (parte da MEMORY: ME-0→ME-5, urgenza massima)
   ─→ F2 Backbone ─→ F3 Migrazione asset ─→ F4 AGENCY live
                                                       ├→ F5 ∥ MARKETING + CONTENT-FACTORY live
                                                       ├→ F6 INFO-BUSINESS (lancio orchestrato)
                                                       ├→ F7 YOUTUBE AUTOMATION
                                                       └→ F8 PUBLISHING/KDP industrializzato
F9 Agenti reali + Sentinels ─→ F10 Auto-miglioramento ─→ F11 E-commerce ─→ F12 Dashboard + scala
```

---

## F1 — Scaffolding EMPIRE OS (`company/`)

**Obiettivo:** la holding diventa NAVIGABILE nell'Explorer, come `orchestration/company/` di CF.

| Task | Output |
|---|---|
| **1.0** | **ECOSISTEMA MEMORY (PRIMA DI TUTTO — urgenza massima):** `company/Memory/` completa (INDEX, STATO-EMPIRE, checkpoints/, decisions/, plans/, sessions/, tasks/, state/, audit/) + template CP/ADR + primo CP + ADR fondativi + regola memory-first in CLAUDE.md. Dettaglio fasi ME-0→ME-5 in `09-ECOSISTEMA-MEMORY.md` |
| 1.1 | `Digital Empire/company/GRUPPO.md` — organigramma holding |
| 1.2 | `company/Mandato/MANDATO-EMPIRE.md` — gli Articoli (posizionamento, brand voice, pricing policy, qualità, regole non negoziabili) |
| 1.3 | `company/Board-CSuite/` — CEO/Empire-Conductor, COO, CTO, CMO, CRO, CFO, Chief-Forge (schede agente complete: identità, responsabilità, I/O, come ragiona, KPI, escalation) |
| 1.4 | `company/Ecosistemi/<01-AGENCY … 10-MEMORY>/` — per ognuno: `ECOSISTEMA.md`, `BACKBONE.md` (come si collega), `Reparti/`, `Workflow/`, `Funzioni/`, `Agenti/` |
| 1.5 | `company/Backbone/{Bus,Brain,Governance,Identity-HR,Observability,Coordination}/` |
| 1.6 | `company/Guilds/` (5) + `company/Sentinels/` (5) + `company/Gerarchia/` (LX→L5) |
| 1.7 | Generatore `scripts/gen-empire.py` (stile gen-group.py CF) — l'albero è rigenerabile |

**Gate F1:** struttura completa, 0 cartelle vuote, ogni nodo ha README "cosa fa · come si collega · come ragiona". Albero coerente coi dossier 01-07.

---

## F2 — Backbone operativo

**Obiettivo:** sistema nervoso acceso.

| Task | Output |
|---|---|
| 2.1 | `ruflo init` in `Digital Empire/` (o root company/) + daemon + memory init |
| 2.2 | Skill **`empire-context`** — la knowledge base DE per agenti (equivalente exponium-context): identità, 3 prodotti+prezzi, ICP, brand voice, Mandato, mappa ecosistemi. PRIMA skill nuova. |
| 2.3 | BUS: cartelle handoffs + contratto JSON standard `{from, to, payload, acceptance_criteria, status}` |
| 2.4 | BRAIN: namespace AgentDB per ecosistema + bridge wiki↔AgentDB (Memory Empire wiki-syncer) |
| 2.5 | GOVERNANCE: `verify-empire.sh` v1 (check struttura + Mandato + zero orfani) |
| 2.6 | IDENTITY-HR: `registro-agenti.yaml` unico |

**Gate F2:** verify-empire verde; memory_store/search funzionanti; empire-context attiva e usata da un agente di test.

---

## F3 — Migrazione asset (zero orfani)

**Obiettivo:** ogni workflow/skill/progetto esistente assegnato al suo reparto. **Mappatura + wrapper, MAI riscrittura.** I sistemi attivi (outreach) non si toccano finché il sostituto non è validato.

| Sorgente | Destinazione |
|---|---|
| `Outreach/Outreach Workflow/` + LinkedIn/Instagram Automation + dashboard | AGENCY / Acquisizione |
| `Copy-Workflow-manuale/copy-workflow/` (A1-A8, S1-S3) | MARKETING / Copywriting (motore) |
| `caroselli/`, Workflow Canva, Workflow pubblicazione automatica | CONTENT-FACTORY |
| `Workflow-libri/`, `KDP - prodottti digitali/`, printing-press | MULTI-BUSINESS / Publishing |
| `Crea siti/`, empire-style, site-* | PLATFORM / Siti |
| skill-creator, content-forge, System OMEGA, SPARC agents | FORGE |
| Empire Studio, Memory Empire, second-brain-vault | INTELLIGENCE (così come sono) |
| avvia-* skill, run schedulate | OPERATIONS |
| beast-preventivi, agency-scalping, market-* | AGENCY + MARKETING (per skill-map) |

| Task | Output |
|---|---|
| 3.1 | `company/skills-map.yaml` — ogni skill → ecosistema → reparto → team |
| 3.2 | `company/org/inventario-asset.yaml` — ogni cartella/progetto → destinazione → azione (usa/wrappa/evolvi) |
| 3.3 | Wrapper L3: ogni workflow esistente diventa un team-workflow con README + handoff contract (il codice resta dov'è) |

**Gate F3:** inventario 100% mappato, 0 orfani, verify-empire esteso con check skills-map.

---

## F4 — AGENCY live (primo ecosistema end-to-end)

**Obiettivo:** il flusso revenue completo gira come ecosistema coordinato:
`lead → outreach (esistente) → call → preventivo (beast-preventivi) → contratto → delivery 7gg → supporto 90gg → testimonianza/upsell`.

Dettaglio nel dossier `01-ECOSISTEMA-AGENCY.md`. **Gate F4:** un ciclo completo reale tracciato nel project state (state.json + trace.jsonl) con handoff contract tra i reparti.

---

## F5 ∥ — MARKETING + CONTENT-FACTORY live

**Obiettivo:** i due ecosistemi trasversali producono per committenti interni reali.

- MARKETING: routing richieste copy cross-ecosistema, gate score ≥80/100 obbligatorio.
- CONTENT-FACTORY: layer engines multi-motore (Canva MCP, HeyGen, ffmpeg, TTS), primo batch caroselli + primo video con brand_kit DE.

Dettaglio nei dossier 03 e 04. **Gate F5:** 1 ordine Agency→Content-Factory e 1 ordine InfoBusiness→Marketing completati via handoff contract, QA gate passato.

---

## F6 — INFO-BUSINESS: lancio orchestrato

**Obiettivo:** il prossimo lancio (corso/ebook) è pianificato ed eseguito dal sistema: Reparto Lanci coordina, Marketing produce le sequenze, Content-Factory gli asset, Platform la pagina.

Dettaglio nel dossier `02-ECOSISTEMA-INFOBUSINESS.md`. **Gate F6:** lancio reale con calendario, asset e sequenze prodotti dal sistema; retro post-lancio nel ReasoningBank.

---

## F7 — YOUTUBE AUTOMATION

**Obiettivo:** primo canale automatizzato.

| Task | Output |
|---|---|
| 7.0 | **Ingestione Empire Studio dei 2 canali riferimento** (@Legamidiamore, @dosementale): campione di video per canale, frame densi + visione Claude, `video-analysis.md` per video → pattern di produzione reverse-engineered in wiki + atoms in Memory Empire. SESSIONE DEDICATA — il video VA VISTO. |
| 7.1 | Scelta niche + brand_kit canale 1 (da analisi 7.0 + Intelligence) |
| 7.2 | Pipeline 4 fasi (Ricerca → Produzione via Content-Factory → Ottimizzazione SEO → Pubblicazione YouTube API) |
| 7.3 | Primo video end-to-end con QA gates; poi cadenza schedulata |

Dettaglio nel dossier `05-ECOSISTEMA-MULTIBUSINESS.md`. **Gate F7:** primo video pubblicato conforme ai 4 QA gate (script, audio, visual, SEO).

---

## F8 — PUBLISHING/KDP industrializzato

**Obiettivo:** pipeline libro end-to-end (Workflow-libri + printing-press) come team L3 con cost guard e QA gate. **Gate F8:** un libro completo prodotto dal flusso integrato.

---

## F9 — Agenti reali + Sentinels

**Obiettivo:** da definizioni markdown ad agenti running: `agent_spawn` per i coordinator dei 10 ecosistemi + Empire-Conductor + 5 Sentinels always-on (Cost, Quality, Drift, Security, Brand-Voice) nel registro Identity-HR. **Gate F9:** roster reale nello swarm, decisione cross-ecosistema presa via hive-mind raft.

---

## F10 — Auto-miglioramento attivo

**Obiettivo:** loop osserva→giudica→distilla→agisci→predici (ReasoningBank + neural_train + autopilot + FORGE che assume/ritira team). Equivalente `evolve.sh` CF a livello holding. **Gate F10:** almeno un'evoluzione organizzativa proposta dal sistema e applicata.

---

## F11 — E-commerce (nuovo business via FORGE)

**Obiettivo:** la FORGE crea il sotto-ecosistema E-comm usando il processo standard (PRD → team → workflow → skill). È anche il TEST che la fabbrica organizzativa funziona. **Gate F11:** sotto-ecosistema generato dalla FORGE conforme allo schema canonico.

---

## F12 — Dashboard + scala

**Obiettivo:** dashboard web della holding (stato ecosistemi, costi, produzione, KPI), scheduling produzioni ricorrenti, scaling multi-canale/multi-cliente/multi-libro via swarm. **Gate F12:** dashboard legge stato reale dal filesystem/AgentDB (mai dichiarato).

---

## Regole di esecuzione (ogni fase)

0. **MEMORY-FIRST (pattern #13, non negoziabile):** prima di QUALSIASI task interrogare
   `company/Memory/` (INDEX + STATO-EMPIRE + CP/ADR rilevanti); dopo OGNI task scrivere
   checkpoint CP. Nessun task è chiuso senza CP-id.
1. `memory_search` pattern rilevanti PRIMA di costruire.
2. Costruire in dry-run dove possibile; spese reali solo con ok esplicito.
3. `verify-empire.sh` verde prima del gate.
4. Checkpoint: memoria CP-xxx + `wiki/log.md` + push GitHub.
5. Retro: fallimenti → ReasoningBank.
6. Il gate lo valida l'utente (Max) per le fasi con output business reale (F4-F8).
