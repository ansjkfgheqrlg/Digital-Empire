---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #cassa #checkout #stampo #pre-checkout #onda-c
Created: 2026-09-08
Last updated: 2026-09-08
---

# La macchina della cassa — dodici gradini, due stampi, un link rotto

**Dodici catture, tutte del 2026-09-08:** `30-pre-copy` · `31-pre-checkout-cm` · `32-pre-checkout-cmb` ·
`33-outemail-pre` · `34-outheadline-pre` · `35-vendita101-pre` · `36-pre-outviral-shop` ·
`37-stripe-claude-speedrun` · `38-presto-disponibile` · `39-ricevi-email` · `41-aps-assistenza` ·
`42-acquista-v101`. Questo documento **estende** il lavoro già fatto in
`reports/24-25-27-28-macchina-del-funnel.md` (e la sua `-COPY.md`), che aveva smontato una sola
cassa del genere (`/outfunnel-1`, 98,00 €, codice `CWSHOP`) insieme a due pagine-ponte e un gradino
di sola-aggiunta. Qui non si ripete quella lettura: si dimostra che quella cassa **non era un caso
isolato ma uno stampo**, se ne trova un secondo mai visto prima, e si scopre un link che porta
diritto a una pagina che non esiste.

---

## DELTA ALLA FABBRICA

**CANONE.** Una cassa mono-prodotto non è un pezzo di design scritto a mano ogni volta: è **un
unico file HTML con cinque variabili** (nome prodotto, prezzo, colore d'accento, quale porzione del
nome si colora, testo del bottone) più un blocco fisso — occhiello, istruzione con eventuale sconto,
"Una tantum", bottone — che non cambia mai, nemmeno per una virgola, da un prodotto all'altro. La
prova è misurata sotto: quattro pagine confrontate riga per riga condividono **la stessa identica
frase di 24 parole** carattere per carattere. Un secondo stampo, per i prodotti a più livelli di
prezzo (corsi/mentorship), sostituisce prezzo-singolo+sconto con un blocco a checklist (✓) e due
bottoni gemelli — ma resta comunque uno stampo unico, non due pagine scritte separatamente.

**PATTERN — due, entrambi confermati da più di un uso.**

1. **`cassa-prodotto-digitale`** (dimostrato ora da 5 usi: `outFunnel` già noto + `outEmail`,
   `outHeadline`, `Vendita101`, `outViral 2` qui misurati). Occhiello corsivo con puntini di
   sospensione, h1 con una porzione colorata, istruzione fissa con sconto incorporato, nome ripetuto,
   prezzo isolato, "Una tantum", bottone "Acquista [Prodotto]".
2. **`cassa-corso-a-livelli`** (dimostrato da 2 usi: `Copywriting Mentorship` e `Copywriting
   Mentorship BASE`, stesso corso due prezzi). Occhiello statico (non corsivo, senza puntini),
   checklist a sette righe con segno di spunta, prezzo con etichetta "pagamento unico", bottone
   "Entra in [Nome livello]". **Nessuno sconto, nessun codice**: la leva qui è la scelta fra due
   piani, non il taglio prezzo.

**GATE.** Tre domande nuove per il controllo di una cassa: **(1)** se esiste un pulsante "Acquista"
su una pagina di vendita, il suo `href` porta a una pagina che **risponde con un prezzo reale**, o a
un 404? Verificato ora su tutte le pagine di questo lotto più le due pagine sorgente che le
richiamano — un caso su due controllati è rotto (sotto, `IL DIFETTO`). **(2)** se un codice sconto
compare su una cassa, è verificato **anche sulle altre casse dello stesso sito** prima di dichiararlo
"specifico del prodotto" — qui il codice `CWSHOP` risulta identico su cinque prodotti diversi, non
uno. **(3)** ogni cassa dichiara la sua altezza e i suoi blocchi *prima* di essere clonata: uno
scarto oltre il 2% dallo stampo di riferimento (qui: 1.509–1.526 px, 40 blocchi) segnala una cassa
che si sta allontanando dal canone, non un errore di misura.

---

## IL MODELLO UNICO

