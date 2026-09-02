---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #sales-page #copy-teardown #ebook #lead-magnet #pricing
Created: 2026-09-02
Last updated: 2026-09-02
---

# STUDIO SITO 06 — andrei-copy.com/manuale-del-copywriter (eBook, 79 €)

**URL:** https://www.andrei-copy.com/manuale-del-copywriter
**Titolo SEO:** `Libro di Copywriting - Manuale del copywriter di Andrei Pascu - Soldi online — AP Formazione`
**Prezzo:** **79,00 €** — eBook, 115 pagine
**Altezza:** 11.067px desktop · 14.237px mobile (+28,6%) · **Blocchi:** 139 · **CTA:** 7 · **Media:** 52
**Catturato:** 2026-09-01 — 13 slice desktop 1440×900 + 17 mobile 390×844
**Fonti grezze:** `capture/06-manuale-del-copywriter/`

> **La pagina più corta dell'ecosistema a pagamento** — un terzo di `/copy`, metà di `outheadline` — eppure vende un prodotto reale. Non è pigrizia: è che **il lavoro di convincimento è delegato a un'anteprima gratuita** piazzata a metà pagina. Qui la pagina non deve convincere: deve consegnare l'anteprima.

---

## 1. LA COSA PIÙ IMPORTANTE DI QUESTA PAGINA

Le altre pagine dell'ecosistema (`funnel-operator`, `outheadline`, `outfunnel`, `copy`) sono lunghe **perché devono chiudere la vendita dentro la pagina**. Questa no.

