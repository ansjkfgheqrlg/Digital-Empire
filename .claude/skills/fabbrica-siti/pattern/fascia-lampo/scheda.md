# fascia-lampo

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md` — TAVOLA 12 (claude-speedrun.com) | canone: `--orange`, `--ink-2`, `--silver-bright`, `--u`, `.in`

## Quando
Fra due sezioni lunghe, quando serve un cambio di ritmo brevissimo — un blocco che si legge in
pochi secondi di scroll, non che si studia. Sulla pagina originale e' la sezione piu' corta fra
quelle con testo reale: 431px contro una media di ~900px.

## Quando NO
Ovunque il colore d'azione sia gia' stato speso altrove nella pagina. La legge CLAUDE-SITI.md §12
concede **un solo** fondo pieno arancione per pagina — questo pattern *e'* quel fondo pieno. Se una
CTA, un badge o un'altra sezione hanno gia' acceso l'arancione a piena superficie, `fascia-lampo`
non si usa una seconda volta: si sceglie quale dei due tenere.

## Il meccanismo
Non e' un contenitore generico riempito d'arancione: e' **l'unica** sezione della pagina dove
l'arancione smette di essere un accento (badge, cerchio, CTA) e diventa lo sfondo intero — ed e'
proprio la rarita' dell'evento a segnalare urgenza massima al lettore.

Il titolo mescola due colori sullo stesso fondo: il testo normale in `--ink-2` (il nero del
canone, mai `#000` puro — vedi la nota in `canone.css` §2), la parola che conta in
`--silver-bright` (bianco). Non e' decorazione: e' la stessa tecnica dell'accento-su-una-parola di
§12, applicata dentro il titolo invece che nel corpo.

Il corpo porta un filetto bianco a sinistra (`border-left`) — non un bordo decorativo qualunque,
ma il segnale visivo che quel testo e' una citazione/voce diretta, non didascalia.

**La grana e' obbligatoria qui piu' che altrove**: un fondo a colore pieno, senza texture propria,
sullo schermo legge "di plastica" — la grana locale (feTurbulence 0.72, multiply) e' quello che lo
fa sembrare stampato e non un rettangolo CSS.

## Cosa cade se sbagli
- **Un secondo fondo pieno arancione altrove in pagina** — annulla l'effetto sorpresa: se l'arancione
  pieno compare due volte, non segnala piu' nulla di eccezionale (viola §12 in modo misurabile).
- **Titolo tutto di un colore solo** — perde il contrasto bianco/nero che guida l'occhio sulla parola
  che conta; diventa un blocco di testo qualunque, solo piu' colorato.
- **Altezza libera invece di `calc(var(--u) * 0.36)`** — se la sezione si allunga, smette di essere
  un "blocco-lampo" e comincia a chiedere di essere letta con calma: il ruolo cambia senza che
  nessuno l'abbia deciso.
- **Grana saltata** — il fondo pieno resta piatto e artificiale; la differenza si vede a distanza,
  non serve zoomare.

## Come lo avvolge la Corsia B
Segue `pattern/CORSIA-B.md` senza eccezioni: il componente React importa `canone.css`, monta dentro
`.page`, e non rinomina nessuna classe. L'unico punto da sorvegliare qui e' il vincolo di §12 —
"un solo fondo pieno arancione per pagina" — che in Corsia B non lo garantisce piu' il CSS da solo
(un sito multi-pagina puo' usare questo componente su piu' pagine diverse senza collidere mai nella
stessa pagina, ma un editor che permette due istanze nella stessa route deve essere lui a rifiutare
la seconda, non il canone).
