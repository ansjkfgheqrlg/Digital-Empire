# FORGE — BACKBONE (infrastruttura dell'organo)

> La spina dorsale della FORGE dentro il Genesi Core: memoria, handoff in ingresso/uscita,
> gate, dipendenze. La topologia swarm e il registro skill restano in [[07-FORGE/BACKBONE.md]].
> Fonte: [[06-ECOSISTEMI-CORE]] §07 · [[07-BACKBONE-RUFLO-SKILLS]]. Collega: [[ECOSISTEMA.md]]

---

## Namespace memoria — `forge/*` (AgentDB)
| Namespace | Contenuto | Test-amnesia |
|---|---|---|
| `forge/builds` | ordini ricevuti e build in corso `{ordine, blueprint, target, status}` | `forge/builds/<id>` ricostruisce a freddo cosa si sta forgiando |
| `forge/evals` | risultati eval e benchmark (pass_rate, variance, baseline vs post) | da qui si carica lo storico qualità di ogni artefatto |
| `forge/registry` | specchio operativo di Identity-HR (agenti forgiati: ruolo, tier, costo, performance) | da qui si verifica chi è assunto/ritirato |
| `forge/templates` | template agenti/skill/team riusabili (no reinvenzione) | il forger legge qui prima di costruire |

**ReasoningBank:** i fallimenti di forgiatura (eval falliti, contraddizioni rilevate) diventano
pattern → la FORGE sbaglia meno alla forgiatura successiva (`reasoningbank-*` via Ruflo).
Memoria operativa (checkpoint, ADR): ecosistema 10 MEMORY (`company/Memory/`) — memory-first #13.

---

## Handoff in INGRESSO (chi manda ordini qui)
| Da | Handoff | Cosa arriva |
|---|---|---|
| **ARCHITETTURA** (gemella) | `HC-ARCH-FORGE` | blueprint validato `{spec, struttura, schema}` → entra in WF-FORGE-PIPELINE / WF-SKILL-NEW / WF-AGENT-NEW / WF-TEAM-NEW. **Niente build senza blueprint.** |
| **ARCHITETTURA** | `HC-ARCH-FORGE-ECO` | org L1→L5 + BACKBONE + bozza dossier → WF-ECOSYSTEM-NEW (costruzione reale dell'ecosistema) |
| **QUALSIASI ecosistema** | ordine capability | `{capability_mancante, contesto, KPI_attesi, budget}` — `frg-chief` lo accoda, poi lo inoltra ad ARCHITETTURA per la forma |
| **INTELLIGENCE** | materia prima | materiale raw ingerito (Empire Studio) + pattern ReasoningBank → input per content-forge |
| **Board (L0)** | mandato ecosistema | mandato ratificato → catena ARCHITETTURA (WF-ECOSYSTEM-DESIGN) → FORGE (WF-ECOSYSTEM-NEW) |

## Handoff in USCITA (a chi consegna)
| A | Handoff | Cosa parte |
|---|---|---|
| **MAXIMILIAN** | `HC-FORGE-MAX` | artefatto costruito + eval report → gate "è all'altezza di Max?" (dopo G-EVAL) |
| **Mandato** | `HC-FORGE-MANDATO` | artefatto approvato da MAXIMILIAN → gate liceità prima della registrazione |
| **Identity-HR** | `HC-FORGE-HR` | assunzione/ritiro: `registro-agenti.yaml` aggiornato (`frg-hr-registrar`) — poi VIVO |
| **Ecosistema richiedente** | consegna | asset installato (skill in `.claude/skills/`, agente/team nel reparto target) + eval report |
| **INTELLIGENCE** | pagina wiki | ogni artefatto → wiki `tools/` + log; enrichment skill esistenti passa per Memory Empire |
| **OPERATIONS** | evento costo | ogni nuovo agente dichiara tier + costo stimato → budget guard pre-approvazione |

---

## Gate dell'organo (catena, nessuno si salta)
**G-SPEC → G-MKD/PRD → G-EVAL → G-CONTRADICTION → G-REGISTRY**
- **G-SPEC** — spec approvata (`frg-spec-writer`) prima di costruire (requisiti, acceptance, out-of-scope).
- **G-MKD/PRD** — documento intermedio completo: content-forge non salta MAI l'MKD; PRD bloccato se context score <60.
- **G-EVAL** — eval ≥ soglia (skill: ≥85% pass) — `frg-eval-runner`.
- **G-CONTRADICTION** — skill-contradiction-analyzer verde vs skill esistenti (anti-drift) — `frg-contradiction-gate`.
- **G-REGISTRY** — Identity-HR aggiornato (artefatto senza registro = artefatto non consegnato) — `frg-hr-registrar`.

Prima della consegna, due gate Genesi Core esterni in serie: **MAXIMILIAN** (standard/visione) e
**Mandato** (liceità). A monte, ARCHITETTURA ha già passato `struct-gate` (G-ARCH1: niente build al buio).
In più: pattern #7 progressive disclosure (kernel ≤500 righe) e pattern #1 schema team canonico, a ogni audit.

---

## Dipendenze
- **A monte:** ARCHITETTURA (blueprint validato, committente diretto) · INTELLIGENCE (materia prima/Empire Studio) · Board (mandati ecosistema).
- **A valle:** MAXIMILIAN + Mandato (gate Genesi Core) · Identity-HR (registra) · ecosistema richiedente (riceve) · OPERATIONS (budget) · INTELLIGENCE (wiki).
- **Trasversale:** AgentDB (namespace `forge/*`) · i motori reali (`Motori/Mappa-Motori.md`) · ciclo a 9 passi ([[10-METODO-CICLO-FASE]]) · topologia star (vedi [[07-FORGE/BACKBONE.md]]).

---

## Confine d'infrastruttura
La FORGE possiede `forge/*` e la catena gate G-SPEC→G-REGISTRY. **Non** possiede gli schemi canonici
(`architettura/schemi`, di ARCHITETTURA), né il giudizio di standard (MAXIMILIAN), né l'enforcement
di liceità (Mandato). Riceve la forma vuota da ARCHITETTURA, la riempie, la valuta, la consegna.

---

## Connessioni
- [[ECOSISTEMA.md]] — porta d'ingresso dell'organo
- [[Motori/Mappa-Motori.md]] — i motori reali wrappati (ciò che rende la FORGE viva)
- [[ARCHITETTURA/BACKBONE.md]] — il gemello a monte (consegna `HC-ARCH-FORGE`)
- [[07-FORGE/BACKBONE.md]] — topologia star, BUS, registro skill (livello ecosistema L1)
- [[06-ECOSISTEMI-CORE]] §07 · [[07-BACKBONE-RUFLO-SKILLS]] — fonte di verità
