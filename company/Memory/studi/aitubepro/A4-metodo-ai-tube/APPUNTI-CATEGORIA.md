# APPUNTI DI CATEGORIA — A4 «Metodo AI Tube» (21 lezioni su 21)

> Cosa insegna davvero questa categoria, tolto il rumore. Non è un riassunto delle lezioni: è
> **la conoscenza che ne resta**, riorganizzata per argomento, con lezione e minuto accanto a ogni
> affermazione perché sia sempre possibile risalire.
>
> Materiale d'origine: `L00-…` → `L20-…` (appunti per lezione), i quattro report di blocco, i
> rapporti grezzi delle sentinelle, `../CONFLITTI.md`, e il registro in `../regole/`.
> **Chiuso il 2026-09-06** · studio complessivo a 21/167.

---

## 0. Il quadro in una pagina

**A4 è il cuore del corso**: 21 lezioni, ~8 ore di parlato, e dentro c'è tutto il metodo che
AI TUBE PRO vende. Studiandole in ordine è emersa una cosa che nessuna singola lezione dice:

> **il corso insegna due mestieri diversi e non lo dichiara mai.**
>
> Uno è **fare video con l'AI** (L00-L05, L19, L20): scegliere gli strumenti, scrivere, generare
> voce e immagini, montare via software. Questo mestiere è il nostro, ed è dove abbiamo imparato
> quasi tutto ciò che vale.
>
> L'altro è **rifare i video degli altri** (L06-L14, L16): scaricare, tradurre, ridoppiare,
> camuffare. Questo mestiere non è il nostro, e **occupa più della metà della categoria**.

Su 21 lezioni, **sette sono tutorial d'interfaccia di editor manuali** che la nostra fabbrica non
aprirà mai, e **cinque insegnano a lavorare su materiale di altri**. Non è un difetto del corso:
è il suo modello. Ma spiega perché il raccolto vero è concentrato in poche lezioni.

---

## 1. La produzione — come si fa un video, davvero

### 1.1 Lo strumento non si sceglie per novità (L00 · 04:48)
Uno strumento entra in produzione **solo se ha uno storico dimostrabile e fa ciò che dichiara**.
I cataloghi AI aggiungono decine di voci al giorno (26 in un giorno solo, misurato a schermo) e la
quasi totalità non arriva a sei mesi. Da qui le **cinque domande** di `scelta-strumenti.md`:
storico · piano B se sparisce · costo per video · **si comanda da programma o solo a click** ·
**con che titolo lo stiamo usando**.

Le ultime due sono nate dallo studio, non dal corso, e sono quelle che hanno lavorato di più:
- la quarta ha bocciato **due famiglie intere** — avatar parlanti (L15) e generatori di musica
  (L17): quarantatré passaggi di dimostrazione, **zero endpoint**;
- la quinta è nata da L13, che insegna ad avere Final Cut «gratis per sempre» **azzerando il
  contatore della prova** dal Terminale. Porta chiusa.

### 1.2 Fliki, lo strumento che usiamo davvero (L04, L19, L20)
È l'unica materia della categoria che tocca il nostro motore, e ha reso di più:
- **il campo `YouTube channel ID(s)` nel profilo** (L19 · 02:40, visto a schermo) serve a opporre
  la licenza Fliki ai reclami sulle clip e musiche che la piattaforma ci fornisce. **Non era mai
  stato nominato in tutta la fabbrica.** Va compilato a mano per i due canali: gratis, mai fatto;
- **la mappa delle pronunce vale per un video solo** (L19 · 08:12, «*to apply while generating
  audio for this video*») e si propaga **solo duplicando un file-modello** (L20 · 40:54, 71:52).
  La nostra catena crea ogni video da zero: **da noi non si applica mai**. Le pronunce si
  correggono nel **testo** dello script;
- **la musica non è automatica**: è una traccia a sé, da scegliere e propagare con `Apply to all
  scenes` (L20 · 03:57, 07:48). Unito al fatto che nel nostro payload non c'è un campo musica,
  chiude la domanda: **i nostri video non hanno musica**;
- **volume della musica 5-15%**, tipico in basso (L20 · 07:13, 07:39) — il 10% di L19 era un
  default visto a schermo, non una prescrizione;
- **due tetti, non uno**: i minuti sono un plafond mensile **negoziabile** (L19 · 00:50), ma
  esiste anche un tetto di **50 scene per file** sul piano base (L20 · 66:59);
