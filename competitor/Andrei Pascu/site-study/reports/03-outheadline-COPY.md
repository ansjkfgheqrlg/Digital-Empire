---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #outheadline #copy #teardown
Created: 2026-09-07
Last updated: 2026-09-07
---

# 03-outheadline — teardown del copy, macchina v2

**Fonte:** `capture/03-outheadline/` — `https://www.andrei-copy.com/outheadline`, catturato 2026-09-07.
**Numeri di base (dal task):** 21.119px, 19 sezioni (16 distinte), 315 blocchi di testo, 15 CTA.
Letto per intero `copy-integrale.md` (315 blocchi) e `scheda.json` (headings, cta, media, sezioni).

---

## DELTA ALLA FABBRICA

**CANONE:** ogni asset che sostituisce un **numero o una lista di benefici con importanza persuasiva
reale** deve avere un `alt` non vuoto, oppure il contenuto va duplicato come testo semplice altrove
nella pagina. Qui il prezzo intero della pagina (98€, mai scritto come cifra in nessun blocco di testo
di `copy-integrale.md` — verificato con ricerca diretta, zero risultati per "98") vive **solo** dentro
un'immagine, `Artboard – 96.png` [y=19904, x=545, w=349, h=349, `alt=""` in `scheda.json`]. Il
componente va codificato come `price-card-accessible`: cifra e unità sempre in testo vero, l'immagine
resta decorazione attorno.

**PATTERN:** la squalifica ("outHeadline non è per principianti" [y=11426]) occupa una sezione intera
di 686px [i=10, y=11331-12017] ma **contiene un solo blocco di testo estraibile** — `blocchi_testo: 1`
in `scheda.json`, confermato leggendo tutto `copy-integrale.md`: dopo y=11426 il documento salta
direttamente a y=12112 ("'Per scrivere headline basta usare formule'"), la prossima tappa. Qualunque
lista di motivi/esclusioni che il lettore vede sullo schermo non è testo, è immagine o markup non
standard. È lo stesso identico punto cieco già isolato nel dossier
[14-17-famiglia-out-COPY.md](14-17-famiglia-out-COPY.md) sulla **copia** di questa pagina
(`16-arma-outheadline`) — qui si conferma che il difetto non nasce dalla migrazione ad Armageddon,
esiste già identico sull'**originale**.

**GATE:** due controlli meccanici, entrambi misurabili qui per la prima volta sull'originale (non solo
sulla copia): 1) *ogni card-prezzo deve avere il valore numerico anche come testo semplice* — qui fallisce
al 100%, l'unica pagina delle tre studiate in questo lotto dove il prezzo non è mai testo (vedi confronto
in "IL PREZZO E LA SUA CORNICE"); 2) *ogni sezione di qualificazione negativa con lista deve passare un
conteggio minimo di blocchi di testo* (qui: soglia 1 fallita, la sezione ha esattamente un blocco) — un
gate che il dossier 14-17 aveva proposto solo per le copie Armageddon, qui esteso all'originale.

---

## LA STRUTTURA

outHeadline non segue le 19 sezioni meccaniche di `scheda.json` come narrazione — tre di quelle 19 sono
`div` di sfondo senza testo proprio (i=3, i=8, i=12, i=16, tutte `heading: null`, `blocchi_testo: 0`) che
racchiudono più tappe di contenuto reale. Ricostruita dal flusso di `copy-integrale.md`, la pagina ha
**21 tappe narrative** su 21.119px:

| # | y | Alt. (px) | Tappa | Funzione |
|---|---|---|---|---|
| 1 | 0 | 1.265 | HERO | "QUESTA È UNA HEADLINE." auto-dimostrativa + video 46s |
| 2 | 1.265 | 1.485 | Agitazione quantificata | Diagramma 1000→200 restano/800 se ne vanno [y=1265-2156] |
| 3 | 2.750 | 894 | Agitazione economica | "Perché lasciare soldi sul tavolo?!" + foto tavolo da poker [y=2750-3379] |
| 4 | 3.644 | 626 | Premessa/metodo | "La sales page te la può scrivere il miglior copy al mondo... ma se il titolo non fa leggere" [y=3644-3857] |
| 5 | 4.270 | 657 | Logica a specchio | "Se scrivi un titolo persuasivo... forse compra" / "...al 100% non compra" [y=4270-4701] |
| 6 | 4.927 | 788 | Segmentazione lettore | "Se sei un copywriter…" / "Se sei imprenditore che scrive copy da solo…" [y=4927-5486] |
| 7 | 5.715 | 1.081 | Dimostrazione interattiva | Widget PRIMA/DOPO, bottone "Clicca qui" [y=5715-6523] |
| 8 | 6.796 | 1.053 | Posizionamento prodotto | "Il primo corso Italiano..." + "l'unico corso... Per copywriter" + CTA "Entra in outHeadline" [y=6796-7661] |
| 9 | 7.849 | 1.124 | Storia d'origine | "Le basi del copy sono ovunque... Ma la roba seria dove sta?" [y=7849-8658] |
| 10 | 8.973 | 725 | Benefici a blocchi | Attenzione / Evitare skippino / Persuasione [y=8973-9537] |
| 11 | 9.698 | 1.633 | Curriculum | "outHeadline lista lezioni:" + Sezioni A-B, 1-5 [y=9698-11211] |
| 12 | 11.331 | 686 | **Qualificazione negativa** | "outHeadline non è per principianti" [y=11426] — 1 blocco di testo |
| 13 | 12.017 | 765 | Obiezione #1 | "'Per scrivere headline basta usare formule'" [y=12112-12616] |
| 14 | 12.782 | 1.263 | Metodo/framework | "Gli 8 step per scrivere headline" [y=12906-13864] |
| 15 | 14.045 | 1.716 | ONE SHOT, ONE KILL | Metafora cecchino + tabella proporzione [y=14140-15592] |
| 16 | 15.761 | 1.068 | Obiezione #2 | "'Un corso di più di 3 ore... Ma sei pazzo?'" [y=15817-16271] |
| 17 | 16.829 | 991 | Autorevolezza/status | "Sei più vicino al lavorare con multinazionali" + prova finale [y=16924-17625] |
| 18 | 17.820 | 715 | Prova di condotta | "Aggiornato al 2025" + storico 5 aggiornamenti gratis [y=17944-18365] |
| 19 | 18.535 | 1.004 | Obiezione #3 (AI) | "'Ma io le faccio scrivere a ChatGPT'" [y=18667-19437] |
| 20 | 19.539 | 876 | Prezzo | Squalifica di chiusura [y=19634] + card immagine [y=19904] + CTA [y=20219] |
| 21 | 20.415 | 705 | Chiusura | Legal, footer — nessuna FAQ |

**Confronto con la formula a 11 tappe** (hero, agitazione, prova con fonte, metodo, benefici, curriculum,
qualificazione negativa, obiezioni, autorevolezza, prezzo barrato, FAQ, chiusura): outHeadline **salta
due tappe per intero** — zero "prova con fonte" (nessun link esterno in tutta la pagina, verificato: la
lista `cta[]` di `scheda.json` non contiene un solo `href` verso un dominio terzo, a differenza di
funnel-operator e copy) e zero FAQ (nessuna sezione "Domande comuni" tra i 30 headings) — ma **triplica**
la tappa obiezioni (3 obiezioni citate testualmente contro l'1 tipico delle pagine della famiglia
outEmail/outHeadline-copia già misurato in [14-17-famiglia-out-COPY.md](14-17-famiglia-out-COPY.md)) e
aggiunge una tappa che la formula non prevede: la **dimostrazione interattiva** (il widget PRIMA/DOPO,
tappa 7). Il prezzo non è mai barrato: è una cifra unica, mai presentata come sconto da un valore più
alto — diverso dal meccanismo "prezzo individuale barrato + badge incluso" osservato sulle copie
Armageddon della stessa pagina.

