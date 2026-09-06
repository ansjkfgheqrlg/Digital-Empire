# CORSIA B — come si avvolge un pattern vanilla

**Legge:** `CLAUDE-SITI.md §5` — *un pattern nuovo si scrive prima in vanilla, poi la Corsia B lo
avvolge in un componente. Mai il contrario: dal vanilla al framework si sale, dal framework al
vanilla si riscrive.*

Questo file vale per **tutti** i pattern. Non ce n'e' uno per cartella, perche' la regola e' una sola.

---

## La regola in tre righe

1. Il `pattern.html` della cartella e' **la fonte**. Il componente React ne e' una copia strutturale.
2. Il CSS **non si riscrive in Tailwind**: si importa. Il canone e' gia' CSS, e Tailwind v4 lo prende
   con un `@import`.
3. Cio' che il pattern fa in JavaScript vanilla, in Corsia B lo fa React — **con lo stesso
   comportamento**, compreso il ramo `prefers-reduced-motion`.

---

## Il passaggio, passo per passo

**1 — il canone entra per primo**
```css
/* src/app/globals.css */
@import "../../../.claude/skills/fabbrica-siti/canone/canone.css";
@import "tailwindcss";
```
Le classi del canone (`grain-fine`, `text-silver-orange`, `btn-orange`, `label`, `prose`, `legal`,
`num-tabular`) restano disponibili **con lo stesso nome**. Tailwind si usa per il layout locale, mai
per ridefinire un valore che il canone ha gia'.

**2 — la colonna resta la colonna**
```tsx
<div className="page">   {/* --u, --col, --btn, --cell vivono qui */}
```
`.page` **non e' decorativa**: e' il nodo che porta le variabili di misura. Un componente montato
fuori da `.page` perde `--u` e collassa.

**3 — lo stato entra in React, il CSS resta CSS**
```tsx
const [posato, setPosato] = useState(false);
const [bloccato, setBloccato] = useState(true);
// ...IntersectionObserver in useEffect, stessi 2500ms e 900ms
<div className={cn("carte", !posato && "is-sparse", bloccato && "is-locked")}>
```
Le classi restano quelle del pattern vanilla. **Non si inventano nomi nuovi in Corsia B:** un
`is-locked` che in B si chiama `locked` rompe il legame fra le due corsie e, alla prima modifica, le
fa divergere.

**4 — il ramo reduced-motion e' obbligatorio anche qui**
```tsx
const reduce = useReducedMotion();          // framer-motion
if (reduce) { setPosato(true); setBloccato(false); return; }
```
§7 non ha un'eccezione per React.

**5 — le animazioni d'ingresso passano a `<Reveal>`**
`.in--a` / `.in--b` / `.in--c` diventano `<Reveal delay={0.18}>` / `0.34` / `0.5`. **Gli stessi
numeri**: i delay del canone sono in millisecondi, quelli di Framer in secondi, e la conversione e'
l'unica cosa che cambia.

---

## Cosa NON si porta in Corsia B

| Cosa | Perche' |
|---|---|
| `<dialog>` e `<details>` nativi | funzionano identici in React. Sostituirli con un componente e' regalare peso e perdere l'accessibilita' gratuita |
| Il parallax in `requestAnimationFrame` | GSAP ScrollTrigger fa lo stesso lavoro meglio, **ma con gli stessi rapporti** (0.2 / 0.155 / 0.09 / 0.04) |
| I valori del canone | mai riscritti come classi Tailwind arbitrarie. Se serve un valore nuovo, si aggiunge **al canone** (§1) |

---

## Il controllo
Un componente di Corsia B e' corretto quando, **affiancato al suo `pattern.html`, e' visivamente
indistinguibile** alla stessa larghezza. Se non lo e', ha ragione il vanilla: e' lui la fonte.