A metà pagina (y=5462, cioè al **49% dell'altezza**) c'è un form email che regala pagine vere del libro:

> *"Ho pescato (casualmente) alcune pagine del libro… E le puoi leggere adesso."*

Da lì in poi la pagina serve solo a chi ha già scaricato, o a chi vuole comprare senza anteprima. **L'anteprima è il vero venditore**, e sostituisce due cose che in questo ecosistema non esistono mai:
1. **La garanzia di rimborso** — assente qui come su tutte le altre pagine (scoperta trasversale #4). Al suo posto: *leggi un pezzo prima di pagare*.
2. **Le testimonianze** — su questa pagina sono **zero**. Nessuna recensione, nessuno screenshot di risultati, nessun numero di copie vendute.

**Regola estratta:** su un prodotto informativo a basso prezzo la prova non è la testimonianza, è **il campione del prodotto stesso**. Costa zero produrlo (esiste già) e ha una credibilità che nessuna testimonianza raggiunge.

> **Correzione a una scoperta precedente.** Avevo scritto "la lunghezza del copy è funzione del prezzo". Questa pagina la smentisce da sola: 79 € su 11.067px contro 98 € su 21.119px (`outheadline`). La regola vera, misurata su 6 pagine, è: **la lunghezza è funzione di quanto lavoro deve fare la pagina**. Se un'anteprima gratuita fa il lavoro, la pagina si accorcia della metà.

---

## 2. PALETTE — misurata su `getComputedStyle`, non stimata

### Testo
| Hex | Usi | Dove |
|---|---|---|
| `#1b1b1d` | **86** | Nero-inchiostro: tutto il corpo su fondo chiaro/grigio |
| `#a8a8a8` | 23 | Grigio: testo sulle sezioni scure **e** testo dei bottoni scuri |
| `#fafafa` | 16 | Bianco sporco: sezioni immagine-fondo scure e footer |
| `#ffffff` | 3 | Solo UI del player video |
| `#919090` | 3 | Micro-copy sotto il form opt-in |
| `#e7e7e7` | 2 | Etichette del player |
| `#ebe9e0` | 2 | Riga legale nel footer |
| `#51b216` | **1** | **Verde, una sola volta**: la parola *"gratuita"* |
| `#ffffff @0.35` | 1 | Divisore footer |

### Sfondi
| Hex | Usi | Ruolo |
|---|---|---|
| `#1b1b1d` | **93** | Nero: nav, card, tutti i bottoni d'acquisto |
| `#a8a8a8` | **28** | **Il grigio medio è il fondo del `<body>`** |
| `#fafafa` | 4 | Sezioni chiare |
| `#0062ff` | **3** | Blu: banner brand, skip-link, **footer a tutta pagina** |
| `#000000 @0.5` | 1 | Bottone play |
| `#a8a8a8 @0.33` / `@0.3` | 2 | Velature |

### Le tre cose che contano
1. **`body_bg = #a8a8a8`** — un grigio medio come fondo pagina. È l'unico sito dell'ecosistema che non parte da bianco o nero. Effetto: il nero `#1b1b1d` non "spara", e le foto prodotto (copertina nera) si fondono col fondo invece di stagliarsi.
2. **Il blu `#0062ff` sopravvive solo in tre punti**, e nessuno dei tre vende: banner di servizio, skip-link, footer istituzionale APsales. **La pagina prodotto rinuncia al colore d'azione del brand** e usa il nero per i bottoni. Conferma la scoperta trasversale #1 (un prodotto = una pelle), qui in versione estrema: la pelle è *assenza di colore*.
3. **Il verde `#51b216` compare una volta sola in tutta la pagina**, sulla parola `gratuita`. Un colore intero speso per una parola. È la mossa cromatica più efficiente che ho misurato nell'ecosistema.

---

## 3. TIPOGRAFIA — misurata

**Famiglie: 5** (`plus-jakarta-sans-o8l9cc` 73 · `elza-8u3n84` 52 · `Clarkson, Arial` 6 · `"DM Sans"` 5 · `Poppins` 1).
Reali: **due** (Jakarta + Elza). Le altre tre sono detriti: Clarkson è la UI del player, DM Sans **tutti i bottoni**, Poppins lo skip-link. `body_font` dichiara `sans-serif`, cioè il fallback di sistema.

### Scala misurata
| Dimensione | lh | Peso | Usi | Ruolo |
|---|---|---|---|---|
| 60,8px | 64,8 | 700 | 5 | H1 di sezione ("Libri di business", "…ho le prove") |
| 48px | 52,9 | 700 | 8 | H2 di svolta ("non un romanzo") |
| 38,4px | 43,5 | 700 | 15 | H3 di blocco |
| 30,5px | 30,5 | 700 | 3 | Occhiello "- Anteprima gratuita -" |
| 24px | 28,2 / normal | 700 | **42** | H4 e voci di elenco capitoli — **il livello più usato** |
| 20,8px | 37,4 | 300 | 2 | Nome prodotto nella card |
| 17,6px | 31,7 | 300 | 2 | Prezzo "79,00 €" |
| 16px | 28,8 | 300 | **30** | Corpo |
| 16px | 28,8 | 700 | 10 | Grassetti dentro il corpo |
| 12,5px | 22,6 | 300 | 6 | Micro-copy legale |

**Rapporto pesi: w700 su 83 blocchi, w300 su 41.** Il 60% dei blocchi è in grassetto. Nell'hub era il 13%. Coerente con la scoperta trasversale #5, con una differenza: qui il grassetto **non** serve a farsi leggere in diagonale su 20.000px, serve perché **il livello 24px/700 fa da impalcatura**: i 21 titoli dei capitoli sono tutti a 24px/700, e da soli sono 42 blocchi su 139.

**Il prezzo è il testo più discreto della pagina**: `79,00 €` a 17,6px in peso 300, dentro la card prodotto, mai nell'headline, mai vicino a un titolo. Compare 2 volte in 11.067px.

---

## 4. STRUTTURA E POSIZIONE DEGLI ELEMENTI

| y (px) | % pagina | Sezione | Fondo |
|---|---|---|---|
| 0–90 | 0% | Nav nera fissa: `Claude Speedrun` (sinistra) · logo (centro) · `Accedi` (destra) | `#1b1b1d` |
| 90–627 | 1–6% | **Hero**: mockup tablet+telefono a sinistra (333×376), copy a destra centrato | Foto texture inchiostro 1440×627 |
| 699–1090 | 6–10% | *"Guarda sto video 👇🏻"* + video 3:33 (394×222) | `#a8a8a8` |
| 1236–1600 | 11–14% | H1 *"✨ Libri di business ✨"* + due colonne di problema | `#a8a8a8` |
| 1713–2116 | 15–19% | *"Perché la maggior parte dei libri dicono tanto e nulla?"* | Foto texture 1440×403 |
| 2163–2420 | 20–22% | H2 *"Il copywriting è un business, non un romanzo"* | `#a8a8a8` |
| 2487–2990 | 22–27% | **4 pilastri** in griglia 2×2, icone PNG 45×45 | `#a8a8a8` |
| 3041 | 27% | H2 *"Ed è ciò che il Manuale del copywriter offre."* | |
| 3194–3460 | 29–31% | **Carosello 12 item** (190×254), frecce circolari 36px ai bordi | |
| 3506–5685 | 32–51% | **Blocco anteprima**, fondo immagine unico da **2.179px** | `banner v1.jpg` |
| 5462–5560 | 49% | **FORM OPT-IN** — input + bottone chiaro 201×64 + micro-copy privacy | |
| 5761–6340 | 52–57% | Due obiezioni di formato + **card prodotto 79 €** (192×192) | `#a8a8a8` |
| 6397–7487 | 58–68% | **Bio autore** su fondo bianco topografico, 4 foto sparse | `background white.png` |
| 7534–8700 | 68–79% | **Indice capitoli**: due accordion affiancati (7 parti · 11 manuali) | Foto texture |
| 8853–9600 | 80–87% | **FAQ**, 8 domande in accordion a tutta larghezza | `#a8a8a8` |
| 9900–10250 | 89–93% | Card prodotto ripetuta + icone pagamento + *"✅ Pagamento sicuro SSL"* | Foto grana |
| 10480–11067 | 95–100% | **Footer APsales blu pieno** con statua dithered, 5 link, disclaimer | `#0062ff` |

**Layout:** colonna centrata ~740px su viewport 1440. L'hero è l'unico blocco a due colonne asimmetriche (immagine 333px a sinistra, testo a destra). Tutto il resto è centrato o in griglia 2 colonne. Nessuna sidebar, nessuna barra sticky di acquisto, nessun contatore.

---

## 5. COMPONENTI — inventario con misure reali

### I 7 bottoni
| y | Testo | Dimensioni | Fondo / Testo | Raggio | Font |
|---|---|---|---|---|---|
| 514 | `Acquista 🔥 Per accesso istantaneo` | 323×54 | `#1b1b1d` / `#a8a8a8` | 10px | DM Sans 600 16px |
| 947 | `Riproduci` | 44×44 | `#000 @0.5` / `#fff` | 100% | — |
| **5462** | **`Ricevi l'anteprima`** | **201×64** | **`#a8a8a8` / `#1b1b1d`** | 10px | DM Sans 600 |
| 6257 | `Compralo e scaricalo` | 192×74 | `#1b1b1d` / `#a8a8a8` | 10px | DM Sans 600 |
| 7347 | `Voglio imparare da te` | 208×53 | `#1b1b1d` / `#fafafa` | 10px | DM Sans 600 |
| 8113 | `Passa al contenuto` (skip-link, x=−14272) | 188×53 | `#0062ff` / `#fafafa` | 10px | Poppins 500 |
| 10091 | `Acquista` | 113×53 | `#1b1b1d` / `#a8a8a8` | 10px | DM Sans 600 |

**Due cose misurate, non interpretate:**
- **Il bottone dell'anteprima è l'unico chiaro e l'unico alto 64px.** Tutti i bottoni d'acquisto sono scuri e alti 53–74px. L'inversione cromatica dice: *questo non è un acquisto*.
- **Il testo delle CTA cambia con lo stato emotivo della sezione**, mai ripetuto uguale:
  `Acquista 🔥 Per accesso istantaneo` (hero: velocità) → `Compralo e scaricalo` (dopo l'obiezione portabilità: azione fisica) → **`Voglio imparare da te`** (dopo la bio: relazione, prima persona, si parla all'autore non al carrello) → `Acquista` (checkout finale: nessun aggettivo).

### Media
52 elementi: 15 immagini reali, 6 `img` con `src` vuoto (carosello in lazy-load mai risolto), video `blob:` 394×222, il resto SVG di interfaccia.
**Tre immagini di fondo a tutta larghezza fanno da separatori di capitolo**: texture inchiostro 627px e 403px, `banner v1.jpg` da **2.179px** (l'intera sezione anteprima), `background white` da 1.090px (bio).

### Raggi
`10px` (6 — tutti i bottoni) · `4px` (2) · `50%` e `100%` (3 — elementi circolari) · `20px`, `15px`, `26px`, `50px` (1 ciascuno). Sistema dichiarato: 10px. Il resto è deriva.

---

## 6. COPY — teardown sezione per sezione, con il perché

### 6.1 Hero
```
- eBook sul Copywriting -
Impara la skill più importante: la vendita scritta
(in 115 pagine pratiche)

Questo libro è l'equivalente della cintura nera in Copywriting, solo che al posto
di metterci anni ci metti 115 pagine. Saprai come vendere qualsiasi cosa a chiunque,
con formule PRATICHE che potrai applicare subito.
```
**Perché funziona.** Tre mosse in quattro righe:
1. **Categoria dichiarata prima del beneficio** (`- eBook sul Copywriting -`): chi non vuole un ebook se ne va subito. Filtro, non vendita.
2. **La promessa non è il risultato, è la compressione del tempo**: *anni → 115 pagine*. La metafora della cintura nera importa uno standard esterno riconosciuto (arti marziali) e lo scambia con un numero verificabile.
3. **Il numero di pagine è ripetuto tre volte in tre righe** (115, 115, e "pratiche"). Su un ebook il numero di pagine è l'unica unità di misura che il compratore possiede: sostituisce il "quante ore di video".

Grassetti sul solo `qualsiasi cosa a chiunque` e `subito.` — cioè su ampiezza e velocità, le due variabili che giustificano 79 €.

### 6.2 Il video: *"Guarda sto video 👇🏻"*
48px, bianco, romanesco volutamente sciatto. Un video di **3:33** subito sotto la piega. Nessun titolo che spieghi cosa contiene, nessuna trascrizione, nessun sottotitolo nel DOM. Il registro parlato ("sto video") è una scelta di prossimità: dopo un headline formale, la voce si abbassa.

### 6.3 Il manifesto anti-categoria
```
✨ Libri di business ✨

✨ 1 concetto in 200 pagine ✨          Finisci il libro che non sai cosa fare
```
**La mossa migliore della pagina.** Non attacca un concorrente: attacca **l'intera categoria di prodotto** a cui il suo prodotto appartiene. Due colonne, due modi di dire la stessa accusa: i libri di business sono gonfi.

Poi la spiegazione del movente altrui — che è ciò che rende l'accusa credibile invece che risentita:
> *"Perché devono. Alla fine se un libro è troppo corto le persone lo vedono come 'superficiale'. Quindi tanti autori si mettono a fare libri su argomenti semplici rendendoli complessi, noiosi e ripetitivi per avere qualche pagina in più da farti leggere."*

**Perché è forte:** non dice "gli altri sono disonesti", dice "gli altri sono **costretti** da un incentivo di mercato". Chi legge non deve giudicare persone, deve solo riconoscere un meccanismo. E il meccanismo lo ha già visto.

Segue la separazione: *"Io non sono 'tanti autori' e non me ne frega di cosa pensano gli altri."* — e qui il grassetto prende una frase intera, la più lunga in bold della pagina: *"L'unico mio obiettivo con il manuale che ho scritto è aiutarti a creare il migliore copy che tu abbia mai scritto. Il resto è secondario."*

### 6.4 *"Il copywriting è un business, non un romanzo"*
48px, grassetto solo su `non un romanzo`. Riporta il tema dal prodotto (libro) al risultato (soldi), e prepara l'unico numero personale della sezione: *"per imparare a fare copy e superare i **10 mila euro mensili** di fatturato non ho usato un paio di concetti da un paio di libri di decenni fa…"*.
**Nota:** *"decenni fa"* è un attacco alla bibliografia classica del copywriting (Ogilvy, Halbert, Sugarman) senza nominare nessuno. Ritorna alla fine con *"Io sono un copywriter adesso"*.

### 6.5 I 4 pilastri — struttura contrappositiva
Griglia 2×2. Ogni pilastro è **titolo positivo (38,4px) + sottotitolo negativo (24px)**:

| Pilastro | Sottotitolo | Cosa nega |
|---|---|---|
| **Pratico** | *non noioso, pieni di esempi* | i manuali teorici |
| **Facile da utilizzare** | *concetti chiari, non da leggere e dimenticare* | i libri che non si consultano |
| **Aggiornato al 2025** | *non scopiazzato da altri libri vecchi* | i classici tradotti |
| **Con strategie innovative** | *non con le solite due formule* | AIDA e PAS |

**Il pattern è "X, non Y" quattro volte di fila.** Ogni promessa arriva già accoppiata all'alternativa che il lettore ha già provato e trovato insufficiente. È il modo più economico di fare comparazione competitiva senza una tabella comparativa.

Chiusura: *"Ed è ciò che il Manuale del copywriter offre."* — il prodotto entra **solo dopo** che i criteri di scelta sono stati stabiliti da lui. Chi legge non valuta più il libro: valuta se il libro rispetta i quattro criteri che ha appena accettato.

### 6.6 La cerniera dell'anteprima
```
- Anteprima gratuita -            (grigio, con "gratuita" in VERDE #51b216)
Il manuale ti dice esattamente come/cosa scrivere per vendere…
…E se non ci credi, ho le prove.
```
Due H1 da 60,8px separati da 291px di vuoto e una doppia freccia giù. **La struttura è quella di un botta-e-risposta interno**: affermazione grossa → obiezione implicita del lettore ("dici tutti così") → *ho le prove*.

Poi due card scure affiancate:
- **La mia promessa per te** — *"Niente storielle, niente esempi inutili… Ogni pagina di questo manuale ti dice cosa fare nel tuo copy."*
- **Per mostrarti che io mantengo le promesse…** — *"Ho pescato **(casualmente)** alcune pagine del libro… E le puoi leggere adesso."*

**La parola che fa tutto il lavoro è `(casualmente)`, tra parentesi.** Se le pagine fossero scelte, sarebbero le migliori — cioè non rappresentative. Dichiarando la casualità, il campione diventa **una statistica sul prodotto intero**. È la stessa logica del "apri una pagina a caso in libreria", riportata online dove non puoi sfogliare.

### 6.7 Il form opt-in
```
Ricevi un'anteprima gratuita del manuale
Dimmi la mail dove inviarti l'anteprima (lo faccio in questo istante) ⬇️
[ Indirizzo e-mail ] [ Ricevi l'anteprima ]
Non invio spam. Ti puoi disiscrivere in qualsiasi momento. Qui trovi l'informativa sul trattamento dei tuoi dati.
```
Misurato: **un solo campo**, bottone chiaro 201×64, micro-copy a 12,5px in `#919090`.

Perché è fatto bene, punto per punto:
- **"Dimmi la mail"** — imperativo rivolto a sé, non all'utente ("inserisci la tua email"). Sposta l'azione sul venditore.
- **"(lo faccio in questo istante)"** — risolve l'unica vera obiezione di un opt-in: *quando arriva?*
- **"⬇️"** — indica il campo, non il bottone. Riduce l'ambiguità di dove cliccare.
- **Tre rassicurazioni in una riga di 12,5px**: niente spam, disiscrizione, link all'informativa. La proporzione è giusta: la riga esiste, ma non pesa quanto la promessa.

È l'applicazione letterale di quanto insegna nel video 4 cat2 ([[Source_Andrei_Pascu_10_Lead_Magnet]]): campo unico, promessa specifica, tempo di consegna dichiarato.

### 6.8 Le due obiezioni di formato
| Obiezione reale | Titolo | Come la chiude |
|---|---|---|
| *"un ebook non si consulta"* | **Ho sempre odiato sfogliare libri** | *"strutturato in maniera pratica e schematica. Troverai la strategia o la formula che farà la differenza in pochissimi secondi"* |
| *"voglio la carta"* | **Sarà sempre con te** | *"Sono in viaggio in treno, in aereo o in qualche hotel… È il 2025, e questo libro puoi averlo sul tuo telefono o sul PC. **Prego.**"* |

**Entrambe partono da un'antipatia dell'autore, non da un vantaggio del prodotto** ("ho sempre odiato", "non sono sempre in ufficio"). Il difetto del formato digitale viene trasformato nella ragione per cui il formato è stato scelto. Il *"Prego."* finale — una parola, punto — è l'unico momento arrogante della pagina, ed è piazzato dove il lettore sta già cedendo.

### 6.9 Bio — *"Okay, ma chi sono io per parlarti di copywriting?"*
Domanda posta **al posto del lettore**, con "Okay" iniziale che simula il turno di parola. I dati, nell'ordine: 2019 come anno d'inizio · *">10 mila euro al mese solo grazie al copywriting"* (grassettato) · *"clienti da tutto il mondo"* (grassettato) · **270 mila persone tra i vari canali social** (link) · community.

Poi la chiusura identitaria, 24px/700:
> *"Io sono un copywriter **adesso**. Non voglio parlarti di strategie che funzionavano qualche anno fa… Voglio insegnarti ciò che funziona nel presente."*

**È la sua difesa contro l'unico attacco serio a un libro di copywriting**: che sia teoria riscaldata. Trasforma la giovinezza professionale (5 anni) da debolezza in argomento.
CTA: `Voglio imparare da te` — **l'unica CTA della pagina che parla del rapporto invece che del prodotto**, ed è l'unica messa dopo la bio. Non è un caso.

### 6.10 Indice capitoli — la trasparenza come strumento di vendita
> *"Voglio che tu sappia con chiarezza che tipi di investimento stai per fare, pertanto eccoti i contenuti del manuale."*

Due accordion affiancati, con l'etichetta della differenza dichiarata: **Parti = sezioni teoriche · Manuali = sezioni pratiche**.

| Parti (teoria) | Manuali (pratica) |
|---|---|
| 1 Cos'è il copywriting | 0 Fasi di scrittura di un copy |
| 2 Perché questo libro è importante | 1 Attenzione |
| 3 Come usare questo libro | 2 Problema |
| 4 Perché le persone comprano | 3 Soluzione |
| **5 La struttura base del copywriting (APSOC)** | 4 Obiezioni |
| 6 I tipi di copywriting | 5 CTA |
| 7 Componente emotiva nel copywriting | 6 Target |
| | 7 Funnel |
| | 8 Storytelling VS Direct response |
| | 9 Conseguenza del non agire + urgenza di tempo |
| | 10 Altre strategie, terminologia e regole |

**18 voci mostrate gratis.** Il rischio percepito ("e se dentro non c'è niente?") viene chiuso mostrando l'intero sommario. E i cinque manuali 1–5 (Attenzione, Problema, Soluzione, Obiezioni, CTA) **sono APSOC** — la stessa struttura che è anche lo standard di copy di Digital Empire ([[Digital_Empire_APSOC]]): il libro è, letteralmente, il manuale di quel framework.

### 6.11 FAQ — 8 domande
`Il libro come lo scarico?` · `Quanto è lungo il libro?` · `Quanto costa?` · **`Cosa cambia tra il corso e il libro?`** · `Questo manuale è adatto anche ai principianti?` · `Posso leggere il manuale su tutti i dispositivi?` · `Questo manuale è solo per chi vuole diventare copywriter professionista?` · `Ho degli amici interessati al libro, possiamo acquistarlo insieme?`

Tre note:
1. **`Cosa cambia tra il corso e il libro?`** — gestisce la cannibalizzazione interna dentro la FAQ, dove costa meno. Il prodotto da 999 € viene protetto qui, non nella pagina di vendita.
2. **`Ho degli amici interessati…`** — è una domanda di *acquisto di gruppo*, cioè un'obiezione di prezzo travestita. Trattarla come logistica invece che come sconto è una scelta di posizionamento.
3. `Quanto costa?` nella FAQ mentre il prezzo è già nella card: ridondanza voluta per chi cerca il numero con Ctrl+F.

### 6.12 Chiusura e footer
Card prodotto ripetuta identica (`Manuale del copywriter` · `79,00 €` · `Acquista`) + icone PayPal/Visa/Mastercard/Apple Pay + *"✅ Pagamento sicuro SSL"*.
Footer **blu `#0062ff` a tutta pagina** con logo **APsales**, statua dithered, 5 link (La mia storia · Store · Recensioni · Risorse · Blog) e il disclaimer legale completo con P.IVA fiorentina.

**Il footer è l'unico punto in cui il brand-madre APsales appare**: la pagina prodotto è neutra, l'azienda compare solo alla fine. Separazione deliberata tra chi vende (Andrei) e chi fattura (Andrei Pascu Sales).

---

## 7. DIFETTI REALI — misurati, non opinioni

1. **Il banner delle scuse.** In basso a sinistra, fisso su desktop e mobile, per tutta la pagina:
   > *"● Stiamo aggiornando il brand — Potresti trovare colori strani, font sbagliati, o simili."* + bottone blu `Capito`

   È un avviso di cantiere **in produzione, su una pagina che incassa**. Su mobile (390px) la card copre parte del bottone `Acquista 🔥` dell'hero — misurato sullo screenshot `mobile-01.png`. **Costo reale: il primo CTA della pagina è parzialmente coperto sul dispositivo maggioritario.** Chi arriva non sa che il brand è in transizione: sa solo che la pagina si scusa da sola.
2. **Contrasto insufficiente nella sezione anteprima.** Titoli `#a8a8a8` su fondo chiaro `#fafafa`: rapporto ~2,2:1, sotto il minimo WCAG AA (4,5:1) per testo normale — e il testo grande resta comunque al limite. È la sezione che porta all'opt-in, cioè la più importante della pagina.
3. **5 famiglie di font e `body_font: sans-serif`.** Il fondo della cascata tipografica è il font di sistema: se un webfont non carica, la pagina cade su Arial.
4. **6 immagini del carosello con `src` vuoto** al momento della cattura (lazy-load non risolto anche dopo scroll forzato). Il carosello dichiara `Item 1 of 12` ma ne serve al massimo 6.
5. **Zero prove sociali.** Nessuna testimonianza, nessun numero di copie vendute, nessuna recensione — su una pagina che vende un libro. L'unico numero verificabile è "270 mila persone tra i vari canali social", che riguarda l'autore, non il libro. Coerente con l'ecosistema, ma qui è più esposto: `/copy` almeno aveva le testimonianze video.
6. **La nav non porta da nessuna parte tranne che a un altro prodotto.** Due voci: `Claude Speedrun` (link esterno) e `Accedi`. Nessun ritorno allo store, nessun menu. Chi vuole vedere altro deve scendere di 11.000px fino al footer.
7. **Mobile +28,6%** (14.237px) senza riduzione di contenuto: le griglie 2×2 diventano pile verticali, il carosello resta.

---

## 8. LE 8 MOSSE DA PORTARE IN DIGITAL EMPIRE

1. **L'anteprima gratuita al 49% della pagina sostituisce la garanzia.** Per il *Manuale Claude Code* (prodotto strutturalmente identico: ebook, prezzo simile) è la mossa più direttamente trasferibile che abbia misurato. Un campione a caso vale più di una promessa di rimborso.
2. **`(casualmente)` tra parentesi.** Dichiarare che il campione non è scelto trasforma l'estratto in prova statistica. Costa una parola.
3. **Un colore intero per una parola sola.** Il verde `#51b216` su *"gratuita"* è l'unico uso in 11.067px. Applicabile a qualunque nostra landing: il colore d'accento non deve decorare, deve marcare **la parola che decide il click**.
4. **Attaccare la categoria, non i concorrenti** — e spiegare il **movente** dell'avversario ("perché devono") invece della sua cattiveria. Fa credibilità senza fare polemica, e non nomina nessuno che possa rispondere.
5. **"X, non Y" ripetuto 4 volte** come tabella comparativa implicita: ogni pilastro nega esplicitamente l'alternativa che il lettore ha già provato.
6. **Il testo della CTA cambia con lo stato emotivo, mai ripetuto uguale.** In particolare: dopo il blocco biografico la CTA parla del rapporto (`Voglio imparare da te`), non del prodotto. Da inserire come regola in `market-landing`.
7. **Mostrare l'intero sommario prima dell'acquisto**, con l'etichetta esplicita di cosa è teoria e cosa è pratica. 18 voci gratis chiudono l'obiezione "dentro non c'è niente" meglio di qualunque aggettivo.
8. **Le obiezioni di formato si chiudono partendo da un'antipatia dell'autore**, non da un vantaggio del prodotto ("ho sempre odiato sfogliare libri"). Il difetto diventa la ragione della scelta.

### E una da NON copiare
**Il banner delle scuse.** Se il brand è in transizione, si spedisce comunque coerenti: nessun cliente ha bisogno di sapere che il font è sbagliato. Un avviso del genere su una pagina di vendita trasferisce al compratore un problema che è nostro. Vale come regola per `empire-premium-style`: **mai spedire un avviso di cantiere su una pagina che incassa.**

---

## 9. UNA COSA CHE CHIUDE UNA DOMANDA APERTA DI IERI

Nella nav di questa pagina, primo link a sinistra, misurato nel DOM a `y=8121`:

```
<a href="https://claude-speedrun.com">Claude Speedrun</a>
```

**`claude-speedrun.com` è promosso dalla barra di navigazione del sito principale di Andrei Pascu.** Non è un sito omonimo né un caso di somiglianza: è **un prodotto suo**, spinto dalla nav di tutte le pagine di `andrei-copy.com`.

Questo chiude *chi è* — resta aperto *chi è arrivato prima* sul linguaggio visivo `#fb4604` + Onest condiviso con `ccm-premium`, che si misura solo con le date (Wayback Machine). Vedi [07-claude-speedrun.md](07-claude-speedrun.md).

---

## Connessioni

- [[Source_Andrei_Pascu_10_Lead_Magnet]] — video 4 cat2: questa pagina è la sua stessa lezione applicata (campo unico, promessa specifica, consegna immediata)
- [[Source_Andrei_Pascu_Importanza_Landing]] — video 5 cat2: la teoria della landing minima
- [07-claude-speedrun.md](07-claude-speedrun.md) — il prodotto linkato dalla nav
- [05-copy-mentorship.md](05-copy-mentorship.md) — il corso da 349/999 € protetto dentro la FAQ di questa pagina
- [01-andrei-copy-home.md](01-andrei-copy-home.md) — l'hub da cui si arriva
- `.claude/skills/market-landing/SKILL.md` — dove va la regola sulle CTA a testo variabile
- `.claude/skills/lead-magnets/SKILL.md` — dove va "il campione del prodotto come lead magnet"