- **Fliki genera effetti sonori da un prompt** (L20 · 44:53) — e sulla loro licenza non dice nulla,
  a differenza delle tracce musicali dichiarate «licenziate» (L20 · 06:06).

### 1.3 Il testo prima di tutto (L01, L02, L03, L05)
La lunghezza di uno script **si costruisce con le fonti, non col prompt** (L05): chiedere «scrivi
più lungo» produce riempimento. Le fonti di supporto vanno **in una colonna del piano
editoriale** (L01 · 05:44), altrimenti si ricerca tutto da capo al video dopo.

La voce va **scelta una volta e fissata** (L03 · 09:25): oggi ogni canale dichiara il suo
`voice_id`, e non lo riscegli a ogni generazione.

### 1.4 I due principi di scrittura (L14 · 09:36, 45:35)
- **i primi 30 secondi sono ritenzione, non solo clic** — titolo e copertina fanno cliccare, i
  primi trenta secondi fanno **restare**. A 137 parole/minuto sono **~68 parole**: budget stretto,
  da dichiarare;
- **il video finisce chiedendo una cosa sola**, motivata, ruotata fra poche varianti.

### 1.5 Il formato è una decisione, non una costante (L04 · 12:50, L11 · 06:55)
La tendina «Size» di Fliki (Portrait/Square/Landscape) dice a cosa serve ogni formato. Da oggi
ogni canale **dichiara** la sua destinazione. Chi monta a mano deve **riquadrare** l'orizzontale in
verticale inseguendo il soggetto (L11): noi generiamo già nel formato giusto — **il formato si
genera, non si ritaglia**.

---

## 2. La ricerca — come si sceglie cosa fare

- **La velocity di un video giovane misura la base iscritti, non l'appeal** (L06 · 07:02). È
  l'argomento migliore incontrato in tutto lo studio, e ha riscritto la nostra regola: non si
  ragiona più per **età** del video ma per **credibilità del segnale** — volume assoluto sotto le
  24 ore (≥10.000 viste) **e** rapporto con gli iscritti del canale sorgente.
- **I cataloghi di strumenti si interrogano anche per argomento** (L00 · 07:57): restituiscono
  idee di canale, e quanti strumenti esistono per una nicchia dice quanto è già industrializzata.
  Indizio, non verdetto.
- **Un canale di successo non è una prova** (L16 · 03:55). Prima di aprire una nicchia su un
  esempio: **su cosa si regge** quel successo (se sul riuso di materiale altrui, la nicchia è
  chiusa) e **è riproducibile da noi oggi**, senza archivio e senza base iscritti. Chi guarda solo
  chi è rimasto in piedi fa **survivorship bias**.

---

## 3. La conformità — la parte più densa, e non per scelta

Questa categoria ha prodotto **più regole di compliance che di produzione**, perché più della metà
delle lezioni insegna a lavorare su materiale altrui e nessuna dice mai come farlo legalmente.

### 3.1 I sette miti del camuffamento
| # | Il mito | Dove |
|---|---|---|
| 1 | Il *fair use* è una regola di YouTube che permette di usare i video degli altri | L06 · 10:36 |
| 2 | Filtri ed effetti rendono il video «originale e non più riconoscibile» | L07 · 24:57 |
| 3 | Le clip protette si possono usare «non meno di 5 secondi» | L10 · 09:02 |
| 4 | Coprire il logo e tradurre i testi «evita problemi di copyright» | L08 · 39:56 |
| 5 | «Sono **4 secondi**… siamo dentro il fair use, andate super tranquilli» | L14 · 20:51 |
| 6 | «La clip non è del canale che la usa, quindi **il fair use decade**: noi siamo a posto» | L14 · 19:50 |
| 7 | «Voce nuova + sottotitoli → **video originali, unici**» | L12 · 08:36 |

**Sbagliano tutti nello stesso punto:** confondono **non farsi riconoscere da una macchina** con
**essere in regola**. Il Content ID identifica; non stabilisce chi ha ragione.
E i numeri si smentiscono fra loro: **5 secondi** in L10, **4 secondi** in L14. Una franchigia che
cambia cifra è una franchigia che nessuno ha letto da nessuna parte.

**La regola di casa, in una riga:** *se una tecnica serve a non farsi riconoscere, quella tecnica
sta ammettendo che c'è qualcosa da riconoscere.*

### 3.2 Le porte chiuse
- **il metodo copia-incolla** (L06): non per gusto, ma perché la difesa è contro la macchina, il
  *fair use* è un istituto straniero frainteso, ed è **lavoro manuale che cancella l'automazione**;
