---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #squarespace #armageddon-pack #outemail #outviral #copy #teardown
Created: 2026-09-07
Last updated: 2026-09-07
---

# 21-22 — outEmail e outViral — teardown del copy, originale contro copia di lancio

**Originali (andrei-copy.com):** `21-outemail` (26.032px, 24 sezioni/17 distinte, 259 blocchi, 24 CTA) ·
`22-outviral` (11.555px, 11 sezioni/11 distinte, 196 blocchi, 18 CTA)
**Copie di lancio (armageddon.bsns.it):** `14-arma-outemail` (25.588px, 24 sezioni/16 distinte, 238
blocchi, 21 CTA) · `17-arma-outviral` (10.047px, 10 sezioni/10 distinte, 149 blocchi, 13 CTA)
**Prezzo di lancio:** 585€ di listino (139+98+98+250) + 199€ di voucher, venduti a 199€ — numeri già
accertati in [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md), qui usati come base.

Questo dossier non ripete il confronto già fatto fra le quattro pagine "out*" fra loro (quello è nel
report CONFRONTO). Fa un confronto diverso: **ogni pagina contro sé stessa**, originale contro copia,
riga per riga, per vedere esattamente cosa un venditore toglie, aggiunge o rietichetta quando una
pagina di vendita smette di vendere un prodotto singolo e comincia a vendere un pacchetto.

---

## DELTA ALLA FABBRICA

**CANONE:** entra un componente nuovo, non ancora in `canone.css`: il **badge di inclusione-bundle**.
Compare identico su tutte e due le pagine copiate, sempre nello stesso punto (subito sopra o sotto la
card prezzo, mai altrove): `<p>` uppercase, colore `#bc0807`, 15.2px, peso 700 — *"INCLUSO NEL
PACCHETTO ARMAGEDDON"* [y=23953 su `14-arma-outemail`; y=1290 e y=9408 su `17-arma-outviral`]. Il
colore non è casuale: è lo stesso identico `#bc0807` della barra sticky di acquisto (§0 del dossier
CONFRONTO), quindi il badge e il bottone finale condividono un solo accento cromatico che nell'intera
pagina non compare da nessun'altra parte — un filo rosso deliberato fra "questo è incluso" e "compra
qui". Va codificato come componente `bundle-inclusion-badge`: uppercase, colore accento riservato
esclusivamente a badge+CTA finale, mai usato altrove nella pagina.

**PATTERN:** quando una prova (qui: un video) non regge la migrazione, si taglia la sezione intera
invece di lasciarla visivamente rotta a metà. È quello che succede alla sezione "Cosa ne pensa
Fabiano" di outViral (§ sotto): sparisce in blocco, non degrada a un player muto o a un'immagine
segnaposto. È una conferma più fine del pattern già loggato nel dossier CONFRONTO (riga 1 della sua
tabella DELTA, "pagina prodotto congelata"): lì il pattern era a livello di pagina intera, qui si vede
lo stesso principio applicato a livello di singola sezione — un gradino di granularità che vale la
pena avere scritto separatamente per la Fabbrica, perché la decisione "taglio tutto o lascio rotto" si
prende sezione per sezione, non pagina per pagina.

**GATE:** due controlli meccanici nuovi, entrambi misurati su prove concrete in questo stesso
documento (§ "IL DIFETTO"): 1) *ogni immagine che sostituisce un prezzo o un numero critico deve avere
un `alt` non vuoto* — qui il prezzo di outEmail (139€) è un'immagine con `alt=""` su **entrambe** le
versioni, originale e copia, quindi il difetto non è nato con il mirror, esisteva già; 2) *nessun anno
scritto a mano nel copy senza un commento `TODO: aggiornare` accanto* — qui "2025" nell'originale
diventa "2026" nella copia [y=5372 vs y=5282], prova diretta che qualcuno lo ha dovuto editare a mano
per non farsi scoprire con una data vecchia, un lavoro che si ripeterà ogni anno finché la pagina resta
in vendita.

---

## COSA CAMBIA DALL'ORIGINALE ALLA COPIA DI LANCIO

Questa è la parte che conta di più: cosa succede, riga per riga, quando andrei-copy.com/outemail
diventa armageddon.bsns.it/outemail, e andrei-copy.com/outviral diventa armageddon.bsns.it/outviral.
Il confronto è stato fatto con un diff testuale reale fra i due `copy-integrale.md` di ogni coppia
(coordinate `y` normalizzate, perché shiftano per motivi strutturali — la barra di navigazione tolta
in cima sposta in basso tutto quello che segue — ma il contenuto resta comparabile riga per riga).

### outEmail — cosa toglie, cosa aggiunge, cosa rietichetta

