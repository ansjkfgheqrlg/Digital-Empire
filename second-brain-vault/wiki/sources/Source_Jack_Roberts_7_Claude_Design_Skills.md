---
Type: SOURCE
Status: Active
Tags: #design #claude-design #ui-sniping #design-loop #copy #mobile #seo #jack-roberts #max17
Created: 2026-09-03
Last updated: 2026-09-03
---

# Source: Jack Roberts — "Insane Claude Design Skills You Actually Need To Build Beautiful Sites"

## Overview

Video di 22m56 (EN, batch `max17` v11) in cui l'autore mostra **sette skill operative** per
costruire siti che convertono, non solo che sono belli — tesi dichiarata in apertura: *"just
because your site looks pretty doesn't mean that it will sell or get customers."* I sette livelli
(Reference → Sitemap → Hero → Mobile → Copy → Dettagli UI → SEO) sono ognuno una coppia
strumento+prompt verbatim, dimostrata dal vivo sulla costruzione di un sito reale (Ridgeline, una
ditta di copertura tetti). Video chiuso a valle di uno stop di sessione: la visione dei 689 frame
e l'analisi erano già scritte su disco (`video-analysis.md`, 1199 righe, 67 atomi), mancava
`coverage.md` (scritto in questa sessione come Stage 5 di verifica) e i passi Stage 6-9.

Il contributo che vale davvero per Digital Empire non è "un altro modo di fare siti" — l'Impero
ha già `empire-premium-style`, `site-design`, `guild-design` (design system proprietario) più
maturi del metodo "prendi in prestito il design system di un altro sito" del video — ma **tre
pattern puntuali che mancano davvero**: l'invariante del **Design Loop** (il giudice non deve
condividere la memoria di chi ha costruito), la **tabella dei 6 "Signs of AI writing"** con
regola+esempio prima/dopo per ciascuno, e il numero operativo **390px** per l'audit mobile.
Tutti e tre verificati come gap reali prima di essere proposti (vedi sezione Consigli).

## Dati Tecnici

- **Video ID:** pUu4G2lINnk
- **Durata:** 22m56s (1376s)
- **Canale:** Jack Roberts · **Lingua:** EN · Pubblicato 2026-08-31, 40.429 visualizzazioni al
  momento dell'ingestione
- **Formato:** Talking head + deck HTML servito in locale (127.0.0.1:5497) + screen-share
  (refers.design, Relume, Claude Desktop, Higgsfield, Savee, 21st.dev, Flaticon, claude-seo,
  Vercel) + b-roll del "Claude Code OS" personale dell'autore
- **Frame:** 688 densi @2s → 270 unici sopra soglia (scene-detector 3.0, riduzione 60.8%) |
  **Frame citati per numero nel testo: 108/270 (40,0%)** | NO-FINTO: **PASS con copertura
  parziale dichiarata, con una discrepanza di conteggio dichiarata e non corretta silenziosamente**
  — l'intestazione originale di `video-analysis.md` dichiarava "182/270 guardati", numero che
  questa verifica non ha potuto confermare con citazioni tracciabili (P12): il numero verificato è
  108/270. Ogni capitolo ha comunque copertura non-zero. Dettaglio completo, capitolo per
  capitolo, in `coverage.md`.
- **KA:** 67 (atoms.json) — 66 osservati, 1 inferito (marcato `➕` e `inferito`)
- **Processing:** pipeline Empire Studio (sessione precedente, visione+analisi) · verifica Stage 5
  + Memory Empire Stage 6-9 (questa sessione, dopo interruzione per limite di sessione)
- **Run:** `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/max17-v11-roberts-design`

## I Sette Livelli — la struttura del metodo

Ogni livello segue lo stesso deck: eyebrow `SKILL 0N · CATEGORIA`, numero enorme, titolo +
citazione-regola, chip degli strumenti, striscia `LIVE DEMO`, frase-ponte al livello successivo —
un template di slide riusabile di per sé.

```
01 REFERENCE        "Pick the site you wish you'd built."          → refers.design, DESIGN.md
02 THE WHOLE MAP     "The $10k site is seven [pagine], non una."    → Relume (brief→sitemap→style)
03 THE SCROLL-STOPPER "Generate the exact image each section needs" → Higgsfield + Design Loop + UI sniping
04 MOBILE            "Where the traffic is" (60% del traffico)      → audit a 390px, mobile-first
05 DE-SLOPIFICATION  "Readers smell AI copy in one line."           → 6 Signs of AI writing
06 ICONS + DETAILS   "UI sniping" da Savee/21st.dev                 → 941 icone, componenti copiati
07 SEO-IFICATION     "Grab a skill. Point Claude at the site."      → claude-seo, keyword ranking
```

