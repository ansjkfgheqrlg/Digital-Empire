---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #store #pricing #affiliazione #ecommerce #teardown
Created: 2026-09-09
Last updated: 2026-09-09
---

# 53-57 — Il negozio: listino, presentazione, pagine di affiliazione

**Pagine studiate:** `55-negozio` (2.601px, 67 blocchi, 2 sezioni) · `56-store` (5.506px, 70 blocchi, **19
CTA**, segmentazione fallita) · `57-store-aps` (1.524px, 32 blocchi, categoria filtrata) · `53-risorse`
(4.039px, 56 blocchi, 4 sezioni, **8 CTA**) · `54-attrezzatura` (9.395px, 27 blocchi, 2 sezioni,
segmentazione riuscita ma **0 CTA nel corpo pagina**). Fonti: `copy-integrale.md` e `scheda.json` di
ognuna delle cinque cartelle in `site-study/capture/`, più cinque screenshot aperti direttamente
(`55-negozio/desktop-01.png`, `.../desktop-02.png`, `56-store/desktop-01.png`, `.../desktop-06.png`,
`54-attrezzatura/desktop-01.png`, `.../desktop-03.png`) per vedere come sono presentati davvero i
prodotti e cosa il DOM da solo non poteva mostrare.

---

## DELTA ALLA FABBRICA

**CANONE:** il sito applica una **regola di divulgazione del prezzo a due velocità**, verificata
confrontando `55-negozio` con `56-store`. Sui 3 corsi-corpo (outHeadline, Copywriting Mentorship,
outViral 2, Vendita101, Mindset: Programma Operativo — 5 prodotti su 8 card di `55-negozio`) **nessun
prezzo compare come testo**, verificato con ricerca diretta nel `copy-integrale.md`: zero occorrenze del
simbolo `€` in tutto il file. Il bottone è sempre *"Info / iscrizioni"* [es. y=586, y=1144, y=1731], mai
un prezzo, mai un bottone di acquisto diretto. Sui prodotti-store minori (Manuale del copywriter,
Workbook, Maglietta) il bottone diventa *"Info / acquisto"* [y=614, y=1173] e il prezzo compare
esplicito una volta raggiunta `56-store` (79,00€, 19,00€, da 24,90€). **Per la Fabbrica: il prezzo si
mostra subito solo sugli articoli a basso rischio di rifiuto (libro, gadget); sui prodotti ad alto
ticket si nasconde dietro un click supplementare**, una tattica di qualificazione del traffico prima
di esporre la cifra — corretta da replicare quando il differenziale di prezzo fra articoli di un
catalogo è ampio (qui, dai 19€ del Workbook ai 649€ dell'Upgrade Copywriting Mentorship, un rapporto
di oltre 34 volte).

**PATTERN:** il sito usa **due linguaggi fotografici distinti per due categorie di prodotto**,
verificato su `56-store`. I corsi digitali (Manuale del copywriter, copy.exe) sono fotografati come
**mockup "smartphone in mano"** — una mano regge un telefono che mostra la cover del prodotto, sempre
la stessa inquadratura (verificato su `media[]`: `w=533, h=533`, quadrato, per tutte le card
Manuale/copy.exe). Gli eventi live (Leads Virali LIVE, varianti Starter/Core/Bourgeoisie) sono invece
fotografati come **veri e propri "biglietti" grafici**: card nere con nome dell'evento, data e ora
stampate sopra ("10 ottobre 18:00" visibile su `desktop-01.png` di `56-store`), taglio diagonale in
stile ticket da concerto. Per la Fabbrica: **il formato del mockup deve comunicare la natura del
prodotto prima ancora del titolo** — smartphone per contenuto digitale fruibile subito, biglietto per
evento con data fissa — un segnale visivo che riduce l'ambiguità "è un corso o un evento?" prima che il
lettore legga una parola.

