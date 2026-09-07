---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #apsales #atlante-visivo #design-system #reference
Created: 2026-09-07
Last updated: 2026-09-07
---

# ATLANTE VISIVO — le tre pagine di servizio di apsales.eu

**Ogni schermata delle tre pagine, con sotto come è fatta.** Misure lette da `scheda.json` di
ciascuna cattura (`18-apsales-servizi`, `19-apsales-landing-page`, `20-apsales-consulenza`),
campionato dal DOM reale; effetti dai file sorgente in `src/`. Tutte le 36 sezioni (5+17+15,
incluse le due varianti di firma ripetuta) sono state aperte una per una con lo strumento di
visione prima di scrivere una sola riga qui sotto.

Questo documento copre **la composizione sezione per sezione** delle tre pagine di servizio. Chi
cerca lo stack (React+TanStack Start), l'inventario degli otto componenti condivisi
(`Ascii`, `RevealFooter`, `StickyCta`, `CallDialog`, `accordion`, `dialog`, `forms.functions`,
`useServerFn`), la verità sul footer a tenda o i quattro difetti misurati nel codice, trova tutto
in [18-20-apsales-servizi-COSTRUZIONE.md](18-20-apsales-servizi-COSTRUZIONE.md), non ripetuto qui.
Il modello di forma è [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md), che copre la pagina radice
con lo stesso taglio di lettura, e [11-armageddon-ATLANTE-VISIVO.md](11-armageddon-ATLANTE-VISIVO.md).

> **Le immagini** vivono in `../capture/18-apsales-servizi/sezioni/`,
> `../capture/19-apsales-landing-page/sezioni/` e `../capture/20-apsales-consulenza/sezioni/`.
>
> **`/servizi`**: 4229px, 5 sezioni, **4 firme distinte** (i=1 hero e i=4 CTA finale condividono
> la stessa firma di layout).
> **`/landing-page`**: 16.040px, 17 sezioni, **17 firme — tutte distinte, il 100%**.
> **`/consulenza`**: 16.832px, 15 sezioni, **14 firme distinte** (i=5 e i=8 condividono la stessa
> firma, sono la stessa continuazione di contenuto spezzata in due blocchi DOM).
>
> Palette di sfondo comune alle tre pagine (nomi dal CSS, HEX dal dossier 13): `bg-void` =
> `#0a0a0b` · `bg-pitch` = `#111111` · `bg-paper` = `#f9f9f9` · unico colore d'azione `#0062ff`.

---

# PARTE 1 — `/servizi` (4229px, 5 sezioni, 4 firme)

## TAVOLA S1 — L'hub "Facciamo solo due cose. Per scelta." (e la sua variante, S4)
![sezione 01](../capture/18-apsales-servizi/sezioni/01-facciamo-solo-due-cose-per-scelta.png)

**Ruolo:** hero della pagina indice — smista il visitatore verso una delle due offerte, senza vendere nessuna delle due qui.

| Campo | Valore |
|---|---|
| y / altezza | 65px / 684px — **16,2%** della pagina |
| Sfondo | `oklch(0.1448 0.002 285)` = `#0a0a0b` (bg-void) |
| Heading | H1 "Facciamo solo due cose. Per scelta." |
| Blocchi di testo | 11 |
| Parole | 39 |
| Media | 0 |
| CTA | 0 (i due blocchi sotto sono anchor di scroll, non veri CTA con `href` esterno) |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|-\|C\|3` — **gruppo 1, rappresentante** |

**Composizione.** H1 su tre righe bianche con "*due cose*" in corsivo, poi due colonne separate da
filetto verticale: "Landing page" con sottotitolo "La pagina che riceve il tuo traffico." e
"Consulenza" con "Un'ora di problem solving con Andrei Pascu." In fondo, la riga di qualificazione:
"Solo per B2B e B2B SaaS che investono **da €5.000 a €100.000 al mese** in ads" — identica, parola
per parola, a quella misurata sulla pagina radice (dossier 13).

### La variante — S4 (stessa firma, non rappresentante)
![sezione 04](../capture/18-apsales-servizi/sezioni/04-dove-stai-perdendo-conversioni.png)

Sezione i=4, y=2407 h=640 (**15,1%**), heading H1 "Dove stai perdendo conversioni?" — **stessa
firma esatta** (`section|relative.overflow-hidden.bg-void|2|-|C|3`, gruppo 1) della Tavola S1: due
colonne di CTA affiancate ("Voglio rifare la landing" in blu pieno, "Voglio una consulenza" a
contorno), zero paragrafo lungo. È il bivio di chiusura pagina, stessa gabbia del bivio di apertura.

**Effetti attivi (entrambe).** Nessuno oltre al colore. Nessuna maschera o blend qui: le sezioni
`Ascii` del sito compaiono altrove (dossier 13), non su questa pagina indice.

**Perché è costruita così.** Aprire e chiudere `/servizi` con **la stessa identica firma di
layout** (bivio a due colonne su bg-void) non è un caso: la pagina è pensata come un imbuto a
clessidra — entra il visitatore indeciso, esce con una delle due scelte già fatta, e la ripetizione
strutturale (stessa gabbia, contenuto diverso) rinforza il messaggio "hai solo due strade" senza
doverlo ripetere a parole.

---

## TAVOLA S2 — Il riquadro "Landing page."
![sezione 02](../capture/18-apsales-servizi/sezioni/02-landing-page.png)

**Ruolo:** vendita sintetica del primo servizio, con metrica e CTA diretta.

| Campo | Valore |
|---|---|
| y / altezza | 749px / 845px — **20,0%**, la sezione più alta di `/servizi` insieme a S3 |
| Sfondo | `oklch(0.1776 0 0)` = `#111111` (bg-pitch) |
| id | `landing` |
| Heading | H2 "Landing page." (corsivo) |
| Blocchi di testo | 11 |
| Parole | 67 |
| Media | 1 — illustrazione ASCII di un laptop, 320×320 circa |
| CTA | 1 — "Voglio rifare la pagina →" (blu pieno) |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|M\|C\|4` — gruppo 2, rappresentante |

**Composizione.** Titolo in corsivo, sottotitolo "Rifacciamo la pagina che riceve il tuo
traffico.", tre righe separate da filetti orizzontali (metodo di misura, tempo di consegna,
garanzia gratuita), CTA blu, e a destra un'illustrazione a puntini bianchi stile ASCII di un
laptop aperto con schermo triangolare (stessa tecnica `Ascii` di `mix-blend-screen` +
`contrast(1.3) brightness(1.45)` misurata sul dossier 13). Sotto l'illustrazione, due dati chiave
in cifre: "Tempo medio di go live — 25 giorni" e "Prezzo — Su preventivo, dopo l'audit", più un
secondo CTA blu "Prenota la consulenza →" (sovrapposto in basso a destra, probabile `StickyCta`).

**Effetti attivi.** `Ascii` sul laptop (blend screen + boost) — identico al pattern osservato su
tutte le altre pagine dell'ecosistema.

**Perché è costruita così.** Il prezzo dichiarato come "su preventivo, dopo l'audit" invece di una
cifra fissa **non nasconde** il costo per ambiguità: lo lega esplicitamente a un passo procedurale
(l'audit) che il cliente deve prima attraversare — coerente con "prima misuriamo, poi scriviamo"
del corpo testo, un posizionamento dati-prima-di-tutto ripetuto ovunque nel copy di questa agenzia.

---

## TAVOLA S3 — Il riquadro "Consulenza."
![sezione 03](../capture/18-apsales-servizi/sezioni/03-consulenza.png)

**Ruolo:** vendita sintetica del secondo servizio, con prezzo fisso ben visibile.

| Campo | Valore |
|---|---|
| y / altezza | 1594px / 813px — **19,2%** |
| Sfondo | `oklch(0.1448 0.002 285)` = `#0a0a0b` (bg-void) |
| id | `consulenza` |
| Heading | H2 "Consulenza." (corsivo) |
| Blocchi di testo | 22 |
| Parole | 70 |
| Media | 0 |
| CTA | 1 — "Fai una consulenza →" (blu pieno) |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|C\|4` — gruppo 3, rappresentante |

**Composizione.** Titolo, sottotitolo "Un'ora di problem solving con Andrei Pascu.", tre righe
descrittive ("Un solo problema da risolvere. Non dieci.", "Esci con un piano a step per il
trimestre...", "Teoria dei vincoli. Niente motivazione, solo decisioni.") e una frase finale con
link inline in blu "il vincolo sei tu" per chi lavora da solo. A destra, un riquadro bordato in blu
(unico bordo colorato della pagina) con "60 minuti, 1:1", il prezzo **€610** in cifre enormi, "IVA
inclusa", "Cosa ti resta — Registrazione + piano in PDF", e il CTA.

**Effetti attivi.** Il riquadro prezzo ha un bordo blu pieno (`border: 1px solid` blu, misurato
visivamente) — l'unico elemento della pagina con un bordo a colore, un modo di isolare visivamente
"questa è la cosa che si paga" senza usare un fondo diverso.

**Perché è costruita così.** A differenza della card "Landing page" (prezzo su preventivo), qui il
prezzo è **una cifra fissa e visibile** (€610): la consulenza ha un costo fisso perché è un
prodotto standardizzato (un'ora, un output), mentre la landing page varia per ambito del progetto
— la differenza di trattamento del prezzo comunica implicitamente la differenza di natura fra i due
servizi, senza doverlo spiegare a parole.

---

## TAVOLA S5 — Il footer
![sezione 05](../capture/18-apsales-servizi/sezioni/05-footer.png)

**Ruolo:** chiusura pagina — qui catturato nel suo stato "non rivelato".

| Campo | Valore |
|---|---|
| y / altezza | 3048px / 1182px — **27,9%**, la sezione più alta dell'intera pagina `/servizi` |
| Sfondo (misurato dal DOM) | `transparent` |
| tag | `footer` (non `section`) |
| Heading | nessuno |
| Blocchi di testo | 19 |
| Parole | 32 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `footer\|relative\|2\|M\|-\|6` — gruppo 5, rappresentante |

**Composizione.** Nello screenshot: il wordmark "APsales" in blu pieno su fondo nero, nella parte
alta dell'inquadratura; il resto appare vuoto. **Identica** alla Tavola 14 del dossier 13
(pagina radice) e alle sezioni-footer di landing-page e consulenza qui sotto — stesso componente
`RevealFooter`, stesso comportamento a tenda già chiarito per intero nel dossier COSTRUZIONE.

**Perché è costruita così.** Il footer occupa **oltre un quarto dell'altezza totale** di
`/servizi` (27,9%, la percentuale più alta fra tutte le sezioni-footer misurate in questo studio,
proprio perché la pagina ospite è la più corta delle tre — 4229px contro i 16.000+ delle altre
due). Non è un footer "cresciuto": è lo stesso identico componente a tenda (`h-screen`, un intero
viewport) che su pagine lunghe passa quasi inosservato in proporzione e qui invece pesa
visibilmente sul totale — un promemoria che le percentuali vanno sempre lette insieme al valore
assoluto, non da sole.

---

# PARTE 2 — `/landing-page` (16.040px, 17 sezioni, 17 firme — tutte distinte)

## TAVOLA L1 — L'hero "Il traffico lo paghi con le ads"
![sezione 01](../capture/19-apsales-landing-page/sezioni/01-il-traffico-lo-paghi-con-le-ads-ma.png)

**Ruolo:** hero specifico del servizio, con doppia CTA (azione diretta / calcolo del guadagno).

| Campo | Valore |
|---|---|
| y / altezza | 65px / 885px — **5,5%** della pagina |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H1 "Il traffico lo paghi con le ads. Ma poi il tuo sito lo *perde*." |
| Blocchi di testo | 9 |
| Parole | 55 |
| Media | 0 |
| CTA | 2 — "Rifai la tua landing →" (blu pieno) · "Quanto puoi guadagnare" (contorno) |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|-\|C\|4` — gruppo 1, rappresentante |

