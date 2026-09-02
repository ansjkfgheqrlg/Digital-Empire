---
Type: SOURCE
Status: Active
Tags: #seo #ai-seo #geo #aeo #keyword-research #customer-language #fan-out #ai-overview #reddit #recensioni #dataforseo #zernio #mcp #claude-skills #nico-ai-ranking #max17
Created: 2026-09-02
Last updated: 2026-09-02
---

# Source: Nico | AI Ranking — Steal My Claude Code Keyword Research System to Rank #1 on Google

## Overview
Walkthrough di 13m20 di un sistema di keyword research costruito come **Claude Skill** che smette di partire dai keyword tool e parte invece da dove le domande dei clienti sono gia' scritte: Reddit, recensioni Google (proprie **e di fino a 5 competitor**), People Also Ask, autocomplete e fan-out queries. La tesi e' che **un terzo delle domande reali ha volume di ricerca zero** e i tool classici quindi non le mostrano affatto. L'output non e' una lista di keyword: e' un piano collegato in cui ogni domanda viene instradata a una destinazione precisa (FAQ terminale, FAQ che linka fuori, pagina propria, video), con l'evidenza che ha guadagnato quella riga. Video 3 del batch `max17`.

Il contributo che vale davvero per Digital Empire non e' il tool: e' **la trasformazione del fan-out da esercizio di brainstorming a dato recuperabile**, con una soglia operativa (numero di sezioni dell'AI Overview) che decide se una domanda merita un paragrafo o una pagina. Ha prodotto 4 patch reali su 6 skill SEO valutate.

## Dati Tecnici

- **Video ID:** E8Ax92etrMc
- **Durata:** 13m20s (800s)
- **Canale:** Nico | AI Ranking · **Lingua:** EN
- **Formato:** Screen share (Claude chat, Zernio, un report HTML scorso a lungo) + talking head PiP
- **Frame:** 400 @2s | **Frame letti: 400/400 — coverage 100%** | NO-FINTO: PASS
- **VTT:** 3080 righe grezze -> 385 righe uniche dopo dedup con timestamp conservati
- **KA:** 58 (27 alta rilevanza DE, 27 media, 4 bassa) | 57 osservati, 1 inferito
- **Processing:** pipeline Empire Studio 2026-09-02 · Memory Empire C-H 2026-09-02 (stessa sessione)
- **Run:** `empire-studio/runs/max17-v03-nico-seo`

## Il Sistema

```
5 FONTI DI "CUSTOMER LANGUAGE" (nessuna e' un keyword tool)
1. Reddit          — thread reali; se manca l'accesso API, fallback site:reddit.com
                     (funziona ma perdi i comment count: segnale di domanda piu' debole)
2. Recensioni Google — proprie E di fino a 5 competitor
3. People Also Ask  — l'espansione nativa di Google
4. Autocomplete     — le varianti reali di formulazione
5. Fan-out queries  — le sotto-domande che il motore AI si pone prima di rispondere,
                      recuperabili come "AI Overview structure"

      v  dedup in "canonical questions"
      v  classificazione su 2 assi

ASSE 1 — INTENTO:  transazionale (-> service page) vs informazionale (-> contenuto dedicato)
ASSE 2 — FORMATO:  4 destinazioni fisse, niente viene scartato
```

| Tag a schermo | Destinazione | Quando |
|---|---|---|
| `answered here` | FAQ terminale | Obiezione reale senza domanda propria. Nessuno ranka per essa, ma lasciarla senza risposta costa il lavoro — e la coppia domanda-risposta e' la forma che i motori AI citano |
| `links to full post` | FAQ che linka fuori | Obiezione che **ha anche** domanda. Risposta breve sulla pagina commerciale per sbloccare la vendita, poi link al pezzo intero |
| `post` | Pagina propria | La domanda ha domanda reale, **oppure** l'AI Overview spacca la risposta in 2+ sezioni: non si puo' rispondere in un paragrafo |
| `video` | Video | La risposta e' qualcosa che si mostra. Verifica prima sulla SERP se l'intento e' video-dominato |

## Le Soglie (la parte riusabile)

```
VOLUME ZERO NON E' MOTIVO DI SCARTO
15 domande canoniche su 37 (circa 40%) avevano volume Google zero.
Tutte e 15 venivano da qualcosa che un cliente aveva scritto davvero.

CONVENZIONI DI LETTURA — da portare in qualsiasi keyword sheet
  0    = interrogato, e genuinamente zero
  n/a  = NON interrogabile: Google Ads rifiuta keyword sopra le dieci parole,
         che e' esattamente la forma di una domanda vera

SEZIONI DELL'AI OVERVIEW = SOGLIA DI FORMATO
  1 blocco   -> risposta da paragrafo, va in FAQ
  2+ sezioni -> ha guadagnato una pagina propria
  Esempio: "metal roof vs shingle?" -> 4 sezioni
  (Cost & Installation / Lifespan & Durability / Energy Efficiency & Climate / Maintenance & Weight)
  "4 sections, so this is article-sized rather than a one-paragraph FAQ"

BOX "CURRENTLY CITED"
  L'AI Overview dice anche CHI sta citando oggi per quella domanda.
  E' il set competitivo reale della risposta — spesso diverso da chi ranka.

GAP RECENSIONI 1-2 STELLE vs 5 STELLE
  gap ampio  -> differenziatore: va detto esplicitamente in pagina
  gap stretto -> table stakes: metterlo in pagina non guadagna nulla
  Con 44 recensioni negative il campione e' piccolo: "direzione, non precisione"
```

## L'Output — template "Site Plan from Customer Language"

Documento a 10 sezioni, ricostruito integralmente in `contenuto-integrale.md` Parte 3:
header con fonti dichiarate -> contatori sommario -> box "N domande a volume zero" -> 4 colonne fonte con esempi -> routing per singola domanda con evidenza -> fan-out breakdown + currently cited -> legenda delle 4 categorie -> piano **pagina servizio per pagina servizio** (FAQ block + "linked from this page") -> tabella sentiment recensioni -> footer metodologico con le convenzioni di lettura.

E' un deliverable clonabile per gli audit cliente dell'agenzia CRO: differenzia da un audit SEO basato solo su Ahrefs/Semrush.

## Stack

| Tool | Ruolo | Costo |
|---|---|---|
| **Claude** (chat, Opus 5 effort High) | Esegue la skill, orchestra le chiamate MCP, produce il report | Piano con Skills + Connectors |
| **DataForSEO** | Reviews, PAA, autocomplete, related/fan-out, AI Overview structure, volumi | ~$0,59 a run (range dichiarato $0,50-$0,80) |
| **Zernio** `mcp.zernio.com/mcp` | Connettore MCP custom che da' a Claude accesso a Reddit (OAuth gestito) | **2 account collegati = gratis** |
| `keyword-language.zip` | La Claude Skill regalata in community — contenuto interno **mai mostrato** | Gratis |

Setup del connettore, verbatim: Claude -> Settings -> Customize -> Connectors -> Add new -> Add custom connector -> URL `mcp.zernio.com/mcp` -> Connect.

## Key Quotes

> "A third of the questions that your customers are actually asking have zero search volume. Not low, but zero."

> "The tools aren't wrong. They're incomplete. So you go somewhere else for the rest. It's already written down." [card a schermo]

> "You're not ranking for a keyword. You're ranking for the topic." [card finale]

> "Questions that are objections become FAQs on the service page that has to overcome them. Questions with real demand become their own page, linked from that FAQ. Questions that need showing rather than telling become videos. Nothing is discarded."

> "4 sections, so this is article-sized rather than a one-paragraph FAQ."

> "A wide gap between the two columns is a differentiator worth putting on the page. A narrow gap means it's table stakes and wins you nothing."

> "With only 44 reviews at 1-2 stars, the left column is a small sample and should be read as direction, not precision."

> "Once every 6 months will be great because you should get some new questions when they come up."

## Numeri Dichiarati

- Report d'esempio: 1.713 raw lines -> 37 canonical questions -> 26 FAQ + 14 blog post + 4 video; 941 recensioni lette
- **15 domande su 37 a volume di ricerca zero**
- 502 thread Reddit su 111 subreddit · 40 PAA · 150 autocomplete · 80 related/fan-out
- Recensioni: 941 on-topic da fino a 5 competitor (44 a 1-2 stelle, 880 a 5 stelle)
- Run reale ("The First Live Run"): 5.895 raw lines, 203.065 commenti Reddit, 1.404 recensioni, **$0,59**, **8 minuti**
- Cadenza consigliata: 1 run ogni 6 mesi per business

## Azione Concreta (Enrichment)

**6 skill SEO valutate, 4 patchate, +70 righe, 0 cancellazioni.**

- `ai-seo/SKILL.md` (**+27**) — due blocchi nuovi in coda a "Query Fan-Out", che prima diceva solo *"brainstorm the 5-10 related queries"*: il fan-out come **dato recuperabile** (AI Overview structure via SERP API) con la soglia 1 blocco = FAQ / 2+ sezioni = pagina propria, il box "currently cited" come set competitivo reale, il volume zero non-scartabile con le convenzioni `0` vs `n/a`; e la tabella di **routing a 4 destinazioni** con la verifica della SERP video-dominata.
- `market-seo/SKILL.md` (**+27**) — Step 6 Content Gap Analysis usava due sole fonti Google: aggiunte Reddit (col fallback e la sua penalita'), recensioni proprie e dei competitor, autocomplete, deduplica in canonical questions, calibrazione della colonna volume; piu' la **gap analysis sulle recensioni** (differenziatore vs table stakes) con l'avvertenza sul campione.
- `programmatic-seo/SKILL.md` (**+4**) — calibrazione di "Validate demand": il volume e' il gate giusto per il *pattern*, sbagliato per le *pagine dentro* il pattern; col proprio freno anti-thin-content (soglia AI Overview).
- `seo-audit/SKILL.md` (**+12**) — "No major gaps in coverage" non e' falsificabile con un keyword tool: aggiunte le tre fonti da controllare e la regola di riportare `0` distinto da `n/a`.

**NON arricchite, dichiarato:** `site-seo` (opera su contenuto gia' deciso — meta tag, JSON-LD, sitemap; il video non tocca quel perimetro, e la scelta di *quali* FAQ mettere in pagina e' posseduta da `ai-seo`) e `schema` (il video non parla **mai** di structured data; l'unica connessione immaginabile e' gia' coperta dalla riga `FAQPage | FAQ content | mainEntity`).

**Gia' coperto, non duplicato:** la tesi "topic non keyword" era gia' in `ai-seo` §Query Fan-Out e in `programmatic-seo`; le 5 regole della "Lesson 6" sono tutte gia' fra Pillar 1, Pillar 2 e la tabella Princeton GEO di `ai-seo`; Reddit come *canale di presenza* era gia' in Pillar 3 — il video lo usa come *fonte di estrazione*, uso diverso, patchato dove si cercano i gap.

Dettaglio in `memory-empire/knowledge/E8Ax92etrMc/enrichment-report.md`.

## Nota di trasparenza — due difetti della fonte, registrati

**1. Il report mostrato non e' l'output della demo.** Nico digita un prompt su *"the plumbing market in Austin, Texas"* (05:02), ma il report che scorre per i successivi 7 minuti e' intestato **"Roofing, Dallas, Texas"**, e la narrazione a 05:30 dice *"I specifically chose Texas and plumbing"* mentre lo schermo mostra "Roofing". I numeri della card finale (5.895 righe, 1.404 recensioni) sono diversi da quelli del report mostrato (1.713 / 941). Il report va letto come **repertorio didattico dell'anatomia del deliverable**, non come prova dell'esecuzione live. Anche il salto prompt -> report e' un taglio netto: nessuna chiamata MCP, nessun log, nessun ragionamento mostrato.

**2. Nessun risultato di ranking o traffico.** Il video si chiude sui numeri di *esecuzione* del report (righe, commenti, recensioni, costo), non su risultati di posizionamento. Le soglie patchate sono euristiche dichiarate dall'autore, non misurate. Fonte inoltre **singola e autopromozionale**: distribuisce la skill in zip attraverso la propria community gratuita e cita un proprio corso. Ogni riga aggiunta alle skill porta l'attribuzione in linea per questo motivo.

## Backlog aperto (registrato, non applicato)

- **Zernio** come connettore MCP Reddit e' trasversale: oltre alla SEO alimenterebbe Competitor Research e Outreach. Decisione di stack, non patch di skill.
- Il template **"Site Plan from Customer Language"** come sezione opzionale di `market-report` / `market-report-pdf` — fuori dal perimetro "solo skill SEO" di questa sessione.

## Connessioni

- [[Source_CS2_Bonus_03_Collegare_Claude]] — la lezione DE sui connettori MCP: stesso meccanismo (custom connector, permessi, URL remoto) che qui viene usato per dare a Claude l'accesso a Reddit via Zernio. Il video ne e' una applicazione reale e a costo quasi nullo
- [[Source_CS2_Bonus_04_Claude_Skills]] — struttura tecnica delle Claude Skills. `keyword-language.zip` e' esattamente quella forma, distribuita come zip da allegare in chat: piu' povera del sistema a 7 file che DE usa gia'
- [[Concept_Meta_Ads_Library_Competitor_Research]] — stesso movimento cognitivo su un'altra fonte pubblica: estrarre intelligence dai dati che i competitor lasciano visibili. Li' gli ads, qui le recensioni e i thread
- [[Source_Andrei_Pascu_Ads_Library_Live]] — il precedente DE di "un tool pubblico letto come corpus di ricerca", con lo stesso limite di fondo: chi insegna il metodo non mostra il risultato a valle
- [[Tool_Memory_Wiki_Bridge]] — il ponte per cui questa ingestione esiste come pagina invece che restare in `memory-empire/knowledge/`
