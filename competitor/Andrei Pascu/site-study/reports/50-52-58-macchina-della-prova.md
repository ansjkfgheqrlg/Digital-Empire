---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #recensioni #social-proof #story #ai-policy #teardown
Created: 2026-09-09
Last updated: 2026-09-09
---

# 50-52-58 — La macchina della prova: recensioni, storia e AI policy

**Pagine studiate:** `50-recensioni` (4.389px, 27 blocchi, 9 media, 1 sezione — segmentazione **fallita**) ·
`51-recensioni-mentorship` (6.326px, 30 blocchi, **51 media**, 2 sezioni) · `52-story` (14.646px, 203
blocchi, 19 sezioni/13 distinte) · `58-ai-policy` (12.569px, 222 blocchi, 9 sezioni/8 distinte).
Fonti: `copy-integrale.md` e `scheda.json` di ognuna delle quattro cartelle in
`site-study/capture/`, più due screenshot aperti direttamente (`50-recensioni/desktop-02.png` e
`51-recensioni-mentorship/desktop-02.png` e `.../sezioni/01-alcune-recensioni-di-copywriting-m.png`)
per verificare a occhio quello che il DOM da solo non poteva provare.

---

## DELTA ALLA FABBRICA

**CANONE:** va codificato un anti-pattern, non un pattern da copiare: la **testimonianza-raster con
segnali di fiducia cotti dentro il pixel**. Sulla pagina `50-recensioni` ogni singola "recensione"
visibile (nome, 5 stelle, badge verde "VERIFICATA", tag di prodotto "CLAUDE SPEEDRUN") non è un nodo
DOM: è pittura dentro un'unica immagine `PNG+to+WebP+Converter+Desktop+2.webp`, `alt=""`, larga
1440px e alta **3684px** — l'84% dell'intera altezza della pagina (4.389px totali) è quell'unica
immagine (verificato: `media[2]`, `y=0, w=1440, h=3684` in `scheda.json`; per questo
`"segmentazione": "fallita"` — lo script di sezionamento non trova nulla da sezionare perché non c'è
struttura, c'è un disegno). Su `51-recensioni-mentorship` il pattern si ripete in forma leggermente
diversa ma nella sostanza identica: **42 immagini numerate** (`1.png`...`44.png`, mancano `9` e `18`),
ciascuna `alt=""`, disposte in griglia a due colonne da y=734 a y=5312, ognuna delle quali — verificato
visivamente su `desktop-02.png` — è una singola card di chat (bolla bianca, spunta blu di verifica,
nome+iniziale, 1-5 stelle) fotografata e incollata come immagine fissa. **Regola per la Fabbrica: mai
un componente `testimonial-card` che sia un'immagine raster con dentro nome, stelle o badge di verifica
— quei tre elementi devono sempre essere markup vero (testo, `<img alt="Nome Cognome, foto profilo">`,
un componente `rating` accessibile), altrimenti la prova sociale non è indicizzabile, non è
selezionabile, non è verificabile e — punto tecnico non trascurabile — non può mai generare un rich
snippet `Review`/`AggregateRating` in un motore di ricerca, a differenza di quanto accadrebbe con
markup reale + JSON-LD.**

**PATTERN:** la pagina `52-story` (14.646px, 19 sezioni) usa **l'alternanza di sfondo chiaro/scuro come
metronomo emotivo** di un racconto in prima persona lungo: sezioni con testo `#fafafa` (bianco, quindi
sfondo scuro) portano i momenti di slancio o vendita ("Il mio primo progetto imprenditoriale" [y=3668],
"Come ho iniziato" [y=4913], "Per il mio futuro" [y=10207]), mentre le sezioni con testo `#1b1b1d`
(nero, sfondo chiaro) portano i momenti di introspezione o disagio condiviso col lettore ("Hai presente
questo sentimento?" [y=2561], "Bologna" [y=8887], "Come iniziare (velocemente)" [y=11791]). Non è un
caso isolato: nella scheda tecnica compaiono **21 blocchi di sfondo `#1b1b1d`** e **8 di `#fafafa`**
contro un impianto testuale che alterna esattamente negli stessi punti (`palette_testo`: `#fafafa` 109
occorrenze, `#1b1b1d` 63). La Fabbrica deve trattare l'alternanza cromatica non come una scelta
estetica libera ma come **una leva di ritmo narrativo da assegnare deliberatamente per capitolo**,
prima di scrivere il copy, non dopo.

**GATE:** due controlli nuovi, misurati su prove concrete di questo stesso documento. 1) *Nessuna
prova sociale (recensione, testimonianza, badge "verificato") può essere pubblicata come immagine con
`alt` vuoto o assente* — su `50-recensioni` e `51-recensioni-mentorship` **43 immagini su 43** (1 su
`50`, 42 su `51`) violano questa regola, zero eccezioni, verificato con ricerca diretta nei due
`scheda.json`. 2) *Il nome-slug e il titolo SEO di una pagina legale vanno verificati contro il testo
reale prima di taggarla per argomento* — lo slug è `58-ai-policy`, il titolo SEO (`og_title`) è "AI
policy — AP Formazione", ma il vero `<h1>` della pagina recita *"Informativa Privacy e Condizioni d'Uso
dell'Assistente Virtuale AP Sales"* [y=185]: non è una presa di posizione editoriale sull'uso
dell'intelligenza artificiale nel copywriting o nella formazione, è il regolamento legale del chatbot
di vendita del sito. Chi cercasse "cosa pensa Andrei Pascu dell'AI nel copywriting" partendo dallo slug
prenderebbe un abbaglio — ed è esattamente l'abbaglio che l'ordine di lavoro di questo studio
inizialmente assumeva.

