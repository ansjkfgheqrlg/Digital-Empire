---
Type: WORKFLOW
Status: Active
Tags: #workflow #copywriting #ads #varianti #veloce #L2.1
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COPY-AD — Workflow Copy Ads (3+ Varianti)

> **Ecosistema:** 04-MARKETING · **Reparto:** L2.1 Copywriting · **Durata target:** 15-20 min
> **Gate di uscita:** score A8 ≥80 su ogni variante + G3 compliance

---

## Scopo

Produce 3+ varianti di copy APSOC per ads (Meta, Google, LinkedIn, TikTok) in modo veloce.
Ogni variante ha una struttura APSOC condensata — non la versione estesa del WF-COPY-FULL.
Il formato ads richiede copy breve (headline 25-30 char, testo 125-150 char per Meta) ma
con la stessa struttura logica APSOC interna. L2.2 Advertising usa questo workflow come
input per le campagne.

---

## Passi del workflow

### Step 1 — Contratto in ingresso (COPY-MASTER)
**Agente:** COPY-MASTER
**Input:** contratto con `formato: "ad"`, piattaforma dichiarata (Meta/Google/LinkedIn/TikTok), ICP
**Azione:**
- Verifica ICP in namespace; se assente e materiali disponibili → A2 fast (solo pain map, senza avatar completo).
- Applica T-AWARENESS-ROUTER per il dosaggio condensato.
- Attiva il workflow ads.
**Output:** contratto validato + piattaforma + dosaggio

### Step 2 — Briefing rapido (A1)
**Agente:** A1 Briefing Analyst
**Input:** contratto + materiali
**Azione:** briefing condensato (5 elementi: prodotto, ICP, pain primario, obiettivo, vincoli piattaforma)
**Nota:** no briefing completo — solo briefing-ads.md (più leggero, ottimizzato per velocità)
**Output:** `briefing-ads.md`

### Step 3 — Produzione 3+ varianti (A3-A7 in sessione condensata)
**Agente:** COPY-MASTER coordina A3-A4-A5-A6-A7 in sessione unica
**Azione:**
- A3: 3 headline per 3 strategie diverse (specchio, curiosity gap, promessa risultato)
- A4: pain condensato (1-2 frasi, non la versione lunga) per ogni variante
- A5: benefit condensato + proof (1 dato o 1 testimonianza breve) per ogni variante
- A6: 1 obiezione per variante (la più critica per la piattaforma/ICP)
- A7: CTA micro-commitment per ogni variante
**Output:** `ads-variants.md` con 3+ varianti complete

### Step 4 — Gate G1 (A8 su ogni variante)
**Agente:** A8 Copy Reviewer
**Input:** ads-variants.md + briefing-ads.md
**Azione:** scoring APSOC condensato per ogni variante; applica violazioni automatiche
**Gate G1:** ≥80 su ogni variante → PASS | < 80 su una → COPY-QA-LEAD
**Output:** `qa-report-ads.md` con score per variante

### Step 5 — Gate G3 compliance (AD4, L2.2)
**Agente:** AD4 Ad Compliance Checker (L2.2 Advertising)
**Input:** ads gated G1 + piattaforma dichiarata
**Azione:** verifica policy Meta/Google/LinkedIn/TikTok: claim proibiti, formati, limiti caratteri
**Gate G3:** PASS → rilascio a L2.2 | FAIL → indica la variante non conforme
**Output:** `compliance-report.md`

---

## Gate di uscita

| Gate | Responsabile | Soglia | Bloccante |
|---|---|---|---|
| G1 Score APSOC | A8 | ≥80 ogni variante | SI |
| G3 Ad Compliance | AD4 (L2.2) | PASS per piattaforma | SI |

---

## Input / Output del workflow

**Input:**
```json
{
  "committente": "L2.2-Advertising | 02-INFO | ...",
  "formato": "ad",
  "piattaforma": "Meta | Google | LinkedIn | TikTok",
  "awareness_level": "...",
  "icp": "...",
  "obiettivo": "click | lead | acquisto",
  "vincoli": "max 125 char corpo, max 30 char headline"
}
```

**Output:**
```json
{
  "varianti": 3,
  "ads_gated_path": "path/al/ads-variants-gated.md",
  "score_per_variante": [82, 80, 85],
  "compliance": "PASS",
  "workflow": "WF-COPY-AD",
  "time_to_output": "[DM] min"
}
```

---

## Connessioni

- [[WF-ADS-CAMPAIGN]] · `company/Ecosistemi/04-MARKETING/Reparti/L2-2-Advertising/workflow/WF-ADS-CAMPAIGN.md` — usa questo WF come input copy
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[copy-master]] · `agenti/copy-master.md`
- [[WF-COPY-FULL]] · `workflow/WF-COPY-FULL.md` — versione estesa per formati complessi
