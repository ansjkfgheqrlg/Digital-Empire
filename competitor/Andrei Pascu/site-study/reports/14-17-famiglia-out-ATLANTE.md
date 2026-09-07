---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #squarespace #famiglia-out #design-system #reference
Created: 2026-09-07
Last updated: 2026-09-07
---

# ATLANTE VISIVO — la famiglia "out*" (outEmail, outFunnel, outHeadline, outViral)

Le sezioni **rappresentanti di gruppo** (`rappresentante: true` in `scheda.json` — le sezioni con la
stessa firma sono lo stesso blocco ripetuto, contate una sola volta) delle quattro pagine, aperte una
per una con lo strumento di visione e raggruppate **per ruolo**, non per pagina. Il confronto
numerico e lo schema ricorrente completo sono nel documento gemello
[14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md); qui si guarda.

**Le immagini** vivono in `../capture/<slug>/sezioni/`. Ogni misura sotto viene dal blocco
corrispondente in `scheda.json → sezioni[]`.

---

## RUOLO 1 — L'HERO

### outEmail
![outEmail hero](../capture/14-arma-outemail/sezioni/01-apriresti-questa.png)

**Cosa si vede:** sfondo fotografico blu petrolio granuloso a tutta larghezza. Titolo bianco enorme
in due misure — "Apriresti questa" a 71px, poi "email?" a **176,6px** (il singolo valore tipografico
più grande misurato su tutte e quattro le pagine), sottolineato da un tratto grigio disegnato a mano.
Sotto, una card grigio chiaro che imita una notifica Gmail ("Azienda itagliana — Caro lettore,
abbiamo una nuova offerta per te", con l'icona Gmail reale). Poi la risposta secca: "No, non
l'apriresti. Anzi, la metteresti in spam." Chiude un bottone blu pieno.

**Misure — sezione i=1:** y=0 / h=1.240px · sfondo `transparent` (eredita il fondo fotografico) ·
11 blocchi di testo, 34 parole, densità 3 · 3 media · 1 CTA ("Impara a scrivere email performanti",
`#0062ff`, radius 10px, → `#outemail-price`).

### outFunnel
![outFunnel hero](../capture/15-arma-outfunnel/sezioni/01-alcuni-fanno-questo-funnel.png)

**Cosa si vede:** rottura netta di registro rispetto a outEmail — sfondo grigio chiaro piatto, **zero
fotografia**. Tre righe di testo scuro intervallate da due diagrammi disegnati: un imbuto verde a 3
step ("Alcuni fanno questo funnel…"), poi un grafo a nodi grigi/viola con frecce tratteggiate ("…E
altri fanno questo…"), poi la chiusura "E poi c'è chi fa questo: **Quello che funziona.**" con un
alone acqua dietro la scritta. Nessun bottone in questa schermata.

**Misure — sezione i=1:** y=0 / h=1.240px · 5 blocchi, 14 parole, densità 1 · **6 media** (i due
diagrammi + le loro icone interne) · **0 CTA**. È l'unico hero della famiglia senza un solo elemento
cliccabile.

### outHeadline
![outHeadline hero](../capture/16-arma-outheadline/sezioni/01-questa-una.png)

**Cosa si vede:** sfondo nero che sfuma in rosso sangue verso il basso. "QUESTA È UNA" in bianco,
"HEADLINE." in rosso `#d50101` a 112,3px — stessa logica di outEmail (claim scioccante, parola chiave
nel colore d'accento), ma qui l'accento è rosso, non un colore diverso su ogni riga. Una freccia rossa
disegnata a mano punta verso il paragrafo sotto. Corsivo in chiusura: "*E guadagnano di più.*"

**Misure — sezione i=1:** y=0 / h=733px (**la più bassa hero della famiglia**) · 8 blocchi, 19
parole, densità 3 · 2 media (freccia + sfondo) · 0 CTA.

### outViral
![outViral hero](../capture/17-arma-outviral/sezioni/01-ottieni-una-media-di-10k-views-nei.png)

**Cosa si vede:** l'unico hero con un logo di prodotto visibile in testa ("**out**Viral", viola +
nero). Sfondo grigio chiaro. Titolo nero con "10K views" in viola acceso. A destra, un collage di
tre mockup (laptop, laptop+telefono, monitor con un frame video) che mostrano l'interfaccia reale del
corso — "30 video-lezioni", "Revisione dei tuoi video", "Interviste a creator con centinaia di
migliaia di follower". Chiude "Senza ca**ate." in nero, a freddare il tono da elenco-benefici appena
letto.

**Misure — sezione i=1:** y=0 / h=769px · 4 blocchi, 36 parole, densità 5 · 5 media · 0 CTA.

**Come cambia da una pagina all'altra:** due registri distinti, non quattro varianti dello stesso
schema. outEmail e outHeadline aprono **scure, con un claim/domanda a effetto** e nessuna prova
visiva del prodotto. outFunnel e outViral aprono **chiare, con una dimostrazione visiva** (diagramma
o mockup reale) al posto dell'hook emotivo. Solo outViral mostra il prodotto stesso (screenshot della
piattaforma) nell'hero; le altre tre lo tengono per dopo.

---

## RUOLO 2 — PROBLEMA / AGITAZIONE (il racconto a fumetti)

### outFunnel (rappresentante del device)
![outFunnel comic](../capture/15-arma-outfunnel/sezioni/04-section.png)

**Cosa si vede:** sette vignette in sequenza verticale, stile fumetto fotografico bianco e nero a
mezzatinta (foto reali filtrate, non disegni), con fumetti di dialogo disegnati a mano. Un personaggio
con gli occhiali spiega "Quindi ti serve un funnel strategico", l'altro protesta "Ma noi si è sempre
fatto così" mostrando una lavagna "ADS → landing page", poi la sequenza vira su un dialogo a due
riquadri ("Domanda: ti piacciono i soldi?" / "Certo che sì") fino alla rivelazione ("Ho ragione, ecco
perché ↓"). **Stesso identico dispositivo grafico** compare su outEmail, con vignette diverse
(`Comic-1-OE-Min.webp` … `Comic-5-OE-Min.webp`, separate da bordi "strappati"
`ripped-fumetto-min.webp`) — è un componente riusato, non un'illustrazione unica per pagina.

**Misure — sezione i=4:** y=2.898 / h=2.780px (la sezione singola più alta misurata in tutta la
famiglia) · **0 blocchi di testo** (tutto il testo persuasivo sta dentro i fumetti disegnati, non nel
DOM) · 10 media · 0 CTA.

**Come cambia da una pagina all'altra:** presente, con lo stesso stile fotografico b/n, su outEmail e
outFunnel. **Assente su outHeadline** (lì il problema si racconta per statistiche e affermazioni
dirette, non per fumetto) e **assente su outViral**, che sostituisce l'intero beat con la timeline
autobiografica del Ruolo 7. Perché il testo dentro le vignette non è nel DOM, questa sezione **pesa
zero sul conteggio "blocchi di copy"** della pagina pur occupando 2.780px — un punto cieco per
qualunque analisi che guardi solo ai blocchi di testo.

---

## RUOLO 3 — PROVA (dimostrazione concreta)

### outEmail
![outEmail prova](../capture/14-arma-outemail/sezioni/20-section.png)

**Cosa si vede:** un widget a carosello che imita una inbox reale — intestazione "Email marketing…
Come si deve" con contatore "1/7", frecce laterali, e una riga email con icona busta, mittente
("Candele Pro"), oggetto in grassetto ("Vogliamo darti fuoco, *nome*…"), anteprima ("Eh… Te lo
meriti… Diciamoci la verità…") e un badge azzurro "Open" in alto a destra. Sette pallini di
paginazione sotto. Il `copy-integrale.md` conferma altri 6 oggetti nello stesso widget (Affitti
Decenti Milano, Piantina Finta S.R.L., Corsi di Cucina Online, Palestra FitLife, EcoVerde Delivery,
Agenzia Viaggi DreamTrip) — tutti scritti nel tono provocatorio che il corso insegna.

**Misure — sezione i=20:** y=21.499 / h=771px · **19 blocchi, densità 18** (fra le più alte della
pagina) · 0 media (è tutto markup/CSS, nessuna immagine) · **9 CTA** — 1 reale + 8 badge "Open"
decorativi senza `href`.

### outHeadline
![outHeadline prova](../capture/16-arma-outheadline/sezioni/05-vedi-la-differenza-tu-stesso.png)

**Cosa si vede:** un tool interattivo "prima/dopo" — un annuncio finto di un fast food ("PRIMA —
Vieni a provare i nostri burger!" su foto reale di hamburger) con un bottone verde "Clicca qui" che,
per `mirror.js`, sostituisce l'immagine con la versione "riscritta". Sotto: "Andare da una versione
all'altra di questa headline non è facile… Ci sono specifiche metodologie per farlo."

**Misure — sezione i=5:** y=5.183 / h=1.053px · 6 blocchi, 32 parole, densità 3 · 2 media · 1 CTA
("Clicca qui", verde `#7ab641`, nessun `href` — l'azione è gestita da JS, non da un link).

### outViral
![outViral prova](../capture/17-arma-outviral/sezioni/07-ti-beccherai-il-valore-di-creator.png)

**Cosa si vede:** l'unica prova della famiglia costruita su **persone reali verificabili**, non su
mockup o statistiche. Griglia 3×2 di creator con foto profilo reale, nome, bio breve, contatore
follower (128k, 150k, 100k, 100k, 181k, 104k — somma **863k**, coerente col claim in titolo "quasi 1
milione") e un bottone "Vai al profilo" per ciascuno, che punta a URL reali (YouTube, TikTok,
Instagram — verificati in `scheda.json → cta[]`).

**Misure — sezione i=7:** y=5.323 / h=1.718px · 20 blocchi, 215 parole, densità 13 · **14 media** (6
foto profilo + 6 icone piattaforma + sfondo) · **6 CTA**, tutti reali (link esterni funzionanti).

**Come cambia da una pagina all'altra:** tre dispositivi di prova completamente diversi per lo stesso
ruolo — inbox finta (outEmail), tool interattivo (outHeadline), persone reali con link verificabili
(outViral). outFunnel usa il fumetto del Ruolo 2 anche come sua prova principale (le statistiche con
fonte, in forma di semplice testo, coprono il resto). Nessuna delle quattro riusa lo stesso
dispositivo di prova di un'altra — a differenza del Ruolo 4 (curriculum), dove tre pagine su quattro
condividono lo stesso identico componente.

---

## RUOLO 4 — CONTENUTO (il curriculum)

### outEmail
![outEmail curriculum](../capture/14-arma-outemail/sezioni/18-lista-video-lezioni.png)

**Cosa si vede:** su fondo nero, titolo "Lista video-lezioni", poi un mini-carosello di 3 card scure
(mockup della piattaforma corsi, accento teal: "Lezione 9 — Opzioni per il lead magnet", "Lezione 10
— Tipi di sequenze automatiche + follow up", "Lezione 11 — Opzioni per upsell/cross-sell base"). Sotto,
un accordion a righe sottili con 3 sezioni ("Sezione 1 - Introduzione", "Sezione 2 - Scrittura",
"Sezione 3 - Strategia"), ciascuna con un'icona busta rosa e un "+" per espandere.

**Misure — sezione i=18:** y=19.912 / h=774px · 55 blocchi, 17 parole, densità 2 · 4 media · 3 CTA
(le tre etichette di sezione, senza `href` — l'apertura è gestita da `mirror.js`).

### outFunnel
![outFunnel curriculum](../capture/15-arma-outfunnel/sezioni/21-div.png)

**Cosa si vede:** **componente pixel-identico** a quello di outEmail — stesso layout, stesso accento
teal, e — verificato aprendo entrambi gli screenshot — **le stesse identiche tre card di anteprima**
("Lezione 9 — Opzioni per il lead magnet" ecc.), argomenti di email marketing non di funnel. È il
difetto di riciclo già segnalato nel report di confronto (§6.1): solo l'accordion sotto cambia
davvero contenuto ("Sezione 1 – Le basi", "Sezione 2 – Esempi strategici", "Sezione 3 – Strategie
avanzate", "Sezione 4 – Esempi di Funnel completi").

**Misure — sezione i=21** (`div\|section-border`, la stessa firma dei divisori decorativi di sfondo
della pagina — la sezione porta contenuto reale nonostante la firma "decorativa", una discrepanza
strutturale annotata qui e non altrove): y=24.054 / h=771px · 1 media dichiarato nel record di
sezione (il resto del contenuto visibile — le card e l'accordion — non risulta contato come blocchi
di testo di quella sezione, verificato guardando lo screenshot: il numero non torna col visivo, va
letto come limite della misurazione automatica più che come sezione vuota).

### outHeadline
![outHeadline curriculum](../capture/16-arma-outheadline/sezioni/09-outheadline-lista-lezioni.png)

**Cosa si vede:** stesso componente, accento verde. Qui però il blocco si ripete **due volte di
fila** nella stessa sezione — prima "Sezioni A & B: introduzione al copy" con le sue 3 card e 2 righe
accordion, poi sotto "Sezioni 1,2,3,4 & 5: come scrivere headline" con altre 3 card e 5 righe
accordion. È la sezione più densa di contenuto misurato di tutta la famiglia.

**Misure — sezione i=9:** y=9.101 / h=1.718px · **94 blocchi di testo** (il valore più alto fra tutte
le sezioni rappresentanti delle quattro pagine), 97 parole, densità 6 · 2 media · **7 CTA** (tutte le
etichette di sezione sommate delle due liste).

### outViral
![outViral curriculum](../capture/17-arma-outviral/sezioni/06-le-video-lezioni.png)

**Cosa si vede:** **rompe lo schema**. Fondo chiaro invece che scuro, layout a due colonne invece del
carosello: a sinistra un accordion "14 video-lezioni su come creare video" (4 righe: basi, approccio,
luce/audio, come funziona TikTok), con accanto — non sopra — un mockup laptop dell'interfaccia reale
del corso ("Benvenuto in outViral"). Sotto, "7 nuove video-lezioni" con l'elenco delle lezioni 15-21
scritto per esteso (non in accordion) e un secondo mockup laptop con l'anteprima di una lezione reale
("STRUTTURA BASE DEI VIDEO").

**Misure — sezione i=6:** y=3.849 / h=1.474px · 73 blocchi, 124 parole, densità 8 · 2 media · 5 CTA.

**Come cambia da una pagina all'altra:** il ruolo "curriculum" è quello con **la maggiore riduzione
d'attrito produttivo** della famiglia — outEmail, outFunnel e outHeadline condividono lo stesso
identico componente scuro (carosello + accordion), cambiando solo l'accento colore e il testo delle
righe. outViral rompe lo schema con un layout chiaro a due colonne e mockup reali al posto delle card
generiche — probabilmente perché, a differenza delle altre tre, ha già mostrato l'interfaccia del
corso nell'hero (Ruolo 1) e qui la riusa invece di introdurne una versione astratta.

---

## RUOLO 5 — QUALIFICAZIONE NEGATIVA ("non è per te se…")

### outEmail
![outEmail qualificazione](../capture/14-arma-outemail/sezioni/11-non-per-tutti-sono-serio.png)

**Cosa si vede:** su nero pieno, "Non è per tutti. Sono serio." Sotto, tre righe con **X rossa**
("Non spiega cos'è una mail di marketing", "Non spiega cosa significa 'copywriting'", "Salta le basi
che, tanto, già sai"), poi un avviso con triangolo giallo ⚠️ ("Quindi non prendere outEmail se sei un
principiante") e la chiusura in grassetto bianco.

**Misure — sezione i=11:** y=13.174 / h=743px · 5 blocchi, 49 parole, densità 7 · 4 media (le 4 icone
X/⚠️) · 0 CTA.

### outHeadline
![outHeadline qualificazione](../capture/16-arma-outheadline/sezioni/10-outheadline-non-per-principianti.png)

**Cosa si vede:** stessa logica, resa completamente diversa — sfondo che sfuma da nero a verde acceso
verso il basso, frecce verdi `❯` al posto delle X rosse, e — a differenza di outEmail — una **seconda
lista positiva** subito sotto ("Questo corso è pensato per: Copywriter che vogliono scrivere al
prossimo livello di persuasione").

**Misure — sezione i=10:** y=10.818 / h=686px · 1 blocco di testo dichiarato (il resto del contenuto
visibile in schermata — le liste — non risulta interamente nel conteggio, stesso limite di
misurazione annotato nel Ruolo 4) · 3 media · 0 CTA.

**Come cambia da una pagina all'altra:** stessa struttura retorica (lista di chi-non-deve-comprare,
icona negativa ripetuta), esecuzione grafica opposta (nero+rosso rigido su outEmail, gradiente
nero→verde su outHeadline). **Assente su outFunnel e outViral** — nessuna delle due qualifica
negativamente il lettore da nessuna parte nel testo catturato.

---

## RUOLO 6 — OBIEZIONI (botta e risposta)

### outEmail
![outEmail obiezione](../capture/14-arma-outemail/sezioni/14-ma-io-so-gi-scrivere-email.png)

**Cosa si vede:** fondo chiaro (l'unica sezione-obiezione su fondo chiaro invece che scuro), titolo
tra virgolette "'Ma io so già scrivere email'", risposta immediata "Bene, allora sei in target.",
poi "Cosa aspettarti:" con tre righe a icona blu tonda (tutorial, strategie avanzate, riassunti).

**Misure — sezione i=14:** y=15.691 / h=658px · 3 blocchi, 29 parole, densità 4 · 1 media · 0 CTA.

### outHeadline
![outHeadline obiezione](../capture/16-arma-outheadline/sezioni/17-ma-io-le-faccio-scrivere-a-chatgp.png)

**Cosa si vede:** titolo tra virgolette "'Ma io le faccio scrivere a ChatGPT'" sotto il logo OpenAI,
poi uno **screenshot reale del browser di Andrei** — cartelle personali visibili ("Lavoro", "Pirate",
"OTTO docs", "Ai"), un segnalibro "Andrei Pascu Copywriting" e un documento aperto "Copy SP oH" — con
una freccia verde disegnata che indica un'icona. Chiude "Ma se non conosci le strategie, non puoi
usare l'AI responsabilmente."

**Misure — sezione i=17:** y=17.930 / h=1.004px · 6 blocchi, 94 parole, densità 9 · 3 media · 0 CTA.

**Come cambia da una pagina all'altra:** stesso schema domanda-tra-virgolette + risposta diretta, ma
l'obiezione è **specifica al prodotto** in ciascun caso (competenza pregressa su outEmail, uso di
ChatGPT su outHeadline) e non riciclata. **Assente su outFunnel e outViral.**

---

## RUOLO 7 — AUTOREVOLEZZA / DIFFERENZIAZIONE

### outEmail
![outEmail autorevolezza](../capture/14-arma-outemail/sezioni/16-andrei-perch-dovrei-comprare-oute.png)

**Cosa si vede:** su nero, il titolo diretto "'Andrei perché dovrei comprare outEmail e non i tuoi
competitor?'" seguito da tre paragrafi in prima persona ("Perché 99% dei miei competitor non sono
copywriter… Anche perché questa pagina l'ho scritta io, Andrei… Sì, il copy è il mio lavoro"), poi
"Impara dal numero 1 copywriting icon…" sopra un'immagine generata: un ritratto in cornice dorata di
Andrei vestito da re, in una sala con affreschi.

**Misure — sezione i=16:** y=17.539 / h=1.348px · 6 blocchi, 133 parole, densità 10 (fra le più alte
misurate) · 1 media (il ritratto) · 0 CTA.

### outViral (variante: timeline autobiografica)
![outViral autorevolezza](../capture/17-arma-outviral/sezioni/08-cosa-ca-o-sto-sbagliando-cit-andr.png)

**Cosa si vede:** non un argomento diretto ma tre "confessioni" datate, alternando foto reali in
bianco e nero di Andrei a sinistra e a destra: *"'Cosa ca**o sto sbagliando?' - cit. Andrei Pascu,
2020"*, *"'Ma… L'ho fatto prima io…' - Cit. Andrei 2020"*, *"'Se solo capissi l'algoritmo…' - Cit.
Andrei 2020"* — ciascuna con un paragrafo di racconto in prima persona sulla frustrazione iniziale.
L'anno è sempre in rosso acceso.

**Misure — sezione i=8:** y=7.041 / h=1.243px · 10 blocchi, 154 parole, densità 12 · 4 media · 0 CTA.

**Come cambia da una pagina all'altra:** outEmail e outHeadline argomentano l'autorevolezza in modo
diretto (perché comprare da me, con affermazioni esplicite). outViral la costruisce per
**narrazione temporale** — lo stesso obiettivo (fiducia nel formatore), un dispositivo retorico
diverso. **Assente come sezione a sé su outFunnel.**

---

## RUOLO 8 — PREZZO (il valore-stack)

### outEmail
![outEmail prezzo](../capture/14-arma-outemail/sezioni/22-adesso-disponibile.png)

**Cosa si vede:** logo prodotto, "adesso disponibile.", poi una card bianca con bordo che pulsa di
un bagliore ciano (l'unica animazione CSS attiva su tutta la famiglia — `pulseShadow 3s ease`):
elenco di 4 benefici con spunta nera, 1 con una X grigia ("Niente strategie basilari che conosci
già"), e il prezzo **€139 barrato in rosso**. Sotto la card, in rosso: "INCLUSO NEL PACCHETTO
ARMAGEDDON".

**Misure — sezione i=22:** y=23.099 / h=1.022px · 3 blocchi, 6 parole, densità 1 · 1 media · 0 CTA
(il prezzo è dentro l'immagine, non un elemento cliccabile a sé).

### outFunnel
![outFunnel prezzo](../capture/15-arma-outfunnel/sezioni/22-outfunnel-probabilmente-non-per-te.png)

**Cosa si vede:** card minimale — solo il logo prodotto (teal) e sotto **€98 barrato in verde**,
"/pagamento unico", "INCLUSO NEL PACCHETTO ARMAGEDDON". Nessun elenco benefici, nessun bagliore.
Condivide la sezione con il titolo di chiusura "outFunnel? Probabilmente non è per te. Ma se lo è…
Stai per svoltare."

**Misure — sezione i=22:** y=24.825 / h=757px · 3 blocchi, 17 parole, densità 2 · 3 media · 0 CTA.

### outHeadline
![outHeadline prezzo](../capture/16-arma-outheadline/sezioni/18-outheadline-probabilmente-non-per.png)

**Cosa si vede:** stessa identica card minimale di outFunnel, accento verde, **€98 barrato**. Stesso
titolo-chiusura, stesso badge rosso sotto.

**Misure — sezione i=18:** y=18.934 / h=872px · 4 blocchi, 17 parole, densità 2 · 3 media · 0 CTA.

### outViral
![outViral prezzo](../capture/17-arma-outviral/sezioni/02-div.png)

**Cosa si vede:** l'unica card prezzo leggibile come **testo semplice**, non immagine — "outViral 2 /
**250,00 €** (barrato) / Una tantum", il badge rosso, e in più i loghi di pagamento (PayPal, Visa,
Mastercard, Amex, Apple Pay). Compare **due volte** sulla pagina: qui, appena sotto l'hero (§1), e di
nuovo verso la fine con l'aggiunta "Paghi una volta, sei dentro per sempre. Pagamento sicuro con
PayPal o qualsiasi carta."

**Misure — sezione i=2** (`div\|section-border`): y=786 / h=717px · 1 media dichiarato · 0 CTA (i
loghi di pagamento sono immagini decorative, non link).

**Come cambia da una pagina all'altra:** stesso schema su tutte e quattro — prezzo individuale
barrato + badge rosso "incluso nel pacchetto" — ma **solo outEmail ha l'elenco benefici e
l'animazione**; le altre tre sono versioni "essenziali" dello stesso componente. **Solo outViral**
rende il prezzo in testo semplice invece che come immagine, ed è l'unica a ripetere il blocco due
volte e ad aggiungere i loghi di pagamento e la rassicurazione "una tantum, per sempre".

---

## RUOLO 9 — FAQ

![outEmail FAQ](../capture/14-arma-outemail/sezioni/23-faq.png)

**Cosa si vede:** su nero, titolo "FAQ", una card con bordo sottile arrotondato contenente 4 righe
accordion con chevron ("Si parla anche di deliverability e compliance?", "Posso prenderlo se sono
principiante?", "Sei sicuro che mi aiuterà?", "Da dove sono prese le strategie nel corso?"). Sotto la
card, la chiusura diretta ("Ti ho praticamente detto tutto… Ribalti 'ste email o no?") e il bottone
blu finale "Ok, ok, facciamolo".

**Misure — sezione i=23 (outEmail):** y=24.121 / h=1.104px · 23 blocchi, 50 parole, densità 5 · 1
media · 5 CTA (4 accordion + 1 bottone reale).

outFunnel ripete lo stesso componente (`../capture/15-arma-outfunnel/sezioni/23-faq.png`, non
riprodotto qui) con solo 3 domande invece di 4 ("Come posso accedere al corso?", "Quanto dura il
corso?", "Devo avere esperienza per capirlo?") e su fondo chiaro invece che nero — sezione i=23:
y=25.582 / h=617px, 16 blocchi, 15 parole, densità 2, 1 media, 3 CTA.

**Come cambia da una pagina all'altra:** stesso componente accordion, stesso numero di domande-tipo
(compliance/principianti/efficacia/fonti), tema colore invertito fra le due pagine che la includono.
**Assente su outHeadline e outViral** — nessuna delle due offre una sezione domande-risposte
esplicita.

---

## RUOLO 10 — CHIUSURA (footer legale + barra sticky)

![outEmail chiusura](../capture/14-arma-outemail/sezioni/24-div.png)

**Cosa si vede:** testo grigio chiaro su nero, giustificato al centro — il disclaimer standard
("Questo sito e i consigli contenuti al suo interno sono opinioni personali a scopo educativo…") e la
riga di partita IVA ("Andrei Pascu Sales · P.I. 02001850474 · Viale Giacomo Matteotti 15, 50121
Firenze (FI)"), con link "Privacy, dati, cookie e simili" verso `andrei-copy.com`.

**Misure — firma `div|ag-legal` su tutte e quattro:** outEmail y=25.225 h=259px · outFunnel y=26.199
h=258px · outHeadline y=19.806 h=258px · outViral y=9.685 h=258px — **stessa identica altezza (±1px)
su tutte e quattro le pagine**, stesso numero di blocchi (3), stesse parole (90), stessa densità (35
— la più alta di ogni pagina, essendo tanto testo in poco spazio).

**Come cambia da una pagina all'altra:** **non cambia.** Verificato testo per testo nei quattro
`copy-integrale.md`: la stringa del disclaimer e quella della P.IVA sono identiche carattere per
carattere sulle quattro pagine — e uguali anche al footer della pagina madre `armageddon.bsns.it/`
(dossier 11, pattern `coda-legale` già in canone). È l'unico blocco della famiglia che non varia mai,
nemmeno nel colore o nella spaziatura.

Trasversale a tutte e quattro, sempre presente ma non fotografabile come sezione a sé (è
`position: fixed`): la **barra sticky** in fondo allo schermo — "Prendi l'Armageddon Pack — 199€"
(rosso `#bc0807`, radius 0px) e "Torna alla pagina principale" (contorno bianco, → `/`) — iniettata
dal mirror (`.ag-sticky` in `mirror.css`), non parte dell'originale Squarespace.

---

## Collegamenti

- [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) — la tabella numerica, lo
  schema ricorrente completo, i difetti e il delta alla Fabbrica
- [11-armageddon.md](11-armageddon.md) — la pagina madre, il pattern `coda-legale` da cui il Ruolo 10
  eredita testo identico
- `.claude/skills/fabbrica-siti/pattern/faq-native/scheda.md` — la versione nativa (`<details>`) del
  Ruolo 9, più leggera di quella vista qui
