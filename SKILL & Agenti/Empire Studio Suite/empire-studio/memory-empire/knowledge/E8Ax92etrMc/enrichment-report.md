# Enrichment Report — E8Ax92etrMc

**Video:** "Steal My Claude Code Keyword Research System to Rank #1 on Google" — Nico | AI Ranking (13m20s, EN)
**Run:** `empire-studio/runs/max17-v03-nico-seo`
**Stage C-H eseguiti:** 2026-09-02 (pipeline Empire Studio Stage 1-5 dello stesso giorno)
**Atoms disponibili:** 58 KA — 27 alta rilevanza DE, 27 media, 4 bassa

---

## Stage D — Relevance / Gap / Scout

### Perimetro valutato

Sei skill SEO di Digital Empire, lette integralmente prima di qualsiasi giudizio:

| Skill | Righe | Dominio posseduto |
|---|---:|---|
| `.claude/skills/ai-seo/SKILL.md` | 485 | AEO/GEO, citabilita' su motori AI, struttura estraibile, fan-out |
| `.claude/skills/seo-audit/SKILL.md` | 497 | Audit tecnico + on-page + qualita' contenuto, keyword targeting |
| `.claude/skills/programmatic-seo/SKILL.md` | 238 | Pagine a scala, 12 playbook, validazione della domanda |
| `.claude/skills/site-seo/SKILL.md` | 438 | Iniezione meta tag/OG/JSON-LD, sitemap, robots, heading audit |
| `.claude/skills/schema/SKILL.md` | 179 | Structured data, JSON-LD, rich results |
| `.claude/skills/market-seo/SKILL.md` | 487 | Audit SEO di una pagina/sito per il cliente, content gap analysis |

### Verdetto per skill

| Skill | Verdetto | Motivo |
|---|---|---|
| `ai-seo` | **BERSAGLIO PRIMARIO** | Possiede gia' una sezione "Query Fan-Out" ma **solo concettuale** (*"brainstorm the 5-10 related queries"*). Non dice che il fan-out e' un dato recuperabile, non ha la soglia sul numero di sezioni, non ha la lettura competitiva "currently cited", non ha il routing formato. 1 patch strutturata |
| `market-seo` | **BERSAGLIO SECONDARIO** | Step 6 "Content Gap Analysis" cita gia' PAA e related searches, ma si ferma li' e gatea tutto sulla colonna "Search Volume Potential". Mancano Reddit, recensioni proprie+competitor, autocomplete, e la gap analysis 1-2 stelle vs 5 stelle. 1 patch |
| `programmatic-seo` | **BERSAGLIO TERZIARIO** | "Validate demand: aggregate search volume / volume distribution / trend direction" e' l'unico gate. Il video mostra che quel gate scarta ~40% delle domande reali. 1 patch di calibrazione |
| `seo-audit` | **PATCH MINORE** | "Site-Wide: No major gaps in coverage" e' un check senza metodo: con un keyword tool il gap non e' falsificabile. 1 patch |
| `site-seo` | **NESSUN ARRICCHIMENTO NECESSARIO** | Vedi motivazione sotto |
| `schema` | **NESSUN ARRICCHIMENTO NECESSARIO** | Vedi motivazione sotto |

---

## Stage E — Gate (permission-guard)

Tutte e 4 le patch sono **additive**: `git diff --numstat` su `.claude/skills/` restituisce **+70 / -0**. Nessuna riga preesistente rimossa, riscritta o contraddetta in silenzio.

Dove il video **tende contro** la skill, la patch e' scritta come **calibrazione dichiarata accanto alla regola originale**, che resta leggibile:
- `programmatic-seo` "Validate demand: aggregate search volume" → la patch non nega il gate, lo circoscrive ("volume is a filter, not the whole gate": giusto per il *pattern*, sbagliato per le *pagine dentro* il pattern) e aggiunge subito il freno anti-thin-content (soglia AI Overview 2+ sezioni), coerente col principio 5 "Quality Over Quantity" gia' presente.
- `market-seo` colonna "Search Volume Potential" → la patch aggiunge una nota di lettura, non riscrive il template della tabella.

