# WF-PRD
## Blueprint documento (da ARCHITETTURA) → PRD tipo A-E con quality score

> Organo: FORGE (Genesi Core) · Reparto owner: L2.3 WORKFLOW-WORKS · Stato: DEFINED
> Riceve un **blueprint documento validato** da ARCHITETTURA (HC-ARCH-FORGE, schema `documento@v1`
> con tipo PRD A-E scelto) e ci scrive il CONTENUTO via `prd-architect-os`. Genera con 4 engine
> (Intake → Context Enrichment → Generation → Validation) e chiude con un quality score 0-100.
> Bloccante: context score < 60 → niente generazione. Collega: [[WF-ARCH-DESIGN]] · [[WF-FORGE-PIPELINE]]

---

## Trigger
- Arriva da ARCHITETTURA un blueprint con `forma_scelta = "documento"` e sottotipo `prd`.
- PLATFORM (WF-SAAS-BUILD) o INFO-BUSINESS (lanci) chiedono una spec di costruzione/lancio.
- `WF-ECOSYSTEM-NEW` richiede il PRD Enterprise (tipo A) come dossier iniziale dell'ecosistema nuovo.
- **Natura:** specializzazione "documento PRD" di WF-FORGE-PIPELINE; il PRD è il deliverable delle fasi S-P di SPARC.

---

## Input (JSON)
```json
{
  "request_id": "ARCH-2026-0617-040",
  "blueprint_ref": "architettura/blueprint/ARCH-2026-0617-040",
  "schema_usato": "documento@v1",
  "forma_scelta": "documento",
  "sottotipo": "prd",
  "tipo_prd": "A | B | C | D | E",
  "validazione": "PASS",
  "prodotto": "es. SaaS book-factory",
  "committente": "06-PLATFORM | 02-INFO-BUSINESS | FORGE-ecosystem"
}
```
- `validazione != PASS` → rigetto ad ARCHITETTURA.

---

## I 5 tipi di PRD (A-E)
| Tipo | Nome | Quando | Lunghezza |
|---|---|---|---|
| A | Enterprise | prodotto complesso, team grande, roadmap multi-fase | 10-30 pagine |
| B | MVP Lean | validazione rapida con risorse minime | 3-5 pagine |
| C | Feature Spec | singola feature su prodotto esistente | 2-4 pagine |
| D | Vibecoding AI-Ready | spec per build AI-assisted (Claude, Cursor) | 4-8 pagine + prompt |
| E | PR/FAQ Amazon-style | focus outcome utente, lavora a ritroso | 3-6 pagine |

---

## Pipeline (passi · agente owner — i 4 engine prd-architect-os)
```
1. APERTURA + INTAKE                   (frg-chief → frg-prd-architect · Intake Engine)
   └── verifica PASS; raccoglie tipo prodotto, audience, vincoli, obiettivi, budget → intake completo

2. CONTEXT ENRICHMENT                  (frg-prd-architect + INTELLIGENCE · Context Engine)
   └── interroga wiki/AgentDB + competitor → calcola context score → G-CONTEXT ≥60 o blocco

3. GENERATION                          (frg-prd-architect · Generation Engine)
   └── PRD nel tipo A-E scelto, sezioni obbligatorie per tipo, dentro la struttura del blueprint

4. VALIDATION                          (frg-prd-architect + frg-eval-runner · Validation Engine)
   └── quality score 0-100 con breakdown per sezione → G-QUALITY ≥75 o iterazione

5. APPROVAZIONE + CONSEGNA              (frg-chief + frg-prd-architect)
   └── sign-off in handoff · archivio forge/prds/ · consegna a MAXIMILIAN → Mandato → committente
```

---

## Gate
- **G-FORGE0:** `validazione != PASS` → rigetto ad ARCHITETTURA.
- **G-CONTEXT (bloccante):** context score < 60 dopo l'enrichment → generazione BLOCCATA; `frg-prd-architect` apre richiesta a INTELLIGENCE (quali dati mancano?) e torna all'Intake. Nessuna eccezione.
- **G-QUALITY:** quality score ≥ 75/100 o iterazione.
- **G-ARCHIVE:** PRD consegnato senza archiviazione in `forge/prds/` = 0.

---

## Output (JSON)
```json
{
  "request_id": "ARCH-2026-0617-040",
  "prd_ref": "forge/prds/ARCH-2026-0617-040",
  "tipo_prd": "B",
  "context_score": 72,
  "quality_score": 81,
  "build_ref": "forge/builds/ARCH-2026-0617-040",
  "handoff_to": "MAXIMILIAN",
  "destinatario": "06-PLATFORM/WF-SAAS-BUILD",
  "status": "delivered"
}
```

---

## Handoff
- **In ingresso:** HC-ARCH-FORGE da `WF-ARCH-DESIGN` (blueprint documento validato, sottotipo PRD).
- **In uscita:** consegna a **MAXIMILIAN** (all'altezza?) → **Mandato** (lecito?) → **Identity-HR** (registra l'artefatto) → destinatario reale: PLATFORM WF-SAAS-BUILD (tipo B/D), INFO-BUSINESS lanci (tipo A/E), FORGE WF-ECOSYSTEM-NEW (tipo A).
- **Confine:** ARCHITETTURA fissa tipo/struttura del documento; WORKFLOW-WORKS scrive il contenuto. Cambio di struttura = nuovo giro ARCH.

---

## Dry-run
Blueprint validato di un PRD tipo B per "SaaS book-factory". Intake completo, context enrichment da wiki
INTELLIGENCE → context score 72 (>60, si procede), generation del PRD B (3-5 pagine), validation →
quality score 81 (>75), archivio in `forge/prds/` → consegna a MAXIMILIAN, destinatario PLATFORM. Caso di
blocco: context score 48 → generation NON parte, richiesta dati a INTELLIGENCE, ritorno a Intake.

---

## Connessioni
- [[WF-ARCH-DESIGN]] — produce il blueprint documento in ingresso
- [[WF-FORGE-PIPELINE]] — motore generale di cui questo è la specializzazione "documento PRD"
- [[WF-ECOSYSTEM-NEW]] — consuma il PRD tipo A come dossier dell'ecosistema nuovo
- [[frg-prd-architect]] · [[frg-eval-runner]] · [[frg-chief]] — agenti owner
- [[06-ECOSISTEMI-CORE]] §07 L2.3 WORKFLOW-WORKS — fonte di verità
