# Audit Log Stage G — E8Ax92etrMc

**Data:** 2026-09-02
**Operazione:** chiusura ciclo Memory Empire Stages C-H su video gia' analizzato
**Video:** "Steal My Claude Code Keyword Research System to Rank #1 on Google" — Nico | AI Ranking, 13m20s, EN
**Run sorgente:** `empire-studio/runs/max17-v03-nico-seo`
**Regola applicata:** `empire-studio/RULES.md` REGOLA 1 (Memory Empire obbligatorio post-ogni-video, Stages C-H)
**Vincolo di sessione:** nessun commit git. Solo scrittura file.

---

## Stato di partenza

Pipeline Empire Studio Stage 1-5 gia' completata il 2026-09-02: `video-analysis.md` (37 KB), `atoms.json` (58 KA), `coverage.md` (400/400 frame letti, NO-FINTO PASS), VTT scaricato. **Layer Memory Empire assente**: nessuna cartella `memory-empire/knowledge/E8Ax92etrMc/`, nessuna pagina wiki, nessun log di ingestione.

Stesso pattern gia' registrato per `j4UInmM9kKA` il 2026-09-01: analisi fatta, ciclo non chiuso a valle. Per RULES §1 il video **non era "fatto"**.

**Nessuna nuova visione dei frame.** Le fonti di questo lavoro sono `video-analysis.md`, `atoms.json`, `coverage.md` e il VTT — non i PNG.

---

## Scelta della cartella di archivio (deviazione dichiarata)

Il brief indicava di controllare in quest'ordine:
1. `C:/Users/Utente/.claude/skills/memory-empire/knowledge/` — **esiste**, 6 video, ultimo aggiornamento 2026-07-09
2. `SKILL & Agenti/Empire Studio Suite/memory-empire/knowledge/` — **esiste**, 2 video, 2026-07-09

Entrambe verificate. Entrambe sono **archivi storici fermi a luglio**. L'archivio vivo e' un terzo, non elencato nel brief:

**`SKILL & Agenti/Empire Studio Suite/empire-studio/memory-empire/knowledge/`** — **52 cartelle video**, ultimo aggiornamento 2026-09-01 (`j4UInmM9kKA`), e' la cartella accanto a `runs/` dove vive la run `max17-v03-nico-seo`, e contiene **tutti** i video Andrei Pascu cat1+cat2 e le lezioni cs2online. E' anche quella che i manifest recenti indicano come `memory-empire/knowledge/...`.

**Decisione:** archiviato li'. Il criterio del brief ("usa quella che esiste gia' e contiene altri video", "guarda come sono fatte le cartelle dei video Andrei Pascu gia' archiviati") punta univocamente a questa cartella. Archiviare in una delle due indicate avrebbe creato un quarto archivio parziale e scollegato dal run.

**Nota di stato per chi rilegge — MIRROR NON SINCRONIZZATO:** esiste un mirror a `.claude/skills/empire-studio/memory-empire/` con contenuto fino a ieri identico, ma **e' una copia fisica separata, non un symlink** (verificato con `os.path.realpath`). **Non e' stato allineato**: il vincolo di sessione vietava di modificare skill diverse dalle sei SEO, e `.claude/skills/empire-studio/` e' una skill. Da oggi il mirror ha 52 cartelle contro le 53 dell'archivio vivo. Il disallineamento fra i due percorsi e' un rischio strutturale ricorrente: candidato a ADR o a un hook di sync.

---

## Stage C — Archivio integrale

Creata `memory-empire/knowledge/E8Ax92etrMc/` con 4 file (convenzione identica alle cartelle Andrei Pascu: `contenuto-integrale.md` + `atoms.json` + `enrichment-report.md` + `ingest-manifest.json`):

