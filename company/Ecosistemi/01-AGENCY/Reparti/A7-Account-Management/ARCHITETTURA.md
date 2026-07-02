---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #account-management #customer-success #retention #A7
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — A7 Account Management & Customer Success

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.

---

## 1. Gerarchia interna

```
01-AGENCY (L1) — AG-DIR
   └── A7 Account Management & Customer Success
         │
         AG-A7-COORD — KAM Lead (coordinator, sonnet)
         ├── AG-A7-ONBOARD Onboarding Specialist (worker, sonnet)
         │     → prima settimana post-firma; presenta processo e milestone
         ├── AG-A7-MID Mid-Point Reviewer (worker, sonnet)
         │     → check a metà delivery (G+3-4); clima cliente, scope
         ├── AG-A7-CLOSE Closure Manager (worker, sonnet)
         │     → fine 90gg: NPS survey, feedback, upsell/referral → A6
         ├── AG-A7-HEALTH Account Health Monitor (worker, haiku)
         │     → dashboard salute cliente; alert automatici churn
         ├── AG-A7-COMM Comunicatore Cliente (worker, sonnet)
         │     → drafta comunicazioni formali su voce di Max
         └── AG-A7-QA Verificatore Customer Success (verifier, sonnet)
               → controlla SLA ticket (A4), milestone, NPS; blocca su rischio
```

**Principio di coordinamento:** AG-A7-COORD è il Key Account Manager assegnato a ogni cliente
alla firma; è il proprietario unico della relazione post-firma e riporta ad AG-DIR. Assegna
i task agli specialisti per fase del ciclo di vita (onboarding → mid → closure). AG-A7-QA è
bloccante su ogni chiusura di milestone, su ogni alert di churn e su ogni closure 90gg:
nessun cliente passa di fase senza che SLA, milestone e NPS siano verificati.

---

## 2. Flussi principali (firma → 90gg → upsell)

### 2.1 Ciclo di vita cliente completo (WF-CUSTOMER-LIFECYCLE)

```
[A4-Delivery: cliente live, contratto firmato]
         │
         ▼
AG-A7-COORD — assegnazione KAM; apre anagrafica in agency/07-account/clients
         │
         ▼
[G+0] AG-A7-ONBOARD — introduce processo, spiega milestone, fissa cadenza touchpoint
         │
         ▼
[ogni settimana] AG-A7-HEALTH — monitora milestone, ticket aperti (da A4), NPS trend
         │
         ▼
[G+3-4] AG-A7-MID — mid-point review: clima cliente, aggiustamenti di scope
         │
         ▼
[G+7] Gate Delivery — check con A10-QA (operations); milestone loggate
         │
         ▼
[settimane 2-12] supporto via A4 (ticket); AG-A7-COORD supervisiona SLA
         │
         ▼
[G+90] AG-A7-CLOSE — NPS survey + feedback + proposta upsell/referral
         │
         ▼
AG-A7-QA — gate finale: NPS raccolto? milestone complete? KAM assegnato per tutto il ciclo?
  → PASS: closure registrata; handoff upsell→A3 / referral→A6 / cross-sell→02-INFO
  → FAIL: AG-A7-COORD ripristina il dato mancante prima di chiudere
```

### 2.2 Intercettazione churn (WF-RETENTION-ALERT)

```
AG-A7-HEALTH — monitora segnali su agency/07-account/health
  → ticket multipli aperti · risposta cliente lenta · NPS intermedio ≤6
         │
         ▼
[entro 24h] alert → AG-A7-COORD (registrato in agency/07-account/alerts)
         │
         ▼
AG-A7-COORD — sceglie azione correttiva:
  → check call (AG-A7-COMM drafta) · fix urgente (escalation A4) · coinvolgimento Max
         │
         ▼
AG-A7-QA — verifica che l'azione sia registrata e che il segnale sia rientrato
  → PASS: alert chiuso con esito · FAIL: alert resta aperto, escalation AG-DIR
```

### 2.3 Handoff upsell / referral a fine ciclo

```
AG-A7-CLOSE — NPS ≥8 e scope ampliabile rilevato
         │
         ▼
upsell-mapper (skill) — mappa opportunità: nuovo sprint, retainer, cross-sell info-product
         │
         ▼
→ A3-Preventivi (upsell sprint/retainer) · → 02-INFO-BUSINESS (cross-sell corso)
→ A6-Marketing-Interno (referral / case study se NPS alto)
  → AG-A7-COORD registra l'esito in agency/07-account/clients
```