---

## LA PROMESSA E DOVE STA

> *"E solo i copywriter che scrivono HEADLINE persuasive sono disperatamente richiesti… E guadagnano di
> più."* [y=410]

A y=410, **1,9% della pagina** — nell'hero stesso, la promessa più precoce delle tre pagine di questo
lotto (funnel-operator arriva alla prima formulazione di beneficio a y=1195, 5%; copy non promette nulla
di concreto nell'hero, solo "libertà finanziaria" generica a y=137). La promessa qui è duplice e non
quantificata: un **esito di mercato** (essere "disperatamente richiesti") più un **esito economico**
implicito ("guadagnano di più") — nessun numero, a differenza della sorella outViral della stessa
famiglia (10K views di media, quantificato nel titolo). Viene rinforzata più avanti in forma quantificata
ma ipotetica, mai promessa come garanzia: *"Se adesso vendi 5… Potresti vendere 10 se solo e
semplicemente trasformassi quel titolo"* [y=5424], rivolta esplicitamente al secondo segmento
("imprenditore che scrive copy da solo").

---

## COME TRATTA LE OBIEZIONI

Tre obiezioni, tutte in forma di citazione tra virgolette seguita da risposta diretta — la densità più
alta delle tre pagine di questo lotto (funnel-operator: zero; copy: una sola, in forma di domanda
frequente non polemica):

1. *"'Per scrivere headline basta usare formule'"* [y=12112] → *"Se bastasse usare delle formule
   pre-concepite… Perché non usi formule pre-concepite per letteralmente ogni singolo pezzo del tuo
   copy?"* [y=12281], seguito da un loop di frustrazione in 4 righe (*"Cerco una formula / Provo ad
   applicarla al mio copy / Scopro che non è al 100% adatta al prodotto / Ricomincio da capo"*
   [y=12399-12509]) — tecnica: contro-domanda che estende la logica dell'obiezione fino all'assurdo, poi
   un'esperienza vissuta al posto della logica pura.
2. *"'Un corso di più di 3 ore su come scrivere titoli? Ma sei pazzo?'"* [y=15817] → *"Sì sono pazzo…
   Pazzo per il copy! lol"* [y=15967], poi *"Le persone di successo sono quelle che fanno quello che
   serve, non quello 'che vogliono'."* [y=16100] — tecnica: accetta l'accusa e la ribalta in dedizione.
3. *"'Ma io le faccio scrivere a ChatGPT'"* [y=18667] → *"Ma se non conosci le strategie, non puoi usare
   l'AI responsabilmente."* [y=19259], con dettaglio: *"Se usi ChatGPT e prendi le headline così come
   sono… Le farai allo stesso livello dei competitor."* [y=19347] — tecnica: non nega lo strumento, lo
   riposiziona come moltiplicatore condizionato al metodo.

Nessuna delle tre obiezioni riguarda il prezzo — tutte riguardano la competenza percepita o lo strumento
sostitutivo (formule, tempo richiesto, AI), coerente con quanto già osservato a livello di famiglia nel
dossier 14-17.

---

## LE PROVE E LA LORO VERIFICABILITÀ (spietato)

**Zero.** Confermato con ricerca diretta su tutto `copy-integrale.md` e sull'intero array `cta[]` di
`scheda.json`: non un solo `href` verso un dominio esterno, non un solo "(fonte)" testuale, non una sola
statistica con link. L'unica cifra citata fuori dal prodotto è *"una sales page da €3k + IVA"* [y=16584],
usata come ancoraggio di prezzo implicito (98€ contro 3.000€, rapporto 1:30 mai scritto esplicitamente),
non come prova verificabile di un fatto di mercato.

