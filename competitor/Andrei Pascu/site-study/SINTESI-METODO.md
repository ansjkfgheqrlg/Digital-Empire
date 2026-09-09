---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #metodo #strato-4 #lanci #sintesi
Created: 2026-09-09
Last updated: 2026-09-09
---

# SINTESI DEL METODO — come costruisce, non come appare

**Terzo documento dell'onda G**, e il più difficile: i primi due dicono *cosa* fa (il sistema visivo)
e *cosa scrive* (il sistema di copy). Questo dice **come lavora** — lo strato 4 del dossier 33, il
solo che non si veda guardando le pagine.

Base: **52 pagine catturate e chiuse**, 7 domini, ~85.000 parole di rapporti, il 2026-09-07/09.
Ogni numero qui sotto è contato sul disco. Dove c'è un'inferenza, è scritto che è un'inferenza.

---

## 1. LA REGOLA MADRE: la piattaforma si sceglie dal lavoro, non dal gusto

| Costruzione | Pagine | Altezza media | Keyframes medi | Cosa ci mette dentro |
|---|---|---|---|---|
| **Squarespace** | **44** | 9.081 px | 28 | il negozio permanente: 61 pagine commerciali, 37 articoli, tutte le casse |
| **Artigianale** | **7** | 14.699 px | 14 | i lanci e l'agenzia: `armageddon`, `claude-speedrun`, i 5 pezzi di `apsales.eu` |

Il dato controintuitivo è il secondo: **le pagine che scrive a mano sono più alte del 62% e hanno la
metà delle animazioni.** Su Squarespace 63 `@keyframes` arrivano di serie che lui li usi o no; a mano
ne mette 9, 34, 39 — cioè li sceglie. **La piattaforma regala movimento e toglie controllo; la mano
costa tempo e restituisce decisione.**

E la scelta segue il denaro, non l'estetica:

- **il negozio** (prodotti da 98 a 999 €, molti, che cambiano spesso) → piattaforma, zero manutenzione;
- **un lancio** (una finestra, un prezzo, un link di pagamento) → a mano, controllo totale;
- **l'agenzia B2B** (`apsales.eu`, dove il cliente è un'azienda) → a mano **e con un kit di
  componenti condiviso** (Section-con-tono, Heading, Deck, Card, due bottoni, due evidenziatori,
  Footer): nessuna sezione scrive stili propri.

**La disciplina cresce col valore del cliente**, non col prezzo del prodotto. Il posto più severo
del suo ecosistema non è il corso da 999 €: è la pagina che vende consulenza alle aziende.

---

## 2. Su Squarespace non personalizza quasi niente — e non è pigrizia

Il `custom.css` del negozio — quello che l'ECOSISTEMA chiamava *"l'unica parte sua di questi siti"* —
misura **1.183 byte su 3,6-8,2 MB scaricati per pagina: lo 0,02%**. Sei regole in tutto, e di quelle
**solo due risultano vive** sulle pagine studiate; le altre quattro puntano a elementi che nel DOM
non esistono più.

> **Quindi il valore delle sue 44 pagine di negozio non sta nel codice. Sta nel copy e nella
> sequenza.** Studiare il CSS di quelle pagine sarebbe stato tempo buttato — e per sette giorni il
> piano ha creduto il contrario.

Questo è il primo insegnamento vero per noi: **la personalizzazione visiva su una piattaforma è il
lavoro a più basso rendimento che esista.** Lui non lo fa. Mette il suo tempo dove si decide.

---

## 3. Il lancio: si specchia il negozio, lo si spoglia, si punta tutto a una cassa

Il meccanismo di `armageddon.bsns.it`, misurato:

1. si prendono le pagine prodotto **originali** dal negozio;
2. se ne fa un **mirror statico**, togliendo ogni script della piattaforma — il commento dentro
   `mirror.js` lo dichiara, identico su tutte e quattro le figlie;
3. si sostituisce il bottone-prezzo del prodotto singolo con il **badge «INCLUSO NEL PACCHETTO
   ARMAGEDDON»** (`#bc0807`, lo stesso colore della barra d'acquisto e di nient'altro);
