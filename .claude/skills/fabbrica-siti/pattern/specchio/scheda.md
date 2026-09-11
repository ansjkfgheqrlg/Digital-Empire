# specchio

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md` — TAVOLA 6 (claude-speedrun.com) | canone: `--paper`, `--fg-on-light`, `--silver-bright`, `--grey`, `--line-light`, `--radius-sm`, `--radius-lg`

## Quando
All'apertura della diagnosi, prima di qualunque promessa. Quando serve far riconoscere al lettore
se stesso in un esempio concreto e leggermente imbarazzante — non descrivergli il problema in
astratto, ma mostrarglielo con un artefatto che potrebbe aver scritto lui.

## Quando NO
Quando non esiste un esempio vero da mostrare. Un DM/messaggio inventato "in generale" (senza
etichetta di contesto plausibile: chi, dove, quando) non funziona come specchio — funziona come
lorem ipsum vestito meglio, e il lettore lo sente. Se il copy non ha ancora un esempio reale
raccolto, questa sezione si scrive per ultima, dopo `COPY.md` (§3), non prima.

## Il meccanismo
Due elementi affiancati, non uno sopra l'altro: la foto (il destinatario, non il mittente) e il
messaggio (quello che gli e' davvero arrivato). L'affiancamento e' cio' che genera l'effetto
specchio — se foto e messaggio fossero impilati verticalmente, il lettore leggerebbe prima l'uno
poi l'altro come due fatti separati; affiancati, li legge come un'unica scena.

La bolla porta un'etichetta mono sopra (`DM di oggi · concessionario, Veneto`) che fa da
didascalia giornalistica — data' il contesto in tre parole, senza raccontarlo — e una riga in
corsivo sotto **con i numeri**: non "riceviamo molti messaggi uguali" ma "41 messaggi identici,
0 risposte". La cifra e' cio' che rende l'esempio verificabile invece che aneddotico.

La foto e' quadrata (rapporto 1:1) perche' e' un ritratto, non un'ambientazione: il formato stesso
dice "questa e' una persona", non "questo e' un luogo".

## Cosa cade se sbagli
- **Foto e testo impilati invece che affiancati** — perde l'effetto scena-unica, torna a essere due
  blocchi di contenuto in sequenza.
- **Messaggio senza numeri nella riga sotto** — la prova diventa un aneddoto, non un dato: la
  differenza fra "sono tanti messaggi uguali" e "41 messaggi uguali" e' la differenza fra
  un'opinione e un fatto controllabile.
- **Etichetta generica ("Un messaggio ricevuto") invece che specifica** — la specificita'
  (`concessionario, Veneto`) e' cio' che rende l'esempio credibile: toglierla lo fa sembrare
  inventato anche quando non lo e'.
- **Bolla dello stesso colore del fondo** — se `--silver-bright` sparisce nel `--paper` sotto certi
  monitor, la bolla perde il suo status di "oggetto a parte" (un messaggio reale, non testo di
  sezione): serve il bordo `--line-light` a marcare il confine.

## Come lo avvolge la Corsia B
Segue `pattern/CORSIA-B.md`. In piu': il div `.spec__foto` qui e' un placeholder a gradiente perche'
Corsia A non porta asset — in Corsia B, quando la foto vera esiste, il componente lo sostituisce con
un `<Image>` (Next.js) che mantiene lo stesso `aspect-ratio: 1/1`, lo stesso `border-radius`, e lo
stesso `alt` descrittivo che oggi vive nell'`aria-label` del div. La bolla `.dm` non cambia: e' gia'
puro HTML/CSS, senza stato, e si porta in React senza nessuna logica aggiuntiva.
