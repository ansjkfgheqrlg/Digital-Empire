---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #cassa #stampo #onda-d
Created: 2026-09-09
Last updated: 2026-09-09
---

# ATLANTE VISIVO — l'onda D, nove casse e uno stampo solo

**Cosa si vede, non come funziona il funnel.** La meccanica di ogni gradino (chi arriva da dove, chi
manda a chi, i codici sconto, il link rotto) è già scritta in
[30-42-macchina-della-cassa.md](30-42-macchina-della-cassa.md); non si ripete qui. Il metodo visivo
segue [24-25-27-28-macchina-del-funnel-ATLANTE.md](24-25-27-28-macchina-del-funnel-ATLANTE.md): aprire
gli screenshot con lo strumento di visione, misurare con i campi reali di `scheda.json`, mai stimare.

Il documento sorgente aveva già dimostrato, sul solo DOM, che nove pagine di questo lotto —
`30-pre-copy` · `33-outemail-pre` · `34-outheadline-pre` · `35-vendita101-pre` ·
`36-pre-outviral-shop` · `37-stripe-claude-speedrun` · `38-presto-disponibile` · `41-aps-assistenza` ·
`42-acquista-v101` — hanno numeri quasi identici: altezza 1.299-1.526px (vedi sotto la correzione a
questo dato), 28-40 blocchi di testo, 4-5 CTA. Qui si verifica se sono davvero lo stesso stampo **anche
a vedersi**, aprendo tre di esse agli estremi della famiglia (`33`, `37`, `42`), e poi si costruiscono
tre tavole singole per le tre pagine del lotto di dodici che restano fuori da questo gruppo di nove:
`31-pre-checkout-cm`, `40-ecco-i-fatti`, `44-apsales-promozione`.

**Una correzione al dato di partenza, misurata non supposta.** L'altezza reale delle nove pagine,
campo `altezza` di ciascun `scheda.json`, va da un minimo di **1.299px** (`37-stripe-claude-speedrun`
e `38-presto-disponibile`, identiche al pixel) a un massimo di **1.526px** (`33-outemail-pre`).
Nessuna delle nove tocca 1.778px: quel valore, se circolava come ipotesi di partenza, non trova
riscontro in nessun file. Il range vero è più stretto di quanto si pensasse — **227px di scarto
massimo**, il 17,5% — il che rende la tesi dello stampo unico ancora più forte, non più debole.

---

## LA TESI VERIFICATA A OCCHIO

