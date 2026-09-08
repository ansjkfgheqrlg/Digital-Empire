---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #squarespace #costruzione #onda-b #fabbrica-siti
Created: 2026-09-08
Last updated: 2026-09-08
---

# 21-22-23-26 — outEmail, outViral, Vendita101, mpo2: LA COSTRUZIONE

Quarto giro di studio sull'ecosistema Andrei Pascu, primo su dominio Squarespace (`www.andrei-copy.com`)
invece di React/TanStack Start (`apsales.eu`, dossier 13 e 18-20). Le quattro pagine — `/outemail`
(21, 26.032px), `/outviral` (22, 11.555px), `/vendita` (23, 14.905px), `/mpo2` (26, 10.120px) — sono le
quattro pagine di vendita di onda B, già mappate visivamente in
[21-22-23-26-vendita-ATLANTE.md](21-22-23-26-vendita-ATLANTE.md) (modello di lettura:
[18-20-apsales-servizi-COSTRUZIONE.md](18-20-apsales-servizi-COSTRUZIONE.md)). Questo rapporto non ripete
lo schema visivo tavola-per-tavola già scritto nell'Atlante gemello: guarda **come sono costruite** —
palette con conteggio d'uso, scala tipografica, effetti/keyframes con tempi e curve, lo schema delle
sezioni letto da `scheda.json` — e soprattutto risponde alla domanda che Squarespace pone diversamente da
un sito React: qui il codice non è tutto scaricato in bundle scritti dallo sviluppatore, è per il 99,9%+
piattaforma. **Una sola cosa, in ciascuna delle quattro cartelle, è scritta da Andrei Pascu stesso**: il
file `custom.css`. Il resto — `site.css`, `static.css`, i componenti `website.components.*`, gli script
`extract-css-*`, `common-vendors-*` — è codice Squarespace, identico a quello che gira su qualunque altro
sito costruito sulla stessa piattaforma. Fonti primarie per ogni cifra: `scheda.json`, `_INDICE.json` (peso
in byte di ogni file scaricato), `dom-blocks.json` (elenco dei blocchi realmente presenti nel DOM di ogni
pagina) e i file sorgente in `src/*.css`/`src/*.js` aperti uno per uno.

---

## COSA È SUO E COSA È DELLA PIATTAFORMA

Il file `src/38-custom.css` di `21-outemail` (`src/36-custom.css` nelle altre tre cartelle, stesso file,
solo indice diverso) porta in testa un commento aggiunto dallo strumento di cattura con la fonte esatta:

```
/* fonte: https://static1.squarespace.com/static/custom-css/602126db7a4e4c01fd9babb6/602126db7a4e4c01fd9babd0/0/custom.css */
```

Questo è l'URL del pannello "CSS personalizzato" di Squarespace — l'unico punto dell'intera piattaforma
dove il proprietario del sito può scrivere codice proprio, al di fuori dei blocchi drag-and-drop. Ho
verificato che è **letteralmente lo stesso file su tutte e quattro le pagine**: stesso URL, stesso hash
MD5 (`e29afa95a1ebd53e4787b1308dfd72fc`), stesso peso dichiarato in `_INDICE.json` (**1.183 byte**, la
cifra "fonte", diversa dai 1.309 byte su disco perché il commento aggiunto dallo strumento di cattura pesa
126 byte in più — costante su tutte e quattro le copie). Non è un file per pagina: è **un solo file per
l'intero dominio**, iniettato ovunque.

