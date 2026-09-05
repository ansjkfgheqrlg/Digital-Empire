# CONFLITTI — dove il corso e la nostra fabbrica dicono cose opposte

> Aperto il **2026-09-05**, alla lezione A4/L05. Fino a L04 non era servito: il corso e la casa
> erano d'accordo, o il corso taceva.
>
> **Regola di arbitrato (piano §6.4):** l'ultima lezione non vince per anzianità, e la nostra
> fabbrica non vince per orgoglio. Vince l'argomento migliore, scritto — e se vince il corso, si
> cambia noi.

---

## C-001 · L'età minima di un video sorgente — **il corso sceglie ciò che noi scartiamo**

| | |
|---|---|
| **Chi** | `A4/L05` (01:09 → 01:18) contro `03-AGENTI-E-RUOLI/operatori/video-analyst.md:31-32` |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, ma con una correzione** |

**Cosa dice il corso.** Il video da replicare si sceglie dalla home di YouTube guardando il
«numero magico»: l'esempio scelto in diretta ha **5.700 like, 89.000 visualizzazioni, 13 ore fa**.
La freschezza *è* il segnale.

**Cosa diciamo noi.** `video-analyst`, alla voce «Maturità»:

> «Sotto le 24 ore la velocity è rumore: un video di 2 ore con 200 viste segna 100 views/ora, un
> dato che non si manterrà. **Scarta tutto ciò che è più giovane di 24 ore.**»

Con la nostra regola, **il video su cui il corso costruisce l'intera lezione madre sarebbe stato
buttato**.

**Arbitrato.** Hanno ragione tutti e due su metà della cosa, e la nostra metà è scritta male.

Il nostro esempio interno smonta la nostra stessa soglia: *«un video di 2 ore con 200 viste»* è
rumore **per via delle 200 viste**, non per via delle 2 ore. 89.000 viste non sono un campione
piccolo a nessuna età. Abbiamo scritto un filtro **temporale** per difenderci da un problema di
**volume**, e così buttiamo via i candidati migliori delle nicchie dove la freschezza è il
prodotto (notizie, gossip, attualità, cronaca).

Ma il corso, dall'altra parte, non ha alcuna difesa: prende ciò che è caldo **adesso**, e con quel
criterio il video di 2 ore con 200 viste entrerebbe eccome.

**Decisione: la soglia delle 24 ore resta, ma diventa condizionale al volume.** Sotto le 24 ore un
candidato entra **solo se il numero assoluto di viste è abbastanza grande da rendere credibile la
velocity**. La soglia di volume la fissa `video-analyst`, e va dichiarata nel file, non lasciata
al buon senso.

Regola che ne nasce: **`A4-L05-01`** (binario A).

---

## C-002 · Una sola fonte, riscritta — **il corso lo fa, noi lo vietiamo**

| | |
|---|---|
| **Chi** | `A4/L05` (01:18, 01:58, 05:14) contro `03-AGENTI-E-RUOLI/operatori/transcript-collector.md` §8-§9 (regola `A4-L01-02`) |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, senza attenuanti** |

**Cosa dice il corso.** Si scarica il sottotitolo di **un** video, lo si dà a ChatGPT
(«riscrivimi questo testo da zero aggiungendo qualche dettaglio… e rendilo originale») e il
risultato diventa il video. Detto due volte come pregio del metodo: **«non so assolutamente nulla
di cosa tratta questo video»**, «non so neanche di cosa parla la notizia».

**Cosa diciamo noi.** `transcript-collector` conta le parole del materiale e, **sotto ~1.500
parole di transcript**, il pacchetto non parte finché non contiene **almeno 2 fonti esterne** sul
tema. La fabbrica pretende **2.220 parole di script finito**.

**Arbitrato — quattro ragioni, e nessuna è di gusto.**

1. **Il corso si contraddice da solo, sedici minuti dopo.** A 05:53 dice: *«vi ricordo che abbiamo
   già visto come prendere tutte le informazioni da siti, blog, da altri video: potremmo fare un
   testo della durata anche di 10, 12, 15, 20 minuti… se io inserissi altre parti di testo, tutto
   questo sarebbe ancora meglio»*. **La via a più fonti la conosce, la dichiara migliore, e non la
   usa nella dimostrazione.** Noi teniamo quella che lui stesso chiama migliore.
