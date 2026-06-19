---
Type: WORKFLOW
Status: Active
Tags: #workflow #copywriting #sales-page #high-ticket #apsoc #L2.1
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COPY-SALES-PAGE — Workflow Sales Page Completa

> **Ecosistema:** 04-MARKETING · **Reparto:** L2.1 Copywriting · **Durata target:** 90-120 min
> **Gate di uscita:** score A8 ≥85 + P prima di S verificato + G2 brand gate + G4 contract

---

## Scopo

Produce una sales page completa con anatomia dettagliata APSOC, gate ≥85 (più alto del
standard), e verifica obbligatoria P prima di S. La sales page è il formato più critico
del reparto — una conversione anche di pochi punti percentuali su un prodotto high-ticket
vale migliaia di euro. Il gate ≥85 riflette questa criticità. Usato principalmente da
02-INFO-BUSINESS per lanci corsi e da 01-AGENCY per landing offerte.

---

## Anatomia della sales page (sezioni obbligatorie)

1. **Hero section** — headline principale (A3) + subheadline + hook visivo (brief per 03-CF)
2. **Problema amplificato** — sezione P completa a 3 livelli (A4); ZERO prodotto
3. **Agitazione** — conseguenze della non-azione (A4 integrato)
4. **Soluzione** — USP + benefit + proof (A5); SEMPRE dopo P (Art.4.2)
5. **Proof section** — testimonianze, dati, case study (A5 integrato)
6. **CTA intermedia** — prima CTA mid-page (A7)
7. **Obiezioni** — 3-4 CPB per le obiezioni critiche (A6)
8. **Garanzia** — se disponibile, integrata dopo O
9. **CTA finale** — chiusura con urgenza reale + passo specifico (A7)
10. **FAQ** — gestione obiezioni minori non nel corpo principale

---

## Passi del workflow

### Step 1 — Contratto (COPY-MASTER)
**Agente:** COPY-MASTER
**Input:** contratto con `formato: "sales-page"`, prodotto, awareness_level, ICP, proof disponibili
**Azione:** verifica ICP + proof; se proof insufficienti → segnala al committente prima di procedere;
applica T-AWARENESS-ROUTER; soglia dichiarata: 85
**Output:** contratto validato, soglia_gate=85 dichiarata

### Step 2 — Avatar esteso (A2)
**Agente:** A2 Target Analyst
**Input:** ICP + tutti i materiali disponibili (incl. testimonianze, call recordings)
**Azione:** avatar esteso + pain map a 3 livelli + language map dettagliata;
per sales page si richiede un avatar più ricco del briefing standard
**Output:** avatar path + pain_map + language_map aggiornati in namespace

### Step 3 — Briefing completo (A1)
**Agente:** A1 Briefing Analyst
**Input:** contratto + avatar + proof (testimonianze, dati, case study verificati)
**Azione:** briefing-completo.md + mappatura proof per sezione (quale proof va in S, quale in O, quale in FAQ)
**Gate:** `pronto_per_scrittura: true` + almeno 3 proof disponibili verificate
**Output:** `briefing-completo.md` + `proof-map.md`

### Step 4 — Hero + Attenzione (A3)
**Agente:** A3 Attention Writer
**Input:** briefing + language map
**Azione:** ≥3 headline alternative + subheadline + hook; per sales page la headline deve reggere
senza il resto della pagina (test di stand-alone)
**Output:** `attention-section.md` con note per brief design hero (→ 03-CF)

### Step 5 — Problema + Agitazione (A4)
**Agente:** A4 Problem Writer
**Input:** briefing + pain map + language map
**Azione:** problema a 3 livelli + agitazione (conseguenze della non-azione nel tempo);
lunghezza P estesa per sales page; ZERO prodotto; ZERO soluzione
**Gate interno:** `menzione_prodotto: false` — BLOCCA se non rispettato
**Output:** `problem-section.md`

### Step 6 — Soluzione + Proof (A5)
**Agente:** A5 Solution Writer
**PREREQUISITO:** Step 5 completato con `menzione_prodotto: false`
**Input:** problem-section.md (verificata) + briefing + proof-map.md
**Azione:** USP + benefit per ogni pain di P + proof integrate per sezione + visione post-acquisto
**Output:** `solution-section.md` + `proof-section.md`

### Step 7 — Obiezioni (A6)
**Agente:** A6 Objections Handler
**Input:** briefing + pain map + proof-map.md
**Azione:** 3-4 obiezioni critiche con CPB; per sales page: obiezione prezzo SEMPRE inclusa
**Output:** `objections-section.md`

### Step 8 — CTA doppia (A7)
**Agente:** A7 CTA Writer
**Input:** briefing + obiettivo azione + urgenza reale
**Azione:** CTA mid-page (step 6 della pagina) + CTA finale (step 9); due versioni distinte
**Output:** `cta-section.md` con `cta_midpage` e `cta_finale`

### Step 9 — Assemblaggio + Gate G1 (A8)
**Agente:** A8 Copy Reviewer
**Input:** copy assemblato con anatomia completa
**Azione:** scoring APSOC 100pt + check P prima di S + check violazioni + check anatomia completa
**Gate G1:** ≥85 → PASS | < 85 → COPY-QA-LEAD
**Output:** `qa-report.md`

### Step 10 — Supervisione gate (COPY-QA-LEAD, se FAIL)
**Agente:** COPY-QA-LEAD
**Input:** report FAIL A8
**Azione:** fix mirato vs rifacimento; per sales page soglia ≥85 le tolleranze sono minori
**Gate:** max 2 iterazioni prima di escalation strutturale

### Step 11 — Gate G2 + G4
**Agente:** BR-QA (G2) + COPY-MASTER (G4)
**Input:** copy gated G1
**Azione:** G2 brand check + G4 vincoli contratto
**Output:** copy finale gated

---

## Gate di uscita

| Gate | Responsabile | Soglia | Bloccante |
|---|---|---|---|
| G1 Score APSOC | A8 | ≥85 | SI — più alto del standard |
| P prima di S | A8 (automatico) | violazione = -15pt | SI |
| G2 Brand | BR-QA (L2.5) | PASS | SI |
| G4 Contract | COPY-MASTER | PASS | SI |

---

## Connessioni

- [[WF-COPY-FULL]] · `workflow/WF-COPY-FULL.md` — pipeline base da cui deriva
- [[a4-problem-writer]] · `agenti/a4-problem-writer.md` — regola P senza prodotto
- [[a5-solution-writer]] · `agenti/a5-solution-writer.md` — prerequisito P completata
- [[copy-qa-lead]] · `agenti/copy-qa-lead.md` — supervisore gate ≥85