**Composizione.** H1 con "perde" in corsivo, sottotitolo con due parole in grassetto
("**statistica**" e "**persuasione creativa**"), riga di posizionamento ("Le landing page più
persuasive in Italia, solo per B2B e SaaS."), due CTA affiancate, e sotto due mini-card
affiancate: "Costo — ↓ più basso" (bianco) e "Risultati — ↑ più alti" (blu).

**Effetti attivi.** Nessuno oltre al colore delle frecce.

**Perché è costruita così.** Il secondo CTA ("Quanto puoi guadagnare") non porta a un modulo di
contatto: **rimanda al calcolatore interattivo** più avanti nella stessa pagina (Tavola L6) — un
anchor-link interno, non un'uscita. Offrire subito nell'hero un percorso "gioca coi numeri prima
di decidere" abbassa l'attrito per chi non è ancora pronto a lasciare un contatto.

---

## TAVOLA L2 — La riga di qualificazione minimale
![sezione 02](../capture/19-apsales-landing-page/sezioni/02-section.png)

**Ruolo:** filtro d'ingresso silenzioso — una sola frase, nessun titolo.

| Campo | Valore |
|---|---|
| y / altezza | 950px / 393px — **2,4%**, fra le più basse della pagina |
| Sfondo | `#111111` (bg-pitch) |
| Heading | nessuno |
| Blocchi di testo | 1 |
| Parole | 29 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|2` — gruppo 2, rappresentante |

**Composizione.** Un solo paragrafo centrato: "Siamo AP Sales, un'agenzia di CRO specializzata nel
**capire cosa si può fare per ottenere più risultati con il proprio marketing** usando la scienza e
l'arte della persuasione etica." — parola per parola identico al manifesto della pagina radice
(Tavola 4 del dossier 13).

**Effetti attivi.** Nessuno: solo tipografia, come nell'originale.

**Perché è costruita così.** Riusare **verbatim** il paragrafo-manifesto della home su una pagina
di servizio specifica dimostra che il posizionamento di marca (chi siamo, come lavoriamo) non
viene riscritto per ogni pagina: è un blocco di identità fisso che compare ovunque serva ancorare
il lettore al brand, indipendentemente dal servizio che sta guardando in quel momento.

---

## TAVOLA L3 — Il diagramma "alcuni comprano / alcuni non comprano"
![sezione 03](../capture/19-apsales-landing-page/sezioni/03-section.png)

**Ruolo:** visualizzazione del problema di base — perché il traffico pagato non basta.

| Campo | Valore |
|---|---|
| y / altezza | 1343px / 692px — **4,3%** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | nessuno |
| Blocchi di testo | 6 |
| Parole | 18 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|3` — gruppo 3, rappresentante |

**Composizione.** Un riquadro bordato con tre caselle in sequenza verticale: "Spendi soldi" →
freccia → "I tuoi potenziali clienti vedono le tue sponsorizzate" → biforcazione a due frecce
diagonali verso "alcuni comprano" (bordo verde) e "alcuni non comprano" (bordo rosso).

**Effetti attivi.** Nessuno oltre al colore dei bordi (verde/rosso), unico uso di rosso su tutta la
pagina — segnale, non decorazione.

**Perché è costruita così.** È l'unico diagramma di flusso vero e proprio (non un elenco numerato)
di tutta la pagina: la biforcazione visualizza il punto esatto dove il funnel si spacca in due
esiti, rendendo tangibile in un'immagine quello che il testo dovrebbe altrimenti spiegare in due
frasi — un caso di "un'immagine al posto di dieci righe" applicato con precisione chirurgica.

---

## TAVOLA L4 — Il manifesto "Il nostro lavoro è aumentare quante persone comprano."
![sezione 04](../capture/19-apsales-landing-page/sezioni/04-il-nostro-lavoro-aumentare-quante.png)

**Ruolo:** riposizionamento — sposta il problema da "generare traffico" a "convertirlo".

| Campo | Valore |
|---|---|
| y / altezza | 2035px / 609px — **3,8%** |
| Sfondo | `#111111` (bg-pitch) |
| Heading | H2 "Il nostro lavoro è aumentare quante persone **comprano**." |
| Blocchi di testo | 4 |
| Parole | 53 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|3` — gruppo 4, rappresentante |

**Composizione.** Titolo con "comprano" in corsivo, sottotitolo ("Perché «semplicemente spendi di
più in ads» non è sempre la risposta."), due paragrafi che spiegano che il traffico non è il
collo di bottiglia ("chiunque può pagare Meta") ma la conversione lo è.

**Effetti attivi.** Nessuno.

**Perché è costruita così.** Nominare esplicitamente l'obiezione più ovvia del cliente
("semplicemente spendi di più in ads") e smontarla in due righe prima ancora di proporre la
soluzione è la stessa disciplina di disinnesco preventivo osservata nella tabella comparativa
della home page (dossier 13): l'obiezione va nominata dall'agenzia, non lasciata al cliente.

---

## TAVOLA L5 — Il dato "da 2 a 3,5%"
![sezione 05](../capture/19-apsales-landing-page/sezioni/05-section.png)

**Ruolo:** promessa quantificata, cifra centrale come protagonista visivo.

| Campo | Valore |
|---|---|
| y / altezza | 2644px / 756px — **4,7%** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | nessuno |
| Blocchi di testo | 6 |
| Parole | 23 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|4` — gruppo 5, rappresentante |

**Composizione.** Un riquadro bordato con "da **2** a **3,5%**" in cifre enormi (il "2" in grigio
opaco, il "3,5%" in blu pieno, contrasto di peso visivo fra valore di partenza e valore
d'arrivo), sottotitolo "la percentuale di persone che agisce dopo aver visto il tuo sito.", e sotto
due colonne separate da filetto verticale: "Più persone ti contattano e comprano." / "Spendi meno
per acquisizione."

**Effetti attivi.** Nessuno oltre al contrasto cromatico fra i due numeri.

**Perché è costruita così.** Colorare il numero di partenza in grigio spento e quello di arrivo in
blu pieno (il colore-azione del brand) fa leggere la cifra come una **transizione di stato**, non
come due dati indipendenti — un trucco tipografico minimo che comunica movimento senza animazione.

---

## TAVOLA L6 — Il calcolatore ROI "Fai due conti."
![sezione 06](../capture/19-apsales-landing-page/sezioni/06-fai-due-conti.png)

**Ruolo:** strumento interattivo — il pattern data-driven più rilevante della pagina.

| Campo | Valore |
|---|---|
| y / altezza | 3400px / 805px — **5,0%** |
| Sfondo | `#111111` (bg-pitch) |
| id | `calcolo` |
| Heading | H2 "Fai due conti." |
| Blocchi di testo | 9 |
| Parole | 43 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|4` — gruppo 6, rappresentante |

**Composizione.** Titolo, sottotitolo, un riquadro con due campi numerici editabili — "Spesa ads
mensile (€)" (default 3000) e "Acquisti al mese" (default 60) — e sotto, in blu grande, l'output
"**+30** acquisti extra al mese" con la nota in piccolo "Assunzione: conversion rate 2,75% →
4,13% (+50%), stesso budget."

**Effetti attivi.** Stato React minimo (due `useState`) che ricalcola l'output a ogni digitazione
— nessuna animazione, il ricalcolo è istantaneo.

**Perché è costruita così — e il suo limite reale.** Letto per intero nel file sorgente
(`09-landing-page-CRAikniJ.js`, dettaglio nel dossier COSTRUZIONE), l'output è calcolato **solo**
da `Math.round(acquisti * 0.5)`: il campo "Spesa ads mensile" non entra mai nella formula, pur
avendo lo stesso peso grafico dell'altro campo. Non è un inganno — l'assunzione a budget costante
è dichiarata nella nota in piccolo — ma visivamente i due input sembrano entrambi determinanti, e
solo leggendo il corpo minuscolo sotto si scopre che uno dei due è di solo contesto. **Il
meccanismo che vale imitare è il calcolo esplicito e immediato**; il difetto da non copiare è la
parità visiva fra un campo che pesa e uno che non pesa.

---

## TAVOLA L7 — Il separatore minimale "indovinare / numeri & persuasione"
![sezione 07](../capture/19-apsales-landing-page/sezioni/07-section.png)

**Ruolo:** transizione di un solo respiro fra il calcolatore e il processo.

| Campo | Valore |
|---|---|
| y / altezza | 4205px / 402px — **2,5%**, fra le più basse della pagina |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | nessuno |
| Blocchi di testo | 3 |
| Parole | 5 |
| Media | 0 |
| CTA | 0 (uno `StickyCta` "Rifai la tua landing" è visibile in overlay, non conteggiato come CTA di questa sezione) |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|2` — gruppo 7, rappresentante |

**Composizione.** Al centro, "indovinare" in rosso barrato (`text-decoration: line-through`) e
sotto, con una spunta blu, "**numeri & persuasione**" in bianco/grassetto — cinque parole in
tutto, nessun paragrafo.

**Effetti attivi.** La barratura sul testo rosso è l'unico uso di testo depennato in tutto lo
studio Andrei Pascu fin qui documentato.

**Perché è costruita così.** Cinque parole bastano quando la composizione fa il lavoro retorico al
posto della sintassi: "indovinare" barrato contro "numeri & persuasione" spuntato è un confronto
completo (metodo scartato vs metodo adottato) senza una sola frase compiuta — la densità
informativa più bassa della pagina (parole:5) coincide qui con un messaggio comunque completo,
perché la forma grafica (barratura+spunta) porta il significato che il testo da solo non porta.

---

## TAVOLA L8 — Il processo in 5 fasi "Come lavoriamo."
![sezione 08](../capture/19-apsales-landing-page/sezioni/08-come-lavoriamo.png)

**Ruolo:** spiegazione del metodo — rende tangibile un servizio altrimenti immateriale.

| Campo | Valore |
|---|---|
| y / altezza | 4607px / 1192px — **7,4%** |
| Sfondo | `#111111` (bg-pitch) |
| Heading | H2 "Come lavoriamo." + 5 sotto-titoli |
| Blocchi di testo | 21 |
| Parole | 82 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|6` — gruppo 8, rappresentante |

**Composizione.** Cinque righe numerate 01-05, ciascuna con numero grande in grigio spento, titolo
in grassetto bianco e una riga di corpo grigio: Installiamo tracciamento compliant (GA4, Meta
Pixel, Clarity) → Guardiamo cosa fanno le persone (heatmap e registrazioni) → Creiamo la nuova
landing sui tuoi numeri → Tracciamo le persone che vedono la pagina (baseline concordata) → Le tue
conversioni aumentano (e se non salgono, si rimette mano gratis).

**Effetti attivi.** Nessuno oltre ai filetti orizzontali che separano ogni fase.

**Perché è costruita così.** L'ultima fase ("Le tue conversioni aumentano") non è un risultato
passivo: la nota "E, a condizioni chiare, se non salgono ci rimettiamo mano. Gratis." la trasforma
in una garanzia incorporata nel processo stesso, non elencata a parte in una sezione "garanzie" —
il rischio del cliente viene assorbito dentro lo step conclusivo del metodo.

---

## TAVOLA L9 — L'offerta "Cosa facciamo."
![sezione 09](../capture/19-apsales-landing-page/sezioni/09-cosa-facciamo.png)

**Ruolo:** dettaglio contrattuale del servizio — cosa è incluso, in chiaro.

| Campo | Valore |
|---|---|
| y / altezza | 5799px / 1019px — **6,4%** |
| Sfondo | `#f9f9f9` — **unica sezione chiara di `/landing-page`** |
| id | `offerta` |
| Heading | H2 "Cosa facciamo." + "Landing Page AP Sales" |
| Blocchi di testo | 16 |
| Parole | 72 |
| Media | 0 |
| CTA | 1 — "Parla con AP Sales →" |
| Firma / gruppo | `section\|scroll-mt-16.theme-paper.bg-paper\|1\|-\|C\|5` — gruppo 9, rappresentante |

**Composizione.** Titolo e sottotitolo centrati su fondo chiaro, poi una card bianca bordata con
"Landing Page AP Sales" e cinque bullet puntati blu (Audit + tracciamento + heatmap del sito
attuale, Analisi statistica competitor/dati/storico/ads, Copy+design+sviluppo, Go live e
collegamento alle campagne, CRO gratuita dopo pubblicazione a condizioni chiare), CTA blu in
fondo alla card.

**Effetti attivi.** Nessuno: è l'unica sezione chiara della pagina, un cambio di registro puro
tramite colore.

**Perché è costruita così.** Passare dal nero al bianco proprio nel momento in cui si elenca cosa
è incluso nel contratto segnala un cambio di funzione (da narrazione a documento) — lo stesso
principio del fondo chiaro unico osservato nella sezione "Piccola agenzia. Standard alti." della
home page (dossier 13, Tavola 10): il chiaro segna sempre un punto di maggiore concretezza/lettura
lenta, non un abbellimento casuale.

---

## TAVOLA L10 — Il form di qualificazione "Parla con AP Sales subito."
![sezione 10](../capture/19-apsales-landing-page/sezioni/10-parla-con-ap-sales-subito.png)

**Ruolo:** raccolta lead — primo punto di contatto reale della pagina.

| Campo | Valore |
|---|---|
| y / altezza | 6818px / 796px — **5,0%** |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `contatto` |
| Heading | H2 "Parla con AP Sales **subito**." |
| Blocchi di testo | 8 |
| Parole | 24 |
| Media | 0 |
| CTA | 4 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|C\|4` — gruppo 10, rappresentante |

**Composizione.** "Subito" in blu, sottotitolo ("Dicci chi sei, ti rispondiamo entro 24 ore."),
tre opzioni a riquadro pieno larghezza impilate verticalmente ("Sono un'azienda B2B" / "Sono una
SaaS" / "Altro") e un quarto CTA blu pieno "Parla con noi →" sotto le tre opzioni.

**Effetti attivi.** Le tre opzioni sono probabilmente radio/select stilizzati come righe cliccabili
a piena larghezza — nessuna icona, solo testo e bordo.

**Perché è costruita così.** Le tre opzioni non fanno una domanda di qualificazione fine
(fatturato, budget, settore): chiedono solo "che tipo di azienda sei" in tre categorie larghissime.
È un form a bassissimo attrito, coerente con la promessa "ti rispondiamo entro 24 ore" — la
qualificazione fine avviene dopo, in chiamata, non nel form stesso.

---

## TAVOLA L11 — Il confronto "AP Sales, o un'altra agenzia?"
![sezione 11](../capture/19-apsales-landing-page/sezioni/11-ap-sales-o-un-altra-agenzia.png)

**Ruolo:** tabella comparativa competitiva — la stessa logica della Tavola 5/9 del dossier 13, qui declinata sul servizio.

| Campo | Valore |
|---|---|
| y / altezza | 7614px / 980px — **6,1%** |
| Sfondo | `#111111` (bg-pitch) |
| Heading | H2 "AP Sales, o un'altra agenzia?" |
| Blocchi di testo | 35 |
| Parole | 73 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|5` — gruppo 11, rappresentante |

**Composizione.** Tabella a due colonne (AP Sales / Altre agenzie) e otto righe: Specializzate in
landing page, Brand stabile e rilevante in italiano, Tecniche ingannevoli nei contenuti (colonna
AP Sales: "No", colonna altre: "Alcune sì"), Modifiche se le performance sono basse ("Sì, più di
70" vs "Solo se paghi"), Specializzate in SaaS e B2B, Capiscono il traffico freddo, Statistica che
puoi controllare, Puoi parlarci ora.

**Effetti attivi.** Nessuno oltre allo sfondo leggermente più chiaro sulla colonna "AP Sales"
(stesso velo blu al 4% già misurato sulla home nel dossier 13).

**Perché è costruita così.** La riga "Modifiche se le performance sono basse" con la cifra "Sì,
più di 70" (non un generico "sì") è la stessa mossa di specificità osservata più volte in questo
studio: un numero preciso, anche piccolo e verificabile solo a parole, pesa di più di un aggettivo
("molte modifiche").

---

## TAVOLA L12 — Il percorso "Cosa succede dopo che ci contatti." (14 tappe)
![sezione 12](../capture/19-apsales-landing-page/sezioni/12-cosa-succede-dopo-che-ci-contatti.png)

**Ruolo:** mappa completa del percorso cliente — la sezione più alta della pagina.

| Campo | Valore |
|---|---|
| y / altezza | 8594px / 2000px — **12,5%, la sezione più alta di `/landing-page`** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H2 "Cosa succede dopo che ci contatti." + 5 sotto-titoli in `headings[]` (14 punti visivi totali) |
| Blocchi di testo | 59 — il valore più alto della pagina |
| Parole | 157 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|10` — gruppo 12, rappresentante |

**Composizione.** Una lista verticale a pallini connessi da una linea continua, con 14 tappe:
Chiamata conoscitiva (24h) → Chiamata di preventivo (se decidi di procedere) → Contratto,
pagamento, fattura → Onboarding → Audit e tracciamento (massimo 10 giorni) → Analisi statistica e
ricerca strategica → Copywriting della pagina → Design della pagina → Sviluppo della pagina →
Approvazione → Go live → Analisi dati → CRO (ottimizzazione) → Consegna finale. Alcune tappe
portano un'etichetta in monospaziato blu ("24H", "SE DECIDI DI PROCEDERE", "MASSIMO 10 GIORNI").

**Effetti attivi.** Nessuno oltre al colore sulle etichette temporali (blu, font monospaziato —
stesso segnale "qui si misura" già osservato sulla home, dossier 13 Tavola 7).

**Perché è costruita così.** Quattordici tappe esplicite, non riassunte in 4-5 fasi macro,
comunicano un processo maturo e ripetibile — più tappe elencate danno l'impressione di un metodo
collaudato, non di improvvisazione, anche se buona parte sono passaggi amministrativi ovvi
(contratto, fattura). È la sezione più lunga in blocchi di testo di tutta la pagina proprio
perché deve fare da "prova di processo" per chi non ha mai comprato niente da quest'agenzia.

---

## TAVOLA L13 — "Tecniche sostenibili." (White Hat / Black Hat)
![sezione 13](../capture/19-apsales-landing-page/sezioni/13-tecniche-sostenibili.png)

**Ruolo:** disclosure etica — differenzia il metodo dell'agenzia dalle tecniche scorrette diffuse nel settore.

| Campo | Valore |
|---|---|
| y / altezza | 10594px / 1170px — **7,3%** |
| Sfondo | `#111111` (bg-pitch) |
| Heading | H2 "Tecniche sostenibili." + "White Hat" + "Black Hat" |
| Blocchi di testo | 29 |
| Parole | 96 |
| Media | 2 — due icone a cappello (bombetta) |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|M\|-\|6` — gruppo 13, rappresentante |

**Composizione.** Due colonne affiancate in un unico riquadro diviso da filetto verticale: "White
Hat" (icona cappello, descrizione positiva) contro "Black Hat" (stessa icona, descrizione negativa
con lista puntata: Timer finti, Numeri aziendali hardcoded, Recensioni finte, Testimonianze
ingannevoli, "E tanto altro"), poi una riga "Noi useremo tecniche di vendita che:" con quattro
punti numerati (Sono compliant / Non danneggiano il tuo brand / Portano lead e clienti più
interessati / Si possono usare sul lungo termine).

**Effetti attivi.** Nessuno oltre al colore (bianco vs grigio spento per differenziare le due
colonne senza usare rosso/verde).

**Perché è costruita così — il meccanismo che vale.** Elencare esplicitamente le tecniche
scorrette usate dai competitor ("timer finti", "recensioni finte") **nomina pubblicamente pratiche
diffuse nel settore CRO/marketing** senza accusare un concorrente specifico: è un modo di
posizionarsi come onesti che non richiede attaccare nessuno per nome, e al tempo stesso pre-educa
il cliente a riconoscere quelle pratiche altrove (rendendolo più scettico verso chi le userà).

---

## TAVOLA L14 — Il manifesto "Hai un buon prodotto. Noi influenziamo la percezione."
![sezione 14](../capture/19-apsales-landing-page/sezioni/14-hai-un-buon-prodotto-noi-influenzi.png)

**Ruolo:** riposizionamento del valore del servizio — dalla pagina alla percezione.

| Campo | Valore |
|---|---|
| y / altezza | 11764px / 900px — **5,6%** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H2 "Hai un buon prodotto. Noi influenziamo la **percezione**." |
| Blocchi di testo | 12 |
| Parole | 49 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|5` — gruppo 14, rappresentante |

**Composizione.** Titolo con "percezione" in corsivo, un riquadro grigliato con al centro la parola
"conversione" bordata, e attorno quattro etichette satellite collegate da frecce puntate ("→
credibilità", "→ velocità", "→ percezione", "→ risultato atteso", "→ pattern comportamentali"),
poi un paragrafo che spiega: "La percezione è cosa pensano le persone. Aumentiamo la percezione di
qualità, velocità e risultati... usando parole, design e tecniche di persuasione etiche e
compliant."

**Effetti attivi.** Griglia di puntini leggerissima sullo sfondo del riquadro (probabile
`bg-dotfield` o `bg-hairgrid`, texture già misurata nel dossier COSTRUZIONE).

**Perché è costruita così.** Il diagramma a stella (un nodo centrale con cinque etichette
satellite) visualizza "conversione" come punto d'arrivo di più leve contemporanee, non di una sola
— coerente con la frase-chiave "usando parole, design e tecniche": tre strumenti diversi che
convergono su un solo risultato, reso visivamente come una rete e non come un elenco lineare.

---

## TAVOLA L15 — Le FAQ statiche (non un accordion)
![sezione 15](../capture/19-apsales-landing-page/sezioni/15-domande-frequenti.png)

**Ruolo:** rimozione delle obiezioni finali — ma qui senza interattività.

| Campo | Valore |
|---|---|
| y / altezza | 12664px / 1615px — **10,1%** |
| Sfondo | `#111111` (bg-pitch) |
| id | `faq` |
| Heading | H2 "Domande frequenti." |
| Blocchi di testo | **1** — un unico blocco di testo per l'intera sezione |
| Parole | 182 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|8` — gruppo 15, rappresentante |

**Composizione.** Titolo, poi otto domande **tutte già aperte e visibili** (non un accordion
cliccabile): Che tipo di accordo offrite? (una tantum, riduzione rischio) → Quanto tempo passerà
dall'accordo al go live? (25 giorni in media) → Cosa succede se le conversioni non aumentano?
(rifacciamo gratis) → Offrite altri servizi di marketing? (no, solo landing e CRO) → Potete
costruire sulla mia piattaforma? (sì, con fee aggiuntiva) → Quanto tempo devo impegnare io e il mio
team? (max 5 ore) → Lavorate solo con aziende italiane? (no, anche anglofone) → Con che aziende
lavorate? (B2B/SaaS ≥€5.000/mese in ads).

**Effetti attivi.** Nessuno: nessun chevron, nessun trigger cliccabile visibile nello screenshot.

**Perché è costruita così — e la conseguenza tecnica reale.** Il componente `accordion` (Radix,
9.211 byte) **non è caricato in questa pagina** (assente da `_INDICE.json` di
`19-apsales-landing-page`), pur esistendo la stessa identica sezione "Domande frequenti." su
`/consulenza` come 14 righe cliccabili con accordion vero (Tavola C13 più sotto). Il
`blocchi_testo: 1` conferma dal DOM quello che lo screenshot mostra: qui le risposte sono contenuto
statico sempre visibile — probabilmente pensato solo per lo schema `FAQPage` in JSON-LD ai fini
SEO, non per l'interazione dell'utente. **Due implementazioni diverse della stessa componente di
prodotto sulla stessa build**, non una scelta di design applicata ovunque.

---

## TAVOLA L16 — La CTA finale "Fai convertire il tuo traffico."
![sezione 16](../capture/19-apsales-landing-page/sezioni/16-fai-convertire-il-tuo-traffico.png)

**Ruolo:** chiusura pagina, ultimo invito prima del footer.

| Campo | Valore |
|---|---|
| y / altezza | 14279px / 579px — **3,6%** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H1 "Fai convertire il tuo **traffico**." |
| Blocchi di testo | 4 |
| Parole | 9 |
| Media | 1 — un mirino a puntini |
| CTA | 1 — "Parla con noi →" |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|M\|C\|3` — gruppo 16, rappresentante |

**Composizione.** Titolo con "traffico" in corsivo, CTA blu pieno, e a destra un piccolo mirino
circolare fatto di puntini bianchi (stessa illustrazione radiale già vista sulla card "Consulenza"
della home, dossier 13 Tavola 6) — qui isolato, senza testo di supporto.

**Effetti attivi.** Probabile maschera radiale sui bordi del mirino (`radial-gradient`), coerente
con gli altri usi dell'illustrazione nello stesso ecosistema.

**Perché è costruita così.** Nove parole in tutto per l'ultima sezione prima del footer: dopo
avere attraversato 15 sezioni di argomentazione, il messaggio finale non ha bisogno di aggiungere
altro — solo un'ultima chiamata all'azione, breve per non affaticare chi è arrivato fin qui.

---

## TAVOLA L17 — Il footer
![sezione 17](../capture/19-apsales-landing-page/sezioni/17-footer.png)

**Ruolo:** chiusura — identico comportamento a tenda già chiarito.

| Campo | Valore |
|---|---|
| y / altezza | 14858px / 1182px — **7,4%** |
| Sfondo | `transparent` |
| Heading | nessuno |
| Blocchi di testo | 19 |
| Parole | 32 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `footer\|relative\|2\|M\|-\|6` — gruppo 17, rappresentante |

**Composizione.** Identica alla Tavola S5: wordmark "APsales" blu su nero, stesso componente
`RevealFooter`. Su una pagina 3,8 volte più lunga di `/servizi`, la stessa sezione-footer pesa
7,4% invece di 27,9%: **stesso componente, peso percentuale molto diverso** in funzione della
lunghezza della pagina ospite.

**Perché è costruita così.** Vedi nota nella Tavola S5: un componente a viewport fisso
(`h-screen`) mantiene un peso assoluto costante indipendentemente dalla pagina, ma il suo peso
relativo cambia radicalmente — utile ricordarlo quando si confrontano percentuali fra pagine di
lunghezza diversa.

---

# PARTE 3 — `/consulenza` (16.832px, 15 sezioni, 14 firme)

## TAVOLA C1 — L'hero "Consulenza di problem solving con Andrei Pascu"
![sezione 01](../capture/20-apsales-consulenza/sezioni/01-consulenza-di-problem-solving-con.png)

**Ruolo:** hero del servizio a pagamento diretto — prezzo visibile fin dalla prima schermata.

| Campo | Valore |
|---|---|
| y / altezza | 65px / 1005px — **6,0%** della pagina |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H1 "Consulenza di *problem solving* con Andrei Pascu" |
| Blocchi di testo | 8 |
| Parole | 48 |
| Media | 1 — illustrazione ASCII di un cavaliere con ascia |
| CTA | 1 — "Fai una consulenza adesso →" |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|M\|C\|5` — gruppo 1, rappresentante |

**Composizione.** H1 su tre righe con "problem solving" in corsivo, sottotitolo, CTA blu pieno, e a
destra l'illustrazione ASCII di un cavaliere templare con ascia sollevata (stessa famiglia grafica
del "biglietto" di claude-speedrun.com e delle illustrazioni di armageddon.bsns.it — coerenza
iconografica in tutto l'ecosistema Andrei Pascu). Sotto l'illustrazione, tre dati chiave: "Formato
— 60 minuti, 1:1", "Output — Piano in step + registrazione", "Prezzo — €610 IVA inclusa" — il
prezzo compare **già nell'hero**, non solo nella sezione offerta più avanti.

**Effetti attivi.** `Ascii` sul cavaliere (blend screen + boost, `contrast(1.35) brightness(1.5)`
misurato nel dossier COSTRUZIONE — leggermente più forte del boost standard, terza intensità
osservata nell'ecosistema).

**Perché è costruita così.** Mostrare il prezzo **subito**, nell'hero, invece di farlo scoprire
dopo un lungo scroll (come su `/landing-page`, dove il prezzo compare solo alla sezione offerta a
metà pagina) è coerente con la natura del prodotto: una consulenza da €610 pagata direttamente
online non ha bisogno di essere "riscaldata" a lungo, il cliente che clicca sa già cosa sta per
vedere.

---

## TAVOLA C2 — Lo schema "Input → accadono cose → Output"
![sezione 02](../capture/20-apsales-consulenza/sezioni/02-qualsiasi-cosa-tu-faccia-hai-un-pr.png)

**Ruolo:** introduzione del framework — ogni attività è un processo, anche se non lo chiami così.

| Campo | Valore |
|---|---|
| y / altezza | 1070px / 644px — **3,8%** |
| Sfondo | `#111111` (bg-pitch) |
| id | `processo` |
| Heading | H2 "Qualsiasi cosa tu faccia… Hai un *processo*." |
| Blocchi di testo | 23 |
| Parole | 13 — pochissimo testo, densità 2 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|3` — gruppo 2, rappresentante |

**Composizione.** Titolo con "processo" in corsivo, e sotto un diagramma minimale a tre caselle:
"Input" (testo grande, nessun riquadro) → freccia tratteggiata → "accadono cose" (dentro un
riquadro tratteggiato, testo grigio spento, deliberatamente vago) → freccia tratteggiata →
"Output" (testo grande, nessun riquadro).

**Effetti attivi.** Nessuno.

**Perché è costruita così.** La casella centrale "accadono cose" — scritta proprio così, in modo
vago e in un riquadro tratteggiato invece che pieno — è l'unico elemento intenzionalmente
indefinito della sezione: rappresenta la scatola nera del processo del cliente, quella che la
consulenza serve ad aprire. Il contrasto fra "Input"/"Output" (definiti, testo pieno) e la scatola
di mezzo (vaga, tratteggiata) comunica il problema meglio di una frase esplicita.

---

## TAVOLA C3 — Il selettore diagnostico "E ogni processo ha un limite"
![sezione 03](../capture/20-apsales-consulenza/sezioni/03-e-ogni-processo-ha-un-limite-che-g.png)

**Ruolo:** strumento interattivo — la Teoria dei Vincoli resa componente cliccabile.

| Campo | Valore |
|---|---|
| y / altezza | 1714px / 1155px — **6,9%** |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `vincolo` |
| Heading | H2 "E ogni processo ha un limite che gli impedisce di *crescere*." |
| Blocchi di testo | 44 |
| Parole | 95 |
| Media | 0 |
| CTA | 6 — le sei voci selezionabili del menu |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|C\|6` — gruppo 3, rappresentante |

**Composizione.** Sottotitolo esplicativo ("Ogni catena si rompe nel punto più debole..."), poi un
riquadro a due colonne: a sinistra un menu verticale di sei voci (Funnel di acquisizione — attiva,
sfondo blu scuro — Campagna Meta Ads, Content organico, Onboarding cliente, Retention, Sistema
referral), a destra il dettaglio della voce selezionata: cinque tappe del funnel (Identifica il
problema, Crea lead magnet, **Landing page** evidenziata in grassetto con etichetta blu "il
vincolo", Sequenza nurture, Sales call) e una frase di chiusura ("Il traffico c'è già. È la pagina
che lo butta via..."). Nota in piccolo: "Esempi illustrativi. Il tuo vincolo si trova in call."

**Effetti attivi.** Cambio di stato del menu (voce attiva evidenziata in blu scuro) — stato React
minimo (un indice selezionato), nessuna animazione di transizione rilevata.

**Perché è costruita così — il meccanismo che vale.** La struttura dati dietro questo componente
(`{title, steps:[...], constraint:<indice>, effect:"..."}`, dettagliata nel dossier COSTRUZIONE) è
la Teoria dei Vincoli di Goldratt applicata in codice: **un solo punto di ogni catena può essere il
vincolo**, e lo strumento lo dimostra lasciando esplorare sei catene diverse mentre segnala sempre
un solo anello debole per volta. È un piccolo motore che qualifica il visitatore mentre gli mostra
qualcosa, non un elenco statico di bullet — pattern riusabile per qualunque pagina di servizio
diagnostico.

---

## TAVOLA C4 — La bio "Ma chi è Andrei Pascu?"
![sezione 04](../capture/20-apsales-consulenza/sezioni/04-ma-chi-andrei-pascu.png)

**Ruolo:** autorità personale — stesso ruolo della Tavola 16 di claude-speedrun, qui su fondo chiaro.

| Campo | Valore |
|---|---|
| y / altezza | 2869px / 1233px — **7,3%** |
| Sfondo | `#f9f9f9` — unica sezione chiara insieme a C10 |
| id | `andrei` |
| Heading | H2 "Ma chi è *Andrei Pascu*?" |
| Blocchi di testo | 10 |
| Parole | 65 |
| Media | 1 — foto ritratto |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.theme-paper.bg-paper\|1\|M\|-\|6` — gruppo 4, rappresentante |

**Composizione.** A sinistra, testo biografico in tre tappe ("Prima — Copywriting", "Poi —
Marketing generale", "Oggi — CRO e marketing statistico") con link inline "formazione." verso il
ramo formativo; a destra, foto ritratto reale (maglietta nera, catena d'oro, auricolari bianchi) —
**stessa foto, diverso crop**, di quella usata sulla home page (dossier 13, Tavola 10). Sotto la
foto, quattro cifre in colonna: 250k Follower organici, 1.500 Clienti formazione, 100+ Clienti
agenzia, 3.900+ Ordini processati.

**Effetti attivi.** Nessuno: fondo chiaro puro, coerente con le altre sezioni "chi siamo" di
questo ecosistema.

**Perché è costruita così.** Le quattro cifre qui differiscono leggermente da quelle della home
(dove comparivano "250.000 follower, 100+ clienti, 1.500+ professionisti formati" in tre voci, non
quattro): su `/consulenza` si aggiunge **"3.900+ Ordini processati"**, una metrica di volume
transazionale assente altrove — coerente col fatto che questa è l'unica pagina di servizio che
vende un prodotto a pagamento diretto e immediato, dove il volume di transazioni pesa come prova
più della fama social.

---

## TAVOLA C5 — "Scopri e/o rimuovi il tuo vincolo." (e la sua continuazione, C8)
![sezione 05](../capture/20-apsales-consulenza/sezioni/05-scopri-e-o-rimuovi-il-tuo-vincolo.png)

**Ruolo:** la sezione più densa di parole della pagina — spiega il doppio taglio dell'essere l'imprenditore del proprio business.

| Campo | Valore |
|---|---|
| y / altezza | 4102px / 1695px — **10,1%** |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `sblocco` |
| Heading | H2 "Scopri e/o rimuovi il tuo *vincolo*." |
| Blocchi di testo | 19 |
| Parole | 184 — **la più alta della pagina** |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|8` — **gruppo 5, rappresentante** |

**Composizione.** Sottotitolo con parte in blu ("Ogni business ha un limite. Quel limite **può
essere rimosso**."), un paragrafo di apertura, due blocchi contrapposti con filetto verticale
colorato (grigio per "Da una parte è un vantaggio" — conoscere bene il proprio business dà
decisioni veloci; blu per "Dall'altra è uno svantaggio" — impedisce una prospettiva oggettiva),
poi "È il motivo per cui più di **100 imprenditori** hanno deciso di investire in 1 ora di
consulenza con Andrei Pascu.", "Andrei ti aiuterà a:" con tre righe separate da filetti (trovare il
vincolo, ridurre la confusione a un problema solo, sviluppare un piano attuabile nel trimestre) e
la nota "Finché rientra in un'area di competenza di Andrei Pascu." — un CTA fluttuante "Prenota la
consulenza" in overlay (probabile `StickyCta`).

### La continuazione — C8 (stessa firma, non rappresentante)
![sezione 08](../capture/20-apsales-consulenza/sezioni/08-section.png)

Sezione i=8, y=8142 h=1531 (**9,1%**), senza heading proprio (`headings: []`) — **stessa firma
esatta** (`section|scroll-mt-16.bg-void|1|-|-|8`, gruppo 5) della Tavola C5, e visivamente la
prosecuzione naturale dei tre riquadri-citazione di Andrei Pascu in prima persona (vedi Tavola C7,
subito prima nel DOM): tre virgolettati corsivi firmati "Andrei Pascu" (sulla ghigliottina che
scende di un centimetro al giorno, sul lavorare 9-10-11 ore per non vedere risultati, sul
distrarsi facendo altro per paura di affrontare il vero problema), chiusi da "È per quello che
Andrei offre... il servizio di consulenza" e "La filosofia di Andrei? Priorità assoluta sui propri
clienti." 9 blocchi di testo, 147 parole.

**Effetti attivi (entrambe).** Nessuno oltre al colore dei filetti verticali.

**Perché è costruita così.** Il DOM tratta queste due sezioni come **due istanze dello stesso
contenitore vuoto di stile** (stessa firma) usato per contenuti diversi ma affini per registro
(entrambi blocchi di testo lunghi, riflessivi, in prima persona o quasi) — la stessa gabbia
strutturale regge sia l'argomentazione logica (C5) sia la testimonianza emotiva diretta (C8),
segno che la "sezione a solo testo su bg-void" è un contenitore neutro riusabile per qualunque
paragrafo lungo, non legato a un contenuto specifico.

---

## TAVOLA C6 — Il selettore sintomi "I soldi si bloccano in uno di questi punti."
![sezione 06](../capture/20-apsales-consulenza/sezioni/06-i-soldi-si-bloccano-in-uno-di-ques.png)

**Ruolo:** secondo strumento diagnostico interattivo — stessa logica del selettore vincolo, applicata ai sintomi invece che alle fasi.

| Campo | Valore |
|---|---|
| y / altezza | 5797px / 1022px — **6,1%** |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `diagnosi` |
| Heading | H2 "I soldi si bloccano in uno di questi punti." |
| Blocchi di testo | 27 |
| Parole | 72 |
| Media | 0 |
| CTA | 4 — le quattro voci selezionabili |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|C\|5` — gruppo 6, rappresentante |

**Composizione.** Stesso schema a due colonne del selettore vincolo (Tavola C3): menu a sinistra
con quattro voci (Non arriva gente dal marketing — attiva, La gente arriva ma non compra, Hai un
team ma non funziona, Non sai cosa fare), dettaglio a destra con elenco puntato blu dei sintomi
specifici della voce attiva (Fai le ads ma i CPL sono troppo alti, I lead sono pochi, I lead che
arrivano sono fuori target, Pubblichi ma non ti scrive nessuno, "E altro...") e chiusura "Lavori da
solo? Vale lo stesso. Al posto del team, **il vincolo sei tu**."

**Effetti attivi.** Stesso pattern di stato del menu della Tavola C3 (voce attiva evidenziata).

**Perché è costruita così.** Comparendo **dopo** il selettore vincolo (C3) e non prima, questo
secondo strumento non introduce un concetto nuovo: **applica lo stesso framework appena imparato**
(un solo anello debole per catena) a un dominio più concreto e riconoscibile (dove si bloccano i
soldi) — una progressione didattica dal concetto astratto all'esempio pratico, non due strumenti
indipendenti messi a caso.

---

## TAVOLA C7 — La statistica shock "4,1 milioni di dichiaranti IVA"
![sezione 07](../capture/20-apsales-consulenza/sezioni/07-nel-2024-ci-sono-stati-4-1-milioni.png)

**Ruolo:** normalizzazione della difficoltà — "non sei tu, è la statistica".

| Campo | Valore |
|---|---|
| y / altezza | 6819px / 1323px — **7,9%** |
| Sfondo | `#111111` (bg-pitch) |
| id | `contesto` |
| Heading | H1 "Nel 2024 ci sono stati 4,1 milioni di dichiaranti IVA in Italia." |
| Blocchi di testo | 8 |
| Parole | 98 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|7` — gruppo 7, rappresentante |

**Composizione.** "4,1M" in cifre bianche enormi (fra le più grandi misurate su questa pagina —
`scala_tipografica` di `20-apsales-consulenza` registra tagli fino a 256px/w800 in tutta la pagina,
candidato più plausibile proprio per questa cifra), sottotitolo con lo stesso dato per esteso, poi
a sinistra un riquadro con cinque righe a barra di distribuzione (Fattura meno di €100k o è in
negativo — 55,93%, la barra più lunga; Fattura più di €100k — 44,1%; soglie cumulative: più di €1M
— 8,5%, più di €10M — 1,07%, sopra i €50M — 0,23%) con nota "E questo neanche include i
forfettari.", a destra un breve testo su quanto sia normale faticare e la menzione "più di 100
consulenze con imprenditori, più di 50 con professionisti".

**Effetti attivi.** Nessuno oltre al colore (barra blu piena vs barre grigie a scalare).

**Perché è costruita così.** Il dato "55,93% fattura meno di €100k o è in negativo" non è scelto a
caso: posiziona la maggioranza silenziosa (non i casi eccezionali da social media) come normalità
statistica, disinnescando il senso di inadeguatezza del lettore prima ancora di introdurre
l'offerta — la stessa funzione della citazione "Nel 2026 sarai avanti o indietro" vista su
claude-speedrun.com, qui però basata su un dato ISTAT-style invece che su un aneddoto personale.

---

## TAVOLA C9 — Il micro-riquadro di disponibilità
![sezione 09](../capture/20-apsales-consulenza/sezioni/09-section.png)

**Ruolo:** ponte di fiducia fra la parte emotiva/diagnostica e il blocco prezzo — rassicura sulla disponibilità reale prima di chiedere il pagamento.

| Campo | Valore |
|---|---|
| y / altezza | 9673px / 644px — **3,8%** |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `disponibilita` |
| Heading | nessuno |
| Blocchi di testo | 8 |
| Parole | 17 |
| Media | 0 |
| CTA | 1 — "Prenota la consulenza →" |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|C\|3` — gruppo 9, rappresentante |

**Composizione.** Un riquadro isolato con bordo blu tratteggiato agli angoli (stile "selezionato"),
titolo "Andrei è disponibile **oggi stesso**." (con "oggi stesso" in corsivo blu), sottotitolo
"Verificato dal calendario reale e aggiornato di Andrei Pascu.", e un link sottolineato blu
"Prenota la consulenza" — nessuna icona, nessuna foto, solo testo dentro una cornice minima.

**Effetti attivi.** Il bordo con angoli marcati (probabile `outline-offset` o quattro pseudo-elementi
angolari) isola visivamente il riquadro come una "notifica" più che come una sezione di contenuto.

**Perché è costruita così — la scoperta di questa tavola.** Questo micro-riquadro è posizionato
esattamente **644px prima** dell'offerta con prezzo (Tavola C10): è un ponte di disponibilità
booking/calendario inserito subito prima del prezzo, un pattern che non compare né su `/servizi`
(che rimanda solo a "prezzo su preventivo", senza rassicurazione di calendario) né su
`/landing-page` (che usa invece un form di qualificazione ben più a monte, Tavola L10, non
immediatamente prima dell'offerta). Su una pagina di pagamento diretto e immediato, la
rassicurazione "c'è posto oggi, il calendario è vero" serve a ridurre l'attrito nell'ultimo tratto
prima del clic sul prezzo — un dettaglio di sequenza assente sulle altre due pagine.

---

## TAVOLA C10 — L'offerta "Consulenza con Andrei Pascu."
![sezione 10](../capture/20-apsales-consulenza/sezioni/10-consulenza-con-andrei-pascu.png)

**Ruolo:** il blocco prezzo — identico nella sostanza a quello della Tavola S3, qui più dettagliato.

| Campo | Valore |
|---|---|
| y / altezza | 10316px / 839px — **5,0%** |
| Sfondo | `#f9f9f9` — unica sezione chiara insieme a C4 |
| id | `offerta` |
| Heading | H2 "Consulenza con *Andrei Pascu*." |
| Blocchi di testo | 17 |
| Parole | 52 |
| Media | 0 |
| CTA | 1 — "Paga, poi scegli data e ora →" |
| Firma / gruppo | `section\|scroll-mt-16.theme-paper.bg-paper\|1\|-\|C\|4` — gruppo 10, rappresentante |

**Composizione.** A sinistra quattro righe separate da filetti (Ricevi anche la registrazione,
Non devi prendere appunti: ti mandiamo un piano in PDF, Totale anonimato su richiesta, Approccio
results-oriented) e la chiusura in grassetto "No motivazione. No frasi magiche. **No cazzate.**";
a destra una card bianca bordata con "60 minuti", "**€610**" in cifre enormi, "IVA inclusa", CTA
blu pieno e la nota "Il modulo si apre qui, senza uscire dalla pagina."

**Effetti attivi.** Nessuno.

**Perché è costruita così.** Il CTA non dice "Acquista" o "Prenota": dice **"Paga, poi scegli data
e ora"** — l'ordine delle azioni è dichiarato esplicitamente nel testo del pulsante stesso, così il
cliente sa che il pagamento avviene *prima* della scelta di data, non dopo. È un dettaglio minuscolo
che previene un'obiezione implicita ("e se pago e poi non trovo un orario buono?") ancora prima che
venga formulata.

---

## TAVOLA C11 — "Cosa succede dopo il pagamento." (5 tappe)
![sezione 11](../capture/20-apsales-consulenza/sezioni/11-cosa-succede-dopo-il-pagamento.png)

**Ruolo:** rassicurazione post-acquisto — il percorso è breve, non 14 tappe come su `/landing-page`.

| Campo | Valore |
|---|---|
| y / altezza | 11155px / 847px — **5,0%** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H2 "Cosa succede dopo il pagamento." |
| Blocchi di testo | 18 |
| Parole | 34 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|4` — gruppo 11, rappresentante |

**Composizione.** Cinque tappe a pallini connessi da linea verticale (stesso stile grafico della
Tavola L12, ma molto più corta): Completi il modulo di fatturazione → Scegli data e ora della tua
consulenza → Ti arriva il link al Google Meet → Consulenza in chiamata → Ricevi il tuo piano
d'azione + riassunto.

**Effetti attivi.** Nessuno oltre al pallino pieno blu sulla prima tappa (stato "corrente/prossimo
passo").

**Perché è costruita così.** Cinque tappe contro le quattordici di `/landing-page` (Tavola L12) non
è un caso di brevità casuale: è coerente col ciclo di vendita. La consulenza è un acquisto
impulsivo a basso attrito (paghi e scegli l'orario), la landing page è un progetto lungo con
contratto e sviluppo — il numero di tappe mostrate riflette onestamente la reale complessità di
ciascun servizio, non una scelta stilistica indipendente dal contenuto.

---

## TAVOLA C12 — "Andrei Pascu vs consulente medio."
![sezione 12](../capture/20-apsales-consulenza/sezioni/12-andrei-pascu-vs-consulente-medio.png)

**Ruolo:** seconda tabella comparativa della pagina — qui contro una categoria generica, non un competitor nominato.

| Campo | Valore |
|---|---|
| y / altezza | 12003px / 1097px — **6,5%** |
| Sfondo | `#111111` (bg-pitch) |
| id | `confronto` |
| Heading | H2 "Andrei Pascu **vs** consulente medio." |
| Blocchi di testo | 20 |
| Parole | 88 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|5` — gruppo 12, rappresentante |

**Composizione.** Tabella a due colonne e cinque righe: Ha avviato un'impresa? (Sì / No) — Rischia
la pelle come te? (Sì / No) — Quando ci parli? (Tra pochi giorni / Tra qualche settimana) — Cosa
ricevi? (Un piano in step che capisci e puoi applicare subito / Un deck di 50 slide, probabilmente
fatte con AI) — Deve pagare gente ogni mese? (Sì / No). Chiude con "Ognuno ha il suo ruolo. Ma
quando sei in trincea, ti serve qualcuno che il fucile lo sa usare. Non qualcuno che parla di
fucili dopo aver letto qualche libro."

**Effetti attivi.** Nessuno.

**Perché è costruita così.** La riga "Cosa ricevi?" contiene la frecciata più diretta di tutta la
pagina ("probabilmente fatte con AI") rivolta a un bersaglio generico e non nominabile
("consulente medio"): permette un colpo specifico e riconoscibile (i deck AI-generati sono un
fenomeno reale e diffuso) senza il rischio legale o reputazionale di nominare un concorrente
preciso.

---

## TAVOLA C13 — La FAQ esplosa (14 righe cliccabili)
![sezione 13](../capture/20-apsales-consulenza/sezioni/13-quello-che-chiedono-prima-di-pagar.png)

**Ruolo:** rimozione delle obiezioni pre-pagamento — qui interattiva, a differenza della gemella statica su `/landing-page`.

| Campo | Valore |
|---|---|
| y / altezza | 13100px / 1856px — **11,0%, la sezione più alta della pagina** |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `faq` |
| Heading | H2 "Quello che chiedono prima di pagare." + 5 domande in `headings[]` |
| Blocchi di testo | 29 |
| Parole | 95 |
| Media | 14 — le 14 icone chevron |
| CTA | 14 — i 14 trigger dell'accordion, uno per domanda |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|M\|C\|9` — gruppo 13, rappresentante |

**Composizione.** Titolo, poi 14 righe accordion chiuse con chevron a destra: Fate fattura? —
Posso pagare con bonifico? — La consulenza è con Andrei Pascu? — Andrei usa l'AI per darmi
consigli? — Il riassunto che ricevo entro 48h è fatto dall'AI? — È possibile fare la consulenza in
presenza? — In questa call mi verranno venduti servizi? — Cosa devo preparare prima della call? —
Chi vede la registrazione della call? — Posso portare un socio o una persona del team? — Devo
spostare la consulenza. Si può? — Un'ora basta davvero? — E se il mio problema non rientra nelle
aree di Andrei? — Ci sono aree che Andrei non copre?

**Effetti attivi.** Accordion Radix vero (stesso `accordion-LU6_yz4t.js` da 9.211 byte misurato
nel dossier COSTRUZIONE), qui effettivamente caricato — a differenza di `/landing-page`.

**Perché è costruita così.** Due domande consecutive ("Andrei usa l'AI per darmi consigli?", "Il
riassunto che ricevo entro 48h è fatto dall'AI?") affrontano di petto il sospetto più moderno e
specifico del 2026 — che un servizio "personale" da €610 sia in realtà mediato o automatizzato
dall'intelligenza artificiale. Nominarlo prima che il cliente lo pensi è la stessa disciplina di
disinnesco preventivo osservata in tutto questo ecosistema, applicata qui a un'obiezione che
probabilmente non esisteva nemmeno come categoria fino a poco tempo fa.

---

## TAVOLA C14 — La CTA finale "Sblocca il vincolo. Ottieni il tuo piano."
![sezione 14](../capture/20-apsales-consulenza/sezioni/14-sblocca-il-vincolo-ottieni-il-tuo.png)

**Ruolo:** chiusura pagina — richiama il linguaggio ("vincolo") introdotto in apertura.

| Campo | Valore |
|---|---|
| y / altezza | 14956px / 694px — **4,1%** |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | H1 "Sblocca il *vincolo*. Ottieni il tuo piano." |
| Blocchi di testo | 7 |
| Parole | 15 |
| Media | 0 |
| CTA | 1 — "Prenota adesso →" |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|-\|C\|3` — gruppo 14, rappresentante |

**Composizione.** Titolo con "vincolo" in corsivo, sottotitolo "Consulenze disponibili entro
pochissimi giorni.", CTA blu pieno — nessun'altra grafica.

**Effetti attivi.** Nessuno.

**Perché è costruita così.** Chiudere ripetendo la parola "vincolo" — lo stesso termine introdotto
nella Tavola C3 e ripreso in C5/C6 — chiude il cerchio semantico dell'intera pagina con una sola
parola: chi è arrivato fin qui ha già imparato cosa significa "il tuo vincolo", quindi il titolo
finale non ha bisogno di rispiegarlo, solo di richiamarlo come promemoria dell'azione da compiere.

---

## TAVOLA C15 — Il footer
![sezione 15](../capture/20-apsales-consulenza/sezioni/15-footer.png)

**Ruolo:** chiusura — terza (e ultima, per questo studio) istanza dello stesso componente a tenda.

| Campo | Valore |
|---|---|
| y / altezza | 15650px / 1182px — **7,0%** |
| Sfondo | `transparent` |
| Heading | nessuno |
| Blocchi di testo | 19 |
| Parole | 32 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `footer\|relative\|2\|M\|-\|6` — gruppo 15, rappresentante |

**Composizione.** Identica alle Tavole S5 e L17.

**Perché è costruita così.** Tre pagine di servizio su tre, più la pagina radice del dossier 13:
**quattro istanze misurate finora dello stesso identico footer**, sempre con lo stesso comportamento
a tenda mai fotografato nel suo stato rivelato da nessuno dei quattro scatti automatici raccolti in
questo studio (vedi "LA VERITÀ SU RevealFooter" nel dossier COSTRUZIONE per la spiegazione tecnica
completa). Non aggiungo qui altro oltre alla conferma numerica: quattro capture su quattro
concordano.

---

## DELTA ALLA FABBRICA

**CANONE:** La stessa ricetta di classi (`relative.overflow-hidden.bg-void`) apre **e** chiude
tutte e quattro le pagine dell'ecosistema apsales.eu misurate fin qui (la radice del dossier 13
più le tre di questo atlante): hero e CTA finale condividono lo stesso involucro strutturale,
cambia solo cosa ci sta dentro (su `/servizi` la firma di apertura e chiusura è addirittura
identica byte per byte, non solo per famiglia di classi). Da portare nel canone della Fabbrica
Siti come regola esplicita: **la sezione di apertura e quella di chiusura di una pagina di
servizio nascono dallo stesso componente-cornice**, non da due sezioni progettate
indipendentemente — garantisce che la pagina "torni a casa" visivamente alla fine di ogni scroll.

**PATTERN:** Il micro-riquadro di disponibilità/calendario (Tavola C9) inserito **immediatamente
prima** del blocco prezzo, e non genericamente "da qualche parte a metà pagina", è un ponte di
fiducia specifico per pagine a pagamento diretto e immediato: rassicura sulla disponibilità reale
nell'ultimo tratto prima del clic. Confrontato con le altre due pagine studiate — assente su
`/servizi` (prezzo su preventivo, nessun ponte necessario) e sostituito da un form di
qualificazione molto più a monte su `/landing-page` (Tavola L10, lontano dall'offerta) — il
posizionamento immediatamente pre-prezzo va portato in Fabbrica come regola di sequenza per
qualunque pagina che vende un appuntamento a pagamento immediato: rassicurazione di disponibilità
subito prima del bottone, non prima nel funnel.

**GATE:** Verificare, per ogni nuova pagina di servizio a pagamento diretto costruita in Fabbrica,
che il numero di tappe mostrate nel percorso "cosa succede dopo" sia proporzionato alla reale
complessità del servizio — qui misurato in 5 tappe per la consulenza (un'ora, un output) contro 14
per la landing page (un progetto di settimane con contratto, design e sviluppo). Un percorso
sovradimensionato per un servizio semplice comunica lentezza non necessaria; uno sottodimensionato
per un progetto complesso rischia di sembrare superficiale. Il numero di tappe è un segnale di
onestà sul carico di lavoro reale, non una scelta di stile libera.

---

## Connessioni

- [08-apsales.md](08-apsales.md) — il primo passaggio sulla home: copy, palette, struttura
- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) e [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) — stack, token, e la tavola per sezione della pagina radice, stesso formato di lettura
- [18-20-apsales-servizi-COSTRUZIONE.md](18-20-apsales-servizi-COSTRUZIONE.md) — gli otto componenti condivisi, la verità su RevealFooter, i quattro difetti misurati nel codice
- [18-20-apsales-servizi-COPY.md](18-20-apsales-servizi-COPY.md) — il teardown del copy delle tre pagine
- [11-armageddon-ATLANTE-VISIVO.md](11-armageddon-ATLANTE-VISIVO.md) — il modello di formato di questo stesso documento
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