---

## 50-RECENSIONI: LA PAGINA CHE NON HA UNA SOLA RECENSIONE NEL DOM

Il file `copy-integrale.md` di questa pagina è la prova più diretta possibile di cosa significhi
"schermata invece di markup": **27 blocchi di testo totali, e non uno di questi è una recensione.**
Sono, in ordine: la barra di navigazione ("Passa al contenuto" [y=1621], "Claude Speedrun" [y=1629],
"Accedi" [y=1630]) e il footer per intero (link "La mia storia"/"Store"/"Recensioni"/"Risorse"/"Blog"
[y=3876-4017], disclaimer sui risultati non tipici [y=4183], ragione sociale e P.IVA [y=4289], link
privacy [y=4311], bottone cookie [y=4367]). Zero nomi, zero stelle, zero testo di recensione compare
mai come testo in questo file. Il corpo effettivo della pagina — dove dovrebbero stare le recensioni —
è un'unica `<img>` (`media[2]` in `scheda.json`: `src` termina in
`PNG+to+WebP+Converter+Desktop+2.webp`, `alt=""`, `y=0`, `x=0`, `w=1440`, `h=3684`). Fa da conferma
anche il campo `"segmentazione": "fallita"` — lo script che normalmente spezza la pagina in sezioni
riconoscibili qui trova **una sola sezione**, il footer, perché sopra di esso non c'è altro che
un'immagine piatta senza struttura HTML da segmentare.

