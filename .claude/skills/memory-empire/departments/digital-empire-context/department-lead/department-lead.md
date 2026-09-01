# digital-empire-context / department-lead

**Ruolo:** Carica il contesto di Digital Empire per ogni query o lavoro. Conosce tutta la wiki, i progetti attivi, i workflow correnti.

## Pipeline
- context-loader: carica wiki + knowledge rilevanti per la query
- knowledge-cartographer: mappa le connessioni tra i contenuti

## Attivazione
Quando intent-type è QUERY_DE o WORK_DE.
