---
Type: REPARTO
Status: Active
Tags: #reparto #marketing #analytics #ottimizzazione #tracking #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# L2.4 — Analytics & Ottimizzazione

> **Ecosistema:** 04-MARKETING · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
> **Standard:** CF-grade (ADR-007) · **Reparto ampliato v2 — base v1 AN1-AN4 intatta (ADR-003)**

---

## Missione

Misurare l'effetto di ogni copy e campagna e chiudere il cerchio tra dato e revisione.
I dati diventano pattern (ReasoningBank) e i pattern diventano revisioni di copy mirate.

**Questo reparto rende il sistema auto-migliorante** (pattern #5 Piano Maestro): ogni run
di copy o campagna alimenta la conoscenza collettiva in `marketing/copy/patterns/{icp}`,
che il COPY-MASTER interroga prima di scrivere qualsiasi nuovo copy.

**Confini netti:**
- L2.4 non scrive copy (L2.1 Copywriting).
- L2.4 non progetta funnel (L2.6 Conversion Architecture).
- L2.4 non implementa il tracking tecnico su server (06-PLATFORM) — produce il piano e
  coordina, ma la messa in opera del tracking vive in 06-PLATFORM.
- L2.4 non forza mai un verdetto A/B sotto soglia statistica: il verdetto è "inconclusivo",
  non "il vincitore è X".

---

## Roster del reparto (7 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AN-LEAD` | Analytics Lead | `agenti/an-lead.md` | coordinator | sonnet | Coordina il reparto; definisce il piano di misurazione per ogni campagna; risponde dei KPI di ottimizzazione |
| `AN1` | Tracking Engineer | `agenti/an1-tracking-engineer.md` | worker | sonnet | Tracking plan, UTM, eventi, conversion API (coordinamento con 06-PLATFORM) |
| `AN2` | Attribution Analyst | `agenti/an2-attribution-analyst.md` | worker | sonnet | Attribuzione per canale/campagna/copy; legge performance per copy_id |
| `AN3` | Experiment Designer | `agenti/an3-experiment-designer.md` | worker | sonnet | Ipotesi, varianti, dimensionamento test; verifica soglia statistica prima del verdetto |
| `AN4` | Insight Distiller | `agenti/an4-insight-distiller.md` | worker | sonnet | Performance → pattern ReasoningBank; scrive in `marketing/copy/patterns/{icp}` e antipatterns |
| `AN5` | Funnel Analyst | `agenti/an5-funnel-analyst.md` | worker | sonnet | Drop rate per sezione APSOC, bounce, micro-conversion → input per L2.6 e A8 diagnosi |
| `AN-OBSERVER` | Marketing Observability Lead | `agenti/an-observer-observability-lead.md` | verifier | sonnet | Monitora i KPI dell'intero ecosistema 04-MARKETING; segnala anomalie al MKT-Conductor; alimenta il report CMO |

**Nota ADR-003:** gli agenti v1 AN1-AN4 esistono in `company/Ecosistemi/04-MARKETING/Agenti/`.
Quei file non vengono toccati. Le schede CF-grade di questo reparto sono le versioni v2 amplificate.

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-TRACKING-SETUP** | `workflow/WF-TRACKING-SETUP.md` | Tracking plan, UTM, eventi, conversion API per ogni campagna/funnel | AN1: ogni evento ha nome, trigger e valore misurato; nessun "evento fantasma" |
| **WF-OPTIMIZATION-LOOP** | `workflow/WF-OPTIMIZATION-LOOP.md` | Loop data-driven §4b: raccolta → diagnosi → distillazione → revisione copy → A/B → consolida | Ciclo tracciato in state.json; pattern consolidati solo con evidenza ripetuta (anti-rumore AN3) |
| **WF-AB-TEST** | `workflow/WF-AB-TEST.md` | Disegno ed esecuzione esperimenti (ipotesi → varianti → dimensione → verdetto) | AN3 verifica dimensione; verdetto con criterio predefinito; esito → `marketing/ads/experiments` |

---

## Skill del reparto

| Skill | Priorità | File |
|---|---|---|
| `copy-performance-loop` | P1 (da forgiare, §6 dossier) | `skills/SKILLS.md` |
| `icp-pattern-library` | P1 (da forgiare, §6 dossier) | `skills/SKILLS.md` |
| `ab-testing` (esistente, mappata) | — | Motore WF-AB-TEST |
| `analytics` (esistente, mappata) | — | Motore WF-TRACKING-SETUP |
| `market-audit` (esistente, mappata) | — | Ausiliaria AN-OBSERVER |
| `market-report` (esistente, mappata) | — | Ausiliaria AN-OBSERVER e report CMO |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Esperimenti chiusi con verdetto / mese | AN3 | N. WF-AB-TEST con verdetto statisticamente valido nel periodo |
| Pattern ICP consolidati | AN4 | N. record validati in `marketing/copy/patterns/*`; crescita = sistema impara |
| Copertura tracking (% eventi senza "fantasma") | AN1 | N. eventi con nome+trigger+valore / tot eventi tracciati |
| Cicli loop ottimizzazione completati | AN-LEAD | N. cicli WF-OPTIMIZATION-LOOP con tutti i 6 passi tracciati |
| Anomalie segnalate da AN-OBSERVER con risoluzione | AN-OBSERVER | N. anomalie risolte / tot segnalate nel periodo; [DM] baseline |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | L2.1 Copywriting (A8) | Score APSOC per copy_id → AN2 per attribuzione performance |
| ← riceve da | L2.2 Advertising | Dati campagna (CTR, CPC, conversion) per canale → AN2 |
| ← riceve da | L2.6 Conversion Architecture (CA3) | Schema micro-conversioni attese → AN5 piano di misurazione |
| ← riceve da | 06-PLATFORM | Implementazione tracking (pixel, eventi server) → AN1 verifica |
| → consegna a | L2.1 Copywriting (COPY-MASTER) | Pattern vincenti e antipattern per ICP (`marketing/copy/patterns/{icp}`) |
| → consegna a | L2.6 Conversion Architecture (CA4) | Drop rate per sezione APSOC → input WF-CRO-SPRINT |
| → consegna a | L2.1 (A8) | Diagnosi sezione APSOC debole → rework mirato (non riscrittura totale) |
| → consegna a | CMO / MKT-Conductor | Report KPI ecosistema (AN-OBSERVER) |
| → consegna a | 06-PLATFORM | Tracking plan + specifica eventi → implementazione |

---

## Escalation

- Soglia statistica non raggiunta dopo 2 cicli → AN3 propone revisione dimensione campione o riduzione varianti; non si forza un verdetto.
- Evento tracking mancante scoperto post-lancio → AN1 segnala a MKT-Conductor + 06-PLATFORM per fix urgente; log in state.
- KPI ecosistema fuori soglia per 2 report consecutivi → AN-OBSERVER segnala al CMO e MKT-Conductor con diagnosi.
- Pattern scritto in namespace senza evidenza sufficiente (< n_minimo run) → AN-LEAD blocca la scrittura; log in anti-rumore state.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
- [[06-ECOSISTEMA-PLATFORM]] · partner implementazione tracking
- [[L2-1-Copywriting]] · destinatario pattern vincenti; fornitore copy_id per attribuzione
- [[L2-6-Conversion-Architecture]] · AN5 fornitore drop rate per WF-CRO-SPRINT
- [[WF-TRACKING-SETUP]] · `workflow/WF-TRACKING-SETUP.md`
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md`
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md`
