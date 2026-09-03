# Enrichment Report — BSUHmVcaO1g

**Video:** "Se usi ancora i prompt... devi vedere questa evoluzione" — Simone Rizzo, 31m23s
**Run:** `max17-v07-rizzo-prompt`, batch max17 v07
**Stage 1-5 eseguiti:** sessione precedente al 2026-09-03 (visione, atomi, coverage) — interrotti
per limite di sessione prima di Stage 6-9
**Stage 6-9 eseguiti:** 2026-09-03 (questa sessione — ripresa da `company/Memory/riprese/EMP-QQ2R.md`)
**Atoms disponibili:** 71 KA · coverage frame **133/224 scene (59,4%), 176/942 frame totali
(18,7%)** — NO-FINTO: PASS con copertura parziale dichiarata (nessun capitolo del video resta
scoperto, dettaglio in `runs/max17-v07-rizzo-prompt/coverage.md`)

---

## Correzione preliminare — un file trovato inesatto

Prima di scrivere qualunque cosa, verificato lo stato reale su disco rispetto a quanto dichiarato
in `ingest-manifest.json` (scritto dalla sentinella `studia-rizzo` prima di morire per limite di
sessione). Il manifest dichiarava:
- `wiki_page`: `second-brain-vault/wiki/sources/Source_Simone_Rizzo_Loop_Engineering.md` — **non
  esisteva su disco**.
- `patches_applied`: due patch a `.claude/agents/guild-prompt.md` e
  `.claude/skills/prompt-engegniring-skill/SKILL.md` — **nessuna delle due esisteva su disco**
  (verificato con grep sui marker di testo dichiarati in ciascuna patch: zero risultati in
  entrambi i file).

Non è chiaro se il manifest sia stato scritto come piano d'intenti mai eseguito o se sia un
artefatto di una fase pianificata poi interrotta prima dell'esecuzione. In ogni caso il file
dichiarava come "fatto" qualcosa che non lo era — esattamente la classe di errore che la regola
NO-FINTO esiste per impedire. Corretto in questa sessione: `patches_applied` svuotato, le due
proposte spostate in `patches_proposed_not_applied` con nota esplicita, `wiki_page` ora punta a
una pagina realmente creata in questa sessione. Segnalato anche nel checkpoint di chiusura.

---

## Stage D — Relevance / Gap / Scout

### La tesi trasferibile del video

Non è "usa questi due comandi nuovi". È che un ciclo autonomo (loop, agente che gira senza
supervisione ad ogni passo) è affidabile solo quanto il suo **meccanismo di verifica** — e che
esiste una gerarchia netta di quanto ci si può fidare di quel meccanismo, dal deterministico
(livello 1) al checkpoint umano (livello 5). Questa tassonomia è generica, non specifica di
Claude Code, e si applica a qualunque processo Digital Empire che oggi gira in autonomia.

### Skill/agenti candidati e verdetto

| Target | Verdetto | Motivo |
|---|---|---|
| `.claude/agents/guild-prompt.md` | **Gap confermato, proposta non applicata** | Ha già una sezione "⚠️ VUOTI DI CONOSCENZA DICHIARATI" aperta (4 punti), governa lo standard prompt dell'Impero, ma non nomina mai Harness/Loop Engineering né una griglia di livelli di fiducia per i cicli autonomi. Verificato con grep: zero occorrenze di "loop", "goal", "harness" nel file. |
| `.claude/skills/prompt-engegniring-skill/SKILL.md` | **Gap confermato, proposta non applicata** | Ha già "GOLDEN PROMPT STRUCTURE (Template per PROMETHEUS)" — il template "Anatomy of a Claude prompt" del video è un template diverso e complementare (prompt di TASK, non di sistema), verificato assente col medesimo grep. |
| `nerve-solve` (Orchestration Layer 1) | Nessuna patch, connessione registrata | Il sistema nervoso cognitivo di NERVE-SOLVE è un candidato naturale per ospitare i 5 Livelli di Verifica come griglia trasversale, ma è fuori dal perimetro di questa sessione (nessuna richiesta esplicita, e patchare un orchestration layer richiede più contesto di quanto disponibile qui). Solo cross-link in wiki. |
| Empire Studio stesso (le sentinelle che leggono i frame) | Osservazione, nessuna azione | Le sentinelle Empire Studio sono di fatto un ciclo Trigger→Execution→Goal-Verify→Output ("coverage.md" dichiara la condizione di terminazione: soglia di copertura + budget di sessione). Non dichiarano oggi esplicitamente su quale dei 5 livelli opera il proprio gate (coverage % è un livello 2, non un 1). Notato, non patchato: serve una decisione di Max su dove vive questa dichiarazione. |

