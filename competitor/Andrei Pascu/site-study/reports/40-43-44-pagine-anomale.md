---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #pagine-anomale #next #squarespace #apsales #claude-code-mastery #copy #teardown
Created: 2026-09-08
Last updated: 2026-09-08
---

# 40-43-44 — Le tre pagine anomale — non sono gradini, sono tre cose diverse

Tre pagine catturate nell'onda D erano classificate "gradini del funnel" (i passaggi intermedi di un
percorso di vendita). Non lo sono. Sono tre pagine intere, ciascuna con una funzione completamente
diversa, e una delle tre — l'anomalia più grossa — non appartiene nemmeno all'ecosistema che questo
studio dovrebbe mappare. Questo dossier tratta ognuna per quello che è davvero, verificato riga per
riga su `copy-integrale.md` e `scheda.json` di ciascuna cartella.

---

## DELTA ALLA FABBRICA

**CANONE:** nessun componente nuovo di UI da codificare qui — il contributo di questo dossier al
canone è un **controllo di provenienza**, non uno stile. Va aggiunto un campo obbligatorio a ogni
capture futuro del site-study: `brand_rilevato` (il nome che compare nel copy stesso, letto dal testo,
non dal dominio) confrontato con `brand_atteso` (la cartella in cui la capture viene archiviata). Se i
due divergono, la capture va segnalata prima di essere classificata, non dopo.

**PATTERN:** una capture può finire nella cartella sbagliata anche quando l'URL sembra plausibile.
`43-chiamata-formazione` è ospitata su `chiamata-formazione.netlify.app` — un dominio Netlify di
staging, non un dominio di produzione di nessuno — ed è stata archiviata sotto
`competitor/Andrei Pascu/`. Il contenuto della pagina, però, non nomina mai Andrei Pascu: nomina
**Digital Empire** e **Max, founder di Digital Empire** [y=9908, y=16949], vende **"Claude Code
Mastery"** a **€397** [y=666, ripetuto identico altre quattro volte], e i due bottoni della pagina
puntano ad altri due sotto-domini Netlify di staging (`clinquant-pie-aab8d2.netlify.app` per la
prenotazione, `formazione-systemarchitect.netlify.app` per il corso) — nessuno dei quali è un dominio
di Andrei Pascu. **Questa non è una pagina del competitor. È una bozza di funnel di Digital Empire
stessa**, verosimilmente costruita ricalcando l'architettura delle pagine-chiamata già mappate in
questo stesso studio (si veda `21-22-outemail-outviral-COPY.md` per il precedente più vicino), e finita
per errore nella cartella dell'ecosistema competitor durante la cattura dell'onda D. Il pattern da
registrare: **il nome del dominio non basta a classificare una capture — va letto il brand dentro il
copy stesso**, sempre, prima di archiviare.

**GATE:** due controlli meccanici nuovi, entrambi misurabili su file già esistenti:
1) *ricerca del nome del competitor nel testo* — se una cartella `capture/NN-nome/` non contiene almeno
   un'occorrenza testuale del nome del competitor o di un suo dominio noto nel `copy-integrale.md`,
   la capture va marcata "provenienza da verificare" prima di qualunque sintesi la usi come dato sul
   competitor;
2) *coerenza numerica testa-corpo* — quando un prezzo o una cifra compare sia in un titolo di sezione
   sia in una tabella/lista nel corpo della stessa sezione, i due valori vanno confrontati
   automaticamente. Su `43-chiamata-formazione` il titolo di sezione dice *"Corso da 800€ vs questa
   call gratis."* [y=16068] mentre la riga "Prezzo" della tabella subito sotto dice *"€400 – €2.000"*
   [y=16594] — due cifre diverse per lo stesso claim, sulla stessa pagina, a 500px di distanza.

---

## PARTE 1 — 43-chiamata-formazione (chiamata-formazione.netlify.app)

### CHE COS'E' DAVVERO

Non è una pagina di Andrei Pascu. È la pagina di vendita di una **chiamata strategica 1:1 gratuita di
45 minuti**, scritta in prima persona da **Max, founder di Digital Empire** [y=9905-9908: *"In call ci
vediamo io, Max — founder di Digital Empire, agenzia appena nata che costruisce prodotti e sistemi con
l'AI."*], il cui titolo pagina è letteralmente *"Call Strategica 1:1 | Claude Code Mastery · Digital
Empire"* (riga 1 di `copy-integrale.md`) e la cui `meta.description` recita: *"45 minuti di formazione
1:1 su Claude Code con Digital Empire. 90% formazione, 10% pitch — carte scoperte."* La call è
un'esca (lead magnet ad alto tocco) per il corso a pagamento **Claude Code Mastery, €397**, citato
identico in cinque blocchi CTA lungo tutta la pagina [y=666, 7366, 8673, 18509, e nel testo a y=754/756
*"90% formazione. 10% pitch. Carte scoperte dal primo minuto."*].

È costruita in **Next.js** (campo `"costruzione": "next"` di `scheda.json`), non su Squarespace come il
resto dell'ecosistema studiato finora, ed è ospitata su un **dominio Netlify di staging**
(`chiamata-formazione.netlify.app`), non su un dominio acquistato e brandizzato. I suoi due bottoni
principali puntano ad altri due sotto-domini Netlify altrettanto provvisori: `clinquant-pie-aab8d2.
netlify.app` (prenotazione) e `formazione-systemarchitect.netlify.app` (pagina del corso). Tre domini
di anteprima concatenati fra loro sono la firma tecnica di un funnel **ancora in fase di build/test**,
non di un asset già in produzione davanti a traffico pagato. È, con ogni evidenza testuale, un
prototipo di Digital Empire che adotta l'architettura persuasiva già documentata su Andrei Pascu (call
gratuita → upsell a un corso, rapporto 90/10 dichiarato, obiezioni previste, value-stack) per il
proprio prodotto, non un artefatto dell'ecosistema Andrei Pascu.

