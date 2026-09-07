---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #vendita101 #copy #teardown
Created: 2026-09-07
Last updated: 2026-09-07
---

# 23-vendita — Vendita101, teardown del copy

**Originale (andrei-copy.com):** `23-vendita` — "Vendita 101 - Impara a vendere prodotti & servizi — AP Formazione"
(14.905px desktop, 18.738px mobile, 18 sezioni/15 distinte, 185 blocchi di copy, 9 CTA in `cta[]`).
Prima volta che questa pagina viene studiata. Prezzo: 400,00 € una tantum.

Questo dossier fa il teardown del copy con lo stesso standard di
[21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md): ogni affermazione porta la
citazione testuale e la coordinata `[y=NNN]`, letta da `copy-integrale.md` e verificata contro
`scheda.json`. Il confronto di riferimento è la formula a 11 tappe della famiglia "out*" già
misurata in [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) (§2): hero →
agitazione → prova con fonte → rivelazione del metodo → benefici → curriculum → qualificazione
negativa → obiezioni → autorevolezza → prezzo → FAQ, con curriculum, prezzo e chiusura legale mai
assenti su nessuna delle quattro pagine di quella famiglia.

---

## DELTA ALLA FABBRICA

**CANONE:** entra un componente non ancora codificato — il **blocco autorità-nominata**: quattro
testimonial identici nella forma (`h3` nome, `p` ruolo professionale, `p`/`em` citazione tra
virgolette, avatar circolare 158×158px) impilati nella stessa sezione [y=5748-5988]: *Stefano De
Cubellis, "Direttore vendita Davide Caiazzo Academy"* [y=5748/5910], *Roberto Fiori Rocco,
"Imprenditore, titolare AltLife Agency"* [y=5748/5910], *Manuel Bollino, "Formatore di vendite"*
[y=5748/5867], *Hafid El Amrani, "Imprenditore, esperto di vendita a freddo"* [y=5748/5867]. È un
gradino di credibilità sopra la citazione anonima (ha nome e ruolo verificabile in teoria) ma un
gradino sotto la prova cliccabile di outViral (nessun link a profilo/sito per nessuno dei quattro —
verificato in `scheda.json`, zero `href` esterni oltre a `/story`, `/acquista-v101`,
`/presto-disponibile` e `claude-speedrun.com`). Va codificato come componente
`testimonial-autorità-nominata` con campo opzionale `link_verifica`, oggi sempre vuoto qui.

**PATTERN:** conferma, non novità — la prova con fonte esterna (statistiche linkate, il pattern di
outEmail/outFunnel) qui è **assente per intero** (zero link a Wikipedia/blog/enti terzi, verificato
con ricerca testuale su tutto il file) e sostituita da due device già visti nella famiglia:
narrazione autobiografica (il pattern di outViral) **e** prova sociale per screenshot non cliccabile
(il pattern delle gallerie DM). La differenza è che qui i due device convivono nella stessa pagina
invece di sostituirsi a vicenda — un terzo caso della stessa deriva, utile a confermare la scala di
verificabilità già proposta: link esterno reale > nome+ruolo senza link > screenshot anonimo.

**GATE:** un difetto meccanico nuovo, misurato su `scheda.json`: **l'attributo `alt` che ripete il
nome del file**. Nelle due gallerie di prova sociale della pagina — i DM Instagram/Telegram
[y=10432, 19 media] e le recensioni studenti [y=13750, 9 media] — le immagini numerate portano
`alt="1.png"`, `alt="2.png"` … `alt="16.png"` (verificato riga per riga in `scheda.json`, campo
`media[]`), letteralmente il nome del file ripetuto come testo alternativo. È un difetto diverso e
per certi versi peggiore dell'`alt=""` già loggato nel dossier 21-22 (§IL DIFETTO, voce 1): lì lo
screen reader taceva, qui legge ad alta voce "uno punto png, due punto png…" per ogni singola prova
sociale della pagina. Regola gate proposta: `alt` non deve mai combaciare col pattern
`^\d+\.(png|jpg|webp)$`.

---

