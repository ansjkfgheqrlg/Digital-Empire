---
Type: CONCEPT
Status: Active
Tags: #workflow #vendite #funnel #salespage #apsoc #IB-L2-VEND
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-SALESPAGE — Sales Page Canonica per Prodotto

> **Workflow:** WF-SALESPAGE · **Reparto:** IB-L2-VEND Vendite & Funnel
> **Trigger:** brief prodotto validato + richiesta sales page (lancio o evergreen)
> **Output:** sales page live + tracking attivo in `infobusiness/vendite/salespage/{prodotto_id}/`
> **Gate di uscita:** IB-VEND-QA G-VEND PASS + tracking debug verde + checkout testato

---

## Scopo

Costruire LA sales page canonica per ogni prodotto — da brief a pagina live — con gate APSOC e
verifica "prove non promesse". Gli asset esistenti in `Lancio corso skill beast/` (Leanding Page
CCM, Page, Sale pag, smerd) vengono CONSOLIDATI in una sola pagina canonica per prodotto;
i duplicati sono archiviati, non cancellati (ADR-003). Una pagina per prodotto, una fonte di verità.

---

## Trigger

```json
{
  "evento": "richiesta_sales_page",
  "prodotto_id": "manuale-claude-code | vendi-la-skill | ...",
  "contesto": "lancio | evergreen",
  "prezzi_approvati_B003": "true | false",
  "deadline": "YYYY-MM-DD"
}
```

---

## Input JSON

```json
{
  "prodotto_id": "...",
  "prodotto_brief": {"cosa_e": "...", "outcome": "...", "icp": "..."},
  "prezzi": {"stato": "approvato | pending", "fonte": "B-003"},
  "brand_kit_id": "DE | ...",
  "direction_apsoc": "da 04-MARKETING (angolo, pain, proof disponibili)",
  "asset_esistenti": ["Lancio corso skill beast/Leanding Page CCM", "Page", "Sale pag"]
}
```

---

## Pipeline (step + owner)

```
[1] IB-VEND-OFFER — offer stack
  → value stack + bonus + garanzia + order bump + upsell + naming
  GATE: prezzi da catalogo approvato B-003; nessun numero placeholder in produzione
  → output: offer_stack.json

[2] IB-VEND-SALESPAGE — copy APSOC (skill cro-copy-architect)
  → attenzione → problema → agitazione → soluzione → proof → offerta → CTA
  → consolida gli asset esistenti in UNA pagina canonica (duplicati → archivio)
  → output: copy_apsoc.md + build_brief (empire-premium-style)

[3] IB-VEND-QA — gate G-VEND (bloccante)
  → APSOC ≥80/100 + "prove non promesse" (ogni claim ha documentazione) + no prezzo placeholder
  → se FAIL: feedback granulare → ritorno step 2
  → se PASS: autorizza handoff

[4] 06-PLATFORM (handoff HC-PL-IB-01) — build + deploy
  → build con empire-premium-style + collega checkout (IB-VEND-CHECKOUT)
  GATE: pagina ≤5s, mobile responsive, ogni link funzionante, checkout collegato

[5] IB-VEND-TRACK — tracking
  → eventi pixel (view, add-to-cart, purchase) + UTM per ogni fonte traffico
  GATE: test eventi in debug mode VERDE prima del go live
```

---

## Gate

| Gate | Owner | Criteri |
|---|---|---|
| G-PREZZO | IB-VEND-OFFER | Prezzi da catalogo approvato B-003; zero placeholder in produzione |
| G-VEND | IB-VEND-QA | APSOC ≥80 + ogni claim documentato + no scarcity falsa + no prezzo placeholder |
| G-BUILD | 06-PLATFORM | Pagina ≤5s, mobile responsive, link ok, checkout collegato e testato |
| G-TRACK | IB-VEND-TRACK | Eventi (view/add-to-cart/purchase) verdi in debug + UTM su ogni fonte |

---

## Output JSON

```json
{
  "prodotto_id": "...",
  "sales_page": {"stato": "live", "url": "...", "versione": "1.0", "pagina_canonica": true},
  "asset_archiviati": ["Lancio corso skill beast/Page (duplicato)"],
  "gate": {"G-VEND": "pass", "G-BUILD": "pass", "G-TRACK": "green"},
  "tracking": {"copertura": "100%", "eventi": ["view", "add_to_cart", "purchase"]},
  "ready_per": "WF-LANCIO (T-14) | WF-FUNNEL-EVERGREEN"
}
```

---

## Handoff

| Direzione | A | Payload | Quando |
|---|---|---|---|
| → 06-PLATFORM | HC-PL-IB-01 | copy_approvato + offer_stack + eventi[] | dopo G-VEND PASS |
| ← team-prezzi B-003 | HC-B003-IB-VEND-01 | catalogo prezzi approvati | prima dello step 1 in produzione |
| → WF-LANCIO | IB-L2-LANCI | sales page live + tracking | a sales page live (contesto lancio) |
| → WF-FUNNEL-EVERGREEN | interno | sales page canonica | a sales page live (contesto evergreen) |

---

## Dry-run (esempio)

**Trigger:** richiesta sales page per "Vendi la Skill", contesto evergreen, prezzi approvati B-003.

1. IB-VEND-OFFER: value stack (corso + 3 bonus) + garanzia 30gg + order bump (template) +
   upsell (mentorship) → prezzi slottati da B-003. offer_stack.json scritto.
2. IB-VEND-SALESPAGE: copy APSOC — apre sul pain "so creare skill ma non le vendo", proof =
   2 casi documentati, CTA singola. Consolida `Sale pag` + `Page` in una pagina canonica.
   Self-check APSOC: 83.
3. IB-VEND-QA: G-VEND → trova 1 claim senza proof ("triplica i clienti") → FAIL → feedback →
   IB-VEND-SALESPAGE riformula su dato verificabile → secondo giro → PASS (APSOC 85).
4. PLATFORM: build empire-premium-style, checkout collegato, pagina 3.2s, mobile ok → G-BUILD PASS.
5. IB-VEND-TRACK: eventi configurati, debug verde, UTM per organic/email/ads → G-TRACK green.

**Esito:** sales page canonica live, tracking 100%, pronta per WF-FUNNEL-EVERGREEN. Duplicati archiviati.

---

## Connessioni

- [[ib-vend-offer]] · `agenti/ib-vend-offer.md`
- [[ib-vend-salespage]] · `agenti/ib-vend-salespage.md`
- [[ib-vend-qa]] · `agenti/ib-vend-qa.md`
- [[WF-FUNNEL-EVERGREEN]] · `workflow/WF-FUNNEL-EVERGREEN.md`
- [[ARCHITETTURA]] · `ARCHITETTURA.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2)
