---
Type: SKILLS
Status: Active
Tags: #skills #vendite #funnel #cro #IB-L2-VEND
Created: 2026-06-21
Last updated: 2026-06-21
---

# Skill — IB-L2-VEND Vendite & Funnel

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.

---

## Skill proprie del reparto (da forgiare via 07-FORGE — standard V2)

### `funnel-gate` — Priorità P1

**Funzione:** gate G-VEND deterministico in uscita dal reparto. Verifica che il funnel sia
pronto per la produzione: percorso end-to-end percorribile, eventi di tracking al 100%,
checkout testato con transazione reale, copy APSOC ≥80, nessun prezzo non approvato, nessuna
scarcity artificiale. Formalizza la logica di IB-VEND-QA.

**Quando invocarla:** prima di ogni go live (sales page, opt-in, sequenza nurture) e a ogni
handoff in uscita verso 06-PLATFORM.

**Input:** `{prodotto_id, copy_apsoc_path, offer_stack.json, eventi_config.json, checkout_test_esito, apsoc_score}`
**Output:** `{gate: "PASS"|"FAIL", checks: {apsoc, prezzi_approvati, tracking_100, checkout_ok, no_scarcity}, feedback[]}`

**Dipendenze:** richiede catalogo prezzi B-003 approvato e tracking verificato in debug.
**PRD da produrre prima della build:** via 07-FORGE, `skill-contradiction-analyzer` contro
`cro` e `verification-quality` (gate generico) per evitare doppi standard.

---

### `evergreen-funnel-orchestrator` — Priorità P2

**Funzione:** orchestrazione del funnel evergreen end-to-end: lead magnet → opt-in → sequenza
nurture (frame Founder Authority Stack) → sales page evergreen → checkout, con loop CRO settimanale.
Formalizza la sequenza di WF-FUNNEL-EVERGREEN coordinando le skill ausiliarie.

**Quando invocarla:** quando un'offerta è stata validata da un lancio (o ib-director decide di
aprire l'evergreen) e va trasformata in vendita continua 365 giorni.

**Input:** `{prodotto_id, offer_stack_validato, frame_autorita (08-INT), lista_email_target}`
**Output:** funnel evergreen configurato (opt-in + nurture 5-7 email + sales page + checkout) +
schema metriche per step pronto per IB-VEND-TRACK.

**Dipendenze:** richiede offer stack validato e frame autorità da 08-INTELLIGENCE.
**PRD da produrre prima della build:** via 07-FORGE, `skill-contradiction-analyzer` contro
`market-funnel`, `emails`, `lead-magnets` (skill ausiliarie mappate qui).

---

## Skill esistenti mappate a IB-L2-VEND

| Skill | Stato | Ruolo in IB-L2-VEND | Note |
|---|---|---|---|
| `cro-copy-architect` | Esistente, mappata | Copy APSOC sales page + email + CTA (IB-VEND-SALESPAGE) | Assembla/adatta; la direction brand resta a 04-MARKETING |
| `empire-premium-style` | Esistente, mappata | Build pagina premium → handoff 06-PLATFORM | L'esecuzione build/deploy è di PLATFORM, non del reparto |
| `lead-magnets` | Esistente, mappata | Opt-in page + lead magnet (IB-VEND-LEAD) | Ausiliaria di `evergreen-funnel-orchestrator` |
| `ab-testing` · `cro` | Esistente, mappata | Disegno ed esecuzione test funnel (IB-VEND-CRO) | 1 test alla volta; no conclusione sotto campione minimo |
| `analytics` | Esistente, mappata | Eventi, UTM, attribution, report per step (IB-VEND-TRACK) | Owner misurazione; alimenta CRO e debrief lancio |
| `paywalls` | Esistente, mappata | Order bump, upsell, upgrade path (IB-VEND-OFFER/CHECKOUT) | Ausiliaria; i prezzi restano da B-003 |
| `emails` | Esistente, mappata | Sequenza nurture 5-7 email; max 1 CTA per email | Owner copy a 04-MARKETING; gate APSOC di IB-VEND-QA |

---

## Regola anti-contraddizione

Prima di forgiare `funnel-gate` e `evergreen-funnel-orchestrator`:
1. Eseguire `skill-contradiction-analyzer` contro `cro`, `market-funnel`, `emails`, `lead-magnets`, `verification-quality`.
2. Se sovrapposizione rilevata: la skill nuova IMPLEMENTA/ESTENDE quella esistente, non la ridefinisce.
3. Gerarchia: skill nuova = motore/gate; skill esistente = ausiliaria o knowledge base.
4. Vincolo trasversale: nessuna skill del reparto inventa o pubblica prezzi (B-002/B-003).

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-VEND — skill area
- [[WF-FUNNEL-EVERGREEN]] · `workflow/WF-FUNNEL-EVERGREEN.md` — usa `evergreen-funnel-orchestrator`
- [[WF-SALESPAGE]] · `workflow/WF-SALESPAGE.md` — usa `funnel-gate` in uscita
- [[ib-vend-qa]] · `agenti/ib-vend-qa.md` — esecutore di `funnel-gate`