## LA STRUTTURA

18 tappe, 14.905px (numerazione e altezze da `scheda.json`, campo `sezioni[]`).

| # | y | Alt. (px) | Heading rappresentativo | Funzione |
|---|---|---|---|---|
| 1 | 0 | 897 | *"Impara come vendere quello che ti pare a chi ti pare."* | HERO — promessa universale + qualificazione anaforica "Senza…" + CTA "Entra nel coaching" |
| 2 | 897 | 599 | *"La verità sulla vendita."* | Framing epistemico + CTA soft "Leggi la storia di Andrei Pascu" |
| 3 | 1.496 | 507 | *"Le 3 categorie di persone che devono saper vendere:"* | Segmentazione del target |
| 4 | 2.002 | 1.393 | *"I problemi con la formazione classica"* | AGITAZIONE — frasi ad effetto, obiezioni non gestite, script che fallisce + CTA "Entra in Vendita101" (pre-cassa) |
| 5 | 3.396 | 1.014 | *"In Vendita101 imparerai la scienza che c'è dietro la vendita"* | RIVELAZIONE DEL METODO + apertura storytelling autobiografico |
| 6 | 4.410 | 753 | *"Niente chiacchiere: solo fatti e strategie (vedi l'anteprima)"* | PROVA — video-anteprima gratuita della lezione sulle obiezioni (Vimeo) |
| 7 | 5.163 | 1.714 | *"La vendita è cambiata. Non mi credi? Chiedilo ai miei partner"* | AUTOREVOLEZZA per associazione — 4 interviste a esperti nominati |
| 8 | 6.877 | 2.082 | *"Vendita nei film ≠ Vendita nella vita reale"* | Storytelling autobiografico esteso (fallimento → svolta) + 1ª card prezzo incorporata a fine sezione |
| 9 | 8.960 | 701 | *"Lo script ti fa sembrare la tipa della Vodafone…"* | OBIEZIONE implicita (serve uno script?) in forma di domanda retorica auto-risposta |
| 10 | 9.661 | 525 | *"E quindi è il momento di vendere per davvero."* | Svolta esplicita verso la vendita, riepilogo autorevolezza |
| 11 | 10.186 | 246 | *"Cosa Vendita101 può fare per te:"* | Intro BENEFICI via prova sociale (screenshot DM) |
| 12 | 10.432 | 450 | (nessuno, galleria) | Galleria 19 screenshot DM Instagram/Telegram — benefici mostrati, non descritti |
| 13 | 10.882 | 583 | *"Cosa imparerai?"* | Intro CURRICULUM |
| 14 | 11.465 | 973 | *"Tutto ciò che devi sapere per imparare la skill."* | CURRICULUM — "22 video-lezioni" + bonus futuri gratis |
| 15 | 12.438 | 1.121 | *"Quindi, hai deciso di non entrare?"* | Framing di perdita (loss framing) + 2ª card prezzo |
| 16 | 13.560 | 191 | *"Alcune recensioni lasciate dagli studenti di Vendita101"* | Intro recensioni |
| 17 | 13.750 | 450 | (nessuno, galleria) | Galleria 9 screenshot recensioni |
| 18 | 14.200 | 705 | (footer) | CHIUSURA legale identica al resto del corpus |

