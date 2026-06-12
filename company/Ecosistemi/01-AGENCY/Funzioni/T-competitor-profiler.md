> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 5 (competitor.py, cro_audit.py)

# T-COMPETITOR-PROFILER — Analista Competitor e Audit Prospect

> Funzione L4 di A1-RICERCA · Worker · Agente: `AG-A1-COMP-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa fa

Produce un **dossier competitor** del prospect: chi sono i principali competitor, i loro punti
deboli, come DE si posiziona in contrasto. Usato principalmente per il dossier pre-call (A3)
e per affinare l'angolo di attacco (A2).

## Script esistenti (usati-così — ADR-003)

| Script | Uso |
|---|---|
| `Agenti/Agency/sub-agents/competitor.py` | raccoglie dati sui principali competitor del prospect |
| `Agenti/Agency/sub-agents/cro_audit.py` | audit CRO del sito del prospect (funnel, conversione) |
| Skill `market-audit` | framework analisi competitiva strutturata |

## Output schema

```json
{
  "prospect": "Azienda Target Srl",
  "audit_sito": {
    "velocita": "lenta (>3s caricamento)",
    "cro": "nessuna CTA above-the-fold, no social proof",
    "funnel": "sito vetrina senza conversione misurabile"
  },
  "competitor_top3": [
    {
      "nome": "Competitor A",
      "punti_debolezza": ["prezzo alto", "nessun supporto post-delivery"],
      "come_DE_si_differenzia": "ownership codice + €0 canoni"
    }
  ],
  "angolo_differenziante": "Il cliente paga loro X/mese per sempre; DE è one-time e il codice è suo"
}
```

## Regole operative

- Dossier pre-call: consegnato ad A3 PRIMA della call con il prospect
- Analisi si basa su dati pubblicamente disponibili (sito, ads, social, prezzi pubblici)
- MAI inventare punti deboli competitor non verificabili: solo ciò che è osservabile
- L'angolo differenziante va in `agency/outreach` come input per A2 e A5

## Failure

| Evento | Risposta |
|---|---|
| Prospect senza sito | applica regola `01_ricerca_no_sito.md`: priorità alta come lead; audit sito = "assente" (questo è il problema da vendere) |
| Competitor non identificabili | dossier senza sezione competitor; non si inventa; Max usa il gap come punto di partenza call |
| cro_audit.py fallisce su sito | tentativo manuale (schermata + analisi visiva); se impossibile → sezione "non analizzato" |

## Connessioni

- [`./T-icp-profiler.md`](./T-icp-profiler.md) (complementare: ICP per nicchia)
- [`../Workflow/WF-MARKET-INTEL.md`](../Workflow/WF-MARKET-INTEL.md) (contesto workflow)
- [`../Reparti/A3-Preventivi/`](../Reparti/A3-Preventivi/) (cliente principale: dossier pre-call)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
