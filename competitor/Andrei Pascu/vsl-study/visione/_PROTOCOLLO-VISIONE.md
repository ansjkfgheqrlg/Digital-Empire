# Protocollo di visione — Fase 2 di EMP-DIOEDIT

Chi guarda i frame segue questo protocollo alla lettera. È scritto una volta sola perché tutti i
Doom Bot di visione lo leggano identico: la tabella che esce deve poter essere fusa fra video
diversi senza rimettere mano alle colonne.

**Regola madre:** *la macchina misura, l'occhio giudica.* I colori si **misurano** con
`vsl-study/scripts/colori_frame.py` (hex, percentuale di area, luminosità). Font, effetti,
inquadratura, postura si **giudicano a occhio** e si dichiarano come giudizio.

## Cosa si guarda
Per ogni video, i frame in `vsl-study/misure/<slug>/frames/stacchi/stacco-NNNN.png`: **il primo
fotogramma di ogni inquadratura.** È lì che si vede il montaggio. Il file
`frames/manifest.json` → `frame_stacchi` dà per ognuno il timestamp (`t`, `hhmmss`) e il numero
d'inquadratura. Se un frame di stacco è ambiguo (nero, mosso), si apre anche il frame denso più
vicino in `frames/frame-NNNN.png` (`frame_densi` nel manifest) — e lo si dice.

**Si guardano TUTTI, uno per uno, con lo strumento di lettura immagini.** Non si campiona, non
si estrapola: un frame non aperto è un frame non visto, e va marcato «NON VISTO», mai descritto
a intuito.

## La tabella — `visione.md`, una riga per inquadratura

| n | t | tipo | testo a schermo (letterale) | font (giudizio) | colori (misurati) | effetto / transizione | soggetto | note |
|---|---|---|---|---|---|---|---|---|

- **tipo**: uno di `parlato` (lui in camera) · `b-roll` · `schermo` (screen recording) · `grafica`
  (titolo, card, numero) · `testo-pieno` (solo testo su fondo) · `misto` · `nero`.
- **testo a schermo**: trascritto **alla lettera**, maiuscole comprese; `—` se assente.
- **font (giudizio)**: famiglia (serif / sans / mono / display), peso (light / regular / bold /
  black), caso (MAIUSCOLO / minuscolo / Titolo), corsivo sì/no, dimensione relativa (piccolo /
  medio / grande / enorme). Se pensi di riconoscere il carattere (es. Plus Jakarta Sans, che è il
  font del suo sito), scrivilo con «?» — è un'ipotesi, non una misura.
- **colori (misurati)**: i primi 3 hex da `colori_frame.py` con la %; più, se c'è, **il colore del
  testo o dell'accento** stimato a occhio con «~».
- **effetto / transizione**: cosa si vede *rispetto al frame precedente*: taglio secco, jump cut
  (stesso set, lui si sposta), zoom in/out, dissolvenza, testo che appare, evidenziazione,
  sottotitolo, freccia/cerchio, split screen, mock-up, ecc. Se nulla: `taglio secco`.
- **soggetto**: dov'è, come è vestito, dove guarda, cosa fa la mano, distanza (primo piano /
  mezzo busto / figura intera) — solo quando è in camera.
- **note**: tutto ciò che non entra sopra e che un montatore vorrebbe sapere.

## Il catalogo — in fondo a `visione.md`
Dopo la tabella, **le ricorrenze**, contate:
1. Quanti frame per tipo (parlato / b-roll / schermo / grafica / testo-pieno).
2. I set/inquadrature ricorrenti (es. «mezzo busto, fondo nero, luce da sinistra» × N).
3. I colori che tornano (hex → in quanti frame).
4. I font che tornano (giudizio → in quanti frame).
5. Gli effetti che tornano, con i timestamp in cui compaiono.
6. **Le cose che compaiono una volta sola** — spesso sono la scelta più deliberata.
7. Il rapporto fra testo a schermo e parlato: quante volte il testo **ripete** ciò che dice,
   quante volte lo **completa**, quante volte è **diverso**. (Incrocia con
   `vsl-study/parlato/<slug>/trascrizione.md`.)

## Vincoli
- **Zero psicologia, zero giudizio di valore.** Non «cattura l'attenzione», non «efficace».
  Solo cosa c'è. Il *perché* è la Fase 4.
- Colori sempre in hex misurati; mai «rosso scuro» senza il numero accanto.
- Console Windows cp1252: nessuna emoji nell'output degli script. Nel Markdown va bene.
- Non scrivere fuori da `vsl-study/visione/<slug>/`.
- Se un frame non si riesce ad aprire, riga con `NON VISTO` e il motivo. Mai inventare.
