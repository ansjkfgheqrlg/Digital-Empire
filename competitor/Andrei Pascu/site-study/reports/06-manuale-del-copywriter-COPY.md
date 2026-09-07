---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #copy-teardown #ebook #lead-magnet #manuale-del-copywriter #machine-v2
Created: 2026-09-07
Last updated: 2026-09-07
---

# 06 — Manuale del copywriter — teardown di copy, macchina v2

**Fonte:** `capture/06-manuale-del-copywriter/` — catturato 2026-09-07 — **11.067px** desktop, **13
sezioni (12 distinte)**, **192 blocchi di testo**, **39 CTA** (`scheda.json → cta[]`).
**Standard di forma:** [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md).
**Rapporto precedente (macchina v1, 2026-09-01):** [06-manuale-del-copywriter.md](06-manuale-del-copywriter.md)
— misurava 139 blocchi, **7 CTA**, 52 media sulla stessa pagina.

> **Il numero che va spiegato subito.** Il rapporto precedente contava **7 CTA** su questa pagina; la
> nuova cattura ne conta **39**. Non è un errore del vecchio rapporto: la sua stessa tabella "I 7
> bottoni" elencava solo elementi con un vero `href` di acquisto o di navigazione (Acquista, Riproduci,
> Ricevi l'anteprima, Compralo e scaricalo, Voglio imparare da te, Passa al contenuto, Acquista finale)
> — sette bottoni reali. La macchina v2 classifica come "CTA" **ogni elemento DOM interattivo con
> sfondo e dimensioni misurabili**, quindi include anche i 18 titoli-accordion dei capitoli e le 8
> domande FAQ, che si aprono/chiudono ma non portano da nessuna parte. Il numero "39" preso alla
> lettera come "39 call-to-action nel senso di marketing" è quindi fuorviante del 460% circa rispetto
> alle CTA vere. La sezione dedicata più sotto rifà il conteggio a mano, elemento per elemento.

---

## DELTA ALLA FABBRICA

**CANONE:** confermato identico il sistema **"CTA a testo variabile, stessa destinazione"** già
registrato dal rapporto v1 — vedi sotto la tabella completa. Da codificare come componente
`cta-emotional-copy`: bottone che cambia testo in base allo stato emotivo della sezione in cui si trova,
mantenendo sempre lo stesso `href` di acquisto.

**PATTERN — il nuovo, il più importante di questo file:** un **accordion di capitoli/FAQ, se misurato
con lo stesso metro di un bottone (bg + dimensioni + interattività), si traveste da "alta densità di
call-to-action" in qualunque report automatico che non separi le due categorie.** Verificato con
`scheda.json → sezioni`: la sezione 10 ("Quali sono i capitoli del Manuale del copywriter?", y=7486, alt.
1.319px) da sola contiene **18 delle 39 CTA totali** (46%), e la sezione 11 (FAQ, y=8806, alt. 868px) ne
contiene altre **8** (20%) — insieme, due sezioni su tredici concentrano il 66% di tutte le "CTA" della
pagina, e **nessuna delle 26 porta a un click reale**. Questo pattern era già presente, in scala minore,
in `outfunnel` (9 elementi su 17 senza `href`, vedi report dedicato) — qui è la maggioranza assoluta.

**GATE:** obbligatorio, per ogni futura misura di "densità di CTA" comparata fra pagine: **separare il
conteggio in due colonne, `cta_navigazionali` (href reale) e `cta_interattive` (toggle/accordion/quiz
senza destinazione)**, e non sommarle mai in un unico numero senza dichiararlo. Applicato qui: 10
navigazionali + 29 interattive = 39 lette insieme, ma il dato utile per un audit di conversione è **10**,
non 39.

---

## LA STRUTTURA — 13 sezioni, confrontate con la formula a 11 tappe

