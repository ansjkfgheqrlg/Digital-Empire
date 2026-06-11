# 🔨 07 — FORGE · La Fabbrica Organizzativa

> **Livello:** L1 · **Priorità:** TRASVERSALE (core) · **Stato:** parziale — motori installati (skill-creator, content-forge, omega-create, prd-architect-os, pipeline SPARC), pipeline di forgiatura in formalizzazione
> **Dossier vincolante:** `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07-FORGE · Gerarchia: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §2
> **Supervisione C-Suite:** Chief-Forge (`company/Board-CSuite/Chief-Forge.md`)

---

## 1. Missione

La FORGE è **HR + R&D organizzativo** della holding: crea, valuta, migliora e ritira
**skill, agenti, team, workflow e interi ecosistemi**. È il motivo per cui EMPIRE OS può
crescere senza toccare l'architettura (⚠️ premessa del Piano Maestro: *"il piano è la
micro-base"*). Nessun altro ecosistema può assumere o ritirare agenti: ogni componente
organizzativo nuovo nasce qui, viene valutato qui, viene registrato qui.

**I due motori reali della FORGE:**
1. **content-forge** — materia prima grezza → artefatto operativo, con **MKD (Master
   Knowledge Document) obbligatorio** come passaggio intermedio. Mai riassumere: espandere.
2. **skill-creator** — creazione, miglioramento e **eval** di skill (init, draft,
   benchmark, variance analysis, description optimization).

Motori di supporto: **omega-create** (progetti/skill per Claude Browser),
**prd-architect-os** (PRD tipo A–E con quality score), **pipeline SPARC** (7 agenti:
specification → planner → researcher → architecture → coder → tester → reviewer).

---

## 2. Il processo standard di forgiatura (ordine → PRD → build → eval → consegna)

Questo è il flusso obbligatorio per QUALSIASI artefatto prodotto dalla FORGE.
Nessuna fase si salta (lo vigila `frg-sparc-warden`; i gate sono in §6).

```
┌─ 0. ORDINE ────────────────────────────────────────────────────────────────┐
│  Qualsiasi ecosistema invia handoff: {capability mancante, contesto,       │
│  KPI attesi, budget}. frg-chief lo mette in coda e lo prioritizza.         │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               ▼
┌─ 1. CONTESTO (regola operativa) ────────────────────────────────────────────┐
│  PRIMA di inventare da zero: chiedere a INTELLIGENCE se Empire Studio ha    │
│  già ingerito materiale sul tema. Se sì → content-forge parte da quello.   │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               ▼
┌─ 2. SPEC ──────────────────── G-SPEC ───────────────────────────────────────┐
│  frg-spec-writer (agent-specification, SPARC fase S): requisiti,            │
│  acceptance criteria, vincoli, out-of-scope. Nessuna build senza spec ok.   │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               ▼
┌─ 3. MKD / PRD ─────────────── G-MKD/PRD ────────────────────────────────────┐
│  Documento intermedio "perfetto": MKD via frg-mkd-forger (content-forge,    │
│  MAI saltato) oppure PRD via frg-prd-architect (bloccato se context <60).   │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               ▼
┌─ 4. BUILD ──────────────────────────────────────────────────────────────────┐
│  Per target: skill → frg-skill-smith (skill-creator) · agente →             │
│  WF-AGENT-NEW (architect-agent, 7-file) · team → WF-TEAM-NEW (schema        │
│  canonico CF) · ecosistema → WF-ECOSYSTEM-NEW (solo mandato Board) ·        │
│  progetto Claude Browser → omega-create. SPARC su ogni build non banale.    │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               ▼
┌─ 5. EVAL ──────────────────── G-EVAL + G-CONTRADICTION ─────────────────────┐
│  frg-eval-runner: eval ≥ soglia (85% pass per skill). frg-contradiction-    │
│  gate: skill-contradiction-analyzer verde vs skill esistenti (anti-drift).  │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               ▼
┌─ 6. CONSEGNA + REGISTRO ───── G-REGISTRY ───────────────────────────────────┐
│  Artefatto installato presso l'ecosistema richiedente + eval report.        │
│  frg-hr-registrar aggiorna Identity-HR (registro-agenti.yaml).              │
│  Pagina wiki tools/ via INTELLIGENCE. Evento costo → OPERATIONS.            │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Regola operativa non negoziabile:** la FORGE non inventa da zero quando esiste materia
prima — prima interroga INTELLIGENCE (Empire Studio); l'MKD intermedio è obbligatorio e
non riassume mai: **espande** (ogni atomo informativo diventa più ricco e strutturato).

---

## 3. DONE WHEN (criteri di completamento dal dossier)

1. Esiste la **pipeline di forgiatura standard** (§2) end-to-end: richiesta → spec →
   MKD/PRD → costruzione → eval → consegna → registro Identity-HR aggiornato.
