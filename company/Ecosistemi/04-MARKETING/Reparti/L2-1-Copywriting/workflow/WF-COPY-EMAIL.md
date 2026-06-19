---
Type: WORKFLOW
Status: Active
Tags: #workflow #copywriting #email #sequenze #lifecycle #L2.1 #L2.3
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COPY-EMAIL — Workflow Copy Sequenze Email

> **Ecosistema:** 04-MARKETING · **Reparto:** L2.1 Copywriting (coordinamento con L2.3)
> **Gate di uscita:** score A8 ≥80 per email + deliverability check E2 (L2.3)

---

## Scopo

Produce il copy delle sequenze email (lancio, nurture, onboarding, win-back) usando APSOC
adattato al formato email. Ogni email della sequenza ha una funzione specifica nella narrativa
lifecycle. WF-COPY-EMAIL è il provider copy per i workflow di L2.3 Email & Lifecycle —
L2.3 possiede la logica della sequenza (trigger, timing, branching); L2.1 possiede il
copy di ogni singola email.

---

## Tipologie di sequenza supportate

| Tipo | Descrizione | N. email tipico |
|---|---|---|
| `lancio` | Pre-lancio → apertura → proof → obiezioni → scarcity → chiusura | 7-10 email |
| `nurture` | Welcome + educazione + case study + offerta morbida | 5-7 email |
| `onboarding` | Attivazione post-acquisto + quick wins + uso prodotto | 3-5 email |
| `win-back` | Churn prevention + re-engagement lista fredda | 3-4 email |

---

## Passi del workflow

### Step 1 — Contratto sequenza (COPY-MASTER)
**Agente:** COPY-MASTER
**Input:** contratto con `formato: "email-seq"`, tipo sequenza, n. email, obiettivo finale
**Azione:** verifica ICP + awareness level per ogni stadio della sequenza; coordina con EMAIL-LEAD (L2.3)
per la struttura della sequenza (trigger, timing) prima di iniziare il copy
**Output:** contratto validato + struttura sequenza approvata da EMAIL-LEAD

### Step 2 — Briefing per sequenza (A1)
**Agente:** A1 Briefing Analyst
**Input:** contratto + struttura sequenza + materiali
**Azione:** briefing-completo.md + per ogni email: obiettivo specifico, awareness level atteso
nel punto della sequenza, proof disponibili per quella email
**Output:** `briefing-email-seq.md` con una riga per ogni email della sequenza

### Step 3 — Avatar + pain map (A2, se non in namespace)
**Agente:** A2 Target Analyst
**Input:** ICP della sequenza
**Azione:** per sequenze di lancio è fondamentale l'avatar con pain map a 3 livelli; per nurture
e onboarding basta l'avatar base; per win-back serve anche la mappa "motivi di churn"
**Output:** avatar path + motivi-churn (per win-back)

### Step 4 — Copy per ogni email (A3-A7 in iterazione per email)
**Agente:** COPY-MASTER coordina A3-A7 per ogni email della sequenza
**Struttura per email:**
- **Subject line:** A3 produce ≥2 alternative (la subject è la headline dell'email)
- **Hook apertura:** A3 (prime 1-2 righe — le uniche lette nel preview)
- **Corpo:** A4-A5-A6 in versione condensata (ogni email ha 1 funzione APSOC dominante)
- **CTA:** A7 micro-commitment (email = basso attrito — non chiedere troppo)

**Adattamento APSOC per email:**
- Email 1 lancio: A dominante (attenzione pura)
- Email 2-3 lancio: P dominante (amplificazione problema)
- Email 4-5 lancio: S dominante (soluzione + proof)
- Email 6-7 lancio: O dominante (gestione obiezioni)
- Email 8-9 lancio: C dominante (CTA + urgenza)

**Output:** `email-copy-seq.md` con ogni email strutturata

### Step 5 — Gate G1 per email (A8)
**Agente:** A8 Copy Reviewer
**Input:** ogni email del pacchetto
**Azione:** scoring APSOC condensato per ogni email; per email la soglia è ≥80 per email ma
si verifica anche la coerenza narrativa della sequenza nel suo insieme
**Gate G1:** ≥80 per email → PASS | < 80 → COPY-QA-LEAD
**Output:** `qa-report-email-seq.md`

### Step 6 — Deliverability check (E2, L2.3)
**Agente:** E2 Deliverability Guard (L2.3 Email & Lifecycle)
**Input:** email gated G1
**Azione:** spam score, controllo trigger parole spam, lunghezza subject, ratio testo/link
**Gate deliverability:** PASS → rilascia a L2.3 per scheduling | FAIL → indica email problema
**Output:** `deliverability-report.md`

---

## Gate di uscita

| Gate | Responsabile | Soglia | Bloccante |
|---|---|---|---|
| G1 Score APSOC | A8 | ≥80 per email | SI |
| Deliverability | E2 (L2.3) | PASS | SI — prima dell'invio |

---

## Connessioni

- [[WF-EMAIL-LAUNCH]] · `company/Ecosistemi/04-MARKETING/Reparti/L2-3-Email-Lifecycle/workflow/WF-EMAIL-LAUNCH.md` — usa questo WF come provider copy
- [[L2-3-Email-Lifecycle]] · reparto che possiede la struttura sequenza; L2.1 possiede il copy
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[copy-master]] · `agenti/copy-master.md`
