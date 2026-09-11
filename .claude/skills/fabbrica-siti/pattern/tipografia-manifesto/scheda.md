# tipografia-manifesto

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md`,
Tavole 3 e 8 ("GET. SHIT. DONE." / "ASCOLTA BENE.") | canone: `--u`, `--orange`, `--ink`,
`--font-shout`, `.num-tabular`, `.asc .box`/`.prova` in
`agency-empire/cantiere/aura-preview/tavola_template.html:148,151-153`

## Quando
Quando serve **una parola sola che grida**, non un titolo di sezione: un cambio di registro
improvviso, il punto della pagina dove il tono cambia da "spiego" a "ti scuoto". Una casella
arancione piena, tipografia pesante, e sotto la prova in numeri che regge quello che la parola ha
appena detto.

## Quando NO
Più di una volta per pagina: è un urlo, e un secondo urlo nella stessa pagina non raddoppia
l'effetto, lo dimezza — il lettore smette di sentirlo come un'eccezione. E mai come sostituto di un
vero H1 o H2 quando la sezione *è* il contenuto principale della pagina: lì la gerarchia semantica
serve davvero, e la casella da sola non la sostituisce.

## Il meccanismo
La differenza che conta rispetto all'originale studiato: nel report, "ASCOLTA BENE." è marcato
**H1** — un secondo H1 deliberato a metà pagina, tecnicamente scorretto per la gerarchia classica ma
intenzionale (Tavola 8, riga 289-290 del report). Qui la scelta è opposta: la casella è **decorazione
tipografica**, `<div aria-hidden="true">`, fuori dall'albero di accessibilità, e il titolo vero e
accessibile è un `<h2 class="sr-only">` visivamente nascosto accanto. Chi legge con lo schermo
sente il titolo una volta sola; chi legge con gli occhi vede la parola grande. Le due cose non si
sovrappongono e non si contraddicono.

`aria-hidden` sulla casella (non `role="presentation"`) è la scelta più sicura fra le due indicate:
`role="presentation"` toglie il ruolo semantico ma **non** toglie il nodo dall'albero di
accessibilità, e un `<h2>` sr-only accanto rischierebbe la doppia lettura. `aria-hidden` esclude
del tutto, senza ambiguità.

Sotto, tre celle di collaudo con `font-variant-numeric: tabular-nums` (§12 del canone): sono
numeri che si leggono a colpo d'occhio, e cifre che non ballano fra loro sono la differenza fra
"si legge una tabella" e "si legge un allineamento sbagliato".

## Cosa cade se sbagli
- **Casella marcata come vero H1/H2 senza titolo nascosto accanto** → la pagina perde un livello di
  gerarchia semantica reale, esattamente il compromesso che l'originale accetta consapevolmente e
  che qui si è scelto di non accettare.
- **`role="presentation"` senza verificare la doppia lettura** → alcuni screen reader leggono
  comunque il testo del nodo, e il titolo vero accanto lo fa sentire due volte.
- **Più caselle-manifesto nella stessa pagina** → vedi "Quando NO": l'effetto si consuma da solo.
- **Casella arancione senza grana locale** → colore pieno senza la sua grana rompe la legge GRANA
  (2026-09-11): l'arancione "brucia" invece di respirare.

## Come lo avvolge la Corsia B
Regola generale in `CORSIA-B.md`. Qui in particolare: `<div aria-hidden>` + `<h2 class="sr-only">`
restano **esattamente** la stessa coppia di nodi in JSX — non diventano un componente `<VisuallyHidden>`
di libreria che nasconde la stessa logica dietro un nome diverso, per lo stesso motivo per cui
`CORSIA-B.md` vieta di rinominare le classi di stato: la coppia va letta, non indovinata, affiancando
il componente al suo `pattern.html`.
