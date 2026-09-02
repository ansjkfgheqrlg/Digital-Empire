# Video Analysis — "Ho creato un intero team di marketing AI con Claude Code in 20 minuti"

- **ID YouTube:** yJOCyyP77bA
- **Titolo:** Ho creato un intero team di marketing AI con Claude Code in 20 minuti
- **Canale:** Giovanni Beggiato (agenzia AI "Gentes AI", community "Avanguardia Plus" su Skool)
- **Durata:** 1194s = 19m54s
- **Data upload:** 2026-07-29
- **View count al momento dell'ingest:** 4.381
- **Lingua:** italiano
- **Frame guardati: 165/165 unici** (su 597 frame densi estratti, 432 scartati perché sotto soglia — vedi `coverage.md`)

---

## L'ARCHITETTURA DEL TEAM

### I 6 specialisti + 1 orchestratore

Ordine ufficiale confermato dalla slide capitoli (frame-015→018, @0:28-0:34) e dal file system (frame-333, frame-342, frame-364):

```
01 STRATEGA
02 ANALISTA CONCORRENZA
03 SPECIALISTA SEO
04 COPYWRITER
05 ESPERTO CONVERSIONI
06 MEDIA BUYER
```

Il narratore dice esplicitamente (00:03:01): *"abbiamo sei specialisti in parallelo oltre ad un orchestratore"* — quindi 6 agenti worker + 1 orchestratore che li coordina e assembla l'output finale.

### Cosa vota/cerca ogni specialista (frame-218/219/220, slide "COSA CERCA OGNI SPECIALISTA" — la più densa di informazione del video)

| Agente | Vota | Checklist |
|---|---|---|
| **STRATEGA** | Messaggio e Crescita | Test dei 5 secondi ("5 SEC"), Parole del cliente, Riacquisto e contatti |
| **SPECIALISTA SEO** | Trovabilità | Titoli delle pagine, Scheda locale curata, Chi esce in prima pagina? (esempio in slide: box "Idraulico Verona") |
| **ESPERTO CONVERSIONI** | Conversione | Percorso del cliente, Il modulo funziona?, Telefono cliccabile? (icona box "Prenota ora") |
| **ANALISTA CONCORRENZA** | Concorrenza | Concorrenti veri: 3-5, Recensioni a confronto, Prezzi visibili? (esempio in slide: "6.9, 300 recensioni") |
| **COPYWRITER** | Senza voto: Dimostra | Prima/Dopo, Soluzioni innovative, Siti che portano preventivi, I 3 testi più deboli |
| **MEDIA BUYER** | Senza voto: Verdetto | Tracciamento attivo? [✓], Pagina di destinazione [✓], Con riserve [⚠], Offerta chiara? [✗], Non pronto [✗] — box "TU DECIDI" |

**Regole della squadra** (stessa slide, in basso, banner "OGNI VOTO HA DIETRO UNO SPECIALISTA"):
1. "Ogni voto cita il sito"
2. "Mai numeri inventati"
3. "Difetti provati nel browser vero"

### Struttura cartelle (Company Brain, frame-004, frame-338, frame-364)

```
Company Brain/
├── _showcase
├── claude
├── obsidian
├── ..tmp
│   └── marketing-marcocalzature/
│       └── TUTTI-I-DELIVERABLE.html      ← output aggregato del run
├── areas
├── code
├── concepts
├── data
├── docs
├── engine
├── entities
├── labs/
│   ├── skool
│   ├── speed-to-lead
│   ├── studio
│   └── team-marketing-AI/
│       ├── assets
│       ├── scripts
│       └── skills/
│           ├── marketing-ads
│           ├── marketing-analisi
│           ├── marketing-competitor
│           ├── marketing-contenuti
│           ├── marketing-email
│           ├── marketing-funnel
│           ├── marketing-landing
│           ├── marketing-opportunita
│           ├── marketing-piano
│           ├── marketing-report
│           ├── marketing-seo
│           └── marketing-social
├── labs/team-marketing-AI/.../squadra/     ← cartella con i file agente .md
│   ├── analista-competitor.md
│   ├── copywriter-pmi.md
│   ├── esperto-conversioni.md
│   ├── specialista-seo.md
│   └── ... (stratega, media-buyer)
├── outputs
├── projects
├── scripts
├── self
├── sources
├── workspace
├── .env
├── .gitignore
└── mcp.json
```

