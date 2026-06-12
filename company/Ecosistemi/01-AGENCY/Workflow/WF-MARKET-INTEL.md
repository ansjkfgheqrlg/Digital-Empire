> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 5 (regole knowledge)

# WF-MARKET-INTEL — Market Intelligence & Nicchia

> Workflow L3 di A1-RICERCA · On-demand (non schedulato)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa è

Produce intelligence su nicchia, competitor e trend per due consumatori interni:
- **A2 Acquisizione**: angolo di attacco corretto per quella nicchia
- **A3 Preventivi**: dossier pre-call con problema quantificato e competitor del prospect

Operazionalizza le regole esistenti: `01_ricerca_no_sito.md` (prospect senza sito → segnale),
`02_ricerca_ads_funnel_scarsi.md` (funnel pubblicitario assente → pain point), `06_ricerca_ai_prospects.md`
(prospect AI-aware → approccio diverso). Usa skill `market-audit` e `icp-radar`.

## Flusso

### Sottoflow 1 — Dossier pre-call (richiesta da A3)

```
INPUT: {lead_id, nicchia, data call}
[T-icp-profiler] carica profilo ICP nicchia da agency/leads + 08 INTELLIGENCE
[T-competitor-profiler] competitor.py + cro_audit.py sul dominio del prospect
[T-qualifier] estrae storico interazioni lead da leads.db
OUTPUT: dossier pre-call {profilo_lead, problema_quantificato, top_3_competitor, punti_debolezza}
        → handoff ad A3 con acceptance criteria verificati
```

### Sottoflow 2 — Report nicchia (schedulato o su richiesta)

```
INPUT: {nicchia, profondità_ricerca}
[T-icp-profiler] definisce/aggiorna ICP per nicchia (criteri qualifica, pain point primari)
[T-competitor-profiler] mappa competitor principali (positioning, pricing, punti deboli)
OUTPUT: report nicchia in agency/leads + entry wiki 08 INTELLIGENCE
        → notifica ad A2 (aggiorna angolo outreach) e ad A3 (aggiorna argomentazione)
```

## I/O

| | Dettaglio |
|---|---|
| **Input** | richiesta da A3 (dossier pre-call) o da A1-COORD (report nicchia), nicchia target, data scadenza |
| **Output** | dossier pre-call per A3 OPPURE report nicchia per A2/A3; entry in `agency/leads` |

## Acceptance criteria (dossier pre-call)

- profilo lead completo (fonte, settore, sito, dimensione azienda)
- problema quantificato (non "sito lento" → "tasso conversione X% sotto benchmark di settore")
- almeno 3 competitor analizzati con punti di debolezza specifici
- consegnato a A3 PRIMA della call (non dopo)

## Regole knowledge layer (asset usati così — ADR-003)

| File | Uso |
|---|---|
| `Agenti/Agency/outreach/rules/01_ricerca_no_sito.md` | criteria di qualifica: senza sito = priorità alta |
| `Agenti/Agency/outreach/rules/02_ricerca_ads_funnel_scarsi.md` | funnel assente = pain point vendibile |
| `Agenti/Agency/outreach/rules/06_ricerca_ai_prospects.md` | prospect già AI-consapevoli: angolo diverso |
| `Agenti/Agency/sub-agents/` (ai-implementation, cro-funnel, no-website) | evoluti in profili T-icp-profiler per le 3 nicchie principali |

## Failure

- Nessun dato competitor trovato → dossier senza competitor section + nota "ricerca insufficiente";
  non si inventa. Max usa il dossier sapendo il gap.
- Dossier non pronto prima della call → alert immediato a A3; la call NON viene cancellata
  (il dossier è un ausilio, non un prerequisito bloccante).
- ICP obsoleto (nicchia cambia dinamiche) → `HC-AG-IN-01` verso 08 INTELLIGENCE per refresh.

## Connessioni

- [`../Reparti/A1-Ricerca/`](../Reparti/A1-Ricerca/) — reparto owner
- [`./WF-LEAD-SOURCING.md`](./WF-LEAD-SOURCING.md) — flusso gemello (lead database)
- [`../Funzioni/T-icp-profiler/`](../Funzioni/T-icp-profiler/) · [`T-competitor-profiler/`](../Funzioni/T-competitor-profiler/)
- [`../Reparti/A3-Preventivi/`](../Reparti/A3-Preventivi/) (cliente primario dossier pre-call)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
