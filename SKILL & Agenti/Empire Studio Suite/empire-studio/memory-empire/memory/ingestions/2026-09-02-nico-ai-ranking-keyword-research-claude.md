# Ingestion Log — E8Ax92etrMc

**Data:** 2026-09-02
**Video:** "Steal My Claude Code Keyword Research System to Rank #1 on Google" — Nico | AI Ranking, 13m20s, EN
**Run:** `empire-studio/runs/max17-v03-nico-seo` (batch max17, v03)
**Tipo:** CHIUSURA CICLO — pipeline Empire Studio Stage 1-5 gia' eseguita oggi, Memory Empire Stage C-H mai eseguito.

## Cosa e' successo davvero

Analisi visiva completa gia' su disco: `video-analysis.md` da 37 KB, 400/400 frame letti con Read nativo (`--interval 2`), 58 atoms, `coverage.md` che certifica coverage 100% e NO-FINTO PASS. Il gap era **interamente a valle**: nessuna cartella `memory-empire/knowledge/E8Ax92etrMc/`, nessuna pagina wiki, nessun log. Per RULES §1 il video **non era "fatto"**.

Stesso pattern gia' registrato il 2026-09-01 per `j4UInmM9kKA` (cat2-marketing 4/15): pipeline completata, layer Memory Empire e wiki mai chiusi. Vale la pena leggerlo come pattern di batch, non come incidente isolato: la pipeline si ferma allo Stage 5 e nessuno chiude C-H.

## Pipeline eseguita oggi

- **Nessuna nuova visione dei frame.** `video-analysis.md`, `atoms.json` e `coverage.md` riusati integralmente.
- VTT ri-processato per intero con dedup riga-per-riga **conservando i timestamp** (385 righe uniche da 3080 grezze) — stesso metodo del video `j4UInmM9kKA`, artefatto intermedio salvato come `transcript_dedup_ts.md` nella run.
- **Stage C:** `contenuto-integrale.md` 41 KB / 408 righe — trascrizione audio integrale + trascrizione visiva verbatim dei 400 frame (card, UI Zernio, lista skill, prompt esatto, anatomia completa del report con tutte le tabelle e i numeri) + template del deliverable + tabella tool + metodo con soglie + "cosa non si vede". Mai riassunta.
- **Stage C:** 58 atoms normalizzati allo schema Memory Empire + manifest completo.
- **Stage D-H:** enrichment research su 6 skill SEO, 4 patch, audit, wiki.

## Scelta dell'archivio (deviazione dal brief, dichiarata)

Il brief indicava due percorsi candidati. Verificati entrambi: esistono ma sono **archivi storici fermi al 2026-07-09** (6 e 2 video). L'archivio vivo e' un terzo, non elencato: `empire-studio/memory-empire/knowledge/` — **52 cartelle**, ultimo aggiornamento 2026-09-01, accanto a `runs/`, contiene tutti gli Andrei Pascu e le lezioni cs2online. Archiviato li'.

Mirror a `.claude/skills/empire-studio/memory-empire/` **NON allineato**: sono due copie fisiche separate, non un symlink (verificato), e il vincolo di sessione vietava di toccare skill diverse dalle sei SEO. Da oggi il mirror ha 52 cartelle contro 53. Rischio strutturale ricorrente, candidato ad ADR.

## Enrichment — esito

**4 patch applicate, 0 cancellazioni** (`git diff --numstat -- .claude/skills/` → **+70 / -0**).

