# Web Reference Strategy (v1.0)

**Reparto:** Web · **Tipo:** documentazione / articoli / ricerca · **Wiki:** Reference / Knowledge Base (MOC)

## Trigger
Query di ricerca avanzata, singola pagina, o sito/documentazione da approfondire.

## Regole obbligatorie
1. **Playwright (render JS)**: per contenuti dinamici; fallback urllib se Playwright assente.
2. **Main content**: estrai solo il contenuto utile (no nav/footer/ads); preserva code block e tabelle.
3. **Screenshot sezioni chiave**: per UI/diagrammi -> Claude li guarda (visione anche sul web).
4. **Meno tempo, piu' sezioni**: l'unita' e' la sezione/pagina, non il timestamp.
5. **Trace**: ogni blocco -> URL (+ screenshot file se visivo).

## Stile nota wiki
Reference / Knowledge Base: gerarchia MOC + pagine atomiche con trace a URL. Code block preservati.

## Decision tree
- Query -> web-researcher trova le fonti (sources.json).
- URL/sito -> site-crawler (cap pagine/profondita') -> doc-extractor (main content).
- Sezioni visive -> screenshot per la visione.

## Performance goal
Fonti pertinenti e autorevoli (no spam); code/tabelle integri; trace a URL su ogni atomo.
