---
Type: SOURCE
Status: Active
Tags: #company-brain #llm-wiki #karpathy #claude-code #memoria-agenti #pandadoc #preventivi #value-based-pricing #single-source-of-truth #giovanni-beggiato #max18
Created: 2026-09-04
Last updated: 2026-09-04
---

# Source: Giovanni Beggiato — Claude Code + Karpathy = Agenti AI da 10.000€

## Overview

Tutorial di 25 minuti in cui l'autore costruisce dal vivo un MVP: un agente che, da una
trascrizione di discovery call, genera una proposta commerciale firmabile su PandaDoc e la
registra come nota nella memoria dell'azienda. La tesi non è "ecco un'automazione": è che **un
agente vale poco da solo e vale molto dentro una memoria persistente**, e che quella memoria ha
una forma già nota — la **LLM Wiki di Andrej Karpathy**, calata sul business come *Company Brain*.
Video 2 del lotto `max18`.

Il valore per Digital Empire non è il caso d'uso (DE ha già `beast-preventivi`, `proposal-gate`,
`preventivo-auto`), ma **tre architetture verificate a schermo che DE possiede a metà**: la regola
*single source of truth* sui prezzi, l'operazione **LINT** come lavoro esplicito dell'AI sulla
propria memoria, e la regola *"nessuna proposta senza nota"* — cioè l'estensione agli artefatti
commerciali dello stesso principio che DE applica già ai task (REGOLA ZERO memory-first). Tutti e
tre confermati come gap reali con `Grep` prima di essere scritti in "Consigli".

## Dati Tecnici

- **Video ID:** LCNk5e5EiCA · **URL:** https://www.youtube.com/watch?v=LCNk5e5EiCA
- **Durata:** 25m03s (1.503s) · **16 capitoli ufficiali** (titoli in inglese, parlato in italiano)
- **Canale:** Giovanni Beggiato — agenzia **Gentes AI** (gentes.ai) · **Lingua:** IT
- **Formato:** misto — ~9 min talking-head + slide Excalidraw, ~10 min screen-share denso
  (Antigravity IDE, Claude Code, Notion, PandaDoc), ~5 min lavagna disegnata dal vivo
- **Frame:** 501 densi @3s → 69 unici (soglia 6,0) | **Frame letti: 80/501 (16,0%), di cui
  69/69 unici = 100%** | **Trascrizione: 612/612 righe uniche = 100%** | NO-FINTO: PASS
- **KA:** 43 (41 osservati, 2 inferiti; 39 con riferimento frame)
- **Data di registrazione del video:** ~23 luglio 2026 (dedotta da tre date coerenti a schermo)
- **Run:** `empire-studio/runs/max18-v02-karpathy-agenti`

## Il Pattern — LLM Wiki di Karpathy

Fonte primaria **letta a schermo nel video**: il post di Andrej Karpathy su X intitolato *"LLM
Knowledge Bases"* (`x.com/karpathy/status/2039800565266...`, datato dall'autore aprile 2026).
Karpathy: *"a large fraction of my recent token throughput is going less into manipulating code,
and more into manipulating knowledge (stored as markdown and images) [...] the LLM writes and
maintains all of the data of the wiki, I rarely touch it directly [...] I thought I had to reach
for fancy RAG, but the LLM has been pretty good about auto-maintaining."*

```
        I TRE STRATI                              LE TRE OPERAZIONI
─────────────────────────────           ────────────────────────────────────
1  FONTI GREZZE                          INGEST  materiale nuovo entra,
   trascrizioni, documenti, email                l'AI legge e aggiorna le note
   si leggono e NON si toccano
                                         QUERY   una domanda sul business,
2  IL WIKI                                       l'AI risponde E CITA le note
   note collegate che l'AI aggiorna
   una per cliente, una per concetto      LINT   contraddizioni, dati vecchi,
                                                 note orfane senza collegamenti
3  LO SCHEMA
   le regole: com'è organizzato
   e come si mantiene

        "L'UMANO CURA LE FONTI E FA LE DOMANDE, L'AI FA IL RESTO"
```

**Limite dichiarato dall'autore stesso**: *"questa infrastruttura è molto molto buona per una
conoscenza di tipo personale [...] va molto bene se siete un solo founder."* Lo scaling a più
persone che scrivono nello stesso cervello è nominato e **rinviato al corso a pagamento**, non
mostrato.