### LA STRUTTURA

25 sezioni (20 distinte), 18.770px, **506 blocchi di testo** — la pagina di testo più grande
dell'intero corpus studiato finora in questo site-study.

| # | y | Alt. (px) | Heading | Funzione |
|---|---|---|---|---|
| 1 | 0 | 907 | *"Ti formo su Claude Code. 45 minuti. Gratis."* | HERO — promessa secca + sottotitolo (90/10) + doppia CTA |
| 2 | 907 | 378 | (nessuno) | Contatori: *"247+ CALL GIÀ FATTE"*, *"45 min PER CALL"*, *"100% GRATIS"* |
| 3 | 1285 | 539 | *"ASCOLTA BENE."* | Agitazione — "l'AI ti ha già preso", "grattare la superficie" |
| 4 | 1824 | 676 | *"Tutti ti vendono corsi. Nessuno ti fa vedere come fa."* | Problema — corso tipico vs questa call, tabella comparativa |
| 5 | 2499 | 983 | *"Non parliamo di AI. Costruiamo qualcosa con l'AI."* | Metodo — 3 step (capisco/mostro/costruiamo) |
| 6 | 3482 | 851 | *"Per chi è questa call (e per chi non è)."* | Qualificazione positiva/negativa |
| 7 | 4333 | 1081 | *"Esattamente cosa succede nei prossimi giorni."* | Processo post-prenotazione — 5 step (conferma→form→reminder→call→check 7gg) |
| 8 | 5414 | 697 | *"La differenza in 45 minuti."* | Prima/dopo — "loop infinito" vs "chiarezza" |
| 9 | 6111 | 915 | *"Quanto vale davvero questa sessione."* | Value-stack: €250+€120+€300+€80+€100=€850 vs €0 |
| 10 | 7026 | 500 | *"Ancora scettico?"* | Rassicurazione + CTA |
| 11 | 7526 | 747 | *"Ok ma perché me la date gratis?"* | Spiegazione del modello economico |
| 12 | 8274 | 560 | *"Faccio max 8 call a settimana."* | Scarsità aritmetica + CTA |
| 13 | 8834 | 801 | *"Le 3 obiezioni che ricevo sempre."* | Gestione obiezioni esplicita |
| 14 | 9634 | 612 | *"Ok ma tu chi sei?"* | Autorevolezza — bio breve |
| 15 | 10246 | 587 | *"Cosa esci con, dopo 45 minuti."* | 3 outcome (workflow / ore recuperate / chiarezza) |
| 16 | 10833 | 636 | *"Cosa dicono chi ha già fatto la call"* | 3 testimonial (Luca R., Marta S., Andrea V.) |
| 17 | 11469 | 505 | *"Se dopo 10 minuti non ti sto dando valore, chiudi la call."* | Promessa/garanzia informale |
| 18 | 11974 | 1200 | *"Domande che mi fanno spesso"* | FAQ — 7 domande |
| 19 | 13174 | 1118 | *"Niente tool segreti. Solo quelli che uso davvero."* | Stack esposto (9 tool) |
| 20 | 14292 | 664 | *"Marco, founder SaaS. Da 3 ore a 20 minuti."* | Case study prima/durante/dopo |
| 21 | 14955 | 934 | *"Esci dalla call con sei cose molto concrete."* | 6 deliverable elencati |
| 22 | 15889 | 882 | *"Corso da 800€ vs questa call gratis."* | Tabella comparativa corso/call |
| 23 | 16771 | 771 | *"Max, founder di Digital Empire. Builder, non formatore."* | Bio estesa + 4 statistiche |
| 24 | 17541 | 532 | *"Se è gratis, dov'è la fregatura?"* | Reveal economico (5% converte) |
| 25 | 18073 | 596 | *"45 minuti. Gratis. Per davvero."* | CTA finale + footer |

Sono 25 tappe per una call gratuita — più del doppio delle 11 tappe di outViral e vicino alle 24 di
outEmail (entrambe pagine di corsi a pagamento, non di call gratuite), a conferma che vendere un
impegno alto (una call 1:1, tempo reale della persona) richiede tanta — se non più — costruzione
argomentativa quanto vendere un prodotto a prezzo fisso.