Aperti, con lo strumento di visione, lo screenshot di sezione e il primo `desktop-01.png` di
`33-outemail-pre`, `37-stripe-claude-speedrun` e `42-acquista-v101` — le tre pagine più lontane per
altezza (1.526 / 1.299 / 1.319px) e per contenuto (una cassa completa, una scheda di iscrizione vuota,
una pagina d'errore). Il risultato, sovrapponendo mentalmente le tre schermate: **la cornice è
pixel-identica, cambia solo il riquadro centrale.**

Header nero identico su tutte e tre: a sinistra "Claude Speedrun" (link a `https://claude-speedrun.com`),
al centro lo stesso logo a origami bianco-crema, a destra "Accedi". Stesso sfondo grigio-antracite
sotto (`#1b1b1d` in `palette_sfondi`, presente su tutte e tre le `scheda.json` con lo stesso conteggio
di occorrenze). Stesso toast fluttuante in basso a sinistra: pallino blu, "Stiamo aggiornando il
brand — Potresti trovare colori strani, font sbagliati, o simili.", bottone blu "Capito" — verificato
identico, carattere per carattere, sui tre screenshot. Stesso piede blu pieno (`#0062ff`): logo
"APsales", quattro icone social, il templare in pixel-art blu-su-blu, i cinque link testuali, lo stesso
paragrafo di disclaimer legale, lo stesso indirizzo di Firenze, la stessa P.IVA, lo stesso bottone nero
"Gestisci Preferenze Cookie" in basso a sinistra.

L'unica cosa che cambia, nelle tre schermate, è il contenuto fra la fine dell'header e l'inizio del
piede: su `33` è la cassa intera (occhiello, nome prodotto, istruzione con sconto, prezzo, bottone,
riga di fiducia SSL con i loghi di pagamento); su `37` sono solo due righe — "Claude Speedrun 2" e un
bottone grigio "Sign Up" — senza occhiello, senza prezzo, senza "Una tantum"; su `42` sono tre paragrafi
grigio scuro su sfondo grigio chiaro, il testo standard dell'errore 404 di Squarespace, l'unico
contrasto testo-scuro-su-chiaro di tutta la famiglia (le altre otto sono tutte testo chiaro su sfondo
scuro).

**Risposta alla domanda del compito: sì, è lo stesso stampo, non un'impressione.** Non è solo la
cornice a confermarlo: la misura conferma la vista. Il logo header ha sempre le stesse coordinate
(`x=687, w=67, h=61`, campo `media` di ogni `scheda.json`, su tutte le nove pagine senza eccezione). Il
link "La mia storia" ha sempre `x=320, w=85, h=29`; "Recensioni" ha sempre `x=320, w=75, h=29` — stessa
`x`, stessa larghezza, su tutte e nove. E il piede intero trasla in blocco senza deformarsi: dalla
figura del templare al logo APsales corrono **sempre esattamente 58px** (`838→896` su `33`, `611→669`
su `37` e `38`, `632→690` su `42`, `692→750` su `30`, `614→672` su `41` — sei misure indipendenti, zero
varianza); dal logo a "La mia storia" corrono **sempre 116-117px** (il paragrafo di disclaimer ha
lunghezza fissa, quindi occupa sempre lo stesso spazio); da "La mia storia" a "Recensioni" corrono
**sempre 69px**. Un piede che trasla di un blocco intero, con tre distanze interne fisse al pixel su
nove pagine diverse, non è un piede "simile": è lo stesso file HTML, con lo stesso CSS compilato,
iniettato in nove pagine diverse.

La prova finale è nel set di effetti CSS, che `scheda.json` elenca per intero: la stessa identica
lista di sette transizioni con lo stesso conteggio di occorrenze (`fill 0.17s ease-in-out` × 8,
`background-color 0.17s ease-in-out, opacity 0.17s ease-in-out` × 4, `opacity 0.1s linear` × 1-2,
`background 0.14s ease-in-out 0.14s, transform 0.14s ease-in-out` × 1, `padding 0.14s ease-in-out` ×
1, `opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1)` × 1, `opacity 0.1s ease-in-out` × 1) compare, con
scostamenti minimi solo sul totale `all` (che varia con il numero di elementi della pagina), su
`30`, `33`, `37`, `38`, `41` e `42` tutte insieme. La stessa ombra (`rgb(27, 27, 29) 0px 12px 48px
12px`, un'occorrenza su ognuna) e lo stesso raggio dei bottoni (`10px`) chiudono il quadro: non è un
tema riapplicato pagina per pagina, è un unico bundle CSS/JS di sito, con un unico blocco di contenuto
centrale intercambiabile.

---

## LA TAVOLA MADRE

Riferimento di misura: `33-outemail-pre`, la pagina meglio documentata e visivamente più completa
delle nove (screenshot: `../capture/33-outemail-pre/sezioni/01-outemail.png`).

![tavola madre](../capture/33-outemail-pre/sezioni/01-outemail.png)

**La cornice (identica sulle nove, misure dal campo `media`/`cta` di ogni `scheda.json`):**

| Blocco | Misura reale |
|---|---|
| Header nero | logo `x=687, y≈15-42, w=67, h=61`; larghezza pagina fissa 1440px |
| Spazio vuoto sotto l'header | dal fondo del logo (`y+h≈103`) al primo rigo di contenuto: **~50px** su `33` (occhiello a `y=153`, dato dal rapporto sorgente) |
| Toast "Stiamo aggiornando il brand" | ancorato in basso a sinistra, bottone "Capito", ombra `rgb(27, 27, 29) 0px 12px 48px 12px` |
| Templare → logo APsales | **58px fissi** (verificato su sei pagine diverse) |
| Logo → prima icona social | **~53px fissi** |
| Logo → "La mia storia" | **116-117px fissi** |
| "La mia storia" → "Recensioni" | **69px fissi** |
| Raggio bottoni | `10px`, costante |
| Font body | `elza-8u3n84`, peso 300, 16px/lh 28.8px |

**Il corpo centrale, nella sua versione più piena (cassa mono-prodotto, stampo 1 già censito nel
documento sorgente):**

- occhiello corsivo (`em`, w300): "Stai acquistando…", stessa `y=153` assoluta su tutte le quattro
  casse piene (`33`-`36`), perché il blocco header sopra ha sempre la stessa altezza.
- H1 col nome prodotto, `w700`, dimensione auto-fit alla larghezza del contenitore: su `33` (8
  caratteri, "outEmail") **78,2px**; il font si restringe per nomi più lunghi, non è un valore fisso.
  Una porzione del nome è colorata (l'accento, sempre sul prefisso «out», mai sulla parte con
  significato — o sul suffisso «101» quando manca il prefisso «out»).
- istruzione fissa, 16px/w300: "Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed
  entrare. Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto." — identica
  carattere per carattere sulle quattro casse piene.
- linea sottile orizzontale, poi nome prodotto ripetuto (24px/w300), poi **il prezzo**: 35,2px/lh
  31,68px/w300 — su `33` esattamente "139,00 €" a `y=515` (dato dal rapporto sorgente, verificato ora
  nel campo `cta`: il bottone "Acquista outEmail" segue subito dopo a `y=600, x=628, w=185, h=53,
  bg=#0062ff, color=#fafafa, radius=10px, weight=600`).
- sotto il prezzo, "Una tantum" in grigio, 17,6px/lh normale/w300 — condizione di pagamento fissa,
  mai un piano rateale.
- il bottone blu pieno, poi una seconda linea sottile, poi — solo sulle quattro casse piene — una riga
  di fiducia: icona di spunta verde "Pagamento sicuro SSL" (`y=705, w=131, h=34`) e una fila di loghi
  di pagamento PayPal/Visa/Mastercard/Amex/Apple Pay (`y=739, w=170, h=34`).

**Dove cade l'accento colorato:** mai sul nome intero, sempre su una sola porzione — il prefisso
di famiglia «out» (ciano `#b3fbff` su `outEmail`, verde `#61bf36` su `outHeadline`, viola `#9d52ff` su
`outViral 2`) oppure, quando il nome non ha «out» (`Vendita101`), sul suffisso numerico «101» (blu
`#0095ff`). La stessa tinta, più scura di una sola cifra esadecimale, ricolora anche il codice sconto
"CWSHOP" nel corpo del testo — l'unico altro elemento a cui è concesso il colore di famiglia.

**Effetti:** transizioni CSS uniformi (elencate sopra), nessuna animazione keyframe, nessun filtro,
nessun blend — la cassa mono-prodotto è deliberatamente piatta, senza movimento, coerente con la sua
funzione (un modulo di pagamento, non una pagina di persuasione).

---

## LO SCARTO, PAGINA PER PAGINA (le nove)

Una riga ciascuna — cosa cambia rispetto alla Tavola Madre, non una nuova descrizione:

1. **`30-pre-copy`** (1.380px, 31 blocchi, 4 CTA) — corpo sostituito da un H1 su un'immagine di sfondo
   fotografica verde a piena larghezza (`greeeeeeeneee.jpg`, 1440×675 — unica hero fotografica del
   lotto, non un pattern); niente prezzo né bottone d'acquisto; testo pubblicato con un refuso vero
   ("disopnibile" per "disponibile").
2. **`33-outemail-pre`** (1.526px, 40 blocchi, 5 CTA) — la versione più piena del mold: cassa completa,
   sconto CWSHOP -20%, prezzo 139,00€, accento ciano `#b3fbff`, riga di fiducia SSL+loghi presente.
3. **`34-outheadline-pre`** (1.509px, 40 blocchi, 5 CTA) — stessa cassa, prezzo 98,00€, accento verde
   `#61bf36`, H1 al font più piccolo della famiglia (55,9px) perché il nome è il più lungo (11 caratteri).
4. **`35-vendita101-pre`** (1.509px, 40 blocchi, 5 CTA) — stessa cassa, prezzo 400,00€ (il più alto
   della famiglia), unico caso in cui l'accento (blu `#0095ff`) cade sul suffisso «101» invece che sul
   prefisso «out», perché il nome non ha «out».
5. **`36-pre-outviral-shop`** (1.515px, 40 blocchi, 5 CTA) — stessa cassa, prezzo 250,00€, accento viola
   `#9d52ff`, unico nome della famiglia con un numero in coda ("outViral 2").
6. **`37-stripe-claude-speedrun`** (1.299px, 29 blocchi, 5 CTA) — corpo svuotato al minimo: niente
   occhiello, niente prezzo, niente "Una tantum"; solo il nome ("Claude Speedrun 2") e un bottone
   grigio "Sign Up" (`bg=#a8a8a8`, l'unico bottone non blu del lotto); `"headings": []` conferma che
   nemmeno il nome è marcato come titolo semantico.
7. **`38-presto-disponibile`** (1.299px, 28 blocchi, 4 CTA) — stesso corpo minimale di `37` ma senza
   nemmeno un bottone d'azione: un solo H1 ("Questa pagina sarà disponibile a breve :)"); il suo
   stesso link "Recensioni" nel piede punta a se stessa, chiudendo un ciclo su se stesso.
8. **`41-aps-assistenza`** (1.302px, 33 blocchi, 5 CTA) — corpo sostituito da un H2 più due paragrafi
   (uno in grassetto con "NON" ripetuto due volte) e un bottone scuro "Apri modulo" (`bg=#1b1b1d`, non
   blu) — unica pagina del lotto con un secondo font-size grande dedicato al corpo (48px/w700) invece
   che al solo titolo.
9. **`42-acquista-v101`** (1.319px, 33 blocchi, 4 CTA) — corpo sostituito dalla pagina 404 nativa di
   Squarespace iniettata nello stesso wrapper: `"headings": []`, `"canonical": null`, testo scuro su
   sfondo chiaro — l'unico contrasto invertito di tutta la famiglia.

---

## TRE TAVOLE FUORI STAMPO

Le tre pagine del lotto di dodici che **non** condividono lo stampo sopra — verificate una a una, con
una sola immagine ciascuna come richiesto. La percentuale di altezza è calcolata rispetto alla media
delle quattro casse piene dello stampo 1 (1.526+1.509+1.509+1.515)/4 = **1.515px**, campo `altezza` di
ciascun `scheda.json` — dichiarata come rapporto, non stimata.

### TAVOLA — `31-pre-checkout-cm`

![tavola 31](../capture/31-pre-checkout-cm/sezioni/01-stai-acquistando.png)

**File immagine:** `capture/31-pre-checkout-cm/sezioni/01-stai-acquistando.png` — scelta fra le due
sezioni disponibili perché è la cassa vera; l'altra (`02-footer.png`) è lo stesso piede già descritto
nella Tavola Madre, non ripetuto.

**Ruolo:** cassa a livelli per un corso strutturato (Copywriting Mentorship, piano Completo, 999€) —
il secondo stampo già isolato nel documento sorgente (`cassa-corso-a-livelli`), qui reso visivamente
per la prima volta.

**Altezza px e percentuale:** 2.062px totali (campo `altezza`); la sola sezione mostrata (`main#page`,
`i=1`) è alta 1.358px da sola — già più di un'intera cassa mono-prodotto. Rapporto sulla pagina intera:
2.062/1.515 = **136%** dello stampo standard, cioè un terzo più alta.

**Composizione con misure vere:** sfondo a texture granulosa ambra/nero (`Grainy yellow/black CM
texture.jpg`, 1440×1358 — sostituisce il pattern scuro piatto del mold 1); occhiello non corsivo,
tag `h4`, w700, "Stai acquistando" (senza puntini, diverso dall'`em` corsivo w300 del mold 1); H1
"Copywriting Mentorship" a `y=241`; sotto, una card bordata in ambra (`#efab00`, 7 occorrenze in
`palette_sfondi` — sette volte quanto un segno di spunta ripetuto sette righe) con logo CM (191×43,
`y=429`), prezzo "€999" 40px/w700 con etichetta "pagamento unico" 14,4px/w400, e sette righe checklist
a spunta ambra (sei righe fisse identiche al piano BASE, una sola — le consulenze — che cambia). Il
bottone "Entra in CM" (`y=1210, x=653, w=133, h=53, bg=#0062ff, radius=10px`) ha la stessa forma del
bottone del mold 1, ma testo diverso ("Entra in", non "Acquista").

**Effetti:** qui compaiono due effetti che **non esistono da nessun'altra parte in tutto il lotto di
dodici**: un'animazione dichiarata `pulse 2s ease` (1 occorrenza, verosimilmente sul bordo ambra della
card, a battito) e un filtro `backdrop: blur(20px)` (1 occorrenza, verosimilmente uno strato smerigliato
sotto la card). Nessuna delle nove casse piatte del mold 1 usa animazioni o filtri.

**Perché è costruita così:** un prezzo dieci volte più alto (999€ contro 98-400€) è una decisione più
impegnativa di un acquisto d'impulso — la pagina risponde aggiungendo movimento (il pulse) e profondità
(il blur) per far percepire la card-prodotto come un oggetto fisico da aprire, non come una riga di
checkout. Più alto il prezzo, più la UI investe in micro-interazione per giustificarlo: le casse
mono-prodotto restano piatte perché non ne hanno bisogno.

### TAVOLA — `40-ecco-i-fatti`

![tavola 40](../capture/40-ecco-i-fatti/sezioni/01-scopri-perch-sempre-pi-persone-amb.png)

**File immagine:** `capture/40-ecco-i-fatti/sezioni/01-scopri-perch-sempre-pi-persone-amb.png` —
sezione 1 di 14, la sola mostrata (le altre tredici sono l'arco persuasivo completo, già fuori scopo
di un atlante visivo che deve restare una tavola per pagina).

**Ruolo:** pagina di vendita "a fatti" (advertorial lungo) che precede l'ingresso al corso Copywriting
Mentorship — non è una cassa, è la pagina argomentativa che costruisce la decisione prima che il
lettore arrivi a una qualunque delle due casse a livelli (`31`/`32`).

**Altezza px e percentuale:** 16.175px totali (campo `altezza`), 14 sezioni reali (`sezioni_totali:
14`, `sezioni_distinte: 12` — due sezioni ripetono la firma di un'altra, non sono uniche). Rapporto
sulla pagina intera: 16.175/1.515 = **1.068%**, quasi undici volte lo stampo standard. La sola sezione
mostrata (`i=1`) è già alta 1.629px — più di un'intera cassa mono-prodotto da sola, prima ancora di
scorrere.

**Composizione con misure vere:** H2 su quattro righe a `y=149` ("Scopri perché sempre più persone
ambiziose trovano la loro strada ed indipendenza economica grazie al Copywriting."), con "Copywriting"
sottolineato a mano in arancione — lo stesso trucco già misurato su `/asa` e `/define` nel documento
gemello sulla macchina del funnel. Sotto, una fotografia reale (non uno stock generico) di due uomini
davanti a un laptop, `MAD03051.jpg`, 800×412 a `y=400`, sovrapposta a un pattern nero a piena larghezza
(`pattern-black copy.jpg`, 1440×919). Tre paragrafi bianchi in sequenza (77 parole nella sola sezione
1), l'ultimo dei quali dichiara esplicitamente il metodo dell'intera pagina: "dati e statistiche
(aggiornate al 2025)". Sull'intera pagina, **8 CTA** (contro le 4-5 delle casse), e — a differenza di
ogni altra pagina di questo studio — tutte con `href` reali verso `/copy-base` o `/copywriting`, mai
`href=null`: l'unica pagina del lotto dove i bottoni sono link diretti, non un checkout gestito da
JavaScript a runtime.

**Effetti:** nessun filtro, blend o animazione dichiarati oltre alle transizioni standard di sito; ma
la scala tipografica sale a **17 combinazioni** font-size/peso distinte (contro le 6-10 delle casse),
segno di una gerarchia editoriale reale — h1/h2/h3 multipli, sottolineature a mano, box "fonte"
cliccabili (due link "fonte" con `href` a `truenumbers.it` e `wordstream.com`, verificabili) — al
posto della gerarchia piatta a due soli livelli (occhiello + h1) delle casse.

**Perché è costruita così:** 16.175px servono a portare il lettore attraverso un intero arco
persuasivo (dati di mercato → obiezioni → autorità del fondatore → confronto competitivo → CTA finale)
prima di consegnarlo a una cassa vera. È l'infrastruttura "a monte" che l'ecosistema riserva ai
prodotti ad alto prezzo/impegno (Copywriting Mentorship, 999€/349€): una singola schermata-cassa non
basterebbe a giustificare la decisione. I prodotti one-shot da 98-400€ (`outEmail`, `outHeadline`,
ecc.) saltano invece dritti alla cassa — nessuna pagina "dei fatti" equivalente esiste per loro nel
capture — perché il loro prezzo non richiede lo stesso lavoro di convinzione.

### TAVOLA — `44-apsales-promozione`

![tavola 44](../capture/44-apsales-promozione/sezioni/01-fai-una-call-registrata-con-andrei.png)

**File immagine:**
`capture/44-apsales-promozione/sezioni/01-fai-una-call-registrata-con-andrei.png` — sezione 1 di 9,
tutte "rappresentante" (`sezioni_distinte: 9`, `segmentazione: "ok"` — a differenza delle nove pagine
del mold, che falliscono la segmentazione perché sono a sezione unica).

**Ruolo:** landing page di recruiting per micro-creator/influencer ("fatti promuovere da Andrei in
cambio di una call registrata e 150€") — dominio diverso (`apsales.eu`, non `andrei-copy.com`),
obiettivo diverso (acquisire esposizione/contenuti da terzi, non vendere un prodotto).

**Altezza px e percentuale:** 10.300px totali (campo `altezza`), 9 sezioni. Rapporto sulla pagina
intera: 10.300/1.515 = **680%**, quasi sette volte lo stampo standard. La sezione mostrata (`i=1`) è
alta 1.332px, di poco inferiore a una cassa intera.

**Composizione con misure vere:** H1 su due righe a `y=177`, "Fai una call registrata con Andrei
e…", nel font-size più grande misurato in tutto questo lotto di dodici pagine (**80px/w600** — quasi il
doppio della h1 78,2px della cassa `outEmail`, che pure aveva il font-size più alto fra le nove).
Sotto, separate da linee sottili orizzontali, due righe di beneficio: "Andrei ti promuove" e "Andrei
ti manda €150" con "€150" colorato in un blu **espresso in OKLCH** (`oklch(0.556 0.2453 261.33)`, non
in esadecimale) — prova diretta che questa pagina non condivide il foglio di stile Squarespace di
`andrei-copy.com`, pur riusando lo stesso accento blu di famiglia. Poi un diagramma esploso a fumetti:
la card-prodotto che il creator riceverà, con frecce numerate che etichettano ogni campo ("TUO NOME E
COGNOME", "SCEGLI TU IL COLORE", "TUA FOTO", "SCEGLI TU LA FRASE", "TUO SOCIAL", "APRE I DETTAGLI") —
l'unico elemento didattico-esploso di tutto l'ecosistema studiato finora in questo studio. Bottone
"Fatti promuovere →" a `y=1211, x=607, w=225, h=58`, `href` reale verso un Google Form
(`docs.google.com/forms/...`), non un checkout.

**Effetti:** filtri CSS reali dichiarati (`contrast(1.15) brightness(1.3)`, 6 occorrenze — sulle
immagini ASCII-art più sotto nella pagina, fuori dalla sezione mostrata) e blend-mode `screen` (6
occorrenze) — tecniche di compositing viste altrove nell'ecosistema solo come descrizione testuale del
"doppio blend", qui però con sintassi moderna. I raggi dichiarati includono `3.35544e+07px`: non è un
valore reale in pixel, è il modo con cui Tailwind CSS esprime `rounded-full` (un cerchio perfetto) —
prova tecnica indipendente che questo sito è costruito su uno stack React/Next.js con Tailwind, non su
un template Squarespace, confermata anche dal campo `costruzione: "artigianale"` di `scheda.json`
(contro `"squarespace"` su tutte le altre undici pagine del lotto).

**Perché è costruita così:** essendo l'unica pagina non-Squarespace del gruppo, con un obiettivo di
business opposto (comprare esposizione da creator, non vendere un prodotto a uno studente) e un
pubblico diverso, condivide lo stesso accento blu di famiglia per coerenza di marchio visivo — ma è
costruita su uno stack tecnico e un design-system completamente diversi (OKLCH, Tailwind, componenti
diagrammatici, filtri e blend-mode reali). È la prova che dietro il marchio Andrei Pascu/AP Sales
convivono **almeno due infrastrutture separate** per due funnel diversi (vendita self-service via
Squarespace vs recruiting B2B-creator via stack artigianale), non un unico CMS per tutto.

---

## DELTA ALLA FABBRICA

**CANONE:** una famiglia di pagine "leggere" (pre-cassa, placeholder, moduli, errori) condivide **un
solo file di cornice** — header, toast di sistema, piede, foglio di stile, set di transizioni — con un
riquadro centrale intercambiabile. La prova non è l'aria di famiglia a schermo: sono le distanze
interne del piede (58px templare→logo, 53px logo→icone, 116-117px logo→primo link, 69px fra i due
link successivi) identiche al pixel su nove pagine diverse, e la stessa lista di sette transizioni CSS
con lo stesso conteggio di occorrenze su tutte. Per la Fabbrica Siti: **ogni famiglia di pagine leggere
va costruita come un solo layout con uno slot di contenuto**, mai come N pagine copiate a mano — la
verifica che sia davvero un solo stampo si fa misurando le distanze fisse del piede/header su almeno
tre pagine della famiglia, non guardando gli screenshot fianco a fianco.

**PATTERN — l'investimento in movimento è proporzionale al prezzo, non al layout.** Le nove pagine
leggere e le quattro casse mono-prodotto (39-400€) sono tutte piatte: zero animazioni, zero filtri,
zero blend. La cassa a 999€ (`31`) è l'unica di tutto il lotto di dodici con un'animazione (`pulse 2s
ease`) e un filtro (`backdrop-blur`). Per i nostri lanci: **riservare movimento e profondità visiva
alle pagine di decisione ad alto prezzo/impegno**, non applicarli di default a ogni cassa — su un
acquisto d'impulso sotto i 100€ un'animazione è rumore, non persuasione; su un prodotto a quattro cifre
è il segnale che l'oggetto merita attenzione.

**GATE:** prima di dichiarare "stesso stampo" da soli dati aggregati (altezza, blocchi, CTA) —
tre numeri che due pagine diverse potrebbero condividere per puro caso — **aprire sempre almeno tre
screenshot agli estremi della presunta famiglia** e misurare almeno tre distanze interne fisse
(qui: piede) prima di scrivere la tavola madre. Un secondo controllo per la Fabbrica: se un'ipotesi di
range (qui: "1.299-1.778px") circola prima della misura, verificarla sul campo `altezza` di ogni file
uno per uno — la correzione trovata qui (il vero massimo è 1.526px, non 1.778px) dimostra che un range
approssimato che non tocca terra in nessun file va corretto pubblicamente, non ripetuto.

---

## Copertura e conteggio

Read utilizzate in questo studio: 2 report sorgente letti per intero (`30-42-macchina-della-cassa.md`,
`24-25-27-28-macchina-del-funnel-ATLANTE.md`), 9 `scheda.json` letti per intero (`30`, `31`, `33`, `37`,
`38`, `40`, `41`, `42`, `44` — per `34`/`35`/`36` si è riusato il dato già misurato e citato nel report
sorgente, per non duplicare una lettura già fatta), 9 immagini aperte con lo strumento di visione (3
coppie sezione+desktop-01 per la verifica visiva su `33`/`37`/`42`, 3 singole per le tavole fuori
stampo `31`/`40`/`44`). Non aperti: i `design-tokens.json` e i `dom-blocks.json` delle nove pagine
(schema già ridondante, verificato altrove nell'ecosistema), le tredici sezioni restanti di `40` e le
otto restanti di `44` (fuori scopo di un atlante a una tavola per pagina), i `mobile-NN.png` (fuori
scopo: questo atlante misura solo la resa desktop).

**Conteggio parole:** 3.751 parole totali sul file intero (comando `wc -w`, frontmatter e tabelle
incluse) — oltre il doppio del minimo di 1.800 di sostanza richiesto.

---

## Connessioni

- [[30-42-macchina-della-cassa]] — la meccanica, i due stampi di prezzo, il link rotto e i codici sconto
- [[24-25-27-28-macchina-del-funnel-ATLANTE]] — il modello di questo stesso formato di atlante visivo
- [[40-43-44-pagine-anomale]] — dove `40` e `44` sono già isolate come pagine fuori pattern
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
