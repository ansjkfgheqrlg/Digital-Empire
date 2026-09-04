# Comandi di riscrittura — il catalogo

> **Regola `A4-L02-03`** (studio AI TUBE PRO, lezione A4/L02, 2026-09-05).
> Prima di questa scheda, in `script-writer.md` la parola «prompt» compariva **una volta sola**,
> ed era l'intestazione di una sezione: ogni riscrittura ripartiva da zero.

## La regola che viene prima di tutti i comandi

**Si allunga con le fonti, mai col serbatoio del modello.**
Il comando «continua» — mostrato nella lezione — fa scrivere altre righe al modello attingendo a
quello che ha in pancia: non porta informazione, porta volume. È la strada più corta verso il
riempitivo, e la nostra fabbrica ci si infila da sola perché pretende **2.220 parole**
(`apex7_orchestrator.py:146`).

Quando lo script è corto, l'ordine è: **prima nuove fonti** (`transcript-collector` §8), poi la
riscrittura che le innesta. Mai «continua».

---

## I quattro comandi

### 1. Riscrittura di base
```
Riscrivi questo testo da zero rendendolo originale, con tono giornalistico.
Mantieni TUTTI i fatti: nomi, date, cifre, luoghi, ruoli.
Le frasi fra virgolette restano identiche all'originale o spariscono: non si riscrivono.
```
La clausola sui fatti e quella sulle virgolette non stanno nella lezione: le aggiungiamo noi,
perché il controllo dei fatti dopo la riscrittura è nostro (`script-writer` §8).
**Mai** «come se fossi un giornalista di *<testata reale>*»: è vietato (`regolatore-copy` §8).

### 2. Innesto della seconda fonte
```
Aggiungi questa parte di testo SENZA ESSERE RIPETITIVO e mantieni l'articolo originale.
Se un'informazione è già presente, non ripeterla con altre parole: saltala.
```
«Senza essere ripetitivo» è la clausola più utile di tutta la lezione: senza, il modello
riscrive tre volte lo stesso fatto con sinonimi diversi e il testo raggiunge le parole richieste
senza dire nulla di più.

### 3. Dall'articolo al copione
```
Scrivi il testo per un video di YouTube partendo da questo,
con le sezioni HOOK, INTRO, CORPO, CTA. Solo il parlato: niente indicazioni di regia,
niente descrizioni delle immagini, niente titoli di scena.
```
Nella lezione il modello restituisce da sé le indicazioni per le immagini e **si mette da solo la
CTA di iscrizione** (visto a schermo, `frame-215`), che poi l'autore cancella a mano. Meglio
chiedere subito solo il parlato che ripulire dopo — e la nostra CTA è quella di casa, non quella
che il modello ha visto in giro.

### 4. Approfondire un dettaglio
```
Dammi più informazioni su <dettaglio emerso nella risposta precedente>.
Elenca le fonti da cui viene ogni informazione.
```
È il comando che porta sostanza vera invece di volume. La richiesta delle fonti la aggiungiamo
noi: quello che il modello aggiunge senza fonte **non entra nello script** — va verificato o
tolto (`script-writer` §8).

### 5. Sorgente in un'altra lingua
```
Riscrivi questo testo in italiano, rendendolo originale.
Mantieni i nomi propri nella grafia originale.
```
La clausola sui nomi la aggiungiamo noi: la traduzione automatica li storpia più delle frasi.
Su una sorgente non italiana valgono gli obblighi in più di `capo-ricerca` §8: il controllo a
n-grammi è cieco e non conta.

---

## Cosa non si chiede mai al modello

- **Di inventare un fatto.** Nella lezione, «scrivimi una notizia del giorno» produce una notizia
  intera e falsa, presentata come dimostrazione di potenza. Per noi la riga fra *riscrivere fatti
  veri* e *generare fatti* è la linea che separa il mestiere dal danno.
- **Di dichiararsi qualcun altro** (`regolatore-copy` §8).
- **Di giudicare se ha copiato.** «Rendilo originale» è un'istruzione, non una verifica: la
  verifica la fa `regolatori.py` con gli n-grammi, e su lingue diverse non la fa nessuno
  automaticamente.

## Connessioni
- [[script-writer]] — chi usa questi comandi e verifica i fatti dopo
- [[transcript-collector]] — da dove arrivano le fonti con cui si allunga
- [[regolatore-copy]] — il divieto di impersonare
- [[capo-ricerca]] — le sorgenti in altre lingue
