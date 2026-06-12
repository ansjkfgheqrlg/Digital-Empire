> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A6 + sez. 4 (step 9) + sez. 8 (Gate Brand)

# WF-CASE-STUDY — Produzione Case Study e Testimonianze

> Workflow L3 di A6-MARKETING-INTERNO · Triggered: Gate Delivery firmato
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A6

## Cosa è

Trasforma ogni delivery chiusa in un **case study APSOC verificato** con metriche reali del
cliente. Produce la prova sociale che alimenta outreach, preventivi e landing.
**Regola assoluta: solo metriche reali fornite dal cliente — mai inventate o stimate.**

## Flusso

```
TRIGGER: Gate Delivery firmato → segnale da A4 ad A6

FASE 1 — Raccolta prova (T-proof-collector) — da avviare entro 7gg dalla firma Gate Delivery:
  Contatto cliente con messaggio personalizzato (non automatico):
    "Abbiamo completato la delivery X giorni fa. Hai avuto modo di fare le prime run?
    Siamo curiosi di sapere i tuoi numeri iniziali per documentare il caso."
  Raccolta: screenshot dashboard, metriche (reply rate, volumi, risparmio ore, ROI stimato)
  → SE il cliente fornisce dati: si procede
  → SE non risponde dopo 7gg: 1 follow-up → poi si chiude SENZA case study
    (non si inventa, non si stima, non si pressano i clienti)

FASE 2 — Raccolta formale a 90gg (T-proof-collector):
  A chiusura supporto 90gg: richiesta testimonianza formale + metriche consolidate
  Formato: scritto (1-2 paragrafi) o video (max 2 minuti)
  → metriche consolidate su 90gg di utilizzo reale

FASE 3 — Scrittura case study (T-case-writer) — skill case-study-forge:
  Struttura APSOC:
    A = hook: la situazione del cliente prima (problema, contesto)
    P = il problema specifico che DE ha risolto (quantificato se possibile)
    S = la soluzione: quale prodotto, come implementato, cosa ha implicato la delivery
    O = obiezioni superate: cosa temeva il cliente, come si è risolto
    C = risultati reali (metriche cliente) + CTA per chi vuole lo stesso risultato
  GATE BRAND: Sentinel Brand-Voice verifica → zero claim non documentati, scarcity solo reale

FASE 4 — Produzione asset (handoff a 03 CF):
  Brief: {case_study_testo, brand_kit_DE, formati_richiesti: [carosello, reel_social_proof, snippet_email]}
  → 03 CF produce asset grafici/video
  → A6 pubblica: landing agency-empire-landing, wiki (fonte prova), database A5 (munizioni outreach)

OUTPUT: case study pubblicato + asset prodotti + testimonianza in agency/clients
```

## I/O

| | Dettaglio |
|---|---|
| **Input** | segnale Gate Delivery firmato da A4; metriche reali del cliente |
| **Output** | case study APSOC + asset grafici; testimonianza in `agency/clients`; feed per A2 (munizioni) e A5 (libreria obiezioni) |

## Regola prova

`T-proof-collector` raccoglie solo ciò che il cliente documenta spontaneamente. Se il cliente
fornisce metriche non verificabili (es. "ho avuto 300 risposte ma non ho il log") → il case
study usa solo la parte qualitativa verificata (testimonianza), non i numeri non verificabili.
Il Brand-Voice Sentinel blocca qualsiasi claim non documentato.

## WF-ASSET-VETRINA (sottoflow incluso)

Manutenzione periodica di `agency-empire-landing` e `presentazione-empire.vercel.app`:
- Ogni nuovo case study → aggiornamento landing (via 06 PLATFORM con `HC-AG-PL-01`)
- Presentazione resta CTA standard di tutti i canali outreach (non si cambia senza ADR)
- Audit semestrale: landing conforme al brand gate, link funzionanti, metriche aggiornate

## Connessioni

- [`../Reparti/A6-Marketing-Interno/`](../Reparti/A6-Marketing-Interno/) — reparto owner
- [`../Funzioni/T-proof-collector/`](../Funzioni/T-proof-collector/) · [`T-case-writer/`](../Funzioni/T-case-writer/) · [`T-upsell-mapper/`](../Funzioni/T-upsell-mapper/)
- [`../Reparti/A4-Delivery/`](../Reparti/A4-Delivery/) (fornitore: segnale Gate Delivery)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/) (cliente: munizioni outreach) · [`../Reparti/A5-Copywriting-Interno/`](../Reparti/A5-Copywriting-Interno/) (testimonianze per libreria obiezioni)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
