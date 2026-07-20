# FAILURE-MODES — youtube-script-factory

| ID | Fallimento | Sintomo | Prevenzione | Rilevazione | Recupero |
|---|---|---|---|---|---|
| F1 | Hook generico ("In questo video vedremo...") | retention <20% nei primi 15s | hook solo dalle 20 formule/4 categorie + checklist hook (≥3 criteri) | scoring sezione hook basso | riscrivere hook da formula categoria giusta; re-score prima di registrare |
| F2 | CTA assente o a 1 solo livello | 0 lead da video con views | sistema CTA 3 livelli obbligatorio (preview/reminder/finale) | checklist CTA; review settimanale lead/video | inserire i 3 livelli e ripubblicare descrizione/pinned |
| F3 | Scoring falsato ("a occhio va bene") | video deboli programmati | nessuna registrazione senza score ≥ fascia 🟡 da `checklist_qualita.py` | audit batch: script senza report JSON | stop programmazione, score reale, fix sezioni carenti (persistente 2× → regola nuova) |
| F4 | Letto integrale 5.166r a ogni uso (spreco contesto) | output lento/superficiale | usare spec.md §mappa + SEZ 6 come kernel operativo | tempo di attivazione >2 min | tornare all'indice; kernel operativo = cheat sheet |
| F5 | Tool non trovati/eseguiti (erano markdown-embedded) | "python3 genera_script.py → file assente" | RISOLTO sprint 1: estratti in `tools/` (2026-07-20). Regola deriva: md vince, ri-estrarre se §7-9 cambiano | smoke compile dopo ogni modifica md | ri-estrazione + `py_compile` 3/3 |
| F6 | Backlog desync (video prodotti non nel manager; mix 70/20/10 violato) | piano settimanale sballato, troppi Conversion | ogni video passa da backlog_manager per stato/performance | report settimanale ≠ realtà canale | riconciliazione da analytics YouTube + fix stato; ricorrente → regola nuova |
| F7 | Sconfinamento: fa strategia/APSOC (deleghe violate) | duplicati strategia, gate saltati | evals E4-E6: delega a `/youtube-lead-machine` (strategia) e `copy-workflow` (QA copy) | output contiene consigli di posizionamento | rimandare alla skill giusta + nota in memory |
