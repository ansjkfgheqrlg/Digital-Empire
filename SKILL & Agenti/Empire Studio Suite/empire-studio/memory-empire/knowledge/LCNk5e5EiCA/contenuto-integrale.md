# Contenuto Integrale — LCNk5e5EiCA
## "Claude Code + Karpathy = Agenti AI da 10.000€" — Giovanni Beggiato (Gentes AI)

- **URL:** https://www.youtube.com/watch?v=LCNk5e5EiCA
- **Durata:** 1.503s = 25m03s · **Lingua:** italiano · **Capitoli ufficiali:** 16
- **Run:** `empire-studio/runs/max18-v02-karpathy-agenti`
- **Ingested:** 2026-09-04 · **Batch:** max18, v02
- **Copertura:** 80/501 frame guardati (16,0%), **69/69 frame unici = 100%**; trascrizione
  612/612 righe uniche = 100% (0:00:02 → 0:24:59)
- **NO-FINTO:** PASS — nessun frame descritto senza essere stato aperto; tutte le lacune
  dichiarate in `runs/max18-v02-karpathy-agenti/coverage.md`

---

## Capitoli ufficiali (da `ingest.json`; titoli in inglese, parlato in italiano)

| Start | Titolo |
|---|---|
| 0:00 | 10,000 AI agents: what we build today |
| 0:43 | Karpathy's pattern: what an LLM wiki is |
| 1:59 | The three layers: raw sources, atomic notes, schema |
| 3:41 | The three AI operations: ingest, query, lint |
| 5:07 | The structure of the company brain we build |
| 6:51 | Generic output vs company brain output |
| 8:53 | Setup: Claude Code and the first prompt |
| 11:08 | The flow: call, brain, signable document |
| 12:43 | PandaDoc: template, dynamic variables and signature |
| 15:10 | Building the proposal generation skill |
| 17:27 | Live test: from call transcript to proposal |
| 19:22 | How to price: cost based or value based |
| 21:01 | Value based pricing: how to calculate the value |
| 21:59 | ROI: what the saved time is worth |
| 23:44 | Entry level pricing and when you need a retainer |
| 24:42 | Wrap up |

---

## PARTE 1 — L'apertura e la doppia tesi (0:00–0:42)

*"In questo momento alcune aziende pagano fino a €10.000 per agenti che possono essere costruiti in
un solo pomeriggio. In questo video costruisco un MVP live dall'inizio alla fine con Cloud Code e vi
lascerò tutti i prompt per replicarlo. Per costruirlo però non andremo a caso. Useremo la teoria di
cui Andrej Karpathy parla quando costruisce con AI, costruendo attorno a questo agente una piccola
Company Brain che potremo utilizzare per costruire automazioni successive."*

Due tesi sovrapposte:
1. **Tecnica** — un agente vale poco da solo, vale dentro una memoria aziendale persistente.
2. **Commerciale** — lo stesso artefatto vale €3.000 o €15.000 a seconda di chi lo compra.

Presentazione: agenzia **Gentes AI**, consulenza ad aziende *"che vanno dai €10.000 al mese fino ai
50 milioni di euro l'anno"*, più una community privata di imprenditori e freelancer.

## PARTE 2 — Il pattern di Karpathy (0:43–3:40)

Fonte primaria letta a schermo: post di **Andrej Karpathy** su X, *"LLM Knowledge Bases"*
(`x.com/karpathy/status/2039800565266...`), datato dall'autore **aprile 2026**. Tre sezioni del
post: **Data ingest** (documenti sorgente in `raw/`, poi un LLM "compila" incrementalmente un wiki
di file `.md` con riassunti, backlink, articoli per concetto; Obsidian Web Clipper per convertire
articoli web), **IDE** (Obsidian come frontend — *"the LLM writes and maintains all of the data of
the wiki, I rarely touch it directly"*), **Q&A** (*"once your wiki is big enough — e.g. mine is
~100 articles and ~400K words — you can ask your LLM agent all kinds of complex questions [...] I
thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining"*).

Mostrato anche il vault Obsidian personale dell'autore in "Galaxy view": **3515 note** (confidenza
media, testo piccolo), cartelle `_showcase, areas, code, concepts, data, docs, engine, entities,
labs, outputs, projects, scripts, self, sources, workspace` + `CLAUDE`, `CONVENTIONS`, `README`.