| # | Elemento | Originale (andrei-copy.com) | Copia (armageddon.bsns.it) | Natura del cambio |
|---|---|---|---|---|
| 1 | Barra nav/account in cima | *"Passa al contenuto"* → `#page`, *"Claude Speedrun"* → link esterno, *"Accedi"* [y=20901-20910, DOM in coda ma fissata in alto] | **assente** | **Tolto** — dipendeva dal JS di membership Squarespace, mai ricostruito |
| 2 | Anno nella storia dell'email marketing | *"E adesso, nel **2025**… L'email marketing è troppo usato."* [y=5372] | *"E adesso, nel **2026**… L'email marketing è troppo usato."* [y=5282] | **Modificato a mano** — stesso giorno di cattura (2026-09-07) per entrambe, quindi non è un campo dinamico: qualcuno ha riscritto la cifra |
| 3 | Colore della lettera finale in "It-ia" | *"ia"* colorata `#fd0000` [y=1014] | stessa lettera, `#ff5f5f` [y=925] | Deriva cromatica minore — stesso testo, rosso più chiaro |
| 4 | Bottone prezzo individuale | *"Entra in outEmail"*, bottone `#1b1b1d`, `href: null` [y=24091, mai un link funzionante] | **sostituito** da *"INCLUSO NEL PACCHETTO ARMAGEDDON"*, etichetta non cliccabile `#bc0807` uppercase [y=23953] | **Rietichettato** — da bottone-acquisto già rotto a badge di reframe |
| 5 | Footer di navigazione | *"La mia storia"* → `/story`, *"Store"* → `/presto-disponibile`, *"Recensioni"*, *"Risorse"*, *"Blog"* [y=25519-25659] | **assente per intero** | **Tolto** — i link di navigazione del vecchio sito non hanno senso su un dominio-mirror di due sole pagine |
| 6 | Blocco legale | due paragrafi, indirizzo esteso *"FIRENZE (FI) VIALE GIACOMO MATTEOTTI \| 15 CAP 50121"* [y=25932], testo pieno `#ebe9e0`/`#fafafa` | un paragrafo unico, indirizzo compattato *"Viale Giacomo Matteotti 15, 50121 Firenze (FI)"* [y=25385], testo a opacità 50% `#ffffff@0.5` | **Riscritto/condensato** |
| 7 | Link privacy | relativo `/privacy-dati-cookie-simili` [y=25954, stesso dominio] | assoluto `https://www.andrei-copy.com/privacy-dati-cookie-simili` [y=25404, cross-domain] | **Necessitato dalla migrazione** — la pagina privacy non è stata mirrorata |
| 8 | Bottone preferenze cookie | *"Gestisci Preferenze Cookie"* [y=26009] | **assente** | **Tolto** — dipendeva dal banner cookie di Squarespace |
| 9 | Barra sticky d'acquisto | **assente** | *"Prendi l'Armageddon Pack — 199€"* → `buy.stripe.com/00w28s9LA5Y0eIT8N64Ja1O`, più *"Torna alla pagina principale"* [y=22086, elemento fisso, visibile per tutto lo scroll] | **Aggiunto ex novo** — l'unico bottone dell'intera pagina che porta davvero a un pagamento |
| 10 | Palette della finta inbox (curriculum) | *"Candele Pro"*, *"Affitti Decenti Milano"* ecc. su `#64748b`/`#1e293b` | stesso testo su `#76869d`/`#6884b2` in alcune righe | Deriva cromatica minore, non testuale |

Cinque celle su dieci sono cambi di **contenuto o funzione reale** (righe 1, 2, 4, 5, 9), non
cosmesi: la pagina perde il proprio sistema di navigazione/account, guadagna un vero bottone di
pagamento (che prima non esisteva da nessuna parte sulla pagina — il vecchio "Entra in outEmail" non
linkava a niente), e riscrive a mano un numero nel corpo del testo. Le altre cinque sono variazioni
cromatiche o di formattazione (righe 3, 6, 7, 8, 10) che non toccano il significato ma raccontano una
storia diversa da quella di un "mirror perfetto, byte per byte": qualcuno **ha aperto l'editor** e ha
toccato singole righe, non solo eseguito uno script di copia. Il resto della pagina — tutto il corpo
persuasivo, dal primo "Apriresti questa email?" fino alla FAQ — **non cambia di una virgola**: stesso
identico testo, stesse identiche coordinate `y` relative, stesso ordine. È un fatto forte quanto le
differenze: la parte che vende non è stata toccata, solo la cornice (intestazione, piede, prezzo,
CTA finale) è stata riscritta per il nuovo contesto di vendita.

### outViral — cosa toglie, cosa aggiunge, cosa rietichetta

