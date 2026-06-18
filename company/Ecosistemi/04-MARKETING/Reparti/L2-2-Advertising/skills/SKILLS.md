---
Type: CONCEPT
Status: Active
Tags: #skills #advertising #marketing #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# SKILLS — L2.2 Advertising

> Mappa delle skill del reparto: skill proprie da forgiare + skill esistenti mappate.
> Standard: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §5.2 e §6`

---

## Skill proprie da forgiare (via 07-FORGE)

### `ads-compliance` — P2

**Reparto owner:** L2.2 Advertising
**Priorità:** P2 (dopo le P0 empire-brand-gate, copy-request-router, brand-strategy-gate)
**Agente owner:** AD4 Ad Compliance Checker

**Cosa fa:**
Pre-flight di compliance policy per campagne pubblicitarie su Meta, Google, LinkedIn, TikTok.
Riceve: copy, visual brief, categoria prodotto, piattaforme target.
Produce: checklist binaria per piattaforma, fail con elementi specifici + correzione richiesta.

**Checklist minima per piattaforma:**
- Meta: lunghezze copy (headline ≤27 car preview, testo ≤125 car preview), text overlay visual ≤20%, no before/after, no claim di guadagno garantito, no discriminazione demografica.
- Google: headline ≤30 car, descrizione ≤90 car, pricing deve corrispondere alla landing, no "click here" in headline, no superlative senza prova.
- LinkedIn: intro ≤150 car visibili, headline ≤70 car, no claim finanziari speculativi, testimonial verificabili.
- TikTok: first frame con hook visivo, audio-on best practice, no contenuto sensazionalistico esagerato.

**Regola di build:** prima di forgiare → contradiction-analyzer contro skill `ads` esistente.
`ads-compliance` implementa il check policy; `ads` implementa la strategia — non si sovrappongono.

**Path futuro:** `company/Ecosistemi/07-FORGE/skills/ads-compliance/`

---

## Skill esistenti mappate a questo reparto

| Skill | Gerarchia | Agente owner | Note |
|---|---|---|---|
| `ads` | Motore primario | ADS-LEAD / AD3 | Strategia campagna, targeting, bidding — entry point advertising |
| `ad-creative` | Motore primario | AD2 | Generazione varianti creative a scala; fan-out swarm |
| `market-ads` | Ausiliaria | AD2 / T-CREATIVE-BATCH | Ausiliaria per batch creative |

**Regola anti-contraddizione:** in caso di conflitto tra `ads` e `ad-creative`, vince il
workflow del reparto (WF-ADS-CAMPAIGN / WF-CREATIVE-TEST). Le skill esistenti sono invocabili
come componenti del workflow, non come alternative autonome al workflow.

---

## Skill trasversali usate dal reparto (non owned)

| Skill | Owner reparto | Uso in L2.2 |
|---|---|---|
| `ab-testing` | L2.4 Analytics | AN3 valida dimensione campione in WF-CREATIVE-TEST |
| `analytics` | L2.4 Analytics | AN2 traccia performance per copy_id in WF-ADS-PERFORMANCE |
| `empire-brand-gate` | LX / SEN-BV | AD-QA invoca per check brand_kit |
| `market-competitors` | L2.5 / 08-INTELLIGENCE | AD1 invoca per competitor audience brief |

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §5.2 e §6`
- [[ad4-compliance-checker]] · `agenti/ad4-compliance-checker.md`
- [[ad2-creative-iterator]] · `agenti/ad2-creative-iterator.md`
- [[REGOLE]] · `regole/REGOLE.md`
