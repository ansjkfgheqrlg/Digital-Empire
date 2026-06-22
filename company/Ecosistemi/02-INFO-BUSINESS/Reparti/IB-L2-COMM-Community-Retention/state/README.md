---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #community #retention #IB-L2-COMM
Created: 2026-06-21
Last updated: 2026-06-21
---

# State — IB-L2-COMM Community & Retention

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto. AgentDB namespace radice: `infobusiness/comm`.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Onboarding | `infobusiness/comm/onboarding/` | Per coorte: n. iscritti, attivati, check milestone (≤24h, modulo 1 ≤7gg) | IB-COMM-ONBOARDER | IB-COORD-COMMUNITY, IB-COMM-HEALTH |
| Health | `infobusiness/comm/health/` | Progress, ultimo accesso, alert abbandono per studente (per coorte) | IB-COMM-HEALTH | IB-COMM-RETENTION, IB-COMM-CROSSSELL, IB-COORD-COMMUNITY |
| Engagement | `infobusiness/comm/engagement/` | Piano rituali + report mensile engagement community | IB-COMM-ENGAGE | IB-COMM-HEALTH, IB-COORD-COMMUNITY |
| Testimonials | `infobusiness/comm/testimonials/` | Testimonianza + metrica verificata (G-COMM PASS) | IB-COMM-SOCIAL | IB-COMM-QA, IB-COORD-COMMUNITY |
| Crosssell | `infobusiness/comm/crosssell/` | Scoring per studente, esiti handoff, log gate G-COMM inviolabile | IB-COMM-CROSSSELL | IB-COMM-QA, IB-COORD-COMMUNITY |

---

## Layout file-system del namespace

```
infobusiness/comm/
├── onboarding/
│   ├── state.json                       → per coorte: iscritti, attivati, milestone check
│   └── {coorte_id}/                      → log sequenza onboarding per coorte
├── health/
│   └── {coorte_id}_health.json           → progress, ultimo accesso, alert abbandono per studente
├── engagement/
│   └── {mese}_community.md               → piano rituali + report engagement mensile
├── testimonials/
│   └── {studente_id}_testimonial.md      → testimonianza + metrica verificata (G-COMM PASS)
└── crosssell/
    ├── state.json                        → scoring per studente, esiti handoff
    └── g-comm-log/                        → log gate G-COMM (consenso + segnale, PASS/FAIL) — inviolabile
```

---

## Struttura file di stato

### Onboarding state (`infobusiness/comm/onboarding/state.json`)

```json
{
  "coorte_id": "COORTE-001",
  "prodotto_id": "corso-x",
  "data_cart_close": "YYYY-MM-DD",
  "n_iscritti": 0,
  "n_attivati_24h": 0,
  "n_modulo1_7gg": 0,
  "studenti": [
    {"studente_id": "STU-001", "accesso_24h": true, "modulo1_7gg": false, "a_rischio": false}
  ],
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Health state (`infobusiness/comm/health/{coorte_id}_health.json`)

```json
{
  "coorte_id": "COORTE-001",
  "data_report": "YYYY-MM-DD",
  "completion_rate": "[DM]",
  "engagement_rate_settimana": "[DM]",
  "studenti": [
    {"studente_id": "STU-001", "ultimo_accesso": "YYYY-MM-DD", "percent_progress": 0, "alert_abbandono": false}
  ],
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Crosssell state (`infobusiness/comm/crosssell/state.json`)

```json
{
  "studente_id": "STU-001",
  "fonte_prodotto": "corso-x",
  "segnale_tipo": "implementazione | completamento>50% | richiesta_diretta | survey",
  "score": 0,
  "soglia_raggiunta": false,
  "consenso": false,
  "data_consenso": "YYYY-MM-DD | null",
  "g_comm_gate": "pending | PASS | FAIL",
  "g_comm_motivo": "optional — dettaglio se FAIL",
  "handoff": "non_avviato | HC-IB-AG-01_inviato",
  "lead_id": "LEAD-001 | null",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

> Nessuna PII (email/telefono) nei file di stato: solo `studente_id` / `lead_id` (R8). AGENCY
> recupera il payload completo dal sistema autorizzato dopo l'handoff.

---

## Regole di integrità dei namespace

1. **Crosssell senza consenso non passa** — un record con `score ≥ 5` ma `consenso: false`
   resta `g_comm_gate: "pending"`. `handoff: "HC-IB-AG-01_inviato"` esige `g_comm_gate: "PASS"`
   e `consenso: true`. IB-COMM-QA è responsabile (R2 + R4).

2. **Testimonianza senza metrica** — un file in `testimonials/` non è pubblicabile senza metrica
   reale verificata da G-COMM. Testimonianza con claim non verificabile = FAIL (R3).

3. **g-comm-log inviolabile** — ogni gate G-COMM (cross-sell e testimonianze) ha una riga
   PASS/FAIL in `crosssell/g-comm-log/`. Handoff o pubblicazione senza riga corrispondente è
   anomalia segnalata a IB-COORD-COMMUNITY (R4).

4. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende
   un workflow interrotto legge lo state per sapere a quale step riprendere. Lo state deve
   rispecchiare esattamente il punto attuale del workflow.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Onboarding state | Step 1 WF-ONBOARDING-STUDENTE (cart-close) | Ad ogni milestone (≤24h, ≤72h, ≤7gg) | A fine coorte; non eliminato |
| Health state | Primo report coorte | Ogni report (settimanale/mensile) | A fine coorte; non eliminato |
| Engagement report | Primo mese di community | Mensile | Conservato; storico engagement |
| Crosssell state | Primo segnale studente registrato | Ad ogni step scoring/consenso/gate | Dopo esito handoff; non eliminato |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace e integrazione con altri sistemi
- [[REGOLE]] · `regole/REGOLE.md` — R2/R3/R4/R8 presidiano l'integrità di questi namespace
- [[WF-ONBOARDING-STUDENTE]] · `workflow/WF-ONBOARDING-STUDENTE.md` — produce onboarding state
- [[WF-COMMUNITY-ATTIVA]] · `workflow/WF-COMMUNITY-ATTIVA.md` — produce engagement report e testimonials
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