**GATE:** tre controlli nuovi, ciascuno misurato su un difetto reale trovato in questo documento. 1)
*L'etichetta del bottone deve sempre corrispondere alla foto del prodotto sopra di essa* — su
`55-negozio`, la card con foto di una felpa nera "REJECT SOCIALISM / EMBRACE CAPITALISM" [y=1600] ha un
bottone che recita *"Coppa"* [y=1703], non "Maglietta" né "Acquista": l'`href` porta comunque a
`/store/p/mens-classic-tee` [verificato in `scheda.json/cta[]`], quindi il prodotto reale è la maglietta,
ma l'etichetta del bottone dice "tazza". 2) *Ogni variante di prezzo gemella (rata vs unica soluzione,
upgrade con/senza sconto) deve avere il proprio `href` catturabile* — su `56-store`, sia *"Upgrade:
Copywriting Mentorship Program (rateizzato)"* [y=2161] sia *"Insider [se hai già il manuale]"* [y=2767]
non hanno un `href` proprio nell'array `cta[]` catturato (solo le rispettive card gemelle, "a saldo" e
"Upgrade: insider", lo hanno) — un buco di cattura da non scambiare per un buco del sito. 3) *Un widget
ad accordion che elenca articoli (gear list, catalogo software) deve essere aperto stato-per-stato prima
di concludere che non contenga link esterni* — su `54-attrezzatura`, `cta[]` è vuoto nel corpo pagina
(0 link), ma la schermata mostra chiaramente un accordion con freccia `▼` per ogni riga (Sony A7 III,
DJI Mic 2, ecc.): il link di affiliazione, se esiste, è quasi certamente dietro il click che espande la
riga, non nel DOM collassato.

---

## IL LISTINO COMPLETO

Tabella ordinata per prezzo crescente, ogni cifra verificata testualmente in `copy-integrale.md` di
`56-store` (unica delle cinque pagine dove i prezzi compaiono come testo semplice, non immagine).
Prodotti gemelli con due varianti di pagamento sono raggruppati sulla stessa riga.

| Prezzo | Prodotto | Pagina/coordinata | `href` |
|---|---|---|---|
| 19,00 € | Workbook | `56-store` [y=4082] | `/store/p/workbook` |
| da 24,90 € | Maglietta "EMBRACE CAPITALISM" | `56-store` [y=4750] | `/store/p/mens-classic-tee` |
| 79,00 € | Manuale del copywriter + prompt AI | `56-store` [y=821] / `57-store-aps` [y=772] | `/store/p/manuale-del-copywriter-x8dnn` |
| 79,00 € | Manuale del copywriter (senza prompt AI) | `56-store` [y=4721] / `57-store-aps` (seconda card) | `/store/p/manuale-del-copywriter` |
| 99,00 € | copy.exe - origin | `56-store` [y=4082] | `/store/p/copyexe-origin` |
| 99,00 € | Upgrade: insider | `56-store` [y=2804] | `/store/p/upgrade-insider` |
| 129,00 € *(scontato da 199,00 €)* | Insider [se hai già il manuale] | `56-store` [y=2804] | non catturato — vedi GATE punto 2 |
| 149,00 € | Starter - Leads Virali LIVE - per Networker | `56-store` [y=1493] | `/store/p/save-them-basico` |
| 199,00 € | Core - Leads Virali LIVE - per Networker | `56-store` [y=1493] | `/store/p/save-them-main` |
| 199,00 € | copy.exe - insider | `56-store` [y=3443] | `/store/p/copy-exe-insider` |
| 216,33 €/mese × 3 *(≈648,99 € totali)* | Upgrade: Copywriting Mentorship Program (rateizzato) | `56-store` [y=2161] | non catturato — vedi GATE punto 2 |
| 499,00 € | Bourgeoisie - Leads Virali LIVE - per Networker | `56-store` [y=850] | `/store/p/save-them-luxury` |
| 500,00 € | copy.exe - black | `56-store` [y=3443] | `/store/p/copyexe-black` |
| 649,00 € | Upgrade: Copywriting Mentorship Program (unica soluzione) | `56-store` [y=2132] | `/store/p/upgrade-copywriting-mentorship-program` |

**14 SKU con prezzo verificabile come testo semplice**, tutti su `56-store` (7 confermati anche
identici su `57-store-aps` per i 2 manuali). Due osservazioni sul listino stesso:

1. **Il rateizzato costa quasi esattamente come il pagamento unico, non di più.** 216,33 € × 3 = 648,99
   €, un centesimo in meno dei 649,00 € richiesti in un'unica soluzione [y=2132]. Non c'è il tipico
   markup "paghi di più se rateizzi" che si vede spesso in questo mercato — un dato da annotare come
   riferimento se decidiamo di introdurre piani rateali nei nostri prodotti.
2. **Il manuale "con prompt AI" costa esattamente come il manuale senza.** 79,00 € in entrambi i casi
   [y=821 e y=4721] — l'aggiunta dei prompt AI è quindi usata come **differenziatore di posizionamento
   a costo marginale zero**, non come upsell a pagamento: chi arriva dalla pagina che menziona l'AI
   compra allo stesso prezzo di chi compra il manuale "puro". Utile a sapersi se pensiamo di bundlare
   prompt/asset AI nei nostri prodotti da vendere.

**Cinque prodotti su 8 di `55-negozio` non hanno alcun prezzo in nessuna delle cinque pagine di questo
documento**, confermato con ricerca diretta: **outHeadline** (→ `/outheadline`), **Copywriting
Mentorship** nella sua versione base (→ `/cm-preordine` — lo slug stesso, "preordine", suggerisce che
l'edizione corrente sia ancora in fase di prevendita, distinta dall'"Upgrade" da 649€ visto sopra, che è
un percorso per chi ha già una versione precedente), **outViral 2** (→ `/outviral`), **Vendita101** (→
`/vendita`), **Mindset: Programma Operativo** (→ `/mpo2`). Il prezzo di questi cinque prodotti — che
sono, con ogni evidenza, i prodotti-corso principali del catalogo, non gli articoli accessori — vive
fuori dal perimetro di queste cinque pagine, dietro il click su "Info / iscrizioni".

---

## COME SONO PRESENTATI I PRODOTTI