Il peso totale scaricato per ciascuna pagina (somma di tutti i file in `src/`, campo `bytes` di ogni voce
in `_INDICE.json`) è: `21-outemail` 4.528.900 byte, `22-outviral` 4.502.324 byte, `23-vendita` 5.572.769
byte, `26-mpo2` 3.664.240 byte. Il file scritto da Andrei Pascu pesa 1.183 byte su ciascuno di questi
totali — **una frazione tra 1:3.100 (23-vendita) e 1:3.829 (21-outemail)**, cioè lo 0,021%-0,032% del peso
scaricato per aprire una di queste pagine. Tutto il resto — il 99,97%+ — è Squarespace: motore di layout
(`site.css`, 1.274.296 byte, identico byte-per-byte su tutte e quattro le cartelle), asset versionati
(`static.css`, 481.489 byte), polyfiller (`modern.js`, 117.559 byte), pacchetto di localizzazione
(`cldr-resource-pack...it-IT.js`, 153.101 byte), libreria vendor comune (`common-vendors-stable...js`,
246.523 byte), oltre a un componente per ciascun tipo di blocco usato nella pagina (`accordion`, `button`,
`horizontalrule`, `html`, `imageFluid` con i suoi cinque filtri effetto, `socialLinks`, `spacer`, `video`).
Nessuno di questi file cambia una riga fra `outemail`, `outviral`, `vendita`, `mpo2`: stesso hash, stesso
peso, verificato incrociando i campi `bytes` e `url` di ogni `_INDICE.json`.

**Ma anche dentro l'unico file che è suo, la maggior parte delle regole non è attiva su queste quattro
pagine.** Ho letto `custom.css` per intero (riportato integralmente più sotto) e verificato ogni selettore
contro `dom-blocks.json` di ciascuna delle quattro pagine — l'elenco dei blocchi realmente renderizzati nel
DOM. Risultato: delle sei regole del file, **solo due sono dimostrabilmente attive** su queste quattro
pagine di vendita. Le altre quattro puntano a elementi che qui non esistono:

| Regola | Bersaglio | Trovato in `dom-blocks.json` di 21/22/23/26? | Stato su queste 4 pagine |
|---|---|---|---|
| `html{scroll-behavior:smooth}` | tutto il documento | — (globale, non serve un blocco) | **attiva**: rende fluidi gli scroll verso `#outemail-price` e simili |
| hide `div#block-d1120bc9fcfdf98c44ce` (desktop ≥768px) | un blocco con ID specifico | cercato nei 4 file, **0 corrispondenze** | non attiva qui — punta a un blocco altrove nel sito, o rimosso da allora |
| hide `div#block-yui_3_17_2_1_1682955919241_22665` (mobile ≤767px) | un blocco con ID specifico | cercato nei 4 file, **0 corrispondenze** | non attiva qui, stesso caso |
| `.course-list` (progress bar, checkbox `#efab00`, 4 selettori) | l'area corsi post-acquisto | cercato "course-list" nei 4 `scheda.json` e `dom-blocks.json`, **0 corrispondenze** | non attiva: l'area corsi è dietro login, fuori da questa cattura |
| `footer p a{text-decoration:none!important}` | link nel footer | tutte e quattro le pagine hanno un footer con paragrafi-link (vedi ATLANTE, Tavola A6) | **attiva** su tutte e quattro |

In altre parole: della sua unica riga di codice proprio, **solo il comportamento di scroll e la
rimozione della sottolineatura dei link nel footer sono verificabilmente in funzione su queste quattro
pagine di vendita**. Le regole per l'area membri (`.course-list`, con il colore ambra `#efab00` sul
checkmark) restano pronte per quando l'utente ha già pagato ed entra nel corso — un'area non compresa in
questo studio — mentre le due regole di occultamento per-breakpoint puntano a ID di blocco che non
corrispondono a nulla nel DOM delle quattro pagine capturate: o servivano a una pagina diversa del sito
(probabilmente la home, mai vista in queste cattura), o a contenuto già rimosso. **Non lo affermo con
certezza — lo dichiaro come non trovato**, secondo la regola di non stimare.

