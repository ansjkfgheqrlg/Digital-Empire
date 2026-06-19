---
Type: CONCEPT
Status: Active
Tags: #architettura #infobusiness #community #retention #IB-L2-COMM
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — IB-L2-COMM Community & Retention

> Cartella-workflow CF-grade. Standard: Content Factory Exponium (corpus Maximilian).
> Dossier sorgente: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-COMM
> Wrappa: reparto v1 `IB-R4-COMMUNITY-RETENTION.md` + agente v1 `IB-COMMUNITY-manager` (ADR-003).

---

## Topologia del team

```
                   ┌──────────────────────────────────┐
                   │   IB-COORD-COMMUNITY (Sonnet)      │
                   │   orchestratore 3 WF + piano comm. │
                   └──────────────┬───────────────────-┘
                                  │
        ┌──────────────┬──────────┼──────────────┬──────────────┐
        │              │          │              │              │
┌───────▼──────┐ ┌─────▼──────┐ ┌─▼──────────┐ ┌─▼──────────┐ ┌─▼──────────┐
│IB-COMM-      │ │IB-COMM-    │ │IB-COMM-    │ │IB-COMM-    │ │IB-COMM-    │
│ONBOARDER     │ │HEALTH      │ │ENGAGE      │ │RETENTION   │ │SOCIAL      │
│(Haiku)       │ │(Haiku)     │ │(Haiku)     │ │(Sonnet)    │ │(Sonnet)    │
│onboarding    │ │monitor     │ │rituali     │ │win-back    │ │testimonial │
└──────────────┘ └─────┬──────┘ └────────────┘ └────────────┘ └─────┬──────┘
                       │ segnali abbandono / progress              │ milestone
                       │                                            │
                 ┌─────▼────────────────────────────────────-──────▼──┐
                 │            IB-COMM-CROSSSELL (Sonnet)               │
                 │  scoring segnali → dossier lead → handoff AGENCY    │
                 └───────────────────────┬─────────────────────────────┘
                                         │ ogni handoff + ogni testimonianza
                          ┌──────────────▼───────────────┐
                          │     IB-COMM-QA (Sonnet)        │
                          │  gate G-COMM — bloccante        │
                          │  (consenso + metrica verificata)│
                          └──────────────────────────────-┘
```

**Topologia:** star da `IB-COORD-COMMUNITY` verso 5 esecutori (3 Haiku always-on + 2 Sonnet su
trigger). `IB-COMM-HEALTH` alimenta `IB-COMM-RETENTION` (segnali abbandono) e `IB-COMM-CROSSSELL`
(progress). `IB-COMM-QA` opera trasversalmente come gate G-COMM su due flussi sensibili:
ogni handoff cross-sell e ogni testimonianza pubblicata. Il gate è bloccante.

---

## Livelli gerarchici interni

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `IB-COORD-COMMUNITY` | Sonnet | Orchestra i 3 WF, gestisce piano community, riporta a IB-DIRECTOR |
| L1 — Verifier | `IB-COMM-QA` | Sonnet | Gate G-COMM su cross-sell e testimonianze (indipendente, bloccante) |
| L2 — Specialist | `IB-COMM-RETENTION` · `IB-COMM-SOCIAL` · `IB-COMM-CROSSSELL` | Sonnet | Win-back, social proof, scoring cross-sell (decisioni di giudizio) |
| L3 — Runner | `IB-COMM-ONBOARDER` · `IB-COMM-HEALTH` · `IB-COMM-ENGAGE` | Haiku | Esecuzione always-on ad alto volume (sequenze, monitor, rituali) |

---

## Flussi principali

### WF-ONBOARDING-STUDENTE (acquisto → modulo 1 ≤7gg)
```
Trigger: acquisto confermato (da IB-L2-LAUNCH / checkout)
  → IB-COMM-ONBOARDER: email benvenuto APSOC ≤1h (skill `onboarding`)
  → T≤24h: accesso piattaforma attivo + email #2 (GATE: accesso verificato da formazione-student)
  → T≤72h: email #3 + check progress (IB-COMM-HEALTH)
  → T≤7gg: se modulo 1 non completato → recovery gentile (IB-COMM-RETENTION)
  → T=7gg: IB-COMM-HEALTH report coorte → IB-COORD-COMMUNITY
Output: studente attivato + progress tracciato in `infobusiness/community/onboarding/`
Gate: accesso piattaforma verificato; errore → alert IB-COORD-COMMUNITY
```

### WF-COMMUNITY-ATTIVA (rituali settimanali + social proof)
```
Trigger: cadenza ricorrente (settimanale + mensile)
  → Lun: IB-COMM-ENGAGE prompt discussione
  → Mer: IB-COMM-ENGAGE contenuto bonus
  → Ven: IB-COMM-ENGAGE Q&A live o top-3 domande
  → ogni 2 sett.: IB-COMM-SOCIAL raccolta testimonianza a milestone
  → ogni mese: IB-COMM-HEALTH report community → IB-COORD-COMMUNITY → piano mese successivo
Gate G-COMM (IB-COMM-QA): nessuna testimonianza pubblicata senza metrica verificata
Output: community attiva + testimonianze raccolte + report mensile + segnali cross-sell identificati
```

