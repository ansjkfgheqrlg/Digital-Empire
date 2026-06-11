# CF-R1 — STRATEGIA CONTENUTI

> Reparto L2 di 03-CONTENT-FACTORY · Coordinatore: `CF-R1-A01-brief-lead`
> Fonte: dossier 03 §2 (CF-R1).

---

## Cosa fa

Trasforma l'ordine in un **piano eseguibile**: brief, angle, calendario, assegnazione
formati. È il cervello a monte della fabbrica: **nessun contenuto si produce senza brief
approvato**. Qui l'ordine grezzo (`order.json`) diventa `brief.json` — angle, hook type,
struttura, canali, vincoli — caricando `brand_kit` + `icp` del tenant (pattern #11).

### Org interna

| Livello | Team | Contenuto | Owner |
|---|---|---|---|
| L3 | **WF-BRIEF** | intake ordine: valida contratto, carica brand_kit+icp, produce `brief.json` | CF-R1-A02-brief-analyst |
| L3 | **WF-CALENDAR** | piano editoriale multi-brand: slot di pubblicazione, mix formati, ricorrenze (skill `content-strategy`) | CF-R1-A04-calendar-planner |
| L4 | T-hook | selezione formula hook dalla libreria (hook-formulas di carousel-factory) | CF-R1-A03 |
| L4 | T-angle | 3 angle alternativi per brief | CF-R1-A03-angle-strategist |
| L4 | T-trend-intake | riceve brief trend da 08-INTELLIGENCE | CF-R1-A02 |

### Agenti L5 (schede in `../../Agenti/`)

| ID | Ruolo | Tier |
|---|---|---|
| CF-R1-A01-brief-lead | coordina intake e brief | sonnet |
| CF-R1-A02-brief-analyst | parse ordine, carica brand_kit/icp, compila brief.json | haiku |
| CF-R1-A03-angle-strategist | 3 angle + hook type da libreria formule | sonnet |
| CF-R1-A04-calendar-planner | piano editoriale, slot, mix formati | sonnet |

---

## Come si collega

**Inbound:**
- `CF-A00-conductor` → ordine validato (`order.json`) da trasformare in brief.
- `08-INTELLIGENCE` → brief di ricerca: trend, hook che funzionano, analisi competitor (T-trend-intake).
- `cf/patterns` (BRAIN) → pattern vincenti pregressi per brand+formato (memory_search pre-task obbligatorio).

**Outbound:**
- `brief.json` per pezzo → reparto di produzione competente (CF-R2 video, CF-R3 testo, CF-R4 visual).
- Slot calendario (WF-CALENDAR) → CF-R5/WF-PUBLISH per la schedulazione.
- Handoff contract standard con acceptance criteria: brief completo = tutti i campi
  obbligatori presenti (angle, hook type, formato, canali, vincoli, riferimento brand_kit/icp).

**Skill knowledge layer:** `content-strategy` (piano editoriale, pillar), `social`,
`market-social` (referenziate, non duplicate — pattern #6).

---

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione:** SOLO su handoff dal CF-A00-conductor (ordine valido). Mai in autonomia.
WF-CALENDAR si attiva anche su base ricorrente (piano editoriale mensile per i brand interni).

**Logica di ragionamento (per ogni ordine):**
1. `memory_search("cf/patterns", brand+formato)` — cosa ha già funzionato per questo tenant.
2. Carica `brand-kit.json` (palette, voice, esempi sì/no) + `icp.json` (dolori, desideri,
   obiezioni, livello di consapevolezza, linguaggio).
3. T-angle propone 3 angle alternativi; T-hook seleziona il tipo di hook dalla libreria
   formule; l'angle scelto va nel brief con motivazione.
4. Compila `brief.json` in `orders/<id>/01-brief/` — un brief per pezzo nei batch.
5. Gate di uscita: brief completo (campi obbligatori). Brief incompleto NON passa:
   torna ad arricchimento o escalation al committente via CF-A00.

**Failure handling:** ordine ambiguo (icp mancante, formato non chiaro) → 1 richiesta
strutturata di chiarimento al committente via conductor; mai inventare. 2 brief
respinti dal reparto a valle → escalation a CF-A00 + entry `cf/failures`.

## KPI del reparto

| KPI | Direzione |
|---|---|
| % brief approvati al primo colpo dal reparto a valle | ↑ |
| Tempo ordine→brief | ↓ |
| % slot calendario rispettati a valle (qualità pianificazione) | ↑ |

*Fonte: dossier 03 §2-§4 · Aggiornato: 2026-06-11*