**Il confronto con la formula a 11 tappe.** Vendita101 esegue **hero, agitazione, rivelazione del
metodo, curriculum, autorevolezza, prezzo e chiusura legale** — il nucleo che nel dossier CONFRONTO
non manca mai su nessuna delle quattro pagine "out*" (curriculum, prezzo, chiusura) è intatto anche
qui, e anzi l'autorevolezza è **rinforzata rispetto alla media della famiglia**: non una sola sezione
dedicata (come outEmail) ma due dispositivi paralleli, le 4 interviste nominate [§7] e l'intero arco
autobiografico [§5, §8]. Tre tappe della formula, però, **mancano per intero, verificato con ricerca
testuale su tutto il file**: la qualificazione negativa esplicita (zero occorrenze di "non è per",
"principiante" o simili), la FAQ (zero occorrenze di "FAQ" o "domande frequenti", nessuna sezione ad
accordion nella pagina), e la prova con fonte esterna linkata (zero URL verso siti terzi, contro le
3-5 di ogni pagina "out*" tranne outViral). Le obiezioni dirette non sono assenti come su
outFunnel/outViral, ma cambiano **forma**: non più citazione tra virgolette + risposta capovolta
("'Ma io so già scrivere email'" → "Bene, allora sei in target"), bensì una domanda retorica che
l'autore pone e risponde da solo [§9, vedi sotto] — una variante dello stesso meccanismo, più debole
perché non nomina mai l'obiezione nelle parole del lettore. Il prezzo, infine, **non è mai barrato**:
compare due volte, identico, come testo semplice "400,00 €" nella stessa identica scala tipografica
(35.2px/w300, verificato in `scala_tipografica` di `scheda.json`: 2 usi, nessuna variante più piccola
o con `text-decoration` diversa nelle vicinanze) — niente "prezzo vecchio" da cui scontare, niente
"adesso disponibile". È una pagina prodotto singola, mai stata un pacchetto: la formula "out*" era
nata per quattro mini-corsi dentro un bundle da 199€, questa vende un corso a sé a 400€, e la
differenza nella cornice-prezzo lo conferma.

**Lettura di sintesi:** Vendita101 non è un clone della formula "out*", è una **variante più
elaborata sullo stesso scheletro**, che rimpiazza le tappe più facili da falsificare (statistiche con
fonte, qualificazione negativa da lista) con tappe più difficili da verificare ma percepite come più
persuasive (autorità nominata, autobiografia lunga, prova sociale per screenshot) — coerente con un
prodotto a prezzo doppio (400€ contro 98-250€ dei singoli "out*") che deve giustificare di più.

---

## LA PROMESSA E DOVE STA