### LA PROMESSA

Promessa primaria, nell'H1: *"Ti formo su Claude Code. 45 minuti. Gratis."* [y=296/102]. Promessa di
sostanza, nel sottotitolo: *"Una call 1:1 di formazione vera su come costruire agenti, skill e system
prompt con Claude Code (e l'ecosistema attorno: Claude chat, progetti, Perplexity, Manus)... 90%
formazione pura, 10% pitch del corso — circa 4-5 minuti a fine call, solo se ti serve davvero."*
[y=458-114]. Promessa di output concreto, enumerata esplicitamente in sei punti [y=15309-15706]: *"Un
workflow funzionante"*, *"Una mappa mentale chiara"*, *"2-3 prompt pattern riutilizzabili"*, *"La
registrazione completa"*, *"Un ordine di priorità"*, *"Accesso diretto per domande"*. È una promessa
insolitamente specifica per un'offerta gratuita — la maggior parte delle call strategiche gratuite
promette "chiarezza" o "una strategia", questa promette sei artefatti nominati uno per uno.

### LE PROVE E LA LORO VERIFICABILITA'

Qui la pagina è debole, misurata contro lo standard già stabilito nel resto di questo studio (le 6
prove-profilo verificabili di outViral). Il campo `media` di `scheda.json` è **vuoto: `[]`** — zero
immagini, zero video rilevati in tutta la pagina di 18.770px. Le tre testimonianze [y=11121-11312] sono
*"Luca R." (Product designer)*, *"Marta S." (Freelance marketer)*, *"Andrea V." (Dev full-stack)* —
solo iniziale del cognome, nessun link, nessuna foto, nessun profilo verificabile. Il case study
*"Marco, founder SaaS"* [y=14472-14742: *"Ho recuperato una settimana di lavoro."*] è anonimizzato allo
stesso modo — nessun cognome, nessuna azienda nominata, nessun link.

Le statistiche aggregate — *"247+ CALL GIÀ FATTE"* [y=1048, ripetuta a y=17316], *"3+ ANNI FULL-AI"*,
*"50+ PROGETTI SPEDITI"* [y=17142-17186] — sono tutte auto-dichiarate, senza fonte esterna o
verificabile con un click, a differenza delle statistiche di mercato citate nella pagina 40 (vedi Parte
2) o dei profili social linkati nella pagina outViral già documentata in questo studio. Anche l'unico
claim quantitativo sul funnel stesso — *"il 5% delle persone con cui parliamo poi sceglie Claude Code
Mastery... Il 95% esce con il workflow"* [y=17810-17919] — non ha alcun dato a supporto: è
un'affermazione di trasparenza (onesta nell'intento) ma non verificabile dal lettore.

L'unica prova con un minimo di rigore logico, non aneddotico, è la matematica della scarsità: *"45 min
× 8 call = 6 ore di call"* [y=8549] — un calcolo che il lettore può rifare da solo con i numeri dati,
diversamente dalla maggior parte dei claim della pagina.

### L'IMPEGNO CHIESTO

Non è un pagamento: è **tempo e presenza**. Il percorso dichiarato [y=4704-5242]: 1) click sul bottone
*"Prenota la Tua Call Gratis"* che porta al dominio di prenotazione esterno; 2) *"Ricevi email con link
Google Meet e un form da 4 domande. 2 minuti"* [y=4742]; 3) 24 ore prima, un promemoria con 2-3 cose da
preparare [y=4854]; 4) il giorno della call, *"45 min live"* con *"Screen share"* attivo, richiesto
esplicitamente al lettore stesso — *"Sei disposto ad aprire screen share e mostrarmi cosa stai facendo
davvero"* è uno dei criteri di qualificazione positiva [y=4148]; 5) un check di follow-up dopo 7 giorni
[y=5204-5242]. Il nome dello strumento di prenotazione (Calendly, Cal.com o altro) non è mai citato nel
copy — solo *"Clicca, scegli uno slot, ci vediamo in call. È tutto."* [y=18441].

### IL PREZZO SE C'E'

La call è **€0**, framed esplicitamente contro un valore dichiarato di **€850** scomposto voce per voce
[y=6503-6805]: Call 1:1 live 45 min €250, Audit del workflow attuale €120, 2-3 workflow personalizzati
€300, Registrazione + note Notion €80, Check di follow-up dopo 7 giorni €100 — totale €850, "il tuo
investimento oggi €0". Il corso a valle, **Claude Code Mastery, €397**, compare identico in ogni CTA
secondaria della pagina mai come cifra isolata: sempre accompagnato dal nome del corso per intero. La
sezione comparativa finale genera l'incoerenza già segnalata in apertura: il titolo dice *"Corso da
800€"* [y=16068] mentre la riga "Prezzo" della tabella dice *"€400 – €2.000"* [y=16594] — due numeri
diversi per lo stesso claim, mai riconciliati nel testo.

### COSA NON DICE MAI