**`55-negozio` è una vetrina-catalogo, non un negozio funzionante.** Otto card in griglia (verificato
su `desktop-01.png` e `desktop-02.png`): ognuna ha un'immagine di copertina (mockup telefono per i
corsi, foto prodotto per gli articoli fisici), un titolo `<h2>` [y=437/995/1554, ripetuto per riga di
griglia], una riga di copy breve in tono da provocazione ("Puoi scrivere quanti copy vuoi e contattare
trecento clienti al giorno, senza una guida resterai a zero" [y=510], "La maggior parte dei libri ci
mette 1 capitolo intero per darti 1 consiglio. Hai tutto sto tempo?" [y=510]), e un bottone nero
uniforme (`bg: #1b1b1d`, `radius: 10px`, verificato su tutti gli 8 CTA prodotto in `scheda.json`) con
testo *"Info / iscrizioni"* o *"Info / acquisto"* a seconda che il prodotto sia un corso o un articolo
fisico/digitale a basso prezzo. Nessun prezzo, nessuna descrizione lunga, nessuna prova sociale sulla
pagina stessa — è un indice, non una vetrina di vendita.

**`56-store` è il negozio Squarespace reale**, con prezzi, foto quadrate ad alta risoluzione (533×533px,
verificato su tutte le card prodotto in `media[]`) e una barra di categoria in testa: *"Leads Virali
LIVE - per Networker | copy.exe | APS Store"* [y=181] — tre collezioni filtrabili. La sezione degli
eventi live (Bourgeoisie/Core/Starter) usa il linguaggio "biglietto" descritto sopra; la sezione
copy.exe usa tre varianti di uno stesso prodotto software (black/insider/origin, prezzi 500/199/99€) con
foto identiche in stile "biglietto nero" anch'esse — segno che "copy.exe" non è un corso ma probabilmente
un tool/software con livelli di accesso a scaglioni di prezzo, coerente con l'altezza pagina del negozio
(5.506px) e il fatto che questo studio non aveva ancora una pagina dedicata a copy.exe fra quelle
catturate finora nell'ecosistema.

**`57-store-aps` è una categoria filtrata dello stesso store**, non una pagina indipendente: il
`canonical` nel suo `<head>` punta a `https://www.andrei-copy.com/store` [verificato in
`scheda.json/meta`], e mostra solo le due varianti del Manuale del copywriter (con e senza prompt AI,
entrambe 79,00€) [y=735-772]. La sua sezione tecnica include anche le intestazioni fantasma *"Filtri"*
e *"Nessun risultato trovato"* [in `sezioni[0].headings`], segno che è la stessa interfaccia a filtro di
`56-store` con il filtro "APS Store" già applicato, capace di mostrare zero risultati se il filtro non
incrocia nessun prodotto — un dettaglio tecnico, non un contenuto autonomo.

**Il difetto di etichetta già citato nel GATE** merita di essere ripreso qui come esempio di
presentazione, non solo di markup: sulla card "Reject socialism." [y=1554-1703 in `copy-integrale.md`
di `55-negozio`], la foto è una felpa nera con la scritta *"REJECT SOCIALISM EMBRACE CAPITALISM"* e un
piccolo logo triangolare, il titolo della card è *"Reject socialism."*, la descrizione recita *"'Reject
socialism, embrace capitalism.' E sopra il logo AP Formazione."* [y=1600] — ma il bottone dice
*"Coppa"* [y=1703]. Aperta la scheda tecnica, l'`href` di quel bottone porta a
`/store/p/mens-classic-tee` [confermato in `scheda.json/cta[]`], cioè alla stessa maglietta, non a una
tazza. È un'etichetta rimasta indietro rispetto al prodotto reale — probabilmente il catalogo offriva in
origine sia una tazza sia una maglietta con la stessa grafica, e il bottone "Coppa" non è stato
aggiornato quando la tazza è stata tolta o sostituita dal capo di abbigliamento.

---

## 53-RISORSE: CONTENUTO GRATUITO, NON UN FLUSSO DI AFFILIAZIONE

Cercando nel campo `cta[]` di `53-risorse/scheda.json`, gli unici link esterni sono **quattro bottoni
rossi identici "Guarda su YouTube"** [y=1375, y=1712, y=2024, y=2329], tutti diretti a
`youtu.be/<id>` (`nvl28y1T6xI`, `f9ddn7AZdZI`, `j4UInmM9kKA`, `URS89smw38w`) — **il canale YouTube
personale di Andrei Pascu**, non un servizio terzo, non un link di affiliazione. La pagina si presenta
come *"Una raccolta di contenuti gratuiti di AP Formazione"* [y=279], con una sezione *"YouTube
videos"* [y=873] che promuove *"una top 4 dei video più utili che abbia mai creato"* [y=979]: titoli
osservati, *"Nel 2026 il marketing avrà questi 9 cambiamenti"* [y=1202], *"Come i RICCHI gestiscono il
loro TEMPO"* [y=1514], *"Usa questi 10 lead magnet per generare contatti (gratis)"* [y=1851], *"Come
vendere in call e chiudere TUTTI"* [y=2163]. **Risposta diretta alla domanda della consegna: `/risorse`
non è una pagina di affiliazione — è content marketing verso il proprio canale, senza alcun link
esterno monetizzato individuato.** L'unico altro elemento della pagina è un teaser *"Presto disponibile"*
per un *"Corso di business"* gratuito di 40 minuti [y=2694-2794] — un lead magnet futuro, non ancora
attivo, senza bottone d'iscrizione catturato.

## 54-ATTREZZATURA: PROBABILE FLUSSO DI AFFILIAZIONE, MAI CENSITO DAL NOSTRO SCAN

Qui la risposta è più delicata e va data con lo stesso rigore metodologico usato nel documento gemello
di questo studio (dossier `50-52-58`, dove un widget Trustpilot era stato scambiato per un'immagine
piatta). **Il campo `cta[]` di `54-attrezzatura/scheda.json` non contiene nessun link esterno** — solo
navigazione e footer, verificato per intero. Ma aprendo `desktop-01.png` la pagina si rivela essere
tutt'altro che vuota di contenuto: *"Attrezzatura e Software di AP Sales"*, sottotitolo *"AGGIORNATO A
LUGLIO 2026"*, tre filtri — *"Tutto 75"*, *"Attrezzatura 31"*, *"Software 44"* — e un link *"APRI
TUTTO"*. Sotto, un accordion categorizzato: **"Camere e Ottiche" (6 articoli)** con Sony A7 III
("Mirrorless full frame — camera principale"), Sony A7C, Sony Zeiss Sonnar T* FE 55mm f/1.8 ZA,
Grandangolo APS-C, Tamron 28-75mm f/2.8; **"Supporti e Stabilizzazione" (6)** con DJI Osmo Mobile, DJI
Ronin RS 2 (Pro Combo), Manfrotto Befree 3-Way Live, Treppiedi assortiti, iFootage Cobra 2 Round Base,
Attacchi e accessori SmallRig; **"Monitor e Registrazione" (2)** con Monitor da campo AndyCine;
**"Audio" (4)** con DJI Mic 2, DJI Mic (prima generazione), DJI Mic Mini, Microfono lavalier DJI; e
almeno **"Luci" (3)** con Luci LED COB amaran, amaran Ace 25x — per un totale dichiarato di **75
articoli** (31 attrezzatura + 44 software) su tutta la pagina, di cui questo studio ne ha aperti e
verificati visivamente circa 21 nei due screenshot controllati.

Ogni riga ha una freccia `▼` sul lato destro — il segno distintivo di un accordion che si espande al
click. **Il nostro strumento di cattura ha letto il widget abbastanza da renderizzarlo in uno
screenshot, ma non è riuscito a estrarne il testo come blocchi DOM** (stesso identico limite già
documentato nel dossier gemello per il widget Trustpilot di `50-recensioni` e per il bottone flottante
Elfsight di `51-recensioni-mentorship`): `blocchi_testo` per questa pagina è 27, tutti nav+footer, e
`headings[]` in `scheda.json` è vuoto nonostante lo screenshot mostri un `<h1>` "Attrezzatura e Software
di AP Sales" ben visibile. Questo significa che **se esistono link di affiliazione (Amazon, DJI,
Sony, Manfrotto, ecc.), sono quasi certamente nascosti dentro lo stato espanso di ogni riga
dell'accordion — uno stato che il nostro scan, fermo al DOM collassato, non ha mai raggiunto e non
può quindi né confermare né escludere.**