- `ai-seo/SKILL.md` — **+27**: due blocchi nuovi in coda a "Query Fan-Out". (a) Il fan-out e' un **dato recuperabile** (AI Overview structure via SERP API), non un brainstorm; **soglia formato 1 blocco = FAQ / 2+ sezioni = pagina propria**; box "currently cited" come set competitivo reale; volume zero non e' motivo di scarto (15/37) + convenzioni `0` vs `n/a`. (b) Tabella di **routing a 4 destinazioni** (FAQ terminale / FAQ che linka fuori / pagina propria / video) con verifica manuale della SERP video-dominata.
- `market-seo/SKILL.md` — **+27**: due blocchi nuovi in coda allo Step 6 Content Gap Analysis. (a) **Customer-language mining**: Reddit (col fallback `site:reddit.com` e la sua penalita'), recensioni Google proprie **e di fino a 5 competitor**, autocomplete, deduplica in canonical questions, calibrazione della colonna volume. (b) **Gap analysis sulle recensioni**: gap ampio 1-2 stelle vs 5 stelle = differenziatore, gap stretto = table stakes, con avvertenza sul campione piccolo.
- `programmatic-seo/SKILL.md` — **+4**: calibrazione di "Validate demand" (il volume e' il gate giusto per il *pattern*, sbagliato per le *pagine dentro* il pattern) con il proprio freno anti-thin-content (soglia AI Overview).
- `seo-audit/SKILL.md` — **+12**: blocco "Customer-language coverage" sotto Keyword Targeting → Site-Wide, perche' "no major gaps in coverage" non e' falsificabile con un keyword tool.

**Non arricchite, dichiarato:**
- `site-seo` — opera su contenuto gia' deciso (meta tag, JSON-LD, sitemap, robots). Il video non tocca nulla di quel perimetro; la decisione su *quali* FAQ mettere in pagina e' content strategy, posseduta da `ai-seo`, dove la patch e' andata.
- `schema` — il video **non parla mai di structured data**. L'unica connessione immaginabile e' gia' coperta dalla riga `FAQPage | FAQ content | mainEntity (Q&A array)`.

**Gia' coperto, non duplicato:** la tesi "topic non keyword" (gia' in `ai-seo` §Query Fan-Out e in `programmatic-seo`); le 5 regole della "Lesson 6" (gia' tutte fra Pillar 1, Pillar 2 e tabella Princeton GEO di `ai-seo`); Reddit come canale di presenza (gia' in Pillar 3 — il video lo usa come fonte di estrazione, uso diverso, patchato altrove).

## Riserva sulla fonte

Fonte **singola, non replicata, autopromozionale**: l'autore vende la skill in zip, la community e un corso. E soprattutto: **il video non mostra alcun risultato di ranking o traffico** a supporto del metodo, si chiude sui numeri di esecuzione del report (righe, commenti, recensioni, costo). Le soglie patchate (2+ sezioni AI Overview, gap recensioni) sono euristiche dichiarate, non misurate. Patchate perche' operative e falsificabili — con attribuzione in linea su ogni riga aggiunta.

**Secondo difetto della fonte, registrato:** il report scorso in dettaglio nel video ("Roofing, Dallas, Texas") **non e' l'output del prompt digitato in demo** ("plumbing market in Austin, Texas"). I numeri della card finale sono diversi da quelli del report mostrato. Il report va letto come repertorio didattico, non come prova di esecuzione. Marcato come inferenza in `video-analysis.md` e come KA-056.

## Difetto tecnico evitato

Line endings verificati prima e dopo ogni patch: `market-seo` era CRLF ed e' rimasto CRLF, le altre tre erano LF e sono rimaste LF. E' esattamente l'errore registrato il 2026-09-01 su `lead-magnets/SKILL.md` (conversione LF→CRLF che gonfio' il diff a 646 righe apparenti) — **non ripetuto**.

## Esito

58 knowledge atoms. 6 skill valutate, 4 patchate, 2 dichiarate senza gap. 1 pagina wiki creata, 2 aggiornate. Gate PASS.

**Nessun commit git**, come da vincolo di sessione: il lavoro e' su disco e non tracciato.

## Debito aperto

- **RULES §6 non eseguito:** nessun checkpoint in `company/Memory/checkpoints/`, `STATO-EMPIRE.md` non aggiornato. Fuori perimetro di questa sessione.
- **Backlog:** valutare Zernio (`mcp.zernio.com/mcp`, 2 account gratis) come connettore MCP Reddit trasversale a SEO / Competitor Research / Outreach — decisione di stack, non patch.
- **Backlog:** clonare il template "Site Plan from Customer Language" (10 sezioni, in `contenuto-integrale.md` Parte 3) come sezione opzionale di `market-report` / `market-report-pdf`.
- **Backlog:** sync fra le due copie fisiche di `empire-studio/`.

## Prossimo passo

Batch max17 — le run `v04-trivellato`, `v05-jaye-agenticos`, `v06-belli-codex`, `v07-rizzo-prompt`, `v08-herk-brain` sono su disco **senza layer Memory Empire**. Stesso gap di questo video: da chiudere una per una.
