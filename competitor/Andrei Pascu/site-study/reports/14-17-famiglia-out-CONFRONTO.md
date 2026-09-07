---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #armageddon-pack #famiglia-out #confronto
Created: 2026-09-07
Last updated: 2026-09-07
---

# 14-17 — la famiglia "out*" — outEmail, outFunnel, outHeadline, outViral

**URL:** `armageddon.bsns.it/outemail` · `/outfunnel` · `/outheadline` · `/outviral`
**Catturate:** 2026-09-07. Prima volta che queste quattro pagine vengono studiate.

Sono le quattro pagine prodotto vendute dentro l'**Armageddon Pack** (dossier
[11-armageddon.md](11-armageddon.md)): quattro mini-corsi, quattro pagine di vendita, un solo
checkout. Questo report le confronta fra loro riga per riga sui dati misurati nei quattro
`scheda.json`; il secondo documento gemello, [14-17-famiglia-out-ATLANTE.md](14-17-famiglia-out-ATLANTE.md),
mostra le sezioni raggruppate per ruolo con gli screenshot aperti uno per uno.

---

## 0. LA VERIFICA DELLO STACK — due motori sotto un solo dominio, e perché

Il campo `costruzione` di ogni `scheda.json` dice `"squarespace"` per tutte e quattro, contro
`"artigianale"` per la pagina madre `armageddon.bsns.it/` (dossier 11) e per `claude-speedrun.com`
(dossier 12) e `apsales.eu` (dossier 13). Verificato, non solo letto:

| Prova | Dove | Cosa dice |
|---|---|---|
| Bundle CSS | `src/07-2bca9184-site.css` di ogni cattura, **1.243 KB** | è il `site.css` di tema Squarespace completo — non un CSS scritto a mano, un intero framework esportato |
| Nomi dei file sorgente | `website.components.accordion.styles.css`, `website.components.imageFluid.styles.css`, `commerce-*-min.it-IT.css`, `vuid.min.js`, `veils.css` | fingerprint di Squarespace 7.1, identici sulle quattro pagine, assenti sulla pagina madre (che ha un solo `armageddon.css` scritto a mano) |
| Percorso asset | `armageddon.bsns.it/assets/mirror/<hash>-<nome-file>.css` | le risorse Squarespace non sono servite da `squarespace-cdn.com`: sono state **scaricate e rimesse in casa** sotto lo stesso dominio |

Ma la prova che cambia la lettura del fatto sta nei commenti dentro `src/02-mirror.css` e
`src/03-mirror.js` (identici byte-per-byte sulle quattro pagine — stesso MD5 su tutte e quattro):

> *"Le pagine sono gli originali di andrei-copy.com, fogli di stile compresi. Questo file aggiunge
> solo quello che serve al funnel sopra: la barra sticky d'acquisto, e il marcatore sui video che
> devono ancora spostarsi su Vimeo."*
> *"Le pagine sono gli originali di andrei-copy.com con ogni script Squarespace rimosso, quindi
> tutto quello che la piattaforma pilotava in JavaScript ha smesso di funzionare."*

E il footer legale di tutte e quattro punta ancora a `www.andrei-copy.com/privacy-dati-cookie-simili`
(verificato in tutti e quattro i `copy-integrale.md`, riga identica).

**Cosa comporta, in pratica:**

1. **Non sono due stack scelti apposta per lo stesso lancio.** Sono un **archivio**: quattro pagine
   prodotto che vivevano su `andrei-copy.com` (il vecchio dominio Squarespace di Andrei Pascu, dove
   presumibilmente vendeva i mini-corsi uno per uno) sono state **catturate staticamente** — HTML,
   CSS, immagini scaricate in locale — e **rimesse in piedi** sotto `armageddon.bsns.it`, il dominio
   nuovo scritto a mano. Il JS di Squarespace è stato tolto (probabilmente per tagliare la
   dipendenza/il costo dell'abbonamento), e un piccolo `mirror.js` (353 righe, vanilla, stesso file
   sulle quattro pagine) **ricostruisce a mano** solo i tre comportamenti che servivano ancora:
   l'accordion delle lezioni, il ridimensionamento delle immagini fluide di Squarespace, e la
   correzione del bug "Indietro" (il tasto Indietro doveva essere premuto più volte per uscire dalla
   pagina, perché ogni scroll-to-anchor aggiungeva una entry nella history — bug riportato da un
   collaboratore interno di nome Andrei, corretto sostituendo `pushState` con `replaceState`).
