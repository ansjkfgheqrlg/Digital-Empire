# FORGE — Organo del Genesi Core (porta d'ingresso)

> La **fabbrica organizzativa** della holding. Dove ARCHITETTURA disegna la forma, la FORGE
> ci costruisce dentro il CONTENUTO. Standard: CF-grade.
> Fonte di verità: [[06-ECOSISTEMI-CORE]] §07-FORGE. Stato: build STEP 2 del Genesi Core.

---

## Missione
La FORGE è **HR + R&D organizzativo** del Genesi Core: crea, valuta, migliora e ritira
**skill, agenti, team, workflow e interi ecosistemi**. È il motivo per cui EMPIRE OS cresce e si
ripara senza riscrivere l'architettura (⚠️ premessa del Piano Maestro: *"il piano è la micro-base"*).
Nessun altro ecosistema può assumere o ritirare componenti organizzativi: ogni cosa nasce qui,
viene valutata qui, viene registrata qui.

In termini SPARC: **ARCHITETTURA possiede Specification → Pseudocode → Architecture; la FORGE
possiede Refinement → Completion.** L'architetto disegna la forma vuota, la fabbrica la riempie.

**Cosa NON è.** Non disegna strutture da zero (le chiede ad ARCHITETTURA). Non giudica se l'output
è *all'altezza di Max* (MAXIMILIAN). Non decide se è *lecito* (Mandato). Riceve un blueprint
validato e costruisce il contenuto reale, lo valuta, lo consegna.

---

## Posizione nel Genesi Core (gemella di ARCHITETTURA)
```
LX  Mandato (legge) · MAXIMILIAN (standard/visione)
 │
GENESI CORE  ┌─ ARCHITETTURA (progetta la struttura) ──┐
             └─ FORGE (costruisce il contenuto) ◄─ blueprint ┘
 │
L0  Board C-Suite (regia)
 │
L1  i 10 ecosistemi (nascono DA Genesi Core, costruiti DALLA FORGE)
```
La FORGE è **gemella di ARCHITETTURA** e **multi-tenant per definizione**: forgia per qualsiasi
ecosistema. ARCHITETTURA → struttura; **FORGE → contenuto** (vedi confine, in fondo).

---

## I 5 reparti (L2) — vedi `Reparti/`
- **L2.1 SKILL-WORKS** — forgia skill: nuove, migliorate, auditate (skill-creator + contradiction-analyzer).
- **L2.2 AGENT-WORKS** — forgia agenti (7-file, architect-agent) e team canonici (coordinator + workers).
- **L2.3 WORKFLOW-WORKS** — forgia workflow e orchestrazioni: content-forge pipeline (MKD) + PRD.
- **L2.4 ECOSYSTEM-WORKS** — forgia interi ecosistemi L1 (livello massimo, solo su mandato Board).
- **L2.5 METHOD-GUARD** — custode dei pattern: SPARC enforcement, omega-create, schema canonico.

## I 10 agenti (`frg-*`) — vedi `Agenti/`
`frg-chief` (Opus, C-Suite L0, coda+approvazioni) · `frg-spec-writer` (Sonnet, fase S) ·
`frg-org-designer` (Opus, org chart) · `frg-skill-smith` (Sonnet, skill-creator) ·
`frg-mkd-forger` (Sonnet, content-forge/MKD) · `frg-prd-architect` (Sonnet, prd-architect-os) ·
`frg-eval-runner` (Haiku, eval) · `frg-contradiction-gate` (Sonnet, anti-drift) ·
`frg-hr-registrar` (Haiku, Identity-HR) · `frg-sparc-warden` (Haiku, SPARC enforcement).

## I 9 workflow (L3) — vedi `Workflow/`
SKILL-WORKS: `WF-SKILL-NEW` · `WF-SKILL-IMPROVE` · `WF-SKILL-AUDIT` —
AGENT-WORKS: `WF-AGENT-NEW` · `WF-TEAM-NEW` —
WORKFLOW-WORKS: `WF-FORGE-PIPELINE` · `WF-PRD` —
ECOSYSTEM-WORKS: `WF-ECOSYSTEM-NEW` — METHOD-GUARD: `WF-SPARC-ENFORCE`.

## I motori reali — vedi `Motori/Mappa-Motori.md`
La FORGE non è documentazione morta: ogni operazione è **wireata a un motore nativo esistente**
e verificato (skill-creator, content-forge, architect-agent, prd-architect-os, sparc-methodology,
skill-contradiction-analyzer, agent-factory, omega-create). La `Mappa-Motori.md` dice ESATTAMENTE
quale skill/agente reale esegue ogni operazione, col path nel workspace.

---

## La catena del Genesi Core (handoff completo)
```
richiesta → ARCHITETTURA (spec + blueprint + struct-gate) → FORGE (costruisce il contenuto)
         → MAXIMILIAN (è all'altezza?) → Mandato (lecito?) → Identity-HR (registra) → VIVO
```
- **ARCHITETTURA** (gemella, a monte): consegna `HC-ARCH-FORGE` (blueprint validato). La FORGE non
  inventa strutture: le riceve e ci costruisce dentro. Niente blueprint = niente build.
- **MAXIMILIAN** (a valle): la FORGE garantisce *contenuto completo ed eval-passed*; MAXIMILIAN che
  sia *all'altezza di Max*. Gate in serie dopo G-EVAL.
- **Mandato** (a valle): forma lecita prima della registrazione.
- **Identity-HR** (a valle): `frg-hr-registrar` registra l'artefatto/agente → poi VIVO.

---

## Confine ferreo: STRUTTURA vs CONTENUTO
**ARCHITETTURA = struttura. FORGE = contenuto.** ARCHITETTURA produce la forma vuota al millimetro
(file, sezioni, I/O, handoff, schema rispettato); la FORGE la riempie col contenuto reale, lo
valuta (eval ≥ soglia) e lo consegna. La FORGE non modifica gli schemi canonici (lo fa ARCHITETTURA
con WF-SCHEMA-EVOLVE): se serve una forma nuova, la chiede. Questo confine impedisce la
sovrapposizione tra i due gemelli del Genesi Core.

---

## Navigazione
- Motori reali → `Motori/Mappa-Motori.md` · Funzioni L4 → `Funzioni/` · Infrastruttura → [[BACKBONE.md]]
- Reparti → `Reparti/` (L2.1→L2.5) · Agenti → `Agenti/` (i 10 `frg-*`) · Workflow → `Workflow/` (i 9)
- Fonte di verità → [[06-ECOSISTEMI-CORE]] §07 · Gemella → [[ARCHITETTURA/ECOSISTEMA.md]]
- Gate a valle → [[12-DOSSIER-MAXIMILIAN]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]] · Registro → Identity-HR
