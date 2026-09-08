---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #onda-b #atlante-visivo #design-system #squarespace
Created: 2026-09-08
Last updated: 2026-09-08
---

# ATLANTE VISIVO — le quattro pagine di vendita di onda B

**Composizione visiva, non copy.** Il copy delle quattro pagine è già coperto da
[21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md), [23-vendita-COPY.md](23-vendita-COPY.md) e
[26-mpo2-COPY.md](26-mpo2-COPY.md): qui non si ripete una frase di quei tre documenti. Questo atlante guarda
**come è costruita ogni schermata** — file immagine, ruolo, altezza, cosa la compone, effetti, perché è fatta
così — con lo stesso metodo di [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md), il modello di forma.

Le quattro pagine vivono tutte sotto `www.andrei-copy.com` (Squarespace), catturate il 2026-09-07:

| Pagina | URL | Prodotto | Altezza desktop | Altezza mobile | Sezioni tot. / distinte |
|---|---|---|---|---|---|
| **21-outemail** | `/outemail` | corso email marketing | 26.032px | 24.629px (**-5%**) | 24 / 17 |
| **22-outviral** | `/outviral` | corso TikTok/virale | 11.555px | 16.559px (**+43%**) | 11 / 11 |
| **23-vendita** | `/vendita` | Vendita101 (corso vendita) | 14.905px | 18.738px (**+26%**) | 18 / 15 |
| **26-mpo2** | `/mpo2` | Mindset: Programma Operativo | 10.120px | 12.554px (**+24%**) | 13 / 13 |

Il primo scarto misurato: **outEmail è l'unica delle quattro che si accorcia sul mobile**, le altre tre si
allungano del 24-43%. Combinato con altri due segnali — `body_bg` di 21 è `#ffffff` mentre le altre tre sono
`#a8a8a8` (grigio medio), e il font dominante di 21 è `Inter` (163 occorrenze) contro `elza-8u3n84` per le
altre tre — la conclusione è che **outEmail gira su un template Squarespace diverso e più vecchio** delle
altre tre pagine, verosimilmente costruito in una fase precedente dell'ecosistema. Le sezioni di 21 usano
infatti la classe `page-section.has-section-divider.full-bleed-section` con wrapper `div.section-border`
annidati — struttura assente nelle altre tre, che usano `page-section.layout-engine-section` più piatto.

**Continuità di brand cross-dominio confermata**: il blu CTA `#0062ff` di queste quattro pagine è
**esattamente lo stesso** blu usato da apsales.eu (Tavola 1, 5, 6 del documento modello) — stesso token,
due domini diversi dello stesso ecosistema Andrei Pascu. Il glow azzurro sulla card prezzo di outEmail
(`rgb(135, 206, 235) 0px 0px 15.47px`, misurato in `ombre`) è un'ombra luminosa coerente con quello stesso
accento.

---

# PARTE A — outEmail (21, 26.032px, 17 firme distinte)

Le immagini vivono in `../capture/21-outemail/sezioni/`.

## TAVOLA A1 — L'apertura in tre atti (sezioni 1-4)

![sezione 01](../capture/21-outemail/sezioni/01-apriresti-questa.png)