2. **Non c'è più un acquisto individuale funzionante.** Le quattro pagine mostrano un prezzo
   "vecchio" barrato (vedi §4) ma **l'unico link di pagamento reale su tutte e quattro le pagine è
   lo stesso, identico URL Stripe**: `buy.stripe.com/00w28s9LA5Y0eIT8N64Ja1O` (verificato con
   grep su tutti e quattro i `scheda.json`: un solo risultato univoco). Le quattro pagine sono state
   **riconvertite da sales page singole a pagine di valore-stack** per un unico prodotto: l'Armageddon
   Pack a 199€. La matematica torna: 139 (outEmail) + 98 (outFunnel) + 98 (outHeadline) + 250
   (outViral) = **585€**, più il voucher da 199€ su Funnel Operator già documentato nel dossier 11
   (598€ + 199€ = **784€ di listino**, identico al numero che il dossier 11 riporta per il pacchetto
   completo) venduti a 199€.
3. **La correzione dei difetti è girata attorno all'originale, non dentro.** `contrast-fix.css`
   (122 righe, identico sulle quattro pagine) rialza a norma WCAG AA testo che nell'originale
   Squarespace era quasi invisibile (sezioni rilette a scuro con testo ancora chiaro-su-chiaro) —
   generato da uno script proprio (`tools/contrast.py`), non da Squarespace. Chi ha fatto il mirror
   ha **misurato e corretto** un difetto reale dell'originale invece di limitarsi a copiarlo.

Questo è il fatto operativo per la Fabbrica: **quando un asset di vendita smette di essere il
prodotto principale, non lo si butta e non lo si ricostruisce — lo si congela, lo si stacca dal
costo di piattaforma, e lo si riusa come giustificazione di valore per l'offerta che sta vendendo
davvero.** Vedi §7.

---

## 1. LA TABELLA DI CONFRONTO

Tutti i numeri sono letti dai quattro `scheda.json`, campo per campo — nessuno stimato.

| Campo | outEmail (14) | outFunnel (15) | outHeadline (16) | outViral (17) |
|---|---|---|---|---|
| Altezza desktop | 25.588px | 26.561px | 20.168px | **10.047px** |
| Altezza mobile | 24.113px | 26.612px | 20.903px | **15.209px** |
| Rapporto mobile/desktop | 0,94× (più corta) | 1,00× | 1,04× | **1,51×** |
| Sezioni totali | 24 | 24 | 19 | 10 |
| Sezioni distinte (gruppi) | 16 | 16 | 14 | **10** |
| Rapporto distinte/totali | 0,67 | 0,67 | 0,74 | **1,00** |
| Blocchi di copy | 238 | 194 | **280** | 149 |
| CTA (campo `cta[]`) | 21 | 14 | 10 | 13 |
| Media (img/svg/video/iframe) | 90 | **104** | 63 | 46 |
| Parole totali | 1.132 | 1.218 | 1.276 | 970 |
| Densità media per sezione | 6,6 | 13,6 | 9,7 | 12,2 |
| Font principale | Inter (152 usi) | Plus Jakarta Sans (76) | Elza (132) | Plus Jakarta Sans (57) |
| Peso dominante | 700 (119) / 300 (39) | 700 (111) / 300 (39) | 700 (156) / 300 (70) | 700 (75) / 300 (35) |
| Sfondo dominante | `#1b1b1d` scuro (42) | `#f4f4f3` chiaro (54) | `#1b1b1d` scuro (31) | `#f4f4f3` chiaro (28) |
| Colore testo dominante | `#fafafa` (141) | `#ffffff` (103) | `#fafafa` (129) | `#1b1b1d` (97) |
| Ombre distinte | 7 | 3 | 1 | **0** |
| Animazioni CSS | **1** (`pulseShadow`, 4 usi) | 0 | 0 | 0 |
| Prezzo individuale mostrato | €139 barrato | €98 barrato | €98 barrato | €250 barrato (×2) |
| FAQ | sì (4 domande) | sì (3 domande) | **no** | **no** |
| Sezione "perché comprare da me" | sì, esplicita | no | no | sostituita da una timeline autobiografica 2020-2024 |