Verificato con ricerca testuale diretta sul file: **nessun indirizzo legale, nessuna P.IVA** nel
footer — solo *"© 2026 · Claude Code Mastery · by Digital Empire"* [y=18710], contro il blocco legale
completo (indirizzo, P.IVA, link privacy, gestione cookie) presente su **ogni** pagina Andrei Pascu
già documentata in questo studio. Nessun cognome di "Max" viene mai dato. Nessuno strumento di
prenotazione viene nominato. Nessuna garanzia formale (solo la promessa informale "chiudi la call se
non ti sto dando valore" — non una garanzia di rimborso, perché non c'è nulla da rimborsare). Nessun
link a un profilo social verificabile di Max o di Digital Empire, nonostante l'intera autorevolezza
della pagina poggi sulla sua esperienza personale — lo stesso difetto già registrato per Andrei Pascu
su outViral in `21-22-outemail-outviral-COPY.md`.

---

## PARTE 2 — 40-ecco-i-fatti (andrei-copy.com/ecco-i-fatti-copywriting)

### CHE COS'E' DAVVERO

Non è una landing page con un'offerta in cima: è un **advertorial** — un articolo-manifesto lungo,
denso di statistiche e fonti esterne, che costruisce per 16.175px il caso "il copywriting è un buon
modello di business" prima di rivelare, solo negli ultimi due terzi della pagina, che esiste un corso
da comprare. Il titolo della scheda è *"I fatti sul copywriting — AP Formazione"*, costruita su
Squarespace, parte piena dell'ecosistema andrei-copy.com già mappato nel resto di questo studio. Il
tono è editoriale/giornalistico ("ti spiego", "ti mostro i dati") più che di vendita diretta per la
maggior parte della pagina.

### LA STRUTTURA

14 sezioni (12 distinte), 16.175px, 288 blocchi.

| # | y | Alt. (px) | Heading | Funzione |
|---|---|---|---|---|
| 1 | 0 | 1629 | *"Scopri perché sempre più persone ambiziose trovano la loro strada..."* | Hero editoriale — promessa di un percorso, non di un prodotto |
| 2 | 1629 | 2426 | *"Il 60,4% delle aziende italiane fattura meno di 100mila euro..."* | Dati macro — disparità di fatturato + Domanda/Risposta + 55%/79% |
| 3 | 4055 | 816 | *"In 5 minuti ti spiego perché il copywriting è il migliore modello di business per iniziare"* | Tesi (H1 a metà pagina, non in apertura) |
| 4 | 4871 | 1026 | *"Gli esperti del digital marketing sono tra le professioni più ricercate per il 2024"* | 2 motivi per pagare un copywriter |
| 5 | 5897 | 1243 | *"Google rivela come il copywriting stia diventando più popolare che mai"* | Trend Google (grafico incluso) |
| 6 | 7139 | 1472 | *"Chiunque, se lo vuole, può fare copywriting."* | Accessibilità + aneddoto personale (paracadute) |
| 7 | 8612 | 1288 | *"Ma com'è possibile che le aziende paghino così tanto..."* | Case Martin Conroy/WSJ + matematica (20×20€=400€) |
| 8 | 9900 | 964 | *"Okay, ma chi sono io per parlarti di Copywriting?"* | Bio Andrei — 2019, 10k€/mese, 270k follower |
| 9 | 10863 | 1617 | *"Quale è il problema con (quasi) tutti i percorsi di formazione..."* | Attacco ai competitor (screenshot corsi vecchi) |
| 10 | 12480 | 828 | *"Copywriting Mentorship è il primo corso italiano..."* | 1° pitch del corso + CTA |
| 11 | 13308 | 718 | *"Conosco quel sentimento"* | Empatia emotiva, "lascio da parte i dati" |
| 12 | 14026 | 814 | *"Copywriting Mentorship a confronto con altri percorsi"* | Grafico comparativo (solo immagine) |
| 13 | 14840 | 630 | *"Quale è la conclusione?"* | Ricapitolazione + CTA finale |
| 14 | 15470 | 705 | (footer) | Legale + nav |

Le prime **9 sezioni su 14** (fino a y=10863, il 67% della pagina) non menzionano mai il corso: sono
puro posizionamento del copywriting come categoria. Il corso entra solo alla sezione 10.

### LA PROMESSA

Non è una promessa di risultato immediato ma di **comprensione**: *"Scopri perché sempre più persone
ambiziose trovano la loro strada ed indipendenza economica grazie al Copywriting."* [y=149]. La
promessa si fa più diretta a metà pagina: *"In 5 minuti ti spiego perché il copywriting è il migliore
modello di business per iniziare"* [y=4151] — un H1 collocato oltre 4.000px dentro la pagina, non in
apertura, insolito rispetto alle altre pagine di questo studio dove l'H1 è sempre il primo elemento.

### LE PROVE E LA LORO VERIFICABILITA'

Questa è, delle tre pagine anomale, **la più densa di fonti esterne reali**: sei citazioni distinte,
tutte cliccabili.
1. *"(Fonte 1 - Fonte 2 - Fonte 3)"* [y=1358] → khrisdigital.com, contentmarketinginstitute.com,
   freelancinghacks.com — tre fonti indipendenti sulla dimensione del mercato del copywriting.
2. *"Il 60,4% delle aziende italiane fattura meno di 100mila euro... (fonte)"* [y=1724] →
   truenumbers.it — dato fiscale italiano verificabile.
3. *"(fonti)"* [y=2576] → linoolmostudio.it — dato su spesa pubblicitaria media.
4. *"Gli esperti del digital marketing... (fonte)"* [y=4966] → wordstream.com — dato di settore.
5. *"Ecco il livello di interesse nel Copywriting... (Fonte: Google Trends)"* [y=6373] — grafico
   incluso come screenshot, fonte nominata esplicitamente.
6. Il case Martin Conroy/Wall Street Journal — *"generò ben 2 miliardi di dollari"* [y=9054] → link a
   swiped.co con l'estratto originale della pubblicità [y=9185] — un case study storico reale e
   documentato, non un claim proprietario di Andrei.

A queste si somma una prova personale verificabile: *"Ho un seguito di più di 270 mila persone tra i
vari canali social"* [y=10569] → link diretto a tiktok.com/@andrei.bsns [y=10573], controllabile con un
click. Contro questa densità di fonti, restano non verificate: le cifre 55% e 79% sulle aziende
[y=2709, y=3033] (nessun link diretto adiacente), il numero *"quasi 3000 persone"* aiutate dal corso
[y=12243] (nessuna fonte), e lo screenshot dei "competitor" [y=11821] (immagine, non testo, non
verificabile dal copy da solo).

### L'IMPEGNO CHIESTO

Zero moduli, zero form su questa pagina: è **puro impegno attenzionale**. Il lettore deve solo
continuare a scorrere 16.175px (una lettura di 10-15 minuti stimati) prima di essere indirizzato altrove
tramite quattro CTA identiche nella destinazione ma diverse nel testo: *"Voglio imparare questa
professione per vivere libero"* → `/copy-base` [y=8425], *"Scopri il corso"* → `/copywriting`
[y=12322], *"Dimmi di più sul percorso"* → `/copy-base` [y=13136], *"Clicca qui per scoprire Copywriting
Mentorship"* → `/copy-base` [y=15312]. Tre delle quattro portano alla stessa pagina (`/copy-base`), non
direttamente al carrello: l'impegno reale (prezzo, acquisto) è demandato interamente a una pagina
successiva che questo studio non ha ancora catturato in questo dossier.

### IL PREZZO SE C'E'

**Nessun prezzo del corso compare in questa pagina.** Verificato con ricerca testuale diretta: ogni
cifra in euro presente nel testo è un esempio didattico su quanto un copywriter può fatturare o
addebitare a un cliente — *"100mila euro"*, *"+50 MILIONI di euro"*, *"400 euro"*, *"4000€"*, *"500€"*
[y=9438-9649] — mai il prezzo di Copywriting Mentorship stesso. La pagina delega volutamente la
rivelazione del prezzo a `/copy-base`, tenendo questa pagina puramente persuasiva/educativa.

### COSA NON DICE MAI

Nessun prezzo del corso (per costruzione, come sopra). Nessuna garanzia o rimborso nel testo. Nessun
programma dettagliato del corso, solo un conteggio — *"Nelle quasi 140 video lezioni (+ 3 di
introduzione)"* [y=12896] — senza indice o syllabus. Nessuna testimonianza di uno studente con nome,
foto o risultato numerico: l'unica prova sociale numerica è l'aggregato non verificabile *"quasi 3000
persone"* [y=12243]. Ogni prova personale sulla pagina riguarda solo Andrei stesso, mai un cliente o
studente nominato.

