> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 WORKFLOW-WORKS · L3 WF-FORGE-PIPELINE

# WF-FORGE-PIPELINE — Workflow L3: Content-Forge (Raw → MKD → Artefatto)

**Ecosistema:** 07-FORGE · **Reparto:** WORKFLOW-WORKS (L2.3) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Trasformare **materia prima grezza** (transcript YouTube, registrazioni workshop, appunti
sparsi, brief interni, intere cartelle) in uno degli 8 target operativi di EMPIRE OS,
passando obbligatoriamente per il **MKD (Master Knowledge Document)** come documento
intermedio "perfetto". Motore: `content-forge` (`SKILL & Agenti/Content-forge/skill - FINALE/`,
433 file). Regola assoluta: **mai riassumere — sempre espandere**.

---

## I 8 target di output

| # | Target | Destinazione |
|---|---|---|
| 1 | Documento espanso | wiki/knowledge/ |
| 2 | Agente | WF-AGENT-NEW per 7-file + registro |
| 3 | Team multi-agente | WF-TEAM-NEW per schema canonico |
| 4 | Skill Anthropic Claude Code | WF-SKILL-NEW per eval e package |
| 5 | Workflow eseguibile | Workflow/ dell'ecosistema richiedente |
| 6 | Orchestration layer | Backbone / swarm script |
| 7 | Nota wiki Obsidian | second-brain-vault/wiki/ |
| 8 | Injection custom | system prompt n8n/CrewAI/LangGraph · RAG pack · template parametrizzato |

---

## Fasi del workflow

| Fase | Attore | Output | Regola critica |
|---|---|---|---|
| **Intake & classifica** | `frg-mkd-forger` | tipo fonte, target, link a INTELLIGENCE | fonte = riassunto di seconda mano → chiedi originale a INTELLIGENCE (G-INTEGRAL) |
| **Context check** | `frg-mkd-forger` | verifica completezza fonte | fonte incompleta → blocco; integra prima |
| **MKD** | `frg-mkd-forger` (content-forge) | Master Knowledge Document: espansione integrale della fonte | OBBLIGATORIO; mai saltato; MKD > fonte in ricchezza |
| **Target build** | `frg-mkd-forger` + reparto specializzato | artefatto nel formato target | un target alla volta; MKD riusabile per altri target dopo |
| **Archiviazione MKD** | `frg-mkd-forger` | MKD archiviato in `forge/builds/` + namespace `forge/mkd/` AgentDB | l'MKD è un asset permanente, non usa-e-getta |
| **Consegna** | `frg-chief` | artefatto all'ecosistema richiedente + entry wiki/log.md | handoff con acceptance_criteria misurabili |

---

## Regola "espandere, non riassumere"

Ogni atomo informativo della fonte diventa **più ricco** nell'MKD:
- esempio generico → esempio concreto con contesto DE
- concetto nudo → concetto + esempi + cross-reference con altri artefatti DE
- lista piatta → lista con rationale per ogni item
- sezione corta della fonte → sezione espansa con tutto ciò che il lettore ha bisogno di sapere

Un MKD più corto della fonte è un **bug** — si itera.

---

## Regola operativa con INTELLIGENCE

La FORGE **non inventa da zero** quando esiste materia prima. Prima di avviare content-forge:
1. Interroga `int-context-packer` (INTELLIGENCE): c'è materiale già ingerito su questo tema?
2. Se sì → content-forge parte dall'archivio Empire Studio (namespace `intelligence/`)
3. Se no → richiede a INTELLIGENCE ingestione (WF-INGEST-*) prima di procedere

---

## KPI

| Metrica | Target |
|---|---|
| MKD prodotti senza fase di archiviazione | 0 |
| Artefatti con MKD mancante | 0 |
| MKD riusati per secondo target | ≥ 20% (economia di scala) |
| Fonti accettate incomplete (senza G-INTEGRAL) | 0 |
