---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #copy-teardown #sales-page #outfunnel #machine-v2
Created: 2026-09-07
Last updated: 2026-09-07
---

# 04 — outFunnel — teardown di copy, macchina v2

**Fonte:** `capture/04-outfunnel/` — catturato 2026-09-07 — **26.993px** desktop, **24 sezioni (16
distinte)**, **215 blocchi di testo**, **17 CTA** (`scheda.json → cta[]`).
**Standard di forma:** [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md).
**Rapporto precedente (macchina v1, 2026-09-01):** [04-outfunnel.md](04-outfunnel.md) — misurava 163
blocchi, 7 CTA, 109 media sulla stessa pagina, e concludeva *"Nessun prezzo in pagina. Né in hero né in
chiusura."*

> **Correzione al rapporto precedente, verificata sulla nuova cattura.** Il prezzo **c'è**: `98€ /
> pagamento unico`, dentro la card verde "outFunnel" appena sopra il bottone finale [y≈25.400 su
> `desktop-29.png`; immagine `Artboard+–+99-min.png`, y=25297, w=327, h=243, `alt=""` in
> `scheda.json → media`]. Non è nel testo di `copy-integrale.md` né della v1 né della v2 per lo stesso
> motivo per cui era invisibile al vecchio studio: **è un'immagine, non testo**, con `alt` vuoto. Se il
> vecchio rapporto diceva il vero il 1° settembre, il prezzo è stato aggiunto nei sei giorni fino alla
> ricattura; se il prezzo c'era già, era già invisibile a qualunque estrazione testuale — inclusa quella
> usata per scrivere quel rapporto. In entrambi i casi, il fatto utile per la Fabbrica è lo stesso: **su
> questa pagina, oggi, il prezzo esiste ma nessuno strumento di lettura automatica del testo lo vede.**
> È lo stesso identico difetto già registrato per `outEmail` nel report
> [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) (`Artboard+41_2.png`, `alt=""`) —
> qui si ripete su una seconda pagina dell'ecosistema, prova che è un pattern di produzione, non un
> incidente isolato.

---

## DELTA ALLA FABBRICA

**CANONE:** conferma piena del sistema **"prodotto = pelle cromatica propria"** già registrato nel
rapporto v1: il verde-acqua/teal (`#3bcf04` sulla parola "profitto" [y=14265], `#006e6a` sul prefisso
"out" [y=18565]) resta l'accento esclusivo di questa pagina, e la card prezzo verde-teal
("outFunnel" su sfondo turchese, vista in `desktop-29.png`) lo conferma anche nell'unico punto
cromatico che il rapporto precedente non aveva potuto descrivere (essendo dentro un'immagine). Da
codificare: `product-accent-teal` per outFunnel, coerente con `product-accent-blue` dell'hub e i toni
già mappati per gli altri prodotti "out*".

**PATTERN:** il **bottone-azione principale può non avere alcuna destinazione capturabile e restare
comunque, visivamente, indistinguibile da un bottone funzionante.** `Entra ora in outFunnel` [y=25571]
è un `<div>` (non un `<a>`, non un `<button>`), colore testo `#a8a8a8` su sfondo `#1b1b1d` — lo stesso
difetto di basso contrasto già segnalato nel 2026-09-01 — con `href: None` verificato sia in
`scheda.json → cta[]` sia in `dom-blocks.json`, e **nessun tag `a` con destinazione in tutto l'intorno
y=25400-25750**. Sul piano onesto: una `div` di Squarespace può essere agganciata a un gestore di click
JavaScript invisibile a un'estrazione statica del DOM (è il meccanismo standard di "aggiungi al
carrello" di molte pagine e-commerce Squarespace) — quindi non si può affermare con certezza che il
bottone sia rotto lato utente reale. Quello che si può affermare con certezza, perché è ciò che questa
cattura misura: **in questa istantanea della pagina non esiste, da nessuna parte nel DOM statico, un
percorso testuale dal click al pagamento.** Per la Fabbrica: ogni bottone-acquisto va marcato con `href`
reale anche quando la logica di aggiunta al carrello è gestita da JS, per garanzia sia di accessibilità
sia di verificabilità in futuri audit automatici.

**GATE:** distinguere per sempre, nel prossimo motore di misura, tra **elemento interattivo** (un
accordion, un quiz, una scheda a comparsa) ed **elemento con destinazione** (link o bottone che porta a
un'azione fuori dal punto in cui si trova). Su questa pagina, degli **17 elementi classificati come
`cta`**, solo **8 hanno un `href` reale**: `Passa al contenuto` [#page], `Claude Speedrun` [esterno],
i quattro bottoni di segmentazione per ruolo [`#tp-copywriter`, `#tp-mediabuyer`, `#tp-titolare`,
`#tp-manager`, tutti y≈20.480-20.560 — **verificati come ancore in-pagina reali**, non decorative], `La
mia storia` [/story] e `Recensioni` [/presto-disponibile]. I restanti 9 (`Prossima domanda` del quiz,
le 4 etichette `📝 Sezione N`, il bottone d'acquisto principale, le 3 domande FAQ) hanno tutti
`href: None`: sono toggle o pulsanti di stato, non collegamenti. Il rapporto già distingue questo per il
`manuale-del-copywriter` (vedi report dedicato, dove la proporzione è ancora più marcata); qui va
scritto come regola generale del gate di misura.

---

## LA STRUTTURA — gli 11 movimenti, confrontati con la formula a 11 tappe

| # | y | Alt. (px) | Movimento | Tappa della formula a 11 | Note |
|---|---|---|---|---|---|
| M1 | 0 | 1.400 | **Tre diagrammi di funnel a confronto**, nessun testo di vendita [y=154-1011] | **Hero**, ma sostituisce la promessa con una dimostrazione visiva | Il lettore si autodiagnostica guardando tre livelli di complessità crescente, non leggendo una headline |
| M2 | 1.400 | 2.600 | *"Perché non venderai solo perché il funnel è lungo… O corto"* [y=1423] → *"È troppo grave per troppi business…"* [y=2151] | **Agitazione** | Ripetizione sonora "troppo… troppi… Troppo" su tre righe [y=2146/2179/2374] |
| M3 | 2.600 | 3.215 | *"Perfetto per te."* [y=2485] → salto a *"Già che ci sei, buttaci sopra benzina"* [y=5815] | Cerniera agitazione→metodo | Gap di 3.215px fra le due headline non descritto dal testo estratto (probabilmente fumetti/illustrazioni, coerente con "M3 fumetti" del rapporto v1) |
| M4 | 5.815 | 833 | *"Buttaci sopra benzina"* + *"Che vuol dire funnel strategico?"* [y=6648] | **Metodo** — definizione | *"Strategia significa applicare step di marketing che provengono da un profondo brainstorming"* [y=6703] |
| M5 | 7.195 | 650 | **Italianissimo vs Vincitore** — i due personaggi [y=7195-7622] | Agitazione/metodo in forma di scena, non di lista | *"che sa che funziona… Non che forse funziona"* [y=7593/7622] — firma stilistica dell'ecosistema |
| M6 | 7.845 | 2.578 | *"La speranza non è una strategia"* [y=7845] → *"Sei qui per bruciare tutto al Crazy Time…"* [y=10972] | Fulcro concettuale — non è una tappa della formula, è lo slogan-manifesto del prodotto | Ripetuto identico in chiusura [y=23920] |
| M7 | 14.077 | 2.184 | **5 statistiche con fonte** [y=14533-16172] | **Prova con fonte** — l'unica tappa completa e verificabile della pagina | Vedi sezione dedicata sotto |
| M8 | 18.032 | 2.146 | *"Vuoi complottare Funnel strategici vincenti"* [y=18032] → *"Lo so. È per quello che ho lanciato outFunnel"* [y=18524] | Presentazione prodotto | Prima menzione esplicita del nome prodotto in 18.500px di pagina (68,6% dell'altezza) |
| M9 | 20.401 | 2.400 | **Segmentazione per ruolo** — 4 bottoni-ancora reali [y=20479] + 4 sezioni dedicate [y=20750-22433] | **Benefici**, segmentati per pubblico | Le 4 ancore funzionano davvero (`#tp-copywriter` ecc.), non solo visivamente |
| M10 | 22.509 | 1.729 | Quiz interattivo [y=22617] + *"outFunnel - benefici"* [y=23038] | Benefici + interattività | *"Dove mandiamo i lettori dopo questa ad/sales page/email?"* — il quiz mostra le domande a cui il lettore non sa rispondere |
| M11 | 24.220 | 2.773 | **Curriculum** (4 sezioni accordion, [y=24560-24785]) → **qualificazione finale** [y=24962] → **prezzo (immagine)** [y≈25.297] → **bottone d'acquisto** [y=25571, senza href] → **FAQ** (3 domande, [y=25855-26064]) → footer | **Curriculum + qualificazione negativa + prezzo + FAQ + chiusura**, tutte compresse nell'ultimo 10% della pagina | Cinque tappe della formula in 2.773px su 26.993 (10,3%) |

**Lettura complessiva:** delle 11 tappe canoniche, outFunnel ne copre esplicitamente **6** (hero
sostituito da dimostrazione, agitazione, metodo, prova con fonte, benefici, curriculum+qualificazione+
prezzo+FAQ+chiusura compressi in coda) e ne salta **5** in forma classica: non c'è un blocco
"obiezioni" con struttura domanda-risposta esplicita (le obiezioni sono incassate dentro le 4 sezioni
di segmentazione per ruolo, come "Disclaimer: in outFunnel non ci si concentra sulla parte tecnica"
[y=21473] — pre-obiezione, non botta-e-risposta), non c'è un'autorevolezza biografica dedicata (a
differenza di `funnel-operator`), e non c'è un prezzo barrato — il prezzo (98€) compare una sola volta,
senza un prezzo "originale" accanto da cui sconterebbe.

---

## LA PROMESSA E DOVE STA

La promessa non vive in una headline dichiarativa ma in una domanda a cui il prodotto promette di saper
rispondere:

> "outFunnel serve a questo: aiutarti a rispondere con **100% sicurezza** alla domanda **'che step
> bisogna mettere in questo funnel?'**" [y=20178]

È l'unica formulazione esplicita della promessa in 26.993px, e arriva al 74,8% della pagina — molto
tardi. Prima di quel punto, la pagina costruisce solo il problema (funnel non strategici, dati come
gioco d'azzardo, il 68% delle aziende senza funnel efficace) senza mai dire in una riga sola cosa
insegnerà esattamente il prodotto. La seconda formulazione, più vicina all'apertura ma indiretta:

> "Impara esattamente **quali step fare** per portare una persona da **sconosciuto** a **cliente** con
> marketing." [y=19627]

Entrambe condividono la stessa struttura: la promessa non è un risultato finanziario ("guadagnerai X"),
è una **competenza specifica e verificabile in una conversazione professionale** — sapere rispondere a
una domanda precisa. Coerente con la lettura già data dal rapporto v1: un prodotto che risolve una
domanda di ansia da call vale più di un prodotto che promette una competenza generica.

---

## COME TRATTA LE OBIEZIONI

outFunnel non ha una sezione "obiezioni" con struttura esplicita domanda-risposta (zero pattern "Ma
io…" trovato nei 215 blocchi). Le obiezioni sono gestite in tre modi diversi, tutti impliciti:

1. **Pre-obiezione per delimitazione dell'offerta**, ripetuta 4 volte identica nelle sezioni di
   segmentazione per ruolo:
   > "Disclaimer: in outFunnel non ci si concentra sulla parte tecnica (come settare le ads, che
   > budget mettere, ecc). Ci si concentra solo ed esclusivamente sulla parte strategica" [y=21473]
   > "in outFunnel non ti viene spiegato come scrivere copy, come disegnare il logo o come settare il
   > budget nelle ads" [y=22300]

   Dichiarare cosa il prodotto **non** contiene previene il rimborso per aspettativa disattesa più
   efficacemente di qualunque botta-e-risposta.
2. **Obiezione di credibilità del mercato locale**, risolta con dato+ironia invece che con difesa:
   > "girando su Facebook Ad Library a me non sembra che in Italia usino chissà che strategia (lol)"
   > [y=15009]
3. **Obiezione "non sono nel target"**, risolta con qualificazione negativa finale, non con una
   sezione dedicata a metà pagina:
   > "outFunnel? Probabilmente non è per te. Ma se lo è… Stai per svoltare." [y=24962]

Il confronto con `outEmail`, che ha due obiezioni esplicite in forma botta-e-risposta (documentato nel
report [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md)), conferma che la gestione
delle obiezioni non è uniforme nell'ecosistema: dipende dal tipo di prodotto. outFunnel, il più
concettuale e meno tecnico dei quattro "out*" studiati finora, preferisce la delimitazione preventiva
alla difesa reattiva.

---

## LE PROVE E LA LORO VERIFICABILITÀ (spietato)

**outFunnel è l'unica pagina dell'ecosistema con fonti esterne verificabili su ogni singola
statistica**, confermato di nuovo su questa cattura — cinque link `a href` reali, tutti diversi, tutti
cliccabili:

| Dato | Link `Fonte` | Dominio | Natura della fonte |
|---|---|---|---|
| 89% dei leader crede nel marketing personalizzato [y=14533] | `https://segment.com/state-of-personalization-report/` [y=14804] | Segment (Twilio) | Azienda di marketing automation — interesse diretto a mostrare risultati favorevoli al proprio settore |
| 313% in più di successo con marketing strategico [y=14941] | `https://coschedule.com/marketing-statistics` [y=15110] | CoSchedule | Software di content marketing — stesso conflitto d'interesse |
| 68% aziende senza funnel efficace [y=15247] | `https://www.salesforce.com/marketing/automation/guide/` [y=15502] | Salesforce | Vendor enterprise di marketing automation — massimo conflitto d'interesse fra i cinque |
| 30%/50% più aperture/clic con email segmentate [y=15611] | `https://www.hubspot.com/marketing-statistics` [y=15837] | HubSpot | Vendor di marketing automation — stesso schema |
| 53,7% marketer: strategia è skill sottovalutata [y=15974] | `https://www.marketingweek.com/2024-career-salary-survey/` [y=16172] | Marketing Week | **L'unica fonte editoriale indipendente delle cinque** — non vende un prodotto di marketing automation |
Il fatto misurabile e spietato: **4 delle 5 fonti sono aziende che vendono strumenti di marketing
automation**, cioè hanno un interesse commerciale diretto a pubblicare statistiche che rendano
"la strategia" (il tema del corso) sembrare più importante di quanto lo sia in un dato indipendente.
Solo la quinta (Marketing Week) è editoriale. Sono link reali, cliccabili, verificabili come esistenti —
un livello di trasparenza che nessun'altra pagina dell'ecosistema raggiunge — ma la scelta delle fonti
stessa (tutte con lo stesso conflitto d'interesse, tranne una) non è mai dichiarata al lettore.

Il resto della pagina non ha bisogno di fonti perché non fa affermazioni statistiche: il confronto
Italianissimo/Vincitore è narrativo, non numerico, e il claim "100% sicurezza" [y=20178] è retorico,
non statistico — misurato, non è accompagnato da nessuna fonte né lo richiede per il registro in cui è
scritto.

---

## LA SCALA DI IMPEGNO

| Livello | Elemento su questa pagina | Presente e funzionante? |
|---|---|---|
| 0 — Lettura | Scroll libero, 26.993px | Sì |
| 1 — Auto-segmentazione | 4 bottoni-ruolo, ancore reali [`#tp-copywriter` ecc., y=20479] | **Sì, verificato** — unico micro-impegno realmente funzionante della pagina |
| 2 — Auto-diagnosi | Quiz interattivo [y=22617] | Sì, ma il quiz non raccoglie dati (nessun campo email, nessun risultato salvato) — è persuasione, non lead-gen |
| 3 — Acquisto | Bottone `Entra ora in outFunnel` [y=25571] | **Non verificabile** — `href: None`, nessuna destinazione trovata nel DOM statico |

La scala si interrompe esattamente al passaggio più importante: non c'è un gradino intermedio di
raccolta contatto (nessun form email su tutta la pagina, confermato — zero input/form nei 215 blocchi),
quindi chi arriva al fondo della pagina senza voler comprare immediatamente non lascia alcuna traccia
recuperabile per un funnel di remarketing.

---

## IL PREZZO E LA SUA CORNICE

Il prezzo — **98€, "pagamento unico"** — è visibile una sola volta, dentro la card verde-teal col nome
del prodotto, a y≈25.297 (confermato in `desktop-29.png` e nei metadati immagine di `scheda.json`).
Non è mai testo semplice: è pixel, `alt=""`, esattamente come il prezzo di `outEmail` documentato nel
report [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md). Nessun prezzo barrato,
nessuno sconto dichiarato, nessuna scadenza: il prezzo compare **una sola volta in 26.993px**, all'89,3%
dell'altezza della pagina, subito prima del bottone d'acquisto e subito dopo la qualificazione negativa
finale — la sequenza è "ti dico chi sei tu (qualificazione) → ti dico quanto costa → ti chiedo di
comprare", senza la consueta giustificazione economica anticipata ("ROI fuori da questo pianeta") che
invece outEmail usa prima di mostrare la cifra. Qui il prezzo arriva "a freddo", senza cornice
persuasiva immediatamente prima.

---

## COSA NON DICE MAI

Verificato con ricerca diretta sui 215 blocchi di questa cattura:

1. **Nessuna garanzia o rimborso** — zero occorrenze di "garanzia"/"rimbors*" riferite al prodotto.
2. **Nessuna scadenza o countdown** — zero occorrenze di "scadenz*"/"countdown"/"mezzanotte".
3. **Nessun conflitto d'interesse dichiarato sulle fonti** — le statistiche vengono presentate come
   neutre, mai con la premessa "questa fonte vende marketing automation, quindi ha interesse a…".
4. **Nessuna durata del corso in ore o minuti** nel corpo persuasivo — a differenza di `outEmail`
   ("334 minuti di tutorial"), qui la lunghezza del corso non viene mai quantificata prima delle FAQ
   (una delle 3 domande FAQ è proprio *"Quanto dura il corso?"* [y=25984], il che conferma che
   l'informazione manca altrove, altrimenti la domanda non avrebbe senso).
5. **Nessun prezzo barrato o sconto** — il 98€ è l'unico numero di prezzo, mai presentato come
   "invece di".

---

## LE FORMULE RICORRENTI

**1. Auto-diagnosi per confronto visivo, non per affermazione**
> "Alcuni fanno questo funnel… E altri fanno questo… E poi c'è chi fa questo:" [y=154/550/1011]

`[PLACEHOLDER: LIVELLO 1, IL PIÙ SEMPLICE]… E altri fanno [LIVELLO 2, PIÙ COMPLESSO]… E poi c'è chi fa
[LIVELLO 3, IL PIÙ SOFISTICATO]:` — tre esempi in scala crescente, zero aggettivi di giudizio, il
lettore si colloca da solo.

**2. Martellamento sonoro con ripetizione della stessa radice su tre gradini di intensità**
> "È **troppo** grave per **troppi** business… […] **Troppo** grave per loro… **Perfetto** per te."
> [y=2146/2179/2374/2485]

`È [PLACEHOLDER: AGGETTIVO] grave per [PLACEHOLDER: AGGETTIVO RIPETUTO] troppi [PLACEHOLDER: BERSAGLIO]…
[STESSO AGGETTIVO] per loro… Perfetto per te.`

**3. Certezza contro probabilità, sempre nella stessa coppia lessicale**
> "ha creato un funnel **che sa che funziona**… Non che **forse** funziona." [y=7593/7622]

`ha creato/fatto [PLACEHOLDER: COSA] che sa che funziona… Non che forse funziona.`

**4. Schema statistica in quattro passaggi fissi**
> `[dato con fonte]` → *"'Marketing personalizzato' è il contrario di 'marketing standard'. Capisci?"*
> [traduzione in parole povere, y=14601] → *"Mia opinione: spesso non lo fanno…"* [opinione marcata
> come tale, y=14703] → *"Menomale che ci sei tu ad aiutarli (e farti pagare nel frattempo)."*
> [istruzione operativa, y=14703]

`[DATO]% [PLACEHOLDER: CLAIM DI MERCATO] (Fonte) → [TRADUZIONE IN PAROLE POVERE] → Mia opinione:
[PLACEHOLDER: perché succede] → E quindi tu [PLACEHOLDER: AZIONE CHE MONETIZZA IL DATO].`

**5. Domanda retorica con risposta prevista e squalificata nella stessa riga**
> "Cosa devi modificare per aumentare quel 2.3%? Se hai detto 'devo cambiare il copy della mail', hai
> appena detto quello che dicono tipo… **Tutti**." [y=10699]

`[DOMANDA APPARENTEMENTE APERTA]? Se hai detto "[PLACEHOLDER: RISPOSTA OVVIA]", hai appena detto quello
che dicono tipo… Tutti.`

**6. Delimitazione esplicita del prodotto, ripetuta identica per ogni segmento di pubblico**
> "in outFunnel non ci si concentra sulla parte tecnica…" [y=21473] · "in outFunnel non ti viene
> spiegato come scrivere copy…" [y=22300]

`In [PRODOTTO] non ci si concentra su [PLACEHOLDER: COMPETENZA CHE IL LETTORE GIÀ HA O CHE NON È IL
FOCUS]. Ci si concentra solo ed esclusivamente su [PLACEHOLDER: IL VERO FOCUS DEL PRODOTTO].`

---

## IL DIFETTO

Tre difetti reali, misurati su questa cattura:

1. **Il prezzo esiste ma è invisibile a qualunque lettura testuale.** `98€ / pagamento unico` compare
   solo dentro `Artboard+–+99-min.png` [y=25297, `alt=""`]: zero occorrenze del simbolo "€" o della
   cifra "98" in tutti i 215 blocchi di `copy-integrale.md`. È lo stesso pattern già registrato per
   `outEmail`, qui confermato su una seconda pagina — non è più un caso isolato, è un modo di produrre
   le card-prezzo di tutto l'ecosistema.
2. **Il bottone d'acquisto principale non ha una destinazione recuperabile nel DOM statico.** `Entra
   ora in outFunnel` [y=25571] è un `<div>`, non un `<a>`: `href: None` sia in `scheda.json` sia in
   `dom-blocks.json`, nessun tag `a` con destinazione trovato nell'intorno y=25400-25750. Sommato al
   contrasto già basso (`#a8a8a8` su `#1b1b1d`, difetto già noto dal 2026-09-01), l'unico invito
   all'acquisto di 26.993px di pagina è, in questa istantanea, sia poco visibile sia privo di un
   percorso testuale verso il pagamento.
3. **Le 4 etichette accordion `📝 Sezione N` [y=24560-24785] appaiono visivamente sbiadite/in
   transizione in `desktop-28.png`** — coerente con il limite di cattura già dichiarato dal rapporto v1
   ("diverse fette sono state scattate mentre gli elementi erano ancora in transizione"): non è un
   difetto della pagina live, ma un limite di questa specifica cattura che va segnalato per chi userà lo
   screenshot come riferimento visivo.

---

## Collegamenti

- [04-outfunnel.md](04-outfunnel.md) — il rapporto di design/struttura (macchina v1, 2026-09-01), qui
  corretto sul punto del prezzo
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — dove è documentato per la prima
  volta il pattern "prezzo come immagine con alt vuoto", qui confermato su una seconda pagina
- [01-andrei-copy-home-COPY.md](01-andrei-copy-home-COPY.md) — l'hub da cui, di fatto, non si arriva mai
  a questa pagina (zero link diretti trovati nella home)
- [06-manuale-del-copywriter-COPY.md](06-manuale-del-copywriter-COPY.md) — il confronto sulla
  distinzione CTA-reale/elemento-interattivo, applicata qui in forma più contenuta (9 su 17)
- `capture/04-outfunnel/copy-integrale.md`, `scheda.json`, `dom-blocks.json`, `desktop-28.png`,
  `desktop-29.png` — le fonti grezze usate per ogni citazione di questo file