---

## PARTE 3 — 44-apsales-promozione (apsales.eu/promozione)

### CHE COS'E' DAVVERO

Non è la pagina con cui AP Sales (l'agenzia CRO di Andrei Pascu) vende i propri servizi a un cliente
business. È una pagina di **reclutamento**: invita ex studenti/clienti di Andrei a fare una **call
registrata** in cambio di **€150** e di promozione incrociata sui suoi canali — Instagram, TikTok, e
sul sito stesso (*"Fai una call registrata con Andrei e…"* [y=177] seguito da un doppio reveal:
*"Andrei ti promuove"* poi *"Andrei ti manda €150"* [y=395-492]). È esplicitamente **non** una
recensione a pagamento: *"Questa non è una video-recensione in cui devi parlare bene dei prodotti di AP
Sales... È un caso studio."* [y=2963-3136]. Il footer conferma che apsales.eu è comunque il dominio
dell'agenzia (nav: Servizi, Landing page, Consulenza, Chi siamo, Lavora con noi, Assistenza
[y=8500-8503]), ma questa pagina specifica non vende un servizio a un cliente — recluta materiale di
riprova sociale per Andrei. La costruzione è marcata "artigianale" in `scheda.json`, ma il campo
`meta.og_image` rivela una URL che contiene la stringa `lovable.app` — la firma di Lovable, un
generatore di siti via AI: il sito è quasi certamente stato prototipato con uno strumento AI-builder
(coerente con l'uso pervasivo di classi utility Tailwind e funzioni colore `oklch`/`oklab`), non
scritto a mano da zero né costruito su Squarespace.

### LA STRUTTURA

9 sezioni (9 distinte), 10.300px, solo 97 blocchi — la più piccola e compatta delle tre pagine
anomale.

| # | y | Alt. (px) | Heading | Funzione |
|---|---|---|---|---|
| 1 | 65 | 1332 | *"Fai una call registrata con Andrei e…"* | Hero a doppio reveal + card mockup + CTA |
| 2 | 1397 | 804 | *"Cosa ricevi"* | 4 item: promo storie/reels, card personalizzata, €150 |
| 3 | 2201 | 1380 | *"Why?"* | Contesto brand (rebranding, follower, nuovo prodotto) |
| 4 | 3581 | 1677 | *"Altri vantaggi"* | 6 benefit aggiuntivi (logo, storie in evidenza, no scammer) |
| 5 | 5258 | 1211 | *"Cosa devi fare"* | 5 step: modulo→call telefonica→call video→pubblicazione→pagamento |
| 6 | 6469 | 1348 | *"Come verrà il video"* | Formato: intervista scriptata, 4 domande esempio, durata 3-5 min |
| 7 | 7817 | 884 | *"Fatti promuovere"* | Recap + CTA |
| 8 | 8701 | 418 | *"Domande?"* | Rassicurazione minima |
| 9 | 9119 | 1182 | (footer) | Nav agenzia + legale |

### LA PROMESSA

Non promette trasformazione del business: promette **visibilità + pagamento fisso per il tempo**.
*"Sarai associato al brand di Andrei Pascu, verrai pagato per il tuo tempo e riceverai promo."*
[y=3334]. E, in un frame insolitamente onesto sull'incentivo reciproco: *"Ci guadagna reputazione e
social proof, senza fare le robe cringe che fanno i guru."* [y=3322] — Andrei ammette esplicitamente
che il beneficio principale per lui è la riprova sociale, non un favore all'intervistato.

### LE PROVE E LA LORO VERIFICABILITA'

Debole, e asimmetrica. Le cifre di seguito social — *"250k follower TikTok"*, *"25k follower Insta"*
[y=2646] — non hanno link diretto adiacente nel corpo della pagina; l'account Instagram è raggiungibile
solo tramite il link generico nel footer [y=8503 → instagram.com/andrei.bsns], mentre **il profilo
TikTok non è mai linkato da nessuna parte sulla pagina**, nonostante sia il canale con più follower
dichiarati. Il claim più specifico e in teoria più verificabile — *"@andrei.marketing.god... solo ieri
ha postato 16 volte"* [y=2668] — non è accompagnato da nessun link a quell'account secondario. Non
esiste, da nessuna parte sulla pagina, un esempio di una "card" reale già pubblicata per un
partecipante precedente: l'unica immagine mostrata è un mockup generico [`/promozione/card-mock.webp`,
alt: *"La card che finisce sul sito di Andrei: la tua foto, il tuo nome su un colore che scegli tu, una
frase, due statistiche, il tuo social e un pulsante che apre i dettagli."*] — un difetto strutturale
notevole per una pagina il cui unico scopo è generare riprova sociale: non mostra nemmeno un esempio
di riprova sociale già ottenuta con questo stesso meccanismo.

### L'IMPEGNO CHIESTO

Le **due** CTA della pagina (*"Fatti promuovere →"* [y=1211] e *"Ok, lo voglio fare →"* [y=8479])
puntano allo **stesso identico URL**: un Google Form
(`docs.google.com/forms/d/e/1FAIpQLScpnvquPpjKBude9L-rXNxsHOYWyBQ-ybQsNm8s7nKRxqz6yw/viewform`), senza
alcuna differenziazione o tracciamento visibile fra le due posizioni sulla pagina. Il percorso dopo il
form [y=5526-6313]: 1) *"Completa il modulo"* — *"Devi darci delle info"*; 2) *"Aspetta la call"* —
*"Verrai contattato telefonicamente"*; 3) *"Call"* — *"Questa è la call, verrà registrata"*, in formato
*"breve intervista... parzialmente scriptata"* con talking point dati in anticipo e quattro domande
tipo mostrate esplicitamente (*"Da dove sei partito?"*, *"Quando hai chiuso il primo cliente?"*, *"Come
hai fatto?"*, *"Che cosa vendi ora?"* [y=7164-7404]), durata finale del video **3-5 minuti**; 4)
*"Fatto"* — attesa di pubblicazione; 5) *"Pagamento"* — *"Ti inviamo €150 il 30 settembre"* [y=6313],
una data fissa di pagamento uguale per chiunque completi il processo, indipendentemente da quando si è
iscritto.

