> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A3 + sez. 6 (skill beast-preventivi)

# T-PROPOSAL-WRITER — Proposal Writer

> Funzione L4 di A3-PREVENTIVI · Worker · Agente: `AG-A3-PROP-W` (opus)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A3

## Cosa fa

Costruisce il documento preventivo completo a partire da brief + audit. Skill principale:
**`beast-preventivi`** + `market-proposal`. Tier opus: la proposta è il momento più critico
del funnel revenue — una proposta sbagliata perde il contratto.

## Struttura documento (problem-first obbligatorio)

```
1. IL TUO PROBLEMA (non "chi siamo")
   → problema quantificato (da T-PROBLEM-AUDIT), impatto economico, perché adesso
   → awareness level: aware → ROI focus; unaware → education del problema primo

2. LA SOLUZIONE PROPOSTA
   → prodotto DE selezionato (da T-PRICING-CONFIG): Outreach Factory / Content Factory / Second Brain
   → cosa include esattamente (no ambiguità di scope)
   → cosa NON include (out-of-scope esplicito)

3. COME FUNZIONA LA DELIVERY
   → 7 giorni su TUO server/macchina
   → Giorno 1: verifica ambiente; Giorni 2-6: setup + training; Giorno 7: UAT + handover
   → Il codice è TUO, zero canoni mensili, zero dipendenza da DE dopo il handover

4. INVESTIMENTO
   → prezzo catalogo: [4.000 / 3.500 / 2.500 / 8.000] € — one-time
   → zero canoni, zero abbonamenti, zero costi ricorrenti DE
   → pagamento: [modalità concordata con Max]

5. GARANZIE E SUPPORTO
   → 90 giorni supporto con SLA definito
   → se in 7 giorni non è funzionante → (clausola di rollback definita con Max)

6. PROSSIMI PASSI
   → CTA unica: firma + pagamento → avvio delivery entro X giorni
```

## Regole inviolabili

- Il documento NON inizia con "Chi siamo" o "Digital Empire è..." — INIZIA con il problema del cliente
- Pricing SOLO da catalogo (T-PRICING-CONFIG): nessuno sconto non autorizzato
- Promesse = solo prove verificabili (Mandato Empire)
- `memory_search` su `agency/proposals` prima di scrivere: evitare errori di preventivi persi

## Failure

| Evento | Risposta |
|---|---|
| Audit mancante | T-proposal-writer non produce senza quantificazione problema; segnala gap a A3-COORD |
| Gate Preventivo boccia | rework specifico con le note del gate; il countdown 48h NON si ferma |
| Richiesta sconto in itinere | risponde "pricing a catalogo, non ho facoltà di deroga; escalation a Max" |

## Connessioni

- [`./T-problem-audit.md`](./T-problem-audit.md) (fornitore) · [`./T-pricing-config.md`](./T-pricing-config.md) (co-input) · [`./T-proposal-qa.md`](./T-proposal-qa.md) (gate successivo)
- [`../Reparti/A3-Preventivi/`](../Reparti/A3-Preventivi/) · [`../Workflow/WF-PREVENTIVO.md`](../Workflow/WF-PREVENTIVO.md)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
