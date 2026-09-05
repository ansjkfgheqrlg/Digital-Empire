# Report — A4/L06 · «Metodo Copia e Incolla»

> Le sei voci obbligatorie del piano (§6.2). Appunti integrali in `appunti.md`, schermate in
> `frame-scelti.md`, arbitrati in `../../CONFLITTI.md`.

---

## 1. Cosa insegna

**Due cose molto diverse, e vanno separate prima di giudicarle.**

**(a) Un metodo di ricerca, che è ottimo.** Come si trova un video da replicare:
- si cerca dentro **canali cash cow** (senza volto), perché sono format ripetibili;
- si usa la scheda vidIQ **«Videos with the highest velocity (views per hour)»**, non la scheda
  «Popolari»;
- **il video deve essere maturo**, e la ragione è la parte migliore della lezione: «è normale che
  un video appena pubblicato faccia tante visualizzazioni, **soprattutto se ci sono tanti iscritti
  al canale**, che vanno subito a vedere il nuovo contenuto» (07:02);
- lo stesso format funziona **in più lingue**, e lo dimostra con due canali reali (Lama Facha
  9,42 M in francese, Famiglia Sfortunata 1,66 M in italiano) che pubblicano **le stesse identiche
  clip**.

**(b) Una procedura di produzione, che è copiare.** Scaricare il video altrui in 1080p, rimuovere
la traccia audio, tradurre lo script, rifare il voiceover, cambiare la musica, **togliere il logo
e tutti i testi a schermo**, riordinare le clip, sostituirne alcune con clip da Envato/Pexels — e
ripubblicare. La difesa dichiarata è: «così **non incorriamo in strike**».

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Pezzo del metodo | Il nostro equivalente | Stato reale |
|---|---|---|
| Cercare dentro canali cash cow senza volto | `channel-scout` + `cashcow_check.py` | **c'è** |
| Ordinare per velocity (VPH) | `video-analyst.md` — `velocity = views / età_in_ore` | **c'è, ed è la stessa formula di vidIQ** |
| Preferire video **maturi** | `video-analyst.md` §2 «Maturità» | **c'è**, appena corretto da `A4-L05-01` (soglia di volume sotto le 24 h) |
| Video sorgente in un'altra lingua | `video-hunter.md` — «bonus: è in un'altra lingua (mercato non ancora saturo)» | **c'è come intuizione**, senza una prova numerica accanto |
| **Riusare le clip del video sorgente** | `fliki_client.py` — `visuals: "ai"` (default) o `stock` | **non lo facciamo e non possiamo farlo**: le immagini nascono dal testo della scena o dall'archivio Fliki |
| Difesa dalla copiatura | `regolatori.py` — `N_GRAM = 8`, `MIN_ELEMENTI_NUOVI = 3` | **c'è, e vigila sul testo**: 8 parole identiche di fila alla fonte fanno scattare il blocco |
| Regole di monetizzazione sui contenuti riutilizzati | `references/monetizzazione-compliance.md` | **c'è** |
| Editing manuale anti-strike (logo, testi, ordine clip) | — | **non esiste, e non deve esistere**: è lavoro a mano in un editor |

## 3. Delta

**La lezione ci dà una cosa preziosa e ce ne chiede una che non possiamo dare.**

**a) Il regalo: perché un video fresco inganna.**
La nostra regola sulla maturità diceva che sotto le 24 ore «la velocity è rumore» — un argomento
**statistico** (campione piccolo, dato instabile). Il corso ne dà uno **migliore, e strutturale**:
sulle prime ore le viste arrivano **dagli iscritti del canale**, che vanno a vedere il nuovo
contenuto perché sono iscritti, non perché il contenuto sia forte. Quindi la velocity di un video
giovane **misura la base iscritti del canale sorgente, non l'appeal del video**.

Per noi che cerchiamo format da replicare **su canali piccoli**, la differenza è tutto: copiare un
video che ha funzionato grazie a 4 milioni di iscritti altrui significa copiare un risultato che
non è riproducibile. La correzione: sotto le 24 ore non basta il volume assoluto (regola
`A4-L05-01`), serve **il volume rapportato agli iscritti del canale**.

**b) La contraddizione interna del corso, che chiude il cerchio su C-001.**
In **L05** sceglie un video di **13 ore** e lo chiama «numero magico». In **L06**, sedici minuti di
lezione dopo, spiega che sui video appena pubblicati le viste vengono dagli iscritti e sceglie
apposta un video **non recente**. Le due lezioni si contraddicono, e nessuna delle due lo dice.
**La nostra correzione le supera entrambe**, perché non ragiona per età ma per **credibilità del
segnale**. Arbitrato in `CONFLITTI.md` **C-001** (aggiornato) e **C-004**.

**c) La richiesta che non possiamo soddisfare: riusare il materiale visivo altrui.**
Non è una questione di gusto, e non basta dire «non ci piace». Tre ragioni concrete, in ordine di
peso:

