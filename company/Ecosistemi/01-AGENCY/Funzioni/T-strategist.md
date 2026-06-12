> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A2 + sez. 5 (strategist.py, insight.py)

# T-STRATEGIST — Strategist Angolo di Attacco

> Funzione L4 di A2-ACQUISIZIONE · Worker · Agente: `AG-A2-STRAT-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2

## Cosa fa

Per ogni lead in `leads.db`, determina l'**angolo di attacco**: il problema specifico da usare
come hook del messaggio outreach, personalizzato per quel lead. Script: `strategist.py`, `insight.py`.

## Logica di ragionamento

1. Carica profilo lead da `leads.db` (settore, sito, segnali, score, tag ICP)
2. Carica ICP nicchia da `agency/leads` (pain point primari, awareness level)
3. Seleziona angolo in ordine di priorità:
   - Segnale specifico del lead (es. "hai ads attive ma senza landing → conversioni basse")
   - Pain point primario della nicchia (da ICP)
   - Differenziante competitor (da T-COMPETITOR-PROFILER se disponibile)
4. Produce `{angolo, evidenza_specifica, awareness_level}` → T-WRITER-APSOC

## Awareness level

| Livello | Significato | Approccio |
|---|---|---|
| `aware` | Sa che l'AI per outreach/content esiste | pitch diretto ROI: "quanto ti costa adesso?" |
| `unaware` | Non sa che esiste la soluzione AI | education prima dell'offerta: problema → impatto → possibilità |

Il livello è estratto dall'ICP e può essere corretto da segnali individuali del lead
(es. "ha pubblicato post sull'AI" → aggiorna a `aware`).

## Failure

| Evento | Risposta |
|---|---|
| Lead senza segnali specifici | usa pain point generico di nicchia; non inventare segnali |
| ICP non disponibile | alert a T-ICP-PROFILER; batch in attesa |
| Angolo già usato con quel lead (via agency/conversations) | seleziona angolo alternativo; se esauriti → lead non contattato questo ciclo |

## Connessioni

- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/)
- [`./T-writer-apsoc.md`](./T-writer-apsoc.md) (cliente diretto dell'angolo)
- [`../Funzioni/T-icp-profiler.md`](./T-icp-profiler.md) · [`../Funzioni/T-competitor-profiler.md`](./T-competitor-profiler.md)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