Le quattro pagine `33-outemail-pre` (1.526 px), `34-outheadline-pre` (1.509 px), `35-vendita101-pre`
(1.509 px) e `36-pre-outviral-shop` (1.515 px) hanno **tutte** 40 blocchi di testo. Confrontate riga
per riga (stesso ordine di `y`, scostamenti di pochi pixel dovuti solo alla lunghezza del nome
prodotto), il testo è quasi interamente lo stesso file con cinque parole cambiate.

### Il blocco che è identico, carattere per carattere

**L'istruzione operativa con lo sconto incorporato** — confrontata sui quattro `copy-integrale.md`:

- `33-outemail-pre` `[y=275]`: «Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed
  entrare. Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto.»
- `34-outheadline-pre` `[y=258]`: stessa stringa, **zero differenze**.
- `35-vendita101-pre` `[y=258]`: stessa stringa, **zero differenze**.
- `36-pre-outviral-shop` `[y=264]`: stessa stringa, **zero differenze**.

Ventiquattro parole, ripetute quattro volte senza mutare un solo carattere — non un template con
segnaposto per il codice: **il codice stesso è cablato nel testo**, non è una variabile.

**"Una tantum"** — condizione di pagamento, identica su tutte e quattro:
`33` `[y=557]`, `34` `[y=540]`, `35` `[y=540]`, `36` `[y=546]`. Due parole, zero varianti.

**L'occhiello** — «Stai acquistando…» in corsivo (`em`), con gli stessi tre puntini di sospensione,
su tutte e quattro: `33` `[y=153]`, `34` `[y=153]`, `35` `[y=153]`, `36` `[y=153]` — **la stessa `y`
assoluta**, perché il blocco sopra (menu) ha sempre la stessa altezza.

**Il piede e il menu** — dodici righe identiche per struttura e testo su tutte e quattro (skip-link,
Claude Speedrun, Accedi, La mia storia, Store, Recensioni, Risorse, Blog, disclaimer legale,
indirizzo con P.IVA, privacy, bottone cookie) — stesso fenomeno già documentato nel rapporto
`-COPY.md` precedente, qui esteso a quattro pagine in più.

### Cosa cambia, e come cambia

| Elemento | `outEmail` | `outHeadline` | `Vendita101` | `outViral 2` |
|---|---|---|---|---|
| Nome prodotto (h1) | outEmail | outHeadline | Vendita101 | outViral 2 |
| Font-size h1 | 78,2px | 55,9px | 63,1px | 72,6px |
| Porzione colorata | «out» | «out» | «101» | «out» |
| Colore accento | `#b3fbff` ciano | `#61bf36` verde | `#0095ff` blu | `#9d52ff` viola |
| Prezzo | 139,00 € | 98,00 € | 400,00 € | 250,00 € |
| Testo bottone | Acquista outEmail | Acquista outHeadline | Acquista Vendita101 | Acquista outViral 2 |

**Osservazione che corregge il canone precedente.** Il rapporto di costruzione sulle pagine-ponte
aveva stabilito: *un colore per pagina, su una parola sola — il verbo della promessa*
(`/asa` colorava «monetizzare», non «copywriting»). Su queste quattro casse la regola è **diversa**:
il colore non cade sulla parola che porta significato (Funnel, Email, Headline, Viral), cade
**sempre sul prefisso di famiglia «out»** — un frammento che di per sé non vuol dire niente — tranne
in `Vendita101`, dove non c'è prefisso «out» e il colore cade sul **suffisso numerico «101»**. La
regola vera, quindi, non è "colora il significato": è **"colora la porzione fissa/brand del nome, non
la porzione variabile"** — l'esatto contrario di quanto osservato sulle pagine-ponte. Sono due
canoni diversi per due funzioni diverse: sulla pagina-ponte il colore guida l'attenzione verso
un'azione; sulla cassa il colore funziona come **logo-lockup**, la firma visiva della famiglia di
prodotto («out-» colorato = riconosci la linea outFunnel/outEmail/outHeadline/outViral), coerente col
fatto che `outFunnel` (rapporto precedente) colora anch'esso «out», in un quinto colore (`#13989a`).
Cinque prodotti, cinque colori diversi, sempre sulla stessa porzione del nome: è un sistema di
codifica-colore-per-canale, non un accento persuasivo.