4. **tutte** le pagine puntano a **un solo link Stripe**;
5. la pagina madre tiene l'offerta: 585 € di listino + 199 € di voucher, **venduti a 199 €**.

**Il mirror non è congelato: è mantenuto.** Prova: l'originale sul negozio dice *«E adesso, nel
**2025**…»*, la copia di lancio — catturata **lo stesso giorno** — dice *«nel **2026**»*. Qualcuno ha
aperto l'editor e ha aggiornato **solo la copia**. La pagina che vende tutto l'anno è rimasta
indietro di dodici mesi.

**Costo del metodo, misurato:** un lancio non richiede di scrivere pagine nuove. Richiede di
**copiare, spogliare e ripuntare**. È la ragione per cui può lanciare spesso.

---

## 4. Tutto ciò che si ripete diventa uno stampo

Tre prove indipendenti, tutte misurate:

- **La pre-cassa è un unico stampo.** Nove pagine fra 1.299 e 1.526 px, 28-40 blocchi, 4-5 CTA. Aperte
  a video: cornice identica al pixel, cambia **solo il riquadro centrale**. Sei variabili in tutto —
  nome prodotto, prezzo, colore, porzione colorata del nome, codice sconto (opzionale), testo del
  bottone.
- **I blocchi di copy sono componenti.** *«Lavori da solo? Vale lo stesso. Al posto del team, il
  vincolo sei tu.»* compare identico, carattere per carattere, su `/servizi` e `/consulenza`.
  *«La speranza non è una strategia.»* attraversa **prodotti diversi** (outFunnel e outViral).
- **Le pagine di vendita hanno una formula fissa a undici tappe** — hero, agitazione, prova con
  fonte, metodo, benefici, curriculum, qualificazione negativa, obiezioni, autorevolezza, prezzo
  barrato, FAQ, chiusura — e le deviazioni sono sistematiche, non casuali: al salire del prezzo
  arrivano **più fonti esterne** (0 → 2 → 5), non più obiezioni.

**La regola sotto le tre prove:** lui non riscrive mai da zero ciò che ha già funzionato una volta.
Ha una libreria — di pagine, di blocchi e di frasi — anche se non la chiama così.

---

## 5. Lucida solo dove si convince, e lascia i difetti dove si transita

Questa è la parte che nessuna analisi estetica avrebbe trovato, e per noi vale più delle altre.

**Dove si convince** (pagine di vendita, pagina madre del lancio): tipografia curata, prove, video,
FAQ scritte a mano, animazioni scelte.

**Dove si transita** (gradini, casse, pagine di servizio) — i difetti misurati, tutti veri:

| Difetto | Misura |
|---|---|
| Il nome del prodotto **sbagliato in due modi diversi** | `<title>` dice «Armageggon», l'URL dice «armadeggon» |
| Il funnel di Vendita101 **è rotto** | `/vendita` manda a `/acquista-v101` che è un **404**; la cassa vera (`/vendita101-pre`, 400 €) **non è linkata da nessuna parte** |
| I prezzi sono **immagini con `alt` vuoto** | outEmail, outFunnel, outHeadline — invisibili a un lettore di schermo e ai motori |
| Il prezzo che si paga è **il testo più piccolo** | 14,88 px, meno del corpo delle FAQ (16,5), mentre «Risparmi €585» sta a 81,6 px |
| Lo stesso `og:image` placeholder su tre pagine diverse | targato `lovable.app`, mai sostituito |
| Un campo del calcolatore ROI **non entra nel calcolo** che mostra | `apsales.eu/landing-page` |
| Il link «Recensioni» del piede | punta a `/presto-disponibile` su **tutte e quattro** le pagine-ponte |

**La lettura onesta:** non è sciatteria diffusa, è **una scelta di dove spendere l'attenzione** — e
la scelta ha un costo che lui probabilmente non ha misurato. Un lancio con la pagina di vendita viva
e la cassa irraggiungibile **perde ogni euro che il copy ha guadagnato**, e nessuno se ne accorge,
perché la pagina di vendita funziona benissimo.

