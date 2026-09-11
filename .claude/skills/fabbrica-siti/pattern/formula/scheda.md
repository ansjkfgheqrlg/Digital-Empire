# formula

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md`,
Tavola 26 ("Produttività = robe utili che fai / unità di tempo", calcolo 6/2=3 → 10/2=5, +66%) |
canone: `--u`, `--orange`, `--silver-dim`, `--radius-sm`, `--ease-heavy`, `.num-tabular`

## Quando
Quando la promessa è **"lavori meglio"** e serve renderla verificabile invece che vaga: una formula
esplicita, un confronto a barre, un calcolo passo-passo con numeri piccoli e controllabili a mente.
È il meccanismo che la Tavola 26 misura come il più elaborato della pagina studiata, e la ragione è
proprio questa — trasforma un'equazione in qualcosa che il lettore può rifare da solo.

## Quando NO
Quando non c'è un vero prima/dopo misurabile: una formula con numeri inventati o arrotondati ad
arte è il difetto opposto di quello che il pattern vuole risolvere — un'equazione finta è peggio di
nessuna equazione, perché sembra una prova e non lo è. E non per un confronto puramente posizionale
("dove sei tu rispetto agli altri"): lì serve `asse-posizionale`, senza numeri.

## Il meccanismo
Il vincolo che conta è §8 della legge, portato al limite: **due** numeri soli nel sorgente
(`data-pezzi` e `data-ore` per la riga "ora" e per la riga "sistema", dentro un blocco `#dati`
nascosto), e ogni altra cifra in pagina — le due percentuali di larghezza della barra, le cifre
"X/ora" accanto a ciascuna barra, il calcolo passo-passo, la percentuale di differenza finale — si
**deriva** da quei due in JavaScript. Cambiare un solo numero nel blocco `#dati` aggiorna tutto il
resto da solo; scriverne uno slegato in un punto qualsiasi del testo è esattamente il difetto che
l'articolo vieta.

La larghezza delle barre non è mai una percentuale scritta: è `valore / max * 100%`, calcolata sul
massimo reale delle due voci — se in futuro "con il sistema" cambia, il massimo si sposta da solo e
la barra "ora" si ridimensiona di conseguenza, senza toccare una riga di CSS.

Il riquadro di calcolo usa una famiglia monospace di sistema (non un valore del canone: il canone
ha solo Onest) **solo** per allineare le cifre in colonna — è dichiarato nel CSS come deroga minima
a §1, perché un font di allineamento non è un colore o una misura, è un tecnicismo di leggibilità.

## Cosa cade se sbagli
- **Una percentuale scritta a mano nel testo del calcolo** → il giorno che i due numeri sorgente
  cambiano, quella riga mente e nessun test se ne accorge: è il difetto misurato altrove nello
  studio, otto cifre per quattro metriche nello stesso negozio.
- **Barra con larghezza fissa in CSS** → la barra smette di rispondere ai dati, diventa
  un'illustrazione invece che un grafico.
- **Grana sulla barra dimenticata** → un riempimento a colore pieno senza la sua grana locale rompe
  la coerenza visiva con il resto della pagina (legge GRANA, 2026-09-11).
- **Transizione di larghezza senza il ramo `reduced-motion`** → la barra che si anima in violazione
  di §7, per chi ha disattivato le animazioni le vede comunque muoversi.

## Come lo avvolge la Corsia B
Regola generale in `CORSIA-B.md`. Qui in particolare: il blocco `#dati` diventa una prop tipizzata
(`{ora: {pezzi, ore}, sistema: {pezzi, ore}}`) invece di un `<div hidden>` con `data-*` — è l'unico
punto dove la Corsia B **migliora** la fonte invece di limitarsi a copiarla, perché React ha un modo
nativo di passare dati che l'HTML statico non ha. Il calcolo (tasso, massimo, differenza) resta
**la stessa funzione**, spostata in una utility condivisa e chiamata da entrambe le corsie: non si
riscrive due volte la stessa aritmetica.