**Anche il font-size dell'h1 non è una scelta manuale.** Il rapporto fra lunghezza del nome e
dimensione del testo è inverso su tutte le cinque misurazioni disponibili (includendo `outFunnel`,
68,3px, 9 caratteri): «outEmail» (8 caratteri) rende al font più grande, 78,2px; «outHeadline» (11
caratteri) al più piccolo, 55,9px. Il contenitore ha una larghezza fissa e il font si restringe per
starci dentro su una riga sola — infrastruttura, non design ripetuto a mano.

### Lo stampo in bianco

```
[MENU — fisso, identico su ogni cassa]
Passa al contenuto · Claude Speedrun · Accedi

[OCCHIELLO — em, corsivo, 16px w300]
Stai acquistando…

[H1 — w700, font-size auto-fit alla larghezza]
[PORZIONE-FISSA-COLORATA][PORZIONE-VARIABILE-BIANCA]
  → es. «out» colorato + «Email» bianco; oppure «Vendita» bianco + «101» colorato

[ISTRUZIONE — p, 16px w300 — TESTO FISSO, MAI RISCRITTO]
Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed entrare.
Ricorda di usare il codice sconto "[CODICE-SCONTO]" per avere il [XX]% di sconto.
  → nei 5 casi noti, [CODICE-SCONTO]=CWSHOP e [XX]=20 non sono mai cambiati:
    di fatto sono costanti, non variabili — vedi "I PREZZI E I CODICI SCONTO"

[NOME PRODOTTO RIPETUTO — div, 24px w300]
[NOME PRODOTTO]

[PREZZO — div, 35.2px w300]
[CIFRA],00 €

[CONDIZIONE — div, 17.6px w300 — TESTO FISSO]
Una tantum

[BOTTONE — div, 16px w600, bg #0062ff, radius 10px]
Acquista [NOME PRODOTTO]

[PIEDE — fisso, identico su ogni cassa, 12 righe]
La mia storia · Store · Recensioni · Risorse · Blog · disclaimer · P.IVA · privacy · cookie
```

Sei segnaposto reali (nome prodotto, font-size derivato, porzione colorata, colore, prezzo, testo
bottone) contro venticinque righe di testo e struttura che non cambiano mai. **Questo è esattamente
il file che Digital Empire deve poter generare a comando** per ogni lancio one-shot: non un template
di design da reinterpretare, ma un file con sei valori da riempire.

### Il secondo stampo — `cassa-corso-a-livelli`

`31-pre-checkout-cm` (2.062 px, 48 blocchi) e `32-pre-checkout-cmb` (2.053 px, 50 blocchi) **non**
appartengono allo stampo sopra: sono un secondo stampo, verificato su due usi. Struttura, riga per
riga:

- occhiello **non corsivo**, tag `h4`, 24px w700: «Stai acquistando» (senza puntini) — stesso testo,
  stessa funzione dello stampo 1, implementazione diversa.
- h1 col nome del corso/livello: «Copywriting Mentorship» `[y=241]` vs «Copywriting Mentorship BASE»
  `[y=230]`.
- h4 fisso: «Questa versione del corso contiene:» — identico su entrambe (`[y=309]` e `[y=280]`).
- **sette righe checklist**, ognuna preceduta da `✓` in un cerchio ambra (`#efab00`, contato 7 volte
  in entrambi gli `scheda.json`, campo `palette_sfondi`). Sei righe sono identiche parola per parola
  fra i due piani (40+ lezioni copywriting, 20+ lezioni clienti, gruppo telegram, PDF/riassunti,
  accesso a vita, esame conclusivo gratuito); **una sola riga cambia**: «Consulenze illimitate con
  Andrei P.» `[y=1008]` sul piano Completo diventa «1 consulenza di 60 min con Andrei P.» `[y=968]`
  sul piano BASE. È l'unica differenza sostanziale fra un prodotto da 999 € e uno da 349 €.
- prezzo isolato con etichetta fissa: «€999 pagamento unico» `[y=514]` / «€349 pagamento unico»
  `[y=474]` — stesso font 40px w700, stessa sotto-etichetta «pagamento unico» 14,4px.
- bottone: «Entra in CM» `[y=1226]` / «Entra in CM BASE» `[y=1217]`.