Tre numeri saltano subito all'occhio: **outViral è l'unica pagina senza un solo blocco ripetuto**
(rapporto 1,00 — vedi §3), **outViral è anche l'unica che cresce del 51% passando al mobile** (le
altre tre restano entro il ±6%), e **l'effetto pulsante sul prezzo esiste su una sola pagina su
quattro** nonostante il ruolo del blocco sia identico sulle altre tre (§6).

---

## 2. LO SCHEMA RICORRENTE — la formula di pagina prodotto

Leggendo le quattro pagine in sequenza (sezioni ordinate per `y`, headings, `copy-integrale.md`)
emerge la stessa **formula in 11 tappe**. Non tutte e quattro le pagine la eseguono per intero: la
tabella sotto mostra dove ciascuna pagina la segue e dove devia.

| # | Tappa | outEmail | outFunnel | outHeadline | outViral |
|---|---|---|---|---|---|
| 1 | **Hero** — nome prodotto + promessa/gancio | sì — domanda scioccante ("Apriresti questa email?") su sfondo scuro | **devia** — nessuna promessa emotiva: un diagramma "funnel comune vs funnel vincente" su sfondo chiaro | sì — claim scioccante ("QUESTA È UNA HEADLINE.") su sfondo scuro | sì, ma diverso — collage di mockup + numero secco ("10K views") su sfondo chiaro |
| 2 | **Agitazione/problema** — la via sbagliata, spesso a fumetti/comic | sì — fumetto fotografico b/n (5 vignette) | sì — stesso device: fumetto fotografico b/n (7 vignette) | sì, ma via testo/statistiche, non fumetto | **assente come blocco a sé** — il problema entra dentro la timeline autobiografica (tappa 9) |
| 3 | **Prova del problema** — statistiche con fonte, esempio concreto | sì — 4 statistiche con link a fonte esterna (Wikipedia, altitudemarketing.com, getresponse.com) | sì — 5 statistiche con fonte (Segment, CoSchedule, Salesforce, HubSpot, MarketingWeek) | sì, senza citare fonti esterne | **assente** — sostituita da un grid di 6 creator reali con nome, foto, follower e link profilo |
| 4 | **Rivelazione del metodo** — "ecco cosa cambia" | sì | sì | sì — tool interattivo prima/dopo (bottone "Clicca qui" che trasforma un annuncio-burger) | sì — "outViral toglierà l'indovinare" |
| 5 | **Benefici a blocchi** (3 colonne, icone) | dentro il curriculum, non a sé | sì — sezione dedicata "outFunnel - benefici" (3 blocchi: lezioni complete / vai deep / not for the weak) | dentro il curriculum | dentro l'elenco lezioni |
| 6 | **Curriculum** — "Lista video-lezioni": 3 card di anteprima + accordion per sezione | sì — componente identico, accento blu | sì — **stesso identico componente grafico**, immagini di anteprima IDENTICHE a quelle di outEmail (vedi §6, difetto) | sì — stesso componente, accento verde | **devia** — layout a due colonne su fondo chiaro, mockup laptop invece del carosello scuro |
| 7 | **Qualificazione negativa** — "non è per tutti / non per principianti" | sì — lista di 3 X rosse | no | sì — stessa logica, resa con freccette verdi su gradiente | no |
| 8 | **Obiezioni dirette** — botta e risposta ("ma io già so scrivere", "uso ChatGPT") | sì (2 obiezioni) | no | sì (2 obiezioni: formule pre-fatte, ChatGPT) | no |
| 9 | **Autorevolezza/differenziazione** — perché comprare da Andrei | sì — sezione esplicita ("Andrei perché dovrei comprare outEmail e non i tuoi competitor?") | **assente** | sì — stessa logica, via track record | sostituita da una timeline in prima persona (2020 → 2024, tre citazioni datate) |
| 10 | **Valore/prezzo** — card con prezzo barrato + "INCLUSO NEL PACCHETTO ARMAGEDDON" | sì | sì | sì | sì — **compare due volte**, la prima già dopo l'hero (§4) |
| 11 | **FAQ** — accordion 3-4 domande | sì | sì | **no** | **no** |
| — | **Chiusura legale** — disclaimer + P.IVA, identico byte-per-byte | sì | sì | sì | sì |
| — | **Barra sticky costante** — "Prendi l'Armageddon Pack — 199€" / "Torna alla pagina principale" | sì | sì | sì | sì |