2. **Il fatto smentisce la promessa.** Con una fonte sola il video prodotto in diretta dura
   **2:34** (`frame-113.png`), contro i «10-20 minuti» annunciati. La fonte singola non regge la
   durata che il metodo stesso si pone come obiettivo.
3. **La lezione è di aprile 2023** (`frame-042.png`, ChatGPT su GPT-3.5). Le regole di YouTube sul
   **contenuto riutilizzato** e sui contenuti generati sono state riscritte da allora: un metodo
   che parafrasa un singolo video altrui non è più un rischio teorico. Vedi
   `references/monetizzazione-compliance.md`.
4. **«Rendilo originale» è un'istruzione a un modello, non una proprietà del contenuto.** La
   differenza fra un testo che *sembra* diverso a un lettore e un contenuto che una piattaforma
   considera originale non viene sfiorata in tutta la lezione.

**Decisione: la regola di casa resta e non si tocca.** Il metodo a fonte singola si registra come
**scartato**, con la motivazione, così che nessuna lezione successiva possa reintrodurlo di
straforo. Quello che **prendiamo** dal corso è la sua stessa frase migliore: la durata si costruisce
**aggiungendo fonti**, non allungando il prompt.

Regola che ne nasce: **`A4-L05-03`** (binario A, azione `scarta`).

---

## C-003 · «Prima la quantità» — **una gerarchia che noi abbiamo già rovesciata**

| | |
|---|---|
| **Chi** | `A4/L05` (04:00) contro `ADR-016` (Ultimo Metro) e l'intero apparato di gate |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, ma il corso ci ricorda un difetto vero** |

**Cosa dice il corso.** «Se vogliamo lavorare sulla **quantità**, che è fondamentale — poi
ovviamente sappiamo benissimo che anche la qualità deve esserci.» La qualità arriva come postilla
dopo la congiunzione.

**Cosa facciamo noi.** Tre gate bloccanti (`niche-gate`, `qa-audio-video`, `seo-gate`), regolatori
sulla configurazione, e uno standard di script a 2.220 parole.

**Arbitrato.** Sulla gerarchia vinciamo noi: un canale che pubblica cento video sbagliati non ha
cento occasioni, ha cento prove che il canale è sbagliato.

**Ma il corso ci mette il dito su una piaga documentata.** Il suo metro è **5 minuti per video**.
Il nostro, ad oggi, non è scritto da nessuna parte: `BASELINE.md` misura i test e i difetti, non
il **tempo per video**. E `ADR-016` dice che abbiamo **25 pezzi finiti mai pubblicati**, il più
vecchio fermo da 135 giorni. Un apparato di qualità che produce e non pubblica non è più severità:
è un altro modo di non consegnare.

**Decisione:** la gerarchia resta la nostra, **ma il tempo per video entra fra le misure.** Se non
sappiamo quanto ci costa un video, non possiamo dire di aver scelto la qualità: possiamo solo dire
di essere lenti e chiamarlo standard.

Regola che ne nasce: **`A4-L05-04`** (binario A).

---

## C-004 · Riusare i fotogrammi del video sorgente — **il corso lo insegna, noi lo vietiamo**

| | |
|---|---|
| **Chi** | `A4/L06` («Metodo Copia e Incolla», tutta la lezione) contro `regolatori.py` (`N_GRAM=8`), `fliki_client.py` (`visuals: ai`) e `references/monetizzazione-compliance.md` |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, e la ragione è tecnica prima che morale** |

**Cosa dice il corso.** Si scarica il video altrui in 1080p (aTubeCatcher), si rimuove la traccia
audio, si traduce lo script, si rifà il voiceover, si cambia la musica, **si toglie il logo e si
rifanno tutti i testi a schermo**, si riordinano le clip e se ne sostituiscono alcune con
materiale da Envato o Pexels. La difesa: «così **non incorriamo in strike**» — con tre strike il
canale è chiuso.

