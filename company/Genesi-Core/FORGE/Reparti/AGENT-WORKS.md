# AGENT-WORKS — FORGE (Genesi Core)

## Missione (confine: FORGE costruisce CONTENUTO, ARCHITETTURA dà la STRUTTURA)
Forgia il **contenuto** delle persone digitali della holding: agenti singoli (L5) e team
completi (L3/L4). ARCHITETTURA consegna la forma vuota — `agente@vN` (7-file: identità,
missione, I/O, reasoning, tool, escalation, KPI) o `team@vN` (coordinator+workers, handoff,
shared_state, acceptance, failure handling) — e AGENT-WORKS ci scrive dentro l'identità reale,
il system prompt, la logica, i contratti di handoff. Non disegna l'organigramma (lo riceve):
lo **incarna**, lo testa con uno smoke test, lo registra. Motori reali: `architect-agent`, `agent-factory`.

## Team agenti (quali frg-* lavorano qui)
| id | ruolo | tier |
|---|---|---|
| `frg-org-designer` | incarna il team dentro lo schema canonico (system prompt, ruoli, handoff) | opus |
| `frg-skill-smith` | collega le skill agli agenti (pattern #6: l'agente USA la skill, non la duplica) | sonnet |
| `frg-hr-registrar` | assume/ritira agenti, traccia costo/performance in Identity-HR | haiku |
| `frg-chief` | Chief-Forge: approva ordine `agente`/`team`, chiude la consegna | opus |

## Workflow di competenza
- **WF-AGENT-NEW** — blueprint agente da ARCHITETTURA → `architect-agent` riempie i 7-file → smoke test reale → registro Identity-HR.
- **WF-TEAM-NEW** — blueprint team L3/L4 → coordinator+workers reali, handoff contract scritti, shared_state schema istanziato, acceptance + escalation → smoke test team → registro.

## Funzioni L4
1. **T-identity** — scrive identità + missione + system prompt dentro la forma 7-file.
2. **T-handoff-contracts** — istanzia i contratti I/O concreti tra membri del team (da forma a JSON reale).
3. **T-shared-state-schema** — riempie lo schema `shared_state` con namespace e chiavi reali.
4. **T-skill-binding** — referenzia le skill che l'agente usa (mai inglobare conoscenza nel prompt).
5. **T-smoke-test** — fa eseguire all'agente/team un task reale piccolo; fallisce → itera, non registra.

## Handoff Contract
- **Riceve** da ARCHITETTURA (**HC-ARCH-FORGE**): `{request_id, blueprint_ref, schema_usato:"agente@vN"|"team@vN", spec_ref, pattern_riusati[], validazione:"PASS"}` → `WF-AGENT-NEW`/`WF-TEAM-NEW`.
- **Costruisce**: contenuto dei 7-file / del team dentro la forma. Tier al ribasso (il più economico che regge). Buco strutturale → ritorno ad ARCHITETTURA.
- **Consegna** a MAXIMILIAN → Mandato → **Identity-HR** (assunzione) + OPERATIONS (cost model). Output: `{agent_id, tier, costo_stimato, smoke:"PASS", skills_usate[]}`.

## Flusso interno (passi reali)
```
blueprint agente@vN | team@vN (PASS) da ARCHITETTURA
  → frg-chief: ordine approvato? memory_search forge/registry → esiste agente affine? → estendi, non duplicare
  → frg-org-designer: riempie identità/prompt/logica dentro la forma 7-file (o roster del team)
  → frg-skill-smith: binding skill (referenzia, non duplica)
  → smoke test reale (task piccolo); fallisce → itera (max 2 cicli, poi escala)
  → frg-hr-registrar: G-REGISTRY → Identity-HR + evento costo a OPERATIONS
  → consegna a MAXIMILIAN → Mandato → VIVO
Output: forge/builds/<request_id> + agente/team registrato in registro-agenti.yaml
```

## Gate
- **G-SPEC** — spec validata ereditata dal blueprint (problema concreto, non "riempire schema").
- **G-EVAL** — smoke test PASS su task reale: non si registra un agente mai testato.
- **G-CONTRADICTION** — nessun agente fotocopia (stesso ruolo, nome diverso) vs registro esistente.
- **G-REGISTRY** — Identity-HR aggiornato + tier/costo dichiarati a OPERATIONS: agente non censito = non esiste.
- **G-MKD/PRD** — se l'agente nasce da raw, l'MKD/PRD di WORKFLOW-WORKS è prerequisito.

## shared_state / memoria (namespace forge/...)
- `forge/queue/<request_id>` — ordine di forgiatura agente/team.
- `forge/builds/<request_id>` — draft 7-file, smoke test report, versioni.
- `forge/registry/agents` — registro-agenti.yaml: ruolo, tier, costo, pass_rate per ogni agente.
- `patterns` (ReasoningBank) — pattern di team che funzionano (riuso anti-reinvenzione).

## KPI
| KPI | Target |
|---|---|
| Artefatti conformi a schema canonico al primo audit | ≥ 90% |
| Agenti registrati con smoke test PASS | 100% |
| Agenti duplicati creati (stesso ruolo) | 0 |
| Copertura registro Identity-HR | 100% agenti |
| Quota agenti su tier economico (WASM/Haiku) | ≥ 70% |

## Connessioni
- [[../../ARCHITETTURA/Workflow/WF-ARCH-DESIGN]] — fornisce il blueprint agente@vN/team@vN (HC-ARCH-FORGE)
- [[../../ARCHITETTURA/Schemi-Canonici/Schema-Agente]] · [[../../ARCHITETTURA/Schemi-Canonici/Schema-Team]] — le forme vuote che questo reparto riempie
- [[SKILL-WORKS]] — gli agenti USANO le skill forgiate lì (pattern #6)
- [[ECOSYSTEM-WORKS]] — fornisce i roster L5 quando l'ordine è un ecosistema intero
- [[../../../Ecosistemi/07-FORGE/Reparti/AGENT-WORKS/README]] — stub v1 di questo reparto

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 AGENT-WORKS + 14-DOSSIER-ARCHITETTURA · Standard CF-grade · 2026-06-16*