**Lettura:** outEmail è l'unica pagina che esegue la formula per intero, in ordine lineare — è
l'istanza di riferimento. outFunnel e outHeadline saltano ciascuna due tappe diverse (outFunnel:
qualificazione negativa e autorevolezza; outHeadline: benefici a sé e FAQ). outViral è la più
divergente: sostituisce due tappe intere (agitazione e prova) con un unico dispositivo — la
timeline autobiografica con prova sociale via creator reali — ed è l'unica a duplicare la tappa
prezzo. La tappa che **non manca mai**, su nessuna delle quattro, è il curriculum (6), il
prezzo/valore (10) e la chiusura legale — sono il nucleo non negoziabile della formula.

---

## 3. RIPETIZIONE vs LUNGHEZZA — cosa insegna

| Pagina | Sezioni totali | Sezioni distinte | Rapporto | Lunghezza |
|---|---|---|---|---|
| outEmail | 24 | 16 | 0,67 | 25.588px |
| outFunnel | 24 | 16 | 0,67 | 26.561px |
| outHeadline | 19 | 14 | 0,74 | 20.168px |
| outViral | 10 | 10 | **1,00** | 10.047px |

Il rapporto scende quasi linearmente con la lunghezza: le due pagine più lunghe (outEmail,
outFunnel) sono anche quelle che ripetono di più lo stesso blocco strutturale — 8 sezioni su 24 sono
copie dello stesso "firma" (stesso tag, stessa classe, stesso numero di figli, stesso schema
media/CTA) di un'altra sezione già vista. outViral, la più corta, non ripete **nessuna** sezione:
ogni schermo è un blocco diverso.

Cosa insegna: la ripetizione qui non è un difetto di distrazione, è la tecnica con cui una pagina di
25.000px viene costruita con **solo 16 componenti reali** — il resto è lo stesso componente
richiamato con contenuto diverso (il divisorio a tutta larghezza `div|section-border`, il blocco
"outX 🤝 [persona]" ripetuto 4 volte identico su outFunnel, il blocco prezzo/CTA riusato tre volte
su outEmail). È efficiente in produzione (un componente, N contenuti) ma è anche esattamente la
metrica che il dossier gemello [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) proponeva
come **gate futuro** ("firme ripetute / sezioni totali sotto soglia"): qui la soglia critica sembra
stare intorno a 0,65-0,70 — sotto quel rapporto la pagina rischia di leggersi come un template
riempito, non come una pagina scritta. Terza conferma indipendente della stessa regola, questa volta
con un range numerico misurato invece che una sola osservazione qualitativa.

---

## 4. LE CTA — quante, dove, come sono fatte

| Pagina | CTA totali (`cta[]`) | y uniche | Prima CTA | Ultima CTA | Passo medio tra CTA uniche |
|---|---|---|---|---|---|
| outEmail | 21 | 15 | y=1.082 (**4,2%** pagina) | y=25.066 (98,0%) | 1.713px |
| outFunnel | 14 | 13 | y=20.389 (**76,8%** pagina) | y=25.959 (97,7%) | 464px |
| outHeadline | 10 | 10 | y=5.967 (29,6% pagina) | y=15.387 (76,3%) | 1.047px |
| outViral | 13 | 9 | y=4.188 (41,7% pagina) | y=8.113 (80,8%) | 491px |

