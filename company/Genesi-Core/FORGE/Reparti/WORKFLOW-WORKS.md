# WORKFLOW-WORKS — FORGE (Genesi Core)

## Missione (confine: FORGE costruisce CONTENUTO, ARCHITETTURA dà la STRUTTURA)
Forgia il **contenuto** di documenti operativi, workflow e orchestrazioni. ARCHITETTURA
consegna la forma — `workflow@vN` (trigger, input, pipeline a passi, gate, output, owner,
dry-run) o `documento/MKD@vN` (struttura, atomi informativi, cross-ref) — e WORKFLOW-WORKS
ci scrive dentro la sostanza: l'MKD espanso, il PRD completo, i passi reali della pipeline.
È la sede dei due motori documentali più potenti della FORGE: **content-forge** (raw → MKD →
target) e **prd-architect-os** (PRD A–E con quality score). Regola assoluta: **mai riassumere, sempre espandere**.

## Team agenti (quali frg-* lavorano qui)
| id | ruolo | tier |
|---|---|---|
| `frg-mkd-forger` | operatore `content-forge`: raw → MKD → target (doc/agent/team/skill/workflow/orchestration/wiki/custom) | sonnet |
| `frg-prd-architect` | operatore `prd-architect-os`: PRD tipo A–E con quality score 0–100 | sonnet |
| `frg-eval-runner` | verifica quality score PRD e completezza MKD | haiku |
| `frg-chief` | Chief-Forge: classifica la fonte, approva la consegna | opus |

## Workflow di competenza
- **WF-FORGE-PIPELINE** (motore `content-forge`) — da raw (transcript, registrazioni, appunti, brief, cartelle) a uno di 8 target. **Passaggio obbligato: l'MKD** (Master Knowledge Document), il documento perfetto intermedio da cui qualsiasi target si forgia.
- **WF-PRD** (motore `prd-architect-os`) — PRD tipo A (Enterprise) · B (MVP Lean) · C (Feature Spec) · D (Vibecoding) · E (PR/FAQ). 4 engine: Intake → Context Enrichment → Generation → Validation. Bloccato se context score < 60.

## Funzioni L4
1. **T-source-classify** — raw testuale/cartella → content-forge; idea/requisiti → prd-architect-os.
2. **T-mkd-build** — espande ogni atomo della fonte in MKD (più ricco, mai più corto: MKD < fonte = bug).
3. **T-target-cast** — dall'MKD forgia il target richiesto (uno alla volta; gli altri restano forgiabili).
4. **T-prd-generate** — PRD del tipo giusto con i 4 engine e quality score.
5. **T-validate** — quality score PRD ≥ 75; MKD completo (G-INTEGRAL: fonte integrale, mai di seconda mano).

## Handoff Contract
- **Riceve** da ARCHITETTURA (**HC-ARCH-FORGE**): `{request_id, blueprint_ref, schema_usato:"workflow@vN"|"documento/MKD@vN", spec_ref, validazione:"PASS"}` — più la materia prima (referenziata da INTELLIGENCE).
- **Costruisce**: l'MKD/PRD/workflow dentro la forma. Quando il target è skill/agente/team → handoff interno a SKILL-WORKS / AGENT-WORKS.
- **Consegna** a MAXIMILIAN → Mandato → registro/wiki; l'MKD si archivia (riusabile). Output: `{mkd_ref|prd_ref, quality_score, target_prodotto}`.

## Flusso interno (passi reali)
```
blueprint workflow@vN | documento@vN (PASS) + materia prima da INTELLIGENCE
  → frg-chief: classifica fonte (raw → content-forge | requisiti → prd-architect-os)
  → content-forge: fonte INTEGRALE? (G-INTEGRAL) → costruisce MKD espandendo ogni atomo
       PRD: context score ≥ 60? no → torna a Intake
  → frg-mkd-forger | frg-prd-architect: dall'MKD/4-engine forgia il target / il PRD
  → frg-eval-runner: quality score (PRD ≥ 75) | completezza MKD
  → target skill/agente/team? → handoff a SKILL-WORKS / AGENT-WORKS
  → archivia MKD in forge/builds (mai buttato) → consegna a MAXIMILIAN
Output: forge/builds/<request_id>/mkd + target prodotto
```

## Gate
- **G-SPEC** — spec validata ereditata dal blueprint.
- **G-MKD/PRD** — content-forge **non salta MAI l'MKD**; PRD bloccato se context score < 60.
- **G-EVAL** — PRD quality score ≥ 75/100; MKD non più corto della fonte (espansione provata).
- **G-CONTRADICTION** — se il target è skill/agente, l'analyzer gira a valle nei reparti destinatari.
- **G-REGISTRY** — target consegnato registrato (skills-map / Identity-HR / wiki) + MKD archiviato.

## shared_state / memoria (namespace forge/...)
- `forge/queue/<request_id>` — ordine di forgiatura documentale.
- `forge/builds/<request_id>/mkd` — l'MKD intermedio (asset riusabile, mai cancellato).
- `forge/builds/<request_id>/prd` — il PRD con quality score e log di Validation.
- `patterns` (ReasoningBank) — pattern di espansione MKD che hanno alzato il valore del target.

## KPI
| KPI | Target |
|---|---|
| PRD quality score (prd-architect-os) | ≥ 75/100 |
| Build content-forge con MKD prodotto (mai saltato) | 100% |
| MKD più ricchi della fonte (espansione, non riassunto) | 100% |
| MKD archiviati e riutilizzati per ≥1 target ulteriore | trend ↑ |
| Tempo richiesta → MKD/PRD consegnato | ≤ 2 giorni |

## Connessioni
- [[../../ARCHITETTURA/Workflow/WF-ARCH-DESIGN]] — fornisce il blueprint workflow@vN / documento@vN (HC-ARCH-FORGE)
- [[../../ARCHITETTURA/Schemi-Canonici/Schema-Workflow]] · [[../../ARCHITETTURA/Schemi-Canonici/Schema-Documento-MKD]] — le forme vuote che questo reparto riempie
- [[SKILL-WORKS]] · [[AGENT-WORKS]] — destinatari quando il target dell'MKD è skill/agente/team
- [[METHOD-GUARD]] — l'MKD/PRD è il deliverable delle fasi S-P di SPARC
- [[../../../Ecosistemi/07-FORGE/Reparti/WORKFLOW-WORKS/README]] — stub v1 di questo reparto

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 WORKFLOW-WORKS + 14-DOSSIER-ARCHITETTURA · Standard CF-grade · 2026-06-16*
