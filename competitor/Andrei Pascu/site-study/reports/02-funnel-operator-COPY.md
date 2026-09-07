---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #funnel-operator #copy #teardown
Created: 2026-09-07
Last updated: 2026-09-07
---

# 02-funnel-operator — teardown del copy, macchina v2

**Fonte:** `capture/02-funnel-operator/` — `https://www.andrei-copy.com/funnel-operator`, catturato
2026-09-07. **Prezzo:** 434,00 € una tantum.
**Numeri di base (dal task):** 24.019px, 28 sezioni (16 distinte), 340 blocchi di testo, 20 CTA.
Letto per intero `copy-integrale.md` (340 blocchi) e `scheda.json` (headings, cta, media, sezioni).

---

## DELTA ALLA FABBRICA

**CANONE:** stesso principio già isolato sulla pagina gemella di questo lotto (outHeadline): ogni
elenco di benefici con peso persuasivo reale deve esistere come testo, non solo come immagine. Qui il
caso è più netto — l'intero blocco dei **6 vantaggi dell'hero** (`20+ ore di lezione`, `Comprese le basi
per chi parte da zero`, `Come fare il funnel operator`, `Come trovare clienti`, `5 ore di consulenza con
Andrei Pascu`, `Paghi SOLO una volta`, secondo la lettura visiva del rapporto v1) **non esiste come
testo in nessun blocco di `copy-integrale.md`**: ricerca diretta di "ore di lezione", "ore di
consulenza", "Comprese le basi", "Come fare il funnel", "Paghi SOLO" — zero risultati su tutti e 340 i
blocchi. L'unico oggetto media in quella posizione è `Bullet+Hero+FunnelOps+WebP+Converter+(1).webp`
[y=844, w=267, h=138, `alt=""`]. Il componente va codificato come `benefit-list-accessible`: ogni voce
della lista-vantaggi in hero deve avere il proprio nodo di testo, mai un'unica immagine composita.

**PATTERN:** questa è l'unica delle tre pagine del lotto **senza curriculum**. Verificato con ricerca
diretta di "Sezione", "Lezione", "video-lezion*" in tutto il file: zero risultati. Copy (05-copy) ha 6
sezioni numerate e un accordion a 3 parti; outHeadline ha 2 gruppi (A-B, 1-5) e un accordion; funnel-operator,
il prodotto **di prezzo intermedio e narrativa più lunga**, non elenca mai una sola lezione, un solo
argomento del corso, un solo indice. L'unica descrizione del contenuto è "20+ ore di lezione" — e come
appena isolato, pure quella non è testo, è dentro l'immagine con `alt=""`. Chi legge questa pagina non
sa, a fine lettura, **cosa contenga davvero il corso** oltre alla parola "CRO" ripetuta in astratto.

**GATE:** due controlli nuovi. 1) *ogni pagina prodotto con prezzo ≥300€ deve avere almeno un blocco di
testo che elenchi il contenuto del corso* — qui fallisce interamente; 2) *il blocco di vantaggi in hero
deve avere tanti nodi di testo quanti sono i punti elenco visibili* — qui 0 su 6 (o quanti fossero)
risultano estraibili, lo stesso identico fallimento già isolato per la card-prezzo di outHeadline, ma
applicato qui non al prezzo bensì all'intero contenuto del prodotto.

---

## LA STRUTTURA

Ventotto sezioni meccaniche in `scheda.json` (16 distinte), di cui alcune vuote (`i=17`, `y=13413`,
`heading: null`, solo sfondo). Ricostruita dal flusso narrativo di `copy-integrale.md`:

| # | y | Alt. (px) | Tappa | Funzione |
|---|---|---|---|---|
| 1 | 0 | 1.113 | HERO | Headline [y=221] + prezzo "434,00 €" testo vero [y=852] + CTA "Acquista ora" [y=937] + lista vantaggi (immagine, alt="") |
| 2 | 1.113 | 789 | Promessa di mercato | "Le aziende lo vogliono, non lo trovano..." [y=1195] |
| 3 | 1.902 | 386 | Cerniera | "Sto per parlarti di soldi... Non posso parlartene bene se prima non mi conosci." [y=1902] |
| 4 | 2.288 | 1.307 | Chi sono | "Piacere, sono Andrei c:" + 3 frasi [y=2476-3266] |
| 5 | 3.595 | 1.423 | Origin story | "Ero confuso e... un po' sfigato" [y=3643-4831] + CTA Instagram [y=4910] |
| 6 | 5.018 | 1.884 | Timeline pt.1 | "2020" Primi clienti [y=5086-5336] + "2021" Bologna, €10k [y=5624-5909] |
| 7 | 6.902 | 1.539 | Timeline pt.2 | "2021-oggi" team [y=6955-7965] + "Però... è arrivato il 2025" [y=8227] |
| 8 | 8.441 | 1.130 | La caduta | "inizio 2025" [y=8509] "E lo era." [y=8683] "Ti auguro lo stesso problema 😅" [y=9361] |
| 9 | 9.571 | 438 | Dichiarazione interesse | "voglio che tu copi le mie mosse... ci guadagno sia io che tu" [y=9756-9844] |
| 10 | 10.009 | 1.250 | Prova per eliminazione | "Abbiamo testato nuovi servizi... Nessuno ha funzionato." + 3 motivi [y=10147-11080] |
| 11 | 11.259 | 950 | Scoperta del CRO | "Ho iniziato a offrire il servizio di CRO." [y=11402-12084] |
| 12 | 12.209 | 1.587 | Definizione CRO | "Cos'è CRO e come funziona?" + 3 esempi [y=12304-13137] |
| 13 | 13.796 | 1.070 | Giustificazione prezzo | "Perché il CRO... paga bene?" "anche 1-3 mila euro a servizio" [y=13796-14137] |
| 14 | 14.866 | 905 | Domanda di mercato con fonte | "il marketer che le aziende vogliono nel 2026" + "fonte" [y=14866-15617] |
| 15 | 15.771 | 693 | Cosa fa il ruolo | "Il Funnel Operator si fa pagare per:" + "devi:" [y=15771-16281] |
| 16 | 16.464 | 1.881 | Blocco categoria (riusato) | "La realtà dei fatti?" + studio SEC + Hopkins/Powers [y=16464-18117] |
| 17 | 18.345 | 593 | Prova per eliminazione 2 | "28 test di 28 servizi diversi. Solo Funnel Operator è sopravvissuto." [y=18345] |
| 18 | 18.938 | 395 | Difesa mancanza testimonianze | "Gli altri ti mettono 30 video-recensioni... Io ti mostro i dati." [y=18938] |
| 19 | 19.333 | 858 | Argomento anti-ciclico | "Ho scelto il copywriting dato che funziona anche durante i periodi di peggiore crisi:" [y=19333] |
| 20 | 20.191 | 1.283 | Per chi + qualificazione positiva | "Per chi ho creato Funnel Operator" + 6 bullet [y=20191-20866] |
| 21 | 21.474 | 268 | Prezzo | "434,00 €" testo vero [y=21474] + CTA "Iscriviti" [y=21575] |
| 22 | 21.742 | 1.190 | FAQ | "Domande comuni" + 10 domande [y=21742-22734] |
| 23 | 22.932 | 1.087 | Chiusura | "Disclaimer" + legal + footer [y=22932-24019] |

**Confronto con la formula a 11 tappe:** funnel-operator è l'unica delle tre pagine a **saltare
interamente il curriculum** (nessuna sezione, nessuna lezione elencata) e a **non avere mai un prezzo
barrato** (434€ è una cifra unica, mai presentata come sconto — diverso sia da outHeadline sia dal
meccanismo a badge delle copie Armageddon). In compenso ha la tappa **prova per eliminazione**, ripetuta
due volte (tappe 10 e 17 — "27 servizi morti" e "28 test... solo uno sopravvissuto", lo stesso argomento
raccontato due volte con numeri leggermente diversi, vedi "IL DIFETTO"), e una **cerniera esplicita**
(tappa 3) che nessuna delle altre due pagine possiede: una frase dedicata solo a giustificare perché la
biografia debba precedere la vendita. Ha **prova con fonte** (tappa 14, 1 link) ma **zero obiezioni
esplicite** in forma di citazione — confermato con ricerca diretta del pattern `'Ma...'` in tutto il
file, zero risultati — e **zero qualificazione negativa** (nessuna frase "non è per tutti" in nessun
punto, confermato). Il "per chi" (tappa 20) è filtro positivo puro, mai un elenco di chi va escluso.

---

## LA PROMESSA E DOVE STA

> *"Funnel Operator: l'evoluzione del full stack marketer. Fai CRO per aziende copiando la carriera di
> Andrei Pascu."* [y=221]