## Livello 1 — Il file DESIGN.md come design DNA

Lo strumento `refers.design` smonta un sito di riferimento (Mintlify, nel caso mostrato) in un
pannello a 4 tab (`DESIGN.md` | `Tokens.of` | `CSS Variables` | `Design Tokens`). Il pezzo che
conta non è il colore in sé ma la **descrizione di ruolo in prosa** accanto a ogni token, verbatim:

> "Mint Green — Brand links, active nav state, feature icons, decorative dots in eyebrow labels,
> the thin underline on inline code references — the only chromatic accent in a monochrome
> system, applied sparingly to make functional moments feel 'switched on'."

Non un nome e un hex: un **ruolo con un perché**. Regola operativa dichiarata a voce: *"what this
has done is given us the design DNA... and when we give that to Claude, we can build a version
for ourselves"* — il riferimento non si copia, si smonta in token e si ricostruisce.

## Livello 2 — "Relume è le ossa, il tuo design system è la pelle"

Flusso completo brief→sitemap→wireframe→style-guide→export (Figma/Webflow/React/HTML/**Export to
Claude nativo**). Regola citata a voce sul tempo speso in sitemap prima di generare pixel: *"an
ounce in print is worth a pound in post."* Il prompt di consegna a Claude, trascritto parola per
parola:

> "hey there i want you to go ahead and build for me a beautiful website based on this particular
> link using the exact design systems and layouts that are included in this zip file that we
> built in relume"

## Livello 3 — Design Loop: il giudice non deve condividere la memoria del costruttore

Il pezzo di metodo più forte del video, dalla guida Notion gratuita dell'autore ("The Design
Loop"), dichiarata **adattamento del Gauntlet Loop di Matt Shumer** (lo stesso creatore citato in
[[Source_Simone_Rizzo_Loop_Engineering]] per la tassonomia Prompt→Context→Harness→Loop
Engineering — due video dello stesso batch arrivano allo stesso nome, "Loop", da due angolazioni
diverse: Rizzo sul *come far girare* un ciclo autonomo, Roberts su *come giudicarlo*).

> "Claude Design has taste. It just can't judge its own work. The context that builds a piece is
> the context that grades it — a chef reviewing their own restaurant. Five stars, every time...
> Parallel agents buy you speed. Fresh context buys you the result."

> "The one thing to remember — A critic that shares memory with the builder is grading its own
> homework. Everything else here is detail."

Quattro meccanismi dichiarati: (1) un teardown in `bar.md` che converte un riferimento in
meccanismi verificabili prima di costruire; (2) tre critici con brief distinti; (3) un preflight
che verifica che il critico possa davvero vedere prima di sprecare un run intero; (4) model
tiering — economico dove il giudizio è meccanico, il modello più forte dove serve gusto.
Si invoca come slash-skill: `/design loop`.

## Livello 3b — UI sniping

Definizione verbatim: *"UI sniping is the idea that we can find any UI component that we like and
bring it over."* Distinzione chiave dichiarata: un'immagine di riferimento (da Savee) **non è un
componente**, va ricostruita nel proprio design system, non copiata. Esempio completo: un widget
di preventivo tetto costruito da un'immagine di riferimento (layout) + un video di riferimento
(animazione "Siri-like"), risultato £7.150 in output — due riferimenti distinti per due dimensioni
distinte (forma e movimento).

## Livello 4 — Mobile: 390px, mai a voce

Il numero operativo del livello (larghezza logica di un iPhone 14/15 in portrait) compare **solo
nella slide**, mai pronunciato. Dato citato a voce: *"60% of traffic at least actually is on our
phones."* Metodo dichiarato: *"we'd start off with the mobile first and then work backwards...
there is no substitute but to actually going through the mobile yourself"* — mobile-first, poi a
ritroso al desktop, **verifica finale sempre umana**.

## Livello 5 — De-slopification: la tabella dei 6 "Signs of AI writing"

Il pezzo più riusabile del video, sei tell con coppia prima/dopo e una regola in una riga:

| # | Il tell | Regola |
|---|---|---|
| 1 | The three-item flourish | "Three adjectives is a rhythm, not an argument. One specification beats it every time." |
| 2 | "Not just X, but Y" | "The construction promises a reveal and then delivers an abstraction." |
| 3 | Elevated verbs (leverage, seamless, robust, elevate...) | "All of them mean nothing and cost a line." |
| 4 | Empty superlatives ("most trusted") | "Unfalsifiable, so the reader discounts it entirely. A date cannot be argued with." |
| 5 | M-dash pileup | "One dash in a paragraph is punctuation. Three is a tic." |
| 6 | Numeri inventati | "Inventing a number is the one unrecoverable mistake. Say the slot is empty instead." |

Regola di tracciabilità del copy, dalla tab "Copy" del sito dimostrativo: *"Not from a brand
workshop. Every line traces to one of four sources, and if a sentence cannot name its source it
does not go on the page."* Psicologia dichiarata sotto: principio "don't make me think" /
system-one cognition — *"people don't read websites, they browse them."*

## Livello 6-7 — UI sniping su libreria e SEO in 5 mosse

Livello 6: `21st.dev` per componenti copiabili come codice, librerie icone (Flaticon/Icons8/
IconScout, $10-12/mese). Livello 7: repo `claude-seo` (25 sub-skill + 18 sub-agent, MIT) con un
prompt SEO in 5 mosse — l'unica davvero nuova rispetto a quanto l'Impero ha già è la quarta:

> "...I want you to **question me on my customer** so that we together can find out the long-tail
> intention words, the short intention words, and I want you to rank those based on volume and
> also difficulty."

Deliverable reale mostrato: strategia SEO di Glaido (startup dell'autore), 351 keyword in tabella
con colonne KEYWORD/EST.VOL/DEMAND INDEX/DIFFICULTY/VERDICT/WHY — la colonna WHY obbligatoria per
ogni verdetto. **Incoerenza dichiarata non spiegata**: la voce cita "28 keyword" su cui
posizionarsi, il documento a schermo ne mostra 351 — l'analisi originale marca il divario ➕ senza
risolverlo per invenzione.

## Key Quotes

> "Claude is the world's number one design agent for building beautiful websites. But just
> because your site looks pretty doesn't mean that it will sell or get customers."

> "A critic that shares memory with the builder is grading its own homework. Everything else here
> is detail."

> "These are the tells that get a line rewritten on sight. Every one of them showed up in a first
> draft of this page and was cut."

> "...if you don't have your own design operating system, you're leaving way too many hours and
> productivity and value on the table." [chiusura, cliffhanger sul video successivo promesso]

## Confronto con Digital Empire (dall'analisi originale, verificato in questa sessione)

**Dove l'Impero è già avanti**: design system proprietario (`guild-design.md`, 380 righe, due
standard A/B con 14 principi non negoziabili, stack Next.js 16+Tailwind v4+Lenis+Framer
Motion+GSAP) — il video non ha equivalente, prende in prestito il design system altrui ogni volta.
Pipeline sito già coperta (`site-brief→site-plan→site-design→site-copy→site-build→site-qa`).

**Dove il video è avanti — verificato con grep prima di proporre, non solo dichiarato**:
1. **Fresh-context critic**: `grep` mirato su `.claude/agents/` per "contesto fresco" / "fresh
   context" / "shares memory" / "grading its own homework" non trova nessun risultato in
   `guild-design.md`, `sentinel-quality.md`, `apex-critic.md` — **il gap è reale**, l'Impero ha
   gate e sentinelle ma nessuna regola scritta che imponga che il giudice non condivida la memoria
   del costruttore.
2. **Mobile 390px**: `grep` su `.claude/agents/` e `.claude/skills/` per "390px" non trova nulla —
   `site-design/SKILL.md` ha solo "mobile-first nei token" (riga 509), senza un numero operativo
   di audit. **Gap reale ma più piccolo di quanto sembri**: la disciplina mobile-first c'è già,
   manca solo il numero.
3. **Tabella "Signs of AI writing"**: qui la verifica ridimensiona la lacuna dichiarata
   dall'analisi originale. `.claude/skills/copy-editing/SKILL.md` (righe 327-334) **ha già** una
   tabella di sostituzione corporate→umano che include 3 delle stesse parole bandite dal video
   (Leverage→Use, Robust→Strong, Seamless→Smooth). **Quello che manca davvero non è la lista di
   parole, ma il formato**: il video lavora a livello di frase intera (esempio completo prima/dopo
   + una regola discorsiva), non di singola parola, e include tell strutturali che
   `copy-editing` non ha — *three-item flourish*, *empty superlatives*, *m-dash pileup*, *numeri
   inventati* — nessuno di questi è un problema di vocabolario, sono pattern retorici.

## Consigli (Stage 8 — proposte, NON applicate in questa sessione)

Coerente con la regola "Consigliare sempre dopo ogni studio". Nessuna patch scritta: il perimetro
di questo lavoro (`company/Memory/riprese/EMP-QQ2R.md`) era chiudere il video fino alla wiki con i
consigli, non modificare skill/agenti condivisi mentre un'altra sentinella (`studia-rizzo`)
lavorava in parallelo sullo stesso repo.

1. **`.claude/agents/guild-design.md`** — aggiungere l'invariante del Design Loop come regola di
   review esplicita: *"un critico che condivide la memoria/contesto di chi ha costruito il pezzo
   non può giudicarlo — serve contesto fresco."* Applicabile subito alle review di design che
   `guild-design` già coordina.
2. **`.claude/skills/site-design/SKILL.md`** — aggiungere **390px** come larghezza operativa
   esplicita dell'audit mobile, accanto alla riga esistente "Mobile-first nei token" (riga 509):
   oggi la disciplina c'è, il numero no.
3. **`.claude/skills/copy-editing/SKILL.md`** — estendere la tabella esistente (righe 327-334, già
   in produzione) da sostituzione-parola a sostituzione-frase: aggiungere i 3 tell strutturali che
   non ha (three-item flourish, empty superlatives, m-dash pileup, numeri inventati) nel formato
   tell+regola+esempio prima/dopo del video, non solo swap lessicale.
4. **Uso interno immediato, senza patch**: la regola "ogni riga di copy deve poter nominare la
   propria fonte o non va in pagina" (tab Copy del sito Ridgeline) è applicabile subito come
   checklist manuale per `cro-copy-architect` / `guild-copy-apsoc`, senza bisogno di modificare
   nessun file — è un criterio di giudizio, non un artefatto da costruire.

## Nota di trasparenza — limiti della fonte (dichiarati dal video stesso e verificati)

- **Il corpo completo della skill Design Loop non è mai a schermo**: solo la tabella dei 4
  meccanismi e l'aside finale. Il resto (come si scrive `bar.md`, i tre brief dei critici, il
  model tiering) resta dietro la pagina risorse dell'autore.
- **SlopMonster** (`github.com/ItsssssJack/SlopMonster`, il repo che darebbe la lista completa dei
  tell) è solo linkato in descrizione, mai aperto a schermo.
- **Claude non è mai mostrato mentre lavora**: si vede il prompt digitato e il risultato finito,
  non il processo in mezzo.
- **28 vs 351 keyword**: incoerenza voce/schermo nel deliverable SEO, non spiegata dal video né
  risolta da questa analisi — marcata ➕, non inventata una spiegazione.
- **Video a 360p**: alcuni valori esadecimali dei token colore sono `[incerto]` o `[illeggibile]`
  — mai completati per invenzione (dettaglio in `coverage.md`).
- **Contenuto misto**: ~6,5% del video è promo (community Skool gratuita 33.3k membri + corso a
  pagamento "Claude Code FULL COURSE"), più tre link affiliati dichiarati in descrizione.
- **Questa pagina wiki è scritta a valle di una verifica Stage 5 che ha trovato una discrepanza di
  conteggio non risolta** (182 dichiarati vs 108 tracciabili) — vedi `coverage.md` per il
  dettaglio completo e onesto della copertura reale.

## Connessioni

- [[Source_Simone_Rizzo_Loop_Engineering]] — stesso batch `max17`, stesso concetto radice: il
  Gauntlet Loop di Matt Shumer. Rizzo lo applica al *ciclo di esecuzione* (`/loop`, `/goal`, 5
  Livelli di Verifica), Roberts lo applica al *ciclo di giudizio* (Design Loop, critico a contesto
  fresco) — due metà dello stesso principio, mai unite in un solo documento dell'Impero.
- [[tools/Tool_Empire_Premium_Style]] — il design system proprietario che questo video conferma
  indirettamente come scelta giusta: `DESIGN.md` di refers.design è lo stesso tipo di artefatto
  (token + ruolo in prosa) che `empire-premium-style` già congela in `design-tokens.css`, ma
  estratto da un sito esistente invece che progettato da zero — complementare, non concorrente.
- [[tools/Tool_Copy_Workflow_Orchestration]] — il sistema APSOC che governa il copy dell'Impero;
  la tabella "Signs of AI writing" di questo video è un contributo puntuale (livello frase, non
  livello messaggio) che si affianca ad APSOC senza sostituirlo.
- [[concepts/Concept_Guardrail_Che_Si_Fanno_Rispettare]] — stesso principio da un'altra
  angolazione: l'invariante del Design Loop ("il critico non deve condividere la memoria del
  costruttore") è un guardrail architetturale, non una regola che dipende dalla buona volontà di
  chi fa la review — si applica separando davvero i contesti, non ricordandosi di farlo.