**Nessuno sconto, nessun codice, su nessuno dei due piani.** La leva di questo stampo non è il
prezzo scontato, è **la scelta fra due offerte della stessa cosa** — un pattern completamente diverso
da quello a sconto, dimostrato dallo stesso venditore sullo stesso sito nella stessa settimana di
cattura, per due famiglie di prodotto diverse (corso strutturato a moduli vs prodotto digitale
one-shot).

---

## LA MAPPA DEI GRADINI

Percorso completo dall'ignaro al pagamento, ricostruito dai campi `cta` di ogni `scheda.json` più una
verifica incrociata sulle pagine sorgente (`05-copy`, `23-vendita`) già presenti nel capture. Dove il
capture non contiene la pagina che porta al gradino, è dichiarato «non trovato nel capture» — non
inventato.

| Pagina | Prodotto | Arriva da | Manda a | Prezzo | Sconto |
|---|---|---|---|---|---|
| `/pre-copy` (30) | Copy.exe: live recording | non trovato nel capture | nessun bottone d'acquisto — solo notifica email | non disponibile | — |
| `/pre-checkout-cm` (31) | Copywriting Mentorship | **verificato**: `/copy` (`05-copy`), bottone «Acquista Completo» → `https://www.andrei-copy.com/pre-checkout-cm` | «Entra in CM», `href=null` (JS/Stripe a runtime) | 999,00 € | nessuno |
| `/pre-checkout-cmb` (32) | Copywriting Mentorship BASE | **verificato**: `/copy` (`05-copy`), bottone «Acquista Base» → `https://www.andrei-copy.com/pre-checkout-cmb` | «Entra in CM BASE», `href=null` | 349,00 € | nessuno |
| `/outemail-pre` (33) | outEmail | non trovato nel capture (presumibile campagna esterna/email) | «Acquista outEmail», `href=null` | 139,00 € | CWSHOP -20% |
| `/outheadline-pre` (34) | outHeadline | non trovato nel capture | «Acquista outHeadline», `href=null` | 98,00 € | CWSHOP -20% |
| `/vendita101-pre` (35) | Vendita101 | non trovato nel capture (e NON è raggiungibile da `/vendita`, vedi `IL DIFETTO`) | «Acquista Vendita101», `href=null` | 400,00 € | CWSHOP -20% |
| `/pre-outviral-shop` (36) | outViral 2 | non trovato nel capture | «Acquista outViral 2», `href=null` | 250,00 € | CWSHOP -20% |
| `/stripe-claude-speedrun` (37) | Claude Speedrun 2 | non trovato nel capture | «Sign Up», `href=null` | non mostrato in pagina | nessuno |
| `/presto-disponibile` (38) | nessuno — placeholder | **verificato su tutte e dodici** le pagine di questo lotto, link «Recensioni» nel piede | nessuno — pagina terminale, e ricircola su se stessa (vedi sotto) | — | — |
| `/ricevi-email-di-andrei-pascu` (39) | lead magnet gratuito (email) | non trovato nel capture | «Clicca e sei dentro», `href=null`, form protetto da reCAPTCHA | gratuito | — |
| `/aps-assistenza` (41) | nessuno — modulo assistenza | non trovato nel capture | «Apri modulo», `href=null` | — | — |
| `/acquista-v101` (42) | dovrebbe essere Vendita101 | **verificato**: `/vendita` (`23-vendita`), bottone «Entra in Vendita101» → `/acquista-v101` `[y=3219]` | pagina 404 — unico link utile è «cliccando qui» → `/` (home) | — | — |

Tre fatti emergono da questa mappa che nessuna singola pagina rivela da sola:

1. **Le quattro casse dello stampo 1 (`33`-`36`) non hanno un ingresso rintracciabile nel sito
   catturato.** Ricerca testuale (`href`) su tutte le 30+ pagine finora catturate: zero corrispondenze.
   Non è un buco della cattura — è coerente con la logica già osservata su `outFunnel`
   (rapporto precedente): sono pagine "buie", raggiungibili solo da link tracciati esterni (email,
   ads, test A/B su headline, contenuto virale) e mai linkate dalla navigazione pubblica. Il nome
   stesso della pagina dichiara il canale: chi arriva a `outEmail` viene da una email, chi arriva a
   `outHeadline` viene da un test di titolo, chi arriva a `pre-outviral-shop` viene da un contenuto
   diventato virale.
