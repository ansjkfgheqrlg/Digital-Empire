---
Type: CONCEPT
Status: Active
Tags: #workflow #vendite #funnel #evergreen #lead-magnet #nurture #IB-L2-VEND
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-FUNNEL-EVERGREEN — Sistema di Vendita Continua 365 Giorni

> **Workflow:** WF-FUNNEL-EVERGREEN · **Reparto:** IB-L2-VEND Vendite & Funnel
> **Trigger:** offerta validata da un lancio (o decisione ib-director di aprire l'evergreen)
> **Output:** revenue continua + pipeline lead per AGENCY in `infobusiness/vendite/evergreen/{prodotto_id}/`
> **Gate di uscita:** IB-VEND-QA G-VEND PASS su ogni email + sales page; tracking 100% step

---

## Scopo

Costruire un sistema di vendita che gira 365 giorni senza dipendere dai lanci. Modello di riferimento:
`InfoBusiness/Funnel Unico Perfetto.pdf` (ingestito come blueprint). **Un lancio valida l'offerta;
il funnel evergreen la scala.** Catena: lead magnet → opt-in → sequenza nurture → sales page evergreen
→ checkout → tracking → loop CRO. Nessuna scarcity falsa (Art.2): l'evergreen vende per valore, non per
deadline finte.

---

## Trigger

```json
{
  "evento": "apri_evergreen",
  "prodotto_id": "...",
  "offerta_validata": "true (da lancio o decisione ib-director)",
  "lead_magnet_confermato_B003": "true | false"
}
```

---

## Input JSON

```json
{
  "prodotto_id": "...",
  "lead_magnet": {"tipo": "ebook | mini-corso", "asset": "Manuale Claude Code (se gratuito da B-003)"},
  "sales_page_canonica": "da WF-SALESPAGE (variante evergreen senza deadline finte)",
  "brand_kit_id": "DE | ...",
  "founder_authority_frame": "da 08-INTELLIGENCE (intelligence Beggiato)",
  "lista_email": {"provider": "...", "tag": "lead-{prodotto_id}"}
}
```

---

## Pipeline (step + owner)

```
[1] IB-VEND-LEAD — lead magnet + opt-in (skill lead-magnets)
  → opt-in page (APSOC + brand voice) → consegna automatica magnet → utente in lista email
  GATE: decisione asset gratuito confermata da B-003; promessa opt-in mantenuta dal magnet

[2] IB-VEND-SALESPAGE — sequenza nurture (skill emails)
  → 5-7 email, frame Founder Authority Stack: valore → autorità → offerta
  GATE IB-VEND-QA: ogni email APSOC verificata; nessuna email con più di 1 CTA

[3] IB-VEND-SALESPAGE — sales page evergreen
  → variante della page di lancio, SENZA deadline finte (Mandato Art.2)
  GATE: "permanente" = senza scarcity artificiale; bonus a scadenza solo se reale

[4] IB-VEND-CHECKOUT — checkout + order bump + upsell
  → prezzi da team-prezzi B-003; transazione reale testata
  GATE: checkout testato; handoff post-purchase a IB-L2-COMM attivo

[5] Acquirente → IB-L2-COMM (HC-IB-VEND-COMM-01)
  → WF-ONBOARDING-STUDENTE → community → cross-sell scout (lead caldi → AGENCY)

[6] Loop continuo — IB-VEND-TRACK + IB-VEND-CRO
  → TRACK misura ogni step (opt-in rate, open rate email, click sales page, conversione)
  → CRO propone 1 test A/B alla volta → risultato in ≥14 giorni → adozione o scarto
```

---

## Gate

| Gate | Owner | Criteri |
|---|---|---|
| G-LEAD | IB-VEND-QA | Opt-in onesto; promessa mantenuta dal magnet; asset confermato B-003 |
| G-NURTURE | IB-VEND-QA | Ogni email APSOC; max 1 CTA per email; frame autorità con asset verificabili |
| G-EVERGREEN | IB-VEND-QA | Nessuna deadline finta; scarcity solo se reale (Art.2) |
| G-CHECKOUT | IB-VEND-CHECKOUT | Transazione reale testata; prezzi approvati; handoff COMM attivo |
| G-TRACK | IB-VEND-TRACK | Copertura 100% step; eventi verdi |

---

## Output JSON

```json
{
  "prodotto_id": "...",
  "funnel_evergreen": {"stato": "live", "step_attivi": 6},
  "metriche_step": {
    "opt_in_rate": 0.30, "email_open_rate": 0.42, "salespage_ctr": 0.18,
    "conversione_evergreen": 0.017, "aov": 78, "revenue_per_lead": 4.10
  },
  "ab_test_in_corso": {"test_id": "...", "step_target": "checkout"},
  "pipeline_lead_agency": "attiva (cross-sell scout su acquirenti)"
}
```

---

## Handoff

| Direzione | A | Payload | Quando |
|---|---|---|---|
| ← team-prezzi B-003 | HC-B003-IB-VEND-01 | prezzo lead magnet + offerta | prima dello step 1 |
| ← 08-INTELLIGENCE | HC-INT-IB-VEND-01 | frame Founder Authority Stack | prima dello step 2 (nurture) |
| → IB-L2-COMM | HC-IB-VEND-COMM-01 | acquirente_id + prodotto_id + canale | all'acquisto (step 5) |
| → WF-CRO-OTTIMIZZAZIONE | interno | metriche_step settimanali | loop continuo (step 6) |

---

## Dry-run (esempio)

**Trigger:** apri evergreen per "Manuale Claude Code" — B-003 conferma: versione base = lead magnet
gratuito; corso completo = prodotto a pagamento.

1. IB-VEND-LEAD: opt-in page "Scarica le prime 40 pagine del Manuale Claude Code" → consegna
   automatica + tag lista. Promessa mantenuta (le 40 pagine sono reali). G-LEAD PASS.
2. IB-VEND-SALESPAGE: 6 email nurture — E1 valore (caso d'uso reale), E2-3 autorità (Founder
   Authority Stack), E4-6 offerta. Una CTA per email. IB-VEND-QA: G-NURTURE PASS.
3. Sales page evergreen: variante senza countdown finto; bonus "sessione Q&A mensile" reale.
   IB-VEND-QA verifica assenza scarcity falsa. G-EVERGREEN PASS.
4. IB-VEND-CHECKOUT: checkout + order bump (toolkit prompt) + upsell (mentorship), prezzi B-003,
   transazione test ok. G-CHECKOUT PASS. Handoff post-purchase attivo.
5. Primo acquirente → HC-IB-VEND-COMM-01 → IB-L2-COMM avvia onboarding.
6. Settimana 1: IB-VEND-TRACK rileva opt-in 30%, checkout 4% (collo di bottiglia) →
   IB-VEND-CRO apre 1 test sul blocco prezzo+garanzia → 14gg → decisione.

**Esito:** funnel evergreen live, tracking 100%, primo loop CRO avviato, pipeline lead per AGENCY attiva.

---

## Connessioni

- [[ib-vend-lead]] · `agenti/ib-vend-lead.md`
- [[ib-vend-salespage]] · `agenti/ib-vend-salespage.md`
- [[ib-vend-checkout]] · `agenti/ib-vend-checkout.md`
- [[WF-SALESPAGE]] · `workflow/WF-SALESPAGE.md`
- [[WF-CRO-OTTIMIZZAZIONE]] · `workflow/WF-CRO-OTTIMIZZAZIONE.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — no scarcity falsa)