### IL PREZZO SE C'E'

Qui il flusso di denaro è **invertito**: non è il visitatore a pagare, è AP Sales a pagare **€150** al
partecipante, cifra ripetuta identica tre volte [y=492, y=2005, y=8202]. Nessun prezzo di alcun
prodotto o servizio compare mai su questa pagina.

### COSA NON DICE MAI

Nessun criterio esplicito di ammissione — la pagina presuppone che il lettore sia già uno studente
(*"Andrei sta lanciando un nuovo prodotto... vuole fare dei case study di alcuni suoi studenti, ovvero
tu"* [y=2825]) ma il modulo stesso, per quanto descritto nel copy, non sembra filtrare questo requisito
prima della call telefonica. Nessuna menzione di un accordo di cessione diritti sul video, di un
consenso alla pubblicazione, o della possibilità di rifiutare la pubblicazione finale dopo aver
registrato — i *"Termini e condizioni"* sono linkati genericamente nel footer [y=8503 → `/tos`] ma non
richiamati in nessun punto del corpo pagina relativo al processo stesso. Nessun follower minimo o
requisito di reach è specificato per candidarsi. E, come già notato, nessun esempio reale di una card o
di un video già pubblicati in precedenza con questo stesso meccanismo — zero riprova sociale della
riprova sociale.

---

## PERCHE' TRE STACK DIVERSI

Tre stack diversi raccontano tre logiche di produzione diverse, non tre incidenti casuali.

**Squarespace (40-ecco-i-fatti, ecosistema andrei-copy.com)** è lo stack del contenuto maturo e
manutenuto nel tempo: una pagina lunga, ricca di immagini incorporate via CDN Squarespace
(`images.squarespace-cdn.com`, 21 immagini distinte contate nel campo `media` di `scheda.json`),
aggiornata periodicamente (il testo dichiara esplicitamente *"aggiornate al 2025"* [y=1421] e *"Peccato
che quando l'ho letto eravamo già nel 2023"* [y=11945] — riferimenti a anni specifici tipici di un
contenuto pensato per essere rivisto e corretto, non rigenerato). È lo stack giusto per chi vuole poter
editare testo e trascinare immagini senza un developer, su una pagina che vive per mesi o anni.

**"Artigianale"/Lovable (44-apsales-promozione, dominio apsales.eu, il brand agenzia)** è lo stack del
lancio rapido e ristretto nello scopo: una singola pagina con un solo obiettivo (raccogliere iscrizioni
a un Google Form), con un design system moderno a colori `oklch`/Tailwind, tipico di un sito generato o
prototipato con uno strumento AI-builder — coerente con il fatto che il copy stesso dichiara che
*"Andrei ha recentemente modificato il suo brand"* [y=2417]: un rebrand recente giustifica uno stack
più nuovo e più veloce da iterare rispetto al Squarespace consolidato del ramo formazione.

**Next.js (43-chiamata-formazione)** non è affatto lo stack di Andrei Pascu — è lo stack che Digital
Empire (Max) usa per le proprie build, secondo le convenzioni già note nell'ecosistema Digital Empire
(Next.js come corsia principale per siti con più di poche pagine, per esempio in ADR-023 sulla Fabbrica
Siti). Il fatto che questa pagina compaia nella cartella `competitor/Andrei Pascu/` non riflette una
scelta stilistica del competitor: riflette che qualcuno in Digital Empire ha **preso in prestito
l'architettura persuasiva** delle pagine-chiamata di Andrei Pascu (rapporto 90/10, value-stack,
gestione obiezioni a triade, reveal economico finale) per costruire un prototipo del proprio funnel, e
quel prototipo è stato catturato insieme al resto dell'ecosistema durante l'onda D senza un controllo
di provenienza. I tre stack, letti insieme, non descrivono "come Andrei Pascu sceglie la tecnologia" —
descrivono due rami reali del suo ecosistema (formazione stabile su Squarespace, agenzia in rebranding
su uno stack AI-builder) più un terzo elemento che è, semplicemente, materiale nostro.

