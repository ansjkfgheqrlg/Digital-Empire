---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #recensioni #trustpilot #social-proof #story #ai-policy #teardown
Created: 2026-09-09
Last updated: 2026-09-09
---

# 50-52-58 — La macchina della prova: recensioni, storia e AI policy

**Pagine studiate:** `50-recensioni` (4.389px, 27 blocchi, 9 media, 1 sezione — segmentazione **fallita**) ·
`51-recensioni-mentorship` (6.326px, 30 blocchi, **51 media**, 2 sezioni) · `52-story` (14.646px, 203
blocchi, 19 sezioni/13 distinte) · `58-ai-policy` (12.569px, 222 blocchi, 9 sezioni/8 distinte).
Fonti: `copy-integrale.md`, `scheda.json` e `dom-blocks.json` di ognuna delle quattro cartelle in
`site-study/capture/`, più otto screenshot aperti direttamente per verificare a occhio quello che il
DOM da solo non poteva provare o aveva provato in modo fuorviante — vedi nota di metodo qui sotto.

**Nota di metodo, scritta perché è successa durante la stesura di questo stesso documento:** una prima
lettura di `50-recensioni`, basata su un'unica schermata parziale (`desktop-02.png`), aveva concluso che
l'intera pagina fosse un'immagine piatta senza alcuna prova verificabile. Aprendo l'intera sequenza
(`desktop-01.png` per primo) è emerso che quella lettura era sbagliata: la sezione contiene un vero
widget Trustpilot, non uno screenshot statico. Il documento che segue riporta la versione corretta, e la
correzione stessa è diventata un gate per la Fabbrica (vedi sotto). Questo per dire in apertura, con
tutta la trasparenza dovuta: **il verdetto finale su "sono verificabili le recensioni" è "dipende da
quale pagina" — sì su `50`, no su `51` — non una risposta unica come l'ordine di lavoro dava per
scontato.**

---

## DELTA ALLA FABBRICA

**CANONE:** questo sito usa **due meccanismi opposti sotto la stessa etichetta "recensioni".**
`50-recensioni` incorpora un **widget Trustpilot reale** — verificato aprendo `desktop-01.png`: un
badge con 5 stelle blu, *"4,9 su 5 stelle su_Trustpilot ↗"* (link esterno cliccabile), *"98 RECENSIONI
VERIFICATE"*, un contatore *"98 recensioni"*, un bottone *"Filtri"*, e più sotto singole card con nome
del recensore (alcuni nome+cognome reali: *"Simone Maiolino"*, *"David Marcan"*, *"Riki Signo"*), da 1 a
5 stelle, badge verde *"✓ VERIFICATA"* per ogni singola recensione, tag di prodotto a destra (osservati
sia *"CLAUDE SPEEDRUN"* sia *"VENDITA 101"* — il widget aggrega e filtra le recensioni di più prodotti
Andrei Pascu in un unico posto), un link *"Leggi di più"* per i testi lunghi, e in fondo un bottone
*"Mostra altre 12 recensioni"* (paginazione, quindi più delle sole recensioni visibili negli screenshot
catturati). `51-recensioni-mentorship`, al contrario, mostra **42 file immagine caricati singolarmente**
(`1.png`...`44.png`), senza alcun collegamento a una piattaforma esterna, zero rating aggregato, zero
badge di verifica indipendente — solo un checkmark blu disegnato dentro il pixel stesso dell'immagine.
**Per la Fabbrica: il primo è il modello da imitare quando costruiamo una pagina di prova sociale**
(piattaforma indipendente e verificabile pubblicamente, badge di verifica reale, aggregato pubblico,
filtro per prodotto, paginazione); **il secondo è l'anti-pattern da evitare** (screenshot incollati a
mano, nessun link, nessuna fonte controllabile, `alt=""` su tutti e 42).

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

