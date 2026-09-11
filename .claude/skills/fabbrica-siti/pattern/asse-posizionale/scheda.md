# asse-posizionale

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md`,
Tavola 18 (il diagramma BROKIE→TU→COMPETITOR) | canone: `--u`, `--orange`, `--silver-dim`,
`--silver-bright`, `.linea`/`.asse` in `agency-empire/cantiere/aura-preview/tavola_template.html:135-145`

## Quando
Quando il lettore deve **collocarsi da solo** fra due estremi — "come lo fai oggi" e "come lo
farebbe un sistema" — senza che nessun aggettivo glielo dica. È l'unica visualizzazione
**posizionale**, non numerica, misurata nello studio: mette il lettore fisicamente al centro di un
asse invece di elencargli dei punti.

## Quando NO
Quando il confronto ha bisogno di una cifra (percentuale, tempo, soldi): lì serve il pattern
`formula`, non un asse senza numeri. E non due volte nella stessa pagina — un solo asse per sito,
altrimenti il lettore smette di sentirsi al centro e comincia a contare quante volte gli è stato
detto.

## Il meccanismo
Il nodo centrale "TU" è **fisicamente diverso** dagli altri due, non solo etichettato diverso:
cerchio più grande (28px contro 14px su `--u` 1180), bordo bianco pieno invece che grigio sottile.
La linea che li unisce è un **gradiente** argento→arancione (`.linea::before`): non collega due
punti uguali, mostra una direzione. Il nodo di destra ("Automatizzato") è pieno arancione — l'unico
colore d'azione della sezione, speso lì e non sul titolo (§12 della legge).

La foto a sinistra (4:5, segnaposto a gradiente, nessuna immagine esterna) porta la riga bianca
**in alto** invece che in basso: stessa ricetta di banda scura + ombra tripla di `cucitura-fotografica`
e `hero-due-strati`, la posizione cambia, il meccanismo no — perché il testo su una foto sta sempre
su una banda scura, non importa dove.

## Cosa cade se sbagli
- **Nodo "TU" della stessa misura degli altri due** → il lettore non si riconosce al centro, l'asse
  diventa un elenco di tre voci uguali e il pattern perde la sua unica ragione d'essere.
- **Linea a tinta unita invece che in gradiente** → sparisce la direzione, resta solo un filo che
  unisce tre pallini senza dirti dove sta andando.
- **Più di un asse in pagina** → ogni asse successivo diluisce il primo: il lettore si è già
  collocato, ripeterglielo suona come un rimprovero.
- **Riga di testo senza banda scura sotto** → su una foto chiara il testo bianco sparisce; è
  esattamente la legge "testo su foto" che esiste per non farlo succedere.

## Come lo avvolge la Corsia B
Regola generale in `CORSIA-B.md`. Qui in particolare: `.linea` e i tre `.linea div` restano classi
identiche nel componente React — è un asse statico, senza stato, quindi non c'è `useState` da
aggiungere: il componente è una copia 1:1 della struttura HTML, con `--foto` del riquadro sinistro
che in Corsia B diventa una vera `<Image>` di Next mantenendo lo stesso `aspect-ratio: 4/5` e la
stessa `.riga` sopra.
