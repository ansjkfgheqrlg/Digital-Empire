# ora-con

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md` — TAVOLA 20 (claude-speedrun.com) | canone: `--orange`, `--silver`, `--silver-dim`, `--ink-2`, `--line-dark`, `.num-tabular`, `.label`

## Quando
Come riepilogo, dopo che il problema e la soluzione sono gia' stati spiegati per esteso altrove
nella pagina. Non introduce concetti nuovi: **ricapitola** in due colonne cio' che il lettore ha
gia' letto, e chiude con un conto che rende il beneficio misurabile invece che dichiarato.

## Quando NO
All'apertura della pagina, prima che il lettore sappia di cosa si sta parlando. Un confronto
ORA/CON senza contesto precedente e' solo una tabella astratta — funziona come *sintesi*, non come
*argomento*: se e' la prima cosa che il lettore vede, gli manca il perche' delle due colonne.

## Il meccanismo
Le due colonne non sono simmetriche nel trattamento visivo, anche se lo sono nella struttura: la
colonna "ORA" usa un pallino vuoto e testo argento (`--silver`, meno saturo, meno presente); la
colonna "CON IL SISTEMA" usa un pallino pieno arancione e testo pieno (`--fg`). La differenza non
e' decorativa — codifica visivamente "assenza" contro "presenza" senza bisogno di dirlo a parole.

Il riquadro calcolo sotto non ripete il confronto: lo **quantifica**. Due righe con una cifra prima
e una dopo (`12 → 41`, `9,5 ore`) — l'unico posto della sezione dove il beneficio smette di essere
qualitativo. Le cifre usano `.num-tabular` (canone.css §12): e' il modo in cui il canone rende un
numero "tecnico" senza inventare un terzo font-family che la legge §1/§3 non prevede.

## Cosa cade se sbagli
- **Le due colonne con lo stesso trattamento cromatico** — sparisce la codifica visiva
  assenza/presenza, e il lettore deve leggere ogni riga per capire quale colonna e' quale.
- **Il calcolo prima delle due colonne** — il numero arriva senza aver ancora visto il confronto
  qualitativo che lo spiega: la cifra sembra piovuta dal nulla invece che dedotta.
- **Un dato duplicato fra colonna e calcolo** (es. "9,5 ore" scritto sia nella lista sia nel
  riquadro con valori diversi) — viola §8 della legge: un numero, una fonte sola nel sorgente.
- **Riquadro calcolo senza grana** — essendo un fondo pieno (`--ink-2`), senza la grana locale
  risalta come un rettangolo CSS piatto in mezzo a una pagina altrimenti testurizzata.

## Come lo avvolge la Corsia B
Segue `pattern/CORSIA-B.md`. Le due colonne restano una griglia CSS pura (nessuno stato, nessuna
interazione) e si portano in React senza logica aggiuntiva. Il riquadro calcolo e' il punto da
sorvegliare quando i numeri diventano dinamici (es. calcolati da un valore che l'utente inserisce
altrove nella pagina): in quel caso `.num-tabular` resta sulla view, ma il valore stesso deve avere
**una sola fonte di stato** — coerente con §8 — non un numero ricalcolato in due componenti diversi.