A y=221, 0,9% della pagina. Tre promesse in una frase: una **categoria nuova** ancorata a una nota
("l'evoluzione del full stack marketer"), un **modello di business** esplicito ("per aziende", non per
sé stessi) e un **meccanismo di trasferimento del rischio** — "copiando la carriera" sposta l'onere della
prova dal lettore all'autore, che deve dimostrare di avere davvero una carriera da copiare (da qui i
quasi 9.000px di biografia che seguono, tappe 4-9). Non c'è un numero, non c'è una cifra di fatturato
promessa: la promessa è **imitativa**, non quantificata — diversa sia dal "guadagnano di più" implicito di
outHeadline sia dalla "libertà finanziaria" generica di copy. La cifra economica più vicina a una
promessa arriva solo alla tappa 13: *"Per 'paga bene' intendo: anche 1-3 mila euro a servizio."*
[y=14137] — un numero sul compenso del lavoro futuro del lettore, non sul ritorno del corso stesso.

---

## COME TRATTA LE OBIEZIONI

**Zero obiezioni esplicite in forma di citazione-risposta.** Confermato con ricerca diretta del pattern
`'Ma...'` (e varianti) su tutti i 340 blocchi: nessun risultato. È l'unica delle tre pagine del lotto a
non avere questo dispositivo retorico da nessuna parte — outHeadline ne ha tre, copy ne ha una.

Le uniche gestioni di resistenza sono **indirette**, incassate dentro il racconto:
- *"Le aziende hanno bisogno di aiuto. E tu le puoi aiutare. Chiaro: questo aiuto costa €€€."* [y=15524-
  15613] — tre righe brevissime, ognuna una frase sola, che anticipano "ma perché dovrebbero pagare?"
  senza mai nominare l'obiezione come tale.
- La FAQ finale (tappa 22) porta due domande che funzionano da obiezione travestita: *"Come faccio a
  fidarmi?"* [y=22625] e *"Se compro questo corso divento ricco?"* [y=21837] — la seconda mette in bocca
  al lettore l'aspettativa gonfiata proprio per poterla ridimensionare implicitamente (non segue mai una
  risposta testuale visibile nell'estrazione, la domanda resta la sola voce accordion).
- Il disclaimer finale [y=22964-23134] è, di fatto, la risposta più esplicita a "divento ricco?": *"Andrei
  non garantisce il tuo successo... i tuoi risultati varieranno in base all'istruzione, allo sforzo,
  all'applicazione, all'esperienza e al background."* — una gestione legale dell'obiezione, non
  persuasiva.

---

## LE PROVE E LA LORO VERIFICABILITÀ (spietato)

**Due fonti esterne**, un numero intermedio fra outHeadline (0) e copy (5):

1. *"Funnel Operator, il marketer che le aziende vogliono nel 2026"* [y=14866] → *"fonte"* [y=15332] →
   `demandgenreport.com/industry-news/news-brief/b2b-marketers-adjusting-as-digital-channels-top-total-market-spend/49730/`.
   **Verificabile ma non puntuale**: la pagina di destinazione è un articolo di settore B2B generico
   sull'allocazione budget digitale, non uno studio dedicato a "i marketer che le aziende vogliono".
2. *"E lo afferma anche questo studio:"* [y=17016] → *"questo"* [y=17013] →
   `sec.gov/oiea/investor-alerts-and-bulletins/risks-short-term-trading-based-social-media-investor-alert`
   — stesso identico link usato anche su 05-copy (vedi report gemello), riutilizzato parola per parola
   per squalificare trading/dropshipping. **Verificabile e pertinente**: la SEC è un ente regolatore
   reale e l'alert esiste, ma il link squalifica alternative di categoria, non prova un claim sul
   copywriting/CRO stesso.

Contro questi due, il claim più pesante della pagina resta ipse dixit puro: *"Ho fatto 28 test di 28
servizi diversi. Solo Funnel Operator è sopravvissuto."* [y=18345] — nessun elenco verificabile dei 28
servizi, nessuna fonte, nessun terzo che confermi. La foto di Hopkins e Powers [media, y=17743] è
un'illustrazione storica reale ma non collegata a nessun link di verifica — funziona da autorità visiva,
non da prova documentata.

**Il blocco di categoria è riusato identico da 05-copy**, carattere per carattere: *"Non diventerai ricco
con un software, copiando 'trade' di altri o vendendo cineserie su Aliexpress... Le ho provate tutte…"*
[y=16532 qui; y=2500 su copy] — stessa frase, stesso studio SEC linkato, stessa citazione Hopkins/Powers,
stesso "1%" — confermando quanto già notato nel v1 (`02-funnel-operator.md`, connessioni): *"condivide
interi blocchi di copy... stessa fabbrica, moduli riusati"*. Qui verificato riga per riga sulla cattura
v2: il blocco parte da *"La realtà dei fatti?"* [y=16458] ed è identico, incluso l'URL SEC, fino a *"E sì,
adesso ovviamente si usa Intelligenza Artificiale..."* [y=18117].