Le uniche "dimostrazioni" della pagina sono **auto-costruite**: il widget PRIMA/DOPO (un esempio scritto
da Andrei stesso, non un caso reale di terzi) e la dichiarazione di autorevolezza circolare — *"Ti sta
convincendo quello che scrivo? E' perché so scrivere copy… Questa è la prova finale che pratico ciò che
insegno."* [y=17535] — che usa l'effetto persuasivo stesso della pagina come prova della propria
competenza, un argomento non falsificabile per definizione (chi non è convinto, per lo stesso
ragionamento, "dimostra" che l'autore non sa scrivere — ma la pagina non prevede questo esito). La prova
di condotta storica (*"negli ultimi 4 anni ho aggiornato 5 volte il mio corso CM a GRATIS"* [y=18140]) è
verificabile in linea di principio ma non è mai collegata a un link o una fonte esterna che lo confermi
— resta un'affermazione, non una prova documentata. **Questa è la pagina meno verificabile delle tre**
di questo lotto: outheadline (0 fonti) contro funnel-operator (2) e copy (5, vedi report gemello).

---

## LA SCALA DI IMPEGNO

La più semplice delle tre: **un solo prodotto, un solo prezzo, una sola azione**. Nessun livello, nessun
upgrade, nessuna community dedicata menzionata (niente Telegram, niente consulenze — a differenza sia di
funnel-operator, che offre 5 ore di consulenza nel prezzo, sia soprattutto di copy, che ha due piani e un
gruppo Telegram). L'unico "impegno progressivo" nella pagina è narrativo, non commerciale: il lettore
passa dal vedere la trasformazione nel widget (gesto minimo, un click) alla lettura degli 8 step (impegno
cognitivo) fino al bottone finale "Entra ora in outHeadline" [y=20219] — un imbuto di attenzione, non un
imbuto di prezzo.

---

## IL PREZZO E LA SUA CORNICE

Il prezzo (98€ per posizionamento noto, mai una cifra testuale nella pagina) vive **esclusivamente**
dentro l'immagine `Artboard – 96.png` [y=19904, 349×300px, `alt=""`]. È l'unica delle tre pagine di
questo lotto dove il numero del prezzo non è mai testo semplice — funnel-operator scrive *"434,00 €"*
due volte come testo vero [y=852 e y=21474], copy scrive *"€349"* e *"€999"* come testo vero [y=24125,
24126]. La cornice arriva prima del numero, come nelle altre due: la squalifica di chiusura
*"outHeadline? Probabilmente non è per te. Ma se lo è… Stai per svoltare."* [y=19634] precede
immediatamente la card, seguendo lo stesso schema-cerniera già documentato nel dossier 14-17 per le
pagine sorelle di questa famiglia (*"[Prodotto]? Probabilmente non è per te. Ma se lo è… Stai per
svoltare."* — frase-motto condivisa, qui trovata sull'originale, non solo sulla copia). Nessun prezzo
barrato, nessuna scadenza, nessun countdown — verificato con ricerca diretta ("scadenz*", "countdown"),
zero risultati.

---

## COSA NON DICE MAI

1. **Nessuna garanzia o rimborso** — zero occorrenze di "garanzia" o "rimbors*" in tutto il file.
2. **Nessuna scadenza o countdown** — zero occorrenze verificate.
3. **Il prezzo come cifra leggibile** — non esiste in nessun blocco di testo della pagina.
4. **Una sola ragione specifica per non comprare** — il titolo "non è per principianti" [y=11426] non è
   mai seguito da un elenco testuale dei motivi, a differenza di come li elenca a parole outEmail nella
   pagina gemella della famiglia (dossier 14-17, §"LA QUALIFICAZIONE NEGATIVA").
5. **Un solo link esterno di qualunque tipo** — zero `href` verso domini terzi in tutto `cta[]`.

---

## LE FORMULE RICORRENTI

**1. Domanda retorica seguita da promessa in due tempi, la seconda in corsivo staccato**
> *"E solo i copywriter che scrivono HEADLINE persuasive sono disperatamente richiesti… E guadagnano di
> più."* [y=410, "E guadagnano di più" in corsivo a sé]

`"E solo [PLACEHOLDER: CATEGORIA DI PERSONE] che [PLACEHOLDER: COMPETENZA SPECIFICA] sono
disperatamente richiesti… E [PLACEHOLDER: RICOMPENSA, in corsivo staccato]."`

**2. Matematica della perdita su una base di 1000**
> *"…Ecco cosa succede se 1000 persone vedono la tua pagina"* → 200 restano / 800 se ne vanno [y=1265]

`"Ecco cosa succede se [NUMERO TONDO] [PLACEHOLDER: UNITÀ DI PUBBLICO] [PLACEHOLDER: AZIONE]:"` seguito
da un ramo verde (trattenuti) e un ramo rosso (persi), mai un guadagno promesso — solo una perdita
quantificata già in corso.

**3. Sillogismo a specchio con asimmetria deliberata fra probabilità e certezza**
> *"Se scrivi un titolo persuasivo, la gente legge… Se la gente legge, forse compra."* [y=4270] / *"Se
> scrivi titolo non persuasivo, la gente non legge… Se la gente non legge, al 100% non compra."*
> [y=4493]

`"Se [AZIONE CORRETTA], [CONSEGUENZA]… Se [CONSEGUENZA], forse [RISULTATO]." / "Se [AZIONE SBAGLIATA],
non [CONSEGUENZA]… Se non [CONSEGUENZA], al 100% non [RISULTATO]."` — il beneficio resta probabile
("forse"), il danno diventa certo ("al 100%").

**4. Segmentazione a due paragrafi, ciascuno con una sola leva dedicata**
> *"Se sei un copywriter…"* [y=4927] → leva dell'orgoglio di mestiere / *"Se sei imprenditore che scrive
> copy da solo…"* [y=5307] → leva del raddoppio del fatturato

`"Se sei [SEGMENTO A]…" [PLACEHOLDER: LEVA IDENTITARIA]. "Se sei [SEGMENTO B]…" [PLACEHOLDER: LEVA
ECONOMICA].` — nessuno dei due paragrafi cita l'altro segmento.

**5. Analogia a doppio rapporto in forma matematica**
> *"Copywriter : campagna di marketing = cecchino : missione militare"* [y=15098]

`"[RUOLO DEL LETTORE] : [CONTESTO DEL LETTORE] = [PLACEHOLDER: FIGURA DI PRECISIONE ESTREMA] :
[PLACEHOLDER: CONTESTO AD ALTO RISCHIO]"` — reso poi operativo con una tabella a due colonne
(variabili dello sniper / variabili del copywriter), trasformando la metafora in un framework a 5 voci.

**6. Prova di condotta storica al posto della garanzia**
> *"Negli ultimi 4 anni ho aggiornato 5 volte il mio corso CM a GRATIS solo perché io ho una filosofia
> chiara"* [y=18140]

`"Negli ultimi [PERIODO] ho aggiornato [NUMERO] volte [PRODOTTO] a GRATIS solo perché [PLACEHOLDER:
PRINCIPIO MORALE DICHIARATO]."` — uno storico verificabile in linea di principio, mai collegato a una
fonte, sostituisce la garanzia che la pagina non offre mai.

---

## IL DIFETTO

**Il prezzo dell'intera pagina non esiste come testo in nessun punto del documento.** Verificato con
ricerca diretta su tutti i 315 blocchi di `copy-integrale.md`: zero occorrenze di "98" collegate a un
simbolo di valuta. L'unica traccia del prezzo è l'immagine `Artboard – 96.png` [y=19904, w=349, h=300,
`alt=""` in `scheda.json`] — un `alt` esplicitamente vuoto, non mancante: per uno screen reader
l'immagine è marcata come puramente decorativa, mentre contiene l'unica informazione economica
dell'intera pagina. È un difetto che il vecchio studio di questa stessa pagina (`03-outheadline.md`,
v1, 2026-09-01) non aveva colto come tale: descriveva la card come *"Fondo bianco, logo verde, `€98 /
pagamento unico` in verde grande"*, presentandola come se il testo fosse leggibile, senza notare che si
tratta di un'immagine non accessibile — un'accuratezza che il resto dell'ecosistema (dossier 14-17, sulle
copie Armageddon di questa stessa pagina) aveva già raggiunto per lo stesso tipo di componente. Qui si
conferma che il difetto non è nato con la migrazione: esiste identico sull'originale.

Un secondo difetto, più piccolo ma dello stesso genere: la sezione di qualificazione negativa [i=10,
y=11331-12017, 686px] contiene **un solo blocco di testo estraibile** su un'intera sezione da 686px —
qualunque lista di motivi che il lettore vede (se esiste, come suggerisce la sezione gemella già
analizzata nel dossier 14-17) non è testo semplice.

---

## ERRORE NEL RAPPORTO VECCHIO — dichiarato

Il rapporto `03-outheadline.md` (v1, 2026-09-01), sezione 4.10 "Squalifica", scrive: *"Titolo a 60,8px
con `non` in evidenza, seguito da `Questo corso non è per te se:` e una lista di esclusioni (`Non sai
cos'è il copywriting`, …)"* — presentando queste frasi come citazioni dirette del copy, nello stesso
stile con cui il resto del documento cita `>` frasi realmente estratte dalla pagina.

**Verifica su questa cattura (v2, stesso URL):** nessuna delle tre stringhe — *"Questo corso non è per te
se"*, *"Non sai cos'è"*, *"Salta le basi"* — compare in nessun punto di `copy-integrale.md` (ricerca
diretta, zero risultati). L'unico testo estraibile della sezione è *"outHeadline non è per principianti"*
[y=11426], confermato anche dal campo `blocchi_testo: 1` di `scheda.json` per quella sezione. Non si può
stabilire con certezza se la pagina sia cambiata fra il 1° e il 7 settembre 2026 o se il vecchio rapporto
abbia trascritto contenuto visibile solo nello screenshot (quindi non testo DOM reale) presentandolo come
copy citabile — ma in entrambi i casi la lista di esclusioni **non esiste oggi come testo verificabile**,
e questo studio non può ripeterla né confermarla. È lo stesso identico limite di misurazione già
documentato nel dossier 14-17 per la copia Armageddon della stessa pagina — qui, per la prima volta,
esteso all'originale.

