---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #blog #corpus #copywriting #seo #cta #onda-f
Created: 2026-09-09
Last updated: 2026-09-09
---

# STUDIO CORPUS — blog.andrei-copy.com (onda F)

**Fonte struttura:** `capture/_corpus-blog/corpus.json` (preso il 2026-09-09, 165 URL totali sotto il dominio, 104 marcate "articolo", 61 non-blog).
**Fonte testo:** quattro campioni integrali in `capture/60-blog-numero-91/`, `capture/60-blog-domanda-funnel/`, `capture/60-blog-titolo-lungo/`, `capture/60-blog-commerciale-corsi/` (ognuno con `copy-integrale.md`, `scheda.json`, `cta_out.txt`).

> Il blog è il motore di posizionamento organico di Andrei Pascu: non vende in prima persona nella maggior parte dei casi, ma costruisce le pagine che Google indicizza e che poi spingono verso `/funnel-operator`, `/vendita`, `/outheadline`, `/manuale-del-copywriter`. Questo studio misura come è costruito quel ponte, non solo come sono scritti i titoli.

---

## DELTA ALLA FABBRICA

**CANONE:** un articolo di blog ha **al massimo un bottone-CTA commerciale nel corpo**, mai due in competizione. Confermato su tutti e quattro i campioni: `60-blog-numero-91` ha un solo bottone (`Scopri di più` → `/outheadline`), `60-blog-titolo-lungo` ha un solo bottone (`Maggiori informazioni sul corso di vendita` → `/vendita`), `60-blog-domanda-funnel` ha un solo bottone (`Informazioni su Funnel Operator` → `/funnel-operator`, anche se preceduto da un link di testo verso la stessa pagina), `60-blog-commerciale-corsi` non ne ha **zero**. Mai un articolo con due prodotti diversi proposti nello stesso pezzo.

**PATTERN:** il bottone finale non compare mai a freddo. È sempre preceduto da una riga di "setup" che nomina il prodotto e ne dichiara l'unicità o lo sconto attivo — testuale, verificato:
- `60-blog-numero-91`, y=6298: *"Ho realizzato un intero corso su come scrivere delle headline estremamente persuasive. È l'unico corso in Italia incentrato unicamente sulle Headline. Se vuoi darci un'occhiata, trovi un pulsante qui sotto:"*
- `60-blog-titolo-lungo`, y=10182: *"Se vuoi approfondire il tema della vendita come si deve [...] ti lascio la pagina con le informazioni sul mio corso di vendita. Adesso lo trovi anche in promozione con 40€ di sconto."*
Il bottone non è mai la prima menzione del prodotto: è la chiusura di una frase che ha già venduto la ragione per cliccare.

**GATE:** prima di pubblicare un articolo, verificare che esista un prodotto tematicamente coerente con l'argomento (headline → corso headline, funnel → corso funnel, vendita → corso vendita). Se non esiste un prodotto coerente, **non forzare un CTA fuori tema**: `60-blog-commerciale-corsi` dimostra che Andrei preferisce zero CTA a un CTA disallineato — l'articolo parla di "come costruiamo i corsi" in astratto e non spinge su un corso specifico perché il pezzo è un contenuto di fiducia/brand, non un contenuto di vendita. La Fabbrica deve marcare ogni bozza di articolo con un campo esplicito `prodotto_collegato: si/no` prima di scriverla, non deciderlo a posteriori.

---

## COSA COPRE IL BLOG

Il file `corpus.json` marca 104 URL come "articolo", ma **solo 37 di queste sono articoli veri con un titolo scritto e un testo**. Le altre 67 sono pagine tassonomiche generate automaticamente da Squarespace: 13 pagine di categoria (`/blog/category/Copywriting`, `/blog/category/Business+Online`, ecc.) e 54 pagine di tag (`/blog/tag/trading`, `/blog/tag/fiverr`, ecc.), verificate contando i pattern `/category/` e `/blog/tag/` dentro l'array `articoli` del file. Questo è rilevante perché le "misure" dichiarate nel file (vedi sezione successiva) sono calcolate su tutte e 104 le voci insieme, mescolando titoli reali ed etichette di una sola parola. Il raggruppamento tematico che segue è fatto sui **37 titoli reali**, non sulle 104 voci, per non contare due volte lo stesso argomento (un articolo + il suo tag).