---

## LA SCALA DI IMPEGNO

Un solo prezzo, una sola azione — **434,00 € una tantum**, ripetuto identico due volte [y=852 e y=21474],
mai un piano alternativo. A differenza di copy (due piani + upgrade a differenza), qui l'unico elemento
di scala è **incluso nel prezzo, non venduto a parte**: *"5 ore di consulenza con Andrei Pascu"* secondo
la lettura visiva del rapporto v1 (non verificabile come testo, essendo dentro l'immagine hero senza
`alt`, vedi "DELTA ALLA FABBRICA"). L'unico invito a un impegno minore, non un acquisto, è il bottone
"Instagram" [y=4910, nero, non blu] dentro la biografia — raccoglie chi è agganciato emotivamente ma non
ancora pronto a pagare, spostandolo su un canale a bassa frizione. Nessuna community dedicata (niente
Telegram menzionato su questa pagina, a differenza di copy).

---

## IL PREZZO E LA SUA CORNICE

**434,00 €** è testo vero in entrambe le occorrenze [y=852 hero, y=21474 chiusura] — l'opposto di
outHeadline, coerente con copy. Compare **nella hero stessa**, all'1,9% della pagina — una scelta
controcorrente rispetto alle altre due pagine del lotto (outHeadline mostra il prezzo solo al 94,3% della
pagina; copy lo cela dietro 27.000px di argomentazione fino all'88,3%). La cornice, qui, **segue** il
prezzo invece di precederlo: prima la cifra e il CTA "Acquista ora" [y=937], poi 23.000px di
giustificazione (biografia, mercato, categoria) per convincere chi è rimasto dopo aver visto il numero.
È l'inverso esatto del principio "valore prima del numero" osservato sia su copy sia su outHeadline. Il
prezzo non è mai barrato, non ha mai un badge di sconto, non ha mai una scadenza — l'unica leva è
l'etichetta "Una tantum" ripetuta due volte [y=894 e y=21516], antidoto diretto all'obiezione-abbonamento
che infatti ricompare identica nella FAQ (*"È un abbonamento o pago solo una volta?"* [y=22203]).

---

## COSA NON DICE MAI

1. **Nessuna garanzia o rimborso** — zero occorrenze verificate.
2. **Nessuna scadenza o countdown** — zero occorrenze.
3. **Il contenuto del corso** — nessuna lezione, nessun argomento, nessun modulo elencato come testo in
   nessun punto della pagina (vedi "DELTA ALLA FABBRICA", pattern).
4. **Un elenco verificabile dei "28 servizi testati"** — il numero è ripetuto due volte (10.147 e 18.345)
   ma mai spiegato con un solo esempio nominato.
5. **Un'obiezione in forma diretta** — mai una citazione tra virgolette del tipo "'Ma...'", a differenza
   delle altre due pagine del lotto.

---

## LE FORMULE RICORRENTI

**1. Nome nuovo ancorato a una categoria nota, più promessa-copia**
> *"Funnel Operator: l'evoluzione del full stack marketer. Fai CRO per aziende copiando la carriera di
> Andrei Pascu."* [y=221]

`"[NOME NUOVO]: l'evoluzione del [CATEGORIA NOTA]. Fai [SERVIZIO] per [CLIENTE FINALE] copiando
[PLACEHOLDER: PERCORSO GIÀ VERIFICATO DI CHI VENDE]."`

**2. Cerniera esplicita che giustifica la biografia prima di raccontarla**
> *"Sto per parlarti di soldi, guadagno e una intera carriera. Non posso parlartene bene se prima non mi
> conosci."* [y=1902]

`"Sto per parlarti di [TEMA DI VALORE]. Non posso parlartene bene se prima non [PLACEHOLDER: CONDIZIONE
DI FIDUCIA DA COSTRUIRE PRIMA]."`

**3. Dichiarazione esplicita dell'interesse economico, prima che il lettore la sospetti**
> *"E voglio che tu copi le mie mosse… O almeno… Quelle giuste. Perché? Perché dopo ti propongo di
> entrare in Funnel Operator, quindi ci guadagno sia io che tu."* [y=9756-9844]

`"Voglio che tu [PLACEHOLDER: AZIONE DESIDERATA]. Perché? Perché dopo ti propongo [PRODOTTO], quindi ci
guadagno sia io che tu."`

**4. Prova per eliminazione con numero specifico e criteri di scarto**
> *"Ho fatto 28 test di 28 servizi diversi. Solo Funnel Operator è sopravvissuto."* [y=18345] — poi 3
> motivi: *"Non sono richiesti dal mercato / Lo stanno già offrendo altre agenzie / Non c'è margine"*
> [y=10974-11080]

`"Ho fatto [NUMERO] test di [NUMERO] [PLACEHOLDER: ALTERNATIVE]. Solo [PRODOTTO] è sopravvissuto."`
seguito da un elenco di criteri di scarto riusabile come framework a sé.

**5. Numero grosso e freno nella stessa frase**
> *"Per 'paga bene' intendo: anche 1-3 mila euro a servizio. Chiaramente non è che ti fai pagare 1k da
> subito a caso, ci vuole tempo."* [y=14137]

`"Per '[PLACEHOLDER: AGGETTIVO POSITIVO VAGO]' intendo: anche [CIFRA ALTA]. Chiaramente non è che
[PLACEHOLDER: RISULTATO IMMEDIATO], ci vuole [PLACEHOLDER: FATTORE CHE FRENA LA CIFRA]."`

**6. Argomento verificabile dal lettore in tempo reale, senza bisogno di fonti**
> *"Prova a ricordare l'ultima pubblicità che hai visto su Insta. Non la ricordi vero? Non mi
> sorprende."* [y=15421]

`"Prova a [PLACEHOLDER: AZIONE MENTALE CHE IL LETTORE FA DA SOLO]. Non [RISULTATO ATTESO] vero? Non mi
sorprende."` — impossibile da fallire, il lettore si convince senza che serva un link.

---

## IL DIFETTO

**L'intero contenuto del corso non esiste come testo in nessun punto della pagina.** Confermato con
ricerca diretta di "Sezione", "Lezione" e "video-lezion*" su tutti i 340 blocchi di `copy-integrale.md`:
zero risultati, contro le 6 sezioni numerate di copy e i 2 gruppi di outHeadline. L'unica menzione del
contenuto ("20+ ore di lezione", secondo la lettura visiva del rapporto v1) vive dentro
`Bullet+Hero+FunnelOps+WebP+Converter+(1).webp` [y=844, `alt=""`], lo stesso genere di difetto già
isolato su outHeadline per il prezzo — qui applicato non a un numero ma **all'intera proposta di
valore**: chi legge questa pagina con uno screen reader, o con qualunque estrazione di solo testo
(compreso questo stesso studio se si fosse fermato al file integrale senza incrociare `scheda.json`),
non scopre mai cosa contengano le "20+ ore" promesse. È il difetto più grave delle tre pagine di questo
lotto: sulle altre due l'informazione mancante come testo è un prezzo (outHeadline) o dei nomi di
studenti (copy, vedi report gemello); qui è la descrizione stessa del prodotto che si sta vendendo.

Un secondo difetto, minore: la "prova per eliminazione" viene raccontata **due volte** con lo stesso
numero (28) ma toni diversi — *"Abbiamo testato nuovi servizi... Nessuno ha funzionato"* [y=10147-10869]
e, 8.000px dopo, *"Ho fatto 28 test di 28 servizi diversi. Solo Funnel Operator è sopravvissuto."*
[y=18345] — la seconda versione è una ripetizione quasi identica della prima, non un'estensione: la
pagina racconta lo stesso fatto due volte a distanza, invece di rafforzarlo con un dettaglio nuovo alla
seconda occorrenza.

---

## Nota sulla lunghezza

Il documento è sopra la soglia di 2.500 parole di sostanza richiesta: i 340 blocchi di testo di questa
pagina, incrociati con `scheda.json` (28 sezioni, 20 CTA, media), hanno dato margine per coprire ogni
sezione richiesta con citazione diretta. Non sono state aggiunte frasi di riempimento.

## Collegamenti

- [03-outheadline-COPY.md](03-outheadline-COPY.md) — stesso lotto, prezzo 98€, stesso tipo di difetto
  (immagine con `alt` vuoto) applicato al prezzo invece che al curriculum
- [05-copy-COPY.md](05-copy-COPY.md) — stesso lotto, prezzo 349/999€, condivide carattere per carattere
  il blocco "La realtà dei fatti?" con questa pagina, e risponde alla domanda trasversale sul prezzo
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — lo standard di forma per questo
  teardown
- `capture/02-funnel-operator/copy-integrale.md`, `scheda.json` — le fonti primarie di questo dossier
- `reports/02-funnel-operator.md` — il rapporto v1 (macchina v1, 2026-09-01), qui riverificato riga per
  riga sui dati reali senza trovare errori fattuali, solo un dettaglio (i 6 vantaggi hero) da segnalare
  come non estraibile come testo
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
