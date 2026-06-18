---
Type: WORKFLOW
Status: Active
Tags: #workflow #advertising #campagna #end-to-end #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-ADS-CAMPAIGN — Campagna Advertising End-to-End

> **Reparto:** L2.2 Advertising · **Owner:** ADS-LEAD
> **Trigger:** richiesta campagna da MKT-Conductor con budget ok esplicito Max (Art.4.3)
> **Output:** campagna pronta al lancio in dry-run + richiesta approvazione

---

## Precondizioni obbligatorie (gate di ingresso)

Prima che il workflow parta, ADS-LEAD verifica:
- [ ] `budget_ok_max: true` nel contratto (assente = workflow non parte, returned to sender)
- [ ] Budget approvato da CFO/Cost-Sentinel documentato
- [ ] Piattaforme dichiarate
- [ ] ICP o `brand_kit_id` fornito
- [ ] Obiettivo misurabile dichiarato (lead, opt-in, acquisto)

---

## Passi del workflow

### PASSO 1 — Strategia campagna (S3 Campaign Strategist, L2.1)

**Agente:** S3 Campaign Strategist (in prestito da L2.1)
**Durata stimata:** 20-30 min

S3 riceve il brief e produce:
- Obiettivo di campagna per piattaforma (CPA target, volume lead)
- Struttura campagna (quante campagne, quanti ad set per piattaforma)
- KPI target per dichiarare la campagna un successo
- Note strategiche per AD1 e AD2

**Handoff:** `strategy_brief.json` → ADS-LEAD

---

### PASSO 2 — Audience e Platform Brief (AD1 + AD5, in parallelo)

**Agenti:** AD1 Audience Analyst (parallelo) + AD5 Platform Specialist (parallelo)
**Durata stimata:** 30-40 min (parallelo)

AD1 produce: segmenti per piattaforma, audience brief, budget split consigliato.
AD5 produce: specifiche tecniche per ogni piattaforma, note algoritmiche, brief visual per 03-CF.

**Handoff:** `audience_brief.json` + `platform_brief.json` → AD2

---

### PASSO 3 — Copy Ads (WF-COPY-AD, L2.1)

**Workflow:** WF-COPY-AD (in L2.1, orchestrato da COPY-MASTER)
**Durata stimata:** 15-30 min (varianti brevi)

L2.1 produce: ≥3 varianti copy APSOC con score ≥80 ciascuna.
Il copy non si scrive qui: questo passo è un handoff out verso L2.1 e un handoff in del risultato.

**Gate G1:** copy score ≥80 su ogni variante. Se sotto soglia → L2.1 itera; ADS-CAMPAIGN aspetta.

**Handoff:** `copy_varianti[]` (con `copy_id`, `hook`, `score_APSOC`) → AD2

---

### PASSO 4 — Visual Brief (BR3, L2.5 → 03-CF)

**Agente:** BR3 Creative Director (in prestito da L2.5)
**Durata stimata:** variabile (dipende da 03-CF)

BR3 riceve il platform_brief da AD5 e produce brief visual per 03-CF.
03-CF produce gli asset visivi (fuori dal perimetro di questo workflow).

**Nota:** se visual non disponibili entro deadline → AD2 procede con varianti copy-only su format
testo-permesso (es. LinkedIn Text Ads, Google Search RSA). ADS-LEAD valuta.

---

### PASSO 5 — Assemblaggio matrice creative (AD2)

**Agente:** AD2 Creative Iterator
**Durata stimata:** 20-40 min (dipende da N varianti)

AD2 riceve: copy_varianti (da L2.1) + visual_asset (da 03-CF) + audience_brief (da AD1) + platform_brief (da AD5).
Produce: matrice copy × visual × audience, tutte le creative assemblate.
Se N×M > 4: fan-out swarm (idempotente).

**Handoff:** `creative_matrix[]` → AD4

---

### PASSO 6 — Compliance check (AD4, gate G3)

**Agente:** AD4 Ad Compliance Checker
**Durata stimata:** 15-20 min

AD4 verifica ogni creative per ogni piattaforma: lunghezze, claim, visual, targeting.
**Gate G3:** PASS = continua. FAIL = blocco → riciclo specifico (copy a L2.1, visual a 03-CF).
Massimo 2 cicli di riciclo; se G3 fallisce 2 volte → escalation ADS-LEAD → MKT-Conductor.

