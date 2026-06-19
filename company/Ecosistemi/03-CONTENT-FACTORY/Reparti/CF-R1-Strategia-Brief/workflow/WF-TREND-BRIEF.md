---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #CF-R1 #trend #urgenza #finestra-stretta
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-TREND-BRIEF — Brief Accelerato per Contenuti a Finestra Stretta

> **ID:** WF-R1-003 · **Owner:** `cf-r1-coord` · **Reparto:** CF-R1 Strategia & Brief
> **Trigger:** brief trend da 08-INTELLIGENCE con urgenza alta/critica, o slot
> "trend-priority" nel piano editoriale che richiede brief entro le prossime ore

---

## Scopo

Produrre un brief eseguibile per contenuti a finestra temporale stretta (trend, news
di nicchia, eventi imprevisti) in un tempo totale ≤1h dall'avvio. Il workflow è una
versione accelerata di WF-BRIEF: mantiene tutti i gate obbligatori ma riduce il numero
di angle da 3 a 1+opzionale, e il gate CF-R1-QA ha SLA interno di ≤30 minuti.

Un trend datato >48h non viene processato: viene scartato con motivo strutturato e
archiviato in `cf/briefs/trend/scartati/`. Non esiste eccezione a questa regola —
un contenuto su un trend scaduto non è contenuto trend.

**Gate d'uscita:** latenza totale intake→brief ≤1h; trend validato (età ≤48h);
brief.json con tutti i campi obbligatori presente; ordine con priorità "trend" inserito
in coda produzione CF-Director (coda priorità alta).

---

## Attori

| Step | Agente | Funzione |
|---|---|---|
| Intake e verifica | `cf-r1-trend` | Riceve brief trend, verifica età ≤48h, aggiorna libreria |
| Coordinamento | `cf-r1-coord` | Decide routing, avvia pipeline accelerata, gestisce SLA |
| Analisi rapida | `cf-r1-analyst` | Caricamento rapido contesto (brand_kit + icp) — versione light |
| Angle urgente | `cf-r1-angle` | Produce 1 angle primario (+ 1 opzionale se il tempo lo permette) |
| Gate accelerato | `cf-r1-qa` | Stesso gate standard WF-BRIEF ma con SLA interno ≤30 min |

---

## Flusso passo-passo

```
[TRIGGER]
Brief trend da 08-INTELLIGENCE in cf/briefs/trend/
O: slot "trend-priority" nel piano CAL-YYYY-WW con scadenza imminente
        │
        ▼
[STEP 1] CF-R1-TREND — verifica temporale (≤5 min)
  → legge brief trend: {topic, brand_slug, data_trend, urgenza, source}
  → calcola età: (now - data_trend) in ore
  → età >48h → SCARTA: archivia in cf/briefs/trend/scartati/ con motivo strutturato
                         STOP — nessuna altra azione
  → età ≤48h → VALIDO: deposita in cf/patterns/<brand_slug>/trend-attivi.json
  → notifica CF-R1-COORD con urgenza e scadenza stimata (data_trend + 72h)
        │
        ▼
[STEP 2] CF-R1-COORD — routing e apertura ordine urgente (≤3 min)
  → apre ordine urgente: assegna order_id "CF-TREND-<YYYYMMDD>-<NNN>"
  → scrive orders/<id>/order.json con flag {"priorita": "trend", "dry_run": false}
  → verifica che il brand_slug abbia brand_kit validato da CF-R2
    (se no → STOP + escalation CF-R2 per onboarding urgente; trend non processato)
  → avvia il timer SLA: brief.json deve essere pronto entro 55 min da questo step
        │
        ▼
[STEP 3] CF-R1-ANALYST — analisi rapida (≤10 min)
  → carica brand_kit + icp: versione light (solo voice, canali, parole_vietate, icp.dolori)
  → identifica formato più adatto al trend (di solito: carosello-ig o reel per trend social)
  → se il formato non è dichiarato nel brief trend → CF-R1-COORD decide (default: carosello-ig)
  → produce context_rapido.json (subset del context.json standard)
        │
        ▼
[STEP 4] CF-R1-ANGLE — angle urgente (≤10 min)
  → input: context_rapido.json + topic trend + urgenza
  → produce angle_A (angle primario, il più forte per quel trend + icp)
  → produce angle_B (opzionale: solo se il tempo del SLA lo permette)
  → il trend è per natura angle_C della libreria standard; qui diventa angle_A
  → verifica conformità brand_kit.voice e Mandato Art.2 su ogni angle prodotto
        │
        ▼
[STEP 5] CF-R1-QA — gate accelerato (≤30 min dall'avvio, SLA interno)
  → STESSA checklist di WF-BRIEF: tutti i 7 campi obbligatori
  → non esistono campi "opzionali per urgenza": il gate è identico al workflow standard
  → PASS: scrive brief.json in orders/<id>/01-brief/
           aggiorna state.json: {priorita: "trend", stato: "completata", timestamp}
  → FAIL: lista campi mancanti a CF-R1-COORD
    → CF-R1-COORD ha 15 minuti per fix e secondo tentativo
    → secondo FAIL → escalation a L1-PRE; ordine sospeso; trend potenzialmente preso in carico
      dalla settimana successiva (se non scaduto)
        │
        ▼
[STEP 6] CF-R1-COORD — inserimento coda priorità (≤2 min)
  → notifica CF-D-DISPATCH: ordine trend-priority pronto per produzione
  → CF-D-DISPATCH inserisce l'ordine in coda priorità alta (sopra ordini standard)
  → logga in wiki/log.md: trend processato, brief pronto, slot produzione assegnato
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G0 — Validità temporale | Età trend ≤48h dalla data_trend | CF-R1-TREND | Intero workflow — STOP se scartato |
| G1 — Brand validato | brand_slug ha brand_kit validato in CF-R2 | CF-R1-COORD | Avvio analisi |
| G2 — Gate brief | Tutti i 7 campi obbligatori presenti e validi | CF-R1-QA | Avanzamento a produzione |
| G3 — SLA ≤1h | brief.json pronto entro 1h dall'avvio workflow | CF-R1-COORD | Segnalazione a L1-PRE se SLA violato |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "trend_id": "TREND-2026-0089",
  "topic": "Creator economy in declino: dati Q2 2026",
  "brand_slug": "mentalita-brutale",
  "nicchia": "imprenditoria-digitale",
  "data_trend": "2026-06-18T14:00:00Z",
  "urgenza": "alta",
  "source": "08-INTELLIGENCE/wiki/trends/creator-economy-Q2-2026.md",
  "formato_suggerito": "carosello-ig"
}
```

