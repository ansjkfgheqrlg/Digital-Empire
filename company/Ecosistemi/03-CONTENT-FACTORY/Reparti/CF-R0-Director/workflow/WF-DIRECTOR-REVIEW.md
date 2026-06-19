---
Type: WORKFLOW
Status: Active
Tags: #workflow #content-factory #review #kpi #board #escalation #cf-r0
Created: 2026-06-19
Last updated: 2026-06-19
---

# WF-DIRECTOR-REVIEW — Review Settimanale KPI e Escalation Board

> **ID:** WF-CF-D-002 · **Owner:** `cf-d-lead` · **Reparto:** CF-R0 Director
> **Trigger:** ogni lunedì mattina (cadenza settimanale fissa) o su richiesta Board
> **Marcatura dossier:** [TARGET-V2]

---

## Scopo

Esaminare ogni settimana i KPI globali di CF-DE, identificare pattern in calo o
anomalie sistemiche, e decidere se eseguire l'ordinaria manutenzione interna o se
escalare al Board con richiesta a 07-FORGE. Il review chiude il loop di governance:
CF-DE non è solo una fabbrica che produce — è un sistema che si auto-monitora
e si auto-migliora attraverso questo ciclo settimanale.

**Gate di uscita:** report settimanale scritto in `cf/kpi`, consegnato a CF-D-LEAD
entro lunedì ore 10; eventuali escalation Board avviate con dossier completo;
nessuna metrica inventata (Mandato Art.2 — se la baseline non esiste: [DM]).

---

## Attori

| Step | Agente CF-R0 | Destinatario esterno |
|---|---|---|
| Raccolta KPI grezzi | `cf-d-status` | — |
| Elaborazione pattern | `cf-d-learn` | — |
| Decisione e azione | `cf-d-lead` | Board/Conductor (escalation), 07-FORGE (richiesta skill) |
| Notifica escalation | `cf-d-lead` | Board Conductor, CMO (se impatta su 04-MKT) |

---

## Flusso passo-passo

```
[TRIGGER: lunedì mattina — cadenza settimanale fissa]
cf-d-lead attiva il ciclo di review settimanale

        │
        ▼
[STEP 1] cf-d-status — Aggregazione KPI settimanali grezzi
  → Legge registry cf/orders: ordini aperti, chiusi, in ritardo della settimana
  → Calcola:
      - N. ordini ricevuti nel periodo
      - N. ordini dispatchati (gate PASS)
      - N. ordini rifiutati (gate FAIL) e tasso di fallimento
      - Lead time medio ordine→dispatch (ore)
      - N. ordini rispettati nella deadline / tot consegnati
      - N. alert ritardo emessi nel periodo
  → Output: KPI grezzi strutturati → cf-d-learn

        │
        ▼
[STEP 2] cf-d-learn — Elaborazione pattern e trend
  → Riceve KPI grezzi da cf-d-status
  → Carica i dati delle 3 settimane precedenti (da cf/kpi)
  → Analisi trend:
      - KPI in crescita → verde (nessuna azione sistemica)
      - KPI stabili → giallo (monitoraggio)
      - KPI in calo 1 ciclo → giallo (segnale da monitorare)
      - KPI in calo 2+ cicli consecutivi → ROSSO (trigger_forge = true)
  → Identifica pattern confermati (≥2 cicli): ritardi sistematici, fail QA ricorrenti,
    inaccuratezze stima budget, colli di bottiglia area
  → Produce bozza report settimanale con: trend, pattern, segnali, raccomandazioni
  → Output: bozza report + trigger_forge (true/false) → cf-d-lead

        │
        ▼
[STEP 3] cf-d-lead — Revisione bozza e decisione
  → Legge la bozza report di cf-d-learn
  → Verifica: nessuna metrica inventata? Ogni dato ha fonte (cf/orders o state.json)?
  → GATE-REPORT:
      se qualsiasi dato senza fonte → richiede a cf-d-learn di rimuovere o sostituire con [DM]
  → Decide le azioni in base al trigger_forge:

  CASO A — trigger_forge = false (tutti i KPI stabili o in crescita):
    → Approva il report settimanale
    → Scrive il record in cf/kpi
    → Nessuna escalation Board necessaria
    → Il report va in archivio; prossimo review: lunedì prossimo

  CASO B — trigger_forge = true (KPI in calo 2 cicli consecutivi):
    → Aggiunge rationale al report: quale KPI, quale pattern, quale area
    → Produce spec del problema per 07-FORGE: sintomo, ipotesi causa, tipo di skill/agente richiesto
    → Prepara dossier escalation Board: report + spec + raccomandazione

        │
        ▼
[STEP 4 — solo se CASO B] cf-d-lead — Escalation Board
  → Invia dossier escalation al conductor Board via handoff
  → Dossier include:
      - KPI in calo: quale metrica, delta rispetto alle 2 settimane precedenti
      - Pattern identificato da cf-d-learn con evidenza ≥2 cicli
      - Spec per 07-FORGE: descrizione del problema, output atteso (nuova skill / agente / regola)
      - Impatto attuale e proiezione se non risolto
  → Invia richiesta formale a 07-FORGE (non attende risposta nel workflow — il loop di
    risposta avviene fuori dal WF-DIRECTOR-REVIEW)

        │
        ▼
[STEP 5] cf-d-lead — Finalizzazione report
  → Aggiunge al record cf/kpi: data, trigger_forge, escalation_avviata (true/false)
  → Scrive entry in orders/trace aggregato (non per ordine singolo, ma per ciclo review)
  → Archivio: il report settimanale in cf/kpi è consultabile da qualsiasi agente CF-R0

[FINE WORKFLOW]
Gate di uscita: report in cf/kpi con timestamp, tutti i dati con fonte, escalation
Board avviata se trigger_forge, nessuna metrica [DM] presentata come dato reale.
```

