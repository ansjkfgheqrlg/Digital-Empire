> Fonte: PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md sez. 2 (L2.3 — EMAIL MARKETING)

# L2.3 — EMAIL MARKETING

> Reparto L2 · Ecosistema: 04-MARKETING
> Ecosistema: `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md`
> Backbone: `company/Ecosistemi/04-MARKETING/BACKBONE.md`

---

## Missione

Email lifecycle "warm": **lancio, nurture, onboarding, win-back/post-cancel**. Produce le sequenze; il copy di ogni singola email passa sempre dal motore L2.1 (WF-COPY-EMAIL).

**Confine col cold outreach:** il cold outreach operativo (Outreach Workflow, writer.py) resta in 01-AGENCY. Marketing L2.3 possiede lo **standard APSOC+V** e fa da QA/evoluzione dei template cold via T-REVIEW (L2.1). Fonte di verità standard: `wiki/concepts/Framework_Cold_Outreach_APSOC.md`.

---

## Struttura interna

| Livello | ID | Contenuto |
|---|---|---|
| Workflow L3 | WF-EMAIL-LAUNCH | Sequenza lancio prodotto (committente tipico: 02-INFO-BUSINESS) |
| Workflow L3 | WF-EMAIL-NURTURE | Welcome + nurture + re-engagement lista |
| Workflow L3 | WF-EMAIL-WINBACK | Post-cancel / churn prevention (skill churn-prevention + emails) |
| Funzione L4 | T-SUBJECT | Subject line testing (usa T-HEADLINE di L2.1 come motore) |
| Funzione L4 | T-SEGMENT | Segmentazione lista per ICP e awareness level |
| Funzione L4 | T-DELIVERABILITY | Igiene lista, warm-up, spam-score, autenticazione dominio |

---

## Agenti L5

| Codice | Agente | Ruolo | Stato |
|---|---|---|---|
| E1 | Lifecycle Architect | Disegno sequenze (trigger, timing, branching) | NUOVO |
| E2 | Deliverability Guard | Spam score, igiene lista, autenticazione | NUOVO |
| E3 | Segmentation Analyst | Segmenti per ICP × awareness × comportamento | NUOVO |

---

## Tre workflow email (sintesi §4c)

**LANCIO** (committente: 02-INFO-BUSINESS)
- E1 disegna sequenza: pre-lancio → apertura → proof → obiezioni → scarcity → chiusura
- WF-COPY-EMAIL scrive ogni email (A6 per le email-obiezione)
- E3 segmenta lista per awareness → E2 verifica deliverability → gate A8 + brand gate G2

**NURTURE** (lista DE / liste clienti multi-tenant via brand_kit)
- E1 disegna welcome + valore ricorrente → T-SUBJECT genera/testa subject
- WF-AB-TEST su subject e CTA → AN4 (L2.4) distilla pattern aperture/click per ICP

**WIN-BACK / POST-CANCEL** (committenti: 02-INFO, 05-MULTI-BUSINESS/SaaS)
- Trigger churn → E1 sequenza win-back (skill churn-prevention)
- A6 Objections Handler: il churn è un'obiezione non gestita
- Exit survey → insight a AN4 → pattern "motivi churn per ICP" in memoria

---

## Vincolo PII

**`aidefence_has_pii` obbligatorio** prima di ogni elaborazione lista email. E2 è owner della policy PII di questo reparto.

---

## KPI principali

| KPI | Definizione |
|---|---|
| Open rate / click rate / reply rate | Per sequenza e segmento ICP |
| Deliverability score | Spam score medio per sequenza |
| Costo per run | Cost-attribution (Cost-Sentinel) |

---

## Connessioni

- `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md` — ecosistema padre
- `company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting.md` — fornitore copy email
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-E1-lifecycle-architect.md`
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-E2-deliverability-guard.md`
- `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md` — standard APSOC+V
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` §2 (L2.3), §4c

*Fonte: dossier 04 §2 (L2.3), §4c · Aggiornato: 2026-06-12*