| File | Dimensione | Contenuto |
|---|---:|---|
| `contenuto-integrale.md` | 41 KB / 408 righe | Parte 1: trascrizione audio integrale, VTT deduplicato riga-per-riga **con timestamp conservati** (385 righe uniche su 3080 grezze), in blocchi da 30s. Parte 2: trascrizione visiva verbatim dei 400 frame (card, UI Zernio, lista skill, prompt esatto, anatomia completa del report con tutte le tabelle e i numeri). Parte 3: template del deliverable a 10 sezioni. Parte 4: tabella tool. Parte 5: metodo integrale con soglie. Parte 6: cosa non si vede. **Mai riassunto** |
| `atoms.json` | 25 KB | 58 KA normalizzati allo schema Memory Empire (`id`, `categoria`, `claim`, `trace`, `confidenza`, `rilevanza_DE`). Ogni `trace` = `E8Ax92etrMc#mm:ss + frames/frame-NNN.png`. 27 alta / 27 media / 4 bassa rilevanza DE; 57 osservati / 1 inferito |
| `ingest-manifest.json` | 7 KB | id, titolo, canale, URL, durata, data ingestione, frame estratti/letti (400/400, interval 2, coverage 100%), dati VTT, path della run e di tutti gli output, key topics, numeri reali, tool citati, avvertenza metodologica, limiti dichiarati, stages completati |
| `enrichment-report.md` | 12 KB | Stage D-H documentato per esteso (vedi sotto) |

**Trascrizione dedup:** prodotto anche `runs/max17-v03-nico-seo/transcript_dedup_ts.md` (14,8 KB) come artefatto intermedio riutilizzabile.

---

## Stage D — Skill valutate: 6

Tutte e sei le `SKILL.md` sono state **lette integralmente** prima di formulare qualsiasi giudizio (2.324 righe complessive), non grep-ate:

| Skill | Righe lette | Verdetto |
|---|---:|---|
| `.claude/skills/ai-seo/SKILL.md` | 485 | Bersaglio primario |
| `.claude/skills/seo-audit/SKILL.md` | 497 | Patch minore |
| `.claude/skills/programmatic-seo/SKILL.md` | 238 | Bersaglio terziario |
| `.claude/skills/site-seo/SKILL.md` | 438 | **Nessun arricchimento necessario** |
| `.claude/skills/schema/SKILL.md` | 179 | **Nessun arricchimento necessario** |
| `.claude/skills/market-seo/SKILL.md` | 487 | Bersaglio secondario |

`market-seo` esiste (era dato per incerto nel brief): `.claude/skills/market-seo/SKILL.md`, 18.936 byte.

---

## Stage E — Gate

4 proposte, 4 approvate, 0 negate. Criteri di gate applicati:

