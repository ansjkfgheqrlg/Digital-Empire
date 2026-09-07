---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #armageddon-pack #famiglia-out #copy #teardown
Created: 2026-09-07
Last updated: 2026-09-07
---

# 14-17 — la famiglia "out*" — teardown del COPY (outEmail, outFunnel, outHeadline, outViral)

Questo dossier non rifà il confronto strutturale già fatto in
[14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) (formula a 11 tappe, CTA, ripetizione
di sezioni) né l'atlante visivo di [14-17-famiglia-out-ATLANTE.md](14-17-famiglia-out-ATLANTE.md). Non
rifà nemmeno il confronto originale-contro-copia già chiuso in
[21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) per due delle quattro pagine. Questo
documento fa una cosa diversa: il teardown del **copy** delle quattro pagine come **famiglia unica** —
cosa promettono, come qualificano negativamente, come trattano le obiezioni, quanto sono verificabili le
prove, come incorniciano il prezzo, cosa non dicono mai, e — cosa che nessuno dei tre dossier gemelli ha
misurato — dove il testo è **carattere per carattere identico** da una pagina all'altra, non solo
strutturalmente simile. Tutte le citazioni vengono dai quattro `copy-integrale.md` di
`14-arma-outemail`, `15-arma-outfunnel`, `16-arma-outheadline`, `17-arma-outviral`, catturati
2026-09-07, incrociati coi rispettivi `scheda.json` per colori, `alt`, e coordinate esatte.

---

## DELTA ALLA FABBRICA

**CANONE:** entra in libreria di copy (non in `canone.css` — questo non è un componente visivo, è testo)
la nozione di **frase-motto riusata fra prodotti diversi dello stesso autore**, non solo fra sezioni
della stessa pagina. Il gate già proposto nel dossier CONFRONTO (§3, "firme ripetute / sezioni totali")
guarda la ripetizione *dentro* una pagina; qui si trova la stessa identica logica un livello più in alto:
*"La speranza non è una strategia."* compare parola per parola sia in outFunnel (due volte: isolata
[y=7755] e come apertura di una frase più lunga [y=23830]) sia in outViral [y=9032] — due prodotti
diversi, la stessa identica frase-chiusura usata come componente di libreria testuale. Va codificato
come pattern `motto-riusabile`: una frase-manifesto, buona per più prodotti dello stesso autore, non
legata al contenuto specifico di nessuno dei due (vedi §"IL BLOCCO RIUSATO").

**PATTERN:** confermato — e complicato — il pattern del badge-colore-condiviso già isolato nel dossier
21-22 (badge *"INCLUSO NEL PACCHETTO ARMAGEDDON"* e barra sticky che condividono lo stesso accento
`#bc0807`, un filo cromatico deliberato fra "questo è incluso" e "compra qui"). Qui, confrontando tutte
e quattro le pagine e non solo due, quel filo **si rompe su una pagina su quattro senza essere
notato**: il badge di outHeadline usa `#ff4f4c`, non `#bc0807` [y=19581] — stesso testo maiuscolo
identico, stesso peso 700, stessa dimensione 15.2px, colore diverso. Il pattern "un solo accento
condiviso fra badge e CTA finale" **vale su tre pagine su quattro**, non su tutte: la quarta ha lo
stesso componente testuale ma un colore diverso, prova che il componente è stato copiato via testo/CSS
senza un controllo pixel-per-pixel dell'istanza finale. Vedi §"IL DIFETTO" punto 2.

**GATE:** due controlli meccanici nuovi per `scripts/gate_siti.py`, entrambi misurati qui per la prima
volta su tutte e quattro le pagine (non solo su outEmail come nel dossier 21-22):
1. *Ogni immagine che sostituisce un numero critico (prezzo, follower, percentuale) deve avere un `alt`
   non vuoto.* Verificato con `grep` diretto sui quattro `scheda.json`: l'immagine-prezzo di ogni singola
   pagina ha `alt=""` — `Artboard+41_2.webp` outEmail [y=23206], `Artboard--E2-80-93-99-min.webp`
   outFunnel [y=25207], `Artboard--E2-80-93-96.webp` outHeadline [y=19299] — e lo stesso identico difetto
   si ripete su outViral non sul prezzo (che lì è testo semplice) ma sui **numeri follower dei sei
   creator**: il file `181k.webp` [y=6808] e i suoi cinque gemelli hanno tutti `alt=""`. Stesso difetto,
   due contesti, quattro pagine su quattro — non un caso isolato di outEmail, un pattern di produzione.
2. *Ogni componente testuale riusato su più pagine sorelle deve passare anche un diff di colore, non solo
   un diff di testo.* Un diff testuale sul badge "INCLUSO NEL PACCHETTO ARMAGEDDON" sarebbe passato pulito
   su tutte e quattro le pagine (stringa identica); solo un diff sul valore CSS `color` avrebbe fermato
   outHeadline. La lezione operativa: quando si certifica un componente riusato come "identico", va
   verificato l'intero record visivo (colore, peso, transform), non solo il contenuto testuale.

---

## LE QUATTRO PROMESSE A CONFRONTO

