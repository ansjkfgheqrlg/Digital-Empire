# BACKBONE — A6 MARKETING INTERNO

> Reparto L2 di 01-AGENCY. Schema canonico: coordinator, I/O, acceptance_criteria, failure_handling, shared_state.

## Coordinator

**AG-A6-COORD** (sonnet) — orchestratore reparto.
Responsabilita': vetrina e prova sociale dell'agency.
Genera inbound e munizioni per outreach e preventivi.

## Team L3 / L4

| ID | Livello | Tipo | Flusso |
|---|---|---|---|
| WF-ASSET-VETRINA | L3 | workflow | manutenzione agency-empire-landing + presentazione-empire.vercel.app (build via 06-PLATFORM) |
| WF-CASE-STUDY | L3 | workflow | delivery chiusa -> raccolta testimonianza -> case study APSOC -> asset via 03-CF -> pubblicazione |
| T-proof-collector | L4 | worker (haiku) | raccolta testimonianze/metriche reali a fine 90gg |
| T-case-writer | L4 | worker (sonnet) | scrittura case study (skill cro-copy-architect) |
| T-upsell-mapper | L4 | worker (sonnet) | mappa cliente -> prossima offerta (skill upsell-mapper) |

## I/O

**Input:**
- Delivery completata + metriche reali da A4 via `HC-A4-A6-testimonianza`
  Payload: client_id, metriche_reali, uat_firmata

**Output:**
- Case study pubblicato su landing/blog
- Asset social da 03-CONTENT-FACTORY (via HC-AG-CF-01)
- Proposta upsell (singolo -> Engine Room EUR 8.000; cliente -> referral)

## Acceptance Criteria

- "Prove non promesse": solo metriche REALI del cliente (verificate dal cliente in UAT)
- Upsell attivo SOLO dopo Gate Delivery PASS + segnale positivo a fine 90gg
- Mai upsell durante il periodo di supporto attivo
- Case study = APSOC applicato (problema -> soluzione -> risultati reali)

## Failure Handling

| Failure | Azione |
|---|---|
| Cliente non da' testimonianza | T-proof-collector segue con follow-up soft; max 2 tentativi; log |
| Metriche non verificabili | Non pubblicare; log come "prova assente" in agency/reasoning |
| Landing non funzionante | Ticket urgente a 06-PLATFORM via HC-AG-PL-01 |

## Asset esistenti

| Path | Team |
|---|---|
| `agency-empire-landing/` | WF-ASSET-VETRINA |
| `presentazione-empire.vercel.app` | WF-ASSET-VETRINA (CTA standard) |
| Skill `cro-copy-architect` (APSOC) | T-case-writer |

## Connessioni

- `A4-DELIVERY/BACKBONE.md` — delivery completata in ingresso
- `company/Backbone/Bus/contracts/` — HC-A4-A6-testimonianza.json, HC-AG-CF-01
- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` sez. 2 (A6)