➕ Inferenza: il pattern è "una skill per ogni deliverable" (`marketing-ads`, `marketing-seo`, ecc. — 11 skill visibili) più una cartella `squadra/` con gli agenti veri e propri (i file `.md` con `name/description/tools` in frontmatter). Il narratore lo conferma a parole (00:11:58): *"la struttura che io ho utilizzato è: ho creato un sacco di skill e poi ho fatto qui una mini squadra."*

### File agente reale letto in video — `copywriter-pmi.md` (frame-342, @11:22, IDE)

Trascrizione best-effort (testo piccolo, alcune parole segnate incerte con `[?]`):

```yaml
---
name: copywriter-pmi
description: Contributo qualitativo, senza voto. Usalo quando serve mostrare al
  titolare, con esempi concreti, quanto migliorerebbero i testi del sito: rivedi
  il titolo principale, il sottotitolo e le call to action. Utile nel funnel per
  mostrarlo in versione prima/dopo — è la parte dell'analisi che si capisce a
  colpo d'occhio.
tools: Read, Bash, WebFetch, WebSearch
---
```

Corpo del file (visibile a scorrere):

```
Sei il copywriter della squadra, specializzato in piccole e medie imprese
italiane. Non dai voti. Prendi i 3 testi più deboli del sito e li riscrivi
davanti ai suoi occhi, in versione prima/dopo. Prima/dopo convince più di
dieci pagine di analisi.

## Cosa cerchi
Passa in rassegna, in quest'ordine di importanza:
1. Il titolo principale della Homepage — la frase più letta di tutto il sito.
   Quasi sempre la più sprecata.
2. Il sottotitolo e la frase di supporto — dove perdi chi è il prodotto e
   perché scegliere te.
3. Le chiamate all'azione — i testi dei bottoni ("Invia", "Scopri di più",
   "Clicca qui") e le frasi che li accompagnano.
4. I titoli delle pagine di servizio o prodotto, se li trovi troppo generici.

## Come riconosci un testo debole
- Generico: potrebbe stare sul sito di qualsiasi azienda ("Qualità e
  professionalità al vostro servizio" non dice niente; "Siamo leader nel
  settore da 30 anni" invece di dirci come/perché).
- Parla dell'azienda, non del beneficio del cliente ("Soluzioni innovative"
  non dice cosa succede dopo).
- Bottoni muti: "Invia", "Scopri di più", "Clicca qui" non dicono cosa
  succede dopo il click.
- Vago: frasi lunghe e inutili, parole che il cliente tipo non userebbe mai.

## Come riscrivi
[testo tagliato dal frame successivo — non ricostruibile con certezza]
```

⚠️ Onestà sulla trascrizione: il frame-342 è l'unico che mostra questo file, la risoluzione dello screenshot rende alcune singole parole ambigue (es. "esempi principali" vs "esempi concreti"); la sezione "Come riscrivi" è tagliata fuori schermo e non è ricostruibile da nessun altro frame del video.

---

## IL PROMPT — integrale

Digitato/mostrato in chat all'inizio (frame-004, @0:06) e ridigitato dal vivo più avanti (frame-379, @12:32):

```
Per favore attiva il mio marketing team su questo URL: https://marcocalzature.it/en
```

Il narratore lo pronuncia identico a voce (00:12:06): *"posso dirgli 'per favore attiva il mio marketing team su questo URL'."*

Non ci sono altri prompt testuali mostrati nel video oltre a questo — il resto del run è autonomo (i 6 agenti lavorano senza ulteriori istruzioni umane).

---

## WALKTHROUGH CRONOLOGICO