### Perché nessuna patch è stata scritta in questa sessione

Il checkpoint `EMP-QQ2R` (sezione 4) elenca tre sentinelle morte in parallelo sullo stesso
lancio (`studia-rizzo`, `studia-roberts`, `sentinella-cfo-ai`) e la regola del ciclo a 9 passi
impone coordinamento prima di un lavoro che tocca skill/agenti condivisi in parallelo con altri.
Modificare `guild-prompt.md` o `prompt-engegniring-skill/SKILL.md` in questa sessione, mentre
`studia-roberts` lavora sullo stesso repo, rischiava una collisione non necessaria: il compito
esplicito di questa ripresa era chiudere il video (wiki + memory + consigli), non patchare skill
condivise. Le due proposte restano scritte per intero nella pagina wiki, pronte per essere
applicate in una sessione dedicata.

---

## Stage E — Gate

Nessuna patch applicata in questa sessione = nessun diff da validare su file condivisi. L'unica
scrittura su file preesistente è la correzione di `ingest-manifest.json` (questo stesso
knowledge folder, non condiviso con altri reparti) per rimuovere le due dichiarazioni false.

---

## Stage H — Cosa ha trovato Memory Empire

**Arricchite:** nessuna skill/agente esistente in questa sessione.

**Creata:** `second-brain-vault/wiki/sources/Source_Simone_Rizzo_Loop_Engineering.md` — pagina
wiki nuova con sezione "Consigli" che porta le due proposte sopra fino al livello di dettaglio
di una patch pronta da applicare, senza applicarle.

**Esplicitamente NON arricchite, e perché:** `nerve-solve` (fuori perimetro, serve decisione di
Max su dove vive la griglia dei 5 livelli), Empire Studio stesso (stesso motivo).

**Tensioni aperte da questo video:** il manifest falso descritto sopra — non è una tensione di
contenuto ma un difetto di processo: una sentinella può scrivere "fatto" prima di aver
verificato che lo fosse davvero. Non risolvibile da questa sessione in generale (serve un
controllo strutturale, es. un gate che confronti `patches_applied` dichiarati con un vero grep
sui file target prima di chiudere il ciclo) — solo il caso singolo è stato corretto qui.

---

## Tracciabilità

- Contenuto integrale: `knowledge/BSUHmVcaO1g/contenuto-integrale.md` (656 righe, per categoria, non riassunto)
- Atoms: `knowledge/BSUHmVcaO1g/atoms.json` (71 KA)
- Manifest: `knowledge/BSUHmVcaO1g/ingest-manifest.json` (corretto in questa sessione)
- Analisi visiva: `runs/max17-v07-rizzo-prompt/video-analysis.md` (922 righe, walkthrough cronologico completo)
- Coverage: `runs/max17-v07-rizzo-prompt/coverage.md` (138 righe, copertura dichiarata blocco per blocco)
- Pagina wiki: `second-brain-vault/wiki/sources/Source_Simone_Rizzo_Loop_Engineering.md`
- Checkpoint di chiusura: `company/Memory/checkpoints/` (vedi ultimo CP-20260903-*)