**GATE:** tre controlli, il primo dei quali nato da un errore fatto e corretto dentro questo stesso
documento. 1) *Mai dichiarare "immagine piatta, quindi non verificabile" basandosi su una sola
schermata o sul solo conteggio di `scheda.json`* — va sempre aperta l'intera sequenza `desktop-NN.png`
della sezione sospetta prima di scrivere il verdetto. Prova diretta: la prima lettura di questo stesso
studio ha scambiato un widget Trustpilot reale (visibile fin da `desktop-01.png`) per contenuto piatto,
fermandosi a `desktop-02.png`. 2) *Nessuna immagine-recensione senza attribuzione minima (nome + fonte
esterna verificabile)* — su `51-recensioni-mentorship`, **42 immagini su 42** hanno `alt=""` e zero
link verso una fonte esterna, verificato per intero in `scheda.json/media[]`. 3) *Il nome-slug e il
titolo SEO di una pagina legale vanno verificati contro il testo reale prima di taggarla per
argomento* — lo slug è `58-ai-policy`, ma il vero `<h1>` recita *"Informativa Privacy e Condizioni
d'Uso dell'Assistente Virtuale AP Sales"* [y=185]: non è una presa di posizione editoriale sull'AI,
è il regolamento legale del chatbot di vendita del sito — l'abbaglio di partenza di questo stesso ordine
di lavoro, corretto qui.

---

## 50-RECENSIONI: UN WIDGET TRUSTPILOT REALE, INVISIBILE AL NOSTRO SCRAPER DI TESTO

Il file `copy-integrale.md` di questa pagina contiene **27 blocchi di testo, e nessuno di questi è una
recensione**: sono, in ordine, la barra di navigazione ("Passa al contenuto" [y=1621], "Claude
Speedrun" [y=1629], "Accedi" [y=1630]) e il footer per intero (link di menu, disclaimer, ragione
sociale, link privacy, bottone cookie). `dom-blocks.json` — il dump grezzo pre-filtro — conferma la
stessa lista, riga per riga identica: **anche a livello di estrazione più bassa, zero nodi DOM
contengono testo di recensione.** `scheda.json` segnala `"segmentazione": "fallita"` e un'unica
immagine fallback (`media[2]`: `PNG+to+WebP+Converter+Desktop+2.webp`, `alt=""`, `y=0`, `w=1440`,
`h=3684` — l'84% dell'altezza totale della pagina). Fin qui, i fatti tecnici puntano tutti nella stessa
direzione: "contenuto non estraibile come testo".

**Ma aprendo la sequenza di screenshot (`desktop-01.png` fino a `desktop-05.png`) la storia cambia
completamente.** `desktop-01.png` mostra, sopra le card di recensione, un blocco che il nostro
estrattore di testo non ha mai visto: l'intestazione *"Cosa dicono i miei studenti?"*, sotto di essa
cinque stelle blu piene, la scritta *"4,9 su 5 stelle su Trustpilot ↗"* — **Trustpilot per nome,
esplicito, con link esterno cliccabile** — e sotto ancora *"98 RECENSIONI VERIFICATE"*, un bottone
*"Filtri"* e il contatore *"98 recensioni"*. Scorrendo (`desktop-02.png` a `desktop-04.png`) si trovano
card di recensione reali, ciascuna con: un'icona-utente generica, un nome (in alcuni casi nome +
cognome verosimile: **Simone Maiolino**, **David Marcan**, **Riki Signo**; in altri solo nome:
**Shanthosh**, **Lorenzo**, **Alex**, **Croma_555**; in due casi **Anonimo**), da 1 a 5 stelle blu, il
testo della recensione, un badge verde *"✓ VERIFICATA"*, e un'etichetta di prodotto a destra — **due
etichette diverse osservate**, *"CLAUDE SPEEDRUN"* e *"VENDITA 101"*, a conferma che questo è un widget
aggregatore che raccoglie le recensioni di più prodotti Andrei Pascu in un solo posto, filtrabili.
Testo esatto di alcune card: *"Il corso è pratico, ha il giusto livello di teoria per capire, lo impari
ed esegui, lo personalizzi per te. Assolutamente ipersodisfatto"* (Shanthosh); *"King"* (Alex, la
recensione più corta osservata); *"ottima, corso clamoroso. ritmo perfetto"* (Croma_555); *"Ogni corso
di Andrei è una garanzia !"* (Simone Maiolino); *"Riguardo v101 direi che è il corso migliore dopo cm4,
ogni parola è una cosa da annotarsi... Se non ti fidi di lui allora non provare neanche a iniziare un
percorso online."* (Riki Signo, su Vendita 101); la card di David Marcan è troncata con un link *"Leggi
di più"* — segno di un componente che gestisce anche il testo lungo con un accordion, non solo un
elenco statico. In fondo a `desktop-04.png` compare il bottone *"Mostra altre 12 recensioni"*: il
widget è paginato, quindi le recensioni visibili nei cinque screenshot catturati (circa 12-13 card
leggibili) sono solo una frazione delle 98 dichiarate.