| Tema | Titoli reali | Esempi |
|---|---|---|
| Copywriting: tecnica e formule | 9 | headline copywriting 91 tecniche, copywriting 5 formule per cta, copywriting 3 principi di vendita, le 6 basi per fare copywriting, trucchi psicologici per generare curiosità |
| Identità professionale, clienti, pricing | 9 | 5 motivi per assumere un copywriter, il mindset del copywriter, come farti pagare 35k a cliente, copywriting come trovare clienti, cosa è un funnel operator, preventivo cosa scrivere |
| Fare soldi online / modelli di business | 8 | tier list 32 modi per fare soldi online, come fare soldi online (x2 varianti), trading affidabile o no, fiverr sopravvalutato, legge della domanda e dell'offerta |
| Mindset e crescita personale | 4 | il blueprint per essere estremamente produttivo, mindset: vivere una vita più positiva, come uscire dal matrix, come nasce un fuffaguru |
| Analisi/casi studio marketing (stagionali) | 3 | 6 migliori campagne di marketing di Natale, analisi copywriting Super Bowl, novità ChatGPT-4 Omni |
| Brand e fiducia (su Andrei / sui corsi) | 2 | stai parlando davvero con Andrei Pascu, le regole con cui costruiamo i nostri corsi |
| Crescita social/content | 1 | come fare views con qualsiasi argomento (TikTok/Reels/Shorts) |
| Anomalia (slug illeggibile) | 1 | `jw15fyf7s7orrthph3bpjgpjmpk3jo` — nessun titolo leggibile, probabile pagina di test o articolo cancellato con URL rimasto indicizzato |

Somma: 37. Il blog **non esiste per parlare di prodotto** — esiste per occupare due aree di ricerca: "sono un copywriter/voglio diventarlo" (18 titoli su 37, quasi metà) e "voglio fare soldi online in generale" (8 titoli su 37). Il tema "corsi" in senso stretto compare solo una volta come articolo dedicato, ed è proprio quello senza CTA (vedi sotto).

La lista dei 54 tag conferma la stessa geografia ma più estesa nel tempo: compaiono `dropshipping`, `network`, `reselling`, `scam`, `truffa`, `outreach`, `cold+dm`, `video+editing` — argomenti trattati in passato ma i cui articoli non sono più (o non sono ancora) nella lista dei 37 titoli reali catturati. Le 13 categorie includono anche `Recipe` e `Wellness`, due categorie Squarespace che non corrispondono a nessun articolo reale nel campione — quasi certamente categorie di default del template mai ripulite.

---

## LA FORMA DEI TITOLI

Il file dichiara, sulle 104 voci totali: titoli con numero 18 (17%), titoli domanda/come 12 (12%), parole per titolo minimo 1 / media 3,4 / massimo 15.

Ricalcolando solo sui 37 titoli reali (escluse le 67 pagine tassonomiche, che essendo etichette da 1-2 parole abbassano artificialmente la media e la percentuale di titoli con numero) il quadro cambia molto:

| Misura | Su 104 voci (corpus.json) | Su 37 titoli reali (ricalcolo) |
|---|---|---|
| Titoli con numero | 18 (17%) | 17 (**46%**) |
| Titoli domanda/come | 12 (12%) | 7 (19%) |
| Parole per titolo (min/media/max) | 1 / 3,4 / 15 | 1 / **7,8** / 15 |

Il valore massimo (15 parole) coincide nei due calcoli, ed è lo stesso titolo: *"Copywriting: 3 principi di vendita che un copywriter deve conoscere (+ esempio un del c\*\*\*o… letteralmente ;)"* — il campione `60-blog-titolo-lungo`. Il valore minimo (1 parola) nel ricalcolo sui titoli reali è lo slug anomalo `jw15fyf7s7orrthph3bpjgpjmpk3jo`, non un titolo vero: **il vero titolo più corto tra i 37 è "Tree of knowledge"-style di 3-4 parole**, non un titolo di 1 parola.