**Nota anti-overfitting (regola di run):** tutte le patch portano in linea l'attribuzione `(fonte: E8Ax92etrMc — Nico | AI Ranking, mm:ss)`. E' una **fonte singola, non replicata**, e per di piu' una fonte che vende un proprio prodotto (skill in zip + community + corso). Nessun principio da questo video e' stato presentato come verita' generale della skill.

**Riserva esplicita registrata:** il video **non mostra alcun risultato di ranking o traffico** a supporto dell'efficacia del metodo. Le soglie numeriche (2+ sezioni AI Overview, gap 1-2 vs 5 stelle) sono euristiche dichiarate dall'autore, non risultati misurati. Sono state patchate perche' **operative e falsificabili**, non perche' dimostrate.

---

## Stage F — Patch applicate (4/4)

### 1. `ai-seo/SKILL.md` — +27 righe, 0 cancellazioni

Inserite in coda alla sezione **"Query Fan-Out (Google AI Search)"**, subito dopo la riga `**Action**: ...brainstorm the 5-10 related queries...`.

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| Il fan-out era solo da **immaginare** ("brainstorm the 5-10 related queries") | Nuovo blocco `#### Retrieving the fan-out instead of guessing it`: la struttura a sezioni dell'AI Overview e' **esposta come dato** dalle SERP API (DataForSEO "AI Overview structure"), insieme a PAA, autocomplete e related searches. Tabella con le tre cose che il dato restituisce e che un brainstorm non da' | KA-029, KA-030 |
| Nessuna soglia per decidere **paragrafo FAQ vs pagina propria** | Soglia esplicita: 1 blocco = risposta da paragrafo; **2+ sezioni = ha guadagnato una pagina propria**. Esempio riportato: `metal roof vs shingle?` in 4 sezioni | KA-031, KA-034 |
| Nessuna lettura competitiva per singola domanda | Il box **"currently cited"** dell'AI Overview e' il set competitivo reale per quella risposta — spesso diverso da chi ranka | KA-030 |
| Nulla sulle domande a **volume zero**: la skill dice solo "long-tail intent matters less than topical authority" | Il volume zero non e' motivo di scarto (15/37 nel dataset pubblicato) + le due convenzioni di lettura `0` vs `n/a` (Google Ads rifiuta keyword sopra le dieci parole, che e' la forma di una domanda vera) | KA-022, KA-043 |
| Nessuna regola di **routing formato** | Nuovo blocco `#### Routing a question to a format`: tabella a 4 destinazioni (FAQ terminale / FAQ che linka fuori / pagina propria / video) con criterio e razionale per ciascuna, piu' la verifica manuale della SERP video-dominata prima di scegliere il formato video | KA-032, KA-033, KA-034, KA-035, KA-045, KA-023 |

### 2. `market-seo/SKILL.md` — +27 righe, 0 cancellazioni

