# Report — A4/L02 · «Scrivere e (ri)scrivere testi originali con A.I»

> Le sei voci obbligatorie del piano (§6.2). Appunti in `appunti.md`, schermate in
> `frame-scelti.md`.

---

## 1. Cosa insegna

Come trasformare la materia prima raccolta in L01 in un testo pubblicabile, con **quattro
comandi** dati a ChatGPT e una leva di scala:

| # | comando (verbatim dalla lezione) | a cosa serve |
|---|---|---|
| 1 | «scrivimi questo testo da zero rendendolo originale come se fossi un giornalista» | la riscrittura di base |
| 2 | «aggiungi questa parte di testo **senza essere ripetitivo** e rendi l'articolo originale» | innestare la seconda fonte senza gonfiare |
| 3 | «scrivi un testo **per un video di YouTube** partendo da questo» | dall'articolo al copione |
| 4 | «mi dai più informazioni su *X*?» | espandere un dettaglio emerso nella prima risposta |

**La leva:** i sottotitoli si possono prendere da canali **in altre lingue** e tradurre
riscrivendo («riscrivimi questo testo traducendolo in italiano»). Serve a due cose: pescare in
pozzi dove i concorrenti italiani non pescano, e scalare su più lingue.

E un comando che **non** si prende: «scrivimi questo testo come se fosse un giornalista **RAI**».
L'autore lo dà, poi si corregge da solo nella stessa lezione — «non possiamo dire che siamo la
RAI, perché non lo siamo» — ma resta detto due volte prima della correzione.

## 2. Cosa facciamo oggi (verificato sul disco, non ricordato)

| Pezzo | Dove | Stato reale |
|---|---|---|
| Obbligo di riscrivere | `apex7_orchestrator.py:1200` | **c'è**, scritto nel pacchetto: «Va RISCRITTO, non copiato: stesso argomento e stesse informazioni reali, parole proprie» |
| Controllo che non sia copia | `regolatori.py:153-178` | **c'è**: n-grammi condivisi con la sorgente → blocco. Dichiara da sé il proprio punto cieco: fra lingue diverse la sovrapposizione è sempre zero e **non prova nulla** (righe 156-158) |
| Catalogo di comandi di riscrittura | — | **NON ESISTE.** In `script-writer.md` la parola «prompt» compare una volta sola, ed è l'intestazione della sezione «System prompt» |
| **Verifica dei fatti** | — | **NON ESISTE IN TUTTA LA FABBRICA.** `grep -ril "verifica dei fatti\|fact-check\|controllo dei fatti"` su tutti i `.md` e `.py`: **zero risultati** |
| Divieto di impersonare una testata | `regolatore-copy.md` §2 | **NON C'È.** I divieti elencati sono anglicismi, frasi lunghe, ritmo da social, emoji, promesse mediche. Nulla su testate, giornalisti o enti reali |
| Sorgenti in altre lingue | `build_candidate_pool.py` | **non previste**: il pool nasce da un elenco fisso di canali italiani della nicchia |

## 3. Delta

**Tre buchi, e il primo è quello che può far male sul serio.**

**a) Nessuno verifica i fatti dopo la riscrittura.**
Il pezzo riscritto nella lezione contiene: un nome e cognome, un'età (63 anni), una data
(13 ottobre 2021), la causa di morte, le dichiarazioni della moglie fra virgolette, la data e il
luogo dei funerali. Un modello che riscrive «con parole proprie» può **spostare una data,
cambiare un'età, attribuire una frase a chi non l'ha detta** — e nella nostra catena non c'è
nessun momento in cui qualcuno confronti i fatti del testo finale con quelli della fonte.

Abbiamo un regolatore che misura se il testo è **troppo simile** all'originale. Non ne abbiamo
nessuno che misuri se è **ancora vero**. Sono due controlli opposti, e ne facciamo solo uno.

**b) Nessun divieto di impersonare una testata o un ente reale.**
«Come se fossi un giornalista RAI» è un comando che l'autore stesso ritira dopo dodici secondi.
Nel nostro `regolatore-copy` non esiste una riga che lo vieterebbe: i divieti riguardano lo stile,
non l'identità. Un testo che si presenta con l'autorevolezza di una testata che non siamo è un
problema di sostanza — non di gusto.