Formule di titolo effettivamente usate, lette sui 37 titoli:
- **Numero/listicle** (quasi la metà): "10 strategie", "5 motivi", "91 tecniche", "3 principi", "5 formule", "7 consigli", "6 consigli pratici", "4 accorgimenti", "32 modi", "6 campagne", "5 pubblicità", "35k" — quasi sempre un numero dispari o comunque non tondo (91, 35k) più credibile di un numero tondo.
- **Imperativo "come" / how-to** (dominante sul formato domanda pura): "come fare soldi online" (×2), "come farti pagare", "come nasce un fuffaguru", "come uscire dal matrix", "come vendere te stesso", "come fare views". Il "come" supera nettamente il punto interrogativo vero e proprio: nei 37 titoli reali il "?" esplicito compare solo su "Cos'è un Funnel Operator?" e implicitamente su "Fiverr sopravvalutato? Ecco perché" e "Trading: affidabile o no".
- **Promessa/beneficio in coda**: "...che vendono sempre", "...per il titolo perfetto", "...per aumentare le tue chance di vendita" — il beneficio quasi sempre chiude la frase, non la apre.
- **Contro-intuizione/debunking**: "i veri motivi per cui non stai facendo soldi", "fiverr sopravvalutato", "come nasce un fuffaguru", "come uscire dal matrix" — la costruzione "quello che pensi è sbagliato, ecco la verità" ricorre più volte.
- **Stagionalità/cultura pop**, usata ma rara (2 titoli su 37): Natale, Super Bowl. Non è una leva sistematica, è opportunistica.

Formule **mai usate** nei 37 titoli reali: nessun titolo con nome di città o location, nessun "top X errori" nel senso negativo classico, nessuna data/anno nel titolo, nessun superlativo isolato senza numero a supporto (mai "il migliore", sempre "i 5 migliori"), nessun clickbait puro senza contenuto dichiarato (zero "non crederai a cosa è successo" scollegato dal tema).

---

## IL PONTE VERSO I PRODOTTI

Qui sta la parte che conta, ed è la più eterogenea dei quattro campioni: non esiste un unico schema di CTA, esistono almeno tre comportamenti diversi.

**`60-blog-numero-91` (Headline Copywriting: 9+1 tecniche) — 1 CTA, a fine articolo.**
Un solo link commerciale in tutto il corpo (~1.347 parole): il bottone `Scopri di più` → `https://www.andrei-copy.com/outheadline`, a y=6505 su un'altezza pagina di 7.911px (cioè all'82% della pagina, subito dopo l'ultimo dei 9 consigli e prima della sezione di paginazione). Nessun altro link a prodotto nel corpo. Rapporto CTA/parole: 1 ogni ~1.350 parole.

