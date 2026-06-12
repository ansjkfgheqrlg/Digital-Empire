> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.2 (Team L4) + sez. 4b (WF-LANCIO T-14/T-7)

# T-COPY-LIAISON — Team Copy Liaison

> Funzione L4 · Reparto: IB-R2-LANCI · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Essere il **punto di contatto strutturato** tra il reparto Lanci e l'ecosistema MARKETING:
compone i handoff contract per richiedere copy (sales page, sequenze email lancio, ad copy),
verifica i rientri contro gli acceptance criteria (APSOC ≥80/100), e segnala i fallback
a `ib-lanci-coordinator` se il copy non supera il gate entro la deadline.

---

## Agente proprietario

`ib-copy-liaison` (worker, tier Haiku — funzione di coordinamento, non di scrittura)

---

## Formato handoff verso MARKETING (esempio)

```json
{
  "from": "infobusiness/lanci",
  "to": "marketing/copywriting",
  "payload": {
    "tipo": "sequenza_email_cart_open",
    "prodotto": "corso-skill-n1",
    "icp": "freelancer_ai_principiante",
    "offer_stack": "corso + bonus MKD + accesso community"
  },
  "acceptance_criteria": ["APSOC >= 80/100", "5 email", "1 CTA per email", "zero promesse di guadagno non provate"],
  "deadline": "T-7",
  "fallback": "escalation a ib-lanci-coordinator"
}
```

---

## Checklist verifica rientro

- [ ] Score A8 (Copy Reviewer) ≥ 80/100 allegato al rientro
- [ ] Brand gate Mandato Empire: PASS
- [ ] Numero di email/pezzi conforme al contratto
- [ ] Una sola CTA per email
- [ ] Zero claim non documentati

---

## Connessioni

- [[IB-R2-LANCI]] — reparto di appartenenza
- [[04-ECOSISTEMA-MARKETING]] — ecosistema destinatario dei handoff copy
- [[T-CALENDARIO]] — fornisce le deadline di invio/rientro copy
- [[T-ASSET-LANCIO]] — i copy verificati entrano nella checklist asset
