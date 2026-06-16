# Mappa-Motori — i motori REALI che la FORGE wrappa

> Questo è il file che rende la FORGE **viva, non documentazione morta.** Ogni operazione di
> forgiatura è qui mappata al motore reale (skill/agente) che la esegue, col **path verificato**
> nel workspace. Se un motore non è qui con un path reale, l'operazione non è eseguibile.
> Fonte: [[06-ECOSISTEMI-CORE]] §07 §5 (asset → reparto) · ADR-003 (si usano/wrappano, non si riscrivono).

---

## Principio (ADR-003)
La FORGE **non riscrive** i motori: li wrappa. Ogni agente `frg-*` è un *operatore* di un motore
nativo esistente. La forgiatura è l'orchestrazione di questi motori dentro i gate G-SPEC→G-REGISTRY.

Legenda path: `~/` = `C:\Users\Utente\.claude\` · workspace = radice `Digital Empire/`.

---

## Tabella maestra — operazione FORGE → motore reale → path

| # | Operazione FORGE | Workflow / Funzione | Motore reale | Path verificato | Stato |
|---|---|---|---|---|---|
| 1 | **Spec / requisiti** (fase S SPARC) | WF-SKILL-NEW · T-spec | `agent-specification` | `~/skills/agent-specification/` | ✅ verificato |
| 2 | **Pianificazione task** | WF-FORGE-PIPELINE | `agent-planner` | `~/skills/agent-planner/` | ✅ verificato |
| 3 | **Ricerca pre-build** | tutti (fase contesto) | `agent-researcher` | `~/skills/agent-researcher/` | ✅ verificato |
| 4 | **Forgia skill** (init, draft, package, eval) | WF-SKILL-NEW · T-draft · T-eval-runner | `skill-creator` | `~/skills/skill-creator/SKILL.md` (+ copia `Crea siti/skills/skill-creator/`) | ✅ verificato |
| 5 | **Raw → MKD → artefatto** (mai riassumere, espandere) | WF-FORGE-PIPELINE | `content-forge` | `~/skills/content-forge/SKILL.md` · archivio: `SKILL & Agenti/Content-forge/skill - FINALE/` (zip 2.0 `Skill-aggiornata.zip`) | ✅ verificato |
| 6 | **Blueprint architettura agente** | WF-AGENT-NEW | `architect-agent` | `~/commands/architect-agent.md` | ✅ verificato (command) |
| 7 | **Struttura sistema (fase A SPARC)** | WF-AGENT-NEW · WF-TEAM-NEW | `agent-architecture` | `~/skills/agent-architecture/` | ✅ verificato |
| 8 | **PRD tipo A–E + quality score** | WF-PRD · T-org-design (eco) | `prd-architect-os` | `~/skills/prd-architect-os/SKILL.md` | ✅ verificato |
| 9 | **Metodo S→P→A→R→C (enforcement)** | WF-SPARC-ENFORCE | `sparc-methodology` | `~/skills/sparc-methodology/SKILL.md` | ✅ verificato |
| 10 | **Anti-contraddizione skill** (gate G-CONTRADICTION) | WF-SKILL-AUDIT | `skill-contradiction-analyzer` | `~/skills/skill-contradiction-analyzer/SKILL.md` | ✅ verificato |
| 11 | **Factory agenti** (7-file, builder, quality) | WF-AGENT-NEW (EVOLVI: merge) | `agent-factory` | `SKILL & Agenti/agent-factory/skills/` → `agent-architect` · `agent-builder` · `agent-quality-sentinel` · `system-prompt-forge` | ✅ verificato (4 sub-skill) |
| 12 | **Progetti/skill per Claude Browser** | WF-SKILL-NEW (variante target) | `omega-create` | `~/skills/omega-create/SKILL.md` · workspace: `System OMEGA - Creazione proggetti e skill per Claude/` | ✅ verificato |
| 13 | **Coder / Tester / Reviewer** (fasi R→C SPARC) | WF-FORGE-PIPELINE (target codice) | `agent-coder` · `agent-tester` · `agent-reviewer` | `~/skills/agent-coder/` · `~/skills/agent-tester/` · `~/skills/agent-reviewer/` | ✅ verificato |
| 14 | **Implementazione automazione** (build codice) | WF-FORGE-PIPELINE (target script) | `build-implementation` | `~/commands/build-implementation.md` | ✅ verificato (command) |
| 15 | **Reference metodo** (Three-Level Architecture) | SKILL-WORKS (reference, non eseguibile) | Skill Master Architecture | `SKILL & Agenti/Skill Master Architecture/` | ✅ verificato (dir reference) |

---

## Quale motore per quale target di forgiatura

| Target | Motore primario | Motori di supporto |
|---|---|---|
| **skill** | `skill-creator` (#4) | `agent-specification` (#1) · `skill-contradiction-analyzer` (#10) · `omega-create` (#12, se Claude Browser) |
| **agente (7-file)** | `architect-agent` (#6) + `agent-factory` (#11) | `agent-architecture` (#7) |
| **team canonico** | `agent-factory/agent-architect` (#11) | `agent-architecture` (#7) — schema canonico CF da ARCHITETTURA |
| **workflow / orchestrazione** | `content-forge` (#5) | `agent-planner` (#2) · pipeline SPARC (#9, #13) |
| **documento MKD** | `content-forge` (#5) | — (MKD obbligatorio, mai saltato) |
| **PRD** | `prd-architect-os` (#8) | — (bloccato se context score <60) |
| **ecosistema intero** | `prd-architect-os` (#8) + `content-forge` (#5) | org L1→L5 disegnato da ARCHITETTURA, FORGE riempie il contenuto |

---

## Mappatura agente operatore `frg-*` → motore
| Agente | Motore wrappato | # in tabella |
|---|---|---|
| `frg-spec-writer` | agent-specification | #1 |
| `frg-skill-smith` | skill-creator | #4 |
| `frg-mkd-forger` | content-forge | #5 |
| `frg-prd-architect` | prd-architect-os | #8 |
| `frg-eval-runner` | skill-creator (modulo eval) | #4 |
| `frg-contradiction-gate` | skill-contradiction-analyzer | #10 |
| `frg-sparc-warden` | sparc-methodology | #9 |
| `frg-org-designer` | agent-factory + architect-agent | #6, #11 |

---

## Note di verifica (2026-06-16)
- Tutti i path `~/skills/*` e `~/commands/*` esistono e contengono `SKILL.md`/`.md` (verificato a build-time).
- `content-forge`: presente sia come skill globale eseguibile (`~/skills/content-forge/`) sia come
  archivio sorgente in `SKILL & Agenti/Content-forge/skill - FINALE/` (versione 2.0 zippata).
- `agent-factory`: NON una skill singola — è una suite di 4 sub-skill reali in `skills/` (vedi #11);
  azione dossier = **EVOLVI** (valutare merge con WF-AGENT-NEW).
- `architect-agent` e `build-implementation`: motori reali come **command** (`~/commands/`), non skill.
- `Skill Master Architecture`: directory di reference metodologico (Three-Level Architecture), non motore eseguibile.

## Connessioni
- [[ECOSISTEMA.md]] — i 5 reparti che orchestrano questi motori
- [[BACKBONE.md]] — gate e namespace `forge/*`
- [[../Funzioni]] — le funzioni L4 che invocano questi motori
- [[ARCHITETTURA/BACKBONE.md]] §"Motori reali wrappati" — i motori lato struttura (a monte)
