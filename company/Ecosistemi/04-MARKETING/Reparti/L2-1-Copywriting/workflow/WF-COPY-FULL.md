---
Type: WORKFLOW
Status: Active
Tags: #workflow #copywriting #full #apsoc #pipeline #L2.1
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COPY-FULL — Pipeline Copy Completa

> **Ecosistema:** 04-MARKETING · **Reparto:** L2.1 Copywriting · **Durata target:** 60-120 min
> **Gate di uscita:** score A8 ≥80 + G2 brand gate + G4 contract check

---

## Scopo

Pipeline A1→A8 completa per copy complesso (sales page, proposta agency, VSL, landing high-ticket).
Questa è la pipeline più lunga del reparto — si usa quando il formato richiede tutte le sezioni
APSOC sviluppate in profondità e quando le proof disponibili richiedono integrazione multi-livello.
Per formati più semplici o veloci, usare WF-COPY-AD o WF-COPY-SOCIAL.

---

## Passi del workflow

### Step 1 — Contratto in ingresso (COPY-MASTER)
**Agente:** COPY-MASTER
**Input:** contratto `{committente, formato, awareness_level, icp, obiettivo, deadline}`
**Azione:**
- Validazione campi obbligatori.
- Se ICP mancante → spawna A2 PRIMA di procedere (Step 1b).
- Deduce awareness_level se assente e lo dichiara nel payload.
- Applica T-AWARENESS-ROUTER → definisce dosaggio APSOC.
- Seleziona WF-COPY-FULL (questo workflow) e lo avvia.
**Output:** contratto validato + dosaggio APSOC dichiarato

### Step 1b — Avatar (A2, se ICP non in namespace)
**Agente:** A2 Target Analyst
**Input:** nicchia + materiali disponibili
**Azione:** costruisce avatar + pain map + language map → salva in `marketing/avatars/{icp}/`
**Output:** path avatar, pain primario, language map pronta per A1 e A4

### Step 2 — Briefing (A1)
**Agente:** A1 Briefing Analyst
**Input:** contratto validato + dosaggio APSOC + materiali del committente
**Azione:** struttura briefing-completo.md con: prodotto, ICP, awareness, dosaggio, obiettivo, proof, vincoli
**Gate:** `pronto_per_scrittura: true` (nessun gap bloccante)
**Output:** `briefing-completo.md`

### Step 3 — Attenzione (A3)
**Agente:** A3 Attention Writer
**Input:** briefing-completo.md + language map
**Azione:** produce ≥3 headline con strategia dichiarata + hook per ciascuna
**Output:** `attention-section.md` con varianti + variante consigliata

### Step 4 — Problema (A4)
**Agente:** A4 Problem Writer
**Input:** briefing-completo.md + pain map + language map
**Azione:** amplificazione dolore a 3 livelli (superficiale → profondo → identitario); ZERO menzione prodotto
**Gate interno:** `menzione_prodotto: false` — OBBLIGATORIO prima di procedere
**Output:** `problem-section.md`

### Step 5 — Soluzione (A5)
**Agente:** A5 Solution Writer
**Input:** problem-section.md (verificata) + briefing-completo.md + proof disponibili
**PREREQUISITO:** A4 completato con `menzione_prodotto: false` — BLOCCO se non rispettato (Art.4.2)
**Azione:** USP + benefit ancorati ai pain + visione post-acquisto + proof integrate
**Output:** `solution-section.md`

### Step 6 — Obiezioni (A6)
**Agente:** A6 Objections Handler
**Input:** briefing-completo.md + pain map + proof disponibili
**Azione:** seleziona 2-4 obiezioni prioritarie; CPB (Claim → Proof → Benefit) per ciascuna
**Output:** `objections-section.md`

### Step 7 — CTA (A7)
**Agente:** A7 CTA Writer
**Input:** briefing-completo.md + obiettivo azione + urgenza disponibile
**Azione:** CTA profonda + urgenza reale (no scarcity falsa — Art.2.3)
**Output:** `cta-section.md`

### Step 8 — Gate G1 (A8)
**Agente:** A8 Copy Reviewer
**Input:** copy assemblato (A+P+S+O+C) + briefing-completo.md
**Azione:** scoring APSOC 100pt + check violazioni automatiche
**Gate G1:** ≥80 standard → PASS | < 80 → FAIL
**Output:** `qa-report.md` con score per dimensione + verdetto

### Step 9 — Supervisione gate (COPY-QA-LEAD, se FAIL)
**Agente:** COPY-QA-LEAD
**Input:** report FAIL di A8
**Azione:** decide fix mirato vs rifacimento; indica agenti da re-iterare
**Gate:** max 2 iterazioni → se ancora FAIL, escalation a COPY-MASTER
**Output:** decisione iterazione + vincoli per ri-esecuzione

### Step 10 — Gate G2 brand (BR-QA, se richiesto)
**Agente:** BR-QA (Brand Consistency Verifier, L2.5)
**Input:** copy gated G1 + brand_kit_id
**Azione:** verifica coerenza copy vs brand_kit dichiarato e Mandato Art.2
**Gate G2:** PASS → procede | FAIL → ritorna a COPY-MASTER con gap brand
**Output:** `brand-gate-report.md`

### Step 11 — Gate G4 contract check (COPY-MASTER)
**Agente:** COPY-MASTER
**Input:** copy gated G1 + G2 + contratto originale
**Azione:** verifica che il copy rispetti i vincoli del contratto (lunghezza, piattaforma, policy)
**Gate G4:** PASS → rilascio | FAIL → re-iterazione specifica
**Output:** copy finale gated pronto per il committente

---

## Gate di uscita

| Gate | Responsabile | Soglia | Bloccante |
|---|---|---|---|
| G1 Score APSOC | A8 | ≥80 standard | SI — nessun rilascio sotto soglia |
| G2 Brand | BR-QA (L2.5) | PASS | SI — se brand_kit dichiarato |
| G4 Contract | COPY-MASTER | tutti i vincoli rispettati | SI |

---

## Input / Output del workflow

**Input:**
```json
{
  "committente": "01-AGENCY | 02-INFO | 03-CF | 05-MB | 04-MKT",
  "formato": "landing | proposta | vsl | ...",
  "awareness_level": "...",
  "icp": "...",
  "obiettivo": "...",
  "deadline": "YYYY-MM-DD"
}
```

**Output:**
```json
{
  "copy_finale": "path/al/copy-finale.md",
  "score_APSOC": 82,
  "qa_report": "path/qa-report.md",
  "brand_gate": "PASS",
  "workflow": "WF-COPY-FULL",
  "iterazioni": 1,
  "pattern_usati": ["..."]
}
```

---

## Connessioni

- [[copy-master]] · `agenti/copy-master.md`
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[copy-qa-lead]] · `agenti/copy-qa-lead.md`
- [[WF-COPY-SALES-PAGE]] · `workflow/WF-COPY-SALES-PAGE.md` — variante con gate ≥85