2. **Le due casse dello stampo 2 (`31`, `32`) hanno un ingresso verificato e funzionante**: la pagina
   di vendita `/copy` (titolo reale: «Corso Copywriting Online - Con Consulenza Gratuita + Metodi
   Clienti + Aggiornamenti Gratis a Vita») offre i due bottoni fianco a fianco, con `href` assoluti e
   corretti.
3. **Un solo ingresso verificato è rotto**: `/vendita` (titolo reale: «Vendita 101 - Impara a vendere
   prodotti & servizi») manda a `/acquista-v101`, che non esiste. Dettagli sotto, in `IL DIFETTO`.

---

## I PREZZI E I CODICI SCONTO

Ogni cifra e ogni codice trovato nelle dodici pagine, con pagina e coordinata:

| Prezzo | Pagina | `[y]` | Codice sconto | Percentuale |
|---|---|---|---|---|
| 999,00 € (etichettato «€999 pagamento unico») | `/pre-checkout-cm` | 514 | nessuno | — |
| 349,00 € (etichettato «€349 pagamento unico») | `/pre-checkout-cmb` | 474 | nessuno | — |
| 139,00 € | `/outemail-pre` | 515 | **CWSHOP** | 20% |
| 98,00 € | `/outheadline-pre` | 497 | **CWSHOP** | 20% |
| 400,00 € | `/vendita101-pre` | 497 | **CWSHOP** | 20% |
| 250,00 € | `/pre-outviral-shop` | 503 | **CWSHOP** | 20% |
| 98,00 € (`outFunnel`, già noto dal rapporto precedente) | `/outfunnel-1` | 500 | **CWSHOP** | 20% |

**Il codice è pubblico e permanente, e ora è verificato su cinque prodotti, non uno.** Il rapporto
precedente aveva scoperto `CWSHOP` scritto in chiaro su `/outfunnel-1` e l'aveva segnalato come difetto
isolato ("un codice pubblico su una pagina indicizzabile"). Con questo lotto la scoperta cambia
scala: **la stringa esatta `"CWSHOP"` e la percentuale esatta `20%` compaiono, senza una sola
variazione di carattere, su outEmail (139 €), outHeadline (98 €), Vendita101 (400 €) e outViral 2
(250 €)** oltre a outFunnel. Non è un codice promozionale legato a un prodotto o a una campagna: è
**uno sconto strutturale del 20% su tutto il catalogo one-shot**, cablato nel testo statico di ogni
cassa dello stampo 1. Il prezzo "vero" di ciascuno di questi cinque prodotti, per chiunque legga il
testo della pagina fino in fondo, è l'80% del prezzo mostrato in alto: 111,20 € (outEmail), 78,40 €
(outHeadline e outFunnel), 320,00 € (Vendita101), 200,00 € (outViral 2).

Nessun altro codice sconto compare in nessuna delle dodici pagine. Le due casse a livelli (CM/CMB)
non hanno mai un codice: la loro leva di prezzo è la scelta del piano, non lo sconto.

---

## I GRADINI CHE NON SONO CASSE

**`/presto-disponibile` (38)** — «Questa pagina sarà disponibile a breve :)» `[y=277]`, unico
contenuto oltre a menu e piede: nessun prezzo, nessun modulo, nessun bottone diverso dalla
navigazione fissa. Funzione reale, verificata ora e non più solo dedotta: è la **destinazione
universale** del link «Recensioni» nel piede. Cercato nel campo `cta` di tutte e dodici le
`scheda.json` di questo lotto — **dodici su dodici**, senza eccezione, il link «Recensioni» porta a
`/presto-disponibile`. Il dettaglio più interessante: **la pagina stessa `/presto-disponibile`
contiene lo stesso piede**, quindi il suo proprio link «Recensioni» punta a se stessa
(`[y=855]` nel suo `scheda.json`) — un ciclo chiuso, non un errore isolato ma la conseguenza
meccanica di un piede condiviso applicato ovunque senza eccezioni, nemmeno sul placeholder stesso.
La funzione di questa pagina non è quindi "vendere" né "informare": è **assorbire senza rompere** il
click di chiunque cerchi prova sociale su un sito che, al momento della cattura, non ne ha ancora
pubblicata nessuna. Tiene fede alla promessa implicita del link (qualcosa esiste) mentre rimanda la
consegna, senza mai restituire un errore 404 al visitatore che cerca recensioni.