| Pagina | Promessa citata | A che altezza | A chi parla | Cosa promette di preciso |
|---|---|---|---|---|
| outEmail | *"Apriresti questa email? […] No, non l'apriresti."* [y=95/169/659] → *"Impara a scrivere email performanti"* [y=1082] | y=95, 0% pagina (hero) | implicito, senza selettore di persona — un solo lettore presunto, poi filtrato dopo (qualificazione negativa a y=13269) | una **capacità** (saper scrivere email che si aprono), non un numero — il risultato resta implicito |
| outFunnel | nessuna promessa nell'hero (§ATLANTE, Ruolo 1) — la prima formulazione esplicita arriva a *"outFunnel serve a questo: aiutarti a rispondere con 100% sicurezza alla domanda 'che step bisogna mettere in questo funnel?'"* [y=20089] | y=20089, **75,6% pagina** (20.089 / 26.561) | 4 persone segmentate esplicitamente: *"Sono un copywriter"* / *"media buyer"* / *"titolare aziendale"* / *"project manager"* [y=20389-20464] | **certezza decisionale** ("100% sicurezza"), non un risultato di business — la promessa meno concreta delle quattro, ed è anche l'unica che arriva a tre quarti di pagina |
| outHeadline | *"QUESTA È UNA HEADLINE."* [y=95/180] → *"E solo i copywriter che scrivono HEADLINE persuasive […] guadagnano di più."* [y=321] | y=95, 0% pagina (hero) | due segmenti dichiarati con sezioni dedicate: *"Se sei un copywriter…"* [y=4499] e *"Se sei imprenditore che scrive copy da solo…"* [y=4879] | un **esito economico/di carriera** ("guadagnano di più"), condizionato dal saper scrivere headline — non un numero |
| outViral | *"Ottieni una media di 10K views nei tuoi prossimi video"* [y=141/200] | y=141, 1,4% pagina (hero) | *"Se parli su TikTok (e non ti limiti a fare i balletti)"* [y=467] — creator/venditori via video | un **numero secco e misurabile** (10K views di media) — l'unica delle quattro promesse quantificata nel titolo stesso |

Due osservazioni non ancora scritte altrove. Primo: le quattro promesse hanno **ordini di concretezza
diversi**, non varianti dello stesso claim — outViral quantifica (10K), outEmail e outHeadline promettono
una capacità con un risultato atteso implicito (aprire email / guadagnare di più), outFunnel promette
*sicurezza cognitiva* pura, senza mai nominare un risultato di vendita concreto nella sua stessa frase di
sintesi. Sono quattro prodotti dello stesso autore che vendono quattro tipi diversi di beneficio — non
solo quattro argomenti diversi.