**00:00–00:12** — Intro. Logo animato canale (icone: lente/SEO, grafico, megafono, matita, bersaglio, fotocamera — le 6 specialità). Giovanni a webcam: *"Ho costruito un intero marketing team con Cloud Code... basta incollare il sito di una piccola impresa e in un paio di minuti sei agenti restituiscono un'analisi completa... i concorrenti che avete estratti dal registro delle imprese, le parole chiave con cui i vostri clienti vi trovano ed i relativi volumi di ricerca ed un piano d'azione pronto all'uso."* Elenca i 6 ruoli a voce: stratega, analista dei concorrenti, specialista SEO, copywriter, esperto di conversioni del sito, media buyer.

**00:12–00:57** — Presentazione canale/agenzia: Gentes AI (sito `gentes.ai`, frame-023/024/025), community privata "Avanguardia Plus" (Skool, frame-027/028/029, 91 membri).

**00:58–04:34** — Spiegazione del metodo tramite slide Excalidraw "DA UN LINK AL PIANO MARKETING" (frame-005), 4 fasi:
1. **La scala dei dati veri** — Ricerca web dichiarata → Volumi di ricerca veri → Attività locali e recensioni → Registro imprese → Partita IVA dal sito → "Mai concorrenti inventati"
2. **Sei specialisti in parallelo**
3. **La mappa delle opportunità** — matrice Impatto/Sforzo con 4 quadranti: Fai subito, Pianifica, Opzionale, Lascia stare
4. **La consegna** — Report PDF per il cliente, Piano 90 giorni, Pagella, Radar concorrenti, Priorità

Narrazione (00:01:19–00:02:56): il team parte dall'URL, fa scraping per trovare la Partita IVA, poi incrocia col registro imprese per capire ATECO e concorrenti reali ("non inventerà mai concorrenti"), controlla attività locali/recensioni via crawling, usa API per volumi di ricerca ("chi vi sta rubando un po' di traffico").