**`/ricevi-email-di-andrei-pascu` (39)** — non è una cassa, è una **squeeze page di lead-gen
gratuita**: h1 «Ma non ti vergogni?» `[y=137]`, corpo «questo è ciò che ti diranno quando
scopriranno che nemmeno paghi per le email di Andrei Pascu…» `[y=289]` (con «nemmeno paghi»
enfatizzato), una freccia emoji «⬇️» `[y=427]` che punta al modulo sottostante, bottone «Clicca e
sei dentro» `[y=838]` e disclaimer irriverente: «Rispetto la tua privacy e bla bla bla. Iscrivendoti
accetti termini e condizioni e privacy e bla bla bla.» `[y=942]` — il "bla bla bla" ripetuto due
volte è una scelta di tono deliberata, non un placeholder dimenticato: normalizza il fastidio del
legalese ironizzandolo, mentre il link vero (`termini e condizioni e privacy` → `/privacy-dati-cookie-simili`)
resta comunque presente e cliccabile. Il modulo è protetto da un `iframe` reCAPTCHA Enterprise
(`[y=890]` nel campo `media`), a conferma che questo è un punto di raccolta dati vero, non
decorativo. Funzione reale: costruire lista email gratuitamente, separata da ogni logica di
pagamento — non un gradino verso la cassa ma un canale d'ingresso alternativo.

**`/aps-assistenza` (41)** — modulo di assistenza clienti con un **gate esplicito nel testo**: «
Attenzione: questo modulo è dedicato solo ed esclusivamente a clienti paganti di AP Sales (corsi,
formazione, consulenze, simili). NON è un modulo per richieste di outreach o simili e le
segnalazioni spam verranno segnalate immediatamente.» `[y=323]`, con «NON» in maiuscolo e grassetto
due volte nel testo sorgente (`strong` a `[y=356]` e `[y=384]`). Il bottone «Apri modulo» `[y=449]`
ha `href=null`: apre presumibilmente un modulo incorporato (Typeform o simile) via JavaScript, non
un link diretto. Funzione reale: **filtro anti-rumore prima del contatto umano** — dichiara la
condizione di accesso (cliente pagante) e la conseguenza della violazione (segnalazione) prima ancora
di mostrare il modulo, così il rumore (outreach, spam) si ferma alla lettura del paragrafo, non
all'apertura del form.

Due pagine aggiuntive del lotto non sono casse nemmeno loro, per ragioni diverse dalle tre sopra:
**`/pre-copy` (30)** è una pagina "prodotto non ancora disponibile" — riusa l'apertura «Stai
acquistando» `[y=146]` (qui senza corsivo né puntini, come nello stampo 2) ma la abbandona subito
dopo: «Ancora non è disopnibile l'acquisto della registrazione di Copy.exe. Sarai notificato via
email quando lo sarà; oppure torna a controllare tra un paio di giorni.» `[y=399]` — **nota**: «disopnibile»
è un refuso di «disponibile», pubblicato. Nessun prezzo, nessun bottone d'acquisto: è un segnaposto
di pre-lancio, costruito sull'URL e sul testo d'apertura definitivi prima che il prodotto esista
davvero. **`/stripe-claude-speedrun` (37)** è ancora più scarno: nessun titolo nel DOM
(`"headings": []`, confermato non dedotto), solo «Claude Speedrun 2» `[y=292]` e un bottone grigio
«Sign Up» `[y=359]` — nessuna delle firme testuali della cassa (niente «Stai acquistando», niente
prezzo, niente "Una tantum"). È una porta d'ingresso a un prodotto diverso (Claude Speedrun, non
Copy.exe/outXxx), probabilmente con pagamento gestito interamente fuori pagina da Stripe stesso,
come suggerisce il nome dello slug.

---