## Il Company Brain — struttura e le tre regole

```
company-brain/
├── CLAUDE.md       → LO SCHEMA (regole, naming, operazioni)
├── fonti/          → STRATO 1, IMMUTABILE — si legge, mai si modifica
├── clienti/        → IL WIKI — una nota per cliente (+ _template.md)
├── offerta/
│   └── offerta.md  → I PREZZI — l'UNICO posto dove vivono
├── proposte/       → IL WIKI — una nota per proposta generata
├── index.md        → IL CATALOGO — una riga per nota, per categoria
├── log.md          → IL REGISTRO — append-only, un evento per riga
├── .claude/skills/ → le automazioni
└── .env            → chiavi API
```

Le tre regole scritte dentro `CLAUDE.md`, recuperate parola per parola dal prompt mostrato a
schermo (`frame-005`, `frame-204`) e confermate dall'output di Claude (`frame-296`):

1. **I prezzi vivono SOLO in `offerta/offerta.md`.** *"Mai inventare un numero, mai copiarli
   altrove."*
2. **Nessuna proposta senza nota.** *"Ogni proposta generata scrive SEMPRE una nota nuova in
   proposte/ con data, cliente, importo, stato e link, più l'aggiornamento di index.md e log.md."*
3. **Mai leggere o mostrare il contenuto di `.env`**, solo i nomi delle chiavi.

Più una quarta, dentro l'operazione INGEST, che è la più sottile: *"Se qualcosa contraddice ciò
che già sai, **segnalalo, non sovrascriverlo in silenzio**."*

## La Dimostrazione A/B — il punto vero del video

Due finestre IDE affiancate, stesso transcript, stessa richiesta. A sinistra Claude Code in
cartella vuota, a destra dentro il Company Brain.

**Senza cervello** — produce un artifact e poi chiede all'umano di **confermare due scelte che ha
inventato lui**: *"Performance evidenziata come la sua preferenza in call, ma ho messo la stima
trimestrale a ~3.000 € [...] se preferisci non mostrare quel totale stimato, lo tolgo."*

**Col cervello** — produce il documento e chiude con **cinque controlli superati contro un file che
esiste**:

> *• Copertina con logo, "Preparata per Marco Rossi – Rossi Marketing", data 23 luglio 2026 ✓*
> *• Pag. "La tua situazione oggi" — 3 paragrafi presi dalla call ✓*
> *• **Prezzi identici a `offerta/offerta.md`**: Standard 2.000 € (1.000 setup + 500/mese × 2),
> Performance 600 € setup + 80 €/meeting ✓*
> *• Nessuna delle due opzioni pre-evidenziata ✓ • Pagina Firma pulita, campi firma/data ✓*
> *• Note registrate: `proposte/rossi-marketing-2026-07-23.md` + index.md e log.md aggiornati*

**La differenza non è estetica, è di verificabilità.** Uno chiede fiducia, l'altro dichiara
controlli contro una fonte. Questo è il pezzo trasferibile a DE, non il template PandaDoc.