**Perché il nostro scraper non le ha viste.** Il pattern è coerente con un widget di terze parti
iniettato via JavaScript (tipicamente Trustpilot distribuisce i propri embed così, spesso dentro un
iframe) che si materializza dopo lo snapshot DOM usato dal nostro strumento per l'estrazione testuale —
lo stesso identico problema già registrato nel dossier gemello di questo studio per il bottone
flottante Elfsight su `51-recensioni-mentorship` (vedi sotto), solo su scala più grande qui. Il nome
generico del file immagine di fallback (`PNG+to+WebP+Converter+Desktop+2.webp`) e il flag
`"segmentazione": "fallita"` sono sintomi della **nostra** pipeline di cattura quando incontra contenuto
che non riesce a scomporre in blocchi di testo — non prova che il sito stesso nasconda qualcosa dietro
un'immagine.

**Cosa resta davvero incerto, con onestà.** Non abbiamo visitato Trustpilot.com per confermare
indipendentemente che il profilo esista e che il punteggio 4,9/5 coincida — è fuori dal perimetro di
questa cattura, che riguarda solo il sito di Andrei Pascu. Non sappiamo nemmeno se l'implementazione
usata da Andrei Pascu esponga anche dati strutturati (JSON-LD `Review`/`AggregateRating`) leggibili da
Google — dipende da come Trustpilot stesso genera il proprio widget embed, un dettaglio che il nostro
scan, fallito su questa sezione, non può confermare né escludere. Quello che possiamo affermare con
certezza, verificato: il badge dichiara una fonte esterna nota e nominata, il punteggio è aggregato
(98 recensioni, 4,9/5), ogni recensione porta un badge di verifica indipendente dalla piattaforma
terza, e il meccanismo è paginato — tre caratteristiche che nessuna delle 42 immagini di
`51-recensioni-mentorship` possiede.

**Il dettaglio "Anonimo" + "VERIFICATA" non è una contraddizione, va corretto rispetto a una lettura
precedente.** Su Trustpilot (come sulla maggior parte delle piattaforme di recensioni verificate),
"verificata" significa che l'autore ha completato una transazione o è stato invitato a recensire in
seguito a un acquisto confermato — non che abbia rivelato la propria identità. Un recensore può restare
"Anonimo" e avere comunque una recensione verificata nel senso tecnico del termine. Va notato comunque
un limite estetico reale: sulla card resta comunque impossibile, per un lettore esterno, risalire a
*chi* sia "Anonimo" o confermare *quale* acquisto abbia generato quella specifica verifica — la fiducia
nel sistema Trustpilot è delegata, non verificabile riga per riga dal lettore.

**Un difetto reale, non corretto dalla nuova lettura:** su tutti e cinque gli screenshot analizzati
resta visibile, fissato in basso a sinistra, un banner *"Stiamo aggiornando il brand… Potresti trovare
colori strani, font sbagliati, o simili."* con bottone *"Capito"* — un disclaimer di cantiere aperto
che copre parzialmente il testo delle recensioni sottostanti su schermi piccoli, friction reale per chi
sta leggendo la prova sociale proprio mentre decide se fidarsi.

---

## 51-RECENSIONI-MENTORSHIP: 42 SCREENSHOT NUMERATI, NESSUN WIDGET DIETRO

Qui la verifica incrociata conferma la prima lettura senza correzioni: `dom-blocks.json` e
`copy-integrale.md` coincidono riga per riga (verificato), la `scheda.json` segnala
`"segmentazione": "ok"` (a differenza di `50`), e i due unici blocchi di testo reali nel corpo pagina
sono un `<h2>` — *"Alcune recensioni di Copywriting Mentorship."* [y=259] — e un `<h4>` dichiarativo sul
metodo di selezione: *"Tutti questi sono studenti completamente casuali del corso."* [y=397]. Il fatto
che l'estrazione testuale qui abbia **funzionato correttamente** (a differenza di `50`) è un segnale
strutturale in più: non c'è un widget nascosto da mancare, il DOM è stato letto per intero e ha
semplicemente trovato solo immagini sotto quei due titoli.

