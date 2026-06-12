> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A3 + sez. 4 (step 5) + sez. 8 (Gate Preventivo)

# WF-PREVENTIVO — Produzione Preventivo Problem-First

> Workflow L3 di A3-PREVENTIVI · Topologia: `pipeline` · SLA: ≤48h dalla discovery call
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A3 + §8

## Cosa è

Pipeline lineare che trasforma trascrizione/appunti di una discovery call in una **proposta
problem-first** inviata entro 48h, con pricing a catalogo, passata dal Gate Preventivo.
Il documento APRE con il problema del cliente — mai con Digital Empire.

## Flusso

```
INPUT: trascrizione/appunti call + storico thread A2 + dossier pre-call A1
           ↓ countdown 48h parte da qui
[T-discovery-brief] → brief strutturato {problema, awareness_level, stack attuale, vincoli_ambiente, budget_signal}
           ↓ brief validato
[T-problem-audit] → problema quantificato (market-audit, cro_audit): non "sito lento" ma "conversione X%"
           ↓ audit con numeri
[T-pricing-config] → selezione prodotto/bundle: Outreach Factory €4.000 / Content Factory €3.500 / Second Brain €2.500 / Engine Room €8.000
           ↓ prodotto selezionato + scope
[T-proposal-writer] → documento completo (skill beast-preventivi + market-proposal)
           ↓ bozza
[T-proposal-qa] → GATE PREVENTIVO (skill proposal-gate)
           ↓ PASS (oppure rework con note specifiche)
OUTPUT: proposta inviata + record in agency/proposals {stato: inviata, data, prodotto, valore}
```

## Gate Preventivo (bloccante — pattern #4)

Criteri obbligatori (tutti devono passare):
- Il documento APRE con il problema del cliente (non con DE)
- Awareness level corretto: aware → ROI immediato; unaware → education prima di offerta
- Pricing SOLO a catalogo (4.000/3.500/2.500/8.000 €); nessuno sconto non autorizzato dal Board
- Promesse = solo prove verificabili (Mandato Empire: zero claim non documentati)
- Scope delivery ≤7gg esplicito nel documento
- Clausola proprietà codice + €0 canoni presente e leggibile
- Supporto 90gg definito con SLA
- Brand voice conforme al Mandato Empire

Gate boccia → note correttive specifiche → rework (il countdown 48h NON si ferma).

## I/O

| | Dettaglio |
|---|---|
| **Input** | trascrizione/appunti call (da Max), dossier pre-call da A1, thread conversazione da A2 |
| **Output** | preventivo inviato (via Max, non automatico) + record in `agency/proposals`; se loss → motivo + pattern in `agency/reasoning` |

## Regole operative

- `memory_search` su `agency/proposals` PRIMA di scrivere: preventivi simili, motivi di loss
- `memory_search` su `agency/reasoning`: pattern di fallimento per quella nicchia
- Proposta inviata SEMPRE via Max (firma umana); WF produce il documento, non lo invia autonomamente
- Brief incompleto (vincoli ambiente mancanti) → richiesta integrazione a Max PRIMA di procedere
  (i prerequisiti ambiente servono ad A4: scoprirli dopo firma → delivery bloccata)
- Richiesta sconto fuori catalogo → NO automatico; eventuale deroga = decisione Board scritta in `agency/proposals`

## Failure

| Evento | Risposta |
|---|---|
| Gate boccia dopo 3 cicli rework | escalation a AG-A3-COORD → brief rilavorato o richiesta chiarimento a Max |
| SLA 48h a rischio | alert a Max con bozza parziale + gap da colmare; decide se procedere o posticipare |
| Loss preventivo | motivo obbligatorio in `agency/proposals`; dopo 2 loss nella stessa nicchia → audit + `HC-AG-IN-01` |
| Scope ambiguo post-firma | non si accetta scope ambiguo; ri-contrattualizzazione con Max prima di avviare A4 |

## Connessioni

- [`../Reparti/A3-Preventivi/`](../Reparti/A3-Preventivi/) — reparto owner
- [`../Funzioni/T-discovery-brief/`](../Funzioni/T-discovery-brief/) · [`T-problem-audit/`](../Funzioni/T-problem-audit/) · [`T-proposal-writer/`](../Funzioni/T-proposal-writer/) · [`T-pricing-config/`](../Funzioni/T-pricing-config/) · [`T-proposal-qa/`](../Funzioni/T-proposal-qa/)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/) (call prenotata → input) · [`../Reparti/A4-Delivery/`](../Reparti/A4-Delivery/) (output: contratto firmato + scope)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
