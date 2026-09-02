# Enrichment Report — DTCyvo6cC54

**Video:** "Every Level of a Claude Second Brain Explained" — Nate Herk | AI Automation, 30m59, EN
**Run:** `empire-studio/runs/max17-v08-herk-brain`
**Stage C-H eseguiti:** 2026-09-02
**Atoms disponibili:** 55 KA — 20 alta rilevanza DE, 17 media, 18 bassa

---

## Stage D — Relevance / Gap / Scout

### Perimetro imposto dal brief

A differenza di run precedenti (dove lo Stage D valutava più skill in un dominio), questo
brief indicava **due bersagli precisi e già scelti da Max**, con il gap **già verificato sulla
wiki reale** (1.831 pagine) nel `video-analysis.md` preesistente:

1. `.claude/skills/sync-wiki-totale/SKILL.md` — aggiungere al report MATCH/GAP una dimensione
   nuova: la valutazione del livello di maturità per area della wiki, sulla scala del video
   (1-5).
2. `.claude/agents/conoscenza-empire.md` — aggiungere una nota operativa sulla natura lessicale
   (non semantica) della ricerca su 1.800+ pagine.

Il brief chiedeva esplicitamente di **verificare il gap di persona prima di scrivere**, non
solo fidarsi del `video-analysis.md` esistente.

### Verifica del gap (fatta di persona in questa sessione)

- **`sync-wiki-totale/SKILL.md`** letto integralmente (52 righe prima della patch). Il passo 3
  ("Aggiorna index.md e log.md") è seguito direttamente dal passo 4 "Report finale
  all'utente" con un formato fisso (Checkpoint totali/ADR totali/Knowledge Memory
  Empire/Pagine create-aggiornate-orfane/GAP residuo). **Nessuna riga, in nessun punto del
  file, menziona un "livello di maturità" o una scala 1-5** — confermato con lettura diretta,
  non solo `grep`.
