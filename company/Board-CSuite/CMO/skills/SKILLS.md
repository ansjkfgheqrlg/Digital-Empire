---
Type: CONCEPT
Status: Active
Tags: #cmo #skills #brand-gate #campagna #icp #apsoc
Created: 2026-06-17
Last updated: 2026-06-17
---

# SKILLS — CMO (Chief Marketing Officer)

> Skill proprie del team CMO. Derivate dal Blueprint `BP-CMO.md`. Ogni skill è un gate
> o un orchestratore: eseguibile, deterministica dove possibile, con output strutturato.
> Stato build: da forgiare via FORGE nella fase appropriata.

---

## Skill 1 — `empire-brand-gate`

**Scopo:** Checklist eseguibile della voce Mandato + APSOC + anti-slop. Gate bloccante.

**Kernel:**
```
Input: testo + formato + brand_kit + icp + score_minimo
Output: { gate_pass: bool, score: int, blocchi: [], feedback_granulare: {} }
```

**Logica:**
1. CPB check: ogni claim ha proof? (bloccante se no)
2. Score APSOC per sezione (pesi A15+P20+S20+O15+C20+V10)
3. Penalità P-dopo-S (−15 automatico)
4. Brand Gate G2 checklist (7 item binari)
5. Verdetto: PASS se score ≥ soglia_formato AND CPB ok AND G2 completo

**Formati supportati:**
- `cold_email` / `dm` → soglia 80
- `ads` / `landing` / `newsletter_cta` → soglia 80
- `sales_page` / `proposta_commerciale` → soglia 85

**Riferimenti:** Mandato Art.4.2 + Framework APSOC (`second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`)
**Agente owner:** `cmo-brand-voice-warden`
**Status build:** da forgiare

---

## Skill 2 — `campaign-orchestrator`

**Scopo:** Orchestrazione campagna multi-canale end-to-end: da obiettivo a execution brief.

**Kernel:**
```
Input: obiettivo + icp_id + budget_envelope + canali_disponibili + deadline
Output: {
  strategia_id, canali: [{canale, awareness_target, struttura_apsoc, kpi}],
  brief_marketing: {...}, brief_content: {...},
  dry_run_budget: {scenario_base, scenario_ottimistico}
}
```

**Logica:**
1. ICP lookup via `cmo-memoria` (o flag [DM] se profilo mancante)
2. Mappa awareness → canali appropriati
3. Struttura APSOC per ogni canale (schema, non testo finale)
4. Dry-run budget per canali a costo variabile
5. Produzione brief per liaison (marketing + content)

**Agenti che la usano:** `cmo-campaign-strategist`, `cmo-conductor`
**Status build:** da forgiare

---

## Skill 3 — `icp-pattern-library`

**Scopo:** Libreria pattern ICP per nicchia — recupero e aggiornamento veloce.
Alta frequenza di query (usata da campaign-strategist, marketing-liaison, content-liaison).

**Kernel:**
```
Input (retrieve): nicchia + formato + awareness_level
Output: [{ pattern_id, testo_esemplare, apsoc_sezione_forte, metrica_conferma, data }]

Input (store): pattern completo con metrica di conferma
Output: { stored: bool, pattern_id: "PATT-..." }

Input (update): pattern_id + nuova metrica
Output: { updated: bool }
```

**Namespace:** `board/cmo/icp-patterns/` (AgentDB)
**Agenti che la usano:** `cmo-memoria`, `cmo-audience-intel`, `cmo-marketing-liaison`
**Regola:** pattern senza metrica di conferma reale = classificato "ipotetico" (non validato)
**Status build:** da forgiare

---

## Note di build per FORGE

- Le 3 skill hanno priorità in quest'ordine: `empire-brand-gate` (blocca la qualità),
  `campaign-orchestrator` (sblocca la produzione), `icp-pattern-library` (accelera iterazioni).
- `empire-brand-gate` riusa lo standard APSOC esistente del SEN-BV di 04-MARKETING:
  non reinventare, estendere e adattare alla scope holding-wide.
- Ogni skill ha un kernel deterministico (dove possibile) + una parte di reasoning (LLM)
  per i giudizi soggettivi (es. "questo è AI-slop?"). La parte deterministica non cambia tra run.

---

## Connessioni

- [[BP-CMO]] · `company/Board-CSuite/_BLUEPRINT/BP-CMO.md` — fonte skill
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[cmo-campaign-strategist]] · `agenti/cmo-campaign-strategist.md`
- [[cmo-memoria]] · `agenti/cmo-memoria.md`
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md` — usa `empire-brand-gate`
- [[Framework_Cold_Outreach_APSOC]] · `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`
- [[12-DOSSIER-MAXIMILIAN]] §4 — standard skill per gli organi C-Suite
