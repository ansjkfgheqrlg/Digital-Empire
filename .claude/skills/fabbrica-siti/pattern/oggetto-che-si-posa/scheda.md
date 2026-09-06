# oggetto-che-si-posa

**Corsia A** | origine: `armageddon.css:508-604` + IIFE (Andrei Pascu) | canone: `.settle`, `--t-slow`, `--ease-heavy`

## Quando
Quando l'offerta ha **un oggetto** da mostrare: un pacchetto, un cofanetto, delle carte, un libro,
uno schermo. L'oggetto e' il protagonista della sezione e deve sembrare **appoggiato**, non
incollato.

## Quando NO
Su liste, tabelle, prezzi in colonna. Se non c'e' un oggetto fisico da posare, questo pattern e'
solo un'animazione in piu' senza significato.

## La sequenza esatta
```
t = 0        HTML: class="carte is-sparse is-locked"   -> arrivano SPARSE
t = vista    IntersectionObserver, threshold 0.3
t = +2500ms  via is-sparse  -> si compongono, 820ms var(--ease-heavy)
t = +3400ms  via is-locked  -> SOLO ORA rispondono al mouse
```

**A cosa serve `is-locked`:** impedire che l'hover parta a meta' volo. E' il dettaglio che nessuno
nota e che tutti sentono. Senza, chi ha il mouse gia' li' vede un oggetto che sbanda.

**Perche' partono sparse nell'HTML e non via JavaScript:** cosi' non c'e' nessun lampo. Lo stato
iniziale e' quello scritto, lo script toglie classi, non le aggiunge.

## Le due trasformazioni contrarie
```css
.carta--fronte -> translate(-0.03u, 0.008u) scale(1.05)
.carta--retro  -> translate(0.055u, -0.02u) rotate(8.9deg)   /* da 7.16deg */
```
Il retro **ruota di piu' mentre si sposta**: due movimenti in direzioni diverse sullo stesso oggetto.
E' quello che da' la sensazione della carta che si scosta invece di scivolare.

## Il riquadro sensibile
`.carte` e' **esattamente l'ingombro delle due carte**, non la sezione. Passarci sopra deve voler
dire passare sopra loro, non sopra meta' pagina.

## Cosa cade se sbagli
- **Niente `is-locked`** -> l'hover parte durante l'arrivo e l'oggetto sbanda.
- **Stato iniziale messo dal JavaScript** -> un lampo alla prima pittura.
- **`.carte` grande quanto la sezione** -> l'oggetto si muove quando il mouse e' lontano, e sembra rotto.
- **Nessun ramo `reduce`** -> viola §7: le carte restano bloccate a meta' per chi ha disattivato le animazioni.
