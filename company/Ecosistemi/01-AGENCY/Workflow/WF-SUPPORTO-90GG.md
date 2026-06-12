> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A4 + sez. 4 (step 8) + sez. 8 (KPI A4)

# WF-SUPPORTO-90GG — Supporto Post-Delivery 90 giorni

> Workflow L3 di A4-DELIVERY · Topologia: `star` · Durata: 90 giorni da Gate Delivery firmato
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A4 + §4

## Cosa è

Supporto strutturato per i 90 giorni successivi al Gate Delivery: intake ticket → triage →
fix → log. Include check proattivi settimanali e chiusura formale a 90gg con review.
Obiettivo: rendere il cliente progressivamente autonomo (ticket decrescenti nel tempo).

## Flusso

### Gestione ticket (continuo, su evento)

```
EVENTO: cliente invia ticket (email / canale dedicato)
[T-support-triage] classifica:
  - BUG: problema nel codice/workflow consegnato → priorità alta, fix entro SLA
  - DOMANDA: il cliente non sa come fare qualcosa → risposta + aggiornamento runbook
  - FUORI SCOPE: richiesta non nel contratto → risposta standard + eventuale proposta estensione
        ↓
[AGente competente] fix / risposta
        ↓
LOG: ogni ticket loggato in agency/delivery/{client_id} con {tipo, data, risoluzione, SLA_rispettato}
```

### Check proattivo settimanale (schedulato da 09 OPERATIONS)

```
CHECK: il sistema del cliente sta girando?
  - Verifica remota log (se il cliente li condivide) o richiesta status
  - Report status: "tutto ok" / "anomalia rilevata" / "token scaduto" / "volume in calo"
  → PASS: log + nessuna azione
  → ANOMALIA: apertura ticket proattivo + fix coordinato con cliente
```

### Chiusura 90gg

```
T+90: A4-COORD apre chiusura formale:
  [T-support-triage] report completo: n. ticket, tipi, SLA, problemi ricorrenti
  [T-training-kit] verifica che il cliente abbia ancora tutti i materiali aggiornati
  → segnale ad A6: "ready per testimonianza e upsell mapping"
  → pattern in agency/reasoning se ci sono stati problemi ricorrenti
  → chiusura account nel namespace agency/delivery
```

## I/O

| | Dettaglio |
|---|---|
| **Input** | ticket cliente, schedule check settimanali da 09 OPS, segnale chiusura a T+90 |
| **Output** | ticket risolti; report settimanale; report chiusura; segnale ad A6 per testimonianza |

## Classificazione ticket (T-support-triage)

| Tipo | Definizione | SLA | Risposta tipo |
|---|---|---|---|
| BUG | Il sistema non funziona come in UAT | 24h lavorative | Fix + verifica + log |
| DOMANDA | Il cliente non ricorda / non sa fare | 48h lavorative | Risposta + aggiornamento runbook/FAQ |
| FUORI SCOPE | Richiesta di funzionalità non nel contratto | Nessun SLA | Risposta standard + proposta commerciale separata |

## Regole operative

- Il ticket viene SOLO loggato e risolto — mai usato per upsell durante i 90gg (viola il brand gate)
- `T-support-triage` riceve SEMPRE il ticket (no bypass umano diretto al fix)
- Ticket ricorrente sullo stesso problema → root cause analysis → aggiornamento runbook
- Il supporto ha obiettivo di ticket DECRESCENTI: se crescono → sistema non abbastanza chiaro → training integrato

## Failure

| Evento | Risposta |
|---|---|
| SLA non rispettato | alert a AG-A4-COORD; escalation a Max se oltre 48h senza risposta |
| Bug non risolvibile in 24h | comunicazione proattiva a cliente con stima; se oltre 72h → Max coinvolto |
| Cliente non raggiungibile per check | log "unreachable" + riprogrammazione; dopo 3 tentativi → chiusura proattiva documentata |

## KPI

| KPI | Definizione |
|---|---|
| Ticket risolti in SLA | % ticket risolti entro i tempi previsti per tipo |
| Ticket per settimana | andamento: deve essere decrescente |
| NPS fine 90gg | rilevato da T-proof-collector di A6 al momento della chiusura |

## Connessioni

- [`../Reparti/A4-Delivery/`](../Reparti/A4-Delivery/) — reparto owner
- [`./WF-DELIVERY-OUTREACH-FACTORY.md`](./WF-DELIVERY-OUTREACH-FACTORY.md) — precede questo workflow
- [`../Funzioni/T-support-triage/`](../Funzioni/T-support-triage/)
- [`../Reparti/A6-Marketing-Interno/`](../Reparti/A6-Marketing-Interno/) (cliente: segnale chiusura → testimonianza)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