| # | y | Alt. (px) | Sezione | Tappa della formula a 11 | Funzione reale |
|---|---|---|---|---|---|
| 1 | 0 | 627 | Hero: *"Impara la skill più importante: la vendita scritta"* [y=176] + CTA acquisto immediato [y=514] | **Hero**, con CTA d'acquisto già presente (raro nell'ecosistema: qui si può comprare dal primo schermo) | Filtro di categoria (*"- eBook sul Copywriting -"* [y=136]) + compressione tempo→pagine |
| 2 | 627 | 567 | *"Guarda sto video 👇🏻"* [y=703], video 3:33 | Prova/dimostrazione informale | Registro parlato, nessuna trascrizione |
| 3 | 1.194 | 519 | *"✨ Libri di business ✨"* — manifesto anti-categoria [y=1242] | **Agitazione**, ma contro la categoria di prodotto, non contro un problema del lettore | *"1 concetto in 200 pagine"* vs *"Finisci il libro che non sai cosa fare"* [y=1416] |
| 4 | 1.713 | 403 | *"Perché la maggior parte dei libri dicono tanto e nulla?"* [y=1760] | Continuazione agitazione + spiegazione del movente altrui | *"Perché devono."* [y=1879] — non accusa, spiega un incentivo |
| 5 | 2.116 | 925 | *"Il copywriting è un business, non un romanzo"* [y=2163] + 4 pilastri "X, non Y" [y=2420-3041] | **Metodo/benefici** in forma comparativa implicita | Unico numero personale: *"superare i 10 mila euro mensili"* [y=2301] |
| 6 | 3.147 | 359 | Carosello 12 item [y=3459] | Curriculum in anteprima visiva | *"Item 1 of 12"* — nessun titolo di capitolo ancora dichiarato qui |
| 7 | 3.506 | 2.179 | **Blocco anteprima gratuita** [y=3690-5548] | **Sostituisce sia "prova con fonte" sia "garanzia"** — vedi sezione dedicata | *"(casualmente)"* [y=4695] — la parola che rende il campione una statistica |
| 8 | 5.685 | 711 | 2 obiezioni di formato + card prezzo 79€ [y=5761-6257] | **Obiezioni + prezzo**, compressi insieme | *"Ho sempre odiato sfogliare libri"* [y=5761] — l'obiezione parte da un'antipatia dell'autore |
| 9 | 6.397 | 1.090 | Bio autore [y=6444-7347] | **Autorevolezza** | *"Io sono un copywriter adesso"* [y=7241] — la giovinezza professionale come argomento, non debolezza |
| 10 | 7.486 | 1.319 | Indice capitoli, 18 voci gratis [y=7534-8652] | **Curriculum** | 7 Parti (teoria) + 11 Manuali (pratica) — i manuali 1-5 sono APSOC |
| 11 | 8.806 | 868 | **FAQ**, 8 domande [y=8853-9540] | **FAQ** | *"Cosa cambia tra il corso e il libro?"* gestisce la cannibalizzazione qui, non in pagina di vendita |
| 12 | 9.674 | 689 | Card prezzo ripetuta + icone pagamento [y=9769-10210] | **Prezzo/chiusura** | *"✅ Pagamento sicuro SSL"* [y=10210] |
| 13 | 10.362 | 705 | Footer istituzionale blu | Chiusura legale | Identico pattern delle altre pagine dell'ecosistema |