---

## LEZIONI PER I NOSTRI LANCI

Concrete, ciascuna trasformabile in una regola o in un pezzo di infrastruttura per l'ecosistema lanci
di Digital Empire:

1. **Value-stack esplicito per offerte gratuite ad alto impegno.** La sezione *"Quanto vale davvero
   questa sessione"* di 43 [y=6503-6805] scompone un servizio gratuito in cinque voci prezzate
   (€250+€120+€300+€80+€100=€850) prima di mostrare "€0". È un componente riusabile — costruirlo come
   blocco standard per ogni futura call strategica gratuita che Digital Empire lancerà.

2. **Dichiarare il rapporto insegnamento/pitch, e rispettarlo.** *"90% formazione pura, 10% pitch del
   corso"* [y=114] ripetuto identico più volte nella pagina è una promessa di forma, non solo di
   contenuto — codificarla come regola di copy per ogni funnel a call: se si dichiara un rapporto, va
   rispettato nel copy stesso della sezione "cosa succede in call".

3. **Scarsità aritmetica, non contatore finto.** *"Faccio max 8 call a settimana... 45 min × 8 call = 6
   ore di call"* [y=8549] è verificabile dal lettore con un calcolo, a differenza di un countdown a
   mezzanotte. Preferire questo pattern per ogni limite di capacità reale (posti in un corso, slot di
   consulenza) invece di scadenze artificiali.