Inserite in coda allo **Step 6 — Content Gap Analysis**, dopo il "Content Gap Template".

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| Il gap analysis usava **due sole fonti Google** (PAA + related searches) | Nuovo blocco `#### Customer-language mining`: tabella con Reddit (incluso il fallback `site:reddit.com` e la penalita' dichiarata di perdere i comment count), recensioni Google proprie **e di fino a 5 competitor**, autocomplete. Piu' il passaggio di **deduplica in "canonical questions"** prima di entrare nella tabella dei gap | KA-003, KA-024, KA-025, KA-026, KA-028, KA-043 |
| La colonna "Search Volume Potential" gateava tutto | Calibrazione: volume zero non squalifica la riga; distinzione `0` vs `n/a`; e il freno — una riga a volume zero merita spesso una FAQ, quasi mai una pagina propria | KA-022, KA-043 |
| Le recensioni comparivano solo come segnale di **Trustworthiness** (E-E-A-T), mai come **fonte di contenuto** | Nuovo blocco `#### Gap analysis sulle recensioni`: gap ampio tra share 1-2 stelle e share 5 stelle = differenziatore da mettere in pagina; gap stretto = table stakes. Esempi reali dal dataset (15,9% vs 3,5% "stood behind the work" = ampio; 4,5% vs 6,6% "cleaned up after themselves" = stretto) + avvertenza sul campione piccolo, da dichiarare nel report | KA-041, KA-042 |

### 3. `programmatic-seo/SKILL.md` — +4 righe, 0 cancellazioni

Inserite sotto **"1. Keyword Pattern Research → Validate demand"**.

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| "Validate demand: aggregate search volume / volume distribution / trend direction" era l'unico gate, applicato indistintamente a pattern e pagine | Calibrazione dichiarata: il volume e' il test giusto per il **pattern**, sbagliato per le **pagine dentro** il pattern. Le domande da customer language tornano spesso a 0 e vanno comunque coperte. Convenzioni `0` vs `n/a` | KA-022, KA-043 |
| Rischio che la calibrazione produca thin content, contro il principio 5 della skill | Freno esplicito nella stessa patch: **non** tutte le domande a volume zero meritano un URL. Il taglio e' la struttura dell'AI Overview — blocco singolo = voce FAQ su pagina esistente; 2+ sezioni = pagina propria | KA-034, KA-031 |

### 4. `seo-audit/SKILL.md` — +12 righe, 0 cancellazioni

Inserite sotto **"Keyword Targeting → Site-Wide"**.

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| "No major gaps in coverage" e' un check **non falsificabile** con un keyword tool: il tool mostra solo i termini che hanno volume | Nuovo blocco `**Customer-language coverage**` con tabella a 3 fonti (thread Reddit di nicchia; recensioni Google proprie e dei competitor; PAA/autocomplete/related) e la domanda di verifica per ciascuna | KA-003, KA-024, KA-025, KA-026 |
| Nessuna indicazione su come **riportare** un finding a volume zero senza che venga letto come "nessuna domanda" | Il finding a volume zero e' un risultato d'audit legittimo (la domanda non risposta costa la vendita, e la coppia domanda-risposta e' la forma che i motori AI citano) + obbligo di distinguere `0` da `n/a` nel report | KA-022, KA-032, KA-043 |

---

## Skill NON arricchite, con motivazione

### `site-seo` — nessun arricchimento necessario

La skill fa **iniezione tecnica su contenuto gia' deciso**: meta tag, Open Graph, Twitter Card, JSON-LD (inclusa `FAQPage`), sitemap.xml, robots.txt, audit gerarchia heading, performance check. Il suo perimetro dichiarato e' *"SEO tecnica e on-page pulita"*, non la scelta di quali contenuti esistano.

Il video non aggiunge nulla su questo perimetro: non tocca meta tag, non tocca markup, non tocca sitemap o robots. L'unico punto di contatto e' che il video decide **quali domande** finiscono nel blocco FAQ di una service page — ma quella e' una decisione di content strategy, che in Digital Empire e' posseduta da `ai-seo` (dove infatti la patch e' stata applicata) e non da `site-seo`, che si limita a generare la `FAQPage` per una sezione FAQ gia' esistente. Patchare qui avrebbe duplicato la regola in due skill con owner diversi.

### `schema` — nessun arricchimento necessario

La skill copre `FAQPage`, `HowTo`, `ItemList`, `Article`, `Product`, `Review/AggregateRating`, validazione e implementazione per stack. Il video **non parla mai di structured data**: non mostra markup, non nomina schema.org, non discute rich results.

L'unica connessione possibile sarebbe "usa `FAQPage` per le FAQ che il routing produce" — ma e' gia' interamente coperto dalla riga esistente `FAQPage | FAQ content | mainEntity (Q&A array)`. Sarebbe un miglioramento inventato per giustificare il lavoro. Nessuna patch.

### Fuori perimetro (non valutate per vincolo di sessione)

`content-strategy`, `market-report`, `market-report-pdf`, `competitor-profiling`, `cro-copy-architect` e le altre skill non-SEO **non** sono state toccate: il perimetro di questa sessione era esplicitamente limitato alle sei skill SEO sopra. Due opportunita' reali restano quindi **aperte e non applicate**, registrate qui perche' non vadano perse:

1. Il template di deliverable **"Site Plan from Customer Language"** (10 sezioni, ricostruito integralmente in `contenuto-integrale.md` Parte 3) e' clonabile come sezione opzionale degli audit cliente di `market-report` / `market-report-pdf`. Leva commerciale concreta: differenzia da un audit SEO basato solo su Ahrefs/Semrush.
2. **Zernio** (`mcp.zernio.com/mcp`, 2 account gratis) come connettore MCP Reddit e' trasversale: oltre alla SEO alimenterebbe il reparto Competitor Research e l'Outreach. Decisione di stack, non un arricchimento di skill — va in backlog, non in patch.

---

## Stage H — Sintesi

**Skill valutate:** 6. **Patchate:** 4 (`ai-seo` +27, `market-seo` +27, `programmatic-seo` +4, `seo-audit` +12). **Non toccate:** 2 (`site-seo`, `schema`), con motivazione sopra.
**Totale:** +70 righe, **0 cancellazioni** (verificato su `git diff --numstat`).
**Line endings preservati:** `market-seo` era CRLF ed e' rimasto CRLF; le altre tre erano LF e sono rimaste LF — errore tecnico gia' registrato nella sessione del 2026-09-01 (video `j4UInmM9kKA`) e non ripetuto qui.

**Cosa era gia' coperto e non e' stato duplicato:**
- La tesi "non ranki per una keyword, ranki per il topic" (KA-054) e' gia' in `ai-seo` (§Query Fan-Out: *"Single-page-per-keyword targeting is less effective. Cover the full topical cluster"*) e in `programmatic-seo` (topic clustering). **Conferma esterna, non conoscenza nuova.**
- Le 5 regole della "Lesson 6" (domande reali come H2/H3, claim con fonte linkata, esperienza propria, 1-2 tabelle, link interni) sono gia' tutte in `ai-seo` (Pillar 1 Structure + Pillar 2 Authority + Princeton GEO table). **Nessuna patch.** E per di piu' provengono da un corso separato, con un flusso diverso (ChatGPT + DataWise), citato di sfuggita in 20 secondi.
- Reddit come **canale di presenza** e' gia' in `ai-seo` Pillar 3 (*"Reddit discussions (1.8% of ChatGPT citations)"*). Il video lo usa come **fonte di estrazione**, che e' un uso diverso — ed e' esattamente per questo che la patch e' andata in `market-seo`/`seo-audit` (dove si cercano i gap) e non in Pillar 3.

**Tensione aperta:** nessuna nuova. Resta la riserva di Stage E — fonte singola, autopromozionale, senza prove di ranking.

---

## Tracciabilita'

- Contenuto integrale: `memory-empire/knowledge/E8Ax92etrMc/contenuto-integrale.md` (41 KB — trascrizione audio deduplicata con timestamp + trascrizione visiva verbatim dei 400 frame)
- Atoms: `memory-empire/knowledge/E8Ax92etrMc/atoms.json` (58 KA, ognuno con `trace` = `video-id#timestamp + frames/frame-NNN.png`)
- Manifest: `memory-empire/knowledge/E8Ax92etrMc/ingest-manifest.json`
- Analisi visiva: `empire-studio/runs/max17-v03-nico-seo/video-analysis.md` — coverage 400/400, NO-FINTO PASS
- Coverage report: `empire-studio/runs/max17-v03-nico-seo/coverage.md`
- Audit Stage G: `memory-empire/memory/audit/2026-09-02-E8Ax92etrMc-stage-g.md`
- Log ingestione: `memory-empire/memory/ingestions/2026-09-02-nico-ai-ranking-keyword-research-claude.md`
- Wiki: `second-brain-vault/wiki/sources/Source_Nico_AI_Ranking_Claude_Keyword_Research.md`