**Verdetto, dato con la stessa onestà del dossier gemello: probabile sì, non confermato.** La struttura
di questa pagina — elenco categorizzato di attrezzatura professionale specifica per marca e modello,
aggiornato a data fissa ("Luglio 2026"), organizzato ad accordion — è indistinguibile, come pattern, da
una classica pagina "gear list" che i creator di contenuti costruiscono quasi sempre con link di
affiliazione (Amazon Associates o programmi diretti dei produttori) dietro ogni articolo. **Se è così,
è esattamente il flusso di ricavo "mai censito" a cui alludeva la consegna di questo studio — ma
resta un'inferenza basata sul pattern del formato, non una citazione diretta di un `href` verificato**,
perché quell'`href`, se esiste, vive in una parte del DOM che il nostro scan non ha mai visto. Per
chiuderlo con certezza servirebbe una cattura che espanda ogni riga dell'accordion prima di leggere il
DOM — un miglioramento di metodo da segnare per la prossima passata su questa pagina, non un lavoro da
fare a mano ora.

---

## IL DIFETTO

Tre difetti reali, ciascuno misurato sui cinque file di questo documento:

1. **Il bottone "Coppa" sulla card "Reject socialism." non corrisponde al prodotto mostrato** (una
   maglietta, non una tazza) — verificato su `55-negozio` [y=1600-1703], `href` confermato verso
   `/store/p/mens-classic-tee` in `scheda.json/cta[]`.
2. **Due varianti di prezzo gemelle (Upgrade CM rateizzato, Insider scontato) non hanno un `href`
   proprio catturato** in `56-store/scheda.json/cta[]` — un buco di cattura, non necessariamente un
   buco del sito, ma che impedisce di verificare se le due card portino davvero a pagine diverse o alla
   stessa pagina prodotto con selettore di piano.