**I TRE STRATI** (slide Excalidraw): 1) **FONTI GREZZE** — trascrizioni, documenti, email; si
leggono e non si toccano. 2) **IL WIKI** — note collegate che l'AI aggiorna, una per cliente e una
per concetto. 3) **LO SCHEMA** — le regole, com'è organizzato e come mantenerlo.

## PARTE 3 — Le tre operazioni (3:41–5:06)

- **INGEST** — materiale nuovo entra, l'AI legge e aggiorna le note.
- **QUERY** — una domanda sul business, l'AI risponde leggendo il wiki **e cita le note** da cui
  prende la risposta.
- **LINT** — controllo automatico delle contraddizioni, pulizia dei dati vecchi, gestione delle
  note orfane.

Claim della slide: **"L'UMANO CURA LE FONTI E FA LE DOMANDE, L'AI FA IL RESTO"**.

**Limite dichiarato dall'autore**: *"questa infrastruttura è molto molto buona per una conoscenza di
tipo personale [...] va molto bene se siete un solo founder."* Lo scaling aziendale è **rinviato al
corso a pagamento** nella community, non mostrato.

## PARTE 4 — La struttura del Company Brain (5:07–6:50)

```
company-brain/
├── CLAUDE.md       → LO SCHEMA (regole, naming, operazioni)
├── fonti/          → STRATO 1, IMMUTABILE
├── clienti/        → IL WIKI (+ _template.md)
├── offerta/offerta.md → I PREZZI, unico posto
├── proposte/       → IL WIKI (+ _template.md)
├── index.md        → IL CATALOGO (una riga per nota, per categoria)
├── log.md          → IL REGISTRO append-only
├── .claude/skills/ → le automazioni
└── .env            → chiavi API
```

Claim della slide: **"DAI UNA CALL, TORNA UNA NOTA"**.

### PROMPT 1 integrale (recuperato parola per parola dallo schermo)

```
<obiettivo>
Crea la struttura di un Company Brain seguendo il pattern "LLM Wiki" di Andrej Karpathy:
tre strati (fonti grezze immutabili, wiki in markdown mantenuto dall'AI, schema di regole)
e tre operazioni (ingest, query, lint). Il cervello e' la memoria dell'azienda: clienti,
offerta e proposte vivono come note di testo collegate che Claude Code legge e aggiorna.
</obiettivo>

<struttura>
company-brain/
├── CLAUDE.md            -> lo SCHEMA: regole, naming, operazioni
├── fonti/               -> strato 1: materiale grezzo IMMUTABILE
│                           (trascrizioni di call, brief, email). Si legge, mai si modifica.
├── clienti/             -> strato 2 (wiki): una nota per cliente
│   └── _template.md
├── offerta/
│   └── offerta.md       -> strato 2 (wiki): l'UNICO posto dove vivono i prezzi
├── proposte/            -> strato 2 (wiki): una nota per proposta generata
│   └── _template.md
├── index.md             -> catalogo: una riga per nota, per categoria
├── log.md               -> registro append-only di ingest e proposte
├── .claude/
│   └── skills/          -> vuota per ora, la riempiamo dopo
└── .env                 -> chiavi API (crea il file vuoto, lo compilo io)
</struttura>

<CLAUDE.md deve contenere>
- Chi e' l'azienda e cosa vende (lascia i segnaposto, li compilo io).
- La mappa dei tre strati: fonti/ e' immutabile; il wiki (clienti/, offerta/, proposte/)
  lo mantieni tu; lo schema e' questo file.
- Le tre operazioni:
  INGEST: quando arriva un file nuovo in fonti/, leggilo, estrai le informazioni e crea o
  aggiorna la nota cliente; poi aggiorna index.md e appendi una riga in log.md. Se qualcosa
  contraddice cio' che gia' sai, segnalalo, non sovrascriverlo in silenzio.
  QUERY: quando ti faccio una domanda sul business, rispondi leggendo il wiki e cita le note
  da cui prendi la risposta.
  LINT: quando te lo chiedo, controlla note in contraddizione, dati vecchi e note orfane
  senza collegamenti.
- Regola 1: i prezzi vivono SOLO in offerta/offerta.md. Mai inventare un numero, mai copiarli
  altrove.
- Regola 2: ogni proposta generata scrive SEMPRE una nota nuova in proposte/ con data, cliente,
  importo, stato e link, piu' l'aggiornamento di index.md e log.md. Nessuna proposta senza nota.
- Regola 3: mai leggere o mostrare il contenuto di .env, solo i nomi delle [chiavi]
</CLAUDE.md deve contenere>
```