## COSA SUCCEDE DOPO IL PAGAMENTO

**Non si capisce, e va dichiarato invece di essere inventato.** Nessuna delle sei pagine con un vero
bottone d'acquisto (`31`, `32`, `33`, `34`, `35`, `36`) contiene, nel testo servito, una sola frase
su cosa succede dopo il click: niente «riceverai un'email con l'accesso», niente menzione di una
pagina di ringraziamento, niente redirect visibile. Tutti e sei i bottoni hanno `href=null` nel
campo `cta` — il pagamento è gestito da JavaScript a runtime (Squarespace Commerce, o per `31`/`32`
uno strato Stripe), e nessun URL di destinazione compare nel documento HTML servito. La ricerca di
`grazie|thank-you|successo|conferma` nei dodici `copy-integrale.md` di questo lotto: **zero
corrispondenze**. L'unica informazione operativa data al lettore, su tutte le sei casse, è quella
già citata nell'istruzione fissa — «loggare nel tuo account, inserire i tuoi dati ed entrare» — che
descrive l'azione nel form di pagamento, non l'esito dopo averla completata.

---

## LEZIONI PER I NOSTRI LANCI

1. **Costruire un generatore di cassa a sei variabili**, non un template da riadattare a mano:
   `NOME_PRODOTTO`, `PREZZO`, `COLORE_ACCENTO`, `PORZIONE_COLORATA` (fissa/brand, mai la parola col
   significato — vedi sopra), `CODICE_SCONTO opzionale`, `TESTO_BOTTONE`. Con questi sei valori una
   nuova cassa mono-prodotto per l'ecosistema LANCI si genera in minuti, sul modello dello stampo in
   bianco sopra.
2. **Font-size dell'h1 auto-fit alla larghezza**, non fisso: se il generatore accetta nomi prodotto
   di lunghezza diversa (da 7 a 12 caratteri come qui), il titolo deve restringersi da solo per stare
   su una riga — infrastruttura once, non un aggiustamento manuale per ogni lancio.
3. **Un solo stampo "a livelli"** per corsi/mentorship con più piani: checklist a spunta, sei righe
   fisse identiche fra i piani, **una sola riga che cambia** (il beneficio che giustifica la
   differenza di prezzo). Non serve differenziare la struttura fra Base e Completo, serve
   differenziare **una riga sola** — è la prova che farlo con due sole variabili (prezzo + riga
   finale) basta a comunicare due offerte distinte.
4. **Il codice sconto è una costante di sistema, non un campo per pagina.** Qui lo stesso codice è
   finito, invariato, su cinque casse diverse — segno che chi lo scrive lo copia da un file, non lo
   inventa per ogni prodotto. Per i nostri lanci: **un solo file di configurazione con il codice
   attivo**, mai una stringa ripetuta a mano nel testo di ogni pagina — così un codice "eterno" non
   nasce per disattenzione, ma resta una scelta esplicita e revocabile in un punto solo.
5. **Gate obbligatorio pre-pubblicazione: ogni bottone "Acquista" con un `href` assoluto va
   verificato con una richiesta HTTP reale prima del lancio**, non fidandosi del nome della pagina di
   destinazione. Qui un solo link rotto (`/vendita` → `/acquista-v101`, 404) blocca l'intero percorso
   d'acquisto di un prodotto da 400 € dalla sua pagina di vendita principale — un test automatico
   da un minuto lo avrebbe preso prima del pubblico.
6. **Se un link secondario di navigazione (tipo "Recensioni") punta a un placeholder, va tracciato
   con una scadenza**, non lasciato lì a propagarsi. Qui il pattern si è diffuso su dodici pagine su
   dodici senza eccezione, incluso un ciclo su se stesso — segno che nessun processo lo ha più
   ricontrollato dopo la prima pubblicazione del piede.
7. **Separare sempre il modulo "cassa" dal modulo "vendita" dal modulo "lead-gen gratuita".** Le sei
   casse misurate qui restano sotto le 40 parole di contenuto proprio (canone già stabilito nel
   rapporto precedente); la squeeze page email (`39`) usa un impianto persuasivo completo (headline
   provocatoria, urgenza sociale, tono ironico) proprio perché non è una cassa. Fondere le due
   logiche in un solo componente riduce la conversione di entrambe.