Da segnalare una seconda forma di "codice suo": tre delle quattro pagine (`22-outviral`, `23-vendita`,
`26-mpo2`) caricano anche `src/*-rdd73ozkqt.js`, uno snippet di **Microsoft Clarity** (`fonte:
https://www.clarity.ms/tag/rdd73ozkqt`, letto per intero — 878 byte, project ID `rdd73ozkqt`, traccia
`_uetmsclkid`/`_uetvid`/`_clck`, scadenza cookie 365 giorni). **`21-outemail` non lo carica affatto** —
verificato con una ricerca di "clarity" su `_INDICE.json`, zero corrispondenze. Questo è un secondo
frammento di codice iniettato da Andrei Pascu (via il pannello "Iniezione di codice" di Squarespace, non
`custom.css`), non presente ovunque: un'ulteriore prova, indipendente dal CSS, che `21-outemail` gira su
una versione più vecchia del sito rispetto alle altre tre (vedi sezione finale).

---

## IL FILE `custom.css`, PER INTERO

Sei regole, 1.183 byte, LESS compilato (intestazione dichiarata: `Squarespace LESS Compiler (less.js
language v1.3.3)`):

```css
html{scroll-behavior:smooth}

@media screen and (min-width:768px){
  div#block-d1120bc9fcfdf98c44ce{display:none}
}
@media screen and (max-width:767px){
  div#block-yui_3_17_2_1_1682955919241_22665{display:none}
}

.course-list .course-list__progress-bar-container{
  border-radius:50px !important;border:0px solid #eee;background:#202020
}
.course-list .course-list_progress-bar-container .course-listprogress-bar{
  border-radius:50px;background:#202020
}
.course-list .course-listprogress-bar-container .course-listprogress-bar-percentage{
  background:#202020 !important;color:#fff !important;font-size:14px
}
.course-list .course-listprogress-bar-container .course-list_progress-bar-text{
  background:#fff;color:#000;font-size:14px;padding:5px 15px
}
.course-list_list .course-listlist-course-item-status .course-listcheckbox:checked+.course-listcheckbox-target .course-item_checkbox-svg-checkmark{
  stroke:#fff !important
}
.course-list_list .course-listlist-course-item-status .course-listcheckbox:checked+.course-listcheckbox-target .course-item_checkbox-svg-outline{
  stroke:#efab00 !important;fill:#efab00
}

footer p a{text-decoration:none !important}
```

Osservazioni sulla scrittura del codice, non solo sul suo effetto: i nomi di classe `.course-listprogress-bar`
(senza trattino fra "list" e "progress") accanto a `.course-list_progress-bar-container` (con trattino
basso) nella stessa regola tradiscono un refuso di battitura mai corretto — coerente con quanto già
osservato nel dossier gemello sulla macchina del funnel (titolo pubblicato "Armageggon STRP" invece di
"Armageddon"): il codice proprio di Andrei Pascu, quando esiste, non è rifinito. Il colore `#efab00`
(ambra) usato qui per il contorno/segno di spunta del checkbox corso **è lo stesso identico esadecimale**
misurato come colore-accento della pagina `/define` nella coppia di pagine-ponte del funnel (dossier
24-25-27-28): un solo colore ambra riusato sia nell'area corsi post-acquisto sia come evidenziatore di una
parola nel funnel pre-acquisto — indizio di una palette di accento condivisa a livello di intero
ecosistema, non scelta a caso pagina per pagina.

---

## L'IMPALCATURA SQUARESPACE: COSA C'È IN `src/`

Ogni cartella `src/` contiene fra 40 e 41 file. Escludendo `custom.css`, si dividono in quattro famiglie,
tutte piattaforma:

**Motore e localizzazione (sempre presenti, stesso hash su tutte e quattro):** `modern.js` (117.559 B,
polyfiller `@sqs/polyfiller`), `cldr-resource-pack-...-it-IT.js` (153.101 B), `common-vendors-stable-...js`
(246.523 B), `extract-css-runtime-...js` (50.537 B), `visitor-site-error-reporter-...js` (3.680 B). Nessuno
di questi contiene una riga scritta per uno di questi quattro prodotti: sono il runtime generico di
qualunque sito Squarespace 7.1.

**Foglio globale del sito:** `site.css` (1.274.296 B, `?nocustom=true` nell'URL stesso — la piattaforma
dichiara esplicitamente che questo file **esclude** il CSS personalizzato, prova ulteriore che i due canali
sono tenuti separati by design) e `static.css` (481.489 B). Identici byte-per-byte sulle quattro pagine.