**outFunnel non offre nessun elemento cliccabile per il primo 76,8% della pagina** — quasi 20.000px
di solo problema/agitazione/prova prima del primo bottone (il selettore di persona "Sono un
copywriter / media buyer / titolare / project manager"). È la deviazione più forte della famiglia su
questo asse: le altre tre mettono un primo punto di contatto entro il 42% della pagina.

**Come sono fatte, misurato:** i bottoni "primari" che portano all'ancora `#<slug>-price` sono
identici su tre pagine su quattro nella forma — `radius: 10px`, `padding: 16px 22.4px`, `size: 16px`,
`weight: 600` — ma **non nel colore**: blu `#0062ff` su outEmail, non presenti come bottone unico su
outFunnel/outHeadline (lì il "bottone" principale a metà pagina è il selettore di persona, sfondo
`#1b1b1d` scuro con testo `#a8a8a8` grigio-chiaro — basso contrasto per essere il punto di
interazione più importante della sezione). **L'unico bottone che porta davvero a un pagamento** — la
barra sticky "Prendi l'Armageddon Pack — 199€" — usa un **terzo colore mai visto altrove sulla
pagina**, `#bc0807` rosso scuro, `radius: 0px`, identico byte per byte sulle quattro pagine (stesso
markup, stesso file `mirror.css`). Tutte le altre CTA (`#<slug>-price`) sono **ancore che scorrono
alla card prezzo**, non pulsanti di acquisto — l'unico link `buy.stripe.com` verificato su tutte e
quattro le pagine sta dentro quella barra sticky (§0).

Non tutto ciò che il campo `cta[]` conta è persuasivo: su outEmail, degli 21 elementi, **7 sono i
badge "Open" decorativi** della finta inbox (nessun `href`) e **4 sono le etichette delle sezioni
del curriculum** (nessun `href`, sono titoli in stile bottone). Le CTA che portano davvero da
qualche parte, su outEmail, sono **6**: cinque ancore al prezzo più il bottone Stripe della barra.

---

## 5. IL COPY — teardown della struttura ricorrente

Le quattro pagine condividono lo stesso scheletro retorico. Citazioni vere, prese da
`copy-integrale.md`.

**Promessa** (sempre nel titolo, mai nel sottotitolo)
- outEmail: *"Apriresti questa email?"* → *"Impara a scrivere email performanti"*
- outFunnel: *"E poi c'è chi fa questo: Quello che funziona."*
- outHeadline: *"E solo i copywriter che scrivono HEADLINE persuasive sono disperatamente
  richiesti… E guadagnano di più."*
- outViral: *"Ottieni una media di 10K views nei tuoi prossimi video"*

**Problema** (colpa condivisa, mai solo del lettore)
- outEmail: *"L'email marketing 'classico' è morto. […] E i killer siamo stati noi… Noi marketer."*
- outFunnel: *"Alcuni fanno questo funnel… …E altri fanno questo… E poi c'è chi fa questo"*
  (il diagramma a imbuto vs il diagramma a grafo)
- outHeadline: *"Se scrivi titolo non persuasivo, la gente non legge… Se la gente non legge, al 100%
  non compra."*
- outViral: *"'Cosa ca**o sto sbagliando?' - cit. Andrei Pascu, 2020"*

**Prova** (statistica con fonte, o dimostrazione)
- outEmail: *"il lavoratore d'ufficio medio riceve 121 email di marketing al giorno"* (fonte:
  altitudemarketing.com)
- outFunnel: *"313% in più di successo per aziende con marketing strategico"* (fonte:
  coschedule.com)
- outHeadline: dimostrazione interattiva ("Clicca qui" trasforma l'headline dell'annuncio-burger)
  invece di una statistica
- outViral: prova sociale diretta — 6 creator reali, nome+foto+follower+link profilo verificabile

**Obiezioni** (solo su 2 delle 4 pagine)
- outEmail: *"'Ma io so già scrivere email'"* → *"Bene, allora sei in target."*
- outHeadline: *"'Ma io le faccio scrivere a ChatGPT'"* → *"Ma se non conosci le strategie, non puoi
  usare l'AI responsabilmente."*
- outFunnel e outViral: **nessuna obiezione esplicita nel testo**

**Prezzo** (sempre barrato, mai il prezzo "vero" scritto per esteso nel copy)
- Le quattro card prezzo (€139 / €98 / €98 / €250) sono **immagini**, non testo semplice — tre delle
  quattro non compaiono nella scansione testuale di `copy-integrale.md` proprio per questo (§6). Il
  solo prezzo leggibile come testo piatto è quello di outViral: *"250,00 € — Una tantum"*.

**Garanzia** — **assente su tutte e quattro le pagine.** Nessuna occorrenza di "garanzia",
"rimborso" o "soddisfatti" riferita al prodotto (verificato con ricerca testuale sui quattro
`copy-integrale.md`). Coerente con il posizionamento "Non è per tutti. Sono serio." — una garanzia
esplicita avrebbe stonato con la cornice di esclusività — ma resta un vuoto reale, non
un'interpretazione.

**Chiusura** (identica, non solo simile)
Tutte e quattro finiscono con lo stesso disclaimer legale parola per parola — verificato anche
contro il footer della pagina madre (dossier 11): *"Questo sito e i consigli contenuti al suo
interno sono opinioni personali a scopo educativo basate sull'esperienza di Andrei Pascu…"* seguito
da *"Andrei Pascu Sales · P.I. 02001850474 · Viale Giacomo Matteotti 15, 50121 Firenze (FI)"*.

---

## 6. I DIFETTI REALI MISURATI

1. **Le immagini di anteprima del curriculum sono copiate, non aggiornate.** Il carosello "Lista
   video-lezioni" di outFunnel mostra **le stesse identiche tre card** di outEmail — stesso testo
   nelle miniature ("Lezione 9: Opzioni per il lead magnet", "Lezione 10: Tipi di sequenze
   automatiche + follow up", "Lezione 11: Opzioni per upsell/cross-sell base") — argomenti di email
   marketing, non di funnel. Verificato aprendo entrambi gli screenshot
   (`14-.../sezioni/18-lista-video-lezioni.png` e `15-.../sezioni/21-div.png`): pixel-identiche.
2. **L'effetto che dovrebbe richiamare l'attenzione sul prezzo esiste su una pagina su quattro.**
   Solo outEmail ha un'animazione attiva (`pulseShadow 3s ease`, bagliore ciano pulsante sulla card
   prezzo, 4 usi). outFunnel, outHeadline e outViral non hanno **nessuna** animazione CSS — la card
   prezzo, sullo stesso ruolo, è statica. `ombre` distinte: 7 su outEmail, 3 su outFunnel, 1 su
   outHeadline, **0 su outViral**.
3. **Nessun prezzo individuale "vero" è più leggibile come testo semplice** su tre pagine su quattro
   (§4) — sono immagini. Chi audita il copy via strumenti di testo (screen reader compreso, in
   assenza di `alt` adeguato) non vede il numero.
4. **outViral cresce del 51% sul mobile** (10.047px → 15.209px) contro un ±6% delle altre tre — la
   griglia a 3 colonne dei 6 creator e il layout a due colonne del curriculum impilano pesantemente,
   più delle altre pagine con contenuti equivalenti.
5. **Nessuna garanzia/rimborso su nessuna delle quattro pagine** (§5) — un vuoto di risposta
   all'obiezione più ovvia ("e se non funziona per me?"), specie dove mancano anche le obiezioni
   dirette (outFunnel, outViral).
6. **Il bottone più importante di una sezione (selettore di persona su outFunnel) ha basso
   contrasto**: sfondo `#1b1b1d`, testo `#a8a8a8` — una combinazione che sulle altre pagine è
   riservata a testo secondario, non a un elemento interattivo primario.
7. **Zero urgenza/scarsità su tutte e quattro le pagine** — nessun countdown, nessuna data di
   scadenza (verificato: nessuna occorrenza di "scadenza", "countdown" o "mezzanotte" nei quattro
   `copy-integrale.md`), a differenza della pagina madre che ha un countdown live per la chiusura
   del pacchetto (dossier 11). La leva urgenza vive solo sulla pagina che chiude, non su quelle che
   costruiscono valore — divisione del lavoro retorico corretta, ma vale la pena notare che nessuna
   delle quattro rimanda esplicitamente alla scadenza nemmeno con una riga di testo.

---

## 7. IL DELTA ALLA FABBRICA

| # | Cosa | Entra? | Motivo |
|---|---|---|---|
| 1 | Il device "pagina prodotto congelata come pagina di valore-stack per un bundle" (§0) | **Sì, come pattern operativo** — non un file CSS/HTML, ma una tecnica di funnel: quando un prodotto smette di vendersi da solo, la sua pagina non si butta, si stacca dal costo di piattaforma (mirror statico) e si riusa per giustificare il prezzo di un pacchetto più grande | Osservato qui per la prima volta nell'ecosistema Andrei Pascu; utile per `PIANO-MAESTRO` più che per `canone.css` — va discusso come pratica, non come token |
| 2 | Il componente "curriculum": 3 card anteprima + accordion per sezione | **Da valutare, non da copiare 1:1** — il principio (mostrare 2-3 lezioni vere prima dell'elenco completo) è generico e riusabile; l'esecuzione qui è già un `<details>` nativo altrove nello stesso ecosistema (pattern `faq-native`, dossier 11) — se lo importiamo, importiamo la versione nativa già in canone, non questa (basata su JS custom ricostruito in `mirror.js`) |
| 3 | La qualificazione negativa a lista X ("non è per te se…") | **Conferma, non pattern nuovo** — stessa logica già presente altrove nell'ecosistema Andrei Pascu; qui arriva una quarta istanza (2 su 4 pagine di questa famiglia) — rafforza la regola già scritta, non ne crea una |
| 4 | I token colore delle quattro pagine (`#0062ff`, `#bc0807`, `#7ab641`, `#9027ff`…) | **No** | sono colori-di-prodotto Squarespace ereditati da `andrei-copy.com`, non un sistema deliberato — nessuna sovrapposizione utile con `canone.css` |
| 5 | Il rapporto "sezioni distinte / sezioni totali" come soglia di gate | **Sì, rafforza il gate proposto nel dossier 13** — terza conferma indipendente, e la prima con un range numerico misurato (0,67-0,74 nelle pagine lunghe, 1,00 nella pagina corta) invece di una sola osservazione qualitativa |
| 6 | L'assenza di garanzia/urgenza su pagine di solo valore-stack | **No, solo annotazione** | non è un pattern da copiare, è un'osservazione sul funnel altrui da tenere a mente quando si progetta la sequenza urgenza/valore delle nostre pagine multi-step |
| 7 | Il difetto delle immagini-anteprima riciclate senza controllo (§6.1) | **Sì, come voce del gate** — "ogni asset visivo riusato fra pagine sorelle deve essere verificato contro il contenuto reale di quella pagina", controllo meccanico e a basso costo da aggiungere a `scripts/gate_siti.py` quando si costruiscono famiglie di pagine prodotto | un errore già osservato una volta (qui, due volte nello stesso mirror) — per la regola del dossier `CLAUDE-SITI.md` §10, un errore visto due volte diventa un controllo del gate |

**Il pezzo che entra davvero:** il rapporto sezioni-distinte/sezioni-totali come soglia di gate
(riga 5) e il controllo anti-riciclo delle immagini di anteprima (riga 7). Il resto o non entra
(i colori, ereditati non progettati) o entra come nota operativa per il piano, non come riga di
codice (riga 1).

---

## Collegamenti

- [11-armageddon.md](11-armageddon.md) — la pagina madre, il countdown, il prezzo del pacchetto
  completo (784€ di listino, 199€ di vendita — la matematica di §0 chiude su questi numeri)
- [14-17-famiglia-out-ATLANTE.md](14-17-famiglia-out-ATLANTE.md) — le sezioni per ruolo con gli
  screenshot aperti
- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — dove nasce l'idea del gate
  "firme ripetute / sezioni totali sotto soglia", qui confermata con un terzo caso
- `.claude/skills/fabbrica-siti/pattern/faq-native/scheda.md` — il pattern `<details>` nativo già in
  canone, più leggero della versione JS custom vista in queste quattro pagine
- `.claude/skills/fabbrica-siti/pattern/coda-legale/scheda.md` — il footer legale, verificato
  identico byte-per-byte su queste quattro pagine e sulla pagina madre
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
