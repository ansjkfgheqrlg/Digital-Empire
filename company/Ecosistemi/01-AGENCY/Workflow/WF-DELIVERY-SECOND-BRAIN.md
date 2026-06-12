> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A4 + sez. 1 (HC-IN-AG-01)

# WF-DELIVERY-SECOND-BRAIN — Delivery Second Brain €2.500

> Workflow L3 di A4-DELIVERY · SLA: ≤7 giorni da ambiente conforme · Dipende da: 08 INTELLIGENCE
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A4 + §1

## Cosa è

Delivery del prodotto **Second Brain €2.500**: knowledge base a grafo + memoria per LLM,
installata sul sistema del cliente. Il template viene richiesto a 08 INTELLIGENCE via
handoff `HC-IN-AG-01`. A4 configura il vault, le skill e la memoria contestuale per il cliente.

## Flusso

```
INPUT: contratto firmato + {dominio_business_cliente, fonti_conoscenza, strumenti_esistenti}

PRE-DELIVERY:
[HANDOFF VERSO 08 INTELLIGENCE — HC-IN-AG-01]
  payload: {template_second_brain, icp_nicchia_cliente, fonti_base}
  acceptance_criteria: template con struttura wiki + namespace memoria + skill base installabili

  → 08 INTELLIGENCE restituisce template configurato via handoff

GIORNO 1 — Verifica ambiente (T-env-setup):
  - Verifica tool disponibili: Obsidian / Notion / sistema di file cliente
  - Verifica accesso LLM client (Claude API key o accesso Claude Code)
  - Spazio storage e permessi
  *** Countdown 7gg parte da ambiente conforme ***

GIORNO 2-3 — Setup vault e struttura (T-config-tenant):
  - Deploy template wiki sul sistema cliente
  - Configurazione namespace memoria contestuale (prefisso univoco per cliente)
  - Importazione fonti iniziali del cliente (PDF, note, documenti interni)
  - Prima ingestione: content-forge su materiale raw cliente → MKD base

GIORNO 4-5 — Skill e memoria (T-config-tenant + T-uat-runner):
  - Installazione skill base DE (empire-context adattato per il cliente)
  - Test query memoria: il cliente pone domande al Second Brain e verifica le risposte
  - Cross-link tra le pagine wiki del cliente (almeno 3 connessioni per pagina)
  - Verifica che la memoria LLM risponda correttamente alle query di business del cliente

GIORNO 6 — Training (T-training-kit):
  - Video: come aggiungere nuove fonti, come interrogare il Second Brain, come aggiornare memoria
  - Runbook: manutenzione periodica (ingest settimanale, aggiornamento index)
  - FAQ specifiche per il dominio di business del cliente

GIORNO 7 — UAT e Handover (T-uat-runner + T-handover-pack):
  - Il cliente esegue da solo un ciclo: ingest documento → query → risposta
  - UAT firmata → Gate Delivery PASS
  - Handover pack: vault completo + skill configurate + README + licenza perpetua

OUTPUT: Second Brain live sul sistema cliente, cliente autonomo
```

## I/O

| | Dettaglio |
|---|---|
| **Input** | contratto + `{dominio_business, fonti_conoscenza, strumenti_esistenti}` da A3 |
| **Output** | vault wiki + namespace memoria configurati sul sistema cliente; UAT firmata; record in `agency/clients` |

## Acceptance criteria handoff a 08 INTELLIGENCE (HC-IN-AG-01)

- Template wiki con struttura Index/Log/Concepts/Projects/Tools/Sources
- Namespace memoria inizializzato con chiavi base
- Skill base installabili (empire-context adattato o cliente-specific)
- Fonti citate e ingest completato (non materiale grezzo non processato)

## Gate Delivery (identico agli altri prodotti — A4)

Workflow sul sistema cliente, run test reale, training erogato, cliente autonomo nell'UAT, UAT firmata, nessuna dipendenza residua, handover pack completo.

## Failure

| Evento | Risposta |
|---|---|
| 08 INTELLIGENCE non consegna template | A4-COORD scala a AG-DIR; delay comunicato a cliente |
| Strumenti cliente incompatibili (niente Obsidian/Notion) | fallback: struttura file plain Markdown documentata nel delivery-playbook |
| Cliente non ha API key LLM | supporto attivazione (il cliente attiva, DE non gestisce le chiavi) |

## Connessioni

- [`../Reparti/A4-Delivery/`](../Reparti/A4-Delivery/) — reparto owner
- [`./WF-DELIVERY-OUTREACH-FACTORY.md`](./WF-DELIVERY-OUTREACH-FACTORY.md) · [`./WF-DELIVERY-CONTENT-FACTORY.md`](./WF-DELIVERY-CONTENT-FACTORY.md)
- [`../Funzioni/T-env-setup/`](../Funzioni/T-env-setup/) · [`T-config-tenant/`](../Funzioni/T-config-tenant/) · [`T-training-kit/`](../Funzioni/T-training-kit/)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