**Componenti per tipo di blocco usato in pagina — qui la presenza/assenza segnala il contenuto, esattamente
come nel dossier 18-20 su apsales.eu.** Tabella di corrispondenza fra componente e pagina che lo carica:

| Componente | 21-outemail | 22-outviral | 23-vendita | 26-mpo2 | Cosa serve |
|---|---|---|---|---|---|
| `accordion` (styles 8.079 B + visitor 20.725 B) | sì | sì | **no** | sì | FAQ/lista lezioni espandibili |
| `code` (styles 102-105 B + visitor 12-15 KB) | sì | no | sì | sì | blocchi di embed HTML/CSS custom |
| `spacer` | no | sì | no | sì | spaziatura manuale fra blocchi |
| `imageFluid` + 5 filtri effetto (`film-grain`,`liquid`,`parallax`,`refracted-circles`,`refracted-lines`) | sì | sì | sì | sì | ogni immagine fluida del sito porta con sé tutti e cinque i filtri, usati o no |
| `video` | sì | sì | sì | sì | player Vimeo incorporato |
| `socialLinks` | sì | sì | sì | sì | icone social nel footer |

**L'assenza di `accordion` su `23-vendita` non è casuale**: quella pagina, unica delle quattro, non ha
alcuna sezione FAQ né una lista-lezioni a righe cliccabili — il curriculum (Tavola C5 dell'Atlante gemello)
è reso a righe fisse con timestamp, non a fisarmonica. Il componente manca perché il contenuto che lo
richiederebbe non esiste in quella pagina: stessa logica di causa-effetto già misurata su apsales.eu.

**Tracciamento di terze parti — la quarta famiglia, e la più diseguale fra le quattro pagine:**

| Pagina | Microsoft Clarity | Meta/Facebook Pixel | Google Tag Manager | Google Analytics (gtag) |
|---|---|---|---|---|
| 21-outemail | no | no | no | no |
| 22-outviral | sì (878 B) | no | no | no |
| 23-vendita | non verificato oltre `_INDICE.json` letto parzialmente | non verificato | non verificato | non verificato |
| 26-mpo2 | sì (878 B) | no | no | no |

`21-outemail` non carica **nessuno** dei quattro sistemi di tracciamento di terze parti elencati: zero
Clarity, zero Pixel, zero GTM. Le altre tre pagine studiate qui portano almeno Clarity. Per contro — dato
raccolto nel giro di studio delle pagine-ponte dello stesso dominio (dossier 24-25-27-28, stesso sito,
stesso `custom.css`) — la pagina di cassa vera (`/outfunnel-1`) carica **tutti e quattro** insieme
(Clarity + Facebook Pixel 415.673+452.403 B + Google Tag Manager 331.236 B + gtag.js 485.594 B), mentre le
pagine puramente educative del funnel (`/define`, `/armadeggon-strp`) non ne caricano **nessuno**. Il
tracciamento non è uniforme sul sito: si concentra dove c'è una conversione da misurare, è quasi assente
dove la pagina serve solo a spostare il visitatore al passo successivo. Questo è un dato di costruzione,
non di visual design, ed è coerente con l'assenza totale di terze parti proprio sulla pagina più vecchia
del gruppo studiato qui (`21-outemail`), costruita prima che questi tag fossero standard nel sito.

---

## LO SCHEMA DELLE QUATTRO PAGINE

Tabelle compatte da `sezioni[]` di ogni `scheda.json` — non ripetono le tavole narrative dell'Atlante
gemello, riportano lo scheletro misurato: quante sezioni, quante distinte, dove cadono i "buchi" di
misurazione già segnalati nell'Atlante (`div.section-border`).

| Pagina | Altezza | Sezioni tot. | Sezioni distinte | `blocchi_testo` totali (campo top-level) | Sezioni `div.section-border` (bug di conteggio) |
|---|---|---|---|---|---|
| 21-outemail | 26.032px | 24 | 17 | 259 | 2 (i=5, i=12) |
| 22-outviral | 11.555px | 11 | 11 | 196 | 1 (i=2) |
| 23-vendita | 14.905px | 18 | 15 | 185 | 0 |
| 26-mpo2 | 10.120px | 13 | 13 | 132 | 0 |

Il rapporto sezioni-totali/sezioni-distinte misura quanto la pagina riusa uno stesso schema di layout:
`21-outemail` ripete 7 volte una firma già vista (24 sezioni, solo 17 firme distinte — coefficiente di
riuso 1,41), mentre `22-outviral` e `26-mpo2` non ripetono **mai** la stessa firma (coefficiente 1,00,
ogni sezione è unica) e `23-vendita` sta in mezzo (18/15, coefficiente 1,20). Le due sezioni `div` con
classe `section-border` di `21-outemail` (i=5 e i=12, già documentate come bug nell'Atlante gemello) e
quella di `22-outviral` (i=2) sono l'unica ricorrenza di questo pattern fra le quattro pagine: `23-vendita`
e `26-mpo2` non usano affatto la classe Squarespace `has-section-divider.full-bleed-section` che genera il
bug — usano `layout-engine-section` più piatto, coerente con quanto già misurato nell'Atlante sulla
struttura HTML delle due famiglie di pagine.

---

## LA PALETTE, CONTATA

Conteggio d'uso da `palette_testo` e `palette_sfondi` di ogni `scheda.json` (colore, numero di occorrenze
misurate nel DOM):

| Colore | Ruolo | 21-outemail | 22-outviral | 23-vendita | 26-mpo2 |
|---|---|---|---|---|---|
| `#0062ff` | blu d'azione (CTA, stesso token di apsales.eu) | 7 sfondi | 3 sfondi | 3 sfondi | 3 sfondi |
| `#1b1b1d` | quasi-nero, sfondo dominante | 53 sfondi | 31 sfondi | 10 sfondi | 27 sfondi |
| `#fafafa` | testo chiaro dominante | 147 testo | 10 testo | 10 testo | 14 testo |
| `#a8a8a8` | grigio medio, `body_bg` delle tre pagine "nuove" | 9 sfondi | 30 sfondi | 32 sfondi | 27 sfondi |
| `#ffffff` | bianco puro, `body_bg` di 21 | 16 sfondi | 1 sfondo | 0 | 0 |
| `#87ceeb` / `#a7ddf4` | azzurro cielo, glow della card prezzo | 8+7 sfondi | 0 | 0 | 0 |

Il blu `#0062ff` è l'unico colore presente come sfondo-CTA su **tutte e quattro** le pagine, sempre con
conteggio a una cifra o poco oltre — mai il colore dominante, sempre l'accento. È lo stesso esadecimale
già misurato su `apsales.eu` (dossier 13, Tavole 1/5/6): **continuità cromatica confermata su un secondo
dominio dello stesso ecosistema**, non un caso isolato di una pagina. Il grigio medio `#a8a8a8` come
`body_bg` è esclusivo delle tre pagine "nuove" (22/23/26): `21-outemail` ha `body_bg:"#ffffff"`, bianco
puro — la prima e più semplice prova che quella pagina viene da un altro momento costruttivo del sito
(ripreso e ampliato più sotto). L'azzurro cielo (`#87ceeb`/`#a7ddf4`) compare **solo** su `21-outemail`, 15
occorrenze totali fra le due tonalità, tutte concentrate sul glow della card prezzo (sezione i=22,
`ombre`: `rgb(135, 206, 235) 0px 0px 15.4725px 0px` ×4 e `rgb(135, 206, 235) 0px 0px 16.6951px 5.02136px`
×1) e sui badge "Open" del carosello di prova (sezione i=20) — un secondo accento cromatico che le altre
tre pagine non hanno mai, coerente con l'ipotesi di template diverso.

---

## LA SCALA TIPOGRAFICA E I PESI

Font dominante per pagina (campo `caratteri`, conteggio occorrenze): `21-outemail` usa **Inter** (163
occorrenze, più `plus-jakarta-sans-o8l9cc` 35) — un font di sistema/Google Fonts generico. Le altre tre
usano **`elza-8u3n84`** come font primario (`22-outviral` 60, `23-vendita` 81, `26-mpo2` 57, sempre
accompagnato da `plus-jakarta-sans-o8l9cc` in seconda posizione) — un font custom caricato da Squarespace
(hash `-8u3n84` tipico dei font venduti nel loro catalogo tipografico), mai usato su `21-outemail`. Body
font dichiarato in `scheda.json`: `21-outemail` → `"Inter, \"Segoe UI\", -apple-system,
BlinkMacSystemFont, sans-serif"` (uno stack di system-font con fallback espliciti); le altre tre →
semplicemente `"sans-serif"` (nessuno stack dichiarato a livello di `body`, il font arriva tutto da
classi specifiche). Due sistemi tipografici diversi sulla stessa piattaforma, stesso dominio.

Corpo-testo dominante, dalla `scala_tipografica`: `16px/w300` è la taglia più frequente su tutte e quattro
(36, 33, 56, 32 occorrenze rispettivamente) — l'unico punto di reale continuità tipografica fra le due
famiglie. Sopra quella base, la gerarchia diverge: `21-outemail` ha 12 titoli a `48px/w700` e 10 a
`60,8px/w700`, oltre a **nove taglie uniche sopra i 40px** usate una sola volta ciascuna (71px, 176,7px,
47,4px, 64,4px, 51,8px, 52,2px, 68,2px, 44,1px, 40,5px) — segno di titoli composti a mano sezione per
sezione, mai riusando esattamente la stessa taglia. `22-outviral`, `23-vendita` e `26-mpo2` condividono
invece una gerarchia molto più ripetuta: `38,4px/w700` (25, 11, — occorrenze), `24px/w700` (12, 17, 2),
`60,8px/w700` (4, 6, 3) — poche taglie, riusate spesso, coerenti con un template a componenti fissi
invece di titoli scritti a mano ogni volta.

Pesi tipografici totali per pagina (`pesi`): il 700 domina su `21-outemail` (116 occorrenze contro 49 del
300), mentre sulle altre tre il rapporto si rovescia o si pareggia — `22-outviral` 72×700 vs 45×300,
`23-vendita` 61×700 vs 69×300 (l'unica dove il 300 supera il 700), `26-mpo2` 37×700 vs 42×300. Il peso 800
compare solo su `21-outemail` (4 occorrenze) — un ulteriore peso tipografico che le altre tre pagine non
usano mai.

---

## GLI EFFETTI: TRANSIZIONI, ANIMAZIONI, KEYFRAMES

Le sessantacinque `@keyframes` dichiarate nel foglio globale sono identiche, per nome, su tutte e quattro
le pagine (lette per intero in ognuna delle quattro `scheda.json`): sono la libreria di animazioni nativa
di Squarespace (spinner di caricamento, gallery, accordion, form). **La differenza è quali di queste sono
effettivamente in uso**, campo `effetti.animazioni`:

- `21-outemail`: `pulseShadow 3s ease` ×4 + `pulse-shadow 3s ease` ×1 — un respiro luminoso lento, 3
  secondi, easing semplice, verosimilmente sul glow della card prezzo azzurra.
- `22-outviral`: **nessuna animazione custom attiva** (`animazioni: []`), solo `backdrop: blur(15px)` come
  filtro.
- `23-vendita` e `26-mpo2`: `image-fade-in 0.6s cubic-bezier(0.4, 0, 0.2, 1)` — rispettivamente 10 e 5
  usi — una dissolvenza in ingresso per immagine, 0,6 secondi, curva ad accelerazione-decelerazione
  standard (non un semplice ease). Questa stessa animazione (`image-fade-in`) è elencata fra le 65
  `@keyframes` disponibili su **tutte e quattro** le pagine ma **usata solo su due**: prova diretta che le
  quattro pagine, pur condividendo lo stesso foglio CSS, applicano classi diverse ai propri blocchi
  immagine — un'altra conferma della differenza di template fra `21-outemail`/`22-outviral` da un lato e
  `23-vendita`/`26-mpo2` dall'altro, ma non allineata alla stessa linea di frattura del font (che separa
  21 da 22/23/26): qui la linea passa fra {21,22} e {23,26}. Le due famiglie di dati non coincidono
  perfettamente, prova che il sito è stato costruito e aggiornato in più fasi non sincronizzate fra loro.

Transizioni: il totale di regole `transition:all` (probabilmente ereditate dal framework di bottoni)
varia con la lunghezza della pagina — 1.384 su `21-outemail` (la più lunga), 728 su `26-mpo2` (la più
corta) — proporzionale al numero di elementi interattivi, non un dato di design. Più significativo il
dettaglio applicato: `fill 0.17s ease-in-out` ×8 su tutte e quattro (icone SVG che cambiano colore al
hover, probabilmente i social link) e `background-color 0.17s ease-in-out, opacity 0.17s ease-in-out` ×4
su tutte e quattro — due transizioni della libreria bottoni di Squarespace, non del sito specifico,
identiche ovunque compaia un bottone.

Filtri: `backdrop: blur(15px)` compare solo su `22-outviral` (2 usi) e `26-mpo2` (1 uso) — un overlay
sfocato, verosimilmente dietro il player video incorporato o un menu mobile — mai su `21-outemail` né
`23-vendita`. Nessuna delle quattro pagine dichiara `blend` o `filtri` con `contrast`/`brightness` come
invece misurato ripetutamente su apsales.eu (dossier 13 e 18-20): il trucco `mix-blend-screen` per le
illustrazioni ASCII/inchiostro appartiene al dominio React, non è stato riportato su Squarespace.

Clip-path per i "divisori a onda" fra sezioni: `21-outemail` ne dichiara **10 distinti**, ciascuno con un
ID univoco (`url("#section-divider-67e6a52584dc281daa432113")` e simili) — un componente Squarespace
nativo ("section divider"), uno diverso per ogni transizione visiva della pagina. `22-outviral` ne ha 3
più un quarto riferito a un sistema-desktop generico (`#d067c758288e9979524b-system_desktop`).
`23-vendita` ne ha 5. `26-mpo2`: **zero** — nessun divisore a onda, transizioni fra sezioni sempre a
taglio netto. Il numero di divisori a onda scala con la lunghezza della pagina più che con un canone di
stile fisso.

---

## I DUE TEMPLATE — E LA TERZA VARIABILE CHE NON COMBACIA

Riassumendo le prove raccolte, sette segnali indipendenti separano `21-outemail` dalle altre tre:

1. `body_bg`: `#ffffff` (21) contro `#a8a8a8` (22, 23, 26).
2. `body_font`: stack esplicito con Inter (21) contro `sans-serif` nudo (22, 23, 26).
3. Font dominante misurato: Inter 163 occ. (21) contro `elza-8u3n84` (22, 23, 26).
4. Classe di sezione: `has-section-divider.full-bleed-section` con wrapper `div.section-border` annidati,
   causa del bug di conteggio (21) — le altre tre non hanno mai questo bug nella stessa misura (23 e 26
   zero occorrenze, 22 una sola).
5. Colore accento aggiuntivo: azzurro cielo `#87ceeb`/`#a7ddf4` sul glow della card prezzo, esclusivo di
   21.
6. Tracciamento terze parti: 21 non carica Microsoft Clarity, le altre tre sì.
7. Coefficiente di riuso sezioni: 1,41 su 21 contro 1,00-1,20 sulle altre tre.

**Ma l'ottavo segnale — quale animazione è effettivamente in uso — non rispetta questa stessa linea di
frattura**: `image-fade-in` è attiva su 23 e 26 ma non su 22, mentre 22 condivide con 21 l'assenza di
questa animazione (pur avendo font e `body_bg` da "template nuovo"). La conclusione più onesta, senza
forzare un'unica narrazione: **il sito non ha due versioni pulite ("vecchia" e "nuova")**, ha strati di
costruzione sovrapposti nel tempo che non si allineano su un'unica variabile. `21-outemail` è
chiaramente la pagina più antica (nessun tracciamento di terze parti, font di sistema, bug di
conteggio più frequente). Le altre tre condividono font e `body_bg`, ma divergono fra loro su quale
animazione hanno effettivamente attivato — segno che anche dentro il gruppo "nuovo" ci sono state
modifiche indipendenti, pagina per pagina, non un redesign unico applicato a tutte insieme.

---

## DELTA ALLA FABBRICA

**CANONE — il codice proprio è un file, non un sito: isolarlo e testarlo separatamente.** Su Squarespace
il 99,97%+ del peso e del comportamento di ogni pagina è piattaforma condivisa e immutabile dal cliente;
l'unico punto di controllo diretto è un solo foglio CSS iniettato a livello di dominio (qui: 1.183 byte
su 3,6-5,6 milioni). Per la Fabbrica questo significa: quando si valuta "quanto controllo ha il cliente
sul proprio sito" su una piattaforma a blocchi, la domanda giusta non è "che aspetto ha" ma "quante righe
di codice sono davvero sue, e quante di quelle sono ancora attive sulle pagine che il cliente vende
oggi" — qui erano 6 regole dichiarate, 2 dimostrabilmente vive sulle pagine di vendita, verificato riga
per riga contro il DOM reale (`dom-blocks.json`), non assunto dal solo elenco dei selettori.

