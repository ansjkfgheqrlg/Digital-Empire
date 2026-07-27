# Novacar srl — mezz'ora di ufficio per auto, tolta di mezzo

**Concessionaria multimarca.** Compra auto dai portali esteri, le rivende in Italia.
**Cosa abbiamo costruito:** il programma che prepara il preventivo al posto dei venditori.
**Quando:** consegnato luglio 2026. In uso sui PC del salone.

---

## Com'era prima

Novacar compra dai portali tedeschi. Ogni auto interessante è un annuncio in tedesco: scheda
tecnica, lista degli optional, venti o trenta foto.

Per far vedere quell'auto a un cliente italiano, qualcuno in ufficio doveva:

1. **Tradurre l'annuncio a mano, voce per voce.** Non il titolo: la scheda tecnica intera e la
   lista degli optional. Chi lo faceva teneva aperto il traduttore in un'altra finestra.
2. **Rifare il prezzo con la calcolatrice.** Prezzo di listino estero, più il ricarico del salone,
   più i costi per metterla su strada. Ogni volta da capo. Ogni volta a mano.
3. **Salvare le foto una per una.** E poi rimetterle nel documento, dove spesso venivano tagliate
   perché non erano della misura giusta.
4. **Rimontare il PDF su Word.** Risultato: ogni venditore consegnava un documento leggermente
   diverso dagli altri.

Circa **mezz'ora di lavoro d'ufficio per una singola auto**. Fatto da una persona pagata per
vendere macchine, non per impaginare documenti.

E il problema vero non è la mezz'ora. È che **in quella mezz'ora il cliente ha già scritto ad
altri tre saloni su WhatsApp.**

---

## Cosa abbiamo costruito

Un programma che gira sul computer del salone. Si usa così:

**Si incolla il link dell'annuncio. Si preme un tasto. Circa due minuti dopo esce il PDF finito.**

Dentro ci sono quattro cose che prima si facevano a mano:

| | |
|---|---|
| **Legge l'annuncio estero** | scheda tecnica e optional riportati in italiano |
| **Calcola il prezzo da solo** | le regole del salone — ricarico, messa su strada, margine — sono impostate una volta dal titolare e valgono per ogni preventivo |
| **Prende tutte le foto** | complete, alla dimensione giusta, mai tagliate. Era una richiesta esplicita di Novacar |
| **Impagina il documento** | sempre uguale, sul modello che Novacar usava già. Quattordici regole di impaginazione, rispettate una per una |

### La parte che di solito nessuno mette

Prima di produrre il PDF, il programma fa **sei controlli**. Se anche uno solo fallisce, **il
documento non esce**:

1. **Dati** — l'annuncio è stato letto per intero: marca, modello, allestimento, scheda tecnica
2. **Prezzo** — il calcolo segue le regole del salone e il totale finisce anche nel titolo
3. **Testo** — scheda tecnica ed equipaggiamento sono in italiano, non in tedesco
4. **Immagini** — tutte le foto presenti, intere, mai tagliate
5. **Impaginazione** — le quattordici regole del modello Novacar rispettate una per una
6. **Consegna** — il PDF si apre e viene archiviato nello storico del salone

Il ragionamento dietro è semplice: **meglio nessun preventivo che un preventivo sbagliato in mano
al cliente.** Un prezzo storto su un documento con il vostro logo sopra costa più di due minuti
di attesa.

---

## I numeri

Misurati sulla macchina, contati sui file, non stimati.

| | |
|---|---|
| **65** | preventivi generati su annunci reali, dal 3 al 13 luglio 2026 |
| **11** | marche diverse: Mercedes, Audi, BMW, Tesla, Toyota, Renault… |
| **~2 minuti** | dal link al PDF finito. Tempo di lavoro della macchina |
| **6** | controlli automatici prima di ogni PDF. Se uno fallisce, non consegna |

### Un preventivo vero, preso dallo storico

**Opel Insignia, 13 luglio 2026.** Annuncio estero letto dalla macchina, scheda tecnica riportata
in italiano, regole di prezzo del salone applicate.

Prezzo dell'annuncio: **15.950 €** → sul preventivo: **19.428 €**

Il totale finisce anche nel titolo del documento — *«Opel Insignia Dynamic 19.428 €»* — perché
Novacar lo voleva così.

---

## Cosa questo caso NON dimostra

Ve lo diciamo noi prima che lo chiediate voi. Le stesse righe sono pubblicate sul nostro sito.

- **Non diciamo che Novacar vende di più.** La macchina produce il documento, non chiude la
  trattativa. Chi vi promette un aumento di vendite grazie a un software vi sta vendendo fumo.
- **I 65 preventivi comprendono i nostri collaudi.** Sono annunci veri e PDF veri, generati
  mentre costruivamo e verificavamo la macchina. Sono la prova che funziona, non il registro
  vendite del cliente.
- **La testimonianza firmata non c'è ancora.** Quando arriva la pubblichiamo con nome e cognome.
  Fino ad allora restano i numeri, che potete verificare in demo.
- **Le ore risparmiate al mese non le abbiamo contate.** Sappiamo quanto ci mette la macchina
  (~2 minuti) e sappiamo cosa si faceva prima a mano. Quante auto passino in un mese lo sa
  Novacar, non noi. Non moltiplichiamo per un numero che non abbiamo misurato.

---

## Perché ve lo stiamo raccontando

Il vostro problema non sono i preventivi auto. Ma la forma è la stessa:

**c'è un lavoro ripetitivo che qualcuno di bravo fa a mano tutti i giorni, e che lo tiene lontano
dal lavoro per cui lo pagate.**

Quello che abbiamo fatto per Novacar è: guardare quel lavoro, capire le regole vere (comprese le
quattordici sull'impaginazione, che nessuno aveva mai scritto da nessuna parte), e costruire la
macchina che lo esegue. Con i controlli che impediscono di consegnare una cosa sbagliata.

**Se volete vedere la stessa macchina girare su un caso vostro, la demo dura trenta minuti.**
Non slide: il programma che gira, sui dati veri di Novacar.

---

<!-- ═══════════════════════════════════════════════════════════════════════
     BLOCCO DA NON PUBBLICARE FINCHÉ NOVACAR NON APPROVA PER ISCRITTO.
     Bozza di virgolettato da sottoporre al cliente — NON è una frase
     che il cliente ha già detto. Se non la conferma, questo blocco
     si cancella. Vedi regola 3 in 00-LEGGIMI.md.
     ═══════════════════════════════════════════════════════════════════════

## Cosa dice il cliente

« [BOZZA DA FAR APPROVARE] Prima ogni auto voleva mezz'ora tra traduzione, calcoli e
impaginazione. Adesso incolliamo il link e il preventivo esce da solo, sempre uguale,
con il nostro modello. »

— [Nome e ruolo], Novacar srl

     ═══════════════════════════════════════════════════════════════════════ -->
