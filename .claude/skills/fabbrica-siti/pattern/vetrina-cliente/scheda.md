# vetrina-cliente

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md`,
Tavola 24 (il carosello esterno "Marius") | canone: `--u`, `--cell`, `--radius`, `--radius-sm`,
`--line-light`, `--paper`, `--fg-on-light`, `--ease-heavy`, `--t-slow`

## Quando
Quando il prodotto è **un pannello, una dashboard, un'interfaccia** che il cliente userà — e la
prova migliore non è descriverla, è farla sfogliare. Ogni volta che servono più di una schermata
per mostrare cosa fa davvero il sistema, senza occupare la pagina con quattro sezioni identiche.

## Quando NO
Con **una sola schermata**: un carosello con un pallino solo è un componente che finge di essere
navigabile e non lo è — meglio un riquadro fermo. E non per uno **screenshot statico di
risultato** (un numero, un grafico di crescita): quello è prova sociale, non un'interfaccia da
esplorare, e vive nel pattern `formula` o in un blocco di prova a parte.

## Il meccanismo
Le "schermate" sono **HTML vero**, non immagini: titolo, righe finto-interfaccia, un piccolo
pannello a tre pallini in alto che imita la barra di una finestra. Zero peso di immagini esterne,
zero `alt` da scrivere — il testo *è* lo screenshot.

Il carosello si sposta con `transform: translateX()` sulla pista (`.vetrina__pista`), non
cambiando `display`: un solo strato che scorre, mai un elemento che appare e sparisce di scatto.
I **pallini di paginazione si generano dal numero reale di schermate** (`schermi.length`), mai
scritti a mano in HTML — è la stessa disciplina di §8 applicata alla navigazione: un contatore
scritto a mano e uno schermo aggiunto dopo, in due punti diversi, sono la ricetta esatta del
disallineamento.

`aria-live="polite"` su un nodo separato (`.vetrina__stato`, visivamente nascosto) annuncia
"Schermata N di totale: titolo" a ogni cambio — uno screen reader non vede la pista scorrere, deve
sentirselo dire. Le frecce **e** le frecce della tastiera (`ArrowLeft`/`ArrowRight`) chiamano la
stessa funzione `vai()`: un solo punto di verità per il cambio schermata, mai due percorsi che
potrebbero disallinearsi.

## Cosa cade se sbagli
- **Pallini scritti a mano in HTML** → il giorno che si aggiunge una quinta schermata restano
  quattro, e il pallino attivo smette di corrispondere a quello che si vede.
- **`aria-live` sulla pista invece che su un nodo a parte** → lo screen reader legge il testo di
  *ogni* schermata mentre la pista scorre, non solo quella corrente: rumore, non annuncio.
- **Frecce senza tastiera** → un carosello che risponde solo al mouse non è navigabile, è cliccabile:
  due cose diverse per chi non usa il mouse.
- **Schermate come immagini invece che HTML** → torna il difetto misurato altrove nello studio (42
  screenshot con `alt=""`): il contenuto smette di esistere per chi non vede lo schermo.

## Come lo avvolge la Corsia B
Regola generale in `CORSIA-B.md`. Qui in particolare: `i`/`vai()`/`totale` diventano `useState` +
`useRef` sulla pista, la generazione dei pallini resta un `.map()` sullo stesso array di schermate
(mai un numero scritto a mano nemmeno in JSX), e `aria-live` resta sullo stesso nodo separato — non
si sposta sul contenitore solo perché in React è più comodo leggerlo da lì.