**`60-blog-domanda-funnel` (Cos'è un Funnel Operator?) — 3 destinazioni commerciali/esterne, precoci e ripetute.**
Qui il comportamento è opposto: il primo link commerciale compare a y=1408 su un'altezza totale di 8.288px, cioè al **17% della pagina**, dopo appena due paragrafi:
- `AP Sales` → `https://www.apsales.eu` (link all'agenzia, non al corso)
- subito dopo, nello stesso paragrafo, un link di testo `Funnel Operator"` → `/funnel-operator` (non è un bottone, è un `<a>` dentro la frase — non compare nell'elenco "cta" dello scheda.json perché quello cattura solo elementi con stile da bottone, non i link semplici in mezzo al testo)
Poi, molto più avanti (y=5810-5868, al 70% della pagina), lo stesso URL `/funnel-operator` viene ripetuto due volte consecutive: prima come link di testo (`questa pagina.`) e subito dopo come bottone (`Informazioni su Funnel Operator`) — ridondanza intenzionale, stesso link due volte di fila. In totale: **3 rimandi a `/funnel-operator`** (1 precoce + 2 tardivi) più 1 rimando esterno all'agenzia. Ci sono anche due link editoriali interni non commerciali (`attività di servizi autonoma` → altro articolo del blog, `trading` → una pagina tag), che servono a tenere il lettore dentro il blog, non a vendere.

**`60-blog-titolo-lungo` (Copywriting: 3 principi di vendita) — 3 touchpoint di conversione, con un canale extra.**
Un link di testo soft a metà pagina (y=9332, dentro l'esempio sullo Unique Selling Point): `corso di vendita telefonica` → `https://www.andrei-copy.com/vendita101`. Poi, a y=10302 (94% di un'altezza di 11.778px), il bottone finale `Maggiori informazioni sul corso di vendita` → `/vendita`. **Da notare: le due URL sono diverse** (`/vendita101` a metà pagina, `/vendita` nel bottone finale) — può essere una vecchia slug, un test A/B o due pagine diverse per lo stesso corso; il dato è riportato così com'è, senza inventare una spiegazione. Infine, subito dopo il bottone, un terzo canale di conversione mai visto negli altri tre campioni: un invito a scrivere in DM su Instagram con una parola chiave per sbloccare uno sconto (`Ps: per avere lo sconto, puoi direttamente scrivermi un dm con scritto "SCONTO VENDITA" al mio profilo instagram` → link a `https://www.instagram.com/andrei.bsns/`). Qui la CTA non è solo "vai alla pagina", è "vai alla pagina O scrivimi in privato con questo codice" — doppio percorso di conversione nello stesso articolo.

**`60-blog-commerciale-corsi` (le regole con cui costruiamo i nostri corsi) — 0 CTA commerciali.**
Fatto misurato, non interpretazione: sui 119 blocchi di testo e ~468 parole di corpo, **nessun link punta a una pagina di vendita, allo store o a un corso specifico**. Gli unici tre link cliccabili nel corpo sono tag chip a fine pagina (`andrei pascu formazione`, `corsi online`, `formazione pratica`), tutti e tre verso pagine `/blog/tag/...`, cioè verso altre pagine del blog, non verso un acquisto. È l'articolo il cui titolo promette più di tutti in tema "corsi" e l'unico a non vendere nulla: probabile scelta deliberata di posizionarlo come contenuto di fiducia/autorità (il "manifesto pedagogico" di Andrei) piuttosto che come pagina di vendita.

Sintesi numerica: da 0 a 3 touchpoint commerciali per articolo, nessuna costante di posizione (a volte all'82% della pagina, a volte al 17%), ma **sempre** una frase di setup prima di ogni bottone, mai un bottone isolato senza contesto.

---

## LA STRUTTURA DI UN SUO ARTICOLO

Letta sui quattro testi integrali (unica fonte per questa sezione, nessuna estrapolazione dagli altri 100 titoli):

**Apertura.** Non c'è un solo schema, ce ne sono almeno due ricorrenti: (a) citazione autorevole esterna nelle prime righe (`60-blog-numero-91` apre con una citazione di David Ogilvy sull'headline, y=693, prima ancora di qualunque frase propria), oppure (b) domanda diretta di auto-verifica al lettore (`60-blog-titolo-lungo` apre con *"ma tra queste sai padroneggiare quella della vendita?"*, y=823). `60-blog-domanda-funnel` aggiunge un elemento non visto altrove: un H2 esplicito *"Risposta breve, se non vuoi leggere tutto."* seguito da un solo paragrafo riassuntivo — un vero e proprio TL;DR dichiarato, prima di entrare nel dettaglio.

**Corpo.** Tre pattern distinti nei quattro campioni:
- Lista numerata con sotto-titoli H4 ripetuti (numero + nome tecnica), uno per ogni punto: `60-blog-numero-91`, 9 tecniche + 1 bonus, ognuna 2-6 frasi.
- Formato FAQ con domande vere come H3 (*"Funnel Operator non è un copywriter glorificato?"*, *"E' facile fare il Funnel Operator?"*) a cui segue una risposta diretta in 1-3 frasi: `60-blog-domanda-funnel`. Nota tecnica: questo articolo usa il tag `h1` per sei sotto-sezioni diverse dello stesso pezzo (non `h2`), verificato nell'array `headings` di `scheda.json` — gerarchia di intestazioni non standard, possibile difetto SEO/accessibilità (vedi sezione successiva).
- Narrazione con dialogo simulato del lettore per continuare il flusso (*"Mhmm Andrei, ma dopo averle anticipate come faccio a gestirle?"*) e un esempio volutamente estremo per essere memorabile (l'esempio del dildo da 18 cm per illustrare la gestione delle obiezioni): `60-blog-titolo-lungo`. Tecnica di scrittura riconoscibile: pone la domanda che il lettore si starebbe già facendo, poi risponde, simulando una conversazione.
- Manifesto in principi brevi, ciascuno un H1 imperativo di 2-5 parole seguito da 1-2 frasi di spiegazione senza dati a supporto (*"Problema prima, soluzione dopo."*, *"Applicare, non memorizzare."*): `60-blog-commerciale-corsi`, 9 principi in fila, poi una sezione "Le regole valgono ovunque" con bullet su Video/Riassunti/Dashboard/Quiz/Area privata/Gruppo Telegram (i "moduli" reali dei suoi corsi, elencati come fatto, non venduti).

**Chiusura.** Anche qui tre esiti diversi: firma personale esplicita (*"Buon lavoro e alla prossima. Andrei"*, in `60-blog-titolo-lungo`, dopo il CTA e il link Instagram), CTA nuda senza sign-off (`60-blog-numero-91`, finisce sul bottone), oppure nessuna vera chiusura — l'articolo si esaurisce nell'ultimo principio e passa direttamente ai tag/paginazione (`60-blog-commerciale-corsi`, `60-blog-domanda-funnel`).

**Lunghezza misurata** (conteggio parole sul corpo articolo, esclusi nav/footer/paginazione, deduplicando le ripetizioni immediate heading+grassetto — stima per difetto/eccesso di pochi punti percentuali, non un conteggio tipografico esatto):

| Campione | Parole corpo (circa) | Altezza pagina | Blocchi testo (scheda.json) |
|---|---|---|---|
| 60-blog-commerciale-corsi | ~468 | 10.333px | 119 |
| 60-blog-domanda-funnel | ~699 | 8.288px | 109 |
| 60-blog-numero-91 | ~1.347 | 7.911px | 136 |
| 60-blog-titolo-lungo | ~1.890 | 11.778px | 175 |

Non c'è un target di lunghezza fisso: da 468 a quasi 1.900 parole, un fattore 4×. L'altezza pagina non è un proxy affidabile della lunghezza testuale (`60-blog-commerciale-corsi` è la seconda pagina più alta ma la più corta a parole, perché piena di immagini schema — 15 immagini contro le 8 di `60-blog-numero-91`).

---

## COSA IMPARIAMO PER IL NOSTRO BLOG

- Un solo bottone-CTA per articolo, mai due: la disciplina osservata in tutti e quattro i campioni va copiata come regola fissa, non come opzione stilistica.
- Il bottone va sempre preceduto da una frase che nomina il prodotto e la sua unicità/promozione attiva: mai un bottone "nudo" senza la frase di setup nella riga immediatamente precedente.
- Titoli con numero: puntare al 40-46% degli articoli con numero in titolo (non al 17% che viene fuori se si contano anche le pagine tag) — usare numeri non tondi (91, 35k) quando possibile per credibilità.
- Il formato "come" (imperativo/how-to) batte nettamente il punto interrogativo puro: preferire "Come fare X" a "Cos'è X?" quando entrambi sono disponibili come frame per lo stesso argomento.
- Un articolo può legittimamente avere zero CTA se è un contenuto di fiducia/brand (vedi `60-blog-commerciale-corsi`): non forzare la vendita in ogni pezzo, ma dichiararlo prima di scriverlo (campo `prodotto_collegato: si/no`), non scoprirlo a revisione fatta.
- Quando un tema ha davvero un prodotto dietro, ripetere il link al prodotto anche 2-3 volte nello stesso articolo (early + late) funziona meglio di un solo rimando tardivo: pattern osservato in `60-blog-domanda-funnel`, con link a `/funnel-operator` sia al 17% che al 70-71% della pagina.
- Un canale di conversione alternativo (DM con parola chiave e sconto) accanto al link diretto amplia la presa senza cannibalizzare il CTA principale: vale la pena testarlo, osservato una sola volta su quattro ma con un meccanismo chiaro e riproducibile.
- Non pubblicare pagine di tag/categoria come se fossero contenuto: il 64% delle URL "articolo" del corpus di Andrei sono in realtà pagine tassonomiche a bassissimo contenuto — un rischio di contenuto sottile che la Fabbrica deve evitare fin dall'architettura dell'informazione (decidere quali tag/categorie generano pagine pubbliche indicizzabili, e quali no).
- Aprire con un TL;DR esplicito (H2 "Risposta breve, se non vuoi leggere tutto") è un pattern isolato ma solido per articoli lunghi/tecnici: rispetta il lettore che scansiona.
- Variare la lunghezza in base al tema, non forzare un conteggio parole fisso: 468 parole per un manifesto di principi, quasi 1.900 per un articolo che deve insegnare un intero framework di vendita con esempi.

---

## IL DIFETTO

**Difetto 1 — misurato sul corpus intero.** Il 64% delle URL classificate come "articolo" nel file `corpus.json` (67 su 104) non sono articoli: sono 13 pagine di categoria e 54 pagine di tag generate automaticamente da Squarespace, quasi certamente a contenuto duplicato o quasi-vuoto (liste di titoli di altri articoli). Solo 37 URL (36%) sono contenuto editoriale vero. Questo non è solo un problema del nostro conteggio: è un problema strutturale del sito di Andrei — ogni frequenza-parola o percentuale calcolata ingenuamente sulle "104 pagine del blog" (come il file stesso dichiara nel blocco `misure`) è inquinata da etichette di tag, non da titoli scritti. Chi studia questo blog copiando i numeri dichiarati senza aprire l'array rischia di concludere che Andrei scrive titoli brevi (3,4 parole medie) quando in realtà i suoi titoli reali sono lunghi quasi 8 parole in media.

**Difetto 2 — misurato su un campione.** `60-blog-commerciale-corsi`, l'unico dei quattro campioni dedicato esplicitamente al tema "come costruiamo i corsi", non contiene nessun link a nessuna pagina di vendita: 0 CTA su ~468 parole e 119 blocchi di testo. Che sia una scelta deliberata (contenuto di fiducia) o un'occasione persa (il pezzo che più di tutti dovrebbe convertire verso `/store` o una pagina corsi generica, e non lo fa) resta un fatto misurabile, non un'opinione: chi legge quell'articolo fino in fondo e vuole comprare un corso non trova un solo link per farlo.

**Difetto 3 — misurato su un campione.** `60-blog-domanda-funnel` usa il tag `h1` per sei sotto-sezioni diverse dello stesso articolo (verificato nell'array `headings` di `scheda.json`: sei elementi `h1` distinti oltre al titolo principale), invece di una gerarchia `h1 → h2 → h3` standard. Effetto pratico: un motore di ricerca o uno screen reader vede sette titoli di primissimo livello nella stessa pagina, senza gerarchia — un difetto tecnico-SEO misurabile, non stilistico.

---

## COSA NON È STATO LETTO (dichiarazione)

Il corpus contiene 104 URL marcate "articolo". **4 sono state aperte e lette integralmente** (i quattro campioni citati in questo documento, con testo completo in `copy-integrale.md` e dati strutturali in `scheda.json`). **Le altre 100 non sono state aperte.** Di conseguenza:
- Tutte le conclusioni delle sezioni "COSA COPRE IL BLOG" e "LA FORMA DEI TITOLI" valgono **solo sui titoli/URL** delle 100 non lette (e sui 37 titoli reali che ne fanno parte), non sul loro testo, sulla loro struttura interna o sulle loro CTA — quei dati non esistono perché quelle pagine non sono state aperte.
- Tutte le conclusioni delle sezioni "IL PONTE VERSO I PRODOTTI", "LA STRUTTURA DI UN SUO ARTICOLO" e i difetti #2 e #3 valgono **solo sui quattro campioni letti** e sono presentate come tali (pattern osservati su 4/104 pezzi, non come legge generale del blog) — dove il documento generalizza ("sempre", "mai") lo fa esplicitamente riferendosi al comportamento confermato nei quattro campioni, non a un'estrapolazione sui 100 articoli non letti.
- Il difetto #1 è l'unico dato che copre l'intero corpus (104 voci), perché è calcolato sugli URL stessi (pattern `/category/` e `/blog/tag/`), non sul testo delle pagine.
