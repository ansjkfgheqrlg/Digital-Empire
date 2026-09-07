# pre-cassa

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/capture/28-outfunnel-1/copy-integrale.md`
(y=149-602) e `.../capture/27-armadeggon-strp/scheda.json` | canone: `--t-78`, `--t-76`, `--t-55`,
`--line-hair`, `--radius-sm`, `.label`, `.num-tabular`, `.card-dark`, `.btn` / `.btn-orange`,
`--orange`, `--font-shout`, `--leading-body`

## Quando
Ogni volta che il prodotto è un acquisto one-shot e il bottone di vendita, senza questo gradino,
porterebbe dritto al gateway di pagamento. È la legge §11 (ADR-024): sei elementi fissi, meno di uno
schermo e mezzo — misurato 1.512 px su `/outfunnel-1` e 1.752 px su `/armadeggon-strp` — niente altro
dentro.

## Quando NO
- **Prodotti in abbonamento.** «Una tantum» diventerebbe una bugia, e il §11 esiste apposta per
  uccidere il sospetto dell'abbonamento — non per costruircelo sopra al contrario.
- **Checkout ospitato da un provider esterno** (Stripe Checkout hosted, Gumroad, pagina di
  riepilogo di terzi): il gradino raddoppia e il cliente legge la stessa cifra due volte. È
  esattamente la violazione che §8 vieta — un dato, non due.
- **Nessun codice sconto e nessuna ambiguità sul tipo di pagamento.** Il gradino può accorciarsi
  (saltare l'elemento 3), ma non sparire: la riaffermazione dell'atto (elemento 1) resta comunque,
  perché è quella che uccide il ripensamento nell'ultimo metro.
- **Carrello con più articoli.** Questo pattern è per un prodotto solo. Un carrello ha bisogno di un
  riepilogo riga per riga — è un altro pattern, non una variante di questo.

## Le cose che si dimenticano sempre
1. **Colorare il codice sconto con l'accento.** Su `/outfunnel-1` il codice CWSHOP usa
   `#139699`, una sfumatura di `#13989a` (il colore delle lettere «out» nel nome prodotto) — di
   fatto **due** occorrenze imparentate, non una. La legge §12 chiede *una* parola, non due. Nel
   pattern il codice resta neutro (bordo `--line-hair`, monospace, nessun colore d'azione): l'unico
   accento della pagina resta speso sul nome del prodotto.
2. **Rendere il codice permanente per pigrizia.** Un codice senza scadenza scritta in pagina — o
   peggio, senza controllo lato server dietro — non è uno sconto, è il prezzo con un passaggio in
   più. Vedi "Il difetto da non copiare" sotto: è già successo, è misurato, non è teoria.
3. **Dimenticare `noindex` sulla pagina.** Se la pre-cassa è raggiungibile solo dopo un clic
   d'acquisto ma resta indicizzabile, Google la trova comunque — è quello che è successo a
   `/outfunnel-1` — e il codice sconto diventa pubblico per chiunque cerchi «nome prodotto sconto».
4. **Duplicare la cifra altrove in pagina** (es. ripeterla nel bottone: «Acquista a 47,00€»). Il
   bottone dice l'azione, non il prezzo — il prezzo ha già il suo posto, isolato, nell'elemento 4.
   Ripeterlo è la violazione di §8 nel punto più facile da non notare perché sembra rafforzare, non
   duplicare.

## La composizione
Colonna centrata, larga al massimo `min(560px, 100%)` — non tutta `--u`: la pre-cassa non è una
pagina larga, è un modulo stretto, perché il compito è uno solo e non serve spazio per altro.

Misure reali da `/outfunnel-1` (pagina 1440px), convertite in frazione di `--u`:

| Elemento | Origine (y, tag) | Misura reale | Frazione applicata |
|---|---|---|---|
| 1. Occhiello | y=149, `<em>` | 16 px | `--u * 0.0111111` |
| 2. Nome prodotto | y=189, `<h1>` | 68,3 px | `--u * 0.0474306` |
| 3. Istruzione | y=261, `<p>` | 16 px | `--u * 0.0111111` |
| 4. Cifra | y=500, `<div>` | 35,2 px | `--u * 0.0244444` |
| 5. Condizione | y=543, `<div>` | 17,6 px | `--u * 0.0122222` |

**17,6 non è un numero indipendente: è esattamente metà di 35,2.** La condizione («Una tantum») è
tipograficamente la metà del corpo della cifra — un rapporto 1:2 misurabile, non un'estetica a
occhio. Il pattern lo mantiene: `.cassa__condizione` è dichiarata come frazione separata proprio per
non perdere quel rapporto se in futuro qualcuno cambia solo `.cassa__cifra`.

Il nome del prodotto ripetuto in piccolo sopra la cifra (elemento «ricevuta») riusa `.label` del
canone (`--t-50`, maiuscolo, `letter-spacing: 0.1em`) invece di inventare una quarta taglia di
testo — è esattamente il ruolo per cui `.label` esiste.

Il bottone usa `.btn` / `.btn-orange` del canone così come sono, **non** i 195×53 px misurati su
AP: §1 dice che il canone vince sul gusto, e vince anche quando il gusto è quello del concorrente
studiato. Nessuna transizione propria da spegnere per §7: `.btn` e `.card-dark` sono già dentro il
blocco `@media (prefers-reduced-motion)` di `canone.css` §14.

## Lo standard di scrittura
**Originale**, `/outfunnel-1` [y=149]: *«Stai acquistando…»* — due parole e tre puntini, prima del
nome del prodotto. Il meccanismo (report macchina-del-funnel): riafferma l'atto invece di
ricominciare a vendere. È l'anti-ripensamento più economico che esista, perché non discute, non
aggiunge un argomento nuovo — presuppone che la decisione sia già presa.

**Placeholder:** *«Stai acquistando…»* seguito dal nome prodotto — questa riga non si personalizza
per prodotto, resta identica: è un meccanismo, non un vezzo di copy. L'unica cosa che cambia sotto è
[PRODOTTO].

**Originale**, [y=261]: *«Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed entrare.
Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto.»* — un'istruzione operativa
(cosa fare adesso, in ordine) più il codice, nello stesso paragrafo: non due blocchi separati.

**Placeholder:** *«Accedi con le credenziali che hai appena creato e completa il pagamento. Se hai
ricevuto un codice nella tua email di conferma, inseriscilo ora: [CODICE] vale solo [FINESTRA DI
TEMPO] e solo per questo acquisto.»* — la finestra di tempo è obbligatoria nel placeholder, non
opzionale: è la correzione strutturale del difetto sotto.

**Originale**, [y=543]: *«Una tantum»* — due parole, attaccate alla cifra, senza una riga di
spiegazione attorno. Il meccanismo: toglie il sospetto dell'abbonamento esattamente nel punto in cui
nasce (subito dopo aver visto un numero), prima che il lettore abbia il tempo di chiederselo.

**Placeholder:** *«Una tantum»* resta invariato — è già alla forma minima possibile, aggiungere
parole indebolirebbe l'effetto, non lo spiegherebbe meglio.

## Il difetto da non copiare
Su `/outfunnel-1` il codice **CWSHOP** — 20% di sconto — è scritto in chiaro su una pagina
**indicizzabile**. Chiunque cerchi «outFunnel sconto» lo trova su Google. Un codice sconto che c'è
sempre, per chiunque, senza bisogno di aver fatto nulla per meritarlo, non è più uno sconto: è il
prezzo. Il listino reale di outFunnel è **78,40 €**, e i «98,00 €» mostrati in pagina sono
decorazione — un ancoraggio di prezzo che nessun cliente reale paga mai.

Questo pattern corregge il difetto in due punti, non in uno solo:
1. **Nel copy** — il codice dell'esempio (`GRAZIE24`) dichiara una finestra esplicita (24 ore),
   non un'eternità muta.
2. **Nella pagina** — `<meta name="robots" content="noindex, nofollow">` in testa al file: una
   pre-cassa raggiungibile solo dopo un clic d'acquisto non ha alcun motivo di essere indicizzata, e
   tenerla fuori dall'indice è la prima barriera contro esattamente il difetto misurato qui.

La disciplina da sola non basta — si stanca, come nota già §8 della legge per un problema analogo.
Il controllo vero (verificare lato server che il codice non sia scaduto) resta fuori dallo scope di
un pattern Corsia A senza stato server: qui si dichiara la regola in copy e in meta, l'applicazione
reale è compito del sistema di pagamento a valle.
