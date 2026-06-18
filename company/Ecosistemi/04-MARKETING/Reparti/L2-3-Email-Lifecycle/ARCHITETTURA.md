---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #email #lifecycle #L2.3 #namespace #flussi
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — L2.3 Email & Lifecycle

> Documento di architettura interna del reparto. Descrive la gerarchia, i flussi lifecycle
> completi, i confini operativi e il namespace di memoria. Standard CF-grade (ADR-007).

---

## 1. Gerarchia interna

```
L2.3 — Email & Lifecycle
│
├── EMAIL-LEAD (coordinator, sonnet)
│     └── coordina tutto il reparto; strategia lifecycle; KPI; escalation
│
├── E1 — Lifecycle Architect (worker, sonnet)
│     └── disegna ogni sequenza: trigger, timing, branching condizionale
│
├── E2 — Deliverability Guard (verifier, sonnet)  ← GATE BLOCCANTE
│     └── spam score, igiene lista, SPF/DKIM/DMARC, PII check obbligatorio
│
├── E3 — Segmentation Analyst (worker, sonnet)
│     └── segmenti per ICP × awareness × comportamento; input da AN3
│
├── E4 — Onboarding Specialist (worker, sonnet)
│     └── welcome + attivazione per SaaS/Info; committenti 05-MB / 02-INFO
│
├── E5 — Win-Back Specialist (worker, sonnet)
│     └── post-cancel, churn prevention, dunning; A6 come asse obiezioni
│
└── E-QA — Email QA Verifier (verifier, sonnet)  ← GATE BLOCCANTE
      └── gate finale: A8 score + brand gate + deliverability pre-invio
```

**Regola gate:** E2 e E-QA sono bloccanti — nessuna email esce senza entrambi i gate.
La catena è: E1 (struttura) → E3 (segmenti) → L2.1 (copy, via WF-COPY-EMAIL) →
E4/E5 (specialisti se rilevanti) → E2 (deliverability) → E-QA (gate finale).

---

## 2. Lifecycle completo — le 5 tipologie

### 2.1 Sequenza Lancio (WF-EMAIL-LAUNCH)
Committente principale: **02-INFO-BUSINESS** (lancio corso/ebook/community).
Struttura narrativa a 7 fasi:
```
T-14 — Pre-lancio: valore puro, curiosità, costruzione anticipazione
T-7  — Apertura lista early: social proof + proposta
T-5  — Proof: testimonianze, risultati, case study
T-3  — Obiezioni principali: A6 come motore (email + landing)
T-1  — Scarcity reale (mai falsa — Mandato Art.2.3)
T+0  — Apertura carrello: CTA diretta
T+3  — Chiusura: ultima email urgenza + recap benefici
```
Gate: WF-COPY-EMAIL score A8 ≥80 su ogni email; E2 deliverability; G2 brand gate;
review umana obbligatoria nelle prime fasi (Art.4.4 Mandato — non si automatizza il lancio).

### 2.2 Welcome + Nurture (WF-EMAIL-NURTURE)
Committenti: tutti gli ecosistemi con lista email opt-in.
Struttura standard:
```
Email 1 (T+0) — Welcome: chi siamo, cosa aspettarsi, quick win
Email 2 (T+2) — Valore: contenuto educativo per ICP
Email 3 (T+5) — Social proof: case study / storia cliente
Email 4 (T+9) — Approfondimento: problema + soluzione parziale
Email 5 (T+14) — CTA: invito a passo successivo (consulenza / prodotto)
Re-engagement (T+30 per inattivi): "sei ancora con noi?"
```
Branch condizionale: chi non apre le prime 3 email → sequenza re-engagement accelerata
(E1 progetta il branch; E3 identifica il segmento).

### 2.3 Onboarding Attivazione (WF-EMAIL-ONBOARDING)
Committenti: **05-MULTI-BUSINESS** (SaaS/canale YouTube), **02-INFO-BUSINESS** (corso acquistato).
Obiettivo: portare il nuovo utente al primo "aha moment" entro 7 giorni.
```
T+0  — Welcome + accesso: link immediato, cosa fare adesso
T+1  — Primo passo: 1 azione specifica (non 5)
T+3  — Check-in: "hai completato X?"  se no → reminder specifico
T+7  — Milestone: celebrazione primo risultato concreto
T+14 — Upsell / comunità: invito al passo successivo
```
Pattern chiave: ogni email ha 1 sola CTA. Il tasso di attivazione (primo passo completato)
è il KPI principale. Stored in `marketing/email/sequences/onboarding/`.