2. Ogni nuovo artefatto rispetta lo **schema team canonico** (pattern #1) e la
   **progressive disclosure** (pattern #7: kernel SKILL.md ≤500 righe, dettaglio in references/).
3. Il registro Identity-HR elenca il **100% degli agenti** con ruolo, costo, performance.
4. La FORGE ha creato almeno: 1 skill nuova con eval ≥ soglia, 1 team L4 completo,
   1 reparto L2 per un ecosistema business.

## 4. Reparti L2 (dal dossier — vincolanti)

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | **SKILL-WORKS** | forgia skill: nuove, migliorate, auditate (skill-creator + contradiction-analyzer) | `Reparti/SKILL-WORKS/` |
| L2.2 | **AGENT-WORKS** | forgia agenti (7-file, architect-agent) e team canonici (coordinator+workers) | `Reparti/AGENT-WORKS/` |
| L2.3 | **WORKFLOW-WORKS** | forgia workflow e orchestrazioni: content-forge pipeline (MKD) + PRD | `Reparti/WORKFLOW-WORKS/` |
| L2.4 | **ECOSYSTEM-WORKS** | forgia interi ecosistemi L1 — il livello massimo, solo su mandato Board | `Reparti/ECOSYSTEM-WORKS/` |
| L2.5 | **METHOD-GUARD** | custode dei pattern: SPARC enforcement, omega-create, schema canonico | `Reparti/METHOD-GUARD/` |

## 5. Workflow L3 e Funzioni L4

| Reparto | Workflow L3 | Funzioni L4 |
|---|---|---|
| SKILL-WORKS | `Workflow/WF-SKILL-NEW/` · `Workflow/WF-SKILL-IMPROVE/` · `Workflow/WF-SKILL-AUDIT/` | `Funzioni/T-spec/` · `Funzioni/T-draft/` · `Funzioni/T-eval-runner/` · `Funzioni/T-description-optimizer/` |
| AGENT-WORKS | `Workflow/WF-AGENT-NEW/` · `Workflow/WF-TEAM-NEW/` | `Funzioni/T-org-design/` · `Funzioni/T-handoff-contracts/` · `Funzioni/T-shared-state-schema/` |
| WORKFLOW-WORKS | `Workflow/WF-FORGE-PIPELINE/` · `Workflow/WF-PRD/` | (operano i motori content-forge / prd-architect-os) |
| ECOSYSTEM-WORKS | `Workflow/WF-ECOSYSTEM-NEW/` | (riusa T-org-design + T-handoff-contracts + T-shared-state-schema) |
| METHOD-GUARD | `Workflow/WF-SPARC-ENFORCE/` | (gate trasversale, nessun L4 proprio) |

## 6. Quality gates (in ordine, nessuno si salta)

| Gate | Verifica | Owner |
|---|---|---|
| **G-SPEC** | spec approvata prima di costruire (requisiti, acceptance, out-of-scope) | frg-spec-writer |
| **G-MKD/PRD** | documento intermedio completo — content-forge non salta MAI l'MKD; PRD bloccato se context score <60 | frg-mkd-forger / frg-prd-architect |
| **G-EVAL** | eval ≥ soglia (skill: ≥85% pass) | frg-eval-runner |
| **G-CONTRADICTION** | skill-contradiction-analyzer verde vs skill esistenti | frg-contradiction-gate |
| **G-REGISTRY** | Identity-HR aggiornato (artefatto senza registro = artefatto non consegnato) | frg-hr-registrar |

## 7. Roster agenti L5 (schede complete in `Agenti/`)

| ID | Ruolo | Tier | Scheda |
|---|---|---|---|
| `frg-chief` | Chief-Forge (C-Suite L0) — approva forgiature, gestisce coda | Opus | `Agenti/frg-chief.md` |
| `frg-spec-writer` | Specification (SPARC S): requisiti, acceptance, out-of-scope | Sonnet | `Agenti/frg-spec-writer.md` |
| `frg-org-designer` | Disegna org chart team/reparti/ecosistemi (schema canonico CF) | Opus | `Agenti/frg-org-designer.md` |
| `frg-skill-smith` | Operatore skill-creator: init, draft, package | Sonnet | `Agenti/frg-skill-smith.md` |
| `frg-mkd-forger` | Operatore content-forge: raw → MKD → artefatto target | Sonnet | `Agenti/frg-mkd-forger.md` |
| `frg-prd-architect` | Operatore prd-architect-os: PRD A–E con quality score | Sonnet | `Agenti/frg-prd-architect.md` |
| `frg-eval-runner` | Esegue eval skill, benchmark, variance analysis | Haiku | `Agenti/frg-eval-runner.md` |
| `frg-contradiction-gate` | skill-contradiction-analyzer su ogni rilascio (anti-drift) | Sonnet | `Agenti/frg-contradiction-gate.md` |
| `frg-hr-registrar` | Identity-HR: assume/ritira agenti, traccia costo/performance | Haiku | `Agenti/frg-hr-registrar.md` |
| `frg-sparc-warden` | Verifica SPARC (S→P→A→R→C), blocca salti di fase | Haiku | `Agenti/frg-sparc-warden.md` |

## 8. Asset esistenti → reparto (ADR-003: si usano/wrappano, non si riscrivono)

| Asset | Reparto | Azione |
|---|---|---|
| skill `skill-creator` (`~/.claude/skills/skill-creator/` + copia in `Crea siti/skills/`) | SKILL-WORKS | **USA** — motore reale #1 |
| `SKILL & Agenti/Content-forge/skill - FINALE/` (content-forge, 433 file) | WORKFLOW-WORKS | **USA** — motore reale #2; MKD obbligatorio |
| `System OMEGA - Creazione proggetti e skill per Claude/` + skill `omega-create` | METHOD-GUARD | **USA** per Claude Browser; **WRAPPA** in WF-SKILL-NEW come variante target |
| skill `prd-architect-os` | WORKFLOW-WORKS / WF-PRD | **USA** |
| skill `architect-agent` | AGENT-WORKS | **USA** |
| `SKILL & Agenti/Skill Master Architecture/` | SKILL-WORKS | **USA** come reference di metodo (Three-Level Architecture) |
| Agenti SPARC (`agent-specification/-planner/-researcher/-architecture/-coder/-tester/-reviewer`) | METHOD-GUARD | **USA** — pipeline SPARC standard |
| skill `sparc-methodology`, `swarm-orchestration` | METHOD-GUARD | **USA** |
| skill `skill-contradiction-analyzer` | SKILL-WORKS / WF-SKILL-AUDIT | **USA** — gate obbligatorio |
| `SKILL & Agenti/agent-factory/` | AGENT-WORKS | **EVOLVI** — valutare merge con WF-AGENT-NEW |

## 9. Skill nuove da forgiare (priorità da dossier + Chief-Forge P0)

| Skill | Scopo | Priorità |
|---|---|---|
| `forge-intake` | form unico di richiesta capability: cattura `{ecosistema, gap, KPI, budget}` e instrada al L3 giusto | ALTA |
| `ecosystem-scaffold` | genera struttura completa L2-L5 + BACKBONE.md per ecosistema nuovo | ALTA |
| `team-canonical-template` | genera team a schema fisso CF (coordinator, workers, I/O, acceptance, escalation, shared_state) | ALTA |
| `agent-retire` | procedura di ritiro agente: deprecazione, archivio, update registro HR | MEDIA |
| `forge-metrics` | report trimestrale: skill create/migliorate, eval medi, tempo di forgiatura | BASSA |

E inoltre (commesse P0 per altri ecosistemi, vedi `Chief-Forge.md`): empire-verify (PLATFORM),
context-pack + wiki-sync-guard (INTELLIGENCE), empire-swarm + cost-ledger + budget-guard
(OPERATIONS), empire-brand-gate (MARKETING).

## 10. KPI

| KPI | Target |
|---|---|
| Tempo richiesta → artefatto consegnato (skill semplice) | ≤ 2 giorni |
| Eval score nuove skill (skill-creator evals) | ≥ 85% pass |
| Artefatti conformi a schema canonico al primo audit | ≥ 90% |
| Copertura registro Identity-HR | 100% agenti |
| PRD quality score (prd-architect-os) | ≥ 75/100 |

## 11. Fasi di build (roadmap interna F1–F5)

| Fase | Cosa | Gate |
|---|---|---|
| F1 | Pipeline WF-SKILL-NEW formalizzata su skill-creator; prima skill = `empire-verify` (per PLATFORM) | skill consegnata con eval verde |
| F2 | WF-FORGE-PIPELINE: content-forge collegato a Empire Studio (input = materiale ingerito) | un MKD→artefatto da materiale reale |
| F3 | Identity-HR: registro agenti popolato (censimento da tutti gli ecosistemi) | 100% censito |
| F4 | WF-TEAM-NEW: forgiare un team L4 reale per un business (es. T-thumbnail per MULTI-BUSINESS/YT) | team operativo |
| F5 | WF-ECOSYSTEM-NEW: dry-run sulla creazione ecosistema E-commerce (F9+ roadmap) | scaffold completo validato |

## 12. Connessioni

- `BACKBONE.md` (questo ecosistema) — topologia star, namespace, handoff
- `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 — dossier vincolante
- `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md` — registro skill, Identity-HR, topologie
- `company/Board-CSuite/Chief-Forge.md` — supervisione C-Suite
- `company/Ecosistemi/08-INTELLIGENCE/` — materia prima (Empire Studio) e archiviazione wiki
- `company/Ecosistemi/09-OPERATIONS/` — pre-approvazione budget per ogni nuovo agente

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07-FORGE · Aggiornato: 2026-06-11 (F1-bis arricchimento)*