⚠️ L'ultima riga della Regola 3 esce dal bordo dello schermo: la parola `chiavi` è ricostruita per
senso, non letta.

### Cosa Claude ha effettivamente creato

`clienti/_template.md` coi campi nome, azienda, email, telefono, contesto, problema, note
decisorie, budget, fonte. `proposte/_template.md` con cliente, data, importo, stato, link, nota.
`offerta/offerta.md` con un listino demo di lead generation a quattro voci (**Setup, Starter,
Growth, Scale**). Verifica eseguita da Claude stesso con `find . -not -path "*/.git/*" | sort`.

## PARTE 5 — Il confronto A/B (6:51–8:52)

Due finestre Antigravity IDE affiancate, ognuna con Claude Code e `bypass permissions`: a sinistra
`Prova No Brain` (cartella vuota), a destra `Brain-Karpathy`. Stesso transcript, stessa richiesta.

**Senza cervello** — un artifact di claude.ai, poi il messaggio: *"Performance evidenziata come 'la
sua preferenza in call', ma ho messo la stima trimestrale a ~3.000 € (600 setup + 30 × 80) [...] Se
preferisci non mostrare quel totale stimato, lo tolgo. [...] Vuoi che ti scriva anche la mail di
accompagnamento?"* — cioè **chiede all'umano di confermare due scelte che ha inventato lui**.

**Col cervello** — *"Fatto. Proposta generata e verificata. [...] Check brand/prezzi (dal tuo PDF
reale): copertina con logo, 'Preparata per Marco Rossi – Rossi Marketing', data 23 luglio 2026 ✓ ·
pag. 'La tua situazione oggi', 3 paragrafi presi dalla call ✓ · **prezzi identici a
offerta/offerta.md**: Standard 2.000 € (1.000 setup + 500/mese × 2), Performance 600 € setup + 80
€/meeting ✓ · nessuna delle due opzioni pre-evidenziata ✓ · pagina Firma pulita ✓ · Note registrate:
`proposte/rossi-marketing-2026-07-23.md` + index.md e log.md aggiornati."*

**La differenza dimostrata non è estetica ma di verificabilità.**

⚠️ Cautela: a voce l'autore liquida il primo output come *"quasi AI slop"* e dice *"non ha nemmeno
il nostro logo"*. Nel frame l'artifact è impaginato e porta "Gentes.AI" come testo; manca il logo
immagine, il template brandizzato e il canale di firma. Il claim è retorica, non un fatto.

## PARTE 6 — Il flusso disegnato prima del codice (11:08–12:42)

```
LA FONTE  →  IL CERVELLO  →  PANDADOC  →  LA MEMORIA
                  ↑
             offerta.md
```
Post-it: *"Il flusso lo disegno io, poi Claude genera"* · *"Claude scrive più veloce, ma il progetto
è mio"*. Claim: **"PRIMA DISEGNO IL FLUSSO, POI GENERO"**. In produzione la fonte è collegabile a un
note-taker (Fathom, Fireflies).

## PARTE 7 — PandaDoc: template, variabili, chiavi API (12:43–15:09)

Template preparato prima del video, brandizzato, con firma digitale configurata e **variabili
dinamiche / text fields** popolate dall'AI. Le due chiavi API, lette integralmente nella pagina
Dev Center → Configuration:

| Chiave | Cosa dà | Limiti a schermo |
|---|---|---|
| Sandbox | test gratuito | prefisso developer su ogni documento, **10 richieste/minuto** |
| Production | go live | nomi documento liberi, **nessun watermark**, **300 chiamate/minuto**, su richiesta |

Più: Webhooks fino a **100** per account; badge account **"Trial 14"**.

Dal Notion dei prerequisiti: *"con la chiave sandbox i documenti escono marcati [DEV] e l'invio a
email esterne fallisce con **403**"*. Ecco perché nel video **nessun documento viene mai inviato
davvero a un cliente**.

### Prerequisiti una-tantum (dal Notion)

1. Template PandaDoc pronto — brandizzato, coi token (nome cliente, azienda, problema, contesto),
   le opzioni di prezzo come **righe opzionali NON preselezionate**, valuta EUR, pagamento Stripe se
   lo si vuole offrire. *"Queste cose si impostano in UI, non via API."*
