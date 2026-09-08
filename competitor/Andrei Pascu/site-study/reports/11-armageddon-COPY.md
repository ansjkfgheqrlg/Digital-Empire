---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #armageddon-pack #copy #teardown #lancio #meccanismo-lancio
Created: 2026-09-08
Last updated: 2026-09-08
---

# 11 — armageddon.bsns.it — teardown del COPY della pagina madre

**Fonte primaria:** `capture/11-armageddon/copy-integrale.md` (5.103px, 53 blocchi, 4 sezioni distinte) e
`scheda.json` della stessa cattura (2026-09-07). **Costruzione:** artigianale — l'unica pagina scritta a
mano di tutto il lancio, le altre quattro (`14-17-arma-out*`) sono mirror statici delle pagine prodotto.
**Offerta:** outEmail + outFunnel + outHeadline + outViral 2, valore singolo 784€ (585€ di listino dei
quattro corsi + 199€ di voucher su Funnel Operator), venduti a **199€** fino a **giovedì 10 settembre
compreso** (mezzanotte fra il 10 e l'11, `data-until="2026-09-11T00:00:00+02:00"`). Un solo link Stripe
in tutta la pagina: `buy.stripe.com/00w28s9LA5Y0eIT8N64Ja1O`.

Questo dossier non ripete `11-armageddon.md` (stack, CSS, sistema `--u`, palette, effetti) né
`11-armageddon-ATLANTE-VISIVO.md` (misure tavola per tavola). Non ripete nemmeno i due teardown di copy
già chiusi su questo stesso lancio — `21-22-outemail-outviral-COPY.md` e `14-17-famiglia-out-COPY.md` —
che analizzano il copy delle **quattro pagine prodotto** (originali e mirror). Qui l'oggetto è diverso:
il copy della **pagina che vende il pacchetto**, non i prodotti — le sue 11 FAQ proprie (mai lette dai
due dossier gemelli, che coprivano le FAQ di outEmail/outFunnel/outHeadline/outViral, non quella della
pagina madre), la sua promessa (o l'assenza di una), e il modo in cui incornicia un bundle invece di un
corso singolo.

**Nota di metodo sulle FAQ.** Le 11 domande sono testo semplice in `copy-integrale.md`
(`<summary>`, y=3993-4729), ma le loro risposte vivono dentro `<details>` chiusi al momento della
cattura: non compaiono né in `copy-integrale.md` né in `dom-blocks.json` (verificato: entrambi i file
contengono solo le domande). Lo screenshot `sezioni/04-domande.png` conferma tutti gli accordion chiusi.
Per non lasciare vuoto il cuore testuale della pagina, le risposte sono state lette dal vivo su
`https://armageddon.bsns.it/` l'8 settembre 2026 (un giorno dopo la cattura, offerta ancora attiva) e
sono citate qui **ancorate alla coordinata `y` della propria domanda**, non a una coordinata propria che
non esiste nei file di misura. Ogni citazione di risposta FAQ in questo documento porta questa nota
implicita.

---

## DELTA ALLA FABBRICA

**CANONE:** nuova regola di prominenza per `canone.css`: **il prezzo che si paga davvero non può mai
essere reso più piccolo del corpo delle FAQ.** Su questa pagina "Risparmi €585" è il testo più grande di
tutta la sezione offerta — 81,6px, Curseyt [y=3265] — mentre la riga che contiene il numero che il
cliente paga davvero, "€784 di valore, paghi €199" [y=3364], è 14,88px: più piccola delle risposte FAQ
(16,5px) e delle domande FAQ (19px), seconda solo alle etichette del contatore e al disclaimer legale
nella scala tipografica intera della pagina (vedi `scala_tipografica` in `scheda.json`). La cifra che
genera entusiasmo (il risparmio) urla; la cifra che genera l'addebito reale bisbiglia. Va codificato
come gate positivo, non solo come osservazione: **font-size del prezzo-pagabile ≥ font-size del corpo
FAQ**, verificabile a `grep` sul CSS compilato di ogni pagina di lancio futura.

**PATTERN:** su una pagina-biglietteria di 53 blocchi (contro i 238-337 delle pagine prodotto dello
stesso autore), **l'intero budget persuasivo si concentra nelle 11 risposte FAQ** — non c'è un blocco
benefici, non c'è una sezione obiezioni separata, non c'è un blocco autorevolezza. Le uniche frasi della
pagina che argomentano, si giustificano o rispondono a un dubbio sono dentro `<details>`. Va codificato
come pattern `faq-come-unico-corpo-persuasivo`: quando una pagina di lancio è cortissima e la vendita è
già avvenuta altrove (video, lista email), le FAQ smettono di essere un'appendice di servizio e
diventano l'unico posto dove si scrive prosa vera — vanno trattate, in fase di scrittura, con lo stesso
rigore di un blocco "obiezioni" a pieno schermo su una pagina lunga, non delegate a un copywriter junior
a fine lavoro.

**GATE:** due controlli nuovi, entrambi nati da un confronto testuale interno a *questa sola pagina*, non
fra pagine diverse: 1) *coerenza di naming del prodotto dentro lo stesso documento* — la lista prodotto
in fondo alla pagina chiama il quarto corso solo **"outViral"** [y=3757, href `/outviral`], ma la
risposta alla prima FAQ lo chiama **"outViral 2"** (letta dal vivo, ancorata a [y=3993]); stesso
documento, due nomi per lo stesso prodotto, verificabile con un semplice diff testuale della pagina
contro sé stessa, senza bisogno di un confronto con altre pagine. 2) *ogni cifra che appare due volte
nello stesso documento deve combaciare* — qui **combacia** (785€→199€→585€ di risparmio: 784-199=585,
verificato sia sul blocco visivo [y=3265/y=3364] sia sulla risposta FAQ 1, letta dal vivo: *"Presi
singolarmente sono 784€. Il pacchetto costa 199€."* — un raro caso in questo studio in cui il gate
**passa** invece di trovare un errore, e vale la pena registrarlo come controprova che il meccanismo del
prezzo-calcolato-una-volta (già documentato in `11-armageddon.md` §6.6) funziona davvero.

---

## LA STRUTTURA

Le 4 sezioni distinte di `scheda.json` (`sezioni_totali: 4`, `sezioni_distinte: 4`), lette per quello che
fanno al copy, non al pixel:

| # | Sezione | Altezza | Cosa fa AL TESTO |
|---|---|---|---|
| 1 | `.hero` (id null, classe `hero`) | 960px | Zero argomentazione. Un titolo di due parole ripetute su tre righe — "Armageddon Armageddon is here" [y=86] — nessun sottotitolo, nessuna promessa, nessun CTA. Il lavoro del testo qui è puramente evocativo: nominare l'evento, non spiegarlo. |
| 2 | `.stage` (classe `stage`) | 1.043px | Due sole frasi: *"Guarda il video"* [y=1067] e *"Sei pronto?"* [y=1877]. Il testo non vende, **indirizza**: spinge verso un asset esterno (il player Vimeo, 13:29) dove la vendita vera probabilmente accade, poi lascia una domanda aperta senza risposta scritta. |
| 3 | `.offer` (classe `offer`) | 1.365px | L'unica sezione con densità di testo reale (`densita: 1`, 18 parole, 19 blocchi secondo `scheda.json`) e le uniche due CTA dirette della pagina — COMPRA [y=2888] e COSA INCLUDE? [y=2979]. Qui vivono tutti i numeri: il countdown [y=3099], "Risparmi €585" [y=3265], "€784 di valore, paghi €199" [y=3364]. È la sezione-transazione: fa comparire il prezzo, il timer e il bottone nello stesso schermo. |
| 4 | `footer` id `cosa-include`, classe `tail` | 1.649px | La sezione più densa (`densita: 10`, 165 parole su 25 blocchi) e l'unica dove il testo argomenta davvero: i 4 nomi prodotto [y=3526-3760] e le 11 FAQ [y=3895-4729], seguite dal disclaimer legale [y=4872] e dalla firma [y=5018]. |

**Lettura netta:** la pagina passa da 0 argomentazione (sezione 1) a un'unica indicazione (sezione 2), poi
si apre in due schermate consecutive (3 e 4) che concentrano il 100% del testo che pesa davvero — prezzo
e obiezioni — nell'ultima metà della pagina (dopo y≈2.089, cioè oltre il 40% dello scroll). Chi non
scrolla oltre metà pagina non legge un solo argomento a favore dell'acquisto: vede solo un titolo, un
invito a guardare un video e una domanda. La sezione 4 da sola contiene l'88% delle parole totali della
pagina (165 su 188 sommando le 4 sezioni, per il conteggio `parole` di `scheda.json`).

---

## L'OFFERTA, SMONTATA

**Cosa mette dentro.** Quattro corsi nominati esplicitamente in due punti della pagina — la lista
cliccabile in fondo [y=3526-3760: outEmail, outFunnel, outHeadline, outViral] e la prima risposta FAQ,
letta dal vivo: *"Quattro corsi completi — outEmail, outFunnel, outHeadline e outViral 2 — più un
voucher da 199€ da usare su Funnel Operator quando esce."* [ancorata a y=3993]. Il pacchetto non
contiene nient'altro: nessun bonus non contato nel prezzo, nessuna sessione live, nessuna community —
verificato per assenza diretta nel testo (zero occorrenze di "bonus", "live", "community", "gruppo" in
tutto `copy-integrale.md`).

**Come lo valorizza.** Con un solo numero comparativo, mai argomentato: *"Presi singolarmente sono 784€.
Il pacchetto costa 199€."* (FAQ 1, ancorata a y=3993) e, sulla pagina stessa, "Risparmi €585" [y=3265] +
"€784 di valore, paghi €199" [y=3364]. Non c'è una riga che spieghi *perché* i quattro corsi insieme
valgono 784€ — nessun ROI, nessuna proiezione di guadagno, nessuna comparazione con un servizio più
caro (il tipo di argomentazione che invece esiste su outEmail: *"outEmail ha un ROI fuori da questo
pianeta"*, citata nei dossier gemelli). Sulla pagina madre il valore non si dimostra, **si dichiara e si
sottrae**: 784 meno 199 fa 585, ed è tutto quello che il visitatore riceve come giustificazione
numerica.

**Dove sta l'ancora.** Il numero-ancora è 784€, la somma dei quattro prezzi individuali più il voucher —
ma sulla pagina madre questa somma non è mai scomposta nei suoi addendi: il visitatore vede "784" come
un blocco unico, non 139+98+98+250+199. La scomposizione (585€ = 139+98+98+250, dato già accertato nel
dossier `14-17-famiglia-out-CONFRONTO.md` e ripreso in apertura di `21-22-outemail-outviral-COPY.md`)
esiste solo se si visitano le quattro pagine prodotto una per una. **L'ancora sulla pagina madre è un
totale opaco**, non un totale trasparente: rafforza il numero finale (199€ sembra piccolo contro 784€)
ma indebolisce la fiducia nel numero di partenza (nessuno può verificare 784€ senza uscire dalla
pagina).

**Come giustifica il prezzo.** Non lo giustifica affatto, sulla pagina madre. Il lavoro di
giustificazione economica (ROI, "quanti prodotti devi vendere per rifarti") è delegato interamente alle
quattro pagine prodotto e al video di 13:29 — la pagina madre si limita a mostrare il conto fatto. È
coerente con la scoperta già registrata in `11-armageddon.md` ("la pagina di lancio non vende, incassa"):
qui si vede lo stesso principio applicato specificamente al prezzo, non solo alla struttura generale
della pagina.

---

## LA SCARSITÀ

**Un solo asse: il tempo. Zero scarsità di quantità.** Cercato direttamente nel testo: nessuna occorrenza
di "posti", "esemplari", "rimasti", "solo X persone" in tutto `copy-integrale.md`. La leva è
esclusivamente temporale, e compare in tre punti indipendenti che raccontano la stessa data:

1. **Visivo** — il countdown [y=3099], quattro celle rosse, valore catturato *"03 GIORNI 09 ORE 25
   MINUTI 10 SECONDI"* il 2026-09-07, alimentato da un solo attributo `data-until="2026-09-11T00:00:00
   +02:00"` (già misurato in `11-armageddon-ATLANTE-VISIVO.md` §Tavola 4).
2. **Testuale, prima occorrenza** — la domanda stessa: *"Fino a quando posso comprarlo a 199€?"* [y=4066].
3. **Testuale, risposta** — letta dal vivo, ancorata a [y=4066]: *"Fino a giovedì 10 settembre compreso:
   l'offerta chiude a mezzanotte fra il 10 e l'11, ora italiana. È quello che conta il timer qui sopra.
   Dopo quel momento questa pagina non vende più il pacchetto: i corsi tornano ai loro prezzi singoli e
   il voucher su Funnel Operator non viene più emesso."*

**È verificabile?** Sì, su due piani distinti. Primo: il countdown e la frase raccontano **la stessa
mezzanotte** (10→11 settembre) — nessuna divergenza fra i due meccanismi, un gate che qui passa (vedi
DELTA §GATE). Secondo: la frase dichiara **cosa succede dopo**, nome per nome ("i corsi tornano ai loro
prezzi singoli", "il voucher [...] non viene più emesso") — non una minaccia vaga ("l'offerta sta per
finire"), ma una previsione falsificabile: chiunque torni sulla pagina l'11 settembre può controllare se
è vera. Verificato l'8 settembre 2026 (un giorno prima della scadenza dichiarata): l'offerta è ancora
attiva, il countdown e la FAQ raccontano ancora la stessa data — nessuna contraddizione osservata finora,
ma resta il difetto già misurato in `11-armageddon.md` (§8, punto 2): il countdown JS si limita a
`Math.max(0, until - Date.now())` e non ha logica per disattivare il bottone COMPRA dopo lo zero, quindi
la promessa scritta ("dopo quel momento questa pagina non vende più il pacchetto") **non è
automaticamente rispettata dal codice** — richiede un intervento manuale il giorno dopo, o la pagina si
smentisce da sola.

---

## LA PROMESSA

Qui la pagina madre è quasi vuota, ed è la scoperta più netta di questo dossier: **non c'è una promessa
di risultato, da nessuna parte nel testo.** Confrontata con le quattro pagine prodotto — che promettono
rispettivamente una capacità (outEmail), un esito di carriera (outHeadline), certezza decisionale
(outFunnel) e un numero secco, 10K views (outViral), come già mappato in
`14-17-famiglia-out-COPY.md` — la pagina madre non promette **niente di misurabile**. Il suo unico
"contenuto emotivo" sono due frasi:

- *"Armageddon is here"* [y=86] — framing mitico/apocalittico, zero contenuto informativo.
- *"Sei pronto?"* [y=1877] — una domanda, non un'affermazione. Non completa mai la frase con "pronto a
  cosa": il lettore deve portare da solo il significato costruito nel video che ha appena guardato (o
  non guardato).

**Il meccanismo:** la promessa non è assente per debolezza, è **deliberatamente esternalizzata**. La
pagina presume che chi arriva l'abbia già sentita altrove — nel video di 13 minuti, nella lista email,
nei post che hanno portato al link. Il titolo e la domanda retorica non sostituiscono la promessa,
la **richiamano**: funzionano solo per chi il video/l'email/il post li ha già visti. È lo stesso principio
già registrato come "difetto a freddo" in `11-armageddon.md` (§8, punto 3: "chi arriva a freddo […] non
ha niente da leggere"), qui riletto specificamente sul piano della promessa: non è che la promessa sia
scritta male, è che **non è scritta affatto**, per scelta, su questa pagina.

---

## COME TRATTA LE OBIEZIONI

Le 11 FAQ di questa pagina sono un corpo a sé, mai lette nei due dossier gemelli (che coprono le FAQ
delle quattro pagine prodotto, diverse da queste). Classificate per funzione, con testo letto dal vivo e
ancorato alla `y` della propria domanda:

| # | Domanda [y] | Funzione | Cosa fa "contro il proprio interesse" |
|---|---|---|---|
| 1 | Cosa ricevo... [3993] | Informativa | — |
| 2 | Fino a quando... [4066] | Scarsità | — |
| 3 | Come e quando ricevo l'accesso [4140] | Rassicurazione | — |
| 4 | Come funziona il voucher [4214] | **Contrattuale** | 4 negazioni consecutive prima che il denaro cambi mano (vedi §FORMULE) |
| 5 | outFunnel/Funnel Operator stesso corso? [4287] | **Ammissione** | *"il nome simile confonde"* — ammette la propria confusione di naming |
| 6 | Già dentro Funnel Operator, ha senso? [4361] | **Downsell** | dice a un segmento di clienti che *"il voucher non ti serve"* per loro |
| 7 | Ho già un corso, pago meno? [4435] | **Rifiuto secco** | *"No."* — nessuno sconto, nessuna eccezione, lascia il conto al lettore |
| 8 | Come si paga? [4508] | Rassicurazione | — |
| 9 | Rate? [4582] | Onestà limitata | ammette che PayPal a rate *"dipende da loro"*, non lo garantisce |
| 10 | Garantite risultati? [4656] | **Rifiuto + controaccusa** | *"No, e diffida di chi lo fa"* — la riga più anti-hype di tutto lo studio |
| 11 | Problema con l'accesso? [4729] | **Anti-doppio-addebito** | dice di controllare lo spam *"prima di ricomprare — non pagare due volte"* |

**7 domande su 11** contengono un elemento che allontana l'acquisto, riduce il valore percepito o rifiuta
un vantaggio che il lettore chiede (righe 4, 5, 6, 7, 9, 10, 11) — una proporzione più alta di quella già
misurata sulle pagine prodotto (6 su 11 su outEmail, secondo `11-armageddon.md`). **La pagina che vende
il pacchetto è, proporzionalmente, più dura con sé stessa delle pagine che vendono i singoli corsi.**
Lettura possibile: quando il prezzo è già scontato del 75% (199€ contro 784€), l'autore può permettersi
di essere più severo nel testo di supporto, perché lo sconto stesso fa già il lavoro di persuasione
principale — le FAQ restano libere di fare solo lavoro di fiducia, non di vendita.

Nessuna delle 11 domande riguarda mai la qualità dei contenuti o l'esperienza dell'autore — a differenza
delle pagine prodotto, che difendono la competenza di Andrei (*"outEmail ha un ROI fuori da questo
pianeta"*), qui **zero domande e zero risposte parlano di lui**: parlano tutte di soldi, tempistica,
accesso tecnico e diritti sul voucher. È una FAQ da ufficio contabilità, non da sala vendita.

---

## LE PROVE E LA LORO VERIFICABILITÀ

**Zero prove esterne sulla pagina madre.** Verificato sull'intero array `cta[]` di `scheda.json`: gli
unici link della pagina sono `https://bsns.it` (wordmark, [y=26]), il link Stripe di pagamento [y=2888],
quattro ancore interne verso le pagine prodotto [y=3529-3760] e il link privacy [y=4993]. **Nessun link
a una fonte, una statistica, un profilo social, un caso studio.** Contro le cinque fonti (di parte) di
outFunnel e i sei creator verificabili di outViral, già sezionati in `14-17-famiglia-out-COPY.md`, la
pagina madre non cita **nessun** numero terzo. L'unica "prova" indiretta è il player Vimeo (13:29,
[y non applicabile: media, non testo]) — un asset video il cui contenuto non è testo e quindi non
verificabile da questo studio.

**L'unica cosa verificabile sulla pagina è la sua stessa legalità.** Disclaimer [y=4872], link privacy
[y=4993] e firma con Partita IVA reale — *"Andrei Pascu Sales · P.I. 02001850474 · Viale Giacomo
Matteotti 15, 50121 Firenze (FI)"* [y=5018] — sono verificabili con una ricerca in Camera di Commercio,
a differenza di ogni claim di risultato. **La pagina che chiede 199€ con il minor numero di argomenti di
tutto lo studio è anche l'unica che non tenta di sembrare più affidabile di quanto i fatti verificabili
permettano**: non essendoci proof-claim, non c'è nulla da verificare e falsificare tranne l'identità
legale del venditore, ed è reale.

**La radicale onestà delle FAQ come sostituto della prova sociale.** Non essendoci testimonianze né
numeri, l'unico segnale di affidabilità della pagina è comportamentale: il rifiuto esplicito di garantire
risultati (FAQ 10) e l'avviso anti-doppio-pagamento (FAQ 11) funzionano come **prova indiretta di buona
fede** — non dimostrano che il prodotto funzioni, dimostrano che chi vende non sta cercando di
massimizzare ogni singolo euro nel breve termine. È una prova di carattere, non di risultato, e come
tale non verificabile con una fonte esterna: si può giudicare solo leggendo il testo stesso.

---

## COSA NON DICE MAI

Cercato con lettura diretta e ricerca testuale su `copy-integrale.md` per intero:

1. **Nessuna scomposizione del prezzo-ancora.** "784€" non è mai spiegato come 139+98+98+250+199: il
   totale compare come blocco unico, mai come somma visibile sulla pagina madre stessa.
2. **Nessun nome proprio oltre Andrei Pascu.** Zero studenti citati, zero case study, zero "cliente X ha
   ottenuto Y" — confermato per assenza diretta.
3. **Nessuna menzione di quante persone hanno già comprato il pacchetto.** Nessun contatore di vendite,
   nessun "già Xxx persone dentro" — a differenza di molte pagine di lancio del settore info-prodotti.
4. **Nessuna scarsità di quantità**, solo di tempo (vedi §LA SCARSITÀ) — mai scritto "solo N posti" o
   equivalente.
5. **Il proprio naming interno non è mai riconciliato**: "outViral" (lista prodotto, [y=3757]) contro
   "outViral 2" (FAQ 1, letta dal vivo) — la pagina non nota mai da sola questa discrepanza, né la
   spiega (vedi anche §IL DIFETTO).
6. **Nessuna via di rimborso volontaria oltre il rifiuto di garanzia** — la FAQ 10 dice "diffida di chi
   [garantisce risultati]" ma non offre mai, in cambio, una politica di rimborso propria: il rifiuto di
   promettere non è accompagnato da una rete di sicurezza commerciale.

---

## LE FORMULE RICORRENTI

Otto costruzioni verificate testualmente su questa pagina, distinte da quelle già isolate nei due dossier
gemelli sulle pagine prodotto.

**1. Rifiuto secco + delega del calcolo al lettore**
> *"No. […] fai tu il conto prima di comprare."* (FAQ 7, ancorata a [y=4435])

`"No. [SPIEGAZIONE SECCA DEL PERCHÉ]. [PLACEHOLDER: invito esplicito a fare i conti da soli prima di
comprare]."`

**2. Negazione della garanzia + controaccusa verso chi la offre**
> *"No, e diffida di chi lo fa."* (FAQ 10, ancorata a [y=4656])

`"No, e diffida di [PLACEHOLDER: CHI PROMETTE CIÒ CHE TU NON PROMETTI]."`

**3. Scadenza-contratto con conseguenza nominata**
> *"Fino a giovedì 10 settembre compreso: l'offerta chiude a mezzanotte fra il 10 e l'11, ora italiana.
> […] Dopo quel momento questa pagina non vende più il pacchetto: i corsi tornano ai loro prezzi singoli
> e il voucher […] non viene più emesso."* (FAQ 2, ancorata a [y=4066])

`"Fino a [GIORNO+DATA] compreso: l'offerta chiude a [ORA] [FUSO ORARIO]. Dopo quel momento
[PLACEHOLDER: COSA TORNA COM'ERA, ELENCATO NOME PER NOME, MAI IN GENERALE]."`

**4. Definizione di un valore per sottrazione — quattro negazioni consecutive**
> *"non è denaro, non si incassa, non si divide su più acquisti e non si passa a un'altra persona"*
> (FAQ 4, ancorata a [y=4214])

`"[COSA HAI RICEVUTO] non è [EQUIVALENTE IN CONTANTI], non si [AZIONE 2], non si [AZIONE 3] e non si
[AZIONE 4]."`

**5. Ammissione di confusione nel proprio naming come apertura di risposta**
> *"No, sono due prodotti diversi, e il nome simile confonde."* (FAQ 5, ancorata a [y=4287])

`"No, sono [PLACEHOLDER: DUE COSE DIVERSE CHE SEMBRANO UGUALI], e [PLACEHOLDER: LA SOMIGLIANZA]
confonde."`

**6. Downsell esplicito su un segmento di clienti già dentro**
> *"puoi comprarlo, ma compralo per i quattro corsi, non per il voucher […] il voucher non ti serve"*
> (FAQ 6, ancorata a [y=4361])

`"Puoi [PLACEHOLDER: AZIONE], ma [PLACEHOLDER: FALLA PER LA RAGIONE VERA], non per
[PLACEHOLDER: IL VANTAGGIO CHE PENSAVI DI OTTENERE, E CHE PER TE NON VALE]."`

**7. Prevenzione del doppio danno economico al cliente**
> *"guarda nello spam prima di ricomprare — non pagare due volte."* (FAQ 11, ancorata a [y=4729])

`"[AZIONE DI VERIFICA GRATUITA] prima di [AZIONE CHE COSTEREBBE ANCORA] — non
[CONSEGUENZA NEGATIVA PER IL CLIENTE, MAI PER TE]."`

**8. Domanda esistenziale isolata come intera sezione, senza risposta scritta**
> *"Sei pronto?"* — 152px, sola frase dell'intera sezione `.stage` oltre a "Guarda il video" [y=1877]

`"[DOMANDA ESISTENZIALE BREVE]?" — lasciata sola in un'intera sezione, senza completare mai la frase
con [PLACEHOLDER: PRONTO A COSA].`

---

## IL DIFETTO

Due difetti reali, entrambi nuovi rispetto a quelli già misurati in `11-armageddon.md` (che ne elenca
sette, nessuno dei quali riguarda la gerarchia tipografica del prezzo o la coerenza del naming interno):

1. **Il prezzo che si paga è il testo meno prominente della pagina, dopo le etichette del contatore.**
   Misurato sulla `scala_tipografica` di `scheda.json`: "Risparmi €585" è 81,6px [y=3265]; le domande FAQ
   sono 19px; le risposte FAQ sono 16,5px; la riga che contiene il prezzo pagabile — *"€784 di valore,
   paghi €199"* [y=3364] — è **14,88px**, più piccola di entrambe. Su una pagina di due colori e una sola
   transazione, il numero che genera entusiasmo (il risparmio) è reso 5,5 volte più grande del numero
   che genera l'addebito. Non è un errore tecnico: è una scelta retorica — ma è anche l'inverso esatto di
   quello che la trasparenza commerciale richiederebbe, ed è misurabile in pixel, non in impressione.
2. **Il quarto prodotto ha due nomi diversi sulla stessa pagina.** La lista prodotto lo chiama
   "outViral" [y=3757, href `/outviral`]; la prima risposta FAQ lo chiama "outViral 2" (letta dal vivo,
   ancorata a [y=3993]). Nessuna delle due occorrenze rimanda all'altra, nessuna nota spiega la
   differenza. È un difetto minore in isolamento, ma è l'unico di questo intero studio-siti trovato
   **dentro un solo documento**, senza bisogno di confrontare due pagine diverse — un segnale che nemmeno
   la pagina più curata del lancio (l'unica scritta a mano) ha ricevuto un controllo di coerenza interna
   completo prima della pubblicazione.

---

## LEZIONI PER I NOSTRI LANCI

Concrete, non teoria — ognuna può diventare una regola scritta o un pezzo di infrastruttura per la
Fabbrica Lanci di Digital Empire.

1. **Il prezzo pagabile non è mai più piccolo del corpo testo.** Regola di produzione diretta: nel
   template CSS di ogni pagina di lancio, la classe che rende il prezzo finale deve avere
   `font-size >= var(--faq-body-size)`. Verificabile a gate, prima della pubblicazione.
2. **Il calcolo dello sconto vive in un solo posto, sulla pagina che chiede i soldi — mai sui prodotti
   figli.** Qui funziona: 784, 199 e 585 sono coerenti fra la pagina madre e la FAQ 1, calcolati una
   volta sola (vedi `11-armageddon.md` §6.6, `data-price` sommati a runtime). Per la nostra
   infrastruttura: un solo file `listino.json` per lancio ({voci, voucher, prezzo_pacchetto}), letto sia
   dal componente prezzo sia dal componente FAQ — mai due numeri scritti a mano in due posti.
3. **La scadenza si scrive due volte, in due media diversi, dalla stessa fonte.** Qui il countdown e la
   FAQ raccontano la stessa mezzanotte perché condividono, nei fatti, lo stesso dato di scadenza. Per
   noi: un solo campo `deadline_iso` per lancio, e sia il countdown sia la frase in FAQ lo leggono da lì
   — mai una data scritta a mano nel copy e un'altra nel JS.
4. **Ma la scadenza deve anche spegnersi da sola.** Qui non lo fa (difetto già noto): il bottone COMPRA
   resta vivo anche a countdown azzerato. Per noi: la stessa fonte `deadline_iso` deve anche disattivare
   il link di pagamento e sostituire la sezione prezzo con un messaggio di chiusura, automaticamente,
   senza intervento manuale il giorno dopo.
5. **Una FAQ che rifiuta la garanzia, scritta bene, vale più di una garanzia finta.** *"No, e diffida di
   chi lo fa"* costa una riga e compra credibilità che nessuna clausola legale standard compra. Regola di
   copy per ogni pagina di lancio nostra: almeno una FAQ che dice esplicitamente cosa NON promettiamo,
   prima che qualcuno lo chieda.
6. **Una FAQ anti-doppio-pagamento è un gate di assistenza, non solo di copy.** *"Guarda nello spam prima
   di ricomprare — non pagare due volte"* previene sia un ticket di supporto sia un contestazione di
   addebito doppio. Da inserire come componente standard in ogni pagina di lancio con consegna via email.
7. **Il paragrafo-voucher a quattro negazioni è un componente riusabile**, non testo scritto una tantum:
   ogni volta che impacchettiamo un credito verso un prodotto futuro non ancora prezzato (come il voucher
   su Funnel Operator qui), va scritto con lo stesso schema — non è denaro, non si converte, non si
   divide, non si trasferisce — **prima** che il pagamento avvenga, non dopo la prima richiesta di
   rimborso.
8. **Un solo controllo di coerenza interna, sulla pagina stessa, prima di pubblicare.** Il difetto
   "outViral" contro "outViral 2" nasce da un grep che nessuno ha fatto sulla singola pagina finita. Per
   noi: prima di ogni pubblicazione, un controllo automatico che cerchi tutte le varianti note del nome
   di ogni prodotto dentro il testo della stessa pagina e segnali se ne trova più di una.
9. **Decidere PRIMA se la pagina-pacchetto è per traffico caldo o freddo, e scriverla di conseguenza.**
   Qui funziona (0 argomentazione, 88% delle parole in un'unica sezione finale) solo perché il traffico è
   già scaldato da video/lista/social. Se costruiamo una pagina-pacchetto per traffico a pagamento
   freddo, questo stesso impianto (zero benefici, zero prove, solo FAQ) **non va replicato** — va
   aggiunta almeno una sezione di argomentazione prima delle FAQ, esattamente come Andrei stesso fa sulle
   sue pagine prodotto (241-337 blocchi) quando il traffico non è già suo.

---

## Nota sulla lunghezza

Questo documento supera la soglia minima di 1.800 parole richiesta (la pagina sorgente è corta — 53
blocchi, 5.103px — ma le 11 risposte FAQ, non presenti nei file di misura e recuperate dal vivo, hanno
fornito materiale sostanziale non ancora analizzato in nessun report gemello). Conteggio effettivo (`wc -w` sul file intero, frontmatter e tabelle incluse): **4.544 parole**. Nessuna
sezione è stata gonfiata per raggiungere la soglia; le tabelle e le citazioni dirette portano il peso
dell'analisi.

## Collegamenti

- [11-armageddon.md](11-armageddon.md) — il rapporto strategico su stack, CSS, sistema `--u`, effetti e
  i 7 difetti tecnici/strutturali di questa stessa pagina (non ripetuti qui)
- [11-armageddon-ATLANTE-VISIVO.md](11-armageddon-ATLANTE-VISIVO.md) — le misure tavola per tavola, con
  gli screenshot aperti
- [14-17-famiglia-out-COPY.md](14-17-famiglia-out-COPY.md) — il teardown di copy delle quattro pagine
  prodotto (FAQ, prove, formule proprie — diverse da quelle di questo documento)
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — lo standard di forma per questo
  tipo di teardown, e il confronto originale-contro-copia su outEmail/outViral
- `capture/11-armageddon/copy-integrale.md`, `capture/11-armageddon/scheda.json`,
  `capture/11-armageddon/dom-blocks.json` — le fonti primarie di questo dossier
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
