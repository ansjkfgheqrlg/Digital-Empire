# 🏭 REPARTO FORGE-AGENT-SKILL — officina agenti & skill dell'impero

> **Missione:** creare NUOVI AGENTI e NUOVE SKILL per tutto Digital Empire, con qualità CF-grade
> (7 file canonici) e intestazione completa (ADR-008), usando come motore **content-forge2.0** (`/forge`)
> e come metodo architetturale **master-build-architecture**.
> **Istituito:** 2026-07-20 (direttiva Max, ADR-009, CP-20260720-002).
> **Intestazione (ADR-008):** Proprietario = 06b-FORGE (L2.1 SKILL-WORKS / L2.2 AGENT-WORKS) ·
> Controllore = `fas-qa-gate` + METHOD-GUARD · Origine = FORGE (auto-serve) · Governo = Mandato + ADR-001/002/003/006.

## Perché esiste
L'impero non è un workflow: è una holding di workflow. Ogni espansione richiede agenti e skill nuove,
fino ad oggi prodotte artigianalmente. Questo reparto è l'officina permanente: trasforma conoscenza grezza
(transcript, appunti, dossier, run di Empire Studio) in **agenti, team e skill production-ready**.

## DONE WHEN (definizione di "fatto")
Un agente/skill è "forgiata" solo quando ha TUTTO:
1. **7 file canonici** (spec.md, system-prompt.md, tools.md, playbook.md, evals.md, failure-modes.md, memory.md)
2. **MKD** prodotto dalla sorgente (mai riassunti — regola content-forge)
3. **Intestazione ADR-008** scritta in testa a spec.md + registrata in `company/REGISTRO-IMPRESA.md`
   e `company/skills-map.yaml` (se skill)
4. **Gate QA passato** (fas-qa-gate: coverage atomi ≥95%, 0 stub/TODO, failure-modes presenti, evals definiti)
5. Checkpoint in `company/Memory/checkpoints/` + (se decisione nuova) ADR

## Struttura
```
FORGE-AGENT-SKILL/
├── README.md              ← questo file (missione + DONE WHEN)
├── agents/
│   ├── README.md          ← roster completo
│   ├── fas-conductor/     ← direttore: intake richiesta → piano di forgia
│   ├── fas-agent-smith/   ← forgia agenti/team (motore: content-forge --target=agent|team)
│   ├── fas-skill-smith/   ← forgia skill ufficiali (motore: content-forge --target=skill)
│   └── fas-qa-gate/       ← gate bloccante: 7-file, coverage, failure-modes, intestazione
├── workflows/
│   ├── WF-AGENT-NEW.md    ← pipeline nuova richiesta agente/team
│   └── WF-SKILL-NEW.md    ← pipeline nuova richiesta skill
├── rules/                 ← R1-R4 (mai riassunti · 7 canonici · failure-modes · intestazione)
├── memory/                ← memory-first: checkpoints/ + INDEX.md del reparto
└── engine/                ← puntatori ai motori wrappati (ADR-003): ../../content-forge2.0, ../../master-build-architecture
```

## Motori (ADR-003 — wrap, MAI riscrittura)
- **`content-forge2.0/`** (root repo) — pipeline MKD → artefatto. Agenti interni: conductor, builders, qa, meta.
- **`master-build-architecture/`** (root repo) — 10 invarianti + processo 10 fasi per le architetture complesse.
- Skill wrapper installate: `.claude/skills/content-forge`, `.claude/skills/master-build-architecture`.

## Handoff (chi ci chiede cosa)
Qualsiasi ecosistema/reparto può richiedere un agente o una skill con il **contratto di richiesta capability**
(dossier 06b §1.2): scopo, input, output, vincoli, esempi. Risposta del reparto: PLAN di forgia →
conferma richiedente → BUILD → GATE → registrazione → consegna.

## Primi mandati (2026-07-20)
1. Wrapper ufficiali installati (content-forge, master-build-architecture, copy-workflow) ✅
2. Architettura impero revisionata → `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md`
3. In pipeline (backlog reparto): skill `/youtube-lead-machine`, agenti reparto YouTube per 04-MARKETING.