**Output (trend valido — PASS):**
```json
{
  "order_id": "CF-TREND-20260619-001",
  "priorita": "trend",
  "brief_path": "orders/CF-TREND-20260619-001/01-brief/brief.json",
  "trend_id": "TREND-2026-0089",
  "eta_trend_ore": 18.5,
  "validita": "OK",
  "gate_r1_qa": "PASS",
  "lead_time_min": 43,
  "sla_rispettato": true,
  "coda_produzione": "priorità-alta",
  "brief": {
    "angle": "contro-intuizione: la creator economy non è in declino — è in selezione",
    "hook_type": "affermazione-diretta",
    "hook_draft": "Il 60% dei creator non sopravviverà al 2026. Non è una crisi — è un filtro.",
    "struttura_formato": "slide-deck",
    "canali": ["instagram"],
    "vincoli_brand": {"parole_vietate": ["forse", "quasi"], "cta_richiesta": "segui per altri dati"},
    "slide_count": "6-8",
    "icp_ref": "brands/mentalita-brutale/icp.json",
    "nota_dati": "dato 60% da source 08-INTELLIGENCE/wiki/trends/creator-economy-Q2-2026.md — verificato"
  }
}
```

**Output (trend scartato — età >48h):**
```json
{
  "trend_id": "TREND-2026-0079",
  "validita": "SCARTATO",
  "eta_trend_ore": 62.0,
  "motivo": "trend datato: 62h dalla data_trend alla data_ricezione (soglia: 48h)",
  "archiviato_in": "cf/briefs/trend/scartati/TREND-2026-0079-scartato.json",
  "azione": "nessuna — ordine non aperto"
}
```

---

## Differenze rispetto a WF-BRIEF standard

| Caratteristica | WF-BRIEF | WF-TREND-BRIEF |
|---|---|---|
| Numero angle prodotti | 3 | 1 (+ 1 opzionale) |
| SLA totale | Nessuno definito ([DM] baseline) | ≤1h dall'avvio |
| SLA gate CF-R1-QA | Nessuno definito | ≤30 min |
| Gate temporale aggiuntivo | No | Sì: età ≤48h (G0 bloccante) |
| Priorità in coda produzione | Standard | Alta (sopra ordini standard) |
| Checklist gate brief | Identica | Identica — nessuna semplificazione |

---

## State

File: `orders/CF-TREND-<YYYYMMDD>-<NNN>/state.json`
```json
{
  "order_id": "CF-TREND-20260619-001",
  "priorita": "trend",
  "trend_id": "TREND-2026-0089",
  "avvio_workflow": "2026-06-19T09:00:00Z",
  "brief_completato": "2026-06-19T09:43:00Z",
  "lead_time_min": 43,
  "sla_rispettato": true
}
```

---

## Connessioni

- [[cf-r1-trend]] · `agenti/cf-r1-trend.md` — intake e verifica temporale
- [[cf-r1-coord]] · `agenti/cf-r1-coord.md` — orchestrazione e SLA
- [[cf-r1-qa]] · `agenti/cf-r1-qa.md` — gate accelerato obbligatorio
- [[WF-BRIEF]] · `workflow/WF-BRIEF.md` — workflow standard di riferimento
- [[WF-CALENDAR]] · `workflow/WF-CALENDAR.md` — slot trend-priority che attivano questo WF
- [[08-INTELLIGENCE]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