2. La chiave API giusta (sandbox per la bozza, production per l'invio).
3. Una trascrizione di discovery call, anche finta, da mettere in `fonti/`.
4. Obsidian installato e puntato sulla cartella, per vedere il grafo.
5. `.env` con `PANDADOC_API_KEY` e `PANDADOC_TEMPLATE_ID`, *"mai a schermo"*.

## PARTE 8 — La skill `/genera-proposta` (15:10–17:26)

Slide **"L'INTEGRAZIONE PANDADOC — ogni pezzo testato da solo"**:

1. **TESTA IL PEZZO** — `inspect_template.py` stampa cosa il template si aspetta davvero
   (`ruolo: Client`, `token: client.name`, `pricing: Prezzi`), perché *"i nomi nel codice devono
   combaciare col template"*. Anti-pattern: *"indovinare + vibe coding che rompe tutto"*.
2. **LA SKILL** — `pandadoc.py` (il client: crea, legge, aspetta la bozza), `create_proposal.py`
   (orchestra), `SKILL.md` (il comando `/genera-proposta`).
3. **IL DETTAGLIO ASINCRONO** — `POST /documents` → `uploaded` → **si aspetta** → `draft` ✅.
   *"PandaDoc non crea il documento all'istante"*; mandarlo prima **fallisce**.

Struttura reale a disco, coincidente con la slide:
`.claude/skills/genera-proposta/{SKILL.md, scripts/{pandadoc.py, create_proposal.py, inspect_template.py}}`.

**Clausola anti-allucinazione** in coda al Prompt 2: *"Se una parte di queste istruzioni è ambigua o
sembra contraddittoria, fermati e spiegami il dubbio invece di indovinare. Non aggiungere librerie,
file o funzionalità extra non richieste."* Al prompt sono allegati l'URL della dashboard e uno
screenshot del template.

**Definizione di skill data dall'autore**: *"la skill non è altro che un modo di dire a Claude
'automatizza questo workflow', perché gli step sono sempre quelli."*

## PARTE 9 — Il test dal vivo (17:27–19:21)

Fonte grezza: `2026-07-10-call-rossi-marketing.md` (naming **data ISO + slug**), transcript di
discovery call letto integralmente a schermo. Il sistema venduto: lead generation a freddo su
Instantly — estrazione lista con **Apify**, arricchimento con **Claude**, sequenze email
personalizzate, invio multi-casella con follow-up automatico, appuntamenti solo da chi risponde
interessato. *"Davide fa la call, non la caccia. Il sistema riempie il calendario, lui chiude."*

**Il listino, identico su tre fonti indipendenti** (transcript-fonte, check dell'agente, PDF finale):

| | Standard | Performance |
|---|---|---|
| Setup | 1.000 € una tantum | 600 € |
| Ricorrente | 500 €/mese × 2 mesi | 80 € per meeting prenotato (~30/trimestre) |
| **Totale 3 mesi** | **2.000 €** | ~3.000 € se i 30 meeting arrivano |
| Pagamento | 50% alla firma, 50% a fine campagna | idem |

Testo stampato sul PDF: *"Stesso sistema, due modi di pagarlo. Nessuna delle due è 'quella giusta',
dipende da come vuoi distribuire l'investimento."* · *"Un meeting = lead qualificato, che si
presenta."*

L'autore chiude tornando nel file grezzo dentro `fonti/` per **confrontare i prezzi della call con
quelli finiti sul PDF** e dichiarare la corrispondenza.

## PARTE 10 — Come prezzare (19:22–24:41)

Slide preparata **"PREZZARE E OFFRIRE, sul valore non sul costo"**:
- ① **PREZZA SUL VALORE** — Azienda A 3.000 € / Azienda B 15.000 €, *"stesso agente, valore
  diverso"* ❌ *non prezzare a ore*
- ② **L'OFFERTA IN CHIARO** — **3 GIORNI → 1 ORA**, *"la proposta pronta appena arriva il lead, la
  rivedi e premi invia"*
- ③ **LA STRUTTURA** — SETUP una tantum **1.000-5.000 €**, RETAINER **500-2.000 €/mese**, *"range
  indicativi"*
- Claim: **"PREZZA IL VALORE, NON LE ORE"**

**Il costo reale di produzione** (scritto a mano sulla lavagna accanto a `COSTO`): ~**$200** di
Claude + ~**$59** di PandaDoc. *"Il costo è una strategia che vi farà perdere e vi farà sempre più
schiacciare i margini."*

**L'ordine di grandezza del valore**: *"un one day training di 8 ore su AI può arrivare a costare
10-15.000. Un'automazione del genere può arrivare a costare anche €10.000. Sarà forse la prima che
venderete? **Assolutamente no**."*

**I due metodi, additivi** (*"non è un o, ma è un e"*), ricostruiti dalla lavagna disegnata dal vivo:

```
METODO 1 — IL TEMPO (proxy)
  VALORE → VBP → TEMPO → (tempo persona per proposta) × (n° proposte al mese)

METODO 2 — IL ROI
  10 ore/mese liberate → 2 clienti presi in quelle ore → cliente medio 2.500 €
  → 2 × 2.500 = 5.000 €/mese di upside (+ il valore orario di chi paghi)
  ⇒ automazione prezzabile intorno ai 6.000 €/mese
```
*"Facciamo numeri a casissimo"* — riserva dell'autore, dichiarata mentre calcola.

**Le tre condizioni**, poste prima di qualunque cifra: *"dovete avere un business che ne ha bisogno,
dovete avere un mercato che ve lo permette, dovete avere un avatar che è disposto a pagare"*. Più:
*"per scalarle non è poi così semplice come farle one-shot"*.

**Entry level**: *"potete cominciare ad offrire questa automazione — **dopo ovviamente averne fatte
un po'** — tra i 1.000 e i 5.000 €."*

**Quando serve il retainer (criterio, non preferenza)**: quando l'automazione deve essere
**mantenuta** perché cambia forma nel tempo. Esempio: aziende di macchinari pesanti che vendono su
mercati **EN / IT / FR / DE** (le quattro sigle sono scritte a mano sulla lavagna), dove le proposte
escono in lingue diverse e prendono forme diverse a seconda del macchinario.

**Chiusura**: *"prezzate in base al valore e non in base alle ore che ci mettete a sviluppare, perché
altrimenti i vostri margini andranno giù, e nessuna azienda di successo prezza mai al costo."*

---

## Contesto commerciale verificato a schermo (non formazione)

- **gentes.ai** — *"AI Growth Partner for B2C Service Businesses"*; loghi Value Group, Higgsfield,
  Anthropic, Notion, Amazon, P&G, Google. Tre fasi: **Audit** (call gratuita 30 min), **Engineering**,
  **Training & Launch**. Due linee: **Lead Generation** (reactivation, ad campaigns, content systems)
  e **Voice AI** (receptionist, lead qualification, appointment setting).
- **Team** — Giovanni Beggiato, CEO Strategy & Systems (*"Led AI initiatives at Amazon delivering
  $4M+ in savings. Won CEO Award, top 2% of employees worldwide"*); Jean-Marc Herrada, COO
  (*"worked with P&G in Manufacturing and Supply Chain, leading teams of 40 people and $100M
  projects"*).
- **Community Skool "Avanguardia Plus"** — 91 membri, 6 online, 2 admin. Corso *Claude Code Per
  Aziende* con indice a schermo (Setup · Subagents · Team di agenti · Gestione Contesto · Skills ·
  MCP), durata **4h52:49**, più moduli *Automazioni Aziendali Claude* (Lead Generation, PandaDoc,
  Preventivi Automatici, GHL, Onboarding), *Costruisci La Tua Company Brain*, *Agenti Vocali*,
  *Personal Brand Masterclass*.
- **Stack** — IDE **Google Antigravity** con **Claude Code** installato come estensione VS Code di
  Anthropic (marketplace Open VSX). L'autore precisa che *"non cambia assolutamente nulla"* rispetto
  alla desktop app.

## Cosa NON è dimostrato (dichiarazione esplicita, regola NO-FINTO)

1. **Nessun documento è mai stato inviato a un cliente**: tutti `[DEV]`, tutti in stato DRAFT
   (dashboard: Your drafts 1, Waiting for others 0, Finalized 0).
2. **Il cliente è dichiaratamente finto** ("Rossi Marketing / Marco Rossi", demo per YouTube).
3. **Nessun euro incassato è mostrato.** La cifra €10.000 del titolo è un tetto teorico con riserva
   incorporata dall'autore stesso.
4. **Il codice della skill non è mai stato ingrandito** — `pandadoc.py`, `create_proposal.py`,
   `inspect_template.py` compaiono solo come nomi di file.
5. **Il `CLAUDE.md` generato non è mai stato aperto a schermo** — se ne conosce il contenuto solo dal
   prompt che lo commissiona e dal riassunto che Claude ne fa.
6. **La scalabilità aziendale del pattern è rinviata** al corso a pagamento.
7. **Contenuti citati ma non ingeriti** (dietro paywall): corso Claude Code 4h52:49, lezione PandaDoc
   49 min, corso Company Brain, modulo Preventivi Automatici.