**Handoff:** `creative_matrix_compliant[]` → AD3 + AD-QA

---

### PASSO 7 — Setup campagna in dry-run (AD3)

**Agente:** AD3 Media Buyer
**Durata stimata:** 20-30 min

AD3 produce `campaign_plan.json` con:
- Struttura account/campagna/ad_set/ad
- Budget allocation per ad set
- Bid strategy + pacing
- Regole di stop automatico su CPA anomalo
- `dry_run: true` (default assoluto)

---

### PASSO 8 — QA finale (AD-QA, gate pre-lancio)

**Agente:** AD-QA Ads QA Verifier
**Durata stimata:** 15-20 min

AD-QA verifica: brand_kit coerente, pricing corretto, claims verificabili, nessun PII.
**Gate AD-QA:** PASS = campagna pronta al lancio. FAIL = blocco → riciclo specifico.

---

### PASSO 9 — Richiesta approvazione (ADS-LEAD)

**Agente:** ADS-LEAD
**Output finale:** pacchetto campagna per Max

ADS-LEAD produce il summary della campagna pronta:
- N varianti creative approvate
- Budget allocation
- CPA stimato (indicativo da dati storici se disponibili, dichiarato come stima se non)
- `approval_richiesta: true`
- state.json aggiornato con tutti i gate PASS

**Nessun lancio avviene prima dell'approvazione esplicita di Max.**
Quando Max approva: `production: true` viene impostato in state.json con `approval_timestamp`
e `approver`. Solo allora AD3 può procedere al lancio.

---

## Gates di uscita (tutti obbligatori, in serie)

| Gate | Agente | Soglia | Esito fail |
|---|---|---|---|
| **G1 — Copy score** | A8 (L2.1) | ≥80/100 su ogni variante | L2.1 itera; ADS-CAMPAIGN aspetta |
| **G3 — Compliance** | AD4 | PASS su ogni piattaforma | Blocco + riciclo specifico (max 2 cicli) |
| **AD-QA gate** | AD-QA | PASS su brand_kit + pricing + legal | Blocco + riciclo specifico |
| **Approvazione Max** | Max (umano) | ok esplicito registrato in state.json | Nessun lancio senza approvazione |

---

## Handoff contract

**Input contratto (da MKT-Conductor):**
```json
{
  "committente": "01-AGENCY | 02-INFO | 04-MKT",
  "piattaforme": ["Meta", "Google", "LinkedIn", "TikTok"],
  "obiettivo": "azione misurabile",
  "budget_ok_max": true,
  "budget_EUR": "campo popolato a runtime",
  "icp": "id avatar o brief inline",
  "brand_kit_id": "DE | cliente-X",
  "deadline": "YYYY-MM-DD",
  "materiali": "copy esistente, case study, visual existenti se disponibili"
}
```

**Output (pacchetto per approvazione Max):**
```json
{
  "campaign_id": "campo popolato a runtime",
  "stato": "pronta-al-lancio",
  "dry_run": true,
  "production": false,
  "g1_copy_pass": true,
  "g3_compliance_pass": true,
  "ad_qa_pass": true,
  "n_varianti": "campo popolato a runtime",
  "budget_allocato": "campo popolato a runtime",
  "approval_richiesta": true
}
```

---

## Esempio operativo

**Scenario:** 02-INFO-BUSINESS lancia corso "Manuale Claude Code". Campagna Meta, budget
2.000 EUR approvato. Deadline 10 giorni.

**Sequenza:** S3 → (AD1 + AD5 parallelo) + WF-COPY-AD → BR3/03-CF → AD2 → AD4 (G3 PASS)
→ AD3 (dry-run) → AD-QA (PASS) → ADS-LEAD emette pacchetto approvazione Max.
Tempo stimato: 90-120 min (escluso tempo 03-CF per visual).

---

## Connessioni

- [[README]] · `README.md` — missione e roster del reparto
- [[ads-lead]] · `agenti/ads-lead.md`
- [[WF-CREATIVE-TEST]] · `workflow/WF-CREATIVE-TEST.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2 + §4c`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.4.3)
