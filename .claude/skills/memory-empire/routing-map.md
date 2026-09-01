# Memory Empire - Routing Map (intento → workflow)

Memory Empire legge l'intento e attiva il workflow giusto. Se il workflow dovrebbe
partire da solo ma non parte, Memory Empire **lo richiama esplicitamente**.

| Segnale / intento | Workflow da attivare | Cosa fa |
|---|---|---|
| Link YouTube (video o canale) | **Empire Studio** (`--dept` interno = youtube) | guarda i video (frame+visione), transcript, tutta la formazione → content-forge via agenti → wiki + Memory Empire |
| Link TikTok | **Empire Studio** (tiktok) | come sopra, frame densi |
| Link sito / "fai ricerca su…" | **Empire Studio** (web) | crawl + estrazione + screenshot → forge → wiki |
| Path a repo/progetto/report | **Empire Studio** (projects) | deep study read-only (architettura/perche'/trace) → forge → wiki |
| "guarda questo video", "prendi la formazione", "mettilo nella wiki" | **Empire Studio** | ingestione completa naturale |
| Domanda/lavoro su Digital Empire (agenzia, corsi, SaaS, ecc.) | **digital-empire-context** (interno) | carica wiki/memoria pertinente e risponde ricco |
| Outreach / email / IG / LinkedIn | workflow Outreach (skill /avvia-*) | richiama il flusso outreach esistente |
| Libri / KDP | workflow Libri | richiama il flusso libri |
| Creazione siti / landing | workflow siti (site/empire-style) | richiama il flusso siti |
| `/sync-wiki-totale` o "sincronizza tutto nella wiki" | **memory-wiki-bridge** (ingestion-archive) | diff company/Memory (checkpoint/ADR/STATO-EMPIRE) vs wiki, colma i gap, aggiorna grafo |

## Regola di fallback (la parte chiave richiesta)
Per OGNI riga: se il workflow **dovrebbe** attivarsi da solo (es. l'utente passa
un link → Empire Studio) ma per qualche motivo non parte, **workflow-router** di
Memory Empire lo capisce e lo **attiva/interroga/richiama** comunque. Memory
Empire e' la rete di sicurezza che garantisce che il workflow giusto venga sempre
eseguito.

## Principio
content-forge NON viene mai invocato "a mano": viene usato **dagli agenti di
Empire Studio** (content-forge-invoker, forge-team) nel modo migliore. Memory
Empire instrada, non scavalca.