Sotto il doppio titolo, verificato campo per campo in `scheda.json/media[]`, ci sono **42 immagini
numerate distinte** (`1.png, 2.png, 3.png, 4.png, 5.png, 6.png, 7.png, 8.png, 10.png, 11.png, 12.png,
13.png, 14.png, 15.png, 16.png, 17.png, 19.png, 20.png, 21.png, 22.png, 23.png, 24.png, 25.png, 26.png,
27.png, 28.png, 29.png, 30.png, 31.png, 32.png, 33.png, 34.png, 35.png, 36.png, 37.png, 38.png, 39.png,
40.png, 41.png, 42.png, 43.png, 44.png** — manca il `9.png` e il `18.png` nella sequenza — disposte in
griglia a due colonne (colonna sinistra x=354/420, colonna destra x=726) da y=734 fino a y=5312,
ciascuna ~361×181px. Sommando queste 42 alle altre 9 immagini della pagina (logo header ×2, foto hero
skyline notturno [y=0, w=1440, h=594], logo footer ×2, 4 icone social SVG) si arriva esattamente a **51
elementi media**, il numero dato in apertura di questo studio — confermato per conteggio diretto.

Aprendo `sezioni/01-alcune-recensioni-di-copywriting-m.png` si vede l'hero: foto aerea notturna di una
città anonima (grattacieli, insegne H&M, Adidas, Salesforce) con il titolo bianco in sovraimpressione.
Aprendo `desktop-02.png`, che mostra la griglia sottostante, si conferma il linguaggio "bolla di chat":
sfondo bianco, nome+iniziale puntata ("**Davide Z.**", "**Leonardo M.**", "**Manuel P.**", "**Francesco
B.**", "**Diego L.**", "**Emanuele C.**"), da 4 a 5 stelle gialle, testo della recensione, **uno
spunta blu di verifica disegnato dentro il pixel dell'immagine stessa** — non un badge di sistema come
il "VERIFICATA" di Trustpilot, solo un'icona grafica fissa, identica su tutte le 42 card, senza alcun
collegamento a una piattaforma che la confermi. Testo leggibile: *"Dovessi trovare una parola per
questo corso, ti direi, SPETTACOLARE... non mi sono mai stancato neanche un minuto."* (Leonardo M.);
*"Parlo per me, il corso VALE ORO [...]"* (Francesco B., testo troncato nel file immagine sorgente
stesso). Sovrapposto al contenuto compare un **bottone flottante bianco "✏️ Entra nel corso / maggiori
info"** con etichetta *"Free Button Widget by Elfsight"* — un CTA iniettato via script di terze parti
che **non compare nell'array `cta[]` di `scheda.json`**, lo stesso identico limite di cattura (widget
JS non visto dallo scan) osservato su scala maggiore su `50-recensioni`. Il numero "0 CTA" nella
sezione recensioni di `51` significa quindi "zero CTA nel DOM statico catturato", non "zero inviti
all'azione mostrati all'utente reale".

**Il dettaglio testuale più interessante resta la frase "Tutti questi sono studenti completamente
casuali del corso."** [y=397] — una dichiarazione di metodo di campionamento presentata come garanzia
di autenticità, non verificabile dal lettore: non c'è modo di confermare che il campione sia davvero
casuale (potrebbe essere una selezione delle 42 migliori tra centinaia). È l'esatto contrario del
meccanismo di `50`, dove l'aggregato (98 recensioni, 4,9/5) è calcolato da una piattaforma terza e non
dichiarato dal venditore stesso.

---

## SONO TESTO O IMMAGINI? — LA RISPOSTA CORRETTA, PAGINA PER PAGINA

**Su `51-recensioni-mentorship`: sono immagini, senza eccezioni.** 30 blocchi di testo totali, di cui
solo 2 sono contenuto reale (titolo + sottotitolo dichiarativo), gli altri 28 sono nav+footer, e **le 42
recensioni sono il 100% immagini**, zero testo, tutte `alt=""`, verificato sia in `scheda.json` sia in
`dom-blocks.json`.

**Su `50-recensioni`: sono testo reale, gestito da un widget esterno (Trustpilot) — il nostro
strumento di cattura non è riuscito a leggerle come testo, ma questo è un limite della cattura, non
del sito.** Correzione esplicita rispetto a una prima lettura basata su una sola schermata parziale.

Le conseguenze pratiche divergono nettamente fra le due pagine:

1. **Indicizzabilità.** Su `51`, impossibile per costruzione: nessun motore di ricerca legge testo
   dentro un `.png` con `alt=""`. Su `50`, dipende dall'implementazione di Trustpilot (fuori dal
   perimetro di questa cattura) — ma un badge Trustpilot pubblico con un profilo aggregato è, per sua
   natura, un segnale di fiducia già indicizzato altrove (sul profilo Trustpilot stesso), anche se la
   singola card sulla pagina di Andrei Pascu non lo fosse.
2. **Verificabilità dal lettore.** Su `51`, zero: nessun link, nessun profilo, nessun ID transazione.
   Su `50`, parziale ma reale: il lettore può cliccare *"su Trustpilot ↗"* e verificare l'aggregato
   pubblicamente, anche se non può risalire alla singola transazione dietro ogni singola card.
3. **Accessibilità.** Su `51`, stesso difetto già registrato nel dossier `21-22` per il prezzo di
   `outEmail` (`alt=""` su contenuto informativo, non decorativo) — qui su scala 42 volte più larga.
   Su `50`, non verificabile da questa cattura (il widget non è stato letto affatto dal nostro
   estrattore, quindi non possiamo dire se Trustpilot stesso lo renda accessibile).
4. **Manutenzione.** Su `51`, ogni aggiunta/correzione richiede riaprire un editor immagine — costo
   ricorrente. Su `50`, la gestione è delegata alla piattaforma terza, zero intervento manuale per
   nuove recensioni.

**Sono attribuite?** Su `50`: sì, con nomi spesso completi e verosimili (**Simone Maiolino**, **David
Marcan**, **Riki Signo**), foto profilo **mai** (icona generica), link al singolo autore **mai**
(il link porta all'aggregato Trustpilot, non al singolo recensore) — ma il badge "VERIFICATA" ha un
significato di sistema reale (transazione confermata), anche se non un'identità disclosata. Su `51`:
solo nome+iniziale puntata (o niente), foto profilo mai, link mai, verifica mai — il livello minimo
possibile di attribuzione.

---

## 52-STORY: A COSA SERVE NEL FUNNEL E DOVE PORTA

`/story` è una pagina-founder-narrative classica, 14.646px suddivisi in **19 sezioni (13 distinte)** —
la più lunga e più densa (203 blocchi di testo) delle quattro studiate in questo dossier. La sua
funzione nel funnel non è ambigua: **costruire autorevolezza personale attraverso un arco narrativo
completo (rottura-caduta-rialzo) per poi convertire quell'autorevolezza in un'unica call-to-action
finale**, non in una vendita diretta di Copywriting Mentorship nonostante il prodotto sia il soggetto
di gran parte del racconto.

**La struttura in sedici tappe, verificata sugli `headings[]` di `scheda.json`:**

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
storia. Non è possibile, dal solo markup catturato, confermare quale motore di sintesi vocale sia in
uso, ma la funzione stessa — rendere una pagina-founder-narrative anche ascoltabile — è un dato di
prodotto interessante più che di copy: aumenta il tempo di permanenza e il canale di consumo (audio in
mobilità) senza toccare il testo.

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

Tre difetti reali, ciascuno misurato sui quattro file di questo studio (uno dei quali è un difetto
del NOSTRO metodo, dichiarato per trasparenza):

1. **Il conteggio automatico di questo stesso studio ha inizialmente scambiato un widget Trustpilot
   reale per un'immagine piatta non verificabile**, perché la prima lettura si è fermata a una sola
   schermata parziale (`desktop-02.png`) invece di aprire l'intera sequenza. Corretto in questo
   documento aprendo `desktop-01.png` per primo. Resta invece confermato, senza correzioni, che le 42
   immagini di `51-recensioni-mentorship` sono innegabilmente prive di testo e di fonte verificabile.
2. **42 immagini su 42 su `51-recensioni-mentorship` hanno `alt` vuoto**, zero eccezioni — non
   indicizzabili, non verificabili, non accessibili. Il dato è totale, non parziale.
3. **Il bottone flottante di conversione su `51-recensioni-mentorship` ("Entra nel corso / maggiori
   info", widget Elfsight) non compare nell'array `cta[]` della cattura automatica** — lo stesso
   identico limite di metodo che ha nascosto il widget Trustpilot su `50`, qui su scala più piccola.
   Qualunque conteggio di CTA fatto su questo studio va letto come "CTA nel DOM statico", non come
   "tutti gli inviti all'azione mostrati all'utente reale".

---

## LEZIONI PER I NOSTRI LANCI

1. **Se costruiamo una pagina di prova sociale, il modello da copiare è `50-recensioni`, non `51`:**
   un aggregatore di recensioni indipendente e verificabile pubblicamente (Trustpilot o equivalente),
   con badge di verifica per singola recensione, aggregato pubblico cliccabile, e filtro per prodotto —
   mai una galleria di screenshot incollati senza fonte.
2. **Mai pubblicare una testimonianza come immagine pura senza un aggancio esterno verificabile.** Ogni
   recensione dei nostri funnel deve avere nome+ruolo in HTML vero, o essere gestita da un widget di una
   piattaforma terza con un aggregato pubblico controllabile — mai il modello raster puro di `51`
   (42 immagini, zero fonte, zero link).
3. **Una pagina-storia fondatore deve avere un CTA finale a basso attrito, non il prodotto di punta** —
   il pattern di `/story` (racconta Copywriting Mentorship per 13 sezioni, converte su `/copy-base`) è
   applicabile 1:1 ai nostri funnel: le pagine ad alta carica emotiva costruiscono fiducia generica,
   la vendita del prodotto premium si fa altrove, con un pubblico già scaldato.
4. **Se costruiamo un assistente AI-facing-cliente (Emperator esposto, bot di vendita, agente di
   supporto), serve un documento equivalente al paragrafo 11 di `58-ai-policy`**: una clausola esplicita
   che nessuna promessa del bot (sconto, garanzia, tempistica) è vincolante finché non confermata per
   iscritto da una persona — è protezione legale reale, non burocrazia decorativa, e la si scrive
   prima di esporre il bot, non dopo il primo incidente.
5. **Mai chiudere un verdetto tecnico su una sola schermata o su un conteggio JSON, quando lo strumento
   segnala "segmentazione fallita" o un'immagine dal nome generico** — apre sempre l'intera sequenza di
   screenshot prima di scrivere "non verificabile". È l'errore fatto e corretto in questo stesso
   documento, ed è esattamente il tipo di falso negativo che farebbe scartare a un cliente una prova
   sociale reale (Trustpilot) scambiandola per fuffa.

## Nota sulla lunghezza

Il documento supera la soglia di 2.500 parole di sostanza richieste: il materiale verificabile sulle
quattro pagine (482 blocchi di testo complessivi fra `copy-integrale.md`, più i quattro `scheda.json`
con sezioni/CTA/media, più otto screenshot aperti direttamente) ha dato margine per coprire ogni domanda
dell'ordine di lavoro con citazioni dirette e coordinate `y`, inclusa la correzione di un errore fatto
durante la stesura stessa.

## Collegamenti

- `capture/50-recensioni/copy-integrale.md`, `.../scheda.json`, `.../dom-blocks.json`,
  `.../desktop-01.png` a `.../desktop-05.png` — il widget Trustpilot reale, corretto rispetto alla
  prima lettura parziale
- `capture/51-recensioni-mentorship/copy-integrale.md`, `.../scheda.json`, `.../dom-blocks.json`,
  `.../desktop-02.png`, `.../sezioni/01-alcune-recensioni-di-copywriting-m.png` — le 42 card numerate
- `capture/52-story/copy-integrale.md`, `.../scheda.json` — il racconto fondatore e il suo CTA reale
- `capture/58-ai-policy/copy-integrale.md`, `.../scheda.json` — il regolamento del chatbot, non una
  policy editoriale sull'AI
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — standard di forma per questo
  documento, e termine di paragone per la prova sociale verificabile (i 6 creator di `outViral`)
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