⚠️ **Cautela** (lezione della sentinella, non dell'autore): a voce l'autore liquida l'output senza
cervello come *"quasi AI slop"* e dice *"non ha nemmeno il nostro logo"*. Guardando davvero il
frame, quell'artifact è un documento impaginato con gerarchia tipografica e "Gentes.AI" presente
come testo. Manca il **logo immagine**, il template brandizzato e il canale di firma. Il claim
"AI slop" è retorica dell'autore, non un fatto verificato a schermo.

## L'Integrazione Tecnica — due lezioni riusabili con qualunque API

**"OGNI PEZZO TESTATO DA SOLO"** (slide `frame-328`, confermata dalla struttura reale a disco):

1. **Prima si interroga il sistema esterno, poi si scrive il codice.** Uno script isolato
   `inspect_template.py` stampa cosa il template si aspetta davvero (`ruolo: Client`,
   `token: client.name`, `pricing: Prezzi`), perché *"i nomi nel codice devono combaciare col
   template"*. Anti-pattern nominato: *"indovinare + vibe coding che rompe tutto"*.
2. **Il dettaglio asincrono**, isolato come trappola a sé stante:
   `POST /documents` → stato `uploaded` → **si aspetta** → stato `draft` → solo allora si agisce.
   *"PandaDoc non crea il documento all'istante"*; mandarlo prima **fallisce**.

La skill generata ha la forma che la slide prometteva:
`.claude/skills/genera-proposta/{SKILL.md, scripts/{pandadoc.py, create_proposal.py, inspect_template.py}}`.

Vincolo operativo da conoscere prima di replicare (letto nella pagina API di PandaDoc,
`frame-322`): la **chiave sandbox** marca ogni documento `[DEV]`, limita a **10 richieste/minuto** e
**fallisce con 403 sull'invio a email esterne**; la **production** toglie il watermark e sale a
**300 chiamate/minuto** ma va richiesta. Per questo **in tutto il video nessun documento viene mai
davvero inviato a un cliente**: restano tutti bozze `[DEV]` in dashboard.

## Il Pricing — prezza il valore, non le ore

Slide + lavagna costruita a mano dal vivo, ricostruita frame per frame.

**Il principio**: lo stesso identico agente vale **3.000 €** per l'Azienda A e **15.000 €** per
l'Azienda B — *"stesso agente, valore diverso"*. Il costo di produzione reale è irrisorio
(~$100-200/mese di Claude + ~$59 di PandaDoc), quindi *"il costo è una strategia che vi farà
perdere e vi farà sempre più schiacciare i margini"*.

**I due metodi, additivi non alternativi** (*"non è un o, ma è un e"*):

```
METODO 1 — IL TEMPO (proxy, dichiarata tale)
  VALORE → VBP → TEMPO → (tempo persona per proposta) × (n° proposte al mese)

METODO 2 — IL ROI
  10 ore/mese liberate
    → in quelle 10 ore la persona prende 2 clienti
    → cliente medio 2.500 €
    → 2 × 2.500 = 5.000 €/mese di upside
    (+ il valore orario di chi paghi)
    ⇒ automazione prezzabile intorno ai 6.000 €/mese
```

**Le tre condizioni** poste *prima* di qualunque cifra: *"dovete avere un business che ne ha
bisogno, dovete avere un mercato che ve lo permette, dovete avere un avatar che è disposto a
pagare"*.

**La struttura entry level**: setup una tantum **1.000-5.000 €**, retainer **500-2.000 €/mese**
(marcati sulla slide come *"range indicativi"*), e a voce: *"dopo ovviamente averne fatte un po'"*.

**Quando serve il retainer — un criterio, non una preferenza**: quando l'automazione **deve
cambiare forma nel tempo**. Esempio dato: aziende di macchinari pesanti che vendono su mercati
EN/IT/FR/DE, dove la proposta esce in lingue diverse e prende forme diverse a seconda del
macchinario.

**Il beneficio venduto al cliente non è l'automazione**: è **"3 GIORNI → 1 ORA"**, con la frase
pronta da mettere in offerta — *"la proposta pronta appena arriva il lead, la rivedi e premi
invia"*.

## Numeri Dichiarati (non verificati indipendentemente salvo dove segnalato)

| Numero | Fonte | Stato |
|---|---|---|
| Listino demo: 2.000 € standard (1.000 setup + 500×2) / 600 € + 80 €/meeting performance; 50-50 di pagamento | transcript-fonte + check agente + PDF finale | **verificato a schermo su 3 fonti indipendenti, coincidono** |
| Sandbox 10 req/min con prefisso `[DEV]`; Production 300 chiamate/min senza watermark; 100 webhook max | pagina Dev Center PandaDoc | **verificato a schermo** |
| Costo di produzione ~$100-200/mese Claude + ~$59 PandaDoc | parlato + lavagna | verificato a schermo (lavagna), non presso i fornitori |
| €10.000 per un'automazione del genere; one-day training AI 10-15.000 € | parlato | **claim con riserva dell'autore incorporata**: *"sarà forse la prima che venderete? Assolutamente no"* |
| Vault Obsidian personale: 3515 note | schermo | **confidenza media** (testo molto piccolo) |
| $4M+ di risparmi in Amazon, top 2% dipendenti; team da 40 e progetti $100M in P&G | sito gentes.ai | claim del sito, non verificato |
| Community Skool: 91 membri, 6 online, 2 admin; corso Claude Code 4h52:49 | schermo | verificato a schermo |
| Clienti "da €10.000/mese fino ai 50 milioni di euro l'anno" | parlato | dichiarazione, non verificata |

## Azione Concreta — Consigli (verificati con grep prima di scrivere)

Nessuna patch applicata: `EMP-QQ2R` Fase 1 è **solo studio**, ordine esplicito di Max.

### 1. I prezzi di DE non hanno un `offerta.md` — sono copiati in 68 file

**Verificato**: `grep -rl "Outreach Factory" --include="*.md" .claude/skills company` → **68 file**.
Il listino (€4.000 Outreach Factory / €3.500 Content Factory / €2.500 Second Brain / €8.000 Engine
Room) è riscritto a mano in `proposal-gate/SKILL.md:31`, `upsell-mapper/SKILL.md:23` e `:31`,
`empire-context/SKILL.md:35`, `delivery-playbook/SKILL.md:24`, `client-handover`,
`outreach-reply-triage`, `carousel-empire`, `company/01-agency/BACKBONE.md` e altri.
**Un `find -iname "offerta*.md" -o -iname "listino*.md"` su tutto il repo non trova nessun file
canonico** (l'unico match è un esempio dentro System OMEGA, non un listino).

→ **Consiglio**: un solo `company/01-agency/OFFERTA.md` come fonte unica, e le skill che lo
**citano** invece di ripeterlo. Oggi un aumento di prezzo richiede 68 modifiche coordinate, e la
prima che sfugge diventa un preventivo sbagliato mandato a un cliente. È la Regola 1 di Karpathy,
applicata a DE.

### 2. `/lint-wiki` è documentato ma non esiste — l'operazione LINT è il buco

**Verificato**: `second-brain-vault/CLAUDE.md` documenta 6 operazioni e quattro comandi —
`/lint-wiki`, `/query-wiki`, `/synthesis`, `/research-topic`. L'operazione LINT è descritta bene
(*"link rotti o orfani, pagine contraddittorie o obsolete, gap tra quello che sappiamo e quello
che dovremmo sapere"*). Ma `ls .claude/skills | grep -i "lint|query-wiki|synthes|research-topic"`
**non restituisce nulla**: nessuna delle quattro skill esiste. È un puntatore che manda a
sbattere, esattamente il caso vietato dalla REGOLA PUNTATORI del `CLAUDE.md` di progetto.

Il pezzo per costruirla **c'è già**: `skill-contradiction-analyzer` confronta due skill e trova
ogni contraddizione con 15 rilevatori. Manca il ponte verso la wiki. Il controllo delle **note
orfane** invece esiste già, dentro `sync-wiki-totale/SKILL.md:31-32`
(`knowledge-cartographer` verifica 2-3 cross-link per pagina).

→ **Consiglio**: o si costruisce `lint-wiki` (contraddizioni + dati vecchi, riusando
`skill-contradiction-analyzer`, con gli orfani già coperti da `sync-wiki-totale`), o si **tolgono i
quattro comandi** da `second-brain-vault/CLAUDE.md`. Lasciarli documentati e assenti è il peggiore
dei tre stati.

### 3. DE ha "nessun task senza Memory" ma non "nessuna proposta senza nota"

**Verificato**: `grep -ni "memory|checkpoint|registra"` su `proposal-gate/SKILL.md` e
`beast-preventivi/SKILL.md` → **zero match in entrambi**. `proposal-gate` ha 9 punti bloccanti
(problem-first, awareness, pricing a catalogo, prove, scope 7gg, proprietà codice, supporto 90gg,
brand voice, timing) e **nessuno riguarda la tracciabilità**. `preventivo-auto` produce
`runs/<id>/listing.json` e un PDF, poi si ferma: nessuna nota, nessun registro.

Il principio però DE **ce l'ha già**, al livello sbagliato: la REGOLA ZERO del `CLAUDE.md` di
progetto dice *"Nessun task è 'fatto' finché non è salvato in Memory"*. Il video lo estende
all'artefatto commerciale.

→ **Consiglio**: un decimo punto in `proposal-gate` — *ogni preventivo emesso scrive una riga in
un registro con data, cliente, importo, stato e link*. Non è burocrazia: senza quel registro DE non
può rispondere a "quanti preventivi abbiamo mandato e quanti sono tornati", che è esattamente il
buco che [[tools/Tool_Tesoreria_Digital_Empire|la Tesoreria]] ha dichiarato aperto (B-043, *"DE non
misura un solo euro"*).

### 4. `beast-preventivi` ha già il valore-vs-costo, gli manca la proxy del tempo salvato

**Verificato**: `beast-preventivi/references/stages/02-pricing.md:19-31` contiene già *"Parti dal
valore, non dal costo — Non calcolare: ore × tariffa oraria"* con un esempio ROI su lead e
conversione di una landing page. **Il principio c'è, il gap è più stretto di come sembra.**

Quello che manca davvero, verificato leggendo il file:
- la **proxy del tempo salvato × frequenza** (`tempo persona per proposta × n° proposte al mese`),
  che è la formula giusta per i deliverable di tipo *automazione/agente*, dove non c'è un funnel
  da cui stimare i lead;
- la **struttura a 2 opzioni non pre-evidenziate**: `beast-preventivi/SKILL.md:83` impone
  *"Sempre 3 opzioni (Essenziale / Professionale / Full Service)"*, gerarchia implicita inclusa. Il
  video usa 2 opzioni **esplicitamente equivalenti** (*"nessuna delle due è quella giusta"*), che è
  una scelta diversa e vale come variante documentata, non come sostituzione.

### 5. La contraddizione sul retainer esiste da tempo in DE, e ora c'è un criterio per scioglierla

**Verificato con grep, quattro posizioni incompatibili nello stesso ecosistema**:

| File | Riga | Dice |
|---|---|---|
| `agency-scalping/SKILL.md` | 68 | *"Retainer > one-shot: revenue ricorrente = sopravvivenza"* |
| `cro-call/SKILL.md` | 1293 | *"PRIMA — Non vendiamo retainer."* |
| `cro-call/SKILL.md` | 2234, 3776 | *"Sprint, non retainer"* |
| `proposal-gate/SKILL.md` | 46 | *"EUR 0 canoni mensili (one-time)"* — **BLOCCA** |
| `cro-strategy-social-(ig-tiktok)/SKILL.md` | 468-472 | *"Agenzie con retainer infiniti ti fregano"* |

Oggi un agente che carichi `agency-scalping` e `proposal-gate` insieme riceve due ordini opposti.
Il video non prende una posizione ideologica: dà un **criterio** — retainer **quando l'automazione
deve cambiare forma nel tempo** (lingue, varianti, manutenzione), altrimenti one-time.

→ **Consiglio**: far girare `skill-contradiction-analyzer` sulla coppia
`agency-scalping` × `proposal-gate` (è lo strumento che DE ha già per questo, e a quanto risulta
non è mai stato usato su questa coppia) e, qualunque sia l'esito, scrivere **il criterio** invece
di ripetere lo slogan in ordine sparso.

### 6. La lezione "uploaded → draft" DE l'ha imparata una volta, in codice, e non l'ha scritta

**Verificato**: `grep -rni "polling|attendi lo stato|stato uploaded" --include="SKILL.md"
.claude/skills` → un solo match, in `ruflo/plugins/ruflo-swarm/skills/monitor-stream`, e riguarda
il tool Monitor, non le API esterne. **Nessuna skill operativa di DE codifica il pattern.**
Però `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py` implementa
esattamente quel ciclo (`poll_status()` con `while waited < max_wait_s`, attesa dello stato
`success`, `time.sleep(5)`), e c'è persino un `fliki_poll_only.py` per riprendere un polling
interrotto — cioè DE ha già pagato quella lezione su Fliki, ma solo in un file.

→ **Consiglio**: scrivere la regola una volta come convenzione (*"un'API che risponde con uno stato
intermedio va interrogata fino allo stato terminale, mai usata subito"*) più il passo di verifica a
monte (*"interroga il sistema esterno per sapere i nomi reali dei campi, non indovinarli"*). Ogni
integrazione futura di DE — PandaDoc, un CRM, un firmatario — la incontrerà.

### 7. PandaDoc non esiste in DE, e il preventivo si ferma al PDF

**Verificato**: `grep -ri "pandadoc" .claude/skills` → **1 solo match**, dentro
`agency-scalping/raw-sources/S002-scalping-agency-02.md` (un dump di materiale grezzo non
distillato). Nessuna integrazione, nessun riferimento operativo. `preventivo-auto` (PreventivoForge,
cliente Novacar) produce un PDF e finisce lì: **nessuna firma digitale, nessun pagamento, nessuna
nota di ritorno**.

→ **Consiglio (proposta, non urgenza)**: valutare un anello *documento firmabile + pagamento* a
valle di `beast-preventivi`/`proposal-gate`. Il guadagno non è il tool ma il dato: un documento
firmabile dice **quando** è stato aperto e **se** è stato firmato, cioè fornisce alla Tesoreria le
due date che oggi mancano. Da soppesare contro il vincolo DE *"€0 canoni mensili"* del punto 5 —
PandaDoc è un abbonamento, e il conflitto va deciso, non aggirato.

## Nota di trasparenza — limiti della fonte

- **Nessun documento è mai stato inviato davvero.** Tutto resta bozza `[DEV]` (chiave sandbox), il
  cliente è dichiaratamente finto, nessun euro incassato è mostrato.
- **Il codice della skill non è mai stato ingrandito**: `pandadoc.py`, `create_proposal.py`,
  `inspect_template.py` compaiono solo come nomi di file. Il `CLAUDE.md` generato non è mai stato
  aperto a schermo — se ne conosce il contenuto solo dal prompt che lo commissiona e dal riassunto
  che Claude ne fa (due fonti concordi, nessuna delle due è il file).
- **La scalabilità aziendale del pattern è rinviata** al corso a pagamento nella community Skool
  "Avanguardia Plus", non dimostrata.
- **Cosa NON è stato ingerito** (dietro paywall, riportato solo come esistente): corso *Claude Code
  Per Aziende* (4h52:49), lezione *PandaDoc* (49 min), corso *Costruisci La Tua Company Brain*,
  modulo *Preventivi Automatici*.

## Connessioni

- [[sources/Source_Nate_Herk_Claude_Second_Brain_Levels|Nate Herk — Every Level of a Claude Second
  Brain Explained]] — **la coppia più stretta della wiki**: Herk classifica i *livelli di retrieval*
  di un second brain (L1 parola esatta → L5 always-on), questo video descrive la *forma della
  memoria* che quei livelli interrogano. Herk aveva misurato DE a Livello 1-2 su 1.831 pagine;
  Karpathy spiega perché le tre operazioni (ingest/query/lint) sono ciò che tiene in vita quel
  livello nel tempo, non un upgrade tecnologico.
- [[sources/Source_Justin_Sung_Guida_Apprendimento|Justin Sung — Guida completa
  all'apprendimento (max18)]] — stesso lotto, e **la stessa diagnosi da due direzioni**: quello
  studio aveva trovato che `atoms.json` di DE non ha archi, *"DE produce isole, non reti"*. Il wiki
  di Karpathy è esattamente l'architettura in cui gli archi (backlink, note collegate, catalogo)
  sono il prodotto principale, non un accessorio.
- [[sources/Source_Giovanni_Beggiato_Guida_Agenzia_AI|Giovanni Beggiato — Come Avviare Un'Agenzia
  AI da 10.000€/Mese]] — **stesso autore**: quella è la guida commerciale completa (nicchia,
  matrice DIY/DWY/DFY, 6 metodologie di acquisizione, fulfillment), questa è il singolo deliverable
  tecnico venduto dentro quel modello. La matrice di pricing di lì e il value-based di qui sono lo
  stesso ragionamento a due livelli di zoom.
- [[sources/Source_Giovanni_Beggiato_CFO_AI_Claude|Giovanni Beggiato — Ho creato un CFO AI che
  controlla l'azienda H24 con Claude]] — **stesso autore, stesso principio architetturale**: lì
  estrazione / calcolo deterministico / interpretazione mai mescolati, con un cancello
  anti-invenzione; qui fonti immutabili / wiki mantenuto dall'AI / schema, con la regola *"i prezzi
  vivono solo in offerta.md"*. Due applicazioni della stessa idea — l'AI non deve poter inventare
  un numero che ha una fonte.
- [[tools/Tool_Tesoreria_Digital_Empire|Tesoreria Digital Empire]] — la regola *"nessuna proposta
  senza nota"* (Consiglio 3) è il pezzo mancante a monte della Tesoreria: senza un registro dei
  preventivi emessi, il reparto che conta i soldi non ha da dove leggere il fatturato promesso.