- **l'aggiramento di licenza** (L13): Final Cut «gratis per sempre» azzerando il contatore;
- **la separazione audio di brani altrui** (L16): lo strumento è pulito, **il materiale in
  ingresso no**;
- **volto e voce di persone reali** (L15 · 11:36): la lezione fa annunciare a un avatar una finta
  notizia di lutto su un cantante italiano **vero**. E la **stessa persona** compare come materiale
  anche in L12 · 01:36. Mai una parola su consenso o copyright: non è una svista, è un modo di
  lavorare;
- **i personaggi protetti generati dall'AI** (L15 · 09:08): generare non crea un titolo.

### 3.3 Cosa si prende invece, e non è poco
**L'idea validata.** Che un format abbia funzionato — in italiano o in un'altra lingua — è il
segnale più economico che esista. **Si replica l'idea e la struttura; il materiale visivo si genera
o si prende alla fonte.**

---

## 4. I quattro arbitrati che dicono qualcosa sulla fonte

| | il contrasto | esito |
|---|---|---|
| **C-005** | L05 sceglie un video di **13 ore** («numero magico»); L06, sedici minuti dopo, sceglie apposta un video **non recente** | vince l'argomento di L06, e supera anche il nostro |
| **C-006** | L05 promette **~5 minuti a video**; L14 lo esegue dal vivo e dichiara **~1 ora** | vince L14: **fattore 12×** |
| **C-007** | L17 promette «saremo noi i proprietari»; otto minuti dopo: col piano gratuito **nessun diritto** | vince il dettaglio |
| *(minore)* | il titolo di L12 dice «in 2 minuti»; dentro, «in 2-3 minuti» | registrato, non arbitrato |

**Quattro casi non sono un incidente: sono un dato sulla fonte.**

> **La regola generale che ne resta, e vale oltre questo corso:** *l'apertura di una lezione dice
> quello che vende, il dettaglio dice quello che sa. Sul denaro, sui diritti e sul tempo si prende
> il dettaglio — e quando c'è di mezzo una licenza, non si crede a nessuno dei due: si leggono i
> termini del fornitore.*

---

## 5. Le cinque cose che questa categoria ci ha fatto scoprire **di noi**

Il raccolto più prezioso non è ciò che il corso insegna: è ciò che ci ha costretto a guardare.

1. **Un gate bloccante bocciava i video sul volume di una musica che non esiste** — per mesi,
   senza che nessuno se ne accorgesse, perché **un criterio che non può fallire non fa rumore**.
2. **`video-producer` ordinava un montaggio a mano abbandonato da mesi** («lo fa l'utente in
   Fliki»), e quattro dei suoi sei ordini erano ineseguibili via API.
3. **Il criterio di scelta degli strumenti non chiedeva la licenza** — quattro domande su storico,
   piano B, costo e comandabilità, e nessuna sul titolo d'uso.
4. **`niche-scout` misurava i numeri di un canale esemplare e non chiedeva mai su cosa si
   reggessero.**
5. **La fabbrica non poteva produrre Shorts**, e nessun documento lo diceva: era una costante
   scritta a mano dentro il payload.

E tre **vantaggi che avevamo senza saperlo** — e che vanno scritti, perché i vantaggi non scritti
si barattano alla prima scorciatoia: la **sincronia** voce/immagini è gratis nel nostro flusso; le
immagini **nascono dal nostro testo**; il **formato si genera** invece di essere ritagliato.

---

## 6. Cosa resta aperto quando A4 chiude

- **Il tempo per video non è ancora misurato** (`A4-L05-04`). Il corso ha un metro (5 minuti
  promessi, ~1 ora reale), noi nessuno. Finché non c'è, «puntiamo sulla qualità» non è una scelta
  dichiarata: è una copertura della lentezza.
- **Il campo `YouTube channel ID(s)` va compilato a mano** per `dosementale` e `legamidiamore`
  (`A4-L19-01`). Gratis, cinque minuti, mai fatto.
- **Tre verifiche contro il payload reale**, da L20: la generazione SFX esiste via API? il timing
  per-media in secondi è supportato? il tetto di 50 scene vale anche via API?
- **D-1 e D-2** (durata impossibile · `verifica_qualita()` mai invocata) restano aperti **di
  proposito**: si chiudono al gate della categoria **A6**, col numero motivato dalla lezione sulla
  durata ottimale.