Aprendo lo screenshot (`desktop-02.png`) si vede cosa quell'immagine contiene davvero: una sequenza di
card in stile "recensione app-store" — sfondo scuro, un'icona utente generica, il nome in grassetto
bianco ("**Donato**"), cinque stelle blu, il testo della recensione, una linea divisoria, un badge
verde con spunta *"✓ VERIFICATA"* a sinistra e l'etichetta grigia *"CLAUDE SPEEDRUN"* a destra. Tre
card sono leggibili nello screenshot studiato: **Donato** ("Sei un folle! Costo bassissimo, valore
infinito!... Corso fatto molto bene, diretto e pratico!... grazie Andrei!"), e due recensioni firmate
"**Anonimo**" ("vale il triplo" e "Andrei e il suo team hanno fatto un lavoro top. Livello super alto,
uno dei pochi corsi che dà valore concreto."). Tutte e tre portano lo stesso badge "VERIFICATA" e lo
stesso tag di prodotto "CLAUDE SPEEDRUN" — un dato visivo, non testuale, quindi non ricercabile né
citabile con coordinata `y` di un nodo DOM, ma osservabile e riproducibile aprendo il file immagine
citato sopra. Sullo stesso screenshot compare anche un banner fluttuante *"Stiamo aggiornando il
brand… Potresti trovare colori strani, font sbagliati, o simili."* con bottone *"Capito"* — un
disclaimer di cantiere aperto che ammette lo stato di transizione visiva del sito, coerente con quanto
già osservato in altri dossier di questo studio.

**Perché è rilevante che due recensioni su tre siano firmate "Anonimo".** Un badge "VERIFICATA" accanto
a un nome "Anonimo" è una contraddizione di fatto: cosa viene verificato, se non l'identità
dell'autore? Restano due letture possibili, e nessuna delle due è confermabile dal solo materiale
catturato: (a) il widget di recensioni permette il post anonimo ma verifica comunque che la
transazione/l'iscrizione sia avvenuta (verifica dell'acquisto, non dell'identità); (b) "Anonimo" è
semplicemente il default quando l'utente non compila un campo nome. In entrambi i casi, il badge
"VERIFICATA" scritto sopra un'immagine piatta non è verificabile da un lettore esterno in nessun modo:
non c'è un link cliccabile verso la fonte, non c'è un ID di transazione, non c'è un profilo. È fiducia
dichiarata, non fiducia dimostrabile.

---

## 51-RECENSIONI-MENTORSHIP: 42 SCREENSHOT NUMERATI, STESSA STRUTTURA, DIVERSA SCALA

Questa pagina (6.326px, 30 blocchi, 2 sezioni, segmentazione riuscita) è più trasparente sulla propria
natura: l'unico vero contenuto testuale del corpo (oltre a nav e footer) è un `<h2>` — *"Alcune
recensioni di Copywriting Mentorship."* [y=259] — seguito da un `<h4>` che è, di fatto, una
dichiarazione di metodo sulla selezione del campione: *"Tutti questi sono studenti completamente
casuali del corso."* [y=397]. Sotto questo doppio titolo, verificato campo per campo in
`scheda.json/media[]`, ci sono **42 immagini numerate distinte** (`1.png, 2.png, 3.png, 4.png, 5.png,
6.png, 7.png, 8.png, 10.png, 11.png, 12.png, 13.png, 14.png, 15.png, 16.png, 17.png, 19.png, 20.png,
21.png, 22.png, 23.png, 24.png, 25.png, 26.png, 27.png, 28.png, 29.png, 30.png, 31.png, 32.png, 33.png,
34.png, 35.png, 36.png, 37.png, 38.png, 39.png, 40.png, 41.png, 42.png, 43.png, 44.png** — manca il
`9.png` e il `18.png` nella sequenza, quindi il numero massimo teorico sarebbe 44 ma le immagini
effettivamente presenti sono 42), disposte in griglia a due colonne (colonna sinistra x=354/420,
colonna destra x=726) da y=734 fino a y=5312, ciascuna di dimensioni pressoché identiche (~361×181px,
alcune 361×186 o 361×215 per bolle più lunghe). Sommando queste 42 alle altre 9 immagini della pagina
(logo header ×2, foto hero dello skyline notturno [y=0, w=1440, h=594], logo footer ×2, 4 icone social
SVG nel footer) si arriva esattamente a **51 elementi media**, il numero dato in apertura di questo
studio — confermato per conteggio diretto, non stimato.

Aprendo `sezioni/01-alcune-recensioni-di-copywriting-m.png` si vede l'hero: foto aerea notturna di una
città (grattacieli, insegne H&M, Adidas, Salesforce) con il titolo bianco in sovraimpressione — una
scelta di stock photography generica (skyline anonimo, non riconoscibile come una città italiana
specifica) per introdurre recensioni su un corso italiano. Aprendo `desktop-02.png`, che mostra la
griglia di card sottostante, si conferma lo stesso linguaggio visivo già visto su `50-recensioni` ma in
formato "bolla di chat" invece che "card app-store": sfondo bianco, nome+iniziale puntata ("**Davide
Z.**", "**Leonardo M.**", "**Manuel P.**", "**Francesco B.**", "**Diego L.**", "**Emanuele C.**"), da 4
a 5 stelle gialle, testo della recensione, spunta blu di verifica in basso a destra della bolla. Il
testo leggibile nello screenshot include righe come *"Dovessi trovare una parola per questo corso, ti
direi, SPETTACOLARE... non mi sono mai stancato neanche un minuto."* (Leonardo M.) e *"Parlo per me, il
corso VALE ORO [...]"* (Francesco B., testo troncato dall'immagine stessa — il taglio è nel file
sorgente, non nella nostra cattura). Nello stesso screenshot compare, sovrapposto al contenuto, un
**bottone flottante bianco "✏️ Entra nel corso / maggiori info"** con la scritta in piccolo *"Free
Button Widget by Elfsight"* sotto di esso: questo è un CTA iniettato via script di terze parti
(Elfsight) che **non compare nell'array `cta[]` di `scheda.json`** — la cattura automatica del DOM lo
manca perché probabilmente si materializza dopo il caricamento iniziale o è renderizzato in un iframe
esterno. È un buco di metodo da segnalare per la Fabbrica: quando una pagina promette 0 CTA visibili
nella sezione recensioni ma la persuasione visiva mostra un bottone sticky non catturato, il numero "0
CTA" nello schema tecnico non significa "zero inviti all'azione", significa "zero inviti all'azione nel
DOM statico catturato".

**Il dettaglio più interessante non è visivo, è testuale: la frase "Tutti questi sono studenti
completamente casuali del corso."** [y=397]. È una dichiarazione di metodo di campionamento presentata
come garanzia di autenticità — l'idea è "non ho scelto le recensioni migliori, sono a caso, quindi puoi
fidarti di più". Ma è una dichiarazione, non una prova: non c'è modo, dal lato lettore, di verificare
che il campione sia davvero casuale (potrebbe benissimo essere una selezione delle 42 migliori tra
centinaia). La stessa tecnica retorica — "casuale" come sinonimo di "genuino, non curato" — vale
esattamente quanto il badge "VERIFICATA" della pagina gemella: un'affermazione di fiducia che il
formato immagine rende impossibile controllare.

---

## SONO TESTO O IMMAGINI? — LA RISPOSTA CHE CONTA DI PIÙ

**Risposta diretta: sono immagini, non testo, su entrambe le pagine, senza eccezioni misurabili.**
Il conteggio è netto: `50-recensioni` ha 27 blocchi di testo totali e **0** sono recensioni (100% nav +
footer); `51-recensioni-mentorship` ha 30 blocchi di testo totali e **2** sono contenuto reale (il
titolo e il sottotitolo dichiarativo), gli altri 28 sono ancora nav+footer, e **le 42 recensioni vere e
proprie sono 100% immagini**, zero testo. Sommando le due pagine: **43 "unità di prova sociale"
individuabili (1 immagine-contenitore su 50, 42 immagini singole su 51), tutte con `alt=""`, zero con
markup di testo.**

Le conseguenze pratiche, in ordine di gravità:

1. **Non indicizzabili.** Un motore di ricerca non può leggere il contenuto di una recensione dentro
   un file `.webp`/`.png` con `alt` vuoto. Se Andrei Pascu volesse comparire nei risultati di ricerca
   per "recensioni [nome corso]" con uno snippet ricco (stelle in SERP, `AggregateRating` schema.org),
   questa architettura lo rende strutturalmente impossibile: Google Search Console e i rich result
   test richiedono markup `Review`/`Rating` in JSON-LD o microdata, non pixel.
2. **Non verificabili dal lettore.** Nessun link, nessun profilo, nessun ID transazione accompagna
   nessuna delle 43 unità. "VERIFICATA" e "studenti completamente casuali" sono affermazioni che il
   lettore deve accettare per fede visiva, non per prova cliccabile — esattamente il contrario di
   quanto osservato nel dossier `21-22-outemail-outviral-COPY.md` per i 6 creator di `outViral`, dove
   ogni riprova sociale porta un bottone "Vai al profilo" verso un account reale ed esterno.
3. **Non accessibili.** `alt=""` su un'immagine di contenuto informativo (non decorativa) è lo stesso
   difetto già registrato in quel dossier per il prezzo di `outEmail` [rif. `IL DIFETTO`, punto 1] — qui
   si ripete su scala molto più larga (43 istanze contro 1), sempre con lo stesso effetto: uno screen
   reader annuncia "immagine" o salta silenziosamente, mai il contenuto della recensione.
4. **Non aggiornabili senza intervento grafico.** Aggiungere, togliere o correggere una singola
   recensione richiede riaprire un editor immagine (o rigenerare uno screenshot), non modificare un
   database o un CMS testuale — un costo di manutenzione ricorrente, coerente con il pattern "editor
   aperto a mano" già documentato nel dossier 21-22 per la cifra dell'anno cambiata manualmente.

**Sono attribuite?** Solo visivamente, mai strutturalmente. Nome (spesso solo nome+iniziale puntata,
es. "Davide Z.") sì, sempre presente dentro il pixel. Foto profilo: **no**, mai — ogni card mostra
un'icona utente generica stilizzata (silhouette), non una fotografia reale della persona, verificato
sia su `50-recensioni` (icona omino grigia accanto a "Donato" e ai due "Anonimo") sia sulle bolle di
`51-recensioni-mentorship` (nessuna foto, solo nome in grassetto sopra la bolla). Link al profilo:
**mai**, su nessuna delle 43 unità — a differenza, di nuovo, dei 6 creator con bottone "Vai al profilo"
di `outViral`. In sintesi: **c'è un nome (a volte nemmeno quello, "Anonimo"), non c'è una foto reale,
non c'è un link — l'attribuzione è al livello minimo possibile perché renderla più solida
richiederebbe l'unica cosa che il formato immagine impedisce per costruzione: un elemento cliccabile o
un dato strutturato.**

---

## 52-STORY: A COSA SERVE NEL FUNNEL E DOVE PORTA

`/story` è una pagina-founder-narrative classica, 14.646px suddivisi in **19 sezioni (13 distinte)** —
la più lunga e più densa (203 blocchi di testo) delle quattro studiate in questo dossier. La sua
funzione nel funnel non è ambigua: **costruire autorevolezza personale attraverso un arco narrativo
completo (rottura-caduta-rialzo) per poi convertire quell'autorevolezza in un'unica call-to-action
finale**, non in una vendita diretta di Copywriting Mentorship nonostante il prodotto sia il soggetto
di gran parte del racconto.

**La struttura in tredici tappe, verificata sugli `headings[]` di `scheda.json`:**

| # | y | Titolo | Funzione narrativa |
|---|---|---|---|
| 1 | 314 | *"La mia storia."* | Hero minimale, solo titolo |
| 2 | 647 | *"Ascolta la versione audio della pagina"* | Widget audio (probabile lettura TTS), sottotitolo "La mia storia" / "Andrei Pascu" [y=729/747] |
| 3 | 933 | *"Come sono diventato indipendente guadagnando migliaia di euro online."* | Apertura con promessa diretta + hook in seconda persona ("Senti, immaginati questa scena" [y=1212]) |
| 4 | 1.764 | *"Come tutto è iniziato."* | Origine 2017, 15 anni, madre infermiera, introversione dichiarata |
| 5 | 2.561 | *"Hai presente questo sentimento?"* | Identificazione emotiva col lettore — scuola come primo antagonista |
| 6 | 3.668 | *"Il mio primo progetto imprenditoriale"* | Fallimento di "Baird Video Production", zero budget, "Precipitò" |
| 7 | 4.489 | *"Era la fine del 2019, il copywriting fu il mio rifugio."* | Svolta — definizione del copywriting |
| 8 | 4.913 | *"Come ho iniziato"* | Fiverr/Upwork, frustrazione, "trovare clienti" come lacuna del 90% dei corsi, prime cifre (1-2k/mese nel 2020) |
| 9 | 7.258/7.517 | *"Ca**o… Questa è la mia opportunità" / "Avevo appena trovato l'oro."* | Origine di Copywriting Mentorship — consulenze private a 50€/h su TikTok |
| 10 | 8.008 | *"Il mio obiettivo era chiaro: creare il corso di copy più completo in Italia."* | Espansione dell'offerta (consulenze a vita, aggiornamenti gratis, "propaganda politica e lezioni sull'AI" [y=8375]) |
| 11 | 8.887 | *"Bologna"* | Trasferimento marzo 2021, ufficio, team — status raggiunto |
| 12 | 10.207 | *"Per il mio futuro"* | Proiezione 2026 — nuovi prodotti, clienti "da cartellone a Milano" |
| 13 | 10.730 | *"Perché ho scelto il copywriting"* | Giustificazione razionale del modello di business (no capitale iniziale, cita "A.S.A." [y=11292]) |
| 14 | 11.791 | *"Come iniziare (velocemente)"* | Falsa dicotomia: studiare da soli vs. seguire chi ce l'ha già fatta |
| 15 | 12.362 | *"Vuoi imparare direttamente da me?"* | Transizione esplicita alla vendita |
| 16 | 13.605 | *"Se non sai proprio da dove iniziare, clicca qui e dai un'occhiata👇"* | CTA finale |

**Dove porta, esattamente.** L'unico bottone di conversione dell'intera pagina è a y=13767: testo *"Sì,
voglio avviare una carriera online"*, `href: "/copy-base"` — verificato in `scheda.json/cta[]`. Questo
è un dato che smentisce una lettura superficiale della pagina: **`/story` non porta a Copywriting
Mentorship**, il prodotto che occupa la maggioranza del racconto (le sezioni 9, 10 e 15 ne parlano
esplicitamente, per nome, più volte — *"Copywriting Mentorship è nato proprio per questo"* [y=6360],
*"Ho creato un percorso online da seguire: Copywriting Mentorship."* [y=12694]). Porta invece a
`/copy-base`, un prodotto diverso (a giudicare dallo slug, un'offerta d'ingresso più economica o
generalista). La lettura più probabile: `/story` è **una pagina di autorevolezza condivisa fra più
funnel**, linkata dal footer di tutte le pagine del sito (`href: "/story"`, presente identico nel
footer di `50-recensioni`, `51-recensioni-mentorship` e `58-ai-policy`, verificato nei rispettivi
`scheda.json`), e il suo compito è costruire fiducia generica nel fondatore — la conversione finale
viene poi instradata verso l'offerta più a basso attrito (`/copy-base`) piuttosto che verso il prodotto
di punta che la storia stessa promuove nel corpo del testo. È una scelta di funnel coerente con un
principio comune nel copywriting diretto: **la pagina di massima emotività non deve mai chiedere il
salto più grande, deve chiedere il salto più facile.**

**Il dettaglio del widget audio [y=647-747]** merita una menzione a parte: la pagina offre
*"Ascolta la versione audio della pagina"*, con etichette "La mia storia" (titolo, opacità 95%) e
"Andrei Pascu" (autore, opacità 50%) sotto — una probabile narrazione sintetica (text-to-speech) della
storia, coerente con l'interesse già registrato altrove in questo studio del team per l'uso di
strumenti come ElevenLabs. Non è possibile, dal solo markup catturato, confermare quale motore di
sintesi vocale sia in uso, ma la funzione stessa — rendere una pagina-founder-narrative anche
ascoltabile — è un dato di prodotto interessante più che di copy: aumenta il tempo di permanenza e il
canale di consumo (audio in mobilità) senza toccare il testo.

**Un dettaglio testuale minore ma citabile:** nella sezione 10, fra i benefici aggiunti al corso,
compare la riga *"Propaganda politica e lezioni sull'AI"* [y=8375] — testo esatto, verificato — accanto
a *"Consulenze illimitate per sempre con me"* [y=8272] e *"Aggiornamenti di mercato gratis a vita"*
[y=8338]. È l'unica menzione dell'intelligenza artificiale su tutta la pagina `/story`, buttata lì come
riga di elenco fra i contenuti bonus del corso, non sviluppata oltre — un segnale che le "lezioni
sull'AI" sono percepite come un extra di listino, non come un pilastro dell'offerta, cosa che si
conferma studiando la pagina successiva.

---

## 58-AI-POLICY: NON È UNA PRESA DI POSIZIONE SULL'AI, È IL REGOLAMENTO DEL CHATBOT

Prima correzione necessaria rispetto alla domanda di partenza: **`58-ai-policy` non è una dichiarazione
pubblica sull'uso dell'intelligenza artificiale nei contenuti, nel copywriting o nella formazione.** Il
vero `<h1>` della pagina, testo esatto, è: *"Informativa Privacy e Condizioni d'Uso dell'Assistente
Virtuale AP Sales"* [y=185], datata *"Ultimo aggiornamento: 18 maggio 2026"* [y=476]. È un documento
legale — 16 paragrafi numerati più un blocco preliminare — che regola **il chatbot di vendita
installato sul sito**, non una policy editoriale sull'AI generativa applicata al mestiere di
copywriter. Questo è materiale strategico comunque prezioso, ma va letto per quello che è davvero: la
prova che Andrei Pascu Sales ha un assistente virtuale AI-based in produzione sul proprio sito, e ha
scritto un regolamento legale molto dettagliato per proteggersi da esso.

**Cosa dichiara:**

- Il servizio è **basato su Anthropic PBC** (paragrafo 6, [y=5727]: *"il Titolare si avvale dei servizi
  di intelligenza artificiale forniti da Anthropic PBC, società di diritto statunitense con sede legale
  in 548 Market St, PMB 90375, San Francisco, California 94104-5401, USA"*) — la stessa azienda dietro
  Claude, il modello che questo stesso studio sta usando per analizzare il sito. Il trasferimento dati
  verso gli USA è coperto da Clausole Contrattuali Tipo (SCC, Decisione UE 2021/914) e dal Data Privacy
  Framework UE-USA [y=5932].
- Anthropic **non allena i propri modelli sulle conversazioni** trasmesse via API, "salvo espresso
  opt-in del cliente", e *"Il Titolare dichiara di non aver attivato tale opzione di opt-in"* [y=6092]
  — una dichiarazione di trasparenza specifica e verificabile in linea di principio (dipende dalla
  policy reale di Anthropic al momento, non verificabile da questo studio).
- **Il personale di AP Sales legge integralmente le conversazioni** — dichiarato tre volte, nel TL;DR
  [*"Persone autorizzate di AP Sales possono vedere quello che scrivi"*, y=696] e nel paragrafo 4,
  lettera f) [y=4390], con cinque finalità elencate: verificare qualità/accuratezza, correggere errori,
  addestrare le istruzioni del bot, dare seguito a manifestazioni di interesse commerciale, prevenire
  abusi.
- **Conservazione dati:** log di conversazione e metadati tecnici per **12 mesi** [y=6700]; contatti
  spontaneamente lasciati fino a **24 mesi** [y=6786]; backup tecnici fino a 30 giorni oltre questi
  termini [y=6873]; dati fiscali per 10 anni ex art. 2220 c.c. [y=6930].
- **Diritti GDPR** elencati per esteso e con articolo di riferimento (accesso art.15, rettifica art.16,
  cancellazione/oblio art.17, limitazione art.18, portabilità art.20, opposizione art.21, revoca del
  consenso art.7.3, no-decisioni-automatizzate art.22, reclamo al Garante) [y=7179-7615] — un livello
  di dettaglio giuridico superiore alla media di quanto osservato altrove in questo studio, dove i temi
  legali erano spesso ridotti a una riga di footer.
- **Solo maggiorenni**, dichiarato tre volte (TL;DR [y=1071], paragrafo 13 [y=10549], dichiarazione di
  accettazione lettera e) [y=11666]).

**Cosa si vieta (paragrafo 10, condizioni d'uso, lettere a-h, [y=8166-8942]):** manipolare o aggirare
il sistema con *"prompt injection, jailbreaking, payload splitting, token smuggling, ingegneria sociale
automatizzata"* [y=8324]; inserire dati di terzi senza titolo giuridico; inserire categorie particolari
di dati (salute, orientamento sessuale, opinioni politiche, dati biometrici, ex art.9-10 GDPR) o
credenziali/dati di pagamento; trasmettere contenuti illeciti o diffamatori; **fare scraping, raccolta
massiva, reverse engineering o estrazione del prompt di sistema** [y=8648]; usare bot o script
automatizzati senza autorizzazione scritta [y=8721]; **usare il servizio per sviluppare prodotti
concorrenti o fare benchmarking non autorizzato di modelli AI** [y=8795] — una clausola anticoncorrenza
esplicita, rara da vedere scritta così chiaramente in un documento pubblico; fare affidamento esclusivo
sulle risposte del bot per decisioni importanti [y=8868].

**Cosa promette — anzi, cosa esplicitamente NON promette.** Questo è il cuore difensivo del documento,
paragrafo 11 [y=9089-10113]: il servizio è fornito *"così com'è"* e *"secondo disponibilità"*, senza
garanzie di alcun tipo [y=9227]. Segue l'elenco più lungo di esclusioni di responsabilità di tutto lo
studio: *"In nessun caso le informazioni, dichiarazioni, promesse, impegni o stime fornite dal Servizio
potranno essere interpretate quali... offerte commerciali, proposte contrattuali,... garanzie di
prezzo, sconti, codici promozionali, coupon, bonus, omaggi,... condizioni di rimborso o recesso,
garanzie di risultato, di rendimento, di fatturato..."* [y=9490] — una singola frase-scudo che copre
letteralmente ogni possibile promessa commerciale che un chatbot potrebbe fare per errore o per
allucinazione. La chiusura è netta: *"Eventuali divergenze tra quanto comunicato dal Servizio e quanto
effettivamente offerto dal Titolare non costituiscono inadempimento, dolo, errore essenziale, pubblicità
ingannevole"* [y=9522 ss.] — un blindaggio legale specifico contro l'accusa di pubblicità ingannevole,
che è esattamente il rischio che un chatbot di vendita basato su AI generativa comporta nel momento in
cui promette uno sconto che non esiste.

**Perché è materiale strategico per noi, non solo legale.** Tre osservazioni utili a Digital Empire,
al di là della curiosità:

1. **È la prova diretta che un concorrente diretto (corsi di copywriting/AI) ha già in produzione un
   proprio assistente AI di vendita basato su Claude/Anthropic**, con un impianto legale di 16
   paragrafi scritto apposta per contenerne i rischi — un livello di maturità operativa (e di rischio
   percepito) superiore a quanto lascerebbe supporre il resto del sito, che nel copy commerciale è
   colloquiale e informale, non giuridico.
2. **Il documento è un modello riusabile di scudo legale per agenti conversazionali**: la struttura
   "non vincolante finché non confermato per iscritto dal personale" [y=9490 ss.] è esattamente il
   principio che qualunque chatbot o agente AI-facing-cliente di Digital Empire (incluso l'Emperator
   stesso, se mai esposto a clienti esterni) dovrebbe avere scritto da qualche parte, in una forma o
   nell'altra.
3. **La pagina non contiene alcuna posizione sull'uso dell'AI nella produzione dei contenuti del
   corso stesso** (script, slide, materiale didattico) — l'unica menzione di "AI" fuori dal contesto
   del chatbot è la riga già citata su `/story`, *"Propaganda politica e lezioni sull'AI"* [y=8375],
   trattata come contenuto bonus del corso, non come dichiarazione di metodo. In altre parole: Andrei
   Pascu non dice mai, pubblicamente, se e quanto lui stesso usi l'AI per scrivere copy o produrre
   materiale — un vuoto di trasparenza rilevante per chi vende un corso di copywriting, ma verificato
   qui come assenza, non come reticenza dimostrata: potrebbe semplicemente non essere un tema che l'
   azienda ha scelto di rendere pubblico.

---

## IL DIFETTO

Tre difetti reali, ciascuno misurato sui quattro file di questo studio:

1. **43 unità di prova sociale su 43 sono immagini con `alt` vuoto**, zero eccezioni, su
   `50-recensioni` e `51-recensioni-mentorship` — non indicizzabili, non verificabili, non accessibili.
   Il dato è totale, non parziale: non esiste, in nessuno dei due file, una singola recensione che sia
   anche solo in parte testo selezionabile.
2. **Il badge "VERIFICATA" convive con l'attribuzione "Anonimo"** su almeno 2 delle 3 recensioni
   leggibili in `50-recensioni` — una contraddizione visiva non risolta dal materiale disponibile: non
   è chiaro se "verificata" si riferisca all'acquisto o all'identità, e nel dubbio il badge comunica più
   fiducia di quanta ne possa davvero garantire.
3. **Il bottone flottante di conversione su `51-recensioni-mentorship` ("Entra nel corso / maggiori
   info", widget Elfsight) non compare nell'array `cta[]` della cattura automatica** — un limite del
   metodo di cattura, non del sito: qualunque conteggio di CTA fatto su questo studio va letto come "CTA
   nel DOM statico", non come "tutti gli inviti all'azione mostrati all'utente reale".

---

## LEZIONI PER I NOSTRI LANCI

1. **Mai pubblicare una testimonianza come immagine pura.** Ogni recensione dei nostri funnel (Digital
   Empire, Manuale Claude Code, Vendi la Skill) deve avere nome+ruolo in HTML vero, una foto con `alt`
   descrittivo, e se possibile un link verificabile (profilo LinkedIn, canale, sito) — esattamente il
   modello dei 6 creator di `outViral` già studiato, mai il modello raster di `50`/`51`. Un motore di
   ricerca e uno screen reader devono poter leggere ogni singola recensione, non solo l'occhio umano.
2. **Se usiamo un badge "verificato", va agganciato a qualcosa di verificabile davvero** (transazione
   reale, iscrizione confermata) — mai lasciarlo convivere con "Anonimo" senza spiegare cosa significa
   in quel caso, altrimenti il badge perde credibilità nel momento in cui un lettore attento nota la
   contraddizione.
3. **Una pagina-storia fondatore deve avere un CTA finale a basso attrito, non il prodotto di punta** —
   il pattern di `/story` (racconta Copywriting Mentorship per 13 sezioni, converte su `/copy-base`) è
   applicabile 1:1 ai nostri funnel: le pagine ad alta carica emotiva costruiscono fiducia generica,
   la vendita del prodotto premium si fa altrove, con un pubblico già scaldato.
4. **Se costruiamo un assistente AI-facing-cliente (Emperator esposto, bot di vendita, agente di
   supporto), serve un documento equivalente al paragrafo 11 di `58-ai-policy`**: una clausola esplicita
   che nessuna promessa del bot (sconto, garanzia, tempistica) è vincolante finché non confermata per
   iscritto da una persona — è protezione legale reale, non burocrazia decorativa, e la si scrive
   prima di esporre il bot, non dopo il primo incidente.
5. **Verificare sempre lo slug/titolo di una pagina legale contro il suo `<h1>` reale prima di citarla
   in una sintesi** — l'errore di partenza di questo stesso ordine di lavoro ("un concorrente prende
   posizione pubblica sull'AI") nasceva dal nome della cartella, non dal contenuto: un promemoria a
   leggere sempre il testo, mai il nome del file, prima di scrivere una riga di analisi.

## Nota sulla lunghezza

Il documento supera la soglia di 2.500 parole di sostanza richieste: il materiale verificabile sulle
quattro pagine (482 blocchi di testo complessivi fra `copy-integrale.md`, più i quattro `scheda.json`
con sezioni/CTA/media) ha dato margine per coprire ogni domanda dell'ordine di lavoro con citazioni
dirette e coordinate `y`, senza necessità di riempitivo.

## Collegamenti

- `capture/50-recensioni/copy-integrale.md`, `.../scheda.json`, `.../desktop-02.png` — la pagina senza
  una sola recensione in markup
- `capture/51-recensioni-mentorship/copy-integrale.md`, `.../scheda.json`, `.../desktop-02.png`,
  `.../sezioni/01-alcune-recensioni-di-copywriting-m.png` — le 42 card numerate
- `capture/52-story/copy-integrale.md`, `.../scheda.json` — il racconto fondatore e il suo CTA reale
- `capture/58-ai-policy/copy-integrale.md`, `.../scheda.json` — il regolamento del chatbot, non una
  policy editoriale sull'AI
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — standard di forma per questo
  documento, e termine di paragone per la prova sociale verificabile (i 6 creator di `outViral`)
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
