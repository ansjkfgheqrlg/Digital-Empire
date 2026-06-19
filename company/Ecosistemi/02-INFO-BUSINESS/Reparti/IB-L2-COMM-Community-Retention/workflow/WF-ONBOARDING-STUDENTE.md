---
Type: CONCEPT
Status: Active
Tags: #workflow #infobusiness #community #onboarding #IB-L2-COMM
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-ONBOARDING-STUDENTE — Onboarding e Attivazione Studente

> **Workflow:** WF-ONBOARDING-STUDENTE · **Reparto:** IB-L2-COMM Community & Retention
> **Trigger:** acquisto confermato (da IB-L2-LAUNCH / checkout)
> **Output:** studente attivato (modulo 1 completato ≤7gg) + progress tracciato
> **Gate di uscita:** accesso piattaforma verificato entro 24h
> **Wrappa:** WF v1 `WF-ONBOARDING-STUDENTE` (IB-R4) — TARGET-V2.

---

## Scopo

Portare ogni acquirente dalla conferma d'ordine al primo modulo completato in ≤7 giorni, con
esperienza fluida e zero friction tecnica. Nessun acquirente aspetta il giorno dopo: email entro
1h, accesso entro 24h. È il workflow che rende vero il principio "il prodotto inizia dopo l'acquisto".

---

## Trigger

- **Evento:** acquisto confermato sul checkout o coorte ricevuta da IB-L2-LAUNCH (HC-LAUNCH-COMM-01).
- **Cadenza:** event-driven per singolo acquirente + scan giornaliero per i follow-up temporizzati.

---

## Input (JSON)

```json
{
  "coorte_id": "lancio-2026-Q3-corso-X",
  "studente_id": "stud-1183",
  "email": "studente@example.com",
  "nome": "Marco",
  "prodotto_id": "corso-claude-code",
  "timestamp_acquisto": "2026-06-18T09:00:00Z"
}
```

---

## Pipeline (step + owner)

```
[T=0] Acquisto confermato — owner: IB-COMM-ONBOARDER
  → verifica idempotenza (sequenza già avviata per studente_id? se sì → stop, no duplicati)
  → invia email #1 benvenuto APSOC ≤1h (skill `onboarding`): "ecco cosa ti aspetta, ecco come accedere"

[T≤24h] Attivazione accesso — owner: IB-COMM-ONBOARDER + formazione-admin
  → richiede attivazione accesso piattaforma a formazione-admin
  → invia email #2: "il tuo percorso inizia qui"
  → GATE: accesso verificato (log da formazione-student)

[T≤72h] Follow-up — owner: IB-COMM-ONBOARDER + IB-COMM-HEALTH
  → email #3: "hai guardato la lezione 1? ecco cosa imparerai questa settimana"
  → IB-COMM-HEALTH legge progress da formazione-student

[T≤7gg] Recovery condizionale — owner: IB-COMM-RETENTION
  → SE modulo 1 non completato → email gentile recovery: "hai bisogno di aiuto?"
  → SE delusione prodotto rilevata → segnale a IB-L2-PRODUCT

[T=7gg] Report coorte — owner: IB-COMM-HEALTH
  → % acquirenti con modulo 1 completato → IB-COORD-COMMUNITY
```

---

## Gate

| Gate | Owner | Criterio | Fallimento |
|---|---|---|---|
| **G-ACCESS** (≤24h) | IB-COMM-ONBOARDER | Accesso piattaforma verificato via formazione-student | Alert immediato a IB-COORD-COMMUNITY + email allo studente "stiamo sistemando" |
| **G-EMAIL** (≤1h) | IB-COMM-ONBOARDER | Email #1 inviata e non in bounce | Bounce → segnala coorte da bonificare a IB-COORD-COMMUNITY |

---

## Output (JSON)

```json
{
  "coorte_id": "lancio-2026-Q3-corso-X",
  "studente_id": "stud-1183",
  "stato_onboarding": "attivato | in_recovery | bloccato_accesso",
  "email_inviate": ["#1 benvenuto", "#2 accesso", "#3 follow-up"],
  "accesso_verificato": true,
  "modulo1_completato": true,
  "tempo_attivazione_ore": 18,
  "namespace": "infobusiness/community/onboarding/lancio-2026-Q3-corso-X/",
  "timestamp": "2026-06-25T09:00:00Z"
}
```

---

## Handoff

- **← IB-L2-LAUNCH** (HC-LAUNCH-COMM-01): riceve la coorte acquirenti al cart-close.
- **→ IB-COMM-RETENTION**: passa il segnale recovery se modulo 1 non completato a 7gg.
- **→ IB-COMM-HEALTH**: alimenta il monitoraggio continuo post-onboarding.
- **→ IB-L2-PRODUCT** (HC-COMM-PROD-01): se la coorte mostra drop-off su un modulo specifico.

---

## Dry-run (esempio)

**Trigger:** Marco acquista "corso-claude-code" il 2026-06-18 alle 09:00.

1. **T=0** — IB-COMM-ONBOARDER: verifica idempotenza (nessuna sequenza attiva) → invia email #1
   alle 09:40 (entro 1h). G-EMAIL PASS.
2. **T+16h** — accesso piattaforma attivato via formazione-admin alle 01:00 del giorno dopo →
   email #2 inviata. G-ACCESS PASS (verificato via formazione-student, tempo: 16h < 24h).
3. **T+72h** — email #3; IB-COMM-HEALTH legge: Marco ha guardato la lezione 1 ma non completato modulo 1.
4. **T+7gg** — modulo 1 ancora non completato → IB-COMM-RETENTION invia email recovery gentile.
   Marco riprende, completa il modulo 1 il giorno 7.
5. **T=7gg** — IB-COMM-HEALTH report: 73/120 modulo 1 completato (61%) → IB-COORD-COMMUNITY.

**Output:** `stato_onboarding: "attivato"`, `tempo_attivazione_ore: 16`, modulo 1 completato. Coorte
al 61% di attivazione → sopra la soglia minima, nessuna escalation prodotto.

---

## Connessioni

- [[ib-comm-onboarder]] · `agenti/ib-comm-onboarder.md`
- [[ib-comm-health]] · `agenti/ib-comm-health.md`
- [[ib-comm-retention]] · `agenti/ib-comm-retention.md`
- [[WF-COMMUNITY-ATTIVA]] · `workflow/WF-COMMUNITY-ATTIVA.md`
- [[state-readme]] · `state/README.md`
- [[IB-R4-COMMUNITY-RETENTION]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-R4-COMMUNITY-RETENTION.md` (v1 wrappato)