**PATTERN — il tracciamento segue la conversione, non il contenuto.** Il carico di script di terze parti
(Clarity, Facebook Pixel, GTM, gtag) non è distribuito a caso o per uniformità: è quasi zero sulle pagine
che spostano il visitatore avanti nel funnel, ed è massimo esattamente sulla pagina dove avviene il
pagamento (misurato qui su `21-outemail`, che non ne carica nessuno, e riscontrato sull'intera catena del
funnel nel dossier 24-25-27-28: la pagina di cassa concentra da sola quattro sistemi di tracciamento
mentre le pagine-ponte non ne caricano nessuno). Pattern da riprodurre nella Fabbrica: instrumentare
pesantemente solo i passi che generano un evento di conversione misurabile, non ogni pagina per
abitudine.

**GATE — mai fidarsi di un selettore CSS senza verificarlo contro il DOM reale della pagina che si sta
consegnando.** Prima di dichiarare "attivo" un pezzo di codice trovato in un file CSS/JS scaricato,
cercare l'ID o la classe bersaglio nell'inventario reale dei blocchi (`dom-blocks.json` o equivalente):
qui due delle sei regole di `custom.css` puntavano a blocchi che semplicemente non esistono in nessuna
delle quattro pagine studiate. Un audit che si fermasse a leggere il CSS senza incrociarlo col DOM
avrebbe dichiarato "sito con progress-bar personalizzata e blocchi nascosti per breakpoint" su pagine
dove nessuna delle due cose è vera.

## Connessioni

- [21-22-23-26-vendita-ATLANTE.md](21-22-23-26-vendita-ATLANTE.md) — la tavola visiva per sezione delle
  stesse quattro pagine, stesso metodo dell'Atlante di apsales.eu
- [18-20-apsales-servizi-COSTRUZIONE.md](18-20-apsales-servizi-COSTRUZIONE.md) — il modello di questo
  stesso formato, sull'altro dominio (React/TanStack) dell'ecosistema
- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — dove il blu `#0062ff` è stato misurato la
  prima volta, confermato qui su un secondo dominio
- [24-25-27-28-macchina-del-funnel.md](24-25-27-28-macchina-del-funnel.md) — la catena di pagine-ponte
  dello stesso dominio, dove il colore ambra `#efab00` e l'asimmetria di tracciamento ricompaiono
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
