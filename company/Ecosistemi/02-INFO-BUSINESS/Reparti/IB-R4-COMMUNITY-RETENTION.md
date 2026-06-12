> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.4 (Reparti L2)

# IB-R4-COMMUNITY-RETENTION — Reparto Community & Retention

> Reparto L2 · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

**Il prodotto inizia dopo l'acquisto.** Onboarding studenti, community attiva
(WhatsApp/Discord), completamento corsi, raccolta testimonianze, referral e
identificazione lead caldi per cross-sell ad AGENCY. Ogni acquirente deve essere
attivato entro 24h e completare il modulo 1 entro 7 giorni.

---

## Workflow L3

| Workflow | Descrizione |
|---|---|
| `WF-ONBOARDING-STUDENTE` | Acquisto → accesso ≤24h → primo modulo completato ≤7gg |
| `WF-COMMUNITY` | Programmazione contenuti community, moderazione, rituali settimanali |

---

## Team L4 (Funzioni)

| Team | Responsabilità |
|---|---|
| `T-onboarding` | Sequenza benvenuto + attivazione (skill `onboarding`, `signup`) |
| `T-retention` | Segnali di abbandono, win-back (skill `churn-prevention`) |
| `T-social-proof` | Raccolta testimonianze/case study a milestone di completamento |
| `T-crosssell` | Scoring segnali "vuole l'implementazione fatta" → handoff AGENCY (skill `referrals`) |

---

## Agenti L5 (roster)

`ib-community-coordinator`, `ib-onboarder`, `ib-engagement-runner`,
`ib-testimonial-harvester`, `ib-crosssell-scout`

---

## Handoff cross-sell verso AGENCY

Gate rigoroso (Mandato Empire — anti-invadenza):
- Solo lead con segnale esplicito (domande in community, completamento moduli avanzati, richiesta diretta)
- Lead consenziente (mai outreach automatico sugli studenti)
- Payload handoff: `{lead, fonte_prodotto, segnale, score}`

---

## KPI

| KPI | Definizione |
|---|---|
| Attivazione | % acquirenti che completano modulo 1 entro 7gg |
| Completamento | % studenti che finiscono il corso |
| Cross-sell | N. lead qualificati passati ad AGENCY per coorte |

---

## Quality Gate

**Gate handoff cross-sell:** lead consenziente + segnale documentato + score.
Fallimento: blocco invio ad AGENCY, segnalazione a `ib-community-coordinator`.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS]] sez. 2.4 + 4b (post-lancio onboarding)
- [[01-ECOSISTEMA-AGENCY]] — destinatario lead caldi cross-sell
- [[IB-R2-LANCI]] — fornisce la coorte studenti post-cart close
- [[04-ECOSISTEMA-MARKETING]] — template email win-back e nurture post-acquisto
