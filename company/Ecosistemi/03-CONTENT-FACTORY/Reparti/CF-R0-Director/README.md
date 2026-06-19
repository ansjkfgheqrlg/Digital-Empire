---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #director #cf-r0 #ordini #priorita #kpi #L0
Created: 2026-06-19
Last updated: 2026-06-19
---

# CF-R0 — CF-DIRECTOR

> **Ecosistema:** 03-CONTENT-FACTORY · **Livello:** L0 (leader ecosistema) · **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §3 CF-R0`
> **Standard:** CF-grade (ADR-007) · **Reparto nuovo TARGET-V2**

---

## Missione

CF-R0 è l'ingresso unico di tutti gli ordini della Content Factory. Non produce contenuti:
orchestra il flusso. Riceve ogni ordine da un committente (01-AGENCY, 02-INFO, 04-MKT,
05-MB, DE-interno), valida il contratto, gestisce la coda per priorità, smista alle tre
aree operative (Pre-Produzione, Produzione, Post-Produzione), presidia i KPI globali di
CF-DE e riporta al Board tramite il conductor.

**Nessun ordine entra nell'ecosistema senza passare per CF-R0.** Nessun lavoro parte
senza ordine valido. Il Director rifiuta ordini incompleti con risposta strutturata
al committente — mai improvvisazione, mai silenzio.

---

## Contratto di ordine (unico punto di ingresso)

Ogni committente deve inviare un ordine nel formato seguente (v1 confermato, §0 dossier):

```json
{
  "order_id": "CF-2026-0001",
  "committente": "01-AGENCY | 02-INFO | 04-MKT | 05-MB-YT | 05-MB-KDP | cliente:<slug> | DE-interno",
  "brand_kit": "brands/<slug>/brand-kit.json",
  "icp": "brands/<slug>/icp.json",
  "formato": "carosello-ig | video-ugc | video-avatar | articolo | newsletter | thumbnail | grafica | publish-only",
  "quantita": 10,
  "deadline": "YYYY-MM-DD",
  "budget": {
    "crediti_engine": 120,
    "tier_max": "sonnet"
  },
  "note": "vincoli specifici, CTA richiesta, canali destinazione, engine_preference (opzionale)"
}
```

**Campo obbligatorio non negoziabile:** `brand_kit` + `icp` devono puntare a file esistenti
e validati dal registry CF-R2. Ordine con `brand_kit` mancante o `icp` mancante = rifiuto
automatico con motivo strutturato. Questo è il gate BLOCCANTE di CF-D-QA (WF-ORDER-INTAKE).

---

## Roster del reparto (7 agenti)

| ID | Agente | File | Tier | Ruolo |
|---|---|---|---|---|
| `CF-D-LEAD` | CF-Director Lead | `agenti/cf-d-lead.md` | opus | Valida ogni ordine; decide priorità coda; riporta al Board |
| `CF-D-QA` | Order Gate Verificatore | `agenti/cf-d-qa.md` | sonnet | Gate brand_kit+icp+budget+formato; BLOCCA ordini incompleti |
| `CF-D-DISPATCH` | Order Dispatcher | `agenti/cf-d-dispatch.md` | sonnet | Smista ordini validati alle 3 aree; crea `orders/<id>/` con state+trace |
| `CF-D-SCHED` | Scheduler & Capacity Planner | `agenti/cf-d-sched.md` | sonnet | Piano carico per area; alert capacità insufficiente; batch merging |
| `CF-D-BUDGET` | Budget Sentinel Coordinator | `agenti/cf-d-budget.md` | haiku | Aggrega stime engine; alert se ordine sfora soglia globale |
| `CF-D-STATUS` | Order Status Monitor | `agenti/cf-d-status.md` | haiku | Dashboard stato ordini real-time; alert committenti su milestone |
| `CF-D-LEARN` | Director Pattern Learner | `agenti/cf-d-learn.md` | sonnet | Aggrega pattern da tutte le aree; report mensile qualità |

---

## Workflow del reparto (2 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-ORDER-INTAKE** | `workflow/WF-ORDER-INTAKE.md` | Validazione ordine → dispatch → slot assegnato | brand_kit+icp presenti e validi; cartella `orders/<id>/` creata; slot assegnato |
| **WF-DIRECTOR-REVIEW** | `workflow/WF-DIRECTOR-REVIEW.md` | Review settimanale KPI globali; escalation Board se KPI calano 2 cicli | Report entro lunedì ore 10; nessuna metrica inventata (Mandato Art.2) |

---

## Namespace di stato

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `cf/orders` | Registry globale ordini attivi: id, committente, stato, area assegnata, slot | CF-D-DISPATCH / CF-D-STATUS |
| `cf/kpi` | KPI globali CF-DE aggregati per ciclo settimanale | CF-D-LEARN / CF-D-STATUS |

Struttura su disco per ogni ordine: `orders/<id>/order.json` + `state.json` + `trace.jsonl`.
Dettaglio schema: `state/README.md`.

---

## KPI globali (riepilogo)

| KPI | Owner | Target |
|---|---|---|
| Lead time ordine→dispatch (ore) | CF-D-DISPATCH | [DM] — baseline al primo ciclo reale |
| % ordini completi al primo giro | CF-D-QA | [DM] — obiettivo >80% in M6 |
| Ordini per area / settimana | CF-D-STATUS | [DM] |
| % ordini rispettati nella deadline | CF-D-LEAD | [DM] |

Dettaglio KPI: `kpi/KPI.md`.

---

## Regola di precedenza coda

In conflitto tra ordini, CF-D-LEAD applica nell'ordine:
1. `deadline` — la scadenza più vicina vince
2. `revenue impact` — ordini Agency (SLA clienti) e lanci Info-Business hanno priorità su interno
3. `interno` — ordini interni DE sono l'ultima priorità in coda

Escalation al Board via hive-mind solo se due committenti hanno stessa priorità e budget
non copre entrambi (caso eccezionale — vedi WF-DIRECTOR-REVIEW §4).

---

## Escalation

- Ordine incompleto → rifiuto automatico CF-D-QA con motivo strutturato JSON → committente
- Capacità area insufficiente → CF-D-SCHED alert → CF-D-LEAD decide: batch merging o escalation Board
- Budget ordine sfora soglia globale → CF-D-BUDGET alert → CF-D-LEAD: richiede approvazione committente prima del dispatch
- KPI calano per 2 cicli settimanali → CF-D-LEARN → CF-D-LEAD → richiesta 07-FORGE (ADR-007)
- Due ordini in conflitto di priorità non risolvibile con regola coda → escalation Board

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Script wrapper → `scripts/README.md`

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §3 CF-R0`
- [[WF-ORDER-INTAKE]] · `workflow/WF-ORDER-INTAKE.md`
- [[WF-DIRECTOR-REVIEW]] · `workflow/WF-DIRECTOR-REVIEW.md`
- [[CF-R1-Strategia-Brief]] · area Pre-Produzione — destinataria degli ordini strategie