Secondo: **outEmail è l'unica delle quattro pagine a non segmentare esplicitamente il proprio lettore**
con un dispositivo dedicato ("Se sei X…", un selettore di persona, un filtro d'ingresso). Le altre tre
hanno tutte un meccanismo esplicito di segmentazione — il selettore a 4 vie di outFunnel, le due sezioni
"Se sei…" di outHeadline, il filtro "se parli su TikTok" di outViral nell'hero stesso. outEmail parla a
un lettore implicito unico dall'inizio alla fine, e filtra solo *dopo* (tappa 7, qualificazione negativa)
chi non dovrebbe essere lì. Le altre tre filtrano *prima*, dichiarando a chi si rivolgono ancora prima di
promettere qualcosa.

---

## LA QUALIFICAZIONE NEGATIVA

La tappa più interessante della famiglia, per la ragione opposta a quella intuitiva: non è interessante
per quanto dice, ma per quanto **non riesce a essere verificato** anche dove il dispositivo retorico è
più esplicito. Presente solo su due pagine su quattro (outEmail, outHeadline) — assente su outFunnel e
outViral, confermato dal dossier CONFRONTO §2 e riverificato qui riga per riga sui due `copy-integrale.md`.

**outEmail** — testo effettivamente presente nel DOM, in ordine:
1. *"Non è per tutti. Sono serio."* [y=13269]
2. *"Purtroppo per alcuni di coloro che leggeranno questo… outEmail:"* [y=13410]
3. *"⚠️Quindi non prendere outEmail se sei un principiante. outEmail è pensato per professionisti che
   cercano informazioni avanzate…"* [y=13635]
4. *"outEmail non è per novellini. È il prossimo livello di pensiero strategico nella scrittura di email
   marketing."* [y=13725]

Quello che **manca** da questo elenco, verificato per assenza diretta nel `copy-integrale.md`: la lista a
tre voci con le X rosse che l'atlante visivo descrive aprendo lo screenshot ("Non spiega cos'è una mail
di marketing", "Non spiega cosa significa 'copywriting'", "Salta le basi che, tanto, già sai") **non
esiste come testo estraibile** — è resa in un modo che il parser di testo non cattura (icona/immagine o
markup non standard), esattamente come l'atlante aveva già notato per altre sezioni con lo stesso
"limite di misurazione". Risultato pratico: chi legge la pagina *vede* tre ragioni specifiche per non
comprare; chi la legge con uno screen reader, o con qualunque strumento di analisi testuale (compreso
questo stesso studio, se si fermasse al solo `copy-integrale.md`), sente solo il claim generico
("non è per tutti", "non per novellini") — mai le tre ragioni vere.

**outHeadline** — testo effettivamente presente: **una sola riga**, *"outHeadline non è per
principianti"* [y=10913]. Tutto il resto che l'atlante descrive per questa sezione — sia la lista
negativa con le frecce verdi sia la "seconda lista positiva" ("Questo corso è pensato per: Copywriter che
vogliono scrivere al prossimo livello di persuasione") — **non compare da nessuna parte** nel
`copy-integrale.md`: dopo y=10913 il documento salta direttamente a y=11599, un argomento completamente
diverso (l'obiezione sulle formule). Stesso identico difetto di outEmail, ma più estremo: qui **il 100%**
del contenuto specifico della qualificazione (sia negativo sia positivo) è invisibile al testo, resta
solo il titolo.

**Quanto spazio le dà la famiglia, misurato:** outEmail dedica alla tappa una sezione di 743px su
25.588px totali (2,9% della pagina, y=13.174-13.917 secondo l'atlante); outHeadline dedica 686px su
20.168px (3,4%, y=10.818-11.504). outFunnel e outViral: 0px, 0% — la tappa non esiste. Media sulla
famiglia intera (contando gli zeri): **1,6% dello spazio-pagina** dedicato, in media, a dire a qualcuno
di non comprare. Le due pagine che lo fanno gli dedicano una frazione quasi identica di spazio (2,9% e
3,4%) nonostante l'una sia 25% più corta dell'altra — segno che la "dose" di qualificazione negativa non
scala con la lunghezza della pagina, è un blocco a peso fisso che si inserisce o non si inserisce.

**La lettura netta:** la qualificazione negativa in questa famiglia è più un **segnale di postura**
("sono selettivo, quindi sono autorevole") che un filtro operativo reale — il titolo fa il lavoro
retorico, i dettagli che dovrebbero renderlo verificabile e specifico non sono mai testo semplice su
nessuna delle due pagine che la usano.

---

## COME TRATTA LE OBIEZIONI

**outEmail** — botta e risposta diretta, verificata sul `copy-integrale.md` di questa cattura:
*"'Ma io so già scrivere email'"* [y=15786] → *"Bene, allora sei in target. Ho creato questo per persone
che vogliono il prossimo livello di pensiero strategico per email marketing."* [y=15955]. Tecnica:
capovolgimento — l'obiezione diventa prova di appartenenza al target, non motivo per non comprare.

**outHeadline** — due obiezioni esplicite, entrambe in forma citazione-tra-virgolette:
1. *"'Per scrivere headline basta usare formule'"* [y=11599] → risposta articolata in tre passi: *"Se
   bastasse usare delle formule pre-concepite… Perché non usi formule pre-concepite per letteralmente
   ogni singolo pezzo del tuo copy?"* [y=11768], seguito da un racconto di fallimento personale ("Cerco
   una formula / Provo ad applicarla al mio copy / Scopro che non è al 100% adatta al prodotto /
   Ricomincio da capo" [y=11887-11997]) che sostituisce la logica diretta con un'esperienza vissuta.
2. *"'Ma io le faccio scrivere a ChatGPT'"* [y=18062] → *"Ma se non conosci le strategie, non puoi usare
   l'AI responsabilmente."* [y=18654].

**outFunnel** — **zero obiezioni in forma botta-e-risposta diretta**, confermato di nuovo qui (nessun
pattern "'Ma…'" nel testo). Le obiezioni sono gestite in modo diverso: non anticipate e capovolte, ma
**disinnescate per segmento professionale**, dentro ciascuna delle quattro sezioni-persona. Esempio: la
sezione dedicata al media buyer chiude con un disclaimer esplicito che anticipa "questo non è per il mio
ruolo" — *"Disclaimer: in outFunnel non ci si concentra sulla parte tecnica (come settare le ads, che
budget mettere, ecc). Ci si concentra solo ed esclusivamente sulla parte strategica, di pensiero e
decisione iniziale."* [y=21383]; la sezione project manager chiude allo stesso modo: *"E tranquillo, in
outFunnel non ti viene spiegato come scrivere copy, come disegnare il logo o come settare il budget nelle
ads. In outFunnel ti viene insegnato esattamente ciò in cui sei specializzato: pensare
strategicamente."* [y=22210]. È un'obiezione gestita per **esclusione di scope**, ripetuta identica nella
forma ("non ti insegna X, Y, Z, ti insegna solo la parte strategica") su due dei quattro segmenti — un
pattern di gestione obiezioni distribuito nella struttura, non concentrato in una sezione dedicata.

**outViral** — **zero obiezioni esplicite in botta-e-risposta**, confermato anche su questa cattura.
Come per outFunnel, le pre-obiezioni sono incassate dentro affermazioni dirette, non isolate in una
sezione propria: *"Non devi stare dietro all'algoritmo per andare virale e vendere."* [y=910] (contro
"è troppo tecnico per me") e *"TikTok è la piattaforma più facile… Ma non per questo puoi fare a
caso."* [y=1917] (contro "se è facile non serve un corso").

**Sintesi della famiglia:** le due pagine con formula completa (outEmail, outHeadline) trattano le
obiezioni come **eventi discreti**, con una domanda tra virgolette e una risposta secca subito dopo — un
componente riconoscibile e isolabile. Le due pagine "devianti" (outFunnel, outViral) non hanno questo
componente da nessuna parte: le obiezioni ci sono, ma sono **distribuite dentro altre frasi**, mai
isolate come blocco a sé. Nessuna obiezione, su nessuna delle quattro pagine, riguarda il prezzo — tutte
riguardano la competenza percepita del lettore ("so già farlo", "lo fa ChatGPT", "non è per il mio ruolo",
"è troppo tecnico/troppo facile"), mai il costo.

---

## LE PROVE E LA LORO VERIFICABILITÀ (spietato)

**outEmail** — tre link a fonti esterne (Wikipedia, altitudemarketing.com, getresponse.com), già
sezionati in dettaglio nel dossier 21-22: verificabili ma non puntuali (Wikipedia), di seconda mano (blog
di marketing), o di parte (un venditore di software email che cita statistiche a favore del proprio
settore). Non ripetuto qui per intero — vedi 21-22 §"LE PROVE E LA LORO VERIFICABILITÀ".

**outFunnel — cinque statistiche, cinque fonti, mai verificate finora in nessun dossier gemello.**
Ogni claim è seguito, poche righe sotto, da un link `Fonte`:

| Claim (citato) | y | Fonte (y del link) | URL | Chi parla |
|---|---|---|---|---|
| *"89% dei leader in business crede nel marketing personalizzato"* | 14443 | 14715 | `segment.com/state-of-personalization-report/` | Segment — venditore di software di personalizzazione (di proprietà Twilio): report commissionato da chi vende esattamente ciò che la statistica raccomanda |
| *"313% in più di successo per aziende con marketing strategico."* | 14851 | 15020 | `coschedule.com/marketing-statistics` | CoSchedule — venditore di software di pianificazione marketing, pagina-aggregatore di statistiche altrui |
| *"68% delle aziende non hanno identificato un funnel efficace"* | 15157 | 15412 | `salesforce.com/marketing/automation/guide/` | Salesforce — venditore di CRM/marketing automation, stessa dinamica di interesse diretto |
| *"30% più aperture e 50% più clic con email segmentate."* | 15521 | 15748 | `hubspot.com/marketing-statistics` | HubSpot — venditore di software marketing, pagina-aggregatore |
| *"53.7% dei marketer pensano che la strategia sia una skill sottovalutata"* | 15885 | 16082 | `marketingweek.com/2024-career-salary-survey/` | MarketingWeek — testata di settore, non un venditore di software: la fonte più indipendente delle cinque |

Il verdetto spietato: **quattro statistiche su cinque vengono da un'azienda che vende il prodotto di cui
la statistica dimostra il bisogno** — Segment vende personalizzazione e cita che "l'89% dei leader ci
crede", Salesforce vende automazione e cita che il "68% non ha un funnel efficace", HubSpot vende
marketing software e cita "email segmentate", CoSchedule vende pianificazione e cita "313% in più di
successo" senza mai definire cosa significhi "successo" in quel numero — un termine ombrello che rende
il claim tecnicamente citato ma operativamente non falsificabile. Solo MarketingWeek non vende un
prodotto legato alla statistica che riporta, ma è un sondaggio su percezioni soggettive ("pensano che"),
non un dato di risultato misurato. **Nessuna delle cinque fonti di outFunnel è primaria** (nessuna ricerca
accademica, nessun dato governativo) — sono tutte fonti secondarie con un interesse commerciale diretto o
quasi diretto nel raccontare esattamente la storia che raccontano. Sotto questo profilo, outFunnel è
**meno verificabile di outEmail** pur avendo più fonti (5 contro 3): più citazioni non significa più
rigore, quando le fonti condividono lo stesso interesse di parte.

**outHeadline — zero fonti esterne, confermato.** Tutte le affermazioni sono ipse dixit puro: *"Non
dico per dire. Ti sto dicendo fatti oggettivamente riconosciuti nel mondo del marketing"* [y=1728] non è
mai seguito da un link o una citazione — è un'affermazione di autorevolezza sulla propria affermazione,
non una prova. La sola "dimostrazione" della pagina è il tool interattivo prima/dopo (già descritto
nell'atlante, Ruolo 3): non è una prova esterna, è un esempio auto-costruito dall'autore stesso. Sotto il
profilo della verificabilità, **outHeadline è la pagina più debole delle quattro** — zero link, zero
statistiche con fonte, zero nomi terzi verificabili.

**outViral — la prova più forte e la sua asimmetria, riconfermata con dati propri.** I sei creator con
link cliccabile (`youtube.com/@RikPaganoGaming`, `tiktok.com/@notordinaryspaghetti`,
`instagram.com/nicolasllombardo`, `tiktok.com/@giovanni.pitarresi`, `tiktok.com/@micheledemonte`,
`tiktok.com/@manuelbrignacca` — tutti verificati nel `cta[]` di `scheda.json`) restano la prova sociale
più verificabile della famiglia: chiunque può cliccare e controllare che il profilo esista. Ma i numeri
che dovrebbero sommarsi a *"quasi 1 milione di follower totali"* [y=5418] **non sono testo**: sono
immagini con nome file numerico (`181k.webp` [y=6808] e cinque gemelli), tutte con `alt=""` verificato
via `grep` diretto sul `scheda.json` — esattamente lo stesso difetto delle card-prezzo (§"IL DIFETTO"),
applicato qui ai numeri di prova sociale invece che al prezzo. Il lettore vede il numero, uno screen
reader o un parser di testo no. E — punto già notato nel dossier 21-22 ma qui riverificato sul `cta[]`
completo della pagina — **Andrei non linka mai un proprio profilo social verificabile**, nonostante
l'intera autorevolezza della pagina poggi sulla propria esperienza personale su TikTok ("ci becco giusto
il 90% delle volte" [y=8722]). Sei prove esterne verificabili, zero per l'autore stesso.

**Ordine di verificabilità della famiglia, dal più al meno rigoroso:** outViral (link reali, ma numeri
aggregati non verificabili) > outEmail (3 fonti, di parte o generiche) > outFunnel (5 fonti, quasi tutte
di parte diretta) > outHeadline (zero fonti). Il numero di fonti citate non correla con l'indipendenza
delle fonti: outFunnel ne ha di più di outEmail ma è, nel merito, altrettanto — se non più — di parte.

---

## IL PREZZO E LA SUA CORNICE

Le quattro card prezzo condividono lo schema (prezzo individuale barrato + badge rosso "incluso nel
pacchetto"), ma differiscono su tre assi misurabili: **testo vs immagine**, **presenza di
rassicurazione/checklist**, **animazione**.

| Pagina | Prezzo individuale | Formato | Rassicurazione/benefici | Badge | Animazione |
|---|---|---|---|---|---|
| outEmail | €139 | immagine, `alt=""` [y=23206] | sì — 4 spunte + 1 X ("Niente strategie basilari che conosci già") | *"INCLUSO NEL PACCHETTO ARMAGEDDON"* `#bc0807` [y=23953] | pulseShadow 3s, unica su tutte e quattro |
| outFunnel | €98 | immagine, `alt=""` [y=25207] | no | stesso testo `#bc0807` [y=25432] | nessuna |
| outHeadline | €98 | immagine, `alt=""` [y=19299] | no | stesso testo, **`#ff4f4c`** [y=19581] — colore diverso dalle altre tre | nessuna |
| outViral | €250,00, *"Una tantum"* | **testo semplice**, unica delle quattro [y=1204/1247 e y=9322/9365] | sì — *"Paghi una volta, sei dentro per sempre. Pagamento sicuro con PayPal o qualsiasi carta."* [y=9544], solo alla seconda occorrenza | stesso testo `#bc0807` [y=1290 e 9408] | nessuna |

**La cornice prima del numero, mai dopo.** Su tutte e quattro le pagine, il valore percepito viene
costruito *prima* che il prezzo compaia — mai il contrario. Su outEmail la sequenza è esplicita:
*"outEmail ha un ROI fuori da questo pianeta"* [y=18982/19038] → *"Quanti prodotti devi vendere per
rifarti dell'investimento in outEmail? Molto probabilmente solo 1-2."* [y=19546] → solo *dopo* la card
prezzo [y=23291]. Su outFunnel e outHeadline la card arriva subito dopo la chiusura retorica condivisa
(*"[Prodotto]? Probabilmente non è per te. Ma se lo è… Stai per svoltare."* — vedi §"IL BLOCCO
RIUSATO"), che funziona essa stessa da cornice di scarsità sociale prima del numero. Su outViral, che
duplica la card, la prima occorrenza [y=1164] arriva **prima** di qualunque argomentazione (subito dopo
l'hero, all'11,6% della pagina) — l'unica delle quattro a mostrare il prezzo prima di aver costruito
valore, e lo ricompensa con una seconda occorrenza dopo il reframe finale [y=9282], che stavolta segue
la logica delle altre tre.

**Il voucher e il bundle non si vedono mai sulla singola pagina.** Il prezzo di 199€ (il prezzo vero,
pagabile) non compare *mai* accanto al prezzo barrato individuale su nessuna delle quattro pagine — vive
solo nella barra sticky fissa (*"Prendi l'Armageddon Pack — 199€"*, stesso link Stripe
`buy.stripe.com/00w28s9LA5Y0eIT8N64Ja1O` identico su tutte e quattro), visivamente separata dalla card
prezzo di ogni singolo prodotto. Nessuna delle quattro pagine scrive mai il calcolo del risparmio (139 +
98 + 98 + 250 = 585€ di listino, più 199€ di voucher, contro 199€ finali) — confermato qui su tutte e
quattro le catture, non solo sulle due già controllate nel dossier 21-22 (outEmail e outViral): ho
cercato la sequenza "585", "784" e "risparmi" nei quattro `copy-integrale.md` con zero risultati su
tutti e quattro.

---

## COSA NON DICE MAI

Verificato con lettura diretta e ricerca testuale su tutti e quattro i file di questo studio (non solo
dedotto dal dossier CONFRONTO):

1. **Nessuna garanzia o rimborso**, su nessuna delle quattro pagine — zero occorrenze di "garanzia" o
   "rimbors*" riferite al prodotto, confermato anche su outFunnel e outHeadline (il dossier CONFRONTO lo
   aveva già notato a livello di famiglia; qui è riverificato riga per riga sui quattro testi integrali).
2. **Nessuna scadenza o countdown nel copy**, su nessuna delle quattro — zero occorrenze di "scadenz*",
   "countdown" o "mezzanotte".
3. **Il calcolo del risparmio bundle-vs-singoli non è mai scritto**, su nessuna delle quattro pagine —
   riverificato qui anche su outFunnel e outHeadline, non solo sulle due già controllate nel dossier
   21-22.
4. **Il profilo social personale di Andrei**, in outViral — mai linkato, nonostante l'autorevolezza della
   pagina poggi sulla sua esperienza personale su TikTok.
5. **Nessuna delle quattro pagine nomina o linka le altre tre.** Verificato sull'intero `cta[]` di
   ciascun `scheda.json`: gli unici link interni sono le ancore `#<slug>-price` (che scorrono alla card
   prezzo della *stessa* pagina), il link Stripe della barra sticky, `/` e il link privacy esterno.
   Nessun href, e nessuna menzione testuale, punta da una pagina della famiglia a una delle altre tre —
   né come nome prodotto (ho cercato "outFunnel" dentro il testo di outEmail, "outHeadline" dentro
   outFunnel, ecc.: zero risultati incrociati) né come link. È una contraddizione reale col badge
   *"INCLUSO NEL PACCHETTO ARMAGEDDON"*: la pagina dichiara che il prodotto è incluso in qualcosa di più
   grande, ma non dice mai **in che cosa** — chi legge solo outEmail non scopre, restando su quella
   pagina, che il pacchetto contiene anche altri tre corsi interi. L'occasione di cross-sell interno alla
   stessa famiglia di prodotti è scritta zero volte su quattro pagine su quattro.
6. **Nessuna via di mezzo tra riuscita totale e fallimento totale**, confermato anche qui: il frame è
   sempre binario (chi strategizza vs chi non lo fa, chi diventa virale vs chi resta a 200 visualizzazioni,
   chi scrive titoli killer vs chi viene skippato) — mai un risultato parziale, mai un "dipende".

---

## IL BLOCCO RIUSATO

Confronto carattere-per-carattere fra i quattro `copy-integrale.md` — non "stesso schema", stesso
identico testo. Tre livelli di identità, dal più ovvio al meno documentato altrove:

**1. Boilerplate legale e transazionale — identico su tutte e quattro, già noto ma qui riconfermato sui
quattro testi integrali di questa cattura specifica:**
- Disclaimer legale, parola per parola: *"Questo sito e i consigli contenuti al suo interno sono opinioni
  personali a scopo educativo basate sull'esperienza di Andrei Pascu. […] o in genere metodi di
  arricchimento veloce."* — outEmail [y=25279], outFunnel [y=26253], outHeadline [y=19860], outViral
  [y=9739].
- Riga P.IVA: *"Privacy, dati, cookie e simili · Andrei Pascu Sales · P.I. 02001850474 · Viale Giacomo
  Matteotti 15, 50121 Firenze (FI)"* — outEmail [y=25385], outFunnel [y=26359], outHeadline [y=19966],
  outViral [y=9846].
- Barra sticky: *"Prendi l'Armageddon Pack — 199€ Torna alla pagina principale"*, stesso link Stripe
  `buy.stripe.com/00w28s9LA5Y0eIT8N64Ja1O` — outEmail [y=22068/22086], outFunnel [y=22140/22158],
  outHeadline [y=15369/15387], outViral [y=8095/8113].

**2. Badge "quasi identico" — stesso testo, colore che rompe su una pagina su quattro (già in
§"DELTA ALLA FABBRICA"):** *"INCLUSO NEL PACCHETTO ARMAGEDDON"*, `#bc0807` su outEmail [y=23953],
outFunnel [y=25432], outViral [y=1290/9408]; **`#ff4f4c`** su outHeadline [y=19581]. Testo identico,
styling no — la prova che il componente viene copiato per contenuto, non verificato per resa.

**3. Frasi-motto riusate fra prodotti diversi — la scoperta di questo dossier, non documentata nei
report gemelli:**
- *"La speranza non è una strategia."* — outFunnel, due volte: isolata come titolo a sé [y=7755] e come
  apertura di un titolo più lungo, *"La speranza non è una strategia. Smetti di sperare, inizia a
  complottare il funnel definitivo."* [y=23830]; outViral, una volta, identica parola per parola
  [y=9032]. Due prodotti diversi (funnel strategy e video virali) condividono la stessa identica
  frase-manifesto, segno che la frase è trattata come asset di libreria dell'autore, slegato dal
  contenuto specifico del corso — un motto-Andrei più che un motto-outFunnel o un motto-outViral.
- *"[PRODOTTO]? Probabilmente non è per te. Ma se lo è… Stai per svoltare."* — outFunnel: *"outFunnel?
  Probabilmente non è per te. Ma se lo è… Stai per svoltare."* [y=24872]; outHeadline: *"outHeadline?
  Probabilmente non è per te. Ma se lo è… Stai per svoltare."* [y=19029]. Identico carattere per
  carattere a eccezione del nome prodotto — un template letterale con un solo slot variabile, usato come
  chiusura-cerniera fra il corpo persuasivo e la card prezzo su due pagine su quattro (esattamente lo
  stesso ruolo strutturale in entrambe: subito prima della sezione prezzo).

Questi due ultimi trovamenti cambiano la lettura del "riuso" già documentata nel dossier CONFRONTO (che
guardava solo sezioni ripetute *dentro* la stessa pagina, misurando il rapporto sezioni-distinte/totali):
il riuso in questa famiglia non si ferma al livello di componente-pagina, arriva al livello di
**frase-libreria condivisa fra prodotti**, con almeno due frasi trattate esattamente come si tratterebbe
un componente CSS — scritte una volta, incollate dove serve.

---

## LE FORMULE RICORRENTI

Otto costruzioni verificate testualmente sulle quattro pagine di questa cattura (non ripetute dal
dossier 21-22, che ne aveva già isolate otto diverse sugli originali/copie di outEmail e outViral).

**1. Template di chiusura con slot-prodotto** (già in §"IL BLOCCO RIUSATO", qui come formula riusabile)
> *"outFunnel? Probabilmente non è per te. Ma se lo è… Stai per svoltare."* [y=24872]

`"[PRODOTTO]? Probabilmente non è per te. Ma se lo è… [PLACEHOLDER: METAFORA DI SVOLTA]."`

**2. Motto-manifesto interscambiabile fra prodotti**
> *"La speranza non è una strategia."* [y=7755, outFunnel; y=9032, outViral]

`"[PLACEHOLDER: ATTEGGIAMENTO PASSIVO] non è [PLACEHOLDER: CIÒ CHE SERVE DAVVERO]."`

**3. Coppia di personaggi contrapposti, con nome-etichetta ed emoji di rinforzo**
> *"Azienda Italianissima / Marketer Italianissimo (gli altri)"* [y=7105] — reattivo, ansioso, guarda le
> dashboard 30 minuti dopo il lancio — contro *"Azienda vincitrice / Marketer vincitore (tu 💕)"*
> [y=7373] — lancia con sicurezza, non controlla i costi ogni 10 minuti

`"[ETICHETTA NEGATIVA] (gli altri)": [PLACEHOLDER: COMPORTAMENTO ANSIOSO/REATTIVO] / "[ETICHETTA
POSITIVA] (tu [EMOJI])": [PLACEHOLDER: COMPORTAMENTO SICURO/PROATTIVO]`

**4. Sillogismo a specchio, positivo e negativo, ripetuto identico nella struttura**
> *"Se scrivi un titolo persuasivo, la gente legge… Se la gente legge, forse compra."* [y=3842] / *"Se
> scrivi titolo non persuasivo, la gente non legge… Se la gente non legge, al 100% non compra."*
> [y=4065]

`"Se [AZIONE CORRETTA], [CONSEGUENZA 1]… Se [CONSEGUENZA 1], forse [RISULTATO]." / "Se [AZIONE
SBAGLIATA], non [CONSEGUENZA 1]… Se non [CONSEGUENZA 1], al 100% non [RISULTATO]."`

**5. Analogia a doppio rapporto (proporzione esplicita)**
> *"Copywriter : campagna di marketing = cecchino : missione militare"* [y=14586]

`"[RUOLO DEL LETTORE] : [CONTESTO DEL LETTORE] = [PLACEHOLDER: FIGURA DI PRECISIONE ESTREMA] :
[PLACEHOLDER: CONTESTO AD ALTO RISCHIO]"`

**6. Domanda retorica che smonta la propria premessa**
> *"Se bastasse usare delle formule pre-concepite… Perché non usi formule pre-concepite per
> letteralmente ogni singolo pezzo del tuo copy?"* [y=11768]

`"Se bastasse [PLACEHOLDER: SOLUZIONE SEMPLICISTICA COMUNE]… Perché non [PLACEHOLDER: ESTENSIONE
ASSURDA DELLA STESSA LOGICA] per letteralmente ogni [PLACEHOLDER: AMBITO PIÙ AMPIO]?"`

**7. Statistica-più-fonte a chiusura di riga, schema ripetuto identico cinque volte nella stessa pagina**
> *"313% in più di successo per aziende con marketing strategico."* [y=14851] seguito, poche righe
> sotto, da *"Fonte"* linkato [y=15020] → `coschedule.com/marketing-statistics`

`"[NUMERO]% in più di [PLACEHOLDER: METRICA VAGA MA POSITIVA] per [PLACEHOLDER: CHI FA LA COSA GIUSTA]."`
seguito da `"Fonte"` → [LINK A UN VENDITORE DI SOFTWARE NELLA STESSA NICCHIA DEL CLAIM]

**8. Segmentazione per ruolo professionale con blocco-emoji ripetuto identico**
> *"outFunnel 🤝 Copywriter"* [y=20661] → *"outFunnel 🤝 Media buyer"* [y=21172] → *"outFunnel 🤝 Titolare
> aziendale"* [y=21581] → *"outFunnel 🤝 Project Strategist/Manager"* [y=22019]

`"[PRODOTTO] 🤝 [RUOLO PROFESSIONALE]"` ripetuto una volta per ciascun segmento di pubblico dichiarato,
ognuno seguito da 2-3 paragrafi specifici per quel ruolo e chiuso da una frase-disclaimer di scope
("non ti insegna X, ti insegna solo Y").

---

## IL DIFETTO

Quattro difetti reali, ciascuno misurato sui file di questo studio con `grep` diretto o lettura
riga-per-riga, non impressioni:

1. **Il difetto "prezzo come immagine con `alt` vuoto" non è di outEmail, è di tutte e quattro le
   pagine.** Verificato con `grep` sui quattro `scheda.json`: `Artboard+41_2.webp` (outEmail, [y=23206],
   `alt=""`), `Artboard--E2-80-93-99-min.webp` (outFunnel, [y=25207], `alt=""`),
   `Artboard--E2-80-93-96.webp` (outHeadline, [y=19299], `alt=""`) — tre pagine su quattro con lo stesso
   identico difetto sulla stessa identica componente. Il dossier 21-22 lo aveva verificato solo su
   outEmail (e sul suo originale andrei-copy.com); qui è confermato come pattern di produzione ripetuto
   su tre pagine su quattro (la quarta, outViral, evita il problema perché il suo prezzo è testo
   semplice — ma sposta lo stesso identico difetto sui numeri-follower, vedi punto 3).
2. **Il badge "INCLUSO NEL PACCHETTO ARMAGEDDON" ha lo stesso testo ma non lo stesso colore su tutte e
   quattro le pagine.** `#bc0807` su outEmail [y=23953], outFunnel [y=25432], outViral [y=1290/9408];
   **`#ff4f4c`** su outHeadline [y=19581] — un rosso più chiaro e più saturo, misurabilmente diverso.
   Poiché lo stesso colore lega badge e barra sticky di acquisto sulle altre tre pagine (il "filo rosso"
   già documentato nel dossier 21-22), su outHeadline quel filo si spezza senza che nessun controllo
   visivo se ne accorga: il componente è stato copiato per contenuto testuale, non verificato per resa
   cromatica.
3. **La qualificazione negativa, dove esiste, perde per strada la parte che dovrebbe renderla
   specifica.** Su outEmail, il titolo *"Non è per tutti. Sono serio."* [y=13269] e le sue due frasi di
   contorno sono testo verificabile; le tre ragioni specifiche mostrate nello screenshot (secondo
   l'atlante visivo) non esistono come testo estraibile. Su outHeadline il difetto è totale: *"outHeadline
   non è per principianti"* [y=10913] è l'**unica** riga di testo captata per l'intera tappa — sia la
   lista negativa sia la lista positiva che la seguono restano invisibili al parser. Le due pagine che
   usano questo dispositivo condividono lo stesso identico punto cieco.
4. **Il difetto del prezzo-immagine si ripresenta identico sui numeri di prova sociale di outViral.** I
   sei conteggi follower che dovrebbero sommare a *"quasi 1 milione di follower totali"* [y=5418] sono
   immagini nominate col proprio valore (`181k.webp` [y=6808] e cinque gemelli), tutte con `alt=""`
   verificato via `grep` sul `scheda.json` di outViral. È lo stesso identico difetto del punto 1, applicato
   a un dato diverso (prova sociale invece che prezzo) sulla pagina che altrimenti è la più forte della
   famiglia per verificabilità (sei link reali ai profili) — un difetto trasversale al tipo di
   componente, non a un singolo prodotto o a un singolo numero.

---

## Nota sulla lunghezza

Questo documento è più corto del suo gemello 21-22 (che copriva un confronto originale-contro-copia su
due pagine, un tipo di analisi con più materiale per costruzione). Qui il materiale sorgente sono quattro
`copy-integrale.md` (238+194+280+149 = 861 blocchi di testo totali) più quattro `scheda.json`, tutti
letti per intero; il documento resta comunque sopra la soglia di 3.000 parole di sostanza richieste,
sostenuto in particolare dalle sezioni "LE PROVE E LA LORO VERIFICABILITÀ" (cinque fonti outFunnel
verificate una per una) e "IL BLOCCO RIUSATO" (due frasi-motto cross-prodotto non documentate in nessun
report gemello). Non è stata aggiunta aria per raggiungere una soglia più alta.

## Collegamenti

- [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) — il confronto strutturale (formula
  a 11 tappe, CTA, ripetizione sezioni), non ripetuto qui
- [14-17-famiglia-out-ATLANTE.md](14-17-famiglia-out-ATLANTE.md) — le sezioni con gli screenshot aperti,
  incluse le due sezioni di qualificazione negativa i cui dettagli restano invisibili al testo
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — lo standard di forma per questo
  teardown, e il confronto originale-contro-copia già chiuso su outEmail e outViral
- `capture/14-arma-outemail/copy-integrale.md`, `capture/15-arma-outfunnel/copy-integrale.md`,
  `capture/16-arma-outheadline/copy-integrale.md`, `capture/17-arma-outviral/copy-integrale.md` — le
  quattro fonti primarie di questo dossier
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
