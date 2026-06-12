> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A3 + sez. 6 (skill discovery-call-brief)

# T-DISCOVERY-BRIEF — Discovery Brief Builder

> Funzione L4 di A3-PREVENTIVI · Worker · Agente: `AG-A3-BRIEF-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A3

## Cosa fa

Due ruoli distinti in A3:

**1. Dossier pre-call** (PRIMA della call): aggrega lead + audit + competitor da A1 → Max arriva
alla call già istruito. Input: `{lead_id, data_call}`.

**2. Brief strutturato post-call** (DOPO la call): trasforma trascrizione/appunti in brief
standardizzato che guida tutto il WF-PREVENTIVO. Skill: `discovery-call-brief`.

## Schema brief post-call

```json
{
  "cliente": "Azienda Target Srl",
  "data_call": "2026-06-11",
  "problema_principale": "Outreach commerciale manuale: 2h/giorno, 20 email/gg, 0 sistema",
  "problema_quantificato": "~40h/mese = ~€2.000 di costo opportunità a ore",
  "awareness_level": "aware",
  "prodotti_considerati": ["Outreach Factory €4.000"],
  "stack_attuale": "Gmail manuale, nessun CRM, sito WordPress",
  "vincoli_ambiente": {
    "os": "Windows 10",
    "ha_server_dedicato": false,
    "ha_vps": true,
    "provider_vps": "Aruba",
    "python_disponibile": true,
    "credenziali_email": "da verificare post-firma"
  },
  "budget_signal": "esplicito: 'quanto costa?', non ha chiesto sconto",
  "obiezioni_emerse": ["'ci vorrà tempo per imparare'"],
  "next_step_concordato": "preventivo entro 48h"
}
```

## Perché i vincoli ambiente sono critici

Il campo `vincoli_ambiente` non è opzionale: A4 ne ha bisogno per pianificare la delivery.
Se la call non ha rilevato i prerequisiti → T-DISCOVERY-BRIEF segnala il gap a Max PRIMA di
scrivere il preventivo. Il countdown 7gg di A4 parte SOLO ad ambiente conforme.

## Failure

| Evento | Risposta |
|---|---|
| Appunti call incompleti | brief marcato "draft" con gap espliciti; richiesta integrazione a Max |
| Vincoli ambiente non rilevati in call | alert: "prerequisiti mancanti — rischio G1 A4" + checklist da far completare al cliente |
| Awareness level ambiguo | usa `aware` per sicurezza (approccio più diretto); segnala ambiguità al brief |

## Asset evoluti qui (azione F3 — dossier §5)

- `Agenti/Agency/outreach/script_chiamata_freddo.md` → diventa la checklist di raccolta info durante call
- `genera_tabella_chiamate.py` → diventa il template di log call strutturato

## Connessioni

- [`../Reparti/A3-Preventivi/`](../Reparti/A3-Preventivi/) · [`../Workflow/WF-PREVENTIVO.md`](../Workflow/WF-PREVENTIVO.md)
- [`./T-problem-audit.md`](./T-problem-audit.md) (downstream: usa il brief) · [`../Funzioni/T-icp-profiler.md`](./T-icp-profiler.md) (upstream: ICP di nicchia)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
