# micro-sondaggio

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md` — TAVOLA 7 (claude-speedrun.com) | canone: `--orange`, `--silver`, `--radius-pill`, `--t-base`, `.label`

## Quando
Dopo una lista di segnali/sintomi, quando il lettore ha appena riconosciuto qualcosa di se' e serve
fargli **compiere un'azione fisica** prima di continuare — non per raccogliere un dato, ma per
aumentare il suo investimento nella pagina. Funziona come cerniera fra diagnosi e soluzione.

## Quando NO
Quando il bivio deve essere vero — cioe' quando le due risposte devono davvero portare a contenuti
diversi (un vero A/B di percorso, un vero form). Questo pattern e' dichiaratamente un
micro-commitment, non un router: usarlo dove serve una vera diramazione e' un inganno che il
lettore scopre al primo clic, e un inganno scoperto costa piu' di quanto il pattern rende.

## Il meccanismo
I due pulsanti sono **identici in tutto**: stesso stile, stesso peso visivo, stesso bordo
argento al 30%, nessuna gerarchia (nessuno dei due e' "primario"). La sola differenza e' il testo.
Questa identita' visiva e' voluta: se un pulsante fosse pieno e l'altro fantasma, il lettore
capirebbe subito che una risposta e' "quella giusta" e il sondaggio perderebbe credibilita'.

Entrambi puntano allo **stesso ancoraggio** (`href="#ascolta-bene"`): non e' un bivio, e' un
imbuto — qualunque cosa il lettore scelga, il flusso prosegue identico. La misura originale lo
conferma: nessuno dei due CTA aveva un `href` diverso dichiarato nella pagina sorgente.

Il clic scrive `data-voto` sull'elemento cliccato — cinque righe di JavaScript, senza animazione.
**Non si spegne con `prefers-reduced-motion`**: quella preferenza disattiva il movimento (§7), non
un cambio di attributo istantaneo che non anima nulla. Spegnerlo sarebbe un'interpretazione troppo
larga della regola, e toglierebbe l'unico feedback che il clic e' stato registrato a chi ha
disattivato le animazioni.

## Cosa cade se sbagli
- **Un pulsante con piu' peso visivo dell'altro** — rompe l'illusione del sondaggio libero: il
  lettore sceglie l'opzione che "sembra" quella giusta, non quella vera.
- **`href` diversi fra i due pulsanti** — trasforma un micro-commitment in un vero bivio non
  progettato: entrambe le destinazioni vanno testate come pagine a se', raddoppiando il lavoro per
  un effetto che non l'ha mai richiesto.
- **JavaScript disattivato sotto `prefers-reduced-motion`** — toglie il feedback del clic senza
  ragione: qui non c'e' nulla da spegnere, perche' non c'e' nulla che si muove.
- **Meno di 4 segnali nella lista sopra** — il pattern si regge sull'accumulo: uno o due segnali non
  costruiscono abbastanza riconoscimento prima della domanda "ti ritrovi?".

## Come lo avvolge la Corsia B
Segue `pattern/CORSIA-B.md`. La parte da tradurre con attenzione e' il JavaScript: in Corsia B
`data-voto` diventa `useState` sul singolo bottone (o un piccolo reducer se i pulsanti sono piu' di
due), **senza** passare dal ramo `useReducedMotion()` di Framer Motion — quel hook resta riservato
a cio' che anima davvero. Gli `href` restano ancore native (`<a href="#ascolta-bene">`), non
`onClick` con `router.push`: e' scroll nella stessa pagina, non navigazione.
