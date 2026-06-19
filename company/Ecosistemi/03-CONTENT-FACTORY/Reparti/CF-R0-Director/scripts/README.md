---
Type: SCRIPTS
Status: Active
Tags: #scripts #content-factory #cf-r0 #cf-order #order-validator #capacity-planner
Created: 2026-06-19
Last updated: 2026-06-19
---

# Scripts — CF-R0 Director

> **Reparto:** CF-R0 · **Ecosistema:** 03-CONTENT-FACTORY · **Versione:** v2

---

## Skill wrappata: `cf-order`

La skill `cf-order` esiste come asset v1 (NON viene riscritta — ADR-003). CF-R0 la
utilizza come motore di intake e creazione struttura cartella ordine nel workflow
WF-ORDER-INTAKE. Il wrapper v2 aggiunge i layer mancanti in v1:

| Layer aggiunto in v2 | Responsabile wrapper |
|---|---|
| Validazione brand_kit contro registry CF-R2 (multi-tenant) | cf-d-qa |
| Verifica icp.json con schema completo | cf-d-qa |
| Capacity check via cf-d-sched prima del dispatch | cf-d-sched |
| Budget check via cf-d-budget con stime reparti | cf-d-budget |
| Scrittura trace.jsonl (struttura di tracciabilità v2) | cf-d-dispatch |

**Come invocare:** la skill `cf-order` viene richiamata nel contesto del workflow
WF-ORDER-INTAKE, step 6 (cf-d-dispatch). Non viene chiamata direttamente dai
committenti — l'ingresso è sempre il contratto di ordine passato a cf-d-lead.

---

## Script target deterministico 1: `order-validator`

**Scopo:** validazione autonoma di un contratto di ordine prima di inviarlo a CF-R0.
Permette a un committente (o a un agente del committente) di verificare se il proprio
ordine passerà il gate CF-D-QA senza inviarlo formalmente.

**Input:** stesso schema del contratto di ordine (§0 dossier).

**Comportamento:**
- Legge il file `brand_kit` indicato: esiste? Schema valido? (slug, visual, voice, canali)
- Legge il file `icp`: esiste? Campi obbligatori presenti?
- Verifica che `formato` sia nella lista ammessa.
- Verifica che `budget.tier_max` sia compatibile con il formato.
- Produce output strutturato: PASS con riepilogo o FAIL con lista errori per campo.

**Non modifica nulla:** è in sola lettura, non crea cartelle né aggiorna il registry.
È uno strumento di pre-validazione, non di esecuzione.

**Path target:** `scripts/order-validator.py` (campo popolato a runtime quando lo
script verrà scritto in fase di build V2-6).

---

## Script target deterministico 2: `capacity-planner`

**Scopo:** calcolo del piano di capacità CF-DE per orizzonte temporale dato.
Permette a cf-d-sched di produrre la risposta slot in modo deterministico leggendo
il modello capacità da file — non in memoria volatile.

**Input:**
```json
{
  "orizzonte_giorni": 7,
  "area": "produzione | pre-produzione | post-produzione | tutte",
  "formato": "carosello-ig | video-ugc | ..."
}
```

**Comportamento:**
- Legge `cf/orders` registry: ordini attivi con area, slot, data completamento stimata.
- Calcola gli slot liberi per area/reparto nell'orizzonte dato.
- Calcola il throughput attuale vs storico per il formato richiesto.
- Output: lista slot liberi ordinati per data, stato capacità (verde/giallo/rosso) per
  ogni area, batch opportunity se ordini simili in finestra ravvicinata.

**Non dispatcha nulla:** è in sola lettura. Le decisioni di dispatch restano a cf-d-lead.

**Path target:** `scripts/capacity-planner.py` (campo popolato a runtime quando lo
script verrà scritto in fase di build V2-6).

---

## Regole di utilizzo script

1. Gli script di CF-R0 sono strumenti di supporto alle decisioni, non sostituti degli agenti.
   Un output PASS di `order-validator` non sostituisce il gate CF-D-QA nel workflow ufficiale.
2. Ogni script è in sola lettura sul registry `cf/orders`: nessuno script di CF-R0 scrive
   nel registry senza passare per cf-d-dispatch.
3. Dry-run disponibile: entrambi gli script supportano un flag `--dry-run` che produce
   l'output senza modificare nulla (standard DE per tutti gli script).

---

## Connessioni

- [[WF-ORDER-INTAKE]] · `workflow/WF-ORDER-INTAKE.md` — workflow che usa la skill cf-order
- [[cf-d-qa]] · `agenti/cf-d-qa.md` — logica che order-validator replica in pre-check
- [[cf-d-sched]] · `agenti/cf-d-sched.md` — agente che usa capacity-planner come supporto
- [[state/README]] · `state/README.md` — registry cf/orders letto dagli script