1. **La difesa proposta è contro la macchina, non contro il diritto.** Cambiare traccia audio,
   ordine delle clip e grafica serve a non farsi riconoscere dal **Content ID**. Ma il Content ID
   è un sistema di identificazione automatica: non decide chi ha ragione. Un titolare può agire
   su un'opera modificata, e la lezione non distingue mai fra **non essere riconosciuti** ed
   **essere in regola**.
2. **Il «fair use» è citato male.** Non è una regola di YouTube ma una dottrina del diritto
   **statunitense**, valutata da un giudice su quattro fattori. L'ordinamento italiano non ha un
   equivalente altrettanto largo. Presentarlo come un permesso concesso dalla piattaforma è la
   parte più rischiosa dell'intera lezione.
3. **Costa lavoro manuale, e uccide l'automazione.** Togliere un logo, rifare tutti i testi a
   schermo, riordinare le clip e sostituirne alcune sono operazioni da editor video, una per una,
   su ogni video. In un corso di *automazione*, è l'unico punto in cui l'automazione sparisce —
   e per noi, che generiamo via API senza aprire un browser, è semplicemente ineseguibile.

**d) Quello che invece prendiamo, ed è concreto: la prova multilingua.**
`video-hunter` dice già che un video in un'altra lingua è un «bonus». La lezione lo trasforma in
**un fatto misurato**: due canali, stesse clip, due lingue, 9,42 M contro 1,66 M di iscritti, e
video gemelli che fanno 63,6k contro 10,4k e 208k contro 75k. Non copiamo le clip — ma **l'idea
validata in un'altra lingua è un candidato forte**, e adesso abbiamo il numero per dirlo.

**Un dato tecnico da tenere:** cambiando voiceover **cambia la durata** (10:56 contro 10:49 sullo
stesso video). Per noi che abbiamo un difetto aperto sulla durata (D-1) è un promemoria: la durata
finale la decide **il parlato**, non il testo — e infatti nel nostro payload `duration` è un campo
inerte.

## 4. Conflitti col nostro modo di fare

Due nuovi, e un aggiornamento a uno esistente:

| id | Il conflitto | Esito |
|---|---|---|
| **C-004** *(nuovo)* | Il corso riusa **il materiale visivo** del video sorgente, difendendosi dal Content ID; noi generiamo le immagini e vigiliamo sul testo con `N_GRAM=8` | **Vinciamo noi**, per tre ragioni: la difesa è contro la macchina e non contro il diritto, il fair use è citato male, e la procedura è manuale |
| **C-005** *(nuovo)* | **Il corso contraddice sé stesso**: L05 sceglie un video di 13 ore, L06 spiega perché non si deve | **Nessuno dei due vince**: la nostra correzione (credibilità del segnale, non età) supera entrambe |
| **C-001** *(aggiornato)* | — | Aggiunto l'argomento migliore del corso: la velocity di un video giovane misura **la base iscritti**, non l'appeal |

## 5. Regole estratte

Tre, nel registro: `regole/A4-metodo-ai-tube/L06_metodo_copia_incolla.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L06-01` | La velocity di un video giovane va **rapportata agli iscritti del canale**: sotto le 24 h le viste arrivano dalla base iscritti, non dall'appeal | `video-analyst.md` | **A** |
| `A4-L06-02` | **Non si riusa il materiale visivo di un video altrui.** Si replica l'**idea validata**, mai i fotogrammi: la difesa dal Content ID non è conformità, e l'editing anti-strike è lavoro manuale che azzera l'automazione | `monetizzazione-compliance.md` | **A** |
| `A4-L06-03` | Un format che ha funzionato **in un'altra lingua** è un candidato forte, e ora con una prova: stesse clip, due lingue, 63,6k contro 10,4k viste | `video-analyst.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e tre applicate subito** (binario A): due agenti/schede, nessuna riga del motore.
- **`A4-L06-01` è il seguito diretto di `A4-L05-01`**, e insieme chiudono bene la questione: la
  prima ha reso la soglia una questione di **volume**, questa la rende una questione di **volume
  relativo al canale**. Il criterio finale sta in `video-analyst.md` §2.
- **`A4-L06-02` è la prima regola dello studio che nasce come divieto**, e va scritta dove serve
  — nella scheda di conformità, non in un agente operativo: un divieto che vive solo in un
  playbook lo si aggira senza accorgersene.
- **Debito dichiarato:** la nostra difesa sulla copiatura vigila **solo sul testo** (`N_GRAM=8`).
  Sul lato visivo non abbiamo alcun controllo — semplicemente perché non riusiamo mai materiale
  altrui. Va scritto: **è una proprietà del nostro flusso, non un controllo**. Se un giorno
  qualcuno introducesse clip scaricate, nessun regolatore se ne accorgerebbe. Annotato in
  `BACKLOG.md`.

**Valore netto della lezione: alto, ma tutto sul lato ricerca.** La procedura di produzione — che
è metà della lezione ed è quella che dà il titolo — è per noi una **porta chiusa**, con le ragioni
scritte. Il lato ricerca invece ci ha dato l'argomento migliore che avessimo sulla maturità dei
video, e una prova numerica per la leva multilingua che avevamo solo come intuizione.