**04:34–05:32** — Spiegazione grafico "iterazioni × tempo": curva rossa (umano, lenta, 2 settimane/14 giorni per arrivare alla stessa qualità) vs curva blu (AI, arriva all'80% pronto in 20 minuti, poi iterazioni umane/AI la portano a completamento). *"L'AI ci permette in magari iterazione 1, iterazione 5, iterazione 10 di avere un output pronto... queste iterazioni richiedono un totale di 20 minuti."*

**05:32–10:59** — Dettaglio di ogni specialista a voce (slide "COSA CERCA OGNI SPECIALISTA", frame-218):
- **Stratega**: "prova dei 5 secondi" (capisci cosa vendi e a chi in 5 secondi?), poi guarda le fonti di traffico (Google Search, Instagram, LinkedIn, YouTube) per giudicare la crescita.
- **Specialista SEO**: "trovabilità" — la persona che non ti conosce ma ha il tuo problema ti trova? Controlla titoli pagina, posizione SEO.
- **Esperto conversioni**: segue il percorso cliente click per click — moduli, contatti, telefono cliccabile vicino alla CTA.
- **Analista concorrenza**: confronta recensioni (numero e contenuto) con i competitor reali trovati via P.IVA/ATECO.
- **Copywriter**: prende la copy vera del sito, propone titoli prima/dopo.
- **Media buyer**: giudica se le ads di oggi sono soldi buttati o no, dà un voto e raccomandazioni.

**10:59–12:32** — Giovanni mostra l'IDE ("Antigravity IDE", VS Code-like) con la cartella `Company Brain`, apre le skill in `team-marketing-AI`, scorre i file degli agenti (ognuno con un "mini prompt" che descrive cosa cercare). Apre `copywriter-pmi.md` (vedi sopra). Digita il prompt e lancia il run su `marcocalzature.it/en` (frame-379).

**12:32–13:45** — Apre l'output aggregato `TUTTI-I-DELIVERABLE.html` (path locale: `/Users/giovannibeggiato/Desktop/Company Brain/tmp/marketing-marcocalzature/TUTTI-I-DELIVERABLE.html`). Tab: Pagella | Mappa opportunità | Campagne Ads | Funnel | Piano SEO | Sequenza Email | Calendario Social | Piano 90 giorni. Spiega che il "report da consegnare al cliente è il PDF separato (REPORT-CLIENTE.pdf)", mentre l'HTML è per uso interno/presentazione.

**13:45–14:33** — Sezione "Pagella Marketing" (fotografia attuale): dati aziendali (P.IVA, indirizzo), canali attivi, dove si perdono i clienti.

**14:33–15:32** — **Verifica dal vivo**: Giovanni apre Instagram (`instagram.com/marcocalzaturemilano`, frame-439) e Facebook reali del cliente per controllare i numeri dichiarati dal report. Risultato confermato a voce (00:14:33): *"vediamo che abbiamo circa 41.000 follower. Perfetto, 45, quindi ha fatto una buona approssimazione... Facebook 18 e 9 [18.9K]... abbiamo 18.000 follower, quindi perfetto. Tutti i dati, come vedete, sono effettivi."*

**15:32–16:03** — Torna sulla Pagella: tabella voti (Messaggio 6.0, Trovabilità 5.0, Conversione 6.5, Concorrenza 3.5, Crescita 7.0 — Voto finale 5.6/10). Commento: *"vogliamo un qualcosa di severo... aree di improvement."*

**16:03–17:00** — Dettaglio "Trovabilità": volumi di ricerca mensili per keyword mancanti sul sito (sneakers donna 90.500/mese, ballerine donna 60.500, sandali donna 40.500 — dedotto dal deliverable). Confronto col concorrente principale (Musto Calzature): *"onestamente non ho idea di chi siano, ma a quanto pare va meglio di noi su quasi tutto."*

**17:00–18:59** — Mappa delle opportunità (matrice impatto/sforzo, 12 mosse), poi tab Campagne Ads: struttura campagna Meta (Gruppo A retargeting+catalogo, Gruppo B freddo), targeting, budget (900/1200/1500 €/mese), metriche prima settimana (CPM, CTR, costo per acquisto, ROAS con soglie di allarme).

**18:59–19:54** — Chiusura: mostra il PDF cliente ("GENTES AI · MARKETING AUDIT · MARCO CALZATURE 5.6") con radar chart Marco vs Musto, tabella testa a testa con 4 concorrenti, matrice priorità (12 mosse numerate), pagina "Il primo passo" (una cosa sola: macchina recensioni + 3 righe di rassicurazione). CTA finale verso la community Skool "Avanguardia Plus" e il corso "Claude Code Corso Completo (4h)".

---

## RISULTATI MOSTRATI (con numeri visibili)

Cliente reale usato come demo: **Marco Calzature** (e-commerce scarpe donna + 3 boutique a Milano, `marcocalzature.it`, P.IVA 08547970153).

**Voto finale: 5.6/10** — media semplice di 5 aree:

| Area | Voto | Semaforo | In una riga |
|---|---|---|---|
| Messaggio | 6.0 | giallo | "Si capisce cosa vendono, non perché sceglierli: la storia vera (1970, famiglia, made in Italy) è nascosta nel 'chi siamo'" |
| Trovabilità | 5.0 | giallo | "Il brand si trova, [ma] le categorie con collezioni stagionali usa-e-getta e 3 boutique invisibili sulla mappa" |
| Conversione | 6.5 | giallo | "Percorso d'acquisto che fila (checkout ospite, click&collect), ma zero recensioni e rassicurazioni lontane dalla decisione" |
| Concorrenza | 3.5 | **rosso** | "Dove il cliente confronta Marco non esiste: Trustpilot 3.2 con 3 recensioni contro i 4.9/1176 di Turci" |
| Crescita | 7.0 | giallo | "Canali accesi (newsletter, 41K su Instagram, pixel attivi) ma nei mesi di lavoro niente riacquisto, SEO non-brand da scoprire" |

**Concorrenti reali trovati** (fonte: Google Places script + ricerca web):

| Nome | Dove | Note |
|---|---|---|
| Turci Calzature | P.le Stazione Genova 3, Milano | 4.9, 1176 recensioni, dal 1907, e-commerce completo |
| Velasca Donna | P.zza Giovine Italia 2, Milano | 4.8, 542 recensioni, monomarca made in Italy, storytelling |
| Musto Calzature | Via Dante 4, Milano | 4.8, 406 recensioni, a un civico dalla boutique di Marco, Klarna + WhatsApp |
| GHIGO Calzature | Viale Tunisia 2, Milano | 4.4, 476 recensioni |
| Walter Calzature | Corso Buenos Aires, Milano | 4.6, 299 recensioni |
| Pepperina | P.zza De Angeli 12, Milano | 4.8, 187 recensioni |

Dichiarazione di trasparenza nel deliverable: *"Registro imprese non disponibile per questa analisi (verifica KYC in corso); profilo camerale e concorrenti per ATECO non inclusi; la lista viene da Google Places e ricerca web."*

**"Verifiche dal vivo" (browser renderizzato, Chrome via MCP)** — sezione metodologica interna al report, molto rilevante:
- Test reale eseguito: click, aggiunta al carrello di un sandalo da 90€, checkout raggiunto e abbandonato prima del pagamento.
- Confermato dal vivo: zero widget recensioni su home/collezione/2 schede prodotto; nessuna info spedizioni/resi/taglie accanto al bottone "Aggiungi al carrello"; "Guida alle taglie" solo nel footer; spese di spedizione sotto i 99€ visibili solo al checkout dopo l'indirizzo; telefoni non cliccabili; nessun link Maps; blog `/blogs/news` in 404; collezioni tutte stagionali (nessuna evergreen); "made in Italy" assente dalla home.
- **Smentite dal vivo** (falsi positivi che una scansione statica avrebbe preso per buoni): categorie "assenti per i crawler senza JavaScript" → in realtà tradotte nel DOM renderizzato; hreflang "assenti" → presenti it/en/x-default nel DOM renderizzato; "non dichiara spedizioni solo Italia" → la pagina renderizzata dice esplicitamente "SHIPMENTS IN ITALY AND EUROPEAN UNION".
- Il voto Conversione è stato **ricalcolato da 6.0 a 6.5** proprio grazie a questa verifica dal vivo (scoperti: ritiro in negozio, checkout ospite con express pay, "Richiedi la taglia").
- **Ipotesi dichiarate esplicitamente dal sistema** (sezione di trasparenza): nessun numero di fatturato/margine/traffico fornito dal titolare; follower Instagram/Facebook osservati da risultati di ricerca (non dai profili — poi verificati dal vivo da Giovanni con esito positivo); Trustpilot 3.2 con 3 recensioni preso da snippet di ricerca (fetch diretto bloccato); ricerca Google eseguita da IP non italiano (da controverificare); registro imprese non interrogato (KYC in corso).
- Il deliverable segnala anche un'**incoerenza reale nei dati del cliente**, trovata confrontando le pagine renderizzate: la data di fondazione dichiarata cambia da pagina a pagina — "la storia vera (1970...)" nel copy analizzato, "A Milano dal 1986" nell'hero della home, "il chi siamo 1989(?)" — con la raccomandazione esplicita "una sola data ovunque".

**Mappa delle opportunità — le 12 mosse** (matrice impatto/sforzo, priorità 1→12):
1. Macchina recensioni: QR in cassa nelle 3 boutique + inviti Google/Trustpilot post acquisto — Alto impatto/Basso sforzo — "il divario più grande coi rivali, parte in due giorni"
2. Tre righe di rassicurazione sotto il bottone di acquisto (spedizioni, resi, guida taglie) — Alto/Basso
3. Hero e blocco storia riscritti, una sola data — Alto/Basso
4. Schede Google Business delle 3 boutique + pagina punti vendita — Alto/Basso
5. Widget recensioni con stelle sul sito — Alto/Medio
6. Collezioni evergreen per parola cercata — Alto/Medio — "paniere da 215.000 ricerche/mese scoperto"
7. Sequenze email (benvenuto, post acquisto, riattivazione) — Alto/Medio
8. Ads: Meta catalogo + retargeting, Google brand + Shopping — Alto/Medio, ma "solo dopo CAPI e recensioni"
9. Conversions API Meta + email su una sola piattaforma — Medio/Basso — "prerequisito del budget ads"
10. [contenuto editoriale] — Basso/Alto — "non ora"
11. Campagne TikTok — Basso/Alto — "non ora: nessun pixel, nessun asset video"
12. Marketplace (Zalando, Amazon) — Medio/Alto — "non ora: prima far rendere il canale [proprio]"

**Campagna Ads proposta** (tab Campagne Ads):
- 1 campagna Meta, obiettivo vendite. Gruppo A: retargeting + catalogo dinamico su saldi/outlet (offerta fino al 50%). Gruppo B: pubblico freddo per interessi sulla nuova collezione (offerta 10% primo ordine + spedizione gratis sopra 99€). 3 annunci per gruppo, A/B test 7 giorni.
- In parallelo: Google campagna brand ("marco calzature" + varianti) + Shopping standard, più retargeting Meta sempre attivo 30 giorni.
- Targeting: Gruppo A = visitatori 30gg + interazioni social 90gg, IT, donne 25-64; Gruppo B = IT, donne 25-54, interessi moda/calzature, esclusioni su acquirenti recenti e query fuori tema ("lavora con noi", "resi", "orari").
- Budget suddiviso:

| Budget mensile | Al giorno | Meta Gruppo A | Meta Gruppo B | Google brand + Shopping |
|---|---|---|---|---|
| 900 € | 30 € | 11 € | 11 € | 8 € |
| **1.200 € (raccomandato)** | 40 € | 14 € | 14 € | 12 € |
| 1.500 € | 50 € | 18 € | 14 € | 18 € |

- Soglie d'allarme metriche prima settimana: CPM sopra 15€ su Meta = "pubblico troppo stretto o creatività debole"; CTR sotto 0,8% su Meta = "l'annuncio non sembra funzionare"; ROAS sotto 1 dopo 30 giorni = "fermarsi a rivedere pagine, non annunci".

---

## CIÒ CHE IL VIDEO NON MOSTRA

- **Il codice sorgente completo di nessun agente** — solo `copywriter-pmi.md` viene aperto, e solo parzialmente (la sezione "Come riscrivi" è tagliata fuori dal frame successivo, mai più mostrata).
- **L'orchestratore stesso** — nessun file di orchestrazione, nessuna configurazione di come i 6 agenti vengono lanciati in parallelo (subagent Claude Code standard? Task tool? script esterno?) viene mostrato a schermo.
- **Le API usate** per volumi di ricerca, registro imprese, Google Places — il narratore dice più volte "abbiamo delle API collegate" ma non mostra mai né i nomi dei provider né le chiavi/configurazione (rimanda alla community a pagamento per il dettaglio: *"vado in dettaglio su che tipo di API ho utilizzato... per chi di voi è in community"*).
- **Il tempo reale di esecuzione del run** — c'è un salto netto tra "incolliamo il link" (12:40) e "ho questi due output" (12:46, pochi secondi di clock ma l'esecuzione reale richiede probabilmente diversi minuti); nessun timer a schermo, nessuna vista sul terminale che gira.
- **Il generatore del PDF cliente** — si vede solo il PDF finito (`REPORT-CLIENTE.pdf`), non lo script/skill che lo produce dall'HTML.
- **Errori o iterazioni fallite** — il video mostra un solo run pulito, mai un secondo tentativo, mai una correzione manuale in diretta, benché il narratore dica esplicitamente che il processo normale prevede iterazioni ("non è mai one-shot").
- **Il contenuto degli altri 4 file agente** (`analista-competitor.md`, `esperto-conversioni.md`, `specialista-seo.md`, più stratega e media-buyer) — visibili solo come nomi file nella sidebar, mai aperti.
- Il video è un long-form senza tagli visibili evidenti nella parte tecnica (niente jump-cut riconoscibili tra i 165 frame ispezionati oltre ai normali stacchi slide↔webcam↔schermo); non ci sono segnali di "fast-forward" dichiarato.

