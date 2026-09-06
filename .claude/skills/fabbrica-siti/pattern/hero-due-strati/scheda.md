# hero-due-strati

**Corsia A** | origine: `armageddon.css:264-303` (Andrei Pascu), fuso col silver-mixing Empire
canone: `--u`, `text-silver-orange`, `text-silver-white`, `--ease-land`

## Quando
Ogni hero che ha **un soggetto al centro** (un volto, un prodotto, un oggetto) e un titolo che deve
stargli sopra senza nasconderlo.

## Quando NO
Hero senza soggetto: senza qualcosa da attraversare, il secondo strato non incide niente e paghi un
tag in piu' per zero effetto. Li' si usa un titolo solo, silver-mixed.

## Il meccanismo
La stessa parola e' nel DOM **due volte, nella stessa posizione**:

| strato | z-index | resa |
|---|---|---|
| pieno | 1, **sotto** il soggetto | la parola e' piena dove c'e' solo il fondo |
| contorno | 3, **sopra** il soggetto | `color: transparent` + `-webkit-text-stroke` |

Dove i due si sovrappongono al soggetto, la parola smette di essere piena e diventa un'**incisione**.

Il contenitore `h1` **non ha z-index**: le parole devono ordinarsi una per una, e uno z-index sul
padre creerebbe un contesto di impilamento che le sigilla tutte insieme.

Lo strato-contorno ha `aria-hidden="true"`: lo screen reader legge la parola **una volta sola**.

## L'atterraggio, tre tempi
| | durata | delay |
|---|---|---|
| soggetto `reveal-zoom` | 1700ms | 0 |
| alone `reveal-fade` | 1400ms | 120ms |
| parola 1 `reveal-rise` | 1200ms | **180ms** (`.in--a`) |
| parola 2 `reveal-rise` | 1200ms | **340ms** (`.in--b`) |

**L'animazione sta sui figli `<i class="in">`, mai sul contenitore.** Il contenitore lo muove il
parallax, e due sistemi di `transform` sullo stesso nodo si annullano a vicenda.

## Le misure
`height: var(--u)` (quadrato sulla colonna) | parola 1 `--u x 0.1996` a `top 0.0622` | parola 2
`--u x 0.2025` a `top 0.62125` | contorno `max(1px, --u x 0.0013)`.

## Cosa cade se sbagli
- **z-index sull'`h1`** -> le tre parole si impilano insieme e l'effetto sparisce del tutto.
- **Animazione sullo `<span>` invece che sull'`<i>`** -> il parallax cancella l'ingresso.
- **`aria-hidden` dimenticato sul contorno** -> il titolo viene letto due volte.
- **Contorno troppo spesso** -> non e' piu' un'incisione, e' un secondo titolo che litiga col primo.