**Lettura complessiva:** delle 11 tappe, il Manuale ne comprime **9 in 11.067px** (un terzo della
lunghezza di `outfunnel`) proprio perché **l'anteprima gratuita (sezione 7) fa il lavoro che altrove
richiede 3-4 sezioni separate** (prova con fonte + garanzia + parte della qualificazione). Manca del
tutto una **qualificazione negativa esplicita** (zero pattern "non è per tutti"/"non prendere questo
se..." nei 192 blocchi) — l'unico accenno di segmentazione è nella FAQ, *"Questo manuale è solo per chi
vuole diventare copywriter professionista?"* [y=9429], posta come domanda del lettore, non come
affermazione dell'autore.

---

## LE 39 CTA: SONO VERE O LINK RIPETUTI? IL CONTEGGIO A MANO

Questa è la domanda a cui questo file deve rispondere per intero. Ho riletto tutti i 39 elementi di
`scheda.json → cta[]`, uno per uno, verificandone `href`, testo e destinazione reale. Risultato:

### Classe A — CTA reali con destinazione (10 su 39, 25,6%)

| y | Testo | Destinazione | Nota |
|---|---|---|---|
| 8113 | "Passa al contenuto" | `#page` | Skip-link, accessibilità |
| 8121 | "Claude Speedrun" | `https://claude-speedrun.com` | Esterno, cross-sell |
| 514 | "Acquista 🔥 Per accesso istantaneo" | `.../store/p/manuale-del-copywriter` | **Acquisto reale** |
| 6037 | "Manuale del copywriter" (nome prodotto nella card) | `/store/p/manuale-del-copywriter` | **Acquisto reale** |
| 6257 | "Compralo e scaricalo" | `.../store/p/manuale-del-copywriter` | **Acquisto reale** |
| 7347 | "Voglio imparare da te" | `.../store/p/manuale-del-copywriter` | **Acquisto reale** |
| 9976 | "Manuale del copywriter" (2ª card, ripetuta) | `/store/p/manuale-del-copywriter` | **Acquisto reale** |
| 10091 | "Acquista" | `.../store/p/manuale-del-copywriter` | **Acquisto reale** |
| 10554 | "La mia storia" | `/story` | Nav |
| 10623 | "Recensioni" | `/presto-disponibile` | Nav, segnaposto |

**Dentro questa classe A, un fatto ancora più preciso:** **6 dei 10 link reali portano tutti alla
stessa identica pagina** (`/store/p/manuale-del-copywriter`, in forma relativa o assoluta), con **sei
testi diversi**: `Acquista 🔥 Per accesso istantaneo` → `Manuale del copywriter` → `Compralo e
scaricalo` → `Voglio imparare da te` → `Manuale del copywriter` (di nuovo) → `Acquista`. Non sono link
ripetuti per pigrizia: il testo cambia con lo stato emotivo della sezione che lo precede esattamente
come già registrato dal rapporto v1 (hero → velocità; dopo l'obiezione di formato → azione fisica; dopo
la bio → relazione; checkout finale → nessun aggettivo). **È una scelta deliberata**, non un difetto:
un solo `href` di destinazione, sei porte d'accesso testuali diverse a seconda di dove si trova il
lettore nel suo percorso di lettura.

### Classe B — elemento funzionale ma non un link (1 su 39, 2,6%)

| y | Testo | Natura |
|---|---|---|
| 5462 | "Ricevi l'anteprima" | Bottone **submit di un form email** — `href: None` è corretto per definizione, un submit non ha una destinazione URL propria |

### Classe C — badge decorativo, non interattivo nella sostanza (2 su 39, 5,1%)

| y | Testo | Natura |
|---|---|---|
| 5961 | "ANTEPRIMA" | Etichetta `#c9c9c9`, sovraimpressa sul mockup del libro — nessun `href`, nessuna funzione di click reale, è un timbro visivo |
| 9900 | "ANTEPRIMA" | Stessa etichetta, ripetuta identica sulla seconda card prezzo |

### Classe D — accordion/toggle senza destinazione (26 su 39, 66,7%)

- **18 titoli di capitolo** [y=7907-8652]: 7 "Parte N" + 11 "Manuale N", tutti `bg: transparent`,
  `href: None`. Verificato visivamente in `desktop-10.png`: ogni riga ha un'icona **"+"** a destra,
  il segno universale di un accordion che si apre in pagina, non di un link che porta altrove.
- **8 domande FAQ** [y=8918-9515]: stessa natura, stessa icona "+", stesso `href: None`.

### Il verdetto

**No, non sono 39 CTA nel senso in cui un marketer userebbe la parola.** Sono **10 collegamenti reali**
(di cui solo 6 sono veri e propri inviti all'acquisto, con testo che cambia ma destinazione unica), **1
bottone funzionale non-link** (il submit del form), **2 etichette decorative**, e **26 leve di accordion**
che aprono testo nella stessa pagina senza portare da nessuna parte. Il numero "39" descrive
correttamente **quanti elementi cliccabili/interattivi** esistono sulla pagina — è un dato reale sulla
densità di interazione — ma descrive malissimo **quante volte la pagina chiede al lettore di comprare o
di uscire dalla pagina**: quella domanda ha come risposta 6, non 39.

**È una scelta o un difetto?** Entrambe le cose, su piani diversi:
- **È una scelta buona** quanto ai 6 CTA d'acquisto veri: variare il testo mantenendo la destinazione è
  una tecnica difendibile e già vista altrove nell'ecosistema.
- **È un difetto di misura**, non della pagina: se questo studio avesse riportato "39 CTA" senza la
  scomposizione qui sopra, avrebbe fatto sembrare il Manuale la pagina con la densità di persuasione più
  alta dell'ecosistema (come lo stesso brief di partenza di questo file presumeva), quando in realtà,
  contando solo Classe A, ha **meno CTA reali di `outfunnel`** (10 contro 8 — anzi ne ha di più in
  valore assoluto, ma su una pagina lunga un terzo, quindi la densità di CTA-reali-per-px è comunque più
  alta: 10/11.067 = 1 ogni 1.107px, contro 8/26.993 = 1 ogni 3.374px di `outfunnel` — su questo, il
  Manuale resta davvero la pagina con CTA reali più fitte, solo non per il motivo o nella misura che il
  numero "39" suggerisce da solo).

---

## LA PROMESSA E DOVE STA

> **"Impara la skill più importante: la vendita scritta (in 115 pagine pratiche)"** [y=176/338]

La promessa condensa **competenza** (la skill più importante) e **compressione di tempo** (115 pagine,
non anni) nella stessa headline. Rinforzata subito sotto dalla metafora della cintura nera:

> "Questo libro è l'equivalente della cintura nera in Copywriting, solo che al posto di metterci anni
> ci metti 115 pagine." [y=380]

Il numero "115" ricorre tre volte in poche righe (pagine, "in 115 pagine pratiche", e implicitamente
nella metafora) — su un ebook è l'unica unità di misura verificabile che il compratore possiede prima
di comprare, ed è usata come sostituto delle "ore di contenuto" che i corsi video dell'ecosistema usano
al suo posto (`outEmail`: "334 minuti di tutorial").

---

## COME TRATTA LE OBIEZIONI

Due obiezioni esplicite, entrambe di **formato**, non di prezzo o di efficacia:

1. *"Ho sempre odiato sfogliare libri"* [y=5761] → risolta con: *"strutturato in maniera pratica e
   schematica. Troverai la strategia o la formula che farà la differenza in pochissimi secondi."*
   [y=5880]
2. *"Sarà sempre con te"* [y=6101] → risolta con: *"È il 2025, e questo libro puoi averlo sul tuo
   telefono o sul PC. Prego."* [y=6176]

Entrambe condividono la stessa struttura retorica: partono da un'antipatia personale dell'autore ("ho
sempre odiato", non "so che a te non piace"), che è più credibile di un vantaggio dichiarato del
prodotto. La terza obiezione, quella di prezzo/valore comparato al corso video da 999€, è gestita
**dentro la FAQ**, non nel corpo persuasivo: *"Cosa cambia tra il corso e il libro?"* [y=9186] — la
cannibalizzazione interna viene disinnescata nel punto della pagina che costa meno attenzione, non
davanti al prezzo.

---

## LE PROVE E LA LORO VERIFICABILITÀ (spietato)

**Zero testimonianze, zero recensioni, zero screenshot di risultati di terzi** — confermato di nuovo su
questa cattura, ricerca diretta sui 192 blocchi: zero occorrenze di "recensione", "testimonianza",
pattern di nome+cognome+citazione. L'unica prova offerta è **il prodotto stesso**, in anteprima:

> "Ho pescato **(casualmente)** alcune pagine del libro… E le puoi leggere adesso." [y=4695]

Analisi spietata della parola `(casualmente)`: è un'affermazione **non verificabile dall'esterno**. Non
c'è modo, per un lettore o per questo studio, di controllare che le pagine mostrate nel form opt-in
siano state davvero estratte a caso e non selezionate come le migliori del libro. È una tecnica di
persuasione efficace (rende il campione una "statistica" implicita sul prodotto intero, come già
osservato dal rapporto v1) ma **la sua efficacia dipende interamente dalla fiducia nella parola stessa,
non da una prova di casualità reale** — nessun timestamp, nessun meccanismo dichiarato ("le pagine sono
generate da un numero casuale tra 1 e 115"), solo l'affermazione.

L'unico numero verificabile in modo indipendente è il link social:

> "Ho un seguito di più di **270 mila persone tra i vari canali social**" [y=6934] → link a
> `https://www.tiktok.com/@andrei.bsns` [y=6938]

Cliccabile, reale, verificato in `dom-blocks.json`. Ma il numero "270 mila" **aggrega canali diversi**
(TikTok, presumibilmente anche Instagram/YouTube) dietro un solo link a un solo profilo TikTok — il
lettore che clicca vede solo una parte del numero dichiarato, non il totale.

---

## LA SCALA DI IMPEGNO

| Livello | Elemento | Presente? |
|---|---|---|
| 0 — Lettura | Scroll, 11.067px | Sì |
| 1 — Guarda il video | Video 3:33 [y=703] | Sì |
| 2 — Lascia un contatto (opt-in) | Form email per l'anteprima [y=5392-5545] | **Sì, funzionante**: 1 campo, bottone 201×64, 3 rassicurazioni in una riga |
| 3 — Riceve valore gratuito | Pagine vere del libro via email | Promesso, non verificabile da questa cattura (richiede l'invio reale) |
| 4 — Acquisto | 6 CTA a testo variabile, stessa destinazione | Sì, **la scala più completa fra le tre pagine di questo studio** |

A differenza sia della home (ferma al livello 1, con falle) sia di `outfunnel` (salta il livello 2, zero
form), il Manuale è l'unica delle tre pagine studiate oggi con **una scala di impegno completa e
funzionante dal livello 0 al livello 4**, opt-in incluso.

---

## IL PREZZO E LA SUA CORNICE

**79,00 €**, sempre testo semplice (mai immagine, a differenza di `outEmail` e di `outfunnel`) [y=6116
e y=10055] — confermato leggendolo direttamente in `copy-integrale.md`, senza bisogno di aprire uno
screenshot. Compare due volte, quasi simmetricamente (52% e 91% dell'altezza pagina), sempre dentro la
stessa card prodotto (mockup+nome+prezzo+bottone), mai nell'headline, mai vicino a un titolo. È il
prezzo più discreto tipograficamente di tutto l'ecosistema misurato finora (17,6px, peso 300) e insieme
l'unico completamente leggibile da un lettore automatico — un contrasto netto con `outfunnel` (98€,
solo immagine) e `outEmail` (139€, solo immagine, documentati nei report collegati).

---

## COSA NON DICE MAI

1. **Nessuna garanzia o rimborso** — zero occorrenze, coerente con l'intero ecosistema.
2. **Nessuna testimonianza o recensione di terzi.**
3. **Nessun conteggio verificabile di copie vendute.**
4. **Il meccanismo di casualità dell'anteprima** — dichiara "(casualmente)" ma non spiega come, né lo
   rende verificabile.
5. **Il numero esatto di follower per singolo canale** — solo l'aggregato "270 mila", con un solo link
   (TikTok) a sostegno.

---

## LE FORMULE RICORRENTI

**1. Metafora di uno standard esterno riconosciuto, scambiata con un numero verificabile**
> "Questo libro è l'equivalente della cintura nera in Copywriting, solo che al posto di metterci anni
> ci metti 115 pagine." [y=380]

`Questo [PRODOTTO] è l'equivalente della [PLACEHOLDER: STANDARD ESTERNO RICONOSCIUTO] in [CAMPO], solo
che al posto di metterci [PLACEHOLDER: TEMPO LUNGO] ci metti [PLACEHOLDER: NUMERO VERIFICABILE].`

**2. Attacco alla categoria di prodotto, con spiegazione del movente altrui**
> "Perché devono. […] tanti autori si mettono a fare libri su argomenti semplici rendendoli complessi,
> noiosi e ripetitivi per avere qualche pagina in più da farti leggere." [y=1879]

`Perché [PLACEHOLDER: CATEGORIA] deve fare così. [SPIEGAZIONE DELL'INCENTIVO DI MERCATO CHE LI COSTRINGE],
non perché [PLACEHOLDER: ACCUSA MORALE EVITATA].`

**3. Struttura contrappositiva "X, non Y" ripetuta su ogni pilastro**
> "Pratico — non noioso, pieni di esempi" · "Facile da utilizzare — non da leggere e dimenticare" ·
> "Aggiornato al 2025 — non scopiazzato da altri libri vecchi" [y=2587-2920]

`[QUALITÀ POSITIVA] — non [PLACEHOLDER: DIFETTO CHE IL LETTORE HA GIÀ SPERIMENTATO ALTROVE].`

**4. Dichiarare la casualità del campione per renderlo statistica**
> "Ho pescato **(casualmente)** alcune pagine del libro… E le puoi leggere adesso." [y=4695]

`Ho preso (casualmente) [PLACEHOLDER: CAMPIONE DEL PRODOTTO]… E lo puoi [PLACEHOLDER: VERIFICARE TU
STESSO] adesso.`

**5. L'obiezione di formato che parte da un'antipatia dell'autore, non da un vantaggio del prodotto**
> "Ho sempre odiato sfogliare libri in maniera maniacale alla ricerca di un piccolo concetto." [y=5880]

`Ho sempre odiato [PLACEHOLDER: IL DIFETTO DEL FORMATO CONCORRENTE]. Con [PRODOTTO] non succederà mai.`

**6. Il testo del bottone cambia col registro della sezione, la destinazione resta identica**
> `Acquista 🔥 Per accesso istantaneo` → `Compralo e scaricalo` → `Voglio imparare da te` → `Acquista`

`[PLACEHOLDER: VERBO+TONO COERENTE CON LO STATO EMOTIVO DELLA SEZIONE CHE PRECEDE], stesso `href` in
ogni occorrenza.`

---

## IL DIFETTO

Due difetti reali, misurati su questa cattura:

1. **Il conteggio "39 CTA" è comparabile con nessun altro numero dell'ecosistema senza la
   scomposizione fatta in questo file.** 26 dei 39 elementi (66,7%) sono accordion di capitoli e FAQ
   senza `href`, verificati visivamente in `desktop-10.png` (icona "+" su ogni riga): confondere questo
   numero con "39 inviti all'azione" sovrastima la persuasività reale della pagina di oltre quattro
   volte rispetto alle 6 vere CTA d'acquisto (Classe A, sottoinsieme "verso lo store").
2. **L'aggregazione "270 mila persone tra i vari canali social" [y=6934] è supportata da un solo link
   verificabile** (TikTok, [y=6938]), non da un totale scomponibile canale per canale. Chi vuole
   verificare il numero può controllare al massimo una frazione non dichiarata di esso.

---

## Collegamenti

- [06-manuale-del-copywriter.md](06-manuale-del-copywriter.md) — il rapporto di design/struttura
  (macchina v1, 2026-09-01), la cui tabella "7 bottoni" è la base del confronto sul conteggio CTA in
  questo file
- [04-outfunnel-COPY.md](04-outfunnel-COPY.md) — dove lo stesso problema di misura (CTA vs elemento
  interattivo) appare in scala minore (9 su 17)
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — dove è documentato per la prima
  volta il pattern "prezzo come immagine con alt vuoto" — qui, per contrasto, il prezzo è testo pulito
- [01-andrei-copy-home-COPY.md](01-andrei-copy-home-COPY.md) — l'hub da cui, come per `outfunnel`, non
  esiste alcun link diretto verso questa pagina
- `capture/06-manuale-del-copywriter/copy-integrale.md`, `scheda.json`, `dom-blocks.json`,
  `desktop-08.png`, `desktop-10.png` — le fonti grezze usate per ogni citazione di questo file
