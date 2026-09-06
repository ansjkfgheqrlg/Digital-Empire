# prova-video

**Corsia A** | origine: `armageddon.css:376-490` (Andrei Pascu) | canone: `--u`, `--font-shout`, `--t-50`

## Quando
Quando **il video e' l'argomento principale** della pagina: VSL, presentazione di lancio, demo. Il
player sta in pagina, non dietro una copertina: **un clic solo, quello sul play**.

## Quando NO
Video di contorno o testimonianze: li' il player va dentro una card e non prende una sezione intera.
E **mai** su una pagina che riceve traffico freddo *senza* un testo alternativo: chi non guarda resta
senza argomenti (difetto n.3 di armageddon).

## Le tre decisioni che contano

**1 - Il richiamo e' bianco, non arancione.**
Su un fondo caldo l'arancione del brand e' l'unica cosa che non si leggerebbe. La regola tipografica
cede al contrasto, e al suo posto arriva un'**ombra doppia**: un alone largo per il fondo chiaro, una
riga secca sotto per staccare.

**2 - `pointer-events: none` sul richiamo.**
Sta sopra il fondo, mai sopra un controllo del player. Senza, il clic sul play puo' finire sul testo.

**3 - `dnt=1` sul player** (l'equivalente YouTube e' `youtube-nocookie.com`).
Niente cookie -> **niente banner da mostrare**. Una scelta tecnica che elimina un elemento di
interfaccia.

## Le misure
riquadro `left: --col + --u x 0.1321`, `width: --u x 0.7631`, `aspect-ratio: 16/9`,
`border-radius: --u x 0.01582` | richiamo `--u x 0.072` | freccia `--u x 0.21`

**Su <=720px:** il riquadro va a `left: var(--col)` e `width: var(--u)` (bordo a bordo) e perde il
raggio; la sezione cresce a `--u x 1.28` perche' il player a tutta larghezza e' piu' alto (56% della
colonna invece di 43%) e senza quella crescita il richiamo sopra e la domanda sotto gli finirebbero
addosso. **Numeri misurati a 390px**, come impone §2.

## Cosa cade se sbagli
- **Copertina davanti al player** -> due clic invece di uno, e il primo non porta valore.
- **Niente `pointer-events: none`** -> il richiamo mangia il clic sul play.
- **Sezione ad altezza fissa su telefono** -> il player va sotto la domanda e la pagina si accavalla.