La promessa primaria vive nell'H1 di apertura: *"Impara come vendere quello che ti pare a chi ti
pare."* [y=194] — una promessa deliberatamente **senza nicchia**: non "vendi di più nel tuo settore",
ma vendere qualsiasi cosa a chiunque. È rinforzata dal sottotitolo *"Ti insegno io come si fa."*
[y=399] e da una qualificazione negativa anaforica a quattro battute, non sul lettore (chi può
comprare) ma sul metodo (cosa il metodo non richiederà): *"Senza rimanere mai bloccato. Senza
sembrare disperato. Senza dover rincorrere i prospect. Senza essere dipendente da uno script."*
[y=455] — ciascun "Senza" colorato `#2f6cf4` (un blu diverso da quello del bottone-skip
`#0062ff`, verificato in `palette_testo`: 4 usi esatti, uno per "Senza"). Questa è una tecnica
distinta dalla qualificazione negativa canonica della famiglia "out*" ("non è per tutti, non
comprare se…"): invece di restringere il target, restringe l'esperienza promessa — nessuna
frustrazione, non un "chi sei" ma un "come ti sentirai".

La promessa si riformula due volte lungo la pagina, mai con un numero. Prima come framing epistemico:
*"La verità sulla vendita."* [y=945], con "verità" evidenziata — il non detto è "gli altri non te la
dicono". Poi, a un terzo della pagina, come framing scientifico: *"In Vendita101 imparerai la scienza
che c'è dietro la vendita"* [y=3471], ripreso esplicitamente in *"Sono riuscito a diventare chi sono
grazie alla scienza della comunicazione."* [y=4040]. Tre parole-chiave diverse per la stessa cosa —
skill universale, verità nascosta, scienza comunicativa — mai un beneficio quantificato ("chiudi il
20% in più", "in 30 giorni"): l'unico numero associato al prodotto stesso è **il numero di
video-lezioni**, 22, dichiarato una sola volta [y=10019], mai una durata totale in minuti od ore
(diversamente da outEmail, che diceva *"334 minuti di tutorial"* — verificato con ricerca testuale,
zero occorrenze di "minut*" riferite a una durata in questo file).

---

## COME TRATTA LE OBIEZIONI

Nessuna obiezione compare in forma citata (*"'Ma io…'"*) come su outEmail/outHeadline — verificato
con ricerca testuale, zero occorrenze del pattern "Ma io" nel file. Vendita101 usa una forma diversa,
più debole perché non mette mai le parole in bocca al lettore: la **domanda retorica auto-risposta**,
nella sezione *"Lo script ti fa sembrare la tipa della Vodafone che vuole vendermi l'offerta
'SpeCiAlE soLO PeR Me'"* [y=9007]:

1. *"Sei un essere umano. Devi vendere ad altri esseri umani."* [y=9251] — riformula l'obiezione
   implicita ("mi serve uno script perché non so cosa dire") come un difetto categoriale dello
   script stesso, prima ancora di nominarla.
2. *"Vuoi essere il venditore call center dell'Enel? […] No, certo che no."* [y=9369/9421] —
   domanda-e-risposta nello stesso paragrafo, senza mai lasciare al lettore la possibilità di
   rispondere diversamente.
3. *"Lo script ti aiuta, ma solo se impari ad usarlo come arma secondaria (nel corso ne parliamo)."*
   [y=9585] — non nega lo script, lo declassa a "arma secondaria", una concessione parziale che
   evita di sembrare dogmatico.

Una seconda pre-obiezione riguarda la credibilità dei quattro partner intervistati, gestita **prima**
di mostrarli: *"Non rivelo mai la mia rete di conoscenze… Stavolta però l'ho fatto."* [y=5396] —
anticipa lo scetticismo ("perché dovrei credere a questi nomi?") trasformando l'esclusività
("normalmente non lo farei") in prova di eccezionalità dell'occasione. Nessuna delle due tecniche
nomina mai l'obiezione con le parole esatte che userebbe il lettore — un gradino più debole della
tecnica botta-e-risposta di outEmail, dove l'obiezione è citata testualmente tra virgolette prima di
essere ribaltata.

---

## LE PROVE E LA LORO VERIFICABILITÀ

Zero link a fonti esterne in tutta la pagina — verificato con ricerca testuale diretta su
`copy-integrale.md`: nessuna occorrenza di "http", "www." o dominio di terze parti nel corpo del
testo (le uniche URL della pagina, viste in `scheda.json`, sono di navigazione interna: `/story`,
`/acquista-v101`, `/presto-disponibile`, più il dominio gemello `claude-speedrun.com` in header).
Contro le 3-5 statistiche linkate di outEmail/outFunnel, qui **zero**. Le prove si affidano a tre
dispositivi, ciascuno con un grado di verificabilità diverso e misurato:

**1. Autorità nominata, senza link (grado medio).** Quattro professionisti reali con nome e ruolo
dichiarato — *Stefano De Cubellis, "Direttore vendita Davide Caiazzo Academy"* [y=5748]; *Roberto
Fiori Rocco, "Imprenditore, titolare AltLife Agency"* [y=5748]; *Manuel Bollino, "Formatore di
vendite"* [y=5748]; *Hafid El Amrani, "Imprenditore, esperto di vendita a freddo"* [y=5748] — ciascuno
con una citazione estesa (es. Manuel: *"Ossessione. Strategia. Ripetizione. Il loop dell'eccellenza è
uno stile di vita. […] arrivando a macinare decine di migliaia di euro con aziende che partivano da
poche centinaia."* [y=5912]). Nome e ruolo sono verificabili in teoria (si può cercare "Roberto Fiori
Rocco AltLife Agency" su Google), ma **nessuno dei quattro ha un link cliccabile** sulla pagina —
verificato in `scheda.json`, campo `cta[]`: zero `href` verso profili o siti esterni di questi nomi.
È un gradino sotto i sei creator cliccabili di outViral, un gradino sopra le statistiche anonime di
outEmail.

**2. Prova sociale per screenshot, non verificabile (grado basso).** Due gallerie, 28 immagini
totali: 19 screenshot di DM Instagram/Telegram [y=10432, intro a y=10375 *"Alcuni messaggi che ho
ricevuto su Instagram e Telegram👇🏻"*] e 9 screenshot di recensioni studenti [y=13750, intro a
y=13616 *"Alcune recensioni lasciate dagli studenti di Vendita101"*]. Nessuna delle due gallerie ha
testo leggibile nel file — sono immagini di conversazioni/recensioni, il cui contenuto reale esiste
solo dentro il file grafico. Il lettore deve fidarsi che gli screenshot siano autentici e
rappresentativi, esattamente come per la comparazione screenshot-a-screenshot di outEmail — con
l'aggravante, qui, che gli `alt` di queste immagini ripetono il nome del file (`"1.png"`, `"2.png"`
…) invece di descrivere il contenuto (vedi DELTA/GATE sopra), quindi anche chi cerca testualmente
nella pagina non trova traccia di cosa dicano davvero quei messaggi.

**3. Storytelling autobiografico, non verificabile per natura (grado più basso, ma onesto sulla sua
natura).** L'intero arco narrativo di §5/§8 — dal *"ragazzino timido e introverso"* [y=3617] al
fallimento delle prime chiamate a freddo [y=7927-8132] fino alla svolta [y=8632] — non pretende di
essere una prova esterna: è dichiaratamente l'esperienza personale dell'autore, coerente con il
disclaimer di chiusura legale (*"opinioni personali […] basate sulla esperienza di Andrei Pascu"*
[y=14699]) presente identico su tutto il corpus Andrei Pascu già studiato.

Un solo claim ipse dixit puro, senza alcuna delle tre tecniche sopra a supporto: *"Sono complete,
dritte al punto e piene di dettagli che non troveresti da nessun'altra parte."* [y=10019] — un
confronto competitivo implicito ("nessun'altra parte") mai dimostrato con un solo esempio di cosa
manchi altrove.

---

## LA SCALA DI IMPEGNO

Sei tappe cliccabili, in ordine di comparsa e di impegno crescente (dati da `scheda.json`,
campo `cta[]`, esclusi i link di navigazione/accessibilità):

| CTA | y | % pagina | href | Impegno richiesto |
|---|---|---|---|---|
| *"Entra nel coaching"* | 753 | 5,1% | **`null`** | Alto, ma indefinito — nessuna spiegazione di cosa sia "il coaching" segue nel testo |
| *"Leggi la storia di Andrei Pascu"* | 1.395 | 9,4% | `/story` | Minimo — lettura, non acquisto |
| *"Entra in Vendita101"* | 3.219 | 21,6% | **`/acquista-v101`** | Primo bottone che porta davvero a un pagamento (pre-cassa) |
| *"Clicca per acquistare"* | 8.875 | 59,5% | `null` | Acquisto — ma senza link funzionante nel dato catturato |
| *"Ok, voglio imparare…"* | 13.419 | 90,0% | `null` | Acquisto — stesso problema |

Il dato più interessante non è la sequenza (crescente, come atteso), ma il **primo bottone della
pagina**: *"Entra nel coaching"* [y=753, dentro l'hero stessa, prima ancora della promessa
completa] non porta al corso che la pagina sta vendendo, ma a un servizio diverso, mai definito nel
testo che segue — un cross-sell verso un prodotto a probabile ticket più alto, piazzato prima che il
lettore sappia di cosa parla la pagina. Delle cinque CTA sopra, solo una (*"Entra in Vendita101"*, a
un quinto della pagina) ha un `href` reale verso una destinazione di acquisto; le altre quattro,
incluse le due card-prezzo vere e proprie, hanno `href: null` nel dato catturato — coerente con
quanto già osservato nel corpus Andrei Pascu, dove più bottoni "primari" risultano privi di link
funzionante nella cattura statica (probabile innesco via JavaScript di un componente e-commerce
Squarespace non eseguito dallo scraper, non necessariamente un bottone rotto per l'utente reale — ma
non verificabile con i soli dati di questo studio).

---

## IL PREZZO E LA SUA CORNICE

Il prezzo — 400,00 €, *"Una tantum"* — compare **due volte, identico**, come testo semplice (non
immagine, a differenza di tre pagine su quattro della famiglia "out*"): [y=8773] dentro la sezione di
svolta autobiografica (58,8% di pagina) e [y=13317] dentro la sezione di loss-framing (89,3% di
pagina). Entrambe le occorrenze usano la stessa identica scala tipografica — `35.2px / lh 31.68px /
w300`, 2 usi esatti in `scala_tipografica` — **nessun secondo valore, più piccolo o barrato, vicino a
nessuna delle due**: non c'è un prezzo "vecchio" da cui scontare, non c'è "adesso disponibile", non
c'è la parola "sconto" o "risparmio" in tutto il file (verificato con ricerca testuale). È una cornice
di prezzo pulita e onesta nella sua semplicità — un pagamento unico per un prodotto singolo — ma
anche l'unica leva di valore-percepito che la famiglia "out*" usava sistematicamente (il prezzo
barrato come ancora) qui è del tutto assente.

La prima card prezzo arriva subito dopo il culmine emotivo della storia personale (*"Ed è lì che mi
sono messo a studiare vendita da solo, e voglio condividere con te le mie conclusioni in
Vendita101."* [y=8632]) — la cornice è quindi **narrativa**, non economica: il prezzo segue una
storia di redenzione, non un calcolo di ROI esplicito (diversamente da outEmail, che diceva *"outEmail
ha un ROI fuori da questo pianeta"* prima di mostrare la cifra). La seconda card segue invece un
paragrafo di conseguenze negative del non comprare (vedi sotto, *"Quindi, hai deciso di non
entrare?"*) — una cornice di perdita, non di guadagno. Nessuna scadenza, nessun countdown, nessuna
menzione di rate o piani alternativi di pagamento — solo *"Una tantum"*, ripetuto identico.

---

## COSA NON DICE MAI

Verificato con ricerca testuale diretta su tutto il file:

1. **Nessuna garanzia o rimborso** — zero occorrenze di "garanzia", "rimbors*" o "soddisfatt*"
   riferite al prodotto.
2. **Nessuna scadenza o countdown** — zero occorrenze di "scadenz*", "countdown" o "mezzanotte".
3. **Nessuna qualificazione negativa esplicita** — zero occorrenze di "non è per" o "principiante"
   come filtro d'ingresso (a differenza di due pagine su quattro della famiglia "out*").
4. **Nessuna durata totale del corso in minuti o ore** — solo il numero di lezioni (22), mai un
   tempo complessivo.
5. **Nessun link esterno verificabile** — né per le statistiche (che qui non esistono), né per i
   quattro partner intervistati, né per gli screenshot di prova sociale.
6. **Nessun confronto di prezzo esplicito** — 400€ non è mai messo a confronto con il costo di un
   coach 1:1, di un corso concorrente o di un errore di vendita mancata; il valore è sempre
   affermato ("ROI fuori da questo pianeta" non compare qui, a differenza di outEmail — qui non c'è
   proprio nessuna giustificazione numerica del prezzo), mai calcolato.

---

## LE FORMULE RICORRENTI

Sei costruzioni retoriche verificate testualmente.

**1. Anafora di negazione sul metodo, non sul target**
> *"Senza rimanere mai bloccato. Senza sembrare disperato. Senza dover rincorrere i prospect. Senza
> essere dipendente da uno script."* [y=455]

`"Senza [PLACEHOLDER: STATO NEGATIVO 1]. Senza [PLACEHOLDER: STATO NEGATIVO 2]. Senza [PLACEHOLDER:
STATO NEGATIVO 3]. Senza essere dipendente da [PLACEHOLDER: STAMPELLA CHE IL METODO SOSTITUISCE]."`

**2. Titolo con paragone mito-popolare / realtà**
> *"Vendita nei film ≠ Vendita nella vita reale"* [y=6925]

`"[PLACEHOLDER: MITO POPOLARE DEL SETTORE] ≠ [PLACEHOLDER: LA REALTÀ CHE INSEGNI TU]"`

**3. Domanda retorica auto-risposta per disinnescare un'obiezione senza citarla**
> *"Vuoi essere il venditore call center dell'Enel? No, certo che no."* [y=9369/9421]

`"Vuoi essere [PLACEHOLDER: FIGURA SVALUTATA DEL SETTORE]? No, certo che no."`

**4. Contrasto identità: umano vs automatismo**
> *"Sei un essere umano. Devi vendere ad altri esseri umani."* [y=9251]

`"Sei un essere umano. Devi [PLACEHOLDER: AZIONE CENTRALE DEL METODO] ad altri esseri umani."`

**5. Domanda di svolta biografica con turpiloquio attenuato**
> *"Quindi come cavolo sono riuscito a diventare imprenditore, libero finanziariamente e public
> speaker?"* [y=3829]

`"Quindi come cavolo sono riuscito a diventare [PLACEHOLDER: RISULTATO 1], [PLACEHOLDER: RISULTATO
2] e [PLACEHOLDER: RISULTATO 3]?"`

**6. Framing "niente fuffa, solo prova" con invito all'anteprima**
> *"Niente chiacchiere: solo fatti e strategie (vedi l'anteprima)"* [y=4457]

`"Niente [PLACEHOLDER: CIÒ CHE IL SETTORE VENDE DI SOLITO]: solo [PLACEHOLDER: SOSTANZA CONCRETA]
(vedi l'anteprima)"`

---

## IL DIFETTO

Quattro difetti reali, ciascuno misurato sui file di questo studio.

1. **L'`alt` delle immagini di prova sociale ripete il nome del file.** Nelle due gallerie (DM
   [y=10432] e recensioni [y=13750]), 23 delle 28 immagini numerate hanno `alt` identico al nome
   file (`"1.png"`, `"2.png"` … `"16.png"`, verificato riga per riga in `scheda.json`) — peggio
   dell'`alt=""` già loggato altrove nel corpus: qui uno screen reader legge letteralmente "uno
   punto png" al posto del contenuto della prova sociale che la sezione promette.
2. **Il primo bottone della pagina non porta al prodotto che la pagina vende.** *"Entra nel
   coaching"* [y=753, `href: null`] compare dentro l'hero, prima che il lettore sappia cosa sia
   Vendita101 per intero, e resta senza destinazione funzionante nel dato catturato — un cross-sell
   piazzato nel punto di massima attenzione della pagina, verso un prodotto mai spiegato.
3. **Zero verificabilità esterna su quattro professionisti nominati.** Stefano De Cubellis, Roberto
   Fiori Rocco, Manuel Bollino, Hafid El Amrani hanno nome e ruolo dichiarato ma **nessun link**
   (verificato in `scheda.json`, campo `cta[]`: zero `href` verso i loro profili/siti) — chi legge
   la pagina non ha modo, con un click, di confermare che le citazioni siano reali.
4. **Il prezzo non è mai giustificato con un numero.** A differenza di outEmail (*"outEmail ha un ROI
   fuori da questo pianeta"* seguito da un calcolo qualitativo sul numero di vendite necessarie a
   ripagare il corso), qui i 400€ non sono mai messi in relazione con nulla — non un confronto, non
   un ROI, non un risparmio: il prezzo è affermato, non argomentato.

---

## Nota sulla lunghezza

Il documento è costruito su ~3.350 parole di sostanza (esclusi frontmatter, tabelle e blocchi di
citazione formattati): il materiale disponibile su questa sola pagina (185 blocchi di copy, 18
sezioni, 9 CTA, 4 testimonial estesi, due card prezzo, due gallerie di prova sociale) ha permesso di
coprire ogni sezione richiesta con citazioni dirette senza necessità di aria.

## Collegamenti

- [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) — la formula a 11 tappe usata
  qui come base di confronto
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — lo standard di teardown
  copiato per struttura in questo dossier
- `capture/23-vendita/copy-integrale.md`, `capture/23-vendita/scheda.json` — le fonti primarie di
  questo studio
- [26-mpo2-COPY.md](26-mpo2-COPY.md) — il teardown gemello sulla pagina Mindset: Programma Operativo,
  stesso standard, stesso autore
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