---

## 3. Confine con A4-Delivery — relazione vs esecuzione

| Aspetto | A7 Account Management (relazione) | A4-Delivery (esecuzione) |
|---|---|---|
| Proprietà cliente | Possiede la relazione post-firma (KAM unico) | Possiede l'esecuzione tecnica dello sprint |
| Ticket di supporto | Supervisiona SLA, escala se a rischio | Apre, lavora e chiude i ticket |
| Milestone | Verifica che siano loggate e comunicate al cliente | Produce e consegna gli artefatti milestone |
| Comunicazione cliente | Drafta e invia comunicazioni formali (AG-A7-COMM) | Comunica dettagli tecnici interni allo sprint |
| Salute del rapporto | Monitora NPS, clima, rischio churn | Non presidia il sentiment relazionale |
| Chiusura 90gg | Esegue NPS, feedback, upsell/referral | Consegna ultimo artefatto e chiude la delivery |

**Regola d'oro:** A4 consegna il lavoro; A7 presidia la relazione attorno al lavoro. Il dato
di SLA ticket è il documento di confine: A4 lo produce, A7 lo legge e agisce sul rischio.
A7 non lavora ticket tecnici; A4 non gestisce NPS, upsell o churn.

---

## 4. Namespace memoria — `agency/07-account/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/07-account/clients` | Anagrafica cliente, KAM assegnato, milestone, stato ciclo, esito upsell/referral | AG-A7-COORD |
| `agency/07-account/health` | Dashboard salute: milestone, ticket aperti (da A4), NPS trend, rischio churn | AG-A7-HEALTH |
| `agency/07-account/alerts` | Alert churn: segnale, data, azione correttiva, esito, stato | AG-A7-COORD |
| `agency/07-account/touchpoints` | Log touchpoint: onboarding, mid-review, closure, comunicazioni inviate | AG-A7-COMM |

**Regola di integrità:** nessun cliente può esistere in `agency/07-account/clients` senza
campo `kam` popolato. Un cliente senza KAM assegnato è un'anomalia bloccante (vedi REGOLE R1).
Nessun dato personale sensibile (PII) oltre nome contatto e ruolo: i recapiti vivono nel CRM,
non nello state (vedi `state/README.md`).

---

## 5. Integrazione con altri reparti e ecosistemi

| Reparto / Ecosistema | Relazione |
|---|---|
| A4-Delivery | Fornisce cliente live + SLA ticket + artefatti milestone (input continuo) |
| A3-Preventivi | Riceve upsell mappati a fine ciclo (nuovo sprint / retainer) |
| A6-Marketing-Interno | Riceve referral e richieste case study quando NPS è alto |
| 02-INFO-BUSINESS | Riceve cross-sell (corso/info-product) per clienti con bisogno formativo |
| 09-OPERATIONS (A10-QA) | Gate Delivery a G+7; verifica milestone loggate |
| 08-INTELLIGENCE | Aggrega NPS e churn rate per report di ecosistema (sola lettura) |

---

## 6. State e ripartibilità

Ogni esecuzione di WF-CUSTOMER-LIFECYCLE produce un `state.json` in
`agency/07-account/clients/{client_id}/` con i campi:
- `client_id` — identificativo univoco del cliente
- `kam` — agente AG-A7-COORD assegnato (obbligatorio, mai vuoto)
- `fase_ciclo` — onboarding / delivery / supporto / closure / chiuso
- `milestone` — lista con stato (loggata / comunicata / completata)
- `nps` — punteggio raccolto a G+90 ([DM] finché non raccolto)
- `alert_aperti` — lista alert churn non ancora rientrati
- `upsell_referral` — stato handoff a A3 / A6 / 02-INFO
- `last_updated` — timestamp ultimo aggiornamento

Questo permette la **ripartibilità a freddo**: un nuovo KAM (o lo stesso dopo amnesia di
sessione) rientra nel ciclo dal punto esatto leggendo lo state, senza ricostruire il contesto
relazionale da zero (test amnesia §6 V2).

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A7`
- [[A4-Delivery]] · fornitore di cliente live + SLA ticket
- [[A3-Preventivi]] · destinatario degli upsell mappati
- [[WF-CUSTOMER-LIFECYCLE]] · `workflow/WF-CUSTOMER-LIFECYCLE.md`
- [[WF-RETENTION-ALERT]] · `workflow/WF-RETENTION-ALERT.md`