**c) Nessun catalogo dei comandi.**
Ogni riscrittura riparte da zero: le stesse istruzioni vengono reinventate ogni volta, e la
clausola più utile della lezione — **«senza essere ripetitivo»** — non è scritta da nessuna parte
in casa nostra. Questa clausola vale doppio per noi, perché la fabbrica pretende 2.220 parole
(`A4-L01-01`): senza un vincolo esplicito contro il riempitivo, il modo più rapido per arrivarci
è dire «continua» — che allunga con quello che il modello ha in pancia, non con informazione.

**Quello che NON prendo:** «continua» come strumento di allungamento (si allunga con le fonti,
mai col serbatoio del modello); la rivendicazione dei «200 contenuti in un'ora», che è un numero
di velocità senza un solo dato di resa; e la fiducia cieca nel «rendilo originale», che affida al
modello la verifica di sé stesso — noi quel controllo lo facciamo con gli n-grammi, e va tenuto.

## 4. Conflitti col nostro modo di fare

**Uno vero, e la lezione lo risolve da sé:** il comando «come se fossi un giornalista RAI» è
incompatibile con qualunque standard di casa nostra. Va registrato come **divieto esplicito**,
non lasciato al buon senso — perché il buon senso, in questa lezione, è arrivato **dodici secondi
dopo** il comando.

Secondo punto, più sottile: la lezione mostra ChatGPT che **inventa una notizia intera** su
richiesta («scrivimi una notizia del giorno») e la presenta come dimostrazione di potenza. Per
noi la distinzione fra *riscrivere fatti veri* e *generare fatti* è la linea che separa il
mestiere dal danno. La lezione non la traccia; noi sì, e va scritto.

## 5. Regole estratte

Quattro, nel registro: `regole/A4-metodo-ai-tube/L02_riscrivere_testi.py`.

| id | regola in una riga | tocca | binario |
|---|---|---|---|
| `A4-L02-01` | **Mai impersonare** una testata, un ente o un giornalista reale: né nel testo, né nel comando dato al modello | `regolatore-copy.md` | **A** |
| `A4-L02-02` | I **fatti presi dalla sorgente** (nomi, date, cifre, citazioni, luoghi) si rileggono uno per uno contro la fonte **dopo** la riscrittura: si controlla che sia ancora vero, non solo che non sia copiato | `script-writer.md` | **A** |
| `A4-L02-03` | Catalogo dei **comandi di riscrittura**, con la clausola anti-ripetizione obbligatoria e il divieto di allungare con «continua»: si allunga con le fonti | nuovo `references/comandi-riscrittura.md` | **A** |
| `A4-L02-04` | Una sorgente **in un'altra lingua** è ammessa e va cercata, ma allora il controllo a n-grammi è cieco per costruzione e serve un **controllo semantico dichiarato** | `capi/capo-ricerca.md` | **A** |

## 6. Applicabilità alla nostra fabbrica

- **Tutte e quattro applicate subito** (binario A): riguardano agenti e schede, non il motore.
- **Debito dichiarato, non tappato con una toppa:** `A4-L02-02` mette l'obbligo di verifica dei
  fatti in capo a chi scrive. Un **regolatore dei fatti** vero — automatico, come quello
  dell'originalità — sarebbe la soluzione giusta, ma è un organo nuovo nell'architettura e si
  apre con un ADR, non dentro una lezione. Va in `BACKLOG.md` con il numero del difetto.
- `A4-L02-04` non apre nuove sorgenti da sola: dice **come** si usa una sorgente non italiana se
  e quando il pool verrà esteso. L'estensione del pool è una decisione di `capo-strategia`, e si
  lega alla leva multilingua già registrata in `A4-L01-04`.

**Valore netto della lezione:** è la lezione più vicina al cuore della fabbrica di tutte quelle
viste finora, e ha scoperto **il buco più grave dello studio**: sappiamo misurare se un testo è
copiato, non sappiamo dire se è ancora vero.