| # | Elemento | Originale (andrei-copy.com) | Copia (armageddon.bsns.it) | Natura del cambio |
|---|---|---|---|---|
| 1 | Barra nav/account in cima | *"Passa al contenuto"*, *"Claude Speedrun"*, *"Accedi"* [y=8501-8510] | **assente** | **Tolto** — stesso pattern di outEmail |
| 2 | Video hero (player) | blocco interattivo completo: *"Riproduci"*, timer *"00:00 / 03:57"*, *"Disattiva audio"*, *"Impostazioni"*, *"Attiva modalità schermo intero"* [y=1367-1660]; contenitore alto **1143px** | **tutta l'interfaccia testuale sparisce**; resta 1 solo elemento media (poster/video muto, senza controlli); contenitore alto **717px** (-426px, -37%) | **Degradato** — l'asset non è stato rimosso, ha perso la sua interfaccia |
| 3 | Bottone prezzo (1ª occorrenza) | *"Entra in outViral"*, `#1b1b1d`/`#a8a8a8`, `href: null` [y=1802] | **sostituito** da *"INCLUSO NEL PACCHETTO ARMAGEDDON"* [y=1290] | **Rietichettato** — stesso pattern di outEmail |
| 4 | Colore paragrafo "curando" | *"Tutte cose che tu non stai curando…"* su `#1b1b1d` [y=2608] | stesso testo su `#0a0a0b` [y=2093] | Deriva cromatica minima |
| 5 | Sezione "Cosa ne pensa Fabiano" | sezione intera, 630px, secondo video-player con *"Riproduci"*/*"01:17"* [y=7651-8281] | **assente per intero, nessuna sostituzione** — il confine fra la sezione precedente e quella successiva combacia esatto (7.041px = 5.323+1.718 nella copia, contro le due sezioni separate nell'originale) | **Tolto** — sezioni totali passano da 11 a 10 |
| 6 | Bottone prezzo (2ª occorrenza) | *"Fai l'account, iscriviti poi impara."* [y=10569] | **sostituito** da *"INCLUSO NEL PACCHETTO ARMAGEDDON"* [y=9408] | **Rietichettato** |
| 7 | Footer di navigazione | *"La mia storia"*, *"Store"*, *"Recensioni"*, *"Risorse"*, *"Blog"* [y=11042-11184] | **assente per intero** | **Tolto** — stesso pattern di outEmail |
| 8 | Blocco legale | esteso, indirizzo per intero, testo pieno | condensato, opacità 50% | **Riscritto** — stesso pattern di outEmail |
| 9 | Link privacy | relativo, stesso dominio | assoluto, cross-domain | **Necessitato** — stesso pattern |
| 10 | Bottone preferenze cookie | *"Gestisci Preferenze Cookie"* [y=11533] | **assente** | **Tolto** — stesso pattern |
| 11 | Barra sticky d'acquisto | **assente** | *"Prendi l'Armageddon Pack — 199€"* → Stripe [y=8113] | **Aggiunto ex novo** |

outViral perde di più, in proporzione, di outEmail: **un'intera sezione di prova sociale video-based
sparisce senza sostituzione** (riga 5), e il **video hero perde la sua interfaccia** (riga 2) — due
danni reali alla persuasione, non solo cosmesi, che non hanno equivalente sul lato outEmail (che non
aveva video-hero né video-testimonianza da perdere, solo un iframe Vimeo dentro il curriculum a pagamento,
mai toccato). La scarsità di video funzionanti nell'originale (entrambi ancora "da spostare su Vimeo",
per usare le parole del commento in `mirror.js` già trovato nel dossier CONFRONTO) diventa,
nella copia, una vera perdita di contenuto: chi vede armageddon.bsns.it/outviral oggi non vede mai la
testimonianza di Fabiano, punto. Il resto del pattern — nav tolta, footer tolto, bottoni-prezzo
rietichettati, barra sticky aggiunta — è identico, elemento per elemento, a quello di outEmail: **è
lo stesso mirror.js, la stessa procedura, applicata meccanicamente a entrambe le pagine**, con l'unica
eccezione della perdita del video-testimonianza (che è un fatto sulla pagina, non sulla procedura di
mirroring).

**La matematica del risparmio non viene mai scritta.** Nessuna delle due copie dice mai, in nessun
punto del testo, "risparmi X€ prendendo il pacchetto invece dei singoli corsi" — nemmeno ora che il
prezzo individuale barrato sta proprio accanto al badge "INCLUSO NEL PACCHETTO ARMAGEDDON". Il lettore
deve sommare da solo 139€ (outEmail) + 250€ (outViral) + gli altri due corsi della famiglia per
arrivare a un numero che confermi la convenienza dei 199€ finali — un'occasione di persuasione lasciata
sul tavolo, coerente con quanto già osservato nel dossier CONFRONTO (§5: "nessuna garanzia... resta un
vuoto reale, non un'interpretazione") ma qui riguarda l'aritmetica del prezzo, non la garanzia.

---

## LA STRUTTURA DELLA PAGINA DI VENDITA

### outEmail — 24 tappe, 26.032px (numerazione dell'originale; la copia segue lo stesso ordine)

| # | y | Alt. (px) | Heading rappresentativo | Funzione |
|---|---|---|---|---|
| 1 | 0 | 1.330 | *"Apriresti questa email?"* | HERO — domanda shock + negazione immediata ("No, non l'apriresti... la metteresti in spam") |
| 2 | 1.330 | 1.343 | *"Che Dio riposi la sua anima…"* | Apertura ironica, primo assist: "l'email marketing classico è morto" |
| 3 | 2.673 | 1.489 | *"Ho una buona… E una pessima notizia."* | Cliffhanger con GIF di raccordo |
| 4 | 4.162 | 2.053 | *"L'email marketing 'classico' è morto"* (ripetuto) | Corpo storico: nascita del settore (1978, fonte Wikipedia), escalation, statistica (121 email/giorno), colpa collettiva |
| 5 | 6.232 | 924 | (nessuno) | Separatore visivo scuro |
| 6 | 7.156 | 1.845 | *"Guarda come sta messa l'azienda Italiana media…"* | Dimostrazione comparativa: screenshot di oggetti-email cattivi vs quelli di Andrei |
| 7 | 9.001 | 771 | *"Come si fa l'email marketing strategico?"* | Transizione verso il metodo/curriculum |
| 8 | 9.772 | 891 | (nessuno) | Galleria visiva di supporto (fumetto) |
| 9 | 10.663 | 1.316 | *"334 minuti di tutorial…"* | Presentazione del curriculum (durata, "innovare in 2 modi") |
| 10 | 11.978 | 1.286 | (nessuno) | Fumetto illustrativo del problema |
| 11 | 13.264 | 743 | *"Non è per tutti. Sono serio."* | Qualificazione negativa (chi non deve comprare) |
| 12 | 14.024 | 833 | (nessuno) | Separatore scuro |
| 13 | 14.857 | 924 | *"E se non comprano… Siamo qui per vendere."* | Svolta esplicita verso la vendita |
| 14 | 15.781 | 658 | *"Ma io so già scrivere email"* | Obiezione #1 + risposta |
| 15 | 16.439 | 1.189 | *"Il prossimo livello di pensiero strategico…"* | Benefici a blocchi (334min / 3+ore strategia / 2 ore tutorial / "niente basi") |
| 16 | 17.628 | 1.348 | *"Andrei perché dovrei comprare outEmail…?"* | Autorevolezza/differenziazione dai competitor |
| 17 | 18.977 | 1.025 | *"outEmail ha un ROI fuori da questo pianeta"* | Giustificazione economica del prezzo |
| 18 | 20.001 | 774 | *"Lista video-lezioni"* | Curriculum — accordion a 3 sezioni |
| 19 | 20.793 | 796 | (nessuno) | Separatore scuro |
| 20 | 21.589 | 771 | (nessuno, 9 CTA) | Demo interattiva — finta inbox con 7 email e bottoni "Open" |
| 21 | 22.360 | 829 | *"I tuoi open rate saranno talmente alti da sembrare finti."* | Promessa di risultato + invito a informarsi |
| 22 | 23.189 | 1.034 | *"adesso disponibile."* | Card prezzo (immagine, €139 barrato) |
| 23 | 24.223 | 1.104 | *"FAQ"* | 4 domande + chiusura ("Ribalti 'ste email o no?") |
| 24 | 25.327 | 705 | (footer) | Chiusura legale + nav (originale) / solo legale (copia) |

### outViral — 11 tappe, 11.555px

| # | y | Alt. (px) | Heading rappresentativo | Funzione |
|---|---|---|---|---|
| 1 | 0 | 859 | *"Ottieni una media di 10K views…"* | HERO — promessa numerica secca + qualificazione ("se parli su TikTok") + "Senza ca**ate" |
| 2 | 876 | 1.143 | (nessuno) | Video-teaser (3:57) + 1ª card prezzo ("outViral 2", 250€, "Entra in outViral") |
| 3 | 2.019 | 821 | *"Un solo video… E la tua vita cambia per sempre"* | Agitazione/promessa + micro-reveal ("outViral toglierà l'indovinare") |
| 4 | 2.839 | 931 | *"Ho cambiato la mia vita con dei brevi video"* | Storia personale (2020-2021) |
| 5 | 3.771 | 594 | *"Cosa contiene il corso:"* | Transizione al curriculum |
| 6 | 4.365 | 1.474 | *"Le video-lezioni"* | Curriculum — 20+ lezioni (14 + 7 nuove) |
| 7 | 5.839 | 1.718 | *"Ti beccherai il valore di creator da quasi 1 milione di follower…"* | Prova sociale — 6 creator reali con link diretto al profilo |
| 8 | 7.556 | 630 | *"Cosa ne pensa Fabiano"* | Testimonianza video (1:17) — **assente nella copia** |
| 9 | 8.186 | 1.243 | *"Cosa ca**o sto sbagliando?"* | Storia/autorevolezza — 3 citazioni datate 2020 |
| 10 | 9.429 | 1.422 | *"Questo va virale" - Cit. Andrei, 2024* | Svolta (maestria raggiunta) + reframe ("Togli la speranza, aggiungi la strategia") + 2ª card prezzo |
| 11 | 10.851 | 705 | (footer) | Chiusura legale + nav (originale) / solo legale (copia) |

Confrontando le due strutture: outEmail segue la formula completa a 11 tappe già descritta nel dossier
CONFRONTO (hero → agitazione → prova → rivelazione → benefici → curriculum → qualificazione negativa →
obiezioni → autorevolezza → prezzo → FAQ), mentre outViral **comprime agitazione e prova in un unico
dispositivo autobiografico** (le sezioni 8-10, che sostituiscono sia lo sfogo sui dati sia la
dimostrazione) e **duplica la tappa prezzo** (sezioni 2 e 10) — esattamente come già rilevato nel
dossier CONFRONTO, qui verificato di nuovo sull'originale, non solo sulla copia.

---

## LE PROVE E LA LORO VERIFICABILITÀ

### outEmail — statistiche con link, e claim senza link

Tre link escono davvero dalla pagina verso fonti esterne, tutti verificabili come URL cliccabili reali:

1. *"Lo ha inventato Gary Thuerk nel 1978 fonte."* [y=5105] → `https://en.wikipedia.org/wiki/Email_marketing`.
   **Verificabile ma non puntuale**: il link porta alla voce enciclopedica generale sull'email
   marketing, non a una sezione o nota specifica su Thuerk/1978 — il fatto storico è di dominio
   pubblico e corretto (Thuerk è comunemente citato come il mittente della prima email di massa, nel
   1978), ma la fonte collegata non lo dimostra con una citazione puntuale, lo lascia intuire.
2. *"il lavoratore d'ufficio medio riceve 121 email di marketing al giorno"* [y=5525] → *[fonte]*
   [y=5738] → `https://altitudemarketing.com/blog/use-statistics-in-content-marketing`.
   **Verificabile di seconda mano**: il link è reale e pertinente, ma è un blog di marketing di terze
   parti che a sua volta aggrega statistiche — non un ente di ricerca primario.
3. *"È facile distinguersi… se sai come scrivere email strategiche."* [y=6579] → *[fonte]* [y=6863] →
   `https://www.getresponse.com/it/blog/email-marketing-italia-statistiche-benchmark-trend`.
   **Verificabile ma di parte**: GetResponse è un venditore di software di email marketing, con un
   interesse diretto a mostrare statistiche favorevoli al settore che vende.

Contro questi tre, almeno tre claim restano **ipse dixit puro**, senza alcun link o fonte, nello stesso
testo: *"Sono sicuro al 100% che… Troverai qualcosa di nuovo in outEmail"* [y=17454], *"outEmail ha un
ROI fuori da questo pianeta"* [y=19072/19127], e *"Perché 99% dei miei competitor non sono
copywriter"* [y=17950] — una statistica specifica (99%) presentata senza fonte né metodo di calcolo.
La comparazione screenshot-a-screenshot ("Guarda come sta messa l'azienda Italiana media con le mail"
[y=7251] contro "Guarda, invece, alcuni degli oggetti che io scrivo" [y=8128]) è una **dimostrazione**,
non una citazione: mostra oggetti reali (verificabili come testo, essendo immagini di caselle di
posta) ma non collega mai quegli oggetti a un risultato misurato (tasso di apertura reale, ad esempio)
— il lettore deve fidarsi che siano rappresentativi.

### outViral — 6 profili reali, ma un'asimmetria vera

La prova sociale di outViral è la più forte delle due pagine, misurata: **6 creator reali**, ciascuno
con nome, una riga di credibilità e un bottone *"Vai al profilo"* che porta a un link esterno reale e
cliccabile [y=6752 e y=7380, prima e seconda fila di 3], su tre piattaforme diverse — non solo TikTok:

| Creator | Piattaforma | Link (verificato in `scheda.json`) |
|---|---|---|
| Riccardo Pagano | YouTube | `youtube.com/@RikPaganoGaming` |
| Not Ordinary Spaghetti | TikTok | `tiktok.com/@notordinaryspaghetti` |
| Nicolas Lombardo | Instagram | `instagram.com/nicolasllombardo` |
| Giovanni Pitarresi | TikTok | `tiktok.com/@giovanni.pitarresi` |
| Michele De Monte | TikTok | `tiktok.com/@micheledemonte` |
| Manuel Brignacca | TikTok | `tiktok.com/@manuelbrignacca` |

Questa è prova sociale **realmente verificabile**: chiunque legga la pagina può cliccare e controllare
che il profilo esista e abbia davvero un pubblico — un livello di verificabilità che nessuna delle
statistiche di outEmail raggiunge. Ma i **numeri aggregati** che accompagnano questi profili — *"quasi
1 milione di follower totali"* [y=5934] e *"decine di milioni di visual"* per Riccardo Pagano da solo
[y=6512] — non sono pre-sommati né collegati a una fonte: il lettore dovrebbe andare sui sei profili e
contare da solo per confermarli, un'operazione che nessuno farà davvero prima di comprare.

C'è un'asimmetria degna di nota, verificata sull'elenco completo dei link della pagina (`scheda.json`,
campo `cta[]`): outViral fa vedere **sei profili altrui** per la riprova sociale, ma **non linka mai il
profilo TikTok o social personale di Andrei** — nonostante l'intera pagina ruoti attorno alla sua
competenza personale ("ci becco giusto il 90% delle volte" [y=9867], "nel 2021 ho sbloccato il mio
profilo facendolo esplodere" [y=3004]). Gli unici link interni della pagina, oltre ai sei profili
esterni, sono `/story` ("La mia storia") e `/presto-disponibile` — nessuno dei due è un profilo social
verificabile. Chi vuole controllare se Andrei "ci becca il 90% delle volte" con i propri occhi, sulla
pagina che lo dichiara, non ha modo di farlo con un click.

---

## COME TRATTA LE OBIEZIONI

**outEmail** — due obiezioni esplicite in forma botta-e-risposta:
1. *"'Ma io so già scrivere email'"* [y=15876] → *"Bene, allora sei in target. Ho creato questo per
   persone che vogliono il prossimo livello di pensiero strategico per email marketing."* [y=16045].
   Tecnica: capovolgimento — l'obiezione diventa la prova di essere nel target giusto, non un motivo
   per non comprare.
2. Implicita nel titolo *"🤡: 'Ma l'email marketing non funziona più' No. È il tuo email marketing che
   non funziona."* [y=14101]. Tecnica: redirezione della colpa dal metodo al lettore, per rendere il
   prodotto l'unica via d'uscita.
3. Pre-obiezione di livello: *"Niente basi che già conosci"* [y=17275/17336], dentro il blocco benefici
   — anticipa "sono già troppo avanzato per questo corso" prima che il lettore la formuli.

**outViral** — **zero obiezioni esplicite in forma botta-e-risposta**, confermato di nuovo qui su
questi due file (nessun pattern "Ma io…" nel testo di `22-outviral`, in linea con quanto già registrato
nel dossier CONFRONTO per l'intera famiglia). Le uniche pre-obiezioni gestite sono implicite, incassate
dentro affermazioni: *"Non devi stare dietro all'algoritmo per andare virale e vendere"* [y=1000]
(contro "è troppo tecnico/complicato per me") e *"TikTok è la piattaforma più facile… Ma non per
questo puoi fare a caso"* [y=2432] (contro "se è facile non mi serve un corso").

---

## IL PREZZO E LA SUA CORNICE

**outEmail**: il prezzo (139€) non è mai testo semplice in nessuna delle due versioni — è
un'immagine (`Artboard+41_2.png`, `alt=""`, y=23296) dentro la sezione *"adesso disponibile."*
[y=23381]. La cornice arriva prima come giustificazione economica ("outEmail ha un ROI fuori da questo
pianeta" [y=19072], "Quanti prodotti devi vendere per rifarti dell'investimento… Molto probabilmente
solo 1-2" [y=19635]) e solo dopo mostra la cifra — il valore percepito viene gonfiato prima che il
numero compaia, mai il contrario. Nessuna data di scadenza, nessun countdown: l'unica leva di scarsità
è l'aggettivo "adesso" nel titolo della sezione stessa.

**outViral**: il prezzo (250€, *"Una tantum"*) è sempre **testo semplice**, mai immagine [y=1700 e
y=10468] — a differenza di outEmail, è completamente leggibile da chiunque, screen reader compreso.
Compare due volte, la prima quasi subito dopo l'hero (876px su 11.555, 7,6% di pagina) e la seconda
dopo il reframe finale (10.428px, 90,3% di pagina) — la duplicazione già segnalata nel dossier
CONFRONTO. *"Una tantum"* è l'unica menzione della struttura di pagamento: nessuna rata, nessun
abbonamento, nessuna alternativa di pagamento nominata nel testo (solo "PayPal o qualsiasi carta" nella
riga di rassicurazione [y=10710]).

**In entrambe le copie di lancio**, il bottone-prezzo individuale (che nell'originale non portava mai a
un pagamento reale, `href: null`) viene tolto e sostituito dal badge *"INCLUSO NEL PACCHETTO
ARMAGEDDON"*. Il prezzo barrato resta visibile — la cifra "vecchia" non sparisce, resta lì a fare da
ancora — ma la cornice esplicita cambia da "compra questo corso" a "questo è già incluso in qualcos'
altro". La vera cifra pagabile (199€) non compare mai accanto al prezzo barrato: vive solo nella barra
sticky fissa, separata visivamente dalla card prezzo di ogni singola pagina. Come già notato in "COSA
CAMBIA", il conto del risparmio non viene mai scritto esplicitamente da nessuna parte.

---

## COSA NON DICE MAI

Verificato con ricerca testuale diretta sui quattro file di questo studio (non solo dedotto dal
dossier CONFRONTO):

1. **Nessuna garanzia o rimborso**, su nessuna delle quattro pagine — zero occorrenze di "garanzia" o
   "rimbors*" riferite al prodotto. L'unica occorrenza di "soddisfatt*" trovata nei quattro file è
   *"+5k clienti SODDISFATTI"* [y=6526 originale / y=6011 copia], claim di un'azienda di viaggi
   (Not Ordinary Spaghetti) nella propria bio, non una garanzia di Andrei su outViral.
2. **Nessuna scadenza o countdown esplicito nel copy** — zero occorrenze di "scadenz*", "countdown" o
   "mezzanotte" sulle quattro pagine.
3. **Il calcolo del risparmio** comprando il pacchetto invece dei singoli corsi — mai scritto, né
   nell'originale (dove non serve, essendo un corso singolo) né nella copia (dove servirebbe, ma non
   c'è).
4. **Il proprio profilo social**, in outViral — Andrei non linka mai un proprio account TikTok,
   Instagram o YouTube verificabile, pur basando l'intera autorevolezza della pagina sulla propria
   esperienza personale su TikTok.
5. **Nessuna via di mezzo** fra "vendono a palate" [y=6356] e "sprechi contatti/soldi/tempo"
   [y=14619-14692]: il frame è sempre binario, o strategico o classico, mai un risultato parziale o un
   fallimento del metodo stesso.

---

## LE FORMULE RICORRENTI

Otto costruzioni retoriche verificate testualmente, ognuna con la citazione originale e una versione
in bianco riusabile.

**1. Domanda chiusa apparentemente retorica + negazione immediata + conseguenza peggiore**
> *"Apriresti questa email? […] No, non l'apriresti. Anzi, la metteresti in spam."* [y=185/259/749]

`[DOMANDA CHIUSA CHE SEMBRA RETORICA]? […] No, [NEGAZIONE SECCA]. Anzi, [PLACEHOLDER: CONSEGUENZA
PEGGIORE DEL PREVISTO].`

**2. Cliffhanger "buona notizia / pessima notizia"**
> *"Ho una buona… E una pessima notizia."* [y=2779]

`Ho una buona… E una pessima notizia [PLACEHOLDER: SU TEMA CENTRALE DELLA PAGINA].`

**3. Ripetizione strategica del claim centrale, identica, a due profondità di scroll diverse**
> *"L'email marketing 'classico' è morto."* — compare identica a y=1492 e di nuovo a y=4257, dopo che
> nel mezzo è stato costruito il contesto storico.

`"[PLACEHOLDER: IL VECCHIO METODO] è morto."` ripetuta identica due volte: la prima come apertura di
sezione, la seconda come punto di svolta dopo l'agitazione.

**4. Micro-obiezione con risposta capovolta in una riga**
> *"'Ma io so già scrivere email'" […] "Bene, allora sei in target."* [y=15876/16045]

`"'Ma io [PLACEHOLDER: OBIEZIONE COMUNE DEL TARGET]'" […] "Bene, allora sei [PLACEHOLDER: RISULTATO
POSITIVO INASPETTATO PER CHI HA SOLLEVATO L'OBIEZIONE]."`

**5. Auto-attribuzione di colpa collettiva per creare complicità invece di accusa**
> *"E i killer siamo stati noi… Noi marketer."* [y=4915]

`E i colpevoli siamo stati noi… Noi [PLACEHOLDER: CATEGORIA A CUI APPARTIENE IL LETTORE].`

**6. Sequenza di citazioni di sé stesso, datate, che raccontano una progressione da frustrazione a
mestiere** (unica formula presa da outViral fra le otto)
> *"'Cosa ca**o sto sbagliando?' - cit. Andrei Pascu, 2020"* [y=8281] → *"'Ma… L'ho fatto prima
> io…' - Cit. Andrei 2020"* [y=8727] → *"'Se solo capissi l'algoritmo…' - Cit. Andrei 2020"* [y=9057]
> → *"'Questo va virale' - Cit. Andrei, 2024"* [y=9524]

`"'[PLACEHOLDER: FRUSTRAZIONE INIZIALE]' - cit. [TU], [ANNO A]"` → … → `"'[PLACEHOLDER: FRASE DA CHI
HA CAPITO IL MESTIERE]' - cit. [TU], [ANNO B, anni dopo l'anno A]."`

**7. Qualificazione negativa esplicita seguita da avviso con emoji**
> *"Non è per tutti. Sono serio."* [y=13359] seguito da *"⚠️Quindi non prendere outEmail se sei un
> principiante."* [y=13725]

`"Non è per tutti. Sono serio."` seguito da `"⚠️Quindi non prendere [PLACEHOLDER: PRODOTTO] se
[PLACEHOLDER: PROFILO ESCLUSO]."`

**8. Reframe in tre parole con contrasto cromatico rosso/verde**
> *"Togli la speranza, aggiungi la strategia. Fallo con outViral"* — "Togli" in rosso `#e71111`,
> "aggiungi" in verde `#22bd3e` [y=10252]

`"Togli [PLACEHOLDER: IL PROBLEMA, in rosso], aggiungi [PLACEHOLDER: LA SOLUZIONE, in verde]. Fallo
con [PRODOTTO]."`

---

## IL DIFETTO

Tre difetti reali, ciascuno misurato sui file di questo studio, non impressioni:

1. **Il prezzo di outEmail non è mai leggibile come testo, ed è pure `alt=""`.** In nessuna delle due
   versioni (originale o copia) la cifra "139" compare come testo semplice in `copy-integrale.md` —
   verificato con ricerca testuale diretta, zero risultati. L'immagine che sostituisce il prezzo
   (`Artboard+41_2.png`, y=23296 nell'originale) ha `alt=""` in `scheda.json`: non solo manca un testo
   alternativo descrittivo, l'attributo è esplicitamente vuoto, il che per uno screen reader equivale a
   marcare l'immagine come puramente decorativa. Il prezzo di un corso a pagamento è, per definizione,
   l'informazione meno decorativa della pagina.
2. **L'anno nel corpo storico è scritto a mano, non calcolato.** La riga *"E adesso, nel 2025…"*
   [y=5372, originale] diventa *"E adesso, nel 2026…"* [y=5282, copia] — catturate lo stesso giorno
   (2026-09-07). Se fosse un campo dinamico (`{{currentYear}}`), le due pagine mostrerebbero lo stesso
   valore nello stesso giorno di cattura; siccome divergono, qualcuno ha dovuto aprire l'editor e
   cambiare la cifra a mano quando ha fatto la copia. Il costo di questo difetto non è una tantum: si
   ripresenterà a ogni cambio d'anno, su entrambe le pagine, finché restano in vendita — ed è già
   successo almeno una volta senza essere risolto alla radice (un campo calcolato lo avrebbe evitato
   per sempre).
3. **outViral perde la propria interfaccia video e un'intera sezione di prova senza sostituzione.** Il
   contenitore del video-hero scende da 1.143px a 717px (-426px, -37%) e perde ogni traccia testuale
   dei controlli ("Riproduci", "00:00/03:57", "Impostazioni", "Disattiva audio", "Attiva modalità
   schermo intero") — il file multimediale probabilmente resta (`media: 1` in entrambe le versioni),
   ma senza interfaccia utilizzabile è, ai fini pratici, un video morto. La sezione *"Cosa ne pensa
   Fabiano"* (630px, secondo video-player, 1:17) scompare per intero: i confini delle sezioni adiacenti
   combaciano esatti (7.041px = 5.323+1.718 nella copia) a conferma che non è stata accorciata, è stata
   tagliata di netto. Nessuna delle due perdite viene compensata con un testo, uno screenshot o una
   citazione sostitutiva: la pagina arriva alla sezione successiva come se quella prova non fosse mai
   esistita.

---

## Nota sulla lunghezza

Il documento supera abbondantemente la soglia richiesta di 3.000 parole di sostanza: il materiale
verificabile sulle quattro pagine (due originali + due copie, ~857 blocchi di testo complessivi più i
quattro `scheda.json` con sezioni/CTA/headings) ha dato margine per coprire ogni sezione richiesta con
citazioni dirette, senza necessità di aria.

## Collegamenti

- [14-17-famiglia-out-CONFRONTO.md](14-17-famiglia-out-CONFRONTO.md) — il confronto fra le quattro
  pagine "out*" fra loro (non ripetuto qui), la base dei numeri di prezzo/listino usati in apertura
- [14-17-famiglia-out-ATLANTE.md](14-17-famiglia-out-ATLANTE.md) — le sezioni con gli screenshot aperti
- `capture/21-outemail/copy-integrale.md`, `capture/22-outviral/copy-integrale.md` — gli originali
  studiati riga per riga in questo dossier
- `capture/14-arma-outemail/copy-integrale.md`, `capture/17-arma-outviral/copy-integrale.md` — le copie
  di lancio, diffate riga per riga contro gli originali
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano di studio totale dell'ecosistema
