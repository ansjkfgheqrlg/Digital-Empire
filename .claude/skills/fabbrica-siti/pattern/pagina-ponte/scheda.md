# pagina-ponte

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/capture/25-define/copy-integrale.md`
(y=165-949) e `.../capture/24-asa/copy-integrale.md` (y=185-1073) | canone: `--t-76`, `--cell`,
`--radius-lg`, `--radius-pill`, `--ease-land`, `--t-fast`, `--t-base`, `.btn` / `.btn-orange`,
`--orange`, `--font-shout`, `--leading-body`

## Quando
Fra due pagine che si convincono a vicenda, quando il passo successivo ha bisogno di un contesto (un
video) prima che il lettore sia pronto a decidere — ma questa pagina non è dove si decide, è dove si
*sposta*. Misurato: 35-36 blocchi di testo, contro i 259 di una vera pagina di vendita (report
macchina-del-funnel). Una sezione, un video, un bottone: chi ci arriva non sta comprando, sta
imparando abbastanza per arrivare alla pagina che vende.

## Quando NO
- **Se il lettore è già convinto.** Un cliente che torna per comprare non ha bisogno di un altro
  video: metterglielo davanti è un gradino in più fra lui e il pagamento, non un aiuto.
- **Se serve chiudere un'obiezione specifica.** Questo pattern ha zero obiezioni per legge — è la
  sua forza per spostare, ed è la sua rottura se lo si usa per convincere. Un'obiezione vera va in
  una FAQ (`faq-native`) o nella pagina di vendita, mai qui.
- **Se il video non esiste ancora.** Una pagina-ponte senza video reale è una pagina vuota con un
  bottone: meglio saltare direttamente al passo successivo che simulare un ponte che non c'è.
- **Se ci sono più di un CTA possibile.** «Un solo bottone» non è una preferenza estetica: è quello
  che rende il pattern una freccia invece che un bivio. Due bottoni qui sono un altro pattern (una
  landing di scelta), non una variante di questo.

## Le cose che si dimenticano sempre
1. **Saltare un livello di intestazione per copiare il sorgente alla lettera.** Su `/asa` la riga di
   controllo del consumo è un `<h3>` senza nessun `<h2>` prima — il titolo è `<h1>`, poi si salta
   dritto a `<h3>`. Il pattern usa **`<h2>`**: stessa taglia visiva (38,4 px), gerarchia corretta.
   Copiare la taglia va bene; copiare il salto di livello è un difetto accessibilità che il
   sorgente ha e che non c'è motivo di ereditare.
2. **Confondere il click-to-play con un'animazione da spegnere.** Il video parte solo al clic
   esplicito dell'utente sul facade: non è un autoplay ambientale, quindi non serve (e sarebbe
   sbagliato) bloccarlo dietro `prefers-reduced-motion` nel JavaScript — quella preferenza riguarda
   il movimento *imposto*, non l'azione *richiesta*. Quello che invece **va** spento in reduced
   motion è la piccola transizione di hover sul cerchio del play: sono due cose diverse, e il
   pattern le tratta diversamente (vedi il commento nel CSS sopra `@media (prefers-reduced-motion)`).
3. **Caricare l'embed video a corredo della pagina invece che al clic.** Un iframe Vimeo o YouTube
   porta con sé centinaia di KB di script del provider anche se il visitatore non lo guarda mai.
   Il facade lazy (poster + bottone play, video vero creato solo al clic) non è un vezzo di
   performance: è quello che tiene la pagina dentro il tetto di peso della Corsia A dichiarato in
   `canone.json` (gate `9_peso`, 250 KB al primo carico).
4. **Rendere il video invisibile senza JavaScript.** Se il facade fosse l'unico modo di vedere il
   video, un browser senza JS (o con JS bloccato) vedrebbe un cerchio inerte. Il `<noscript>` con lo
   stesso video dentro non è un fallback di cortesia: è la condizione che rende lecito usare JS qui,
   per la regola del codice dettata in cima a questo lavoro — "deve funzionare anche senza".

## La composizione
Colonna centrata `min(760px, 100%)` — più larga della pre-cassa perché qui c'è un video da ospitare,
ma comunque un modulo, non una pagina piena larghezza `--u`.

Misure reali, convertite in frazione di `--u` sulla base della pagina sorgente (1440 px):

| Elemento | Origine (y, tag, pagina) | Misura reale | Frazione applicata |
|---|---|---|---|
| Titolo | y=165/185, `<h1>`, `/define` e `/asa` | 60,8 px | `--u * 0.0422222` |
| Riga d'ingresso | y=327, `<p>`, `/define` | 16 px | `--u * 0.0111111` |
| Video (larghezza) | y=460, `<iframe>` w=732, `/define` | 732/1440 | `--u * 0.5083333` |
| Riga di controllo | y=878, `<h3→h2>`, `/asa` | 38,4 px | `--u * 0.0266667` |

Il rapporto del video (732:413 nel sorgente) è **≈ 16:9** — si usa `aspect-ratio: 16/9`, il valore
standard, invece di portarsi dietro un numero storto per una differenza sotto l'1%: la legge §6
chiede di dichiarare l'origine dei numeri non ovvi, non di essere ridicoli sulla quinta cifra
decimale.

Il cerchio del play riusa **`var(--cell)`** del canone (56-85 px) invece di inventare una taglia
nuova: è la stessa soglia — "sotto questa misura non si tocca in modo affidabile" — già motivata nel
canone per la cella del contatore. Un'icona di riproduzione ha lo stesso vincolo di un bersaglio
touch: non serviva una seconda variabile per lo stesso motivo.

**L'accento (§12) si spende sulla parola che porta i soldi**, non su quella che descrive il mestiere
— esattamente come su `/asa`, dove è colorato «monetizzare» e non «copywriting». Nel titolo
d'esempio l'accento è su **«automatizzare»**, non su «Manuale Claude Code»: è il verbo che vende il
risultato, il nome del prodotto resta testo normale.

## Lo standard di scrittura
**Originale**, `/define` [y=327]: *«Te lo spiego in questo video con un esempio pratico»* — una
riga breve, in prima persona, che dice cosa sta per succedere (un video) e perché vale la pena
guardarlo (un esempio pratico, non teoria).

**Placeholder:** *«Te lo faccio vedere in questo video, con un caso vero.»* — stessa struttura
(annuncio + motivo per restare), diversa solo nel verbo: [PROMESSA IN UNA RIGA], sempre in prima
persona, sempre prima del video, mai dopo.

**Originale**, `/asa` [y=878], la riga che il report chiama "la riga che vale il viaggio": *«Ti
consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»* Il
meccanismo (report macchina-del-funnel): non è cortesia, è **controllo del consumo** — chiede di
spendere il tempo *prima* del clic. Chi arriva al bottone ha già visto il video, quindi clicca
sapendo cosa sta per ottenere: meno rimborsi, meno assistenza, un clic di qualità più alta.

**Placeholder:** *«Ti consiglio di guardare tutto il video prima di cliccare il pulsante qui sotto:
capisci meglio cosa stai per ottenere.»* — la struttura non si tocca: consiglio esplicito + "prima
di cliccare" + il beneficio del guardare per intero. Solo [COSA STAI PER OTTENERE] cambia per
prodotto; il meccanismo — mettere una condizione temporale prima del bottone — resta identico,
perché è quello che fa il lavoro, non le parole esatte.

## Il difetto da non copiare
Nessuno specifico a questo pattern: `/define` e `/asa` sono le due pagine più pulite dello studio,
senza refusi né incongruenze misurate. L'unico scostamento dal sorgente è quello dichiarato sopra
("Le cose che si dimenticano sempre" §1) — il salto di livello di intestazione — corretto qui, non
copiato.