---

## Regola anti-metrica-inventata (Mandato Art.2)

Nessun report uscito da questo workflow può contenere:
- Percentuali calcolate su campioni inferiori a 3 ordini (troppo rumore).
- Target numerici non stabiliti con evidenza reale (si scrive [DM] o "da stabilire in M6").
- Confronti con periodi precedenti se il dato precedente non è archiviato in `cf/kpi`.

CF-D-LEARN ha il mandato di rimuovere o marcare [DM] qualsiasi dato sospetto prima
che CF-D-LEAD approvi il report. Il Board deve poter fidarsi dei numeri che legge.

---

## Trigger escalation 07-FORGE (ADR-007)

La richiesta a 07-FORGE viene avviata solo quando:
1. Un KPI specifico cala per 2 cicli settimanali consecutivi (non 1 ciclo — può essere rumore).
2. CF-D-LEARN ha identificato un pattern confermato che spiega il calo (non un'ipotesi).
3. La soluzione richiede una nuova skill o un nuovo agente (non una correzione operativa che
   CF-D-LEAD può fare in autonomia nella settimana).

Esempi di trigger validi: fail_rate QA sistematicamente >20% su brand_kit_mancante (servono
istruzioni più chiare o un check automatico nell'onboarding), lead_time in calo per problema
capacità CF-R5 (serve un nuovo agente carosello-worker).

Esempi di NON-trigger: singolo ordine consegnato in ritardo (varianza), fail_rate su
formato non supportato (aggiungere il formato non richiede una skill nuova).

---

## Input / Output del workflow

**Input (attivazione):**
```json
{
  "tipo_task": "review_settimanale",
  "settimana": "2026-W25",
  "cf_d_status_disponibile": true,
  "cf_d_learn_disponibile": true
}
```

**Output (report approvato):**
```json
{
  "workflow": "WF-DIRECTOR-REVIEW",
  "settimana": "2026-W25",
  "timestamp_report": "YYYY-MM-DDTHH:MM:SS",
  "kpi_settimana": {
    "ordini_ricevuti": 12,
    "ordini_dispatchati": 10,
    "fail_rate_qa": 0.17,
    "lead_time_medio_ore": 3.2,
    "ordini_rispettati_deadline_pct": 0.90,
    "alert_ritardo": 1
  },
  "trend": {
    "fail_rate_qa": "stabile (0.15 → 0.17 → 0.17 — non calo sistematico)",
    "lead_time": "in miglioramento (5.1h → 3.8h → 3.2h)"
  },
  "trigger_forge": false,
  "escalation_board": false,
  "archiviato_in": "cf/kpi/2026-W25.json"
}
```

**Output (escalation Board):**
```json
{
  "workflow": "WF-DIRECTOR-REVIEW",
  "settimana": "2026-W25",
  "trigger_forge": true,
  "kpi_in_calo": {
    "metrica": "ordini_rispettati_deadline_pct",
    "settimana_-2": 0.95,
    "settimana_-1": 0.82,
    "settimana_corrente": 0.75,
    "delta": "-0.20 in 2 cicli"
  },
  "pattern_cf_d_learn": "CF-R3 satura per ordini video-ugc con deadline <5gg — capacità insufficiente",
  "spec_07_forge": {
    "problema": "CF-R3 raggiunge saturazione con >3 ordini video-ugc paralleli",
    "output_atteso": "nuovo agente video-worker per CF-R3 che gestisce pipeline ffmpeg in parallelo",
    "urgenza": "alta — impatta SLA Agency"
  },
  "escalation_board": true,
  "dossier_inviato_a": "Board-Conductor",
  "timestamp": "YYYY-MM-DDTHH:MM:SS"
}
```

---

## Connessioni

- [[cf-d-lead]] · `agenti/cf-d-lead.md` — orchestra il workflow e decide l'escalation
- [[cf-d-status]] · `agenti/cf-d-status.md` — step 1, KPI grezzi
- [[cf-d-learn]] · `agenti/cf-d-learn.md` — step 2, pattern e trigger_forge
- [[kpi/KPI]] · `kpi/KPI.md` — definizione delle metriche analizzate in questo workflow
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §3 WF-DIRECTOR-REVIEW`