### WF-CROSSSELL-BRIDGE (segnale → consenso → handoff AGENCY)
```
Trigger: segnale studente (domanda implementazione / completamento >50% / richiesta diretta / survey)
  → IB-COMM-CROSSSELL: scoring (segnale 3pt + completamento ≥50% 2pt + survey positiva 5pt)
  → Score ≥5: prepara dossier {lead_id, fonte_prodotto, segnale, score, consenso}
  → IB-COMM-QA: gate G-COMM (consenso esplicito verificato + segnale documentato)
  → Handoff HC-IB-AG-01 → 01-AGENCY (Acquisizione)
Output: lead qualificato per AGENCY + handoff documentato + relazione studente intatta
Gate: consenso esplicito; nessun outreach automatico — bloccante
```

---

## Flussi con ecosistemi esterni

### IB-L2-COMM ← IB-L2-LAUNCH (coorte studenti)
```
A cart-close, IB-L2-LAUNCH passa la coorte acquirenti a IB-L2-COMM.
Schema: {coorte_id, lista_acquirenti[], prodotto_id, data_cart_close}
IB-COMM-ONBOARDER avvia la sequenza onboarding per ogni acquirente entro 1h.
```

### IB-L2-COMM ↔ formazione-student / formazione-admin (piattaforma)
```
IB-COMM-HEALTH legge da formazione-student: ultimo_accesso, moduli_completati, % progress.
IB-COMM-ONBOARDER verifica con formazione-admin: accesso piattaforma attivato (GATE onboarding).
Schema lettura: {studente_id, ultimo_accesso, moduli_completati[], percent_progress}
```

### IB-L2-COMM → 01-AGENCY (lead cross-sell)
```
IB-COMM-CROSSSELL → handoff HC-IB-AG-01 verso 01-AGENCY (Acquisizione).
Payload: {lead_id, fonte_prodotto, segnale, score, consenso, data_consenso}
Acceptance: consenso esplicito verificato G-COMM; segnale documentato; score ≥ 5.
```

### IB-L2-COMM → IB-L2-PRODUCT (feedback prodotto)
```
Se completion rate di una coorte < soglia → IB-COORD-COMMUNITY segnala a IB-L2-PRODUCT.
Schema: {coorte_id, completion_rate, drop_off_modulo, n_studenti} — input per revisione prodotto.
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-LAUNCH-COMM-01` | IB-L2-LAUNCH → IB-L2-COMM | coorte_id + lista_acquirenti + prodotto_id | coorte completa al cart-close, ogni acquirente con email valida |
| `HC-IB-AG-01` | IB-L2-COMM → 01-AGENCY | lead_id + fonte_prodotto + segnale + score + consenso | consenso esplicito verificato G-COMM; segnale documentato; score ≥ 5 |
| `HC-COMM-PROD-01` | IB-L2-COMM → IB-L2-PRODUCT | coorte_id + completion_rate + drop_off_modulo | report a fine coorte; usato come feedback prodotto |

---

## Namespace memoria

```
infobusiness/community/
├── onboarding/
│   ├── state.json              → per coorte: n. iscritti, attivati, milestone check
│   └── {coorte_id}/            → log sequenza onboarding per coorte
├── health/
│   └── {coorte_id}_health.json → progress, ultimo accesso, alert abbandono per studente
├── engagement/
│   └── {mese}_community.md     → piano rituali + report engagement mensile
├── testimonials/
│   └── {studente_id}_testimonial.md → testimonianza + metrica verificata (G-COMM PASS)
└── crosssell/
    ├── state.json              → scoring per studente, esiti handoff
    └── g-comm-log/             → log gate G-COMM (consenso + segnale, PASS/FAIL) — inviolabile
```

---

## Skill del reparto

| Skill | File | Funzione |
|---|---|---|
| `crosssell-bridge` (P0, nuova) | `skills/SKILLS.md` | Gate G-COMM deterministico: consenso + segnale + score ≥ soglia |
| `onboarding` (esistente) | mapping dossier | Sequenza attivazione — IB-COMM-ONBOARDER |
| `churn-prevention` (esistente) | mapping dossier | Win-back — IB-COMM-RETENTION |
| `community-marketing` (esistente) | mapping dossier | Strategia community — IB-COMM-ENGAGE |

---

## Connessioni

- [[README]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-COMM-Community-Retention/README.md`
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-COMM
- [[WF-ONBOARDING-STUDENTE]] · `workflow/WF-ONBOARDING-STUDENTE.md`
- [[WF-COMMUNITY-ATTIVA]] · `workflow/WF-COMMUNITY-ATTIVA.md`
- [[WF-CROSSSELL-BRIDGE]] · `workflow/WF-CROSSSELL-BRIDGE.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — prove non promesse)
- [[IB-COMMUNITY-manager]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-COMMUNITY-manager.md`
