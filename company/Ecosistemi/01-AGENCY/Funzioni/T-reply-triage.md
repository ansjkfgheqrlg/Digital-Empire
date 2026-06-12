> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A2 + sez. 6 (skill outreach-reply-triage)

# T-REPLY-TRIAGE — Triage Risposte Outreach

> Funzione L4 di A2-ACQUISIZIONE · Worker · Agente: `AG-A2-TRIAGE-W` (haiku)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2

## Cosa fa

Classifica ogni risposta in ingresso in 4 categorie e determina la prossima azione.
Skill: `outreach-reply-triage` (è anche **prodotto** — versione parametrizzata consegnata ai
clienti Outreach Factory come parte del handover, pattern #11).

## 4 categorie di triage

| Categoria | Segnali | Prossima azione |
|---|---|---|
| INTERESSATO | "mi interessa", "dimmi di più", "quando possiamo parlare?" | → conversation_manager → booking call |
| OBIEZIONE | "troppo costoso", "lo facciamo già", "non è il momento" | → T-FOLLOWUP con risposta specifica dalla libreria obiezioni |
| NO | "non siamo interessati", "rimuovi dalla lista", risposta negativa netta | → stop definitivo, tag "do-not-contact" in leads.db |
| OUT-OF-OFFICE | risposta automatica assenza | → follow-up riprogrammato alla data di rientro indicata |

## Regole assolute

- **MAI rispondere a un "NO" categorico** — è una regola del dossier, non una linea guida
- "Rimuovi dalla lista" → eliminazione immediata da `leads.db` (GDPR compliance)
- Classificazione dubbia → flag per revisione umana da AG-A2-COORD (non si indovina)
- PII-scan prima di ogni store in `agency/conversations` (`aidefence_has_pii`)

## Output per categoria

```json
{
  "lead_email": "...",
  "risposta_raw": "...",
  "categoria": "INTERESSATO",
  "prossima_azione": "conversation_manager",
  "urgenza": "alta",
  "flag_umano": false
}
```

## Multi-tenancy

La versione prodotto (consegnata ai clienti Outreach Factory) è parametrizzata con il
`brand_kit` del cliente: le 4 categorie e le regole sono identiche, ma i template di risposta
usano il tono e la firma del cliente (non DE). Pattern #11: zero hardcoding.

## Failure

| Evento | Risposta |
|---|---|
| Risposta ambigua / ironica | flag `umano=true`; AG-A2-COORD decide la categoria |
| Spike risposte negative (NO > X%) | alert + pattern in agency/reasoning; possibile problema con il template |
| Reply monitor non funzionante | alert a 09 OPS; le risposte si accumulano ma non si perdono (inbox) |

## Connessioni

- [`./T-sender.md`](./T-sender.md) (upstream: genera i messaggi ricevono risposta) · [`./T-followup.md`](./T-followup.md) (downstream: OBIEZIONE)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