- **`conoscenza-empire.md`** letto integralmente (176 righe prima della patch). La tabella
  "COSA POSSIEDI" (sezione 3) elenca la wiki (fonte #2, 1.828+ pagine) e l'archivio video
  (fonte #1) senza mai qualificare **come** si cerca in quelle fonti. La sezione 2 "LA LEGGE"
  impone di dichiarare un vuoto di conoscenza quando l'Impero non sa qualcosa, ma **non
  distingue mai** tra "non lo sa" e "non ho trovato le parole giuste per cercarlo" — il gap
  esatto descritto dal brief.
- **Verifica indipendente sulla wiki reale** (non solo riuso del `video-analysis.md`):
  `find second-brain-vault/wiki -iname "*.md" | wc -l` conferma l'ordine di grandezza
  1.831 pagine; nessun file di configurazione plugin Obsidian (`.smart-env/`,
  `smart-connections`) trovato nella wiki DE; nessun riferimento a Qdrant/Pinecone/pgvector in
  `second-brain-vault/`. La ricerca sulla wiki DE oggi è quindi confermata **lessicale**
  (nome file, wikilink, grep) — non semantica.

**Verdetto**: gap reale su entrambi i fronti, confermato prima di scrivere qualunque riga.

---

## Stage E — Gate (permission-guard)

Entrambe le patch sono **additive**: `git diff --numstat` → **+16 / 0** su
`conoscenza-empire.md` e **+13 / -1** su `sync-wiki-totale/SKILL.md` (la sola "cancellazione"
è la rinumerazione del marcatore di lista da "4." a "5." per lo step "Report finale
all'utente", dovuta all'inserimento di un nuovo step 4 in mezzo — nessun contenuto esistente è
stato rimosso o riscritto).

- La patch a `sync-wiki-totale` **non sostituisce** il formato di report esistente: aggiunge
  un nuovo step 4 (valutazione maturità) prima del vecchio step "Report finale" (ora step 5) e
  una nuova riga dentro il template di report esistente, senza toccare le righe precedenti
  (Checkpoint/ADR/Knowledge Memory Empire/Pagine/GAP residuo restano identiche).
- La patch a `conoscenza-empire.md` **non contraddice** la Legge #1 (§2, "non inventi... se
  l'Impero non sa una cosa, la risposta è 'Digital Empire non ha conoscenza su questo'") — la
  **estende** con un passo preliminare esplicito ("prova più di una formulazione prima di
  dichiarare il vuoto"), coerente con lo spirito già presente nella sezione 4 "COME RISPONDI"
  ("Prima cerchi, poi parli").
- **Attribuzione in linea obbligatoria**: ogni aggiunta porta
  `(fonte: DTCyvo6cC54 — Nate Herk, mm:ss)`.
- **Anti-overfitting**: fonte singola (un video, un autore). Entrambe le aggiunte sono scritte
  come regola operativa falsificabile (una scala con criteri osservabili; un passo di verifica
  con azione concreta "prova sinonimi"), non come claim di efficacia generale.

**Riserva registrata**: la scala a 5 livelli è una tassonomia proposta da un singolo creator
(Nate Herk), non uno standard di settore. È stata trattata nelle patch esplicitamente come
"scala Nate Herk" (mai presentata come standard universale), per non far passare un'opinione
di un autore come un fatto oggettivo dell'Impero.

---

## Stage F — Patch applicate (2 file, 2 blocchi, +29 righe, 0 cancellazioni di contenuto)

### 1. `.claude/skills/sync-wiki-totale/SKILL.md` — +12 righe nette (+13/-1, rinumerazione)

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| Il report MATCH/GAP contava pagine/checkpoint/ADR ma non diceva mai **a che livello di retrieval** sta un'area della wiki | Nuovo step 4: valutazione del livello di maturità per area sulla scala a 5 livelli del video (1=file organizzati, 2=wiki curata con router, 3=ricerca semantica, 4=knowledge graph, 5=processi always-on), con criterio esplicito "non giudica la qualità dei contenuti, dice quando conviene salire di livello" | KA-001, KA-009, KA-019, KA-027, KA-038, KA-041 |
| Il template di report finale non aveva una riga per questa dimensione | Nuova riga nel template: `Livello di maturita' (scala Nate Herk 1-5) per area sincronizzata: [area]: livello N — [motivo breve]` | KA-041, KA-042 |

### 2. `.claude/agents/conoscenza-empire.md` — +16 righe, 0 cancellazioni

Nuovo box "⚠️ Onestà epistemica — la ricerca su 1.800+ pagine è oggi lessicale, non
semantica", inserito nella sezione 3 "COSA POSSIEDI" subito dopo il box esistente "⚠️ Trappola
nota — B-033" (stesso stile di callout, stesso livello di importanza):

| Gap nell'agente (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| Nessuna qualificazione di **come** si cerca nelle fonti #1/#2 (lessicale vs semantica) | Dichiarazione esplicita: 1.831+ pagine cercabili solo per nome file/wikilink/parola esatta, nessuna ricerca per significato | KA-018, KA-019, KA-024 |
| La Legge #1 ("non inventi, dichiara il vuoto") non distingueva "vuoto reale" da "termine sbagliato" | Regola operativa: prima di dichiarare un vuoto, provare più di una formulazione (sinonimi, IT/EN, nome esatto vs descrizione) — esempio diretto dal video: `"posting frequency"` → 0 risultati lessicali su una nota che dice `"content cadence"` | KA-019 |

**Line endings verificati e preservati**: entrambi i file erano **LF-only** prima della patch
(verificato con conteggio binario `\r\n` vs `\n`-only) e sono rimasti LF-only dopo — usato lo
strumento Edit standard, nessuna conversione di line ending introdotta (confermato con lo
stesso script di conteggio eseguito prima e dopo).

---

## Skill/agenti NON toccati, con motivazione

Il brief vietava esplicitamente di toccare qualunque altra skill o agente: *"Nessun'altra
skill o agente va toccato."* Rispettato: nessun terzo file letto per modifica, nessuna terza
skill valutata per patch. Le uniche altre letture in questa sessione sono state di sola
consultazione (struttura archivio `yJOCyyP77bA`/`E8Ax92etrMc` per convenzione, wiki
`index.md`/`log.md` per lo Stage H) — mai scritte.

---

## Stage H — Sintesi

**Artefatti valutati:** 2/2 (`sync-wiki-totale`, `conoscenza-empire`), entrambi reali e
patchati.
**Totale:** +29 righe nette, **0 cancellazioni di contenuto** (1 rinumerazione di marcatore di
lista in `sync-wiki-totale`, non una rimozione di contenuto).
**Line endings preservati:** entrambi i file erano LF-only e sono rimasti LF-only.

**Cosa era già coperto e non è stato duplicato:**
- `conoscenza-empire.md` §4 "COME RISPONDI" già istruiva "Prima cerchi, poi parli" — la nuova
  patch non ripete questo principio, lo specializza sul caso "ricerca lessicale che fallisce
  non è prova di vuoto".
- `sync-wiki-totale` già aveva un passo di verifica pagine orfane (cross-link) — non toccato,
  la patch aggiunge una dimensione ortogonale (maturità di retrieval, non completezza del
  grafo).

**Tensione aperta:** nessuna. Entrambe le patch sono dichiarazioni operative falsificabili,
non giudizi di valore.

---

## Backlog registrato (proposte, non costruite)

- **B-040** — Ricerca semantica sulla wiki (salto al Livello 3). Plugin Obsidian "Smart
  Connections", gratuito, $0, locale. Impatto diretto su `conoscenza-empire` (che oggi può
  dichiarare un vuoto che è solo un termine mancato). Origine: DTCyvo6cC54.
- **B-041** — Logica di pruning della wiki (two-bucket: cosa resta consultabile, cosa si
  archivia). Origine: DTCyvo6cC54.

Entrambe scritte in `company/Memory/BACKLOG.md` come proposte da approvare da Max, non come
lavoro fatto.

---

## Tracciabilità

- Contenuto integrale: `memory-empire/knowledge/DTCyvo6cC54/contenuto-integrale.md`
- Atoms: `memory-empire/knowledge/DTCyvo6cC54/atoms.json` (55 KA, ognuno con `trace` =
  `DTCyvo6cC54#mm:ss + frames/frame-NNN.png`)
- Manifest: `memory-empire/knowledge/DTCyvo6cC54/ingest-manifest.json`
- Analisi visiva: `empire-studio/runs/max17-v08-herk-brain/video-analysis.md` — coverage
  130/130 frame unici, NO-FINTO PASS
- Coverage report: `empire-studio/runs/max17-v08-herk-brain/coverage.md`
- Audit Stage G: `memory-empire/memory/audit/2026-09-02-DTCyvo6cC54-stage-g.md`
- Log ingestione: `memory-empire/memory/ingestions/2026-09-02-nate-herk-second-brain-levels.md`
- Wiki: `second-brain-vault/wiki/sources/Source_Nate_Herk_Claude_Second_Brain_Levels.md`
