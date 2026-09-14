# COPY-F5-gamma — scagnozzo γ («frecce + foto di riferimento», dossier F5)

Ordini di Max (14/09 notte): (1) freccette sotto le 3 card di «Tre sistemi» con spiegazione letterale,
(2) correzione della freccia di Service #02 (Content Factory), (3) le due foto 09/10 in pagina con freccia
verso una nota. Testo esistente delle sezioni toccate: **invariato, parola per parola**. Qui solo le frasi
nuove aggiunte.

## 1 — Tre sistemi (`src/sezioni-rifatte/vsl-v2.tsx`, componente `FrecciaNota`)
Una nota sotto ciascuna delle 3 card, letterale e semplice, come chiesto da Max:

- **Outreach Factory** → «Cioè: ogni mattina il sistema scrive e manda i messaggi ai tuoi potenziali clienti, da solo.»
- **Content Factory** → «Cioè: gli dai un brief, lui produce caroselli, script e caption pronti su Drive.»
- **Second Brain** → «Cioè: l'AI ricorda il tuo business e risponde senza che tu glielo rispieghi.»

## 2 — Service #02 · Content Factory (`src/components/sections/service-deep.tsx`, `ContentDeep`)
Solo correzione di posizione/percorso della freccia F4 (`.c2-freccia*` → `.c2b-freccia*`). Il testo della
nota resta **esattamente quello di F4**, non è stato riscritto:
«Lo so, stiamo andando un po' di fretta… Ti sto già spiegando il mio secondo servizio. Nessuna confusione,
mi raccomando: questo è un altro servizio. Non si tratta più di Outreach.»

## 3 — Le due foto di riferimento (09 rif-pensa, 10 rif-smorfia)

- **`src/sezioni-aggiunte/frase-barrata.tsx`** — foto `rif-smorfia.jpg` a destra della riga barrata «Ti serve
  un altro tool.», con freccia verso la nota:
  «La faccia di chi ha appena pagato il terzo abbonamento del mese.»

- **`src/sezioni-aggiunte/prima-dopo.tsx`** — foto `rif-pensa.jpg` accanto al titolo «La stessa cosa, pagata
  in due modi.», con freccia verso la nota:
  «Sta facendo i conti. Li facciamo insieme qui sotto: 12 mesi, due colonne.»

## Nota tecnica — grana sulle foto (§14 vs ordine esplicito)
Il canone del progetto (`aggiunte-c.css` §14) vieta la grana sopra il soggetto di una foto ("mai grana
sopra il soggetto"). L'ordine di Max per F5 chiede invece esplicitamente "leggera grana" su
`rif-smorfia.jpg`. Ho risolto tenendo la grana molto leggera (opacity .12, stesso rumore di `.c-grana` ma
più debole) così il soggetto resta chiaramente leggibile — compromesso dichiarato, non deciso in silenzio.
Applicata alla stessa classe condivisa (`.f5-rif-fig::after`) anche su `rif-pensa.jpg` per coerenza tra le
due foto (Max non l'aveva chiesta esplicitamente lì, ma l'aveva chiesta "sempre" come legge generale, vedi
memoria "Grana sempre + scritte su foto sempre leggibili").