---

## CONFRONTO CON DIGITAL EMPIRE

**Cosa fa questo video meglio o più velocemente di come lavora DE oggi:**

1. **Verifica dal vivo con browser renderizzato reale.** Il sistema di Beggiato usa "Chrome via MCP" per fare gesti reali (click, add-to-cart, checkout abbandonato) e SMENTIRE dal vivo ipotesi sbagliate (es. hreflang dati per assenti da un fetch statico ma presenti nel DOM renderizzato). Il `market-audit` di DE (verificato in `.claude/skills/market-audit/SKILL.md`) usa solo `WebFetch` sulla homepage + 5 pagine chiave — **fetch statico, non browser renderizzato**. Non c'è nessun MCP di tipo Playwright/Puppeteer configurato in `.mcp.json` a livello di progetto (solo `claude-flow`, e risulta disconnesso in questa sessione). Questo è un gap concreto e misurabile.
2. **Trasparenza esplicita delle ipotesi non verificate** ("Ipotesi dichiarate": nessun numero di fatturato dato dal titolare, follower non verificati sui profili nativi, ricerca Google da IP non italiano da controverificare, ecc.). È un pattern di onestà epistemica che rende il deliverable difendibile davanti al cliente — non risulta un pattern esplicito e standardizzato nei deliverable DE attuali.
3. **Un solo comando in linguaggio naturale ("attiva il mio marketing team su questo URL")** attiva l'intera pipeline di 6 agenti + orchestratore senza altri prompt intermedi. Il ciclo DE (ADR-006, RECALL→SPEC→PRE-MORTEM→BUILD→GATE→REVIEW→TEST→COMMIT→RETRO) è più rigoroso ma comporta più touchpoint umani per lo stesso tipo di audit cliente.
4. **Auto-correzione interna al report**: il sistema di Beggiato ricalcola un voto (Conversione 6.0→6.5) *dentro lo stesso deliverable* quando la verifica dal vivo contraddice la prima stima — un log di revisione visibile al cliente, non solo un output finale statico.