> **Per Digital Empire questo è il regalo più grande dello studio.** Non «facciamo pagine belle come
> lui»: *facciamo la parte che lui trascura*. La cassa che risolve, il prezzo leggibile, il numero
> fuori dall'immagine. Sono cinque controlli automatici — costano un pomeriggio — e valgono la
> differenza fra un lancio che incassa e uno che sembra incassare.

---

## 6. La prova sociale ha due regimi, e uno è verificabile

- `/recensioni-andrei-pascu`: **widget Trustpilot vero** — 4,9/5, 98 recensioni, badge «Verificata»
  per singola recensione, nomi reali, filtro per prodotto. Prova esterna, controllabile da chiunque.
- `/recensioni-copywriting-mentorship`: **42 screenshot** caricati a mano, `alt=""`, nessuna fonte
  esterna, zero verificabilità.

**Il regime forte sta sul prodotto d'ingresso, quello debole sul prodotto caro.** Inferenza, non
misura: sul prodotto caro le prove verificabili sono poche, e si compensa col volume di immagini.

---

## 7. Come si muove nel tempo

- Il negozio **non si tocca**: la stessa pagina resta in vendita per anni (il «2025» ancora lì).
- Il lancio **si costruisce sopra**, si spoglia, si mantiene, e vive nella sua finestra.
- Il blog **non è un motore**: 37 articoli veri (non 105 — gli altri 67 erano indici di tag generati
  dalla piattaforma), quasi la metà costruiti su un numero nel titolo.
- L'agenzia B2B è il **cantiere nuovo**: React + TanStack Start, kit condiviso,
  `prefers-reduced-motion` rispettato ovunque. È lì che il suo mestiere sta crescendo.

---

## DELTA ALLA FABBRICA

**CANONE.** Un articolo nuovo, che nasce da §1 di questo documento: *la piattaforma si sceglie dalla
vita del pezzo* — permanente e mutevole → piattaforma; finestra breve con una sola cassa →
artigianale; cliente che è un'azienda → artigianale **con kit condiviso**. È già metà di ADR-023 (due
corsie): questo lo completa con il criterio della **durata**, che ci mancava.

**PATTERN.** `mirror-di-lancio`: prendere pagine prodotto esistenti, spogliarle degli script, puntare
tutto a una cassa unica, sostituire il bottone-prezzo con un badge di inclusione. Due usi già
dimostrati (le quattro figlie di armageddon sono lo stesso pattern applicato quattro volte).

**GATE.** I cinque controlli che nascono dai suoi difetti sono già scritti in ADR-024 (controlli 3-8)
e **il numero 8 è il primo gate obbligatorio dell'ecosistema LANCI**: nessun lancio parte se la
catena dall'annuncio alla cassa non è stata percorsa a macchina.

---

## LE CINQUE COSE DA RUBARE SUBITO

1. **Lo stampo di pre-cassa a sei variabili** — generabile a comando, già pattern nella Fabbrica.
2. **Il mirror di lancio** — lanciare senza scrivere pagine nuove.
3. **La libreria di frasi** — i blocchi di copy che si riusano identici fra prodotti diversi.
4. **Lo sconto dopo la decisione**, mai prima — ma **a scadenza**, non pubblico e permanente come il suo.
5. **Il kit condiviso** delle pagine B2B — nessuna sezione scrive stili propri.

## LE TRE COSE DA FARE MEGLIO DI LUI

1. **La cassa deve risolvere.** Un `404` in fondo al funnel annulla tutto il copy che sta sopra.
2. **Il prezzo si legge.** Cifra pagabile ≥ corpo del testo di servizio, e mai dentro un'immagine.
3. **Le prove si verificano.** Se una testimonianza non è controllabile da un estraneo, non è prova:
   è decorazione.

---

## Connessioni
- [[SINTESI-SISTEMA-VISIVO]] · [[SINTESI-SISTEMA-COPY]] — gli altri due documenti dell'onda G
- [[ECOSISTEMA]] — l'elenco vero e le tre correzioni del 2026-09-09
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano, e la PARTE VI sui lanci
- `company/Memory/decisions/ADR-024-canone-v2-primo-strato.md` — gli otto controlli
- `company/Memory/tasks/TASK-LANCI-20260908-ANATOMIA-ANDREI-PASCU.md` — dove va tutto questo