8. **Un modulo di assistenza con gate esplicito nel testo** (chi può scrivere, chi viene segnalato)
   è infrastruttura riusabile a basso costo: una singola frase di avvertenza prima del form filtra
   outreach e spam senza bisogno di moderazione umana a monte. Vale costruirne un equivalente per i
   canali di supporto di Digital Empire.
9. **Naming per canale, non per campagna generica.** `outEmail`, `outHeadline`, `pre-outviral-shop`
   dichiarano nel nome stesso la fonte di traffico prevista — attribuzione senza bisogno di
   parametri UTM aggiuntivi per capire da dove arriva chi compra quale variante. Per i nostri lanci:
   uno slug per canale di ingresso, tenuto fuori dalla sitemap/nav pubblica di proposito (qui zero
   pagine del sito linkano queste quattro casse), cosi resta tracciabile e non viene mai raggiunto
   per errore da traffico organico non qualificato.

---

## IL DIFETTO

**Un link rotto sulla pagina di vendita di un prodotto da 400 €, misurato e non supposto.**
`23-vendita` (titolo reale: «Vendita 101 - Impara a vendere prodotti & servizi») contiene il bottone
«Entra in Vendita101» con `href="/acquista-v101"`, `[y=3219]` — verificato nel campo `cta` del suo
`scheda.json`, riga 550. La pagina `42-acquista-v101`, catturata a quell'esatto URL, **non è una
cassa**: è la pagina d'errore di Squarespace. Il suo contenuto integrale, `copy-integrale.md`:
«Non è stato possibile trovare la pagina che stai cercando. Questo può essere dovuto a:» `[y=106]`,
seguito da due cause elencate — «Un errore nell'URL inserito nel tuo browser…» `[y=323]` e «La
pagina che stai cercando è stata spostata o eliminata.» `[y=352]` — e un rimando alla home
(«cliccando qui» → `/`, `[y=401]`). Conferma indipendente nello `scheda.json`: `"headings": []`
(nessun titolo di pagina reale), `"canonical": null` (nessun URL canonico dichiarato — una pagina
viva ne ha sempre uno, come si vede su tutte le altre undici di questo lotto), `og_title` generico
«AP Formazione» invece del titolo specifico della pagina. Tre segnali indipendenti, non uno solo,
concordano: **questa pagina non esiste**.

Il prodotto Vendita101 **ha** una cassa funzionante e misurata in questo stesso lotto —
`35-vendita101-pre`, 400,00 €, stessa struttura dello stampo 1 — ma **nessuna pagina del sito
catturato la linka**. Il risultato pratico: chiunque arrivi sulla pagina di vendita di Vendita101 e
clicchi il bottone di acquisto principale **non trova un modulo di pagamento, trova un 404** — e la
cassa che avrebbe dovuto ricevere quel click resta raggiungibile solo da chi conosce già l'URL
esatto o arriva da un canale esterno non ancora catturato. Non è un typo di una lettera: `/acquista-v101`
e `/vendita101-pre` sono due slug completamente diversi, il che esclude un refuso di battitura e
suggerisce invece un **URL sostituito durante un refactor** (probabilmente il vecchio slug della
cassa, mai aggiornato sul bottone della pagina di vendita quando la cassa è stata ricostruita altrove
sotto un nome diverso). È il tipo di guasto che uno script di controllo link, eseguito una sola volta
prima di ogni pubblicazione, avrebbe intercettato in meno di un minuto — e che invece è rimasto in
produzione fino a questa cattura.

---

## Connessioni
- [[24-25-27-28-macchina-del-funnel]] — il primo esempio dello stampo 1 (`outFunnel`), qui esteso a cinque usi
- [[24-25-27-28-macchina-del-funnel-COPY]] — l'inventario testuale di riferimento per il metodo di conteggio
- [[ECOSISTEMA]] — la mappa dei gradini rivela almeno due ingressi (`/copy`, `/vendita`) e un link rotto da registrare
- [[33-PIANO-STUDIO-TOTALE-ANDREI-PASCU]] — `/pre-checkout-cm` e `/pre-checkout-cmb` sono uno stampo mai censito prima di questo documento