**Cosa facciamo noi.** Le immagini nascono dal testo della scena (`visuals: "ai"`) o
dall'archivio Fliki; i regolatori bloccano la copiatura **del testo** con `N_GRAM = 8`.

**Arbitrato — tre ragioni, in ordine di peso:**

1. **La difesa proposta è contro la macchina, non contro il diritto.** Cambiare audio, ordine e
   grafica serve a non farsi riconoscere dal **Content ID**, che identifica e basta: non
   stabilisce chi ha ragione. Un titolare può agire anche su un'opera modificata. Il metodo
   confonde per tutta la lezione **non essere riconosciuti** con **essere in regola**.
2. **Il «fair use» è citato come se fosse una regola di YouTube.** È una dottrina del diritto
   **statunitense**, valutata da un giudice su quattro fattori; l'ordinamento italiano non ha un
   equivalente altrettanto largo. Costruire un modello di business su un istituto straniero
   frainteso è il rischio più grosso della lezione.
3. **È lavoro manuale e cancella l'automazione.** Togliere un logo e rifare ogni testo a schermo,
   su ogni video, è lavoro da editor. La nostra catena genera via API senza aprire un browser:
   **quel passaggio non è eseguibile**, non solo sconveniente.

**Decisione: porta chiusa, scritta nella scheda di conformità** (non in un playbook: un divieto
che vive in un playbook si aggira senza accorgersene). **Si prende l'idea validata, mai i
fotogrammi.**

**Limite nostro, dichiarato nello stesso atto:** la difesa sulla copiatura vigila **solo sul
testo**. Sul visivo non c'è controllo, perché non riusiamo mai materiale altrui — **è una
proprietà del flusso, non un presidio**. Annotato in `BACKLOG.md`.

Regola che ne nasce: **`A4-L06-02`** (binario A).

---

## C-005 · **Il corso contraddice sé stesso** sulla freschezza del video sorgente

| | |
|---|---|
| **Chi** | `A4/L05` (01:09) contro `A4/L06` (07:02) — stessa categoria, due lezioni consecutive |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — non vince nessuna delle due: la nostra correzione le supera entrambe** |

**L05** sceglie un video di **13 ore** e lo chiama «numero magico»: la freschezza *è* il segnale.

**L06**, sedici minuti di lezione dopo, dice il contrario e con un argomento migliore: «è normale
che **un video appena pubblicato faccia tante visualizzazioni, soprattutto se ci sono tanti
iscritti al canale**, che vanno subito a vedere il nuovo contenuto» — e sceglie apposta un video
**non recente**.

**Nessuna delle due lezioni dichiara il contrasto.** Chi segue il corso in ordine riceve due
istruzioni opposte a distanza di una lezione.

**Arbitrato.** L'argomento di L06 è il migliore dei tre in campo — meglio anche del nostro. Il
nostro diceva «sotto le 24 ore la velocity è **rumore**»: un argomento **statistico**. L06 dice
che la velocity di un video giovane **misura la base iscritti del canale, non l'appeal del
contenuto**: un argomento **strutturale**, e per noi decisivo, perché replichiamo su canali
piccoli. Copiare un format che ha fatto numeri grazie a 4 milioni di iscritti altrui significa
copiare **un risultato non riproducibile**.

**Decisione:** la nostra regola non ragiona più per **età** ma per **credibilità del segnale**, in
due passaggi che stanno entrambi in `video-analyst.md` §2:
1. sotto le 24 ore serve un **volume assoluto** che regga (C-001, ≥10.000 viste);
2. e comunque il volume va **rapportato agli iscritti del canale sorgente**, dichiarando il
   rapporto accanto alla velocity.

Così passa il caso di L05 (89.000 viste in 13 ore, se il canale non è gigantesco) e si scarta
quello che L06 teme (il video fresco che vive di iscritti).

Regola che ne nasce: **`A4-L06-01`** (binario A). Aggiorna **C-001**, che resta valido ma
incompleto da solo.
