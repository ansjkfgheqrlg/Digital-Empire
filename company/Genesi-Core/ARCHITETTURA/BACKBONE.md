# ARCHITETTURA — BACKBONE (infrastruttura dell'organo)

> La spina dorsale dell'organo ARCHITETTURA: memoria, handoff, gate, motori reali wrappati, dipendenze.
> Fonte: [[14-DOSSIER-ARCHITETTURA]] §6 (relazioni) · §7 (state) · §9 (gerarchia). Collega: [[ECOSISTEMA.md]]

---

## Namespace memoria — `architettura/*` (AgentDB)
| Namespace | Contenuto | Test-amnesia |
|---|---|---|
| `architettura/schemi` | le 9 forme/schemi canonici **versionati** (es. `skill@v3`, `agente@v2`) — la costituzione | da qui si carica lo schema di ogni tipo |
| `architettura/blueprint` | ogni blueprint prodotto `{richiesta→spec→struttura→validazione}` | `architettura/blueprint/<id>` ricostruisce a freddo il design |
| `architettura/pattern` | libreria pattern riusabili della Pattern Guild | anti-reinvenzione: lo scout legge qui prima di disegnare |
| `architettura/validazioni` | esiti `struct-gate` per audit + ReasoningBank (buchi ricorrenti) | alimenta WF-SCHEMA-EVOLVE |

**ReasoningBank:** i buchi strutturali ricorrenti ("dimenticano sempre l'escalation") diventano pattern →
lo schema canonico si rafforza (WF-SCHEMA-EVOLVE) → la FORGE sbaglia meno.

---

## Handoff in INGRESSO (chi manda richieste qui)
| Da | Handoff | Cosa arriva |
|---|---|---|
| **07-FORGE** (conductor) | richiesta design | `{tipo, scopo, vincoli}` → entra in WF-ARCH-DESIGN (la FORGE non inventa strutture) |
| **Board (L0)** | mandato ecosistema | mandato ratificato → WF-ECOSYSTEM-DESIGN |
| **Qualsiasi ecosistema** | richiesta artefatto | passa dalla FORGE che la inoltra qui per la forma |
| **MAXIMILIAN / Mandato** | check strutturale | chiamano `struct-gate` (WF-STRUCT-VALIDATE) prima del proprio gate |

## Handoff in USCITA (a chi consegna)
| A | Handoff | Cosa parte |
|---|---|---|
| **07-FORGE / WF-FORGE-PIPELINE** | `HC-ARCH-FORGE` | blueprint validato → la FORGE costruisce il CONTENUTO |
| **07-FORGE / WF-SKILL-NEW · WF-AGENT-NEW · WF-TEAM-NEW** | `HC-ARCH-FORGE` | blueprint del tipo specifico |
| **07-FORGE / WF-ECOSYSTEM-NEW** | `HC-ARCH-FORGE-ECO` | org L1→L5 + BACKBONE + bozza dossier → costruzione reale |
| **10-MEMORY / WF-ADR-REGISTER** | `HC-ME-ADR` | ADR quando uno schema canonico evolve (WF-SCHEMA-EVOLVE) |

---

## Gate dell'organo
- **struct-gate** ([[WF-STRUCT-VALIDATE]]) — il gate strutturale deterministico della holding: `{COMPLETO|INCOMPLETO, buchi:[…]}`
  vs schema canonico. Bloccante. Usato **pre-FORGE** (blueprint completo?) e **post-FORGE** (il costruito rispetta il blueprint?).
  Owner: `arch-validator` + `arch-contradiction`. È parte del passo 4 (GATE) del ciclo a 9 passi.
- **G-ARCH1:** nessun blueprint non-validato passa alla FORGE (niente costruzione al buio).

---

## Motori reali wrappati (no documentazione morta — §8 PRE-MORTEM R1)
Ogni schema/blueprint/gate è **wireable a un motore nativo esistente**, non solo descritto:
| Funzione | Motore reale |
|---|---|
| Spec / requirements | `agent-specification` · `prd-architect-os` |
| Blueprint struttura artefatto | `architect-agent` · `agent-architecture` |
| Metodo Spec→Pseudo→Arch | `sparc-methodology` (SPARC) |
| Forma skill | `skill-creator` · Skill Master Architecture |
| Forma agente | `agent-factory` / agent-architect |
| Anti-contraddizione | `skill-contradiction-analyzer` |
| Org design ecosistemi | org-design (motore L2.5) |
| Fan-out parallelo (scout ‖ spec) | `swarm-orchestration` |

---

## Dipendenze
- **A monte:** 07-FORGE (committente principale) · Board (mandati ecosistema) · INTELLIGENCE (dossier mercato per WF-ECOSYSTEM-DESIGN).
- **A valle:** 07-FORGE (riceve i blueprint e costruisce) · MAXIMILIAN + Mandato (gate successivi) · Identity-HR (registra) · 10-MEMORY (ADR).
- **Trasversale:** AgentDB (namespace `architettura/*`) · `swarm-orchestration` (fan-out) · ciclo a 9 passi ([[10-METODO-CICLO-FASE]]).

---

## Confine d'infrastruttura
ARCHITETTURA possiede `architettura/*` e lo `struct-gate`. **Non** possiede la costruzione del contenuto
(`forge/*`), né il giudizio di standard (MAXIMILIAN), né l'enforcement di liceità (Mandato). La forma vuota
esce da qui; tutto il resto è a valle.

---

## Connessioni
- [[ECOSISTEMA.md]] — porta d'ingresso dell'organo
- [[WF-ARCH-DESIGN]] · [[WF-STRUCT-VALIDATE]] · [[WF-ECOSYSTEM-DESIGN]] · [[WF-SCHEMA-EVOLVE]] — i 4 workflow
- [[14-DOSSIER-ARCHITETTURA]] §6–§7–§9 — fonte di verità
- 07-FORGE: ECOSISTEMA.md · BACKBONE.md · WF-FORGE-PIPELINE · WF-ECOSYSTEM-NEW — il gemello costruttore