- **Additive-only:** verificato a posteriori con `git diff --numstat -- .claude/skills/` → `+70 / -0`. Zero cancellazioni.
- **Nessuna contraddizione silenziosa:** dove il video tende contro una regola esistente (`programmatic-seo` "Validate demand: aggregate search volume"; `market-seo` colonna "Search Volume Potential") la patch e' scritta come **calibrazione dichiarata accanto** alla regola, che resta leggibile e non viene sostituita.
- **Anti-thin-content:** la calibrazione su `programmatic-seo` porta con se' il proprio freno (soglia AI Overview 2+ sezioni) per non entrare in conflitto col principio 5 "Quality Over Quantity" gia' presente nella skill.
- **Attribuzione in linea obbligatoria:** ogni aggiunta porta `(fonte: E8Ax92etrMc — Nico | AI Ranking, mm:ss)`.
- **Anti-overfitting:** fonte singola, non replicata, e autopromozionale (l'autore vende skill in zip + community + corso). Nessun principio presentato come verita' generale della skill.

**Riserva registrata:** il video non mostra **alcun** risultato di ranking o traffico (prima/dopo). Le soglie numeriche patchate sono euristiche dichiarate dall'autore, non risultati misurati. Approvate perche' **operative e falsificabili**, non perche' dimostrate. Questa riserva e' scritta anche in `enrichment-report.md`.

---

## Stage F — Patch applicate: 4 skill, +70 righe, 0 cancellazioni

| Skill | Righe | Punto di innesto | Aggiunta |
|---|---:|---|---|
| `ai-seo/SKILL.md` | **+27** | Coda della sezione "Query Fan-Out (Google AI Search)" | Due nuovi blocchi. `#### Retrieving the fan-out instead of guessing it`: il fan-out e' un **dato recuperabile** (AI Overview structure via SERP API) e non un brainstorm; tabella di cosa restituisce; **soglia formato: 1 blocco = FAQ, 2+ sezioni = pagina propria** (esempio `metal roof vs shingle?` in 4 sezioni); box "currently cited" come set competitivo reale; **volume zero non e' motivo di scarto** (15/37) + convenzioni `0` vs `n/a` (Google Ads rifiuta keyword oltre 10 parole). `#### Routing a question to a format`: tabella a 4 destinazioni (FAQ terminale / FAQ che linka fuori / pagina propria / video) con criterio e razionale, piu' la verifica manuale della SERP video-dominata |
| `market-seo/SKILL.md` | **+27** | Coda dello Step 6 "Content Gap Analysis", dopo il Content Gap Template | Due nuovi blocchi. `#### Customer-language mining`: le tre fonti mancanti oltre a PAA e related searches — Reddit (col fallback `site:reddit.com` e la sua penalita' dichiarata), recensioni Google proprie **e di fino a 5 competitor**, autocomplete; piu' la deduplica in "canonical questions"; piu' la calibrazione della colonna "Search Volume Potential". `#### Gap analysis sulle recensioni`: gap ampio 1-2 stelle vs 5 stelle = differenziatore da mettere in pagina, gap stretto = table stakes; esempi reali dal dataset; avvertenza sul campione piccolo da dichiarare nel report |
| `programmatic-seo/SKILL.md` | **+4** | Sotto "1. Keyword Pattern Research → Validate demand" | Calibrazione: il volume e' il gate giusto per il **pattern**, sbagliato per le **pagine dentro** il pattern (15/37 a volume zero, tutte da linguaggio cliente reale) + convenzioni `0` vs `n/a`; e il freno anti-thin-content: non tutte le domande a volume zero meritano un URL, il taglio e' la struttura dell'AI Overview |
| `seo-audit/SKILL.md` | **+12** | Sotto "Keyword Targeting → Site-Wide" | Nuovo blocco `**Customer-language coverage**`: "No major gaps in coverage" non e' falsificabile con un keyword tool; tabella a 3 fonti da controllare (thread Reddit di nicchia, recensioni proprie e dei competitor, PAA/autocomplete/related) con la domanda di verifica per ciascuna; un finding a volume zero e' un risultato d'audit legittimo; obbligo di distinguere `0` da `n/a` nel report |

**Line endings verificati e preservati:** `market-seo` era CRLF ed e' rimasto CRLF; `ai-seo`, `seo-audit`, `programmatic-seo` erano LF e sono rimasti LF. E' l'errore tecnico registrato il 2026-09-01 su `lead-magnets/SKILL.md` (conversione LF→CRLF che gonfio' il diff a 646 righe apparenti) — **non ripetuto**.

**Copie non toccate, deliberatamente:** esistono copie delle stesse skill in `Agency page/Clienti/marketingskills-main/skills/`, `Clienti/EXPONIUM/.agents/skills/`, `Crea siti/skills/` e `Agenti/Agency/skills/`. Sono deliverable cliente e snapshot, fuori dal perimetro. Patchate solo le copie vive in `.claude/skills/`.

---

## Skill NON toccate: 2

### `site-seo` — nessun arricchimento necessario
Perimetro dichiarato: *"SEO tecnica e on-page pulita"* — iniezione di meta tag, Open Graph, Twitter Card, JSON-LD (inclusa `FAQPage`), sitemap.xml, robots.txt, audit gerarchia heading, performance check. Opera su contenuto **gia' deciso**.
Il video non tocca meta tag, markup, sitemap o robots. L'unico punto di contatto e' *quali* domande finiscono nel blocco FAQ di una service page — decisione di content strategy, posseduta in Digital Empire da `ai-seo` (dove la patch e' andata) e non da `site-seo`, che si limita a generare la `FAQPage` per una sezione FAQ gia' esistente. Patchare qui avrebbe duplicato la stessa regola sotto due owner diversi.

### `schema` — nessun arricchimento necessario
La skill copre gia' `FAQPage`, `HowTo`, `ItemList`, `Article`, `Product`, `Review/AggregateRating`, validazione e implementazione per stack.
Il video **non parla mai di structured data**: nessun markup mostrato, schema.org mai nominato, rich results mai discussi. L'unica connessione immaginabile ("usa `FAQPage` per le FAQ prodotte dal routing") e' gia' interamente coperta dalla riga esistente `FAQPage | FAQ content | mainEntity (Q&A array)`. Sarebbe stato un miglioramento inventato per giustificare il lavoro.

---

## Cosa era gia' coperto e non e' stato duplicato

- **"Non ranki per una keyword, ranki per il topic"** (KA-054, la tesi centrale del video) e' gia' in `ai-seo` §Query Fan-Out (*"Single-page-per-keyword targeting is less effective. Cover the full topical cluster"*) e in `programmatic-seo` (topic clustering). Conferma esterna, non conoscenza nuova.
- **Le 5 regole della "Lesson 6"** (domande reali come H2/H3, claim con fonte linkata, esperienza propria, 1-2 tabelle, link interni) sono tutte gia' in `ai-seo` fra Pillar 1 Structure, Pillar 2 Authority e la tabella Princeton GEO. Provengono per di piu' da un corso separato con flusso diverso (ChatGPT + DataWise), citato in un aside di 20 secondi.
- **Reddit come canale di presenza** e' gia' in `ai-seo` Pillar 3. Il video lo usa come **fonte di estrazione**, uso diverso — ed e' per questo che la patch e' andata dove si cercano i gap (`market-seo`, `seo-audit`) e non in Pillar 3.

---

## Opportunita' reali NON applicate (fuori perimetro, registrate per non perderle)

1. **Template di deliverable "Site Plan from Customer Language"** (10 sezioni, ricostruito integralmente in `contenuto-integrale.md` Parte 3) — clonabile come sezione opzionale negli audit cliente di `market-report` / `market-report-pdf`. Leva commerciale: differenzia da un audit SEO basato solo su Ahrefs/Semrush. Fuori dal perimetro "solo skill SEO elencate" di questa sessione.
2. **Zernio** (`mcp.zernio.com/mcp`, 2 account gratis) come connettore MCP Reddit — trasversale a SEO, Competitor Research e Outreach. E' una decisione di stack, non un arricchimento di skill: va in `company/Memory/BACKLOG.md` o in un ADR, non in una patch.
3. **Sync `.claude/skills/empire-studio/` ↔ `SKILL & Agenti/Empire Studio Suite/empire-studio/`** — due copie fisiche separate, non un symlink, **oggi disallineate** (52 vs 53 cartelle). Non sanabile in questa sessione: il mirror sta dentro una skill e il perimetro vietava di toccare skill non-SEO.

---

## Stage H — Wiki

- **Creata:** `second-brain-vault/wiki/sources/Source_Nico_AI_Ranking_Claude_Keyword_Research.md` (stile e frontmatter delle pagine `Source_Andrei_Pascu_*` della stessa cartella, verificati su due esemplari prima della scrittura)
- **Aggiornata:** `second-brain-vault/wiki/index.md` (sezione Sources)
- **Aggiornata:** `second-brain-vault/wiki/log.md` (entry sotto `## 2026-09-02`)
- Cross-link verificati come esistenti prima di essere scritti.

---

## Esito

**58 knowledge atoms archiviati. 6 skill valutate, 4 patchate (+70 / -0), 2 dichiarate senza gap. 1 pagina wiki creata, 2 aggiornate. Gate PASS.**

**Nessun commit git eseguito**, come da vincolo di sessione. Il lavoro e' su disco e non tracciato: chi riprende deve committare o valutare esplicitamente.

**Conformita' RULES.md:**
- §1 Stages C-H: tutti eseguiti e documentati → PASS
- §2 NO-FINTO: nessun frame descritto senza essere stato letto; questa sessione non ha riletto frame, ha riusato `video-analysis.md` con coverage 400/400 gia' certificata → PASS
- §5 Tracciabilita' P12: ogni atom porta `video-id#timestamp + frames/frame-NNN.png` → PASS
- §6 company/Memory: **NON eseguito** — nessun checkpoint in `company/Memory/checkpoints/`, `STATO-EMPIRE.md` non aggiornato. Fuori dal perimetro di questa sessione (che vietava i commit). **Debito aperto e dichiarato.**
