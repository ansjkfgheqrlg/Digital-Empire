# faq-native

**Corsia A** | origine: `armageddon.css:749-812` (Andrei Pascu) | canone: `--line-hair`, `--measure-body`, `--t-76`

## Quando
Sempre, quando ci sono domande da rispondere. **`<details>` nativo**: si apre con JavaScript
disattivato, non ha dipendenze, e porta gia' dentro l'accessibilita' che un accordion fatto a mano
deve reimplementare da zero (tastiera, stato, annuncio).

## Quando NO
Se le "domande" sono in realta' benefici travestiti. Una FAQ che non risponde a un'obiezione vera e'
copy nascosto in un cassetto, e nessuno apre un cassetto per farsi vendere qualcosa.

## Le due cose che si dimenticano sempre
1. **`list-style: none` sul summary** (Firefox, Chrome) **e** `::-webkit-details-marker { display: none }`
   (Safari). Servono **entrambe**: Safari disegna il suo triangolo se gliene dici una sola.
2. **Il marcatore e' `content`**, `+` che diventa `\2013` su `[open]`. Nessun'icona da caricare,
   nessuno stato da sincronizzare.

## La composizione
Le domande sono **allineate a sinistra dentro un blocco centrato**. Il commento originale:
*"because these are read."* Tutto il resto della pagina e' centrato perche' va guardato; questo
blocco e' testo, e il testo si legge da un margine fisso.

Risposte a `--measure-body` (64ch) con `line-height: 1.66` e opacita' `--t-76`. I `<strong>` tornano
a opacita' piena: sono i punti su cui l'occhio si ferma scorrendo.

## Lo standard di scrittura, che vale piu' del CSS
Sul sito studiato, **6 risposte su 11 allontanano l'acquisto**: *"Ho gia' uno dei quattro corsi.
Posso pagare meno?" -> "No. [...] fai tu il conto prima di comprare."* | *"Mi garantite dei risultati?"
-> "No, e diffida di chi lo fa."*

**Il meccanismo:** dicendo apertamente le cose che costano, si compra il diritto di essere creduti su
quelle che rendono. Una FAQ che risponde solo a favore di chi vende non viene letta come una
risposta: viene letta come altro copy.

## Cosa cade se sbagli
- **Una sola delle due regole sul marcatore** -> su Safari compaiono due segni.
- **Accordion in JavaScript** -> senza JS le risposte spariscono, e con esse le obiezioni chiuse.
- **FAQ tutte a favore** -> il blocco perde la sua unica funzione.
