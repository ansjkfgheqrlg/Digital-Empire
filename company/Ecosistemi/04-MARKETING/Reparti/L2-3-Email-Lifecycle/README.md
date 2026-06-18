---
Type: REPARTO
Status: Active
Tags: #reparto #marketing #email #lifecycle #nurture #onboarding #winback #L2.3
Created: 2026-06-18
Last updated: 2026-06-18
---

# L2.3 — Email & Lifecycle

> **Ecosistema:** 04-MARKETING · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.3`
> **Standard:** CF-grade (ADR-007) · **Evoluisce il v1 (E1-E3 in `company/Ecosistemi/04-MARKETING/Agenti/`) — NON toccare i file v1 (ADR-003)**

---

## Missione

Email lifecycle completo — lancio, onboarding, nurture, win-back/post-cancel, transazionale.
Marketing possiede lo **standard APSOC+V** e fa QA/evoluzione dei template; il copy delle
email viene sempre da L2.1 (WF-COPY-EMAIL) o dal gate A8. Il contenuto strategico — trigger,
timing, branching, segmentazione — è di questo reparto.

**Confine con il cold outreach operativo (ADR-003 — NON negoziabile):** il cold outreach
(Outreach Workflow, `writer.py`, campagne cold 01-AGENCY) resta integralmente in 01-AGENCY.
Marketing possiede lo standard qualitativo (APSOC+V ≥80) e fa QA/revisione dei template
via T-REVIEW di L2.1. Non tocca il runtime operativo.

---

## Roster del reparto (7 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `EMAIL-LEAD` | Email & Lifecycle Lead | `agenti/email-lead.md` | coordinator | sonnet | Coordina il reparto; strategia lifecycle; risponde dei KPI email |
| `E1` | Lifecycle Architect | `agenti/e1-lifecycle-architect.md` | worker | sonnet | Disegno sequenze: trigger, timing, branching per awareness × comportamento |
| `E2` | Deliverability Guard | `agenti/e2-deliverability-guard.md` | verifier | sonnet | Spam score, igiene lista, SPF/DKIM/DMARC; PII check obbligatorio Art.7 |
| `E3` | Segmentation Analyst | `agenti/e3-segmentation-analyst.md` | worker | sonnet | Segmenti per ICP × awareness × comportamento; input da AN3 |
| `E4` | Onboarding Specialist | `agenti/e4-onboarding-specialist.md` | worker | sonnet | Sequenze onboarding welcome + attivazione per SaaS/Info; committenti 05-MB/02-INFO |
| `E5` | Win-Back Specialist | `agenti/e5-winback-specialist.md` | worker | sonnet | Post-cancel e churn prevention; skill churn-prevention; A6 Objections asse portante |
| `E-QA` | Email QA Verifier | `agenti/e-qa-email-verifier.md` | verifier | sonnet | Verifica ogni email vs A8 score + brand gate + deliverability prima dell'invio |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-EMAIL-LAUNCH** | `workflow/WF-EMAIL-LAUNCH.md` | Sequenza lancio per 02-INFO: pre-lancio → apertura → proof → obiezioni → scarcity → chiusura | WF-COPY-EMAIL score ≥80; E2 deliverability; G2 brand gate; review umana nelle prime fasi (Art.4.4) |
| **WF-EMAIL-NURTURE** | `workflow/WF-EMAIL-NURTURE.md` | Welcome + nurture + re-engagement lista; A/B test subject; AN4 distilla pattern | A8 ≥80; WF-AB-TEST su subject e CTA; AN4 pattern |
| **WF-EMAIL-ONBOARDING** | `workflow/WF-EMAIL-ONBOARDING.md` | Onboarding attivazione utenti SaaS/Info | E4 progetta; E2 verifica; pattern in `marketing/email/sequences` |
| **WF-EMAIL-WINBACK** | `workflow/WF-EMAIL-WINBACK.md` | Post-cancel / churn prevention / dunning; exit survey → insight | E5 + A6; esito → AN4 → pattern motivi churn per ICP |

---

## Skill del reparto

| Skill | Priorità | Note |
|---|---|---|
| `email-lifecycle-architect` | P2 (da forgiarsi) | Skill propria L2.3 — vedi `skills/SKILLS.md` |
| `emails` | esistente | Standard compositivo email; mappata a questo reparto |
| `cold-email` | esistente | Standard cold; QA template dal reparto, runtime in 01-AGENCY |
| `churn-prevention` | esistente | Asse di E5/WF-EMAIL-WINBACK |
| `sms` | esistente | Canale complementare email lifecycle |
| `popups` | esistente | Touchpoint opt-in; input lista per le sequenze |

---

## KPI del reparto

| KPI | Owner | Note |
|---|---|---|
| Open rate per sequenza e segmento ICP | EMAIL-LEAD | Baseline da primo run reale; [DM] |
| Click-through rate (CTA principale) | E-QA | Per tipo di sequenza; [DM] |
| Reply rate (sequenze cold-warm) | E1 | Confine con 01-AGENCY; [DM] |
| Spam score medio degli output | E2 | Target ≤3/10 su ogni batch |
| PII incidents | E2 | Deve essere 0 |
| Churn prevention rate (win-back) | E5 | % recuperati / totale churn; [DM] |
| First-pass QA rate (E-QA) | E-QA | % email che passano gate al primo tentativo |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | L2.1 Copywriting | Copy email gated (WF-COPY-EMAIL, A8 ≥80) |
| ← riceve da | L2.4 Analytics (AN3/AN4) | Insight pattern per segmentazione e ottimizzazione sequenze |
| ← riceve da | L2.6 Conv. Architecture | Obiettivi per stage email nel funnel (MoFu/BoFu) |
| ← riceve da | 02-INFO-BUSINESS | Brief lancio (prodotto, data, avatar, fase awareness) |
| ← riceve da | 05-MULTI-BUSINESS | Brief onboarding (SaaS/canale) |
| → consegna a | 01-AGENCY | Standard QA template cold (T-REVIEW L2.1 → E-QA) |
| → consegna a | AN4 (L2.4) | Pattern sequenze per ICP → ReasoningBank |
| → consegna a | committenti | Sequenza email pronta, gated, con report E-QA |

---

## Escalation

- Lista con PII non verificata → E2 blocca immediatamente; escalation a MKT-Conductor + committente (Art.7.2).
- Score APSOC email <70 dopo 2 iterazioni → EMAIL-LEAD richiede sessione A8 + COPY-MASTER (non si itera indefinitamente).
- Dominio non autenticato (SPF/DKIM/DMARC mancante) → E2 blocca l'invio; escalation a 06-PLATFORM per setup tecnico.
- Sequenza win-back con tasso disengagement >40% della lista → E5 + E2 valutano igiene lista prima di procedere.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.3`
- [[L2-1-Copywriting]] · fornitore copy via WF-COPY-EMAIL; A8 gate su ogni email
- [[L2-4-Analytics]] · AN3 test; AN4 pattern ReasoningBank; AN2 attribution
- [[01-AGENCY-V2]] · confine cold outreach; QA template via T-REVIEW