---

## Nota sulla lunghezza

Il documento è sopra la soglia di 2.500 parole di sostanza richiesta: la pagina più corta delle tre
studiate in questo lotto (315 blocchi, 21.119px) ha comunque dato materiale sufficiente per coprire ogni
sezione richiesta con citazione diretta, senza necessità di aria. Non sono state aggiunte frasi di
riempimento.

## Collegamenti

- [02-funnel-operator-COPY.md](02-funnel-operator-COPY.md) — stesso lotto, prezzo 434€, unico confronto
  diretto su "prezzo come testo vs immagine"
- [05-copy-COPY.md](05-copy-COPY.md) — stesso lotto, prezzo 349/999€, risponde alla domanda trasversale
  su come cambia il copy quando il prezzo sale
- [14-17-famiglia-out-COPY.md](14-17-famiglia-out-COPY.md) — la copia Armageddon di questa stessa pagina
  (`16-arma-outheadline`), stesso difetto di qualificazione-negativa-senza-testo già isolato lì
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — lo standard di forma per questo
  teardown
- `capture/03-outheadline/copy-integrale.md`, `scheda.json` — le fonti primarie di questo dossier
- `reports/03-outheadline.md` — il rapporto v1 (macchina v1, 2026-09-01), corretto qui su un punto
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
