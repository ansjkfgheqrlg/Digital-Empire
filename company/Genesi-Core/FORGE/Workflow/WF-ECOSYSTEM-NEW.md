# WF-ECOSYSTEM-NEW
## Blueprint org L2.5 (da ARCHITETTURA) → ecosistema completo costruito

> Organo: FORGE (Genesi Core) · Reparto owner: L2.4 ECOSYSTEM-WORKS · Stato: DEFINED (F9+)
> Il livello massimo della FORGE. Riceve da ARCHITETTURA la **org-blueprint completa L2-L5 validata**
> (prodotta dal ramo `WF-ECOSYSTEM-DESIGN` di L2.5 Progettazione-Ecosistemi) e ci costruisce dentro
> il CONTENUTO: ECOSISTEMA.md, BACKBONE.md, agenti reali, namespace memoria, dossier PIANO-MAESTRO.
> Mai inventa l'org chart — arriva architettata e PASS. Collega: [[WF-ARCH-DESIGN]] · [[WF-ECOSYSTEM-DESIGN]]

---

## Trigger
- Arriva da ARCHITETTURA un blueprint con `forma_scelta = "ecosistema"` (HC-ARCH-FORGE), prodotto dal ramo `WF-ECOSYSTEM-DESIGN` (L2.5).
- **Attivazione SOLO con mandato Board (L0) ratificato** via hive-mind consensus (raft).
- Primo uso previsto: ecosistema E-commerce (F9+ roadmap, build FORGE F5).
- **Natura:** regola "tutto o niente" — un ecosistema mezzo-scaffoldato non si consegna.

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0701-001",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0701-001",
  "schema_usato": "ecosistema@v1",
  "forma_scelta": "ecosistema",
  "validazione": "PASS",
  "org_l2_l5": "blueprint completo reparti L2 / workflow L3 / funzioni L4 / roster L5",
  "mandato_board": { "missione": "...", "revenue_model": "...", "done_when": "...", "budget": "...", "sponsor": "..." },
  "dossier_intelligence": "intelligence/research/<eco>",
  "business_case_ops": "operations/cost-model/<eco>"
}
```
- `validazione != PASS` OR `mandato_board` incompleto (5 campi) → rigetto. Niente scaffold al buio.

---

## Prerequisiti (gate d'ingresso — tutti obbligatori)
1. **Mandato Board completo**: missione, revenue model, DONE WHEN, budget, sponsor C-Suite.
2. **Dossier INTELLIGENCE**: ricerca mercato + competitor + trend (WF-COMPETITOR + WF-TREND).
3. **Business case OPERATIONS**: costo di run stimato dell'ecosistema prima di scaffoldare.
4. **ADR in Memory**: decisione registrata in `company/Memory/decisions/`.

---

## Pipeline (passi · agente owner)
```
1. MANDATO + PRD CHECK                 (frg-chief)
   └── verifica PASS + 5 campi mandato + prerequisiti; PRD Enterprise (tipo A) via WF-PRD → quality ≥75

2. SCAFFOLD FILESYSTEM                  (frg-skill-smith · skill ecosystem-scaffold)
   └── Reparti/ Workflow/ Funzioni/ Agenti/ + ECOSISTEMA.md + BACKBONE.md DENTRO la org-blueprint

3. NAMESPACE MEMORIA                    (frg-hr-registrar)
   └── ruflo memory init --namespace <eco> → risponde a memory_search

4. AGENTI L5 (per ogni ruolo roster)    (WF-AGENT-NEW + WF-TEAM-NEW, in parallelo)
   └── ogni agente/team del roster creato, smoke-testato, registrato

5. DOSSIER PIANO-MAESTRO                 (frg-prd-architect + frg-org-designer)
   └── nuovo file 0N-ECOSISTEMA-*.md proposto alla Board per ratifica

6. DRY-RUN + REGISTRAZIONE HOLDING       (frg-chief + frg-hr-registrar)   →  vedi Gate
   └── verify.sh verde · handoff coerenti con gli altri ecosistemi · skills-map + registro + GRUPPO.md
   └── consegna a MAXIMILIAN → Mandato → Identity-HR → ecosistema VIVO
```

---

## Gate
- **G-FORGE0:** `validazione != PASS` o mandato incompleto → rigetto.
- **G-PRD:** PRD Enterprise (tipo A) con quality score ≥ 75 prima dello scaffold.
- **G-CANONICO:** org conforme allo scheletro degli altri 9 ecosistemi (zero divergenze dallo schema canonico).
- **G-DRYRUN:** struttura navigabile (verify.sh cat.1 verde) + handoff fittizio coerente con gli altri + namespace risponde + ≥1 agente reale smoke-verde, PRIMA del go-live.
- **G-TUTTO-O-NIENTE:** manca uno dei deliverable (org / ECOSISTEMA+BACKBONE / dossier / namespace / registro) → **rollback** (elimina scaffold parziale + ADR di rollback in Memory).

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0701-001",
  "ecosistema_id": "11-ECOMMERCE",
  "path": "company/Ecosistemi/11-ECOMMERCE/",
  "dossier_piano_maestro": "PIANO-MAESTRO/11-ECOSISTEMA-ECOMMERCE.md",
  "namespace_memoria": "ecommerce",
  "agenti_registrati": 14,
  "build_ref": "forge/builds/ARCH-2026-0701-001",
  "dryrun": "PASS",
  "handoff_to": "MAXIMILIAN",
  "status": "delivered"
}
```

---

## Handoff
- **In ingresso:** HC-ARCH-FORGE da `WF-ECOSYSTEM-DESIGN` (org-blueprint completa L2-L5 validata).
- **In sub-flusso:** `WF-PRD` (tipo A), `WF-AGENT-NEW` + `WF-TEAM-NEW` (roster).
- **In uscita:** consegna a **MAXIMILIAN** (all'altezza?) → **Mandato** (lecito? ratifica Board) → **Identity-HR** (registra agenti + skills-map + GRUPPO.md) → ecosistema VIVO.
- **Confine:** ARCHITETTURA disegna l'org intera; ECOSYSTEM-WORKS la costruisce. Cambio di org = nuovo giro WF-ECOSYSTEM-DESIGN.

---

## Dry-run
Mandato Board per E-commerce ratificato + org-blueprint validata da ARCHITETTURA. frg-skill-smith
scaffolda l'albero, namespace `ecommerce` inizializzato, roster spawnato via WF-AGENT-NEW/WF-TEAM-NEW,
dossier `11-ECOSISTEMA-ECOMMERCE.md` proposto, verify.sh verde, handoff fittizio coerente con gli altri 10
→ consegna a MAXIMILIAN. Caso rollback: manca il namespace → scaffold eliminato + ADR di rollback.

---

## Connessioni
- [[WF-ECOSYSTEM-DESIGN]] — ramo ARCHITETTURA L2.5 che produce l'org-blueprint in ingresso
- [[WF-ARCH-DESIGN]] — instrada qui le richieste di tipo ecosistema (passo 1)
- [[WF-PRD]] · [[WF-AGENT-NEW]] · [[WF-TEAM-NEW]] — sub-flussi
- [[frg-org-designer]] · [[frg-skill-smith]] · [[frg-prd-architect]] · [[frg-hr-registrar]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.4 ECOSYSTEM-WORKS — fonte di verità