**Cosa DE fa già meglio (o alla pari):**

1. **DE ha già un equivalente diretto**: `market-audit` (skill) orchestra **5 subagent paralleli** (`market-competitive`, `market-content`, `market-conversion`, `market-strategy`, `market-technical`) con classificazione automatica del tipo di business (SaaS/E-commerce/Agency/Local/Creator/Marketplace) — una sofisticazione di targeting che il video di Beggiato non mostra esplicitamente (il suo sistema sembra generico per e-commerce/PMI locali, senza un ramo di classificazione dichiarato a schermo).
2. **Governance**: DE ha Sentinelle dedicate (`sentinel-brandvoice`, `sentinel-quality`, `sentinel-drift`, `sentinel-cost`, `sentinel-security`) e Guild (`guild-copy-apsoc`, `guild-quality`) che vigilano su claim senza prova, drift architetturale, costi — un livello di governo che nel video di Beggiato non esiste (è un solo operatore, nessun secondo controllo automatico).
3. **Ecosistema Memory con ADR**: DE traccia le decisioni architetturali (15 ADR) e i checkpoint; il sistema di Beggiato non mostra alcuna persistenza di stato tra run (ogni run sembra da zero, cartella `tmp/marketing-<cliente>/`).
4. **PDF report già standardizzato**: DE ha `market-report-pdf` con gauge di punteggio, grafici a barre — sostanzialmente lo stesso tipo di output del PDF `REPORT-CLIENTE.pdf` mostrato nel video, quindi DE non parte da zero su questo fronte.