3. **`54-attrezzatura` mostra 75 articoli attrezzatura/software ma zero link esterni nel DOM
   catturato** — il widget ad accordion nasconde qualunque link di affiliazione dietro uno stato
   espanso mai raggiunto dal nostro scan; il flusso di ricavo ipotizzato dalla consegna di questo studio
   resta plausibile ma non dimostrato con una citazione diretta.

---

## LEZIONI PER I NOSTRI LANCI

1. **Prezzo subito sui prodotti a basso rischio, prezzo dietro un click sui prodotti ad alto ticket** —
   il pattern di `55`/`56` (nessun prezzo su corsi da centinaia di euro, prezzo esplicito su
   libro/gadget da 19-25€) è applicabile ai nostri cataloghi quando il rapporto fra il prodotto più
   economico e quello più caro supera un ordine di grandezza, come qui (19€ contro 649€, 34 volte).
2. **Se offriamo un piano rateale, non deve costare di più della soluzione unica** — qui 216,33€×3
   (648,99€) contro 649,00€ è sostanzialmente lo stesso prezzo: un piano rateale percepito come "gratis"
   nella sua comodità aumenta la conversione senza dover giustificare un sovrapprezzo.
3. **Ogni bottone deve essere riverificato quando cambia il prodotto sotto di esso** — l'errore
   "Coppa" su una maglietta è un promemoria concreto: quando aggiorniamo la fotografia o l'assortimento
   di una card prodotto, il testo del bottone va controllato lo stesso giorno, non number a campione
   mesi dopo.
4. **Una gear-list con link di affiliazione va costruita in modo che il link sia visibile anche a
   widget/DOM collassato** — se mai costruiamo una pagina di attrezzatura consigliata per i nostri
   corsi, il link di acquisto/affiliazione non va nascosto dietro un accordion che richiede
   un'interazione: sia per la nostra stessa tracciabilità interna sia per l'indicizzazione, il link va
   esposto già nello stato di default della riga.
5. **Il differenziatore "con AI" a costo marginale zero è una leva di posizionamento, non di prezzo** —
   il Manuale del copywriter "+ prompt AI" costa uguale alla versione senza: se aggiungiamo asset AI ai
   nostri prodotti, possiamo usarli per attirare un segmento di pubblico diverso (chi cerca
   specificamente "prompt AI") senza dover giustificare un prezzo diverso, a patto che il costo di
   produzione dell'aggiunta sia realmente trascurabile.

## Nota sulla lunghezza

Il documento è vicino alla soglia di 2.500 parole di sostanza richieste, non oltre: le cinque pagine di
questo studio sono strutturalmente più povere di testo libero rispetto alle quattro del dossier gemello
(negozio, categorie e liste prodotto, non narrazione) — 252 blocchi di testo complessivi fra le cinque
`copy-integrale.md`, contro gli oltre 480 dell'altro documento. Il materiale verificabile (listino,
etichette, struttura a tre pagine store/categoria/catalogo, gear list da 75 articoli) ha comunque
permesso di coprire ogni domanda della consegna con citazioni dirette e coordinate `y`, senza
riempitivo: dove il materiale finiva, il paragrafo si è chiuso.

## Collegamenti

- `capture/55-negozio/copy-integrale.md`, `.../scheda.json`, `.../desktop-01.png`,
  `.../desktop-02.png` — la vetrina-catalogo a 8 card senza prezzo
- `capture/56-store/copy-integrale.md`, `.../scheda.json`, `.../desktop-01.png`,
  `.../desktop-06.png` — il negozio reale con listino completo
- `capture/57-store-aps/copy-integrale.md`, `.../scheda.json` — la categoria filtrata dello stesso store
- `capture/53-risorse/copy-integrale.md`, `.../scheda.json` — i video YouTube gratuiti, non affiliazione
- `capture/54-attrezzatura/copy-integrale.md`, `.../scheda.json`, `.../desktop-01.png`,
  `.../desktop-03.png` — la gear list da 75 articoli con link probabilmente nascosti nell'accordion
- [50-52-58-macchina-della-prova.md](50-52-58-macchina-della-prova.md) — il dossier gemello, con lo
  stesso limite di metodo (widget JS invisibili al nostro scan) trovato su Trustpilot ed Elfsight
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