### 2.4 Win-Back / Churn Prevention (WF-EMAIL-WINBACK)
Committenti: 05-MB (SaaS cancel), 02-INFO (abbandono community), 01-AGENCY (clienti inattivi).
Struttura 4 fasi:
```
Fase 1 — Rilevamento: E5 riceve trigger cancel/inattività da committente
Fase 2 — Exit survey: email breve (2 domande max) → insight motivo churn
Fase 3 — Sequenza win-back: E5 + A6 (obiezioni = motivo churn + CPB)
Fase 4 — Dunning (SaaS): reminder pagamento con empathy, non pressione
```
A6 (Objections Handler) è l'asse portante: il churn è un'obiezione non gestita in tempo.
Insight exit survey → AN4 → pattern "motivi di churn per ICP" in `marketing/email/sequences/winback/patterns/`.

### 2.5 Email Transazionali
Conferme acquisto, notifiche, ricevute — progettate una volta e non cambiate.
E1 le architetta; E-QA verifica brand gate; E2 verifica deliverability tecnica.
Non seguono workflow completo: usano template approvati + check E-QA spot.

---

## 3. Confine col cold outreach (ADR-003 — non derogabile)

| Proprietà | In questo reparto (L2.3) | In 01-AGENCY (fuori) |
|---|---|---|
| **Lista** | Opt-in esistente (ha espresso interesse) | Cold (nessuna relazione precedente) |
| **Strumento** | ESP (Mailchimp, ActiveCampaign, ecc.) | `writer.py`, Outreach Workflow |
| **Runtime** | Questo reparto | 01-AGENCY intoccabile (ADR-003) |
| **QA standard** | E-QA (questo reparto) | T-REVIEW L2.1 su template → E-QA consulta |
| **APSOC+V** | Standard proprietà Marketing | Applicato via wrapper (ADR-003) |

**Regola:** L2.3 non scrive né modifica script cold. Può fare QA del template (via T-REVIEW
di L2.1 + E-QA come consulente) quando 01-AGENCY lo richiede esplicitamente.

---

## 4. Namespace memory (`marketing/email/sequences`)

Schema standard per ogni sequenza archiviata:

```
marketing/email/sequences/
├── launch/
│   ├── {lancio_id}/
│   │   ├── sequence_map.json       ← output E1 (trigger, timing, branch)
│   │   ├── emails/                 ← copy gated (A8 ≥80)
│   │   │   ├── email_01.md
│   │   │   └── ...
│   │   ├── deliverability_report.json  ← output E2
│   │   └── qa_report.json          ← output E-QA
├── nurture/
│   └── {lista_id}/
├── onboarding/
│   └── {prodotto_id}/
└── winback/
    ├── {progetto_id}/
    └── patterns/
        └── {icp_id}.json           ← pattern motivi churn da AN4
```

**Regole integrità namespace:**
- Ogni sequenza ha un `sequence_id` univoco (prefisso: `SEQ-YYYY-NNN`).
- I report E2 e E-QA sono obbligatori: nessuna sequenza è "completa" senza entrambi.
- Le email non-gated (A8 <80) non entrano nel namespace — rientrano solo dopo correzione.
- PII policy: nessun dato anagrafico reale nelle sequenze; solo `{nome}`, `{email}` come placeholder.

---

## 5. PII check obbligatorio (Mandato Art.7.2)

**Prima di ogni elaborazione di lista email:**
1. Verificare che il committente abbia dichiarato la base giuridica (consenso / legittimo interesse).
2. `aidefence_has_pii` obbligatorio su ogni sample di lista prima dell'elaborazione (E2 esegue).
3. Dati anagrafici reali non transitano nel namespace: solo aggregate o pseudonimizzati.
4. In caso di PII non dichiarata o non gestita: E2 blocca, escalation immediata a MKT-Conductor.
5. Log dell'esito PII check in ogni `deliverability_report.json`.

---

## 6. Integrazioni cross-reparto e cross-ecosistema

```
08-INTELLIGENCE ──► E3 (dati ICP e comportamento lista)
L2.1 Copywriting ──► ogni email (copy via WF-COPY-EMAIL; A8 gate)
L2.4 Analytics ─────► AN3 (test), AN4 (pattern), AN2 (performance)
L2.6 Conv. Arch. ──► obiettivi stage email nel funnel
02-INFO-BUSINESS ──► trigger lancio (date, prodotto, avatar)
05-MULTI-BUSINESS ──► trigger onboarding (nuovo utente SaaS/canale)
06-PLATFORM ────────► ESP setup tecnico (SPF/DKIM/DMARC — E2 verifica, Platform configura)
```

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.3`
- [[L2-3-Email-Lifecycle-README]] · `Reparti/L2-3-Email-Lifecycle/README.md`
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