**Cosa va rubato, concretamente:**

- Il **pattern "verifica dal vivo che smentisce l'analisi statica"** — va portato dentro `market-audit`/`market-competitive`/`market-conversion` come step esplicito, non opzionale.
- Il blocco **"Ipotesi dichiarate"** a fine sezione — va reso un blocco standard obbligatorio in ogni deliverable `market-*` DE (coerente con lo spirito NO-FINTO che DE già applica ai video, va esteso ai report cliente).
- La **matrice impatto/sforzo con "Ha senso qui?"** come colonna esplicita di giustificazione per mossa — DE ha già priorità nei suoi report ma non necessariamente questa colonna di giustificazione riga-per-riga.

---

## CONSIGLI

*(direttiva Max 2026-09-02, `emperator.md` §6.10 — nomi verificati in `.claude/skills/` e `.claude/agents/` prima di citarli)*

1. **Cosa migliorare in DE con questa conoscenza**: aggiungere uno step di "verifica dal vivo" con browser reale dentro `market-audit` (fase 2, prima dell'aggregazione finale) — oggi il flusso usa solo `WebFetch`. Concretamente: dopo che `market-conversion` e `market-technical` producono le loro stime, un passaggio con un browser controllato (MCP Playwright, da aggiungere) deve confermare o smentire almeno i claim più critici (form funzionante, prezzi/spedizioni visibili, telefono cliccabile), esattamente come ha fatto Beggiato sul checkout di Marco Calzature. Senza questo, `market-audit` rischia di prendere per buoni claim statici che il rendering reale smentisce.

2. **Quale skill nuova creare**: non esiste oggi in `.claude/skills/` una skill dedicata alla verifica browser-reale generica (esiste solo `playwright-dev`, che è la guida per SVILUPPARE Playwright stesso, non per usarlo come tool di verifica CRO). Proposta: nuova skill `live-verification` (o estensione di `cro-ricerca`) che prende una lista di claim da verificare (spedizioni, form, CTA, recensioni, prezzo) e restituisce un blocco "Verifiche dal vivo / Smentite dal vivo" nello stesso formato mostrato nel video, riusabile da `market-audit`, `cro-ricerca` e `market-competitors`.

3. **Quale agente nuovo serve**: DE non ha un agente equivalente ad "analista-concorrenza" che incroci Partita IVA → registro imprese → ATECO → Google Places per trovare concorrenti *reali* e non ipotizzati. `market-competitive` (agente esistente, in `.claude/agents/`) fa "analisi competitiva" ma la sua descrizione non menziona verifica su registro imprese/P.IVA. Proposta: agente nuovo `competitor-kyc` (o potenziamento diretto di `market-competitive`) con lo stesso principio "mai concorrenti inventati" del video — obbligo di citare la fonte (Google Places, registro imprese, ricerca web) per ogni concorrente elencato.

4. **Quale workflow nuovo costruire**: un workflow "un link → pacchetto marketing completo per PMI/agenzia" analogo a quello del video, ma sopra l'infrastruttura DE esistente (`market-audit` + `market-report-pdf` + Sentinelle). Oggi DE ha i pezzi ma non un singolo comando end-to-end equivalente a "attiva il mio marketing team su questo URL" che produca in un colpo solo: pagella, mappa opportunità, campagne ads, funnel, piano SEO, sequenza email, calendario social, piano 90 giorni + PDF cliente — con verifica dal vivo integrata. È il gap più grande osservato.

5. **Quale workflow/skill esistente potenziare, e con quale pezzo preciso**: `market-audit` (SKILL.md, Phase 1 "Discovery") va potenziato aggiungendo, subito dopo la sezione 1.1 "Fetch the Target URL" (che oggi usa solo `WebFetch`), un passaggio di rendering reale + gesti (click/add-to-cart/checkout) prima del lancio dei 5 subagent — così anche `market-conversion` e `market-technical` ricevono dati "dal vivo" invece che dal solo HTML statico. Questo è il pezzo preciso, riproducibile 1:1 dal video (sezione "Verifiche dal vivo" del deliverable Marco Calzature).

**Nessun gap inventato oltre questi**: gli altri elementi del video (pagella con voti, mappa opportunità impatto/sforzo, PDF cliente con radar concorrenti, piano 90 giorni) hanno già un equivalente diretto e comparabile in `market-audit` + `market-report-pdf` — non c'è lì un gap reale da segnalare.