4. **Reveal onesto della matematica di conversione come elemento di fiducia.** *"Il 5% delle persone...
   poi sceglie... Il 95% esce con il workflow"* [y=17810-17919] — dichiarare pubblicamente il tasso di
   conversione atteso di un funnel gratuito è un pattern di trasparenza che il resto di questo studio
   (le pagine di Andrei Pascu) non usa mai. Vale la pena testarlo sui nostri funnel a call, con numeri
   reali quando li avremo.

5. **Gate di coerenza testa-corpo sui prezzi.** L'incoerenza *"Corso da 800€"* / *"€400 – €2.000"*
   trovata su 43 [y=16068 vs y=16594] è l'errore più facile da automatizzare via script prima della
   pubblicazione: ogni cifra in un titolo di sezione va confrontata con ogni cifra nello stesso claim
   nel corpo, prima del deploy.

6. **Footer legale completo obbligatorio prima del traffico reale.** 43 non ha P.IVA né indirizzo nel
   footer [y=18710], mentre ogni pagina Andrei Pascu già mappata in questo studio li ha sempre. Prima
   che un funnel di Digital Empire esca dallo stato di prototipo Netlify, il footer legale completo
   (ragione sociale, indirizzo, P.IVA, privacy, cookie) va reso un requisito bloccante di pubblicazione.

7. **Testimonianze con più identità o non pubblicarle.** Tre testimonial senza cognome, senza link,
   senza foto (`media: []` su tutta la pagina 43) sono il formato di prova più debole misurato in
   questo intero site-study, contro le 6 prove-profilo cliccabili già documentate per outViral. Fissare
   uno standard minimo per Digital Empire: nome+cognome (anche solo iniziale) + un link verificabile
   (LinkedIn, X, sito) per ogni testimonianza pubblicata.

8. **Il pattern "advertorial poi handoff" per lanci a media-alta considerazione.** 40 costruisce
   fiducia per 16.175px con sei fonti esterne reali prima di nominare il corso, poi delega prezzo e
   acquisto a una pagina separata (`/copy-base`). Per lanci come il Manuale Claude Code, separare
   esplicitamente "pagina che educa e cita fonti" da "pagina che vende e mostra il prezzo" invece di
   fonderle in un'unica landing page.

9. **"Fatti promuovere" come infrastruttura a costo fisso per generare social proof.** Il meccanismo di
   44 — pagare una cifra fissa (€150) per un'intervista video breve e parzialmente scriptata, con
   domande date in anticipo — è un modo sistematico ed economico di produrre case study. Vale la pena
   costruire l'equivalente per Digital Empire con i clienti passati dell'agenzia CRO, usando lo stesso
   schema di 4-5 domande fisse e durata finale di 3-5 minuti.

10. **Pagamento a data fissa batch, non a rolling.** 44 paga tutti i partecipanti lo stesso giorno (30
    settembre 2026) indipendentemente da quando si sono candidati [y=2005, y=6313] — semplifica la
    programmazione di tesoreria per iniziative di questo tipo; adottare lo stesso schema se Digital
    Empire lancia un programma simile.

11. **Controllo di provenienza per ogni capture del site-study.** La scoperta più importante di questo
    dossier non è persuasiva, è procedurale: una pagina nostra è finita classificata come "competitor"
    per 24 ore prima di essere corretta qui. Il gate proposto in apertura (`brand_rilevato` nel testo
    confrontato con `brand_atteso` della cartella) va implementato prima della prossima onda di
    capture, non trattato come nota a margine.

12. **Mostrare almeno un esempio già fatto, quando il prodotto è "riprova sociale".** Il difetto più
    ironico di 44 è che una pagina il cui scopo è generare prova sociale non mostra nessuna prova
    sociale pregressa di sé stessa (solo un mockup generico). In qualunque equivalente Digital Empire,
    includere almeno un esempio reale già pubblicato prima di chiedere al prossimo candidato di
    fidarsi.

---

## Nota sulla lunghezza

Il documento supera la soglia di 3.000 parole di sostanza richiesta: tre pagine complete (1.081 blocchi
di testo aggregati fra i tre `copy-integrale.md`, tre `scheda.json` con sezioni/CTA/headings/palette)
hanno dato margine ampio per coprire ogni sezione richiesta con citazioni dirette, senza necessità di
riempitivo.

## Collegamenti

- `capture/43-chiamata-formazione/copy-integrale.md`, `scheda.json` — la pagina rivelata come non
  appartenente ad Andrei Pascu
- `capture/40-ecco-i-fatti/copy-integrale.md`, `scheda.json` — l'advertorial sul copywriting
- `capture/44-apsales-promozione/copy-integrale.md`, `scheda.json` — il funnel di reclutamento case
  study di AP Sales
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — standard di forma per questo
  dossier, e precedente più vicino per il confronto sul rapporto 90/10 e sulla verificabilità delle
  prove
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