**01 — Hero** (`i=1`, y=0, h=1330, gruppo 1 rappresentante). Sfondo: la foto `Vivid Blue Abstract Gradient
Wallpaper.jpg` (1440×1330) — **non è un colore piatto**, è un asset fotografico riusato altre 3 volte più
in basso nella stessa pagina (y=6186, y=7070, y=13978) come fondale-ricorrente ai punti di svolta narrativa,
una firma visiva della pagina. Sopra: eyebrow "Apriresti questa" (48px) + "email?" in bold enorme con una
freccia-swash SVG sottolineata a mano; sotto, una card-finta di notifica Gmail ("Azienda ita**gl**iana /
Caro lettore, abbiamo una nuova offerta per te") con l'icona ufficiale Gmail — il primo elemento di finzione
visiva della pagina, usato per far *vedere* il problema (l'email generica) prima di descriverlo a parole.
Segue H1 "No, non l'apriresti..." e la frase "Eppure, questo è il livello di email marketing in **Italia**"
dove **Italia** è colorata lettera per lettera come la bandiera (verde-bianco-rosso) — un dettaglio
tipografico minuscolo che collega il claim al paese target senza aggiungere una parola. CTA blu piena
"Impara a scrivere email performanti" (320×53, radius 10px).

![sezione 02](../capture/21-outemail/sezioni/02-che-dio-riposi-la-sua-anima.png)

**02 — "Che Dio riposi la sua anima..."** (`i=2`, y=1330, h=1343, gruppo 2 rappresentante). Fondo nero
pieno. Immagine centrale: un uomo in tonaca da prete dietro un pulpito rosso velluto, mani giunte, con sul
leggio lo schermo di un laptop che mostra un'email-tipo ("Risparmia il 30%... Annulla iscrizione") — la
*email marketing classica* messa letteralmente al funerale. Sotto: claim "Email marketing strategico" in
verde acceso, poi 4 riquadri-icona (Marketer/Copywriter/Imprenditori/Ecommerce) a segmentare il pubblico.
Chiude con freccia chevron-down, invito a scorrere. **Sezione 03** (non rappresentante, stessa firma
`page-section.has-section-divider.full-bleed-section|3|M|-|7`) ripete lo schema con solo heading "Ho una
buona... e una pessima notizia." — non vista separatamente, stesso impianto.

![sezione 04](../capture/21-outemail/sezioni/04-l-email-marketing-classico-morto.png)

**04 — "L'email marketing 'classico' è morto"** (`i=4`, y=4162, h=2053 — **la più alta di tutta la pagina**,
20 blocchi, 120 parole, la sezione editoriale più densa). Apre con la scritta "COLPEVOLE" ripetuta 4 volte
in rosso dietro un uomo in nero con coltello insanguinato — immagine drammatica per un claim storico-tecnico
("l'email marketing è nato nel 1978"). Segue un ritratto reale di Gary Thuerk (l'inventore, foto storica
autentica, non stock) accanto al mini-storico per decennio (2000/2010/2025), poi un'illustrazione a busta
con "121 email di marketing al giorno" per quantificare il rumore. Chiude bold: "I killer siamo noi...".
**Perché è costruita così**: tre registri visivi diversi in una sezione sola (dramma/cinema → foto
documentaria → infografica) tengono viva l'attenzione per 2053px di scroll, la sezione più a rischio
abbandono della pagina.

## TAVOLA A2 — Il difetto della `div.section-border` (sezioni 05 e 12)

![sezione 05](../capture/21-outemail/sezioni/05-div.png)

**05** (`i=5`, y=6232, h=924, tag `div`, classi `section-border`, **rappresentante gruppo 5**). `scheda.json`
dichiara per questa sezione: `blocchi_testo: 0`, `heading: null`, `media: 1`. Lo screenshot mostra invece
un H2 completo ("Ma sai cosa ho capito io e tante altre aziende che vendono a palate con le email?"), due
paragrafi di corpo, e una card rossa con glow al neon ("Nel mercato mediocre, solo **2,87%** delle persone
clicca il pulsante nelle email" + cursore disegnato) — **contenuto reale e sostanzioso, contato come zero**.
La stessa identica firma-difetto ricompare identica in **12-div.png** (`i=12`, y=14024, h=833, gruppo 12):
dichiarato `blocchi_testo:0 / heading:null / media:1`, lo screenshot mostra un H2 completo ("🤡: 'Ma l'email
marketing non funziona più'... No. È il **tuo** email marketing che non funziona."), tre bullet e una CTA
di continuazione. **Due occorrenze identiche sulla stessa pagina non sono un caso isolato**: ogni volta che
Squarespace rende un blocco `div.section-border` (il bordo/divisore visivo tra due `page-section`), lo
script di misurazione conta solo il DOM del div-contenitore vuoto e non il contenuto reale, che
strutturalmente appartiene a un layer diverso (probabilmente il layout-engine di Squarespace inietta il
testo in un nodo fratello non incluso nella query). Vedi "DIFETTI TRASVERSALI" più sotto: lo stesso pattern
si ripete su 22-outviral.

## TAVOLA A3 — Prova sociale con schermate finte e vere (sezione 06) e il buco nero (sezione 07)

![sezione 06](../capture/21-outemail/sezioni/06-guarda-come-sta-messa-l-azienda-it.png)

**06** (`i=6`, y=7156, h=1845, gruppo 6 rappresentante). Collage di sei oggetti-email reali di aziende
italiane (nomi e loghi visibilmente sfocati/redatti per privacy) presentati come notifiche di inbox, poi il
contrappunto: gli oggetti scritti dall'autore mostrati come **bolle di chat** (stile iMessage/WhatsApp) —
non email, conversazioni — un trucco di registro che rende gli esempi "suoi" più informali e memorabili di
quelli redatti e formali del competitor implicito ("l'azienda italiana media"). Nessun effetto oltre al
layout a due colonne.

![sezione 07](../capture/21-outemail/sezioni/07-come-si-fa-l-email.png)

**07 — "Come si fa l'email marketing strategico?"** (`i=7`, y=9001, h=771, gruppo 7 rappresentante).
`scheda.json` dichiara `media: 2`; lo screenshot mostra **solo testo su sfondo nero assoluto, nient'altro**
— per tutti i 771px della sezione. **Terza occorrenza del difetto media-fantasma** su questa sola pagina
(dopo le due `div.section-border`): qui il tag è un normale `section`, non un div-bordo, quindi la causa è
diversa — verosimilmente due asset (icone o un piccolo indicatore di scroll) che non erano ancora arrivati
al momento dello scatto. La sezione non-rappresentante **08** (stessa firma, gruppo 7, y=9772 h=891) ha
`media:4, blocchi_testo:0` — probabile lista di loghi/badge non vista separatamente per economia.

## TAVOLA A4 — Il fumetto anti-scarcity e la qualificazione negativa

![sezione 10](../capture/21-outemail/sezioni/10-section.png)

**10** (`i=10`, y=11978, h=1286, gruppo 10 rappresentante, `heading: null`, `media: 5`). Striscia a fumetti
in bianco e nero stile mezzatinta, tre vignette: un ragazzo con laptop dice "Ma potrebbe essere un po' too
much per te", l'altro risponde "Ah, lol, vuoi farmi scarcity?", chiude "NOPE!" — **un'auto-parodia della
finta scarsità**, coerente con l'etica anti-hype già documentata su apsales.eu ("niente countdown finti",
Tavola 13 del modello). È l'unico contenuto illustrato-a-fumetti di questa pagina (outEmail userà lo stesso
device molto più pesantemente in fondo, sezioni 9856-13106 del DOM, non riprese qui per economia). La
sezione **15** (non rappresentante, stessa firma gruppo 10, y=16439) ripete l'impianto con heading diverso.

![sezione 11](../capture/21-outemail/sezioni/11-non-per-tutti-sono-serio.png)

**11 — "Non è per tutti. Sono serio."** (`i=11`, y=13264, h=743, gruppo 11 rappresentante). Qualificazione
**negativa**: tre X rosse elencano cosa outEmail **non** fa (non spiega cos'è una mail, non spiega
copywriting, non salta le basi che già sai), seguite da un avviso ⚠️ giallo "non prendere outEmail se sei
un principiante". **Perché funziona**: dire a chi NON serve il prodotto aumenta la credibilità di chi
resta — la stessa mossa di filtro-ingresso di apsales.eu (Tavola 1 del modello, la riga di qualificazione
al 50% di opacità), qui però resa esplicita ed elencata invece che sussurrata in una riga.

## TAVOLA A5 — Curriculum, prova e prezzo (sezioni 18, 20, 22, 23)

![sezione 18](../capture/21-outemail/sezioni/18-lista-video-lezioni.png)

**18 — "Lista video-lezioni"** (`i=18`, y=20001, h=774, gruppo 18 rappresentante, 55 blocchi testo — il
valore più alto della pagina insieme al footer, ma qui sono le celle nascoste dell'accordion). Tre
thumbnail scure di lezione + tre righe accordion chiuse ("Sezione 1 - Introduzione" ecc.) con icona "+".
Bordo inferiore ondulato via `clip-path: url(#section-divider-...)` — `scheda.json` elenca **10 clip-path
diversi**, uno per ogni transizione a onda della pagina, ciascuno con un ID univoco: un componente
Squarespace nativo ("section divider"), non un asset SVG custom per sezione.

![sezione 20](../capture/21-outemail/sezioni/20-section.png)

**20** (`i=20`, y=21589, h=771, gruppo 20 rappresentante, `heading:null`, `cta:9`, `media:0`). Carosello di
prova con pager "1/7": una card alla volta mostra un oggetto-email reale ("Candele Pro / Vogliamo darti
fuoco, *nome*... / Open") con frecce prev/next e 7 pallini di navigazione — 19 blocchi testo totali nel DOM
(le 7 card precaricate, non tutte visibili nello scatto). **Nota per la Fabbrica Siti**: questo stesso file
(`20-section.png`, stesso contenuto) è referenziato anche in `14-17-famiglia-out-ATLANTE.md` come prova
della versione "arma" (di lancio) di outEmail — **la sezione è riusata identica tra pagina di vendita e
variante di lancio**, zero restyling.

![sezione 22](../capture/21-outemail/sezioni/22-adesso-disponibile.png)

**22 — "outEmail adesso disponibile"** (`i=22`, y=23189, h=1034, gruppo 22 rappresentante). Card prezzo
bianca su fondo chiaro con **glow azzurro** attorno al bordo (l'ombra `rgb(135,206,235) 0px 0px 16.7px
5px` misurata in `scheda.json`), 4 spunte verdi + 1 voce esclusa in grigio con X ("Niente strategie
basilari che conosci già" — la stessa logica "cosa NON include" della Tavola 11, qui dentro la card prezzo
stessa), prezzo **€139**, CTA nera piena "Entra in outEmail". Anche questa sezione è condivisa
byte-per-byte con la variante di lancio (`14-arma-outemail/sezioni/22-...`), confermato in
`14-17-famiglia-out-ATLANTE.md` riga 316-317.

![sezione 23](../capture/21-outemail/sezioni/23-faq.png)

**23 — FAQ** (`i=23`, y=24223, h=1104, gruppo 23 rappresentante). Card unica con bordo arrotondato, 4
accordion chiusi (deliverability/compliance, principianti, "sei sicuro che mi aiuterà?", fonte delle
strategie), chiusura in bold con domanda retorica ("Ribalti 'ste email o no?") e CTA blu "Ok, ok,
facciamolo". Anche questa è condivisa con la variante di lancio (family atlas riga 368).

## TAVOLA A6 — Il footer (condiviso dalle quattro pagine)

![footer](../capture/21-outemail/sezioni/24-footer.png)

**24 — Footer** (`i=24`, y=25327, h=705, tag `footer`, firma `footer|sections|1|M|C|4`). Fondo blu pieno
`#0062ff`, wordmark **"APsales"** (non "outEmail", non "AP Formazione") in bianco, un guerriero
pixel-art/ASCII bianco su blu sullo sfondo destro (stesso trucco `Ascii` di blend-screen documentato su
apsales.eu, Tavola 2 del modello), link (La mia storia/Store/Recensioni/Risorse/Blog), disclaimer legale,
P.IVA. **Questa identica firma di footer (`footer|sections|1|M|C|4`) è stata verificata su tutte e quattro
le pagine di questo studio** (21, 22, 23, 26): un solo footer globale del dominio `andrei-copy.com`,
brandizzato "APsales" indipendentemente dal prodotto venduto sulla pagina — chi arriva in fondo a una
pagina outEmail o Vendita101 vede comunque il marchio-ombrello, non il prodotto appena scorso. Non
riletto separatamente per le altre tre pagine per economia, essendo la stessa istanza di componente.

---

# PARTE B — outViral (22, 11.555px, 11 firme, tutte distinte)

Pagina più corta e più lineare delle quattro: nessuna sezione ripete la firma di un'altra. Palette di sfondo
dominante: `#1b1b1d` (testo, 100 occ.) su `body_bg #a8a8a8` (grigio medio) — diversamente da outEmail, qui
non c'è un fondo bianco puro come base. Immagini in `../capture/22-outviral/sezioni/`.

## TAVOLA B1 — L'hero a collage (01) e il secondo hero video (02, difetto)

![sezione 01](../capture/22-outviral/sezioni/01-ottieni-una-media-di-10k-views-nei.png)

**01 — Hero** (`i=1`, y=0, h=859, gruppo 1 rappresentante). Fondo nuvole viola/violetto (prima ricorrenza
della texture "marmo fluido" che caratterizza questa pagina — vedi sotto). Wordmark "**out**Viral" (out in
viola, Viral in bianco). H1 "Ottieni una media di 10K views nei tuoi prossimi video", sub "Se parli su
TikTok... ti insegno esattamente cosa dire", "Senza ca**ate." in bold. A destra, **non una foto singola ma
un collage di 3 mockup-dispositivo** (laptop con lezioni, tablet+telefono con "Revisione dei tuoi video",
monitor con volto sfumato "Interviste a creator con centinaia di migliaia di follower") — l'hero comunica
tre benefici in parallelo invece di uno slogan singolo, diversamente da tutte le altre hero di queste
quattro pagine che aprono con un solo claim fotografico.

![sezione 02](../capture/22-outviral/sezioni/02-div.png)

**02** (`i=2`, y=876, h=1143, tag `div`, classi `section-border`, gruppo 2 rappresentante). `scheda.json`
dichiara `blocchi_testo:0, heading:null, media:1`. Lo screenshot mostra invece un secondo blocco-hero
completo: H2 "Non devi stare dietro all'algoritmo per andare virale e vendere.", un **player video
incorporato** (thumbnail "L'ALGORITMO È SECONDARIO" con grafico in discesa dietro un ragazzo al telefono,
controlli reali 00:00/03:57, icona TikTok), poi la card prezzo testuale "outViral 2 / 250,00€ / Una tantum"
+ CTA "Entra in outViral" + loghi di pagamento. **Stesso identico difetto di misurazione della Tavola A2**:
`div.section-border` che nasconde contenuto reale e sostanzioso ai contatori del DOM. Confermato su due
pagine diverse (21 e 22): non è un incidente isolato, è sistemico per questa classe Squarespace.

## TAVOLA B2 — Storia personale a coppia di foto e curriculum (03-06)

![sezione 03](../capture/22-outviral/sezioni/03-un-solo-video-e-la-tua-vita-cambia.png)

**03** (`i=3`, y=2019, h=821, gruppo 3 rappresentante). Testo su fondo grigio chiaro sopra, poi split a
fondo marmo-viola con **screenshot reale del profilo TikTok dell'autore** (262,9K follower, 6,7M like,
bio "Parlo di marketing, seguimi per imparare! outViral 2: adesso disponibile") — prova social mostrata
come screenshot di prodotto vero, non come badge grafico.

![sezione 04](../capture/22-outviral/sezioni/04-ho-cambiato-la-mia-vita-con-dei-br.png)

**04 — "Ho cambiato la mia vita con dei brevi video"** (`i=4`, y=2839, h=931, gruppo 4 rappresentante).
Due mockup-telefono affiancati **2020 (0 follower) → 2024 (260k follower)**, poi tre stat-box (260K+
follower / 6.4M like / 2.7M views negli ultimi 28 giorni). Confronto prima/dopo cronologico, l'unico delle
quattro pagine a usare due date reali come struttura portante della prova.

![sezione 05](../capture/22-outviral/sezioni/05-cosa-contiene-il-corso.png)

**05 — "Cosa contiene il corso"** (`i=5`, y=3771, h=594, gruppo 5 rappresentante). Fondo marmo blu/viola
scuro (seconda variante della texture fluida), griglia 2×3 di feature-icona (video-lezioni, esempi
pratici, revisione video, contenuti extra, gruppo Telegram, accesso illimitato) — layout identico nello
schema a quello che ricomparirà su mpo2 sezione 11, con icone diverse.

![sezione 06](../capture/22-outviral/sezioni/06-le-video-lezioni.png)

**06 — "Le video-lezioni"** (`i=6`, y=4365, h=1474, gruppo 6 rappresentante, 73 blocchi testo — il valore
più alto della pagina). Fondo grigio chiaro, due mockup scuri di piattaforma-corso (laptop + due
smartphone), colonna sinistra ad accordion (14 lezioni base, collassate), colonna destra aperta "7 nuove
video-lezioni" con elenco puntato completo (Lezione 15-21, ciascuna con una riga di descrizione) — la
sezione mostra sia il curriculum "storico" collassato sia l'espansione recente aperta, segnalando
visivamente che il corso viene aggiornato nel tempo.

## TAVOLA B3 — Il difetto di leggibilità: prova sociale quasi invisibile (07-08)

![sezione 07](../capture/22-outviral/sezioni/07-ti-beccherai-il-valore-di-creator.png)

**07 — Muro creator** (`i=7`, y=5839, h=1718, gruppo 7 rappresentante, 14 media — il valore più alto della
pagina). Griglia 3×2 di 6 creator (Riccardo Pagano 128k, Not Ordinary Spaghetti 150k, Nicolas Lombardo
100k, Giovanni Pitarresi 100k, Michele De Monte 181k, Manuel Brignacca 104k), ognuno con avatar circolare,
nome, bio breve, follower e bottone "Vai al profilo". **Difetto di contrasto misurato sullo screenshot**:
l'H2 di apertura e i paragrafi bio sono renderizzati in grigio scuro **quasi invisibile** sul fondo
marmo-nero-blu della sezione — nomi, numeri follower e i bottoni (bianco pieno su nero) restano
perfettamente leggibili, ma il body-copy no. Non è un artefatto di cattura (il testo altrove sulla stessa
pagina, su fondi chiari, è nitido): è un vero problema di contrasto colore-su-colore in questa sezione
specifica.

![sezione 08](../capture/22-outviral/sezioni/08-cosa-ne-pensa-fabiano.png)

**08 — "Cosa ne pensa Fabiano"** (`i=8`, y=7556, h=630, gruppo 8 rappresentante, 32 blocchi testo, 12
media). **Stesso difetto di contrasto ripetuto immediatamente dopo**: il titolo "Cosa ne pensa Fabiano" è
leggibile solo a fatica sul fondo nero. Sotto, un player video split-frame: a sinistra la card
"Fabiano — Studente di outViral" con play button, a destra un fermo-immagine reale dello studente al
telefono/webcam — probabile embed di testimonianza video con doppio frame (intro grafica + volto reale).
**Due sezioni consecutive con lo stesso difetto di leggibilità non sono casuali**: la coppia 07-08 condivide
la stessa famiglia di fondo scuro-marmorizzato, segno che il token di colore testo-su-scuro usato qui non è
quello standard della pagina (altrove il bianco pieno funziona) ma una variante più scura non ricalibrata.

## TAVOLA B4 — Il racconto rosso→verde e la chiusura (09-10)

![sezione 09](../capture/22-outviral/sezioni/09-cosa-ca-o-sto-sbagliando-cit-andr.png)

**09 — "Cosa ca**o sto sbagliando? - cit. Andrei Pascu, 2020"** (`i=9`, y=8186, h=1243, gruppo 9
rappresentante). Fondo marmo **rosso** (terza variante texture, colore-codificato: qui è il momento del
fallimento nel racconto). Tre citazioni in prima persona con foto b/n dell'autore giovane al lavoro,
layout alternato testo-sinistra/testo-destra.

![sezione 10](../capture/22-outviral/sezioni/10-questo-va-virale-cit-andrei-2024.png)

**10 — "Questo va virale - cit. Andrei, 2024"** (`i=10`, y=9429, h=1422, gruppo 10 rappresentante — CTA
finale). Fondo marmo **verde** — quarta e ultima variante texture, e il colore cambia esattamente quando
il racconto passa dal fallimento (2020, rosso) alla vittoria (2024, verde). Foto al tramonto su terrazza,
frase-chiave "**Togli** la speranza, **aggiungi** la strategia" con "Togli" in rosso e "aggiungi" in verde
— **la stessa coppia cromatica della texture di sfondo applicata anche al lettering**, coerenza totale tra
colore-ambiente e colore-parola. Prezzo 250€ ripetuto, CTA alternativa "Fai l'account, iscriviti poi
impara." (diversa dal CTA della sezione 02, A/B interno o solo variazione di tono), loghi pagamento.
**Pattern da portare in Fabbrica**: il colore di sfondo come segnale di stadio narrativo (viola=hook,
grigio=spiegazione, rosso=fallimento, verde=redenzione) è un device replicabile a basso costo — non serve
nuova illustrazione, basta un filtro colore sulla stessa texture marmorizzata.

**11 — Footer**: condiviso, vedi Tavola A6.

---

# PARTE C — Vendita101 (23, 14.905px, 15 firme distinte su 18 sezioni)

Immagini in `../capture/23-vendita/sezioni/`. Font dominante `elza-8u3n84` (81 occ.) + `plus-jakarta-sans`
(50) — diverso da outEmail, coerente con outViral e mpo2.

## TAVOLA C1 — Hero e primo respiro (01-02)

![sezione 01](../capture/23-vendita/sezioni/01-impara-come-vendere-quello-che-ti.png)

**01 — Hero** (`i=1`, y=0, h=897, gruppo 1 rappresentante). Foto sfocata di un evento/palco con overlay
scuro, wordmark "Vendita101", H1 "Impara come vendere quello che ti pare a chi ti pare.", sub "Ti insegno
io come si fa.", poi **lista "Senza..." a 4 righe** (senza rimanere bloccato / senza sembrare disperato /
senza dover rincorrere i prospect / senza essere dipendente da uno script) — **lo stesso device di
posizionamento-per-negazione della hero di outViral** ("Senza ca**ate.") e delle qualificazioni negative
di outEmail (Tavola A4): il canone dell'ecosistema preferisce dire cosa il cliente NON dovrà più fare
piuttosto che elencare i benefici in positivo. A destra, foto di un uomo ripreso di spalle con felpa
"AP Formazione" e logo triangolare — non un volto, un simbolo di appartenenza.

![sezione 02](../capture/23-vendita/sezioni/02-la-verit-sulla-vendita.png)

**02 — "La verità sulla vendita."** (`i=2`, y=897, h=599, gruppo 2 rappresentante). Fondo grigio medio
pieno, nessuna immagine, un solo H2 centrato con sottolineatura a mano sulla parola "verità", un solo CTA
("Leggi la storia di Andrei Pascu"). **Sezione-respiro deliberata**: stessa funzione della Tavola 4 di
apsales.eu nel documento modello (unico blocco centrato su una pagina altrimenti allineata a sinistra) e
della sezione 14 di outEmail (unica sezione chiara) — il canone "una pausa visiva a metà pagina lunga" si
conferma qui per la terza volta in due domini diversi.

## TAVOLA C2 — Il difetto della barra sticky (sezione 03)

![sezione 03](../capture/23-vendita/sezioni/03-le-3-categorie-di-persone-che-devo.png)

**03 — "Le 3 categorie di persone che devono saper vendere:"** (`i=3`, y=1496, h=507, gruppo 3
rappresentante). **Difetto di cattura misurato**: una barra nera piena larghezza — logo, link "Claude
Speedrun" a sinistra, "Accedi" a destra — attraversa lo screenshot **a metà altezza**, tagliando
letteralmente in due l'H2 ("Le 3 categorie di persone" resta sopra la barra, "che devono saper vendere:"
sparisce sotto). Sotto la barra, tre righe icona+testo (venditori / lavoratori autonomi e imprenditori /
chi vuole fare 100 mila euro l'anno) sono leggibili solo in parte. Questa non è la normale barra di
navigazione in cima alla pagina: è un elemento `position:fixed` del sito (il men navigazione con link a
un prodotto esterno, "Claude Speedrun") che nello scatto **compare incollato dentro il corpo di una
sezione a metà pagina** — segno che lo screenshot integrale è stato assemblato per scroll-e-scatto
successivi, e l'elemento fisso è stato catturato "congelato" nella sua posizione-di-viewport a ogni
scatto, finendo impresso più volte lungo l'immagine totale invece che una sola volta in cima. **Lo stesso
identico difetto ricompare su 26-mpo2 sezione 02** (vedi Tavola D1): non è un incidente di una pagina sola,
è un artefatto del metodo di cattura full-page usato per questo sito.

## TAVOLA C3 — Diagnosi, storia e prova (04-08)

![sezione 04](../capture/23-vendita/sezioni/04-i-problemi-con-la-formazione-class.png)

**04 — "I problemi con la formazione classica"** (`i=4`, y=2002, h=1393, gruppo 4 rappresentante). Tre
colonne diagnostiche (icona virgolette / icona punto interrogativo / icona X), ciascuna con bullet-list di
esempi concreti (frasi ad effetto vuote, obiezioni non gestite, motivi per cui il mercato non si fida più
dei venditori). Nessun effetto oltre al colore, la densità informativa fa il lavoro.

![sezione 05](../capture/23-vendita/sezioni/05-in-vendita101-imparerai-la-scienza.png)

**05 — "In Vendita101 imparerai la scienza..."** (`i=5`, y=3396, h=1014, gruppo 5 rappresentante). **Coppia
di foto ragazzo-adulto**: foto b/n adolescente con poster band in camera sua, poi foto adulto in giacca su
sfondo città al tramonto — narrazione "timido e introverso" → "imprenditore, libero finanziariamente,
public speaker". **Lo stesso identico device biografico ricompare identico su mpo2 sezione 06** (Tavola
D2): due foto, stesso ordine cronologico giovane→adulto, stessa funzione di prova-per-trasformazione. È un
componente riusabile del canone dell'ecosistema, non un'invenzione a sé di una singola pagina.

![sezione 06](../capture/23-vendita/sezioni/06-niente-chiacchiere-solo-fatti-e-st.png)

**06 — "Niente chiacchiere: solo fatti e strategie"** (`i=6`, y=4410, h=753, gruppo 6 rappresentante,
`media:2`). **Difetto media-differito misurato**: sotto il paragrafo di apertura c'è uno spazio vuoto di
circa 450px — quasi due terzi dell'altezza della sezione — dove il testo ("Anteprima gratuita di
Vendita101... Clicca e vedi il video") promette un video che nello screenshot **non è presente**: nessun
player, nessun thumbnail, solo fondo. Questo è esattamente il difetto anticipato dal briefing di lavoro:
asset differito (video-embed a caricamento lento) non arrivato al momento dello scatto, mentre il DOM lo
dichiara comunque presente (`media:2`).

![sezione 07](../capture/23-vendita/sezioni/07-la-vendita-cambiata-non-mi-credi-c.png)

**07 — "La vendita è cambiata. Chiedilo ai miei partner"** (`i=7`, y=5163, h=1714, gruppo 7
rappresentante). Griglia di 4 partner (Stefano De Cubellis, Roberto Fiori Rocco, Manuel Bollino, Hafid El
Amrani) con foto circolare, ruolo, citazione estesa (fino a 6 righe ciascuna — più lunghe delle bio-brevi
del muro-creator di outViral), icona LinkedIn/Instagram cliccabile. Registro visivo più "corporate" che su
outViral: foto professionali, non screenshot da smartphone, quote strutturate invece di flex sui follower
— coerente con un pubblico B2B/professionale per un corso di vendita rispetto al pubblico creator di
outViral.

![sezione 08](../capture/23-vendita/sezioni/08-vendita-nei-film-vendita-nella-vit.png)

**08 — "Vendita nei film ≠ Vendita nella vita reale"** (`i=8`, y=6877, h=2082 — **la sezione più alta e più
densa di testo di tutto l'atlante**, 398 parole, 18 blocchi). Racconto di fallimento personale esteso: foto
di un uomo con nastro rosso a X sopra (rifiutato), poi selfie etichettato con tre freccette ("io" / "lo
script che non sapevo usare" / "il cliente che mi aveva appena chiuso in faccia") — didascalie-freccia
disegnate a mano sopra la foto, tecnica non vista altrove nelle quattro pagine. Il prezzo (**400€**) compare
già qui, a metà pagina, non solo nella CTA finale — un ancoraggio di prezzo precoce dopo il punto di massima
empatia del racconto, prima che il lettore razionalizzi un rifiuto.

## TAVOLA C4 — Testo puro senza media (09-10) e il buco nero più grande (11-12)

![sezione 09](../capture/23-vendita/sezioni/09-lo-script-ti-fa-sembrare-la-tipa-d.png)

**09** (`i=9`, y=8960, h=701, gruppo 9 rappresentante, `media:1`). Solo testo, nessuna immagine visibile:
argomentazione diretta ("Lo script ti fa sembrare la tipa della Vodafone...") con paragrafi brevi e
sottotitoli in grassetto, nessun effetto — la densità verbale più alta per pixel della pagina (149 parole
in appena 701px, densità 21).

![sezione 10](../capture/23-vendita/sezioni/10-e-quindi-il-momento-di-vendere-per.png)

**10** (`i=10`, y=9661, h=525, gruppo 10 rappresentante, `media:0`). Sezione-cerniera puramente testuale,
transizione dalla diagnosi all'offerta ("E quindi è il momento di vendere per davvero."), menziona per la
prima volta il numero di lezioni (22).

![sezione 11](../capture/23-vendita/sezioni/11-cosa-vendita101-pu-fare-per-te.png)

**11** (`i=11`, y=10186, h=246 — la sezione più bassa della pagina). Solo heading e sottotitolo, introduce
la gallery sottostante.

![sezione 12](../capture/23-vendita/sezioni/12-section.png)

**12 — Gallery** (`i=12`, y=10432, h=450, classe `gallery-section`, gruppo 12 rappresentante). **Il
difetto media-differito più netto di tutto l'atlante**: `scheda.json` dichiara `media:19` — diciannove
immagini — e lo screenshot mostra **una tela completamente vuota**, solo le due frecce prev/next di
navigazione, nessuna delle 19 immagini (presumibilmente screenshot di DM Instagram/Telegram, a giudicare
dal contesto testuale della sezione 11 subito sopra: "Alcuni messaggi che ho ricevuto su Instagram e
Telegram"). Zero contenuto visibile su 19 dichiarati — la prova più forte raccolta in questo studio che il
tipo `gallery-section.full-bleed-section` di Squarespace carica in modo differito e può mancare
completamente lo scatto automatico.

## TAVOLA C5 — Curriculum e chiusura (14-15)

![sezione 14](../capture/23-vendita/sezioni/14-tutto-ci-che-devi-sapere-per-impar.png)

**14 — "Tutto ciò che devi sapere per imparare la skill."** (`i=14`, y=11465, h=973, gruppo 14
rappresentante). Curriculum completo in due colonne di righe-lezione con timestamp (Lezione 0, A, B, C poi
1-22), incluse 5 lezioni-intervista tenute dagli stessi 4 partner mostrati in Tavola C3 sezione 07 (Roberto
Fiori Rocco, Manuel Bollino, Stefano De Cubellis, Hafid El Amrani) più Harvey Specter/Tommy Shelby come
riferimenti pop (lezioni 17-18, analisi del linguaggio del corpo di personaggi fittizi). **Incrocio
verificato**: i volti mostrati come "referenze/social proof" nella sezione 07 sono anche autori di
contenuto reale nel curriculum — il canone della sezione-testimonial non è solo prova, è anteprima del
prodotto stesso.

![sezione 15](../capture/23-vendita/sezioni/15-quindi-hai-deciso-di-non-entrare.png)

**15 — "Quindi, hai deciso di non entrare?"** (`i=15`, y=12438, h=1121, gruppo 15 rappresentante). Chiusura
a leva psicologica inversa: 4 righe con doppia gerarchia tipografica — riga superiore piccola e sbiadita
(la premessa, es. "Contatterai persone pronte a pagarti...") e riga inferiore grande e in bold (la
conseguenza negativa, "Ma non riuscirai a chiudere la vendita") — ognuna con icona X rossa. Prezzo 400€
ripetuto, CTA "Ok, voglio imparare...", loghi pagamento. **15 — Footer**: condiviso, vedi Tavola A6.

---

# PARTE D — Mindset: Programma Operativo (26-mpo2, 10.120px, 13 firme, tutte distinte)

La pagina più corta e più lineare delle quattro. Immagini in `../capture/26-mpo2/sezioni/`.

## TAVOLA D1 — Hero anti-motivazionale (01) e il secondo difetto di barra sticky (02)

![sezione 01](../capture/26-mpo2/sezioni/01-ti-insegner-il-mindset-che-ho-usat.png)

**01 — Hero** (`i=1`, y=0, h=971, gruppo 1 rappresentante). Foto di un locale/concerto con overlay rosso
scuro, logo a fiocco/asterisco "MINDSET PROGRAMMA OPERATIVO", H1 "Ti insegnerò il mindset che ho usato per
costruire un'agenzia di marketing a 6 cifre", sub in corsivo "Impari il mindset imprenditoriale a livello
pratico. **Niente discorsi motivazionali inutili.**" — la hero di un prodotto sul "mindset" apre negando
esplicitamente di essere motivazionale, una mossa di distanziamento di categoria dal rumore concorrente
del settore (i corsi-mindset generici). CTA "Inizia il percorso 🎯".

![sezione 02](../capture/26-mpo2/sezioni/02-non-basta-crederci-per-avere-succe.png)

**02 — "Non 'basta crederci' per avere successo"** (`i=2`, y=971, h=546, gruppo 2 rappresentante).
**Terza occorrenza del difetto barra-sticky**: la stessa barra nera con "Claude Speedrun" e "Accedi" taglia
lo screenshot a circa un terzo dall'alto, sovrapponendosi sia alla coda dell'heading sia al bordo inferiore
del player video sottostante (thumbnail "QUELLO CHE NESSUNO TI INSEGNA" con play button, sfondo rosso a
colonne di luce). Confermato ora su **due pagine diverse** (23 e 26): il difetto non dipende dal contenuto
della singola pagina, dipende dal metodo di cattura del sito nel suo complesso.

## TAVOLA D2 — Anti-motivazionale per immagini (03) e coppia biografica (06)

![sezione 03](../capture/26-mpo2/sezioni/03-avere-mindset-non-significa-guarda.png)

**03 — "Avere Mindset non significa guardare video motivazionali"** (`i=3`, y=1517, h=827, gruppo 3
rappresentante). Colonna di 3 thumbnail impilate di tipici video motivazionali da social ("BASTA SCUSE",
"NON MOLLARE", "VAI AVANTI") ciascuna **barrata da una grande X rossa diagonale** — l'unica sezione delle
quattro pagine che nega un intero genere di contenuto (non solo "i miei competitor", ma "i video
motivazionali" come categoria) per differenziare il prodotto. A destra, testo che definisce "chiarezza" e
"costanza" come i due soli ingredienti reali.

![sezione 04](../capture/26-mpo2/sezioni/04-perch-non-stai-raggiungendo-i-tuoi.png)

**04** (`i=4`, y=2344, h=454, gruppo 4 rappresentante). Solo testo su fondo chiarissimo, nessun media,
reframe diretto ("non sei sfortunato, sei disinformato").

![sezione 05](../capture/26-mpo2/sezioni/05-section.png)

**05** (`i=5`, y=2797, h=594, gruppo 5 rappresentante, `heading:null`). Piccola card bianca arrotondata
isolata su fondo grigio ("Rimani sui tuoi obiettivi 🎯") più un paragrafo breve — non un vero titolo H*,
solo un callout visivo, coerente col dato `heading:null` (nessun incoerenza qui, a differenza delle
`div.section-border` di altre pagine).

![sezione 06](../capture/26-mpo2/sezioni/06-il-mindset-si-impara-e-io-voglio-i.png)

**06 — "Il mindset si impara, e io voglio insegnarlo a te" / "Vali più di quello che pensi"** (`i=6`,
y=3391, h=1185, gruppo 6 rappresentante). **Stessa coppia di foto giovane/adulto** già vista su Vendita101
sezione 05 (Tavola C3): qui foto b/n adolescente al telefono in camera, poi foto adulto su rooftop al
tramonto — di nuovo l'arco "timido e debole" → "chi vali davvero". **Terza conferma nello studio**
(outEmail usa Gary Thuerk come figura storica esterna, ma Vendita101 e mpo2 riusano letteralmente lo stesso
schema-a-due-foto per l'autore stesso): componente di prova biografica standard dell'ecosistema, non
un'idea isolata di una pagina.

## TAVOLA D3 — Diagnosi (07) e curriculum a card (08)

![sezione 07](../capture/26-mpo2/sezioni/07-il-vero-motivo-per-cui-non-sei-dov.png)

**07 — "Il vero motivo per cui non sei dove vorresti essere"** (`i=7`, y=4576, h=822, gruppo 7
rappresentante). Quattro righe diagnostiche con icona a doppia freccia curva (↝) invece dei bullet standard
delle altre pagine — un dettaglio grafico minore ma distintivo, non riusato altrove nello studio.

![sezione 08](../capture/26-mpo2/sezioni/08-argomenti-trattati-nel-percorso.png)

**08 — "Argomenti trattati nel percorso"** (`i=8`, y=5398, h=1437, gruppo 8 rappresentante). Curriculum in
**7 card bianche con badge rosso "SEZIONE N"**, ciascuna con 5-8 bullet a freccia — il curriculum
visivamente più curato delle quattro pagine: badge colorato, ombra sotto ogni card, gerarchia titolo/bullet
chiara. A confronto, il curriculum di outEmail (Tavola A5, accordion) e di Vendita101 (Tavola C5, righe con
timestamp) sono entrambi più piatti e meno scanning-friendly. **Pattern da preferire in Fabbrica**: card
numerate con badge colorato batte sia l'accordion sia la lista a righe per leggibilità di un curriculum
lungo.

## TAVOLA D4 — Gallery che funziona (09-10) e il difetto di animazione congelata (11)

![sezione 09](../capture/26-mpo2/sezioni/09-ecco-i-pareri-di-alcuni-studenti-d.png)

**09** (`i=9`, y=6835, h=297, gruppo 9 rappresentante). Solo heading introduttivo alla gallery sottostante
("Ecco i pareri di alcuni studenti della prima versione di Mindset: Programma Operativo").

![sezione 10](../capture/26-mpo2/sezioni/10-section.png)

**10 — Gallery** (`i=10`, y=7132, h=450, classe `gallery-section`, gruppo 10 rappresentante, `media:17`).
**Qui la gallery ha funzionato**: tre card-fumetto di recensioni reali visibili (Marco via DM Instagram,
Stefano 5 stelle, Alice 4 stelle) con frecce prev/next. Il confronto diretto con la Tavola C4 (gallery di
Vendita101, completamente vuota con `media:19`) prova che il componente `gallery-section` **può** rendere
correttamente — il fallimento osservato altrove è un problema di tempistica/ordine di caricamento al
momento dello scatto, non un difetto strutturale del componente stesso.

![sezione 11](../capture/26-mpo2/sezioni/11-tutto-ci-che-ti-serve.png)

**11 — "Tutto ciò che ti serve"** (`i=11`, y=7582, h=934, gruppo 11 rappresentante). Cinque card-feature
(video-lezioni, praticità, community, step-by-step, mindset) rese perfettamente a piena opacità in bianco e
rosso. **Ma subito sotto**, il prezzo "250,00 €" e "Una tantum" sono renderizzati **semi-trasparenti,
"fantasma"** contro il fondo nero — leggibili solo a fatica. Le card sopra sono nitide, il testo sotto è
sbiadito nello stesso identico frame: la spiegazione più coerente è un'animazione di comparsa
(scroll-reveal a opacità crescente) sul blocco prezzo, catturata **a metà transizione** dallo scatto
automatico, mentre le card sopra avevano già completato la loro animazione di ingresso. Difetto nuovo,
distinto dai due precedenti (barra sticky, media differito): qui il contenuto **esiste** ma è stato
fotografato mentre si stava ancora dissolvendo dentro la vista.

## TAVOLA D5 — FAQ chiara (12)

![sezione 12](../capture/26-mpo2/sezioni/12-domande-comuni.png)

**12 — "Domande comuni"** (`i=12`, y=8516, h=899, gruppo 12 rappresentante, `cta:7`). Sette righe accordion
su **fondo grigio chiaro** — l'inverso di outEmail, dove la FAQ (Tavola A5, sezione 23) è su fondo scuro.
Nessuna delle quattro pagine tiene un canone fisso per il colore di sfondo della FAQ: 21 la fa scura, 26 la
fa chiara — probabile scelta di pacing locale (l'ultima sezione prima della FAQ, qui, era già scura, quindi
la FAQ schiarisce per varietà; su outEmail vale il contrario).

**13 — Footer**: condiviso, vedi Tavola A6.

---

# DIFETTI TRASVERSALI — cinque pattern ripetuti, non incidenti isolati

Ogni voce qui sotto è comparsa **almeno due volte** su pagine diverse: non sono difetti-di-una-sezione, sono
comportamenti sistemici del sito o del metodo di cattura, e vanno trattati come tali.

1. **`div.section-border` nasconde contenuto reale ai contatori.** Confermato tre volte: outEmail sezioni 5
   e 12, outViral sezione 2. In tutti e tre i casi `scheda.json` dichiara `blocchi_testo:0, heading:null`
   mentre lo screenshot mostra un H2 completo, paragrafi e in un caso (outViral) un intero blocco-prezzo con
   player video. Limitato alle pagine con classe `page-section.has-section-divider` (outEmail, outViral) —
   assente su Vendita101 e mpo2, che usano una struttura Squarespace diversa.

2. **Barra di navigazione fissa "impressa" a metà pagina.** Confermato due volte: Vendita101 sezione 3,
   mpo2 sezione 2. Stesso identico elemento (barra nera, "Claude Speedrun" a sinistra, "Accedi" a destra)
   compare a un'altezza che non è la cima della pagina, tagliando un heading in un caso e il bordo di un
   player video nell'altro. Artefatto di cattura full-page per scroll-e-scatto, non un bug del sito reale
   visibile a un utente che scorre normalmente.

3. **Media dichiarato ma assente allo scatto (asset differito).** Confermato quattro volte, con intensità
   crescente: outEmail sezione 7 (2 media dichiarati, zero visibili su fondo nero), Vendita101 sezione 6
   (video anteprima assente, ~450px di vuoto), Vendita101 sezione 12 (**19 media dichiarati, zero visibili**,
   solo frecce di navigazione — il caso più netto), mentre la gallery equivalente su mpo2 (sezione 10, 17
   media) ha funzionato. La differenza tra successo e fallimento è temporale/di caricamento, non
   strutturale — il componente Squarespace è lo stesso.

4. **Testo quasi invisibile su fondo scuro-marmorizzato.** Confermato due volte consecutive su outViral:
   sezioni 7 e 8, entrambe con heading e body-copy in grigio scuro su fondo nero-marmo, mentre bottoni e
   numeri nella stessa sezione restano leggibili. Un solo token di colore-testo non ricalibrato per quella
   specifica famiglia di fondo.

5. **Animazione di comparsa congelata a metà transizione.** Osservato una volta ma distinto e diagnosticabile:
   mpo2 sezione 11, dove il blocco prezzo sotto una griglia di feature-card è semi-trasparente mentre tutto
   il resto della sezione è a piena opacità nello stesso fotogramma.

---

# CONFRONTO CON LA FAMIGLIA DI LANCIO (14-17)

`14-17-famiglia-out-ATLANTE.md` documenta le varianti "arma"/di lancio di outEmail e outViral (cartelle
`14-arma-outemail` e `17-arma-outviral`). Il confronto diretto sui nomi-file conferma che **almeno sei
sezioni di outEmail sono condivise, invariate, tra la pagina di vendita (21, qui studiata) e la sua
variante di lancio**: la qualificazione negativa (`11-non-per-tutti-sono-serio.png`), l'obiezione
"so già scrivere email" (`14-...png`), l'autorevolezza col ritratto-re (`16-andrei-perch...png`), il
curriculum (`18-lista-video-lezioni.png`), il carosello di prova oggetti-email (`20-section.png`), la
card prezzo (`22-adesso-disponibile.png`) e la FAQ (`23-faq.png`). Per outViral, il muro-creator
(`07-ti-beccherai-il-valore-di-creator.png`) è condiviso identico. **Non c'è restyling tra pagina di
vendita e pagina di lancio per questi due prodotti**: il team riusa il componente byte-per-byte invece di
ricostruirlo, a differenza di quanto il documento 14-17 registra per outFunnel e outHeadline (che invece
rielaborano gli stessi beat con layout diversi). Per Vendita101 e mpo2 non esiste (in questo studio) una
cartella "arma" gemella da confrontare — restano le uniche due pagine senza una variante di lancio nota.

---

# DELTA ALLA FABBRICA

**CANONE:**
Fissare come regola per ogni landing lunga della Fabbrica: (1) il blu d'azione resta un token unico
condiviso a livello di ecosistema, mai reinventato pagina per pagina; (2) ogni pagina lunga (>10.000px)
contiene almeno una sezione-respiro a fondo piatto e testo centrato, posizionata dopo il primo terzo della
pagina; (3) la qualificazione del cliente si scrive per negazione ("Senza X, Senza Y, Senza Z" o "Questo
NON fa...") prima ancora di elencare i benefici in positivo — è il device più riusato delle quattro pagine
studiate, non un'eccezione di una sola.

**PATTERN:**
Adottare la coppia di foto "giovane/adulto" come componente standard per ogni pagina-prodotto guidata da un
fondatore-persona (vista identica su Vendita101 e mpo2, variante-fonte su outEmail con figura storica
esterna): due immagini, ordine cronologico fisso, una riga di trasformazione tra le due. Adottare il
curriculum a card numerate con badge colorato (mpo2, Tavola D3) come default sopra l'accordion piatto o la
lista a timestamp, per leggibilità superiore su corsi con più di 15 lezioni. Dove la pagina ha più di uno
stadio narrativo (hook/problema/soluzione), considerare il colore di sfondo come segnale di stadio
(outViral: viola→grigio→rosso→verde) invece di un colore fisso per tutta la pagina.

**GATE:**
Prima di consegnare qualunque scheda.json prodotta da questo stesso metodo di scraping, verificare a mano
ogni sezione con tag `div` e classe contenente `border` o `divider`: se dichiara `blocchi_testo:0` e
`heading:null` ma ha un'altezza superiore a ~600px, è quasi certamente un falso negativo — aprire lo
screenshot prima di fidarsi del numero. Prima di ogni cattura full-page automatica, nascondere o rimuovere
temporaneamente gli elementi `position:fixed`/`sticky` dal DOM, altrimenti si ripeterà l'artefatto
barra-in-mezzo-alla-pagina osservato due volte in questo solo studio. Per ogni sezione con classe
`gallery-section` o media dichiarati >5, introdurre un'attesa esplicita (wait-for-network-idle o
wait-for-selector sull'ultimo elemento atteso) prima dello scatto: la differenza tra la gallery vuota di
Vendita101 e quella riuscita di mpo2 è puramente temporale e replicabile con un'attesa più lunga.

---

## Nota di copertura

Read utilizzate in questo studio: 4 file `scheda.json` (sezione `sezioni` + intestazione palette/font per
tutte e quattro), 1 documento modello, 1 documento famiglia di lancio (grep mirato), 53 immagini di sezione
(17 su 21-outemail, 10 su 22-outviral, 14 su 23-vendita, 12 su 26-mpo2 — una per firma rappresentante,
footer condiviso verificato una sola volta e riferito per le altre tre). Non aperti: le 30 sezioni
non-rappresentanti (stessa firma di una già vista, dichiarate nel testo dove rilevante) e i quattro
`design-tokens.json` (ridondanti con i campi palette/raggi/ombre già presenti in ogni `scheda.json` di
testa, verificato su un campione). Copertura sezioni rappresentative: 53/53 (100%).
