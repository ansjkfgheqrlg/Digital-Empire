> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 6 (skill icp-radar)

# T-ICP-PROFILER — Profiler ICP e Nicchia

> Funzione L4 di A1-RICERCA · Worker · Agente: `AG-A1-ICP-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa fa

Definisce e aggiorna i profili ICP (Ideal Customer Profile) per nicchia. È la fonte di verità
per T-QUALIFIER e per l'angolo di attacco di A2. Usa la skill **`icp-radar`**.
Input da 08 INTELLIGENCE (customer research, trend) via `HC-IN-AG-01`.

## Profilo ICP — schema

```json
{
  "nicchia": "ecommerce-moda",
  "versione": "2026-06-11",
  "criteri_include": {
    "settori": ["moda", "abbigliamento", "accessori"],
    "dimensione": "1-50 dipendenti",
    "segnali": ["sito-esistente", "ads-attive", "email-aziendale"]
  },
  "criteri_exclude": {
    "dimensione": ">200 dipendenti (enterprise)",
    "segnali": ["no-sito (regola 01)", "brand-nazionale-consolidato"]
  },
  "pain_point_primari": [
    "tasso di conversione basso vs benchmark settore",
    "produzione contenuti manuale e lenta",
    "outreach commerciale assente o inefficace"
  ],
  "awareness_level": "aware (sanno che esiste l'AI ma non sanno come implementarla)",
  "soglia_score": 60,
  "angolo_attacco_raccomandato": "ROI immediato: quanto ti costa adesso produrre 1 contenuto?"
}
```

## Quando aggiornare l'ICP

- Ingresso in una **nuova nicchia** (richiesta da A2 o da Max)
- **Win rate cala per 2 cicli** sulla stessa nicchia → ICP potrebbe essere obsoleto
- **Nuovi dati da 08 INTELLIGENCE** (trend, competitor, cambio awareness del mercato)
- Input esplicito da AG-A1-COORD

## Comportamento

- Versiona ogni profilo ICP: `{nicchia}_v{YYYYMMDD}` in `agency/leads` namespace
- Il profilo nuovo NON sovrascrive il vecchio: mantiene storico per confrontare performance
- La soglia score è proprietà del profilo ICP (non fissa in T-QUALIFIER)
- Skill `icp-radar` guida la costruzione con criteri di qualifica espliciti

## Failure

| Evento | Risposta |
|---|---|
| Dati insufficienti per la nicchia | ICP marcato "draft": T-qualifier usa soglia conservativa (70); alert a AG-A1-COORD per raccogliere più dati |
| Nicchia senza ICP → richiesta scraping | STOP: non si scrappa senza ICP esplicito (ordine di esecuzione obbligatorio) |

## Connessioni

- [`./T-qualifier.md`](./T-qualifier.md) (cliente principale dell'ICP)
- [`./T-competitor-profiler.md`](./T-competitor-profiler.md) (complementare: competitor per nicchia)
- [`../Reparti/A1-Ricerca/`](../Reparti/A1-Ricerca/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
