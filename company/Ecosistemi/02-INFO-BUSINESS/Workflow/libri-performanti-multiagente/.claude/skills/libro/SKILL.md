---
name: libro
description: Scrive un libro KDP completo, dall'argomento al pacchetto pronto da caricare. Il testo lo scrive Claude in sessione — nessun bot, nessuna API, nessun modello chiamato da codice. Usa questa skill quando Gael dice "/libro", "scrivi un libro", "riprendi il libro X", "facciamo un libro sulla nicchia Y", o quando serve riempire il magazzino di argomenti per la settimana.
---

# Scrivere un libro KDP

**Il principio, da non dimenticare mai**: il libro lo scrivo IO, qui, in sessione. Il codice
Python non chiama nessun modello — impagina, conta le pagine vere, valida, impacchetta.
Ogni tentativo di automatizzare la scrittura su questo progetto è fallito (LM Arena→captcha,
Claude CLI→limite di spesa e prompt troncati). L'unico libro completo mai prodotto,
*The Quiet Hours*, è nato scrivendolo in sessione.

Se ti viene l'istinto di scrivere uno script che generi i capitoli: **è l'errore già fatto
tre volte**. Il codice serve solo per ciò che una macchina fa meglio di una persona.

---

## Come si parte

| Gael dice | Cosa faccio |
|---|---|
| `/libro` | prendo il prossimo argomento dal magazzino e scrivo |
| `/libro <nicchia o idea>` | parto da quello che ha detto lui, saltando il magazzino |
| `/libro riprendi <slug>` | continuo un libro lasciato a metà |
| `/libro ricerca` | riempio il magazzino con 7 argomenti nuovi |

Prima di tutto, sempre: `python -m engine.kdp stato` per vedere cosa c'è già in lavorazione.
**Se c'è un libro incompleto, si finisce quello prima di aprirne un altro** — un catalogo si
costruisce con libri finiti, non con bozze.

---

## Il magazzino argomenti (`/libro ricerca`)

Serve a pagare la fase di giudizio una volta sola, e avere una settimana di libri pronti.

1. **Cerco sul web** nicchie KDP che vendono davvero: cosa funziona ora nella narrativa di
   genere, sottogeneri in crescita, cosa cercano i lettori. Uso `WebSearch`.
2. **Verifico ogni candidata con numeri veri**, mai a sensazione:
   ```
   python -m engine.kdp nicchie --keywords "<candidata 1>" "<candidata 2>" ...
   ```
   Guardo recensioni mediane (basse = aggredibile), concorrenti deboli, prezzo medio.
3. **Scarto senza pietà** ciò che non regge. Meglio 4 argomenti solidi che 7 riempitivi.
4. Scrivo un file JSON con gli argomenti sopravvissuti e lo inserisco:
   ```
   python -m engine.kdp magazzino --aggiungi <file.json>
   ```
   Formato di ogni voce:
   ```json
   {
     "nicchia": "small town romance suspense",
     "titolo_lavoro": "The Lighthouse Letter",
     "premessa": "2-3 righe: chi è il protagonista, cosa gli succede, qual è la posta in gioco.",
     "dati_amazon": {"punteggio": 77.4, "recensioni_mediana": 324, "prezzo_medio": 10.77, "concorrenti_deboli": 6}
   }
   ```
   Il codice **rifiuta** argomenti senza `dati_amazon` e quelli che non sono storie (diari,
   planner, journal): è voluto, non è un ostacolo da aggirare.

---

## Scrivere il libro

### 1. Prendi l'argomento e crea il progetto
```
python -m engine.kdp magazzino --prendi
python -m engine.kdp nuovo "<Titolo Del Libro>" --nicchia "<nicchia>"
```

### 2. Scrivo `outline.md` — la mappa
Deve contenere, e sono tutti obbligatori:
- **Titolo definitivo** — commerciale, chiaro sul genere
- **Personaggi** — protagonista, comprimari, antagonista: nome, età, ruolo, cosa vuole
- **Trama in 3 atti** — impianto, complicazione, risoluzione (col colpo di scena finale)
- **Scaletta dei 24 capitoli** — una riga per capitolo, cosa succede

Se l'outline è solido i capitoli vengono da sé e restano coerenti. Se è vago, il libro va in
contraddizione al capitolo 12 — è già successo.

### 3. Scrivo `copertina-prompt.md` — il prompt per Gael
**PRIMA dei capitoli, e glielo consegno subito nel messaggio.** Non è un dettaglio d'ordine:
su The Ninth Winter il libro è stato finito il 17 e la copertina è arrivata il 18, **un
giorno intero di attesa a libro fermo**. Il prompt si può scrivere adesso, quindi si scrive
adesso e Gael genera mentre io scrivo i capitoli.

**Gael genera l'immagine, io scrivo il prompt.** Deve essere lungo, specifico e completo:
non solo lo sfondo, ma **tutta la copertina finita, testo incluso**.

Ci vanno dentro, tutti:
- **Formato**: verticale 2:3 (rapporto da copertina di libro), alta risoluzione
- **Scena e soggetto**: cosa si vede, chi c'è, cosa sta succedendo, l'ambientazione precisa
- **Atmosfera e luce**: ora del giorno, meteo, sorgenti luminose, mood emotivo
- **Palette**: colori dominanti e d'accento, nominati esplicitamente
- **Stile**: illustrazione/pittura digitale/fotografico, riferimenti di genere, livello di
  dettaglio, resa, nitidezza, grana
- **Composizione**: dove sta il soggetto, quale zona resta libera per il titolo
- **IL TESTO, per esteso**: il titolo scritto **lettera per lettera** come deve apparire, il
  nome dell'autore, dove vanno collocati, che tipo di carattere (serif/sans, peso, effetti),
  che dimensione relativa, che trattamento (ombra, contorno, rilievo) perché restino
  leggibili anche in miniatura
- **Cosa NON deve esserci**: altre scritte, watermark, bordi, cornici

Scrivo il prompt in inglese (i modelli di immagini lo capiscono meglio) e lo consegno a Gael
nel messaggio, oltre a salvarlo nel file.

### 4. Scrivo i capitoli
Un file per capitolo: `capitoli/cap_01.md`, `cap_02.md`, …

```markdown
# Titolo del capitolo

Primo paragrafo.

Secondo paragrafo.
```

**Regole di lavoro, non negoziabili:**
- **8 capitoli per blocco, 3 blocchi in tutto.** Prima erano 4-6 per timore che la qualità
  calasse; adesso il gate qui sotto intercetta il calo, quindi il limite non serve più. Se
  il gate boccia un blocco da 8, torno a 6 **e lo dico**.
- **~1600 parole a capitolo** (24 × 1600 = 38.400 = **120 pagine, il centro esatto** della
  finestra 115-125). **Mirare al minimo è l'errore che costa**: The Ninth Winter è atterrato
  a 115,2 pagine, sul bordo, e ogni ritocco lo faceva cadere sotto — quattro riprese, quattro
  PDF rigenerati. Al centro ho ±1.600 parole di margine.
- **DOPO OGNI BLOCCO, sempre, prima di scrivere il successivo:**
  ```
  python -m engine.kdp blocco <slug>
  ```
  Gira in meno di un secondo (niente PDF, niente OCR) e controlla: dove atterra il libro a
  questo ritmo, lineette, capitoli troncati, riassunti aggiornati, fili aperti da troppo.
  **Se esce con errore mi fermo e correggo QUEL blocco**, non i prossimi.

  > Provato sullo stato reale del 13 agosto: il gate boccia gli 8 capitoli a 1.041 parole
  > dicendo *"il libro chiude a 25.176 parole, 11.624 sotto il minimo"*, più 37 lineette e i
  > riassunti mancanti. Tutti e tre i difetti che sono stati scoperti al capitolo 24.

- **`riassunti.md` si scrive DENTRO lo stesso passaggio dei capitoli**, mai in un giro
  separato. Formato fisso, tre righe per capitolo (Succede / Cambia / Resta aperto) più la
  lista **Fili aperti** in testa: `- [cap NN] cosa è rimasto in sospeso`. Il gate legge quella
  lista e blocca se un filo invecchia di oltre 6 capitoli — è ciò che avrebbe pescato Efrain
  al capitolo 22 invece che con una scena-toppa al 24.
- **Prima di ogni blocco rileggo `outline.md` + `riassunti.md`** — la continuità viene da lì,
  non dalla memoria della sessione
- Ogni capitolo chiude su un gancio che tira al successivo
- **Nessun capitolo finisce a metà frase.** Lo controlla `kdp blocco`, e lo ricontrolla la
  consegna. Parole a posto, pagine a posto, e va in stampa un capitolo mozzo: è il difetto
  che nessun altro controllo vede.
- **MAI lineette lunghe: `—` `–` `--`.** Regola non negoziabile di Gael (2026-08-18), e il
  controllo `valida_lineette` **blocca la consegna** se ce ne sono. Sono la firma più
  riconoscibile della scrittura automatica: su Amazon "sembra scritto dall'AI" è la
  recensione che affonda un titolo.
  Si tolgono **riscrivendo la frase**, non sostituendo il segno con un altro segno:

  | invece di | scrivi |
  |---|---|
  | `Rebecca è ostetrica — mani ferme — e conta i giorni` | `Rebecca è ostetrica, mani ferme, e conta i giorni` |
  | `Lui si voltò — non c'era nessuno` | `Lui si voltò. Non c'era nessuno.` |
  | `Una cosa sola contava — la verità` | `Una cosa sola contava: la verità` |
  | `Aveva ragione — o almeno lo credeva` | `Aveva ragione (o almeno lo credeva)` |

  **I trattini delle parole composte restano**: `twenty-nine`, `hand-lettered`, `chow-chow`
  in inglese sono ortografia, non stile. Toglierli fa sembrare il libro scritto male.
  Lo verifica `kdp blocco` a ogni blocco. A fine libro sono state **193 righe** da
  riscrivere a mano su due libri: al capitolo 8 sarebbero state 37.

Controllo l'avanzamento quando serve:
```
python -m engine.kdp stato <slug>
```

### 5. Il copy KDP — **prima della consegna, non davanti alla form di caricamento**
Scrivo `copy.json` nella cartella del libro e lo salvo col comando. Non si modifica a mano
`progetto.json`: e' cosi' che i primi tre libri hanno preso il copy, e i difetti sono usciti
solo alla consegna (3 lineette nella descrizione di The Ninth Winter, 2 in The Quiet Hours,
**a pacchetto gia' consegnato**).

```
python -m engine.kdp copy <slug> --file LIBRI/in_lavorazione/<slug>/copy.json
```

Campi: `titolo_finale`, `sottotitolo`, `descrizione`, `keywords` (max 7), `categorie`,
`codici_bisac` (max 3), `bio_autore`, `descrizione_html`, `prezzo_suggerito_usd`.
I primi quattro sono **obbligatori**: senza, il comando rifiuta e non salva niente. Il copy
passa dagli stessi controlli del libro (niente lineette lunghe, limiti della form KDP), e
se sbaglia **esce 1 e il copy non viene scritto**: il difetto si ferma dove nasce.

### 6. La copertina torna da Gael
Gli chiedo il PNG. Poi:
```
python -m engine.kdp consegna <slug> --cover <percorso.png>
```
Il codice porta l'immagine a norma KDP (2:3, 1800×2700), **senza riscriverci sopra il
titolo** — quello l'ha già disegnato il modello seguendo il prompt.

> Se l'immagine arriva **senza testo** o col titolo **sbagliato**, e solo in quel caso:
> `--scrivi-titolo` lo stampa sopra con un font vero. È la rete di sicurezza, non la norma.

### 7. Consegna
`consegna` produce il `.docx` KDP, il PDF, **l'EPUB**, conta le **pagine vere rileggendo il
PDF** e scrive `REPORT.md` + `validazione.json`. Se è sotto le 115 pagine **si ferma e dice
quanti capitoli mancano**.

Il pacchetto finito esce in `LIBRI/libri_pronti/<Titolo>/`. Da lì lo carica Gael a mano.

**La cartella nasce anche senza il PNG** (2026-08-25). `consegna <slug>` senza `--cover`
crea comunque il pacchetto con dentro manoscritto, PDF, EPUB, `COPERTINA-PROMPT.md` e
`KDP_METADATA.txt` col copy vero: i tre artefatti che il flusso produce da solo stanno in
una cartella sola, subito, invece di restare sparsi finché non arriva l'immagine. Il libro
però **non è pubblicabile**: `validazione.json` scrive "Copertina assente" fra i bloccanti
ed esce 1. Quando Gael manda il PNG si rilancia `consegna <slug> --cover <file.png>` e la
stessa cartella si aggiorna.

Per sapere in un colpo solo se il pacchetto è a posto:
```
python -m engine.kdp pacchetto <slug>
```
Elenca i file attesi e distingue due stati che prima si confondevano: **COMPLETO** (i tre
artefatti ci sono, exit 0) e **CARICABILE SU KDP** (c'è anche l'immagine). Un pacchetto
completo senza immagine non è un difetto del flusso: è il punto in cui il lavoro passa a Gael.

**Tre cose da sapere sul verdetto:**

- **`verifiche_non_eseguite` non è una sezione di avvisi.** Elenca i controlli che *non hanno
  detto di sì* perché mancava lo strumento. Se il PDF non si è potuto fare, la consegna
  **blocca**: un numero di pagine non misurato non vale come misurato.
- **Il copy passa dagli stessi controlli del libro.** Niente lineette lunghe nella
  descrizione, nel sottotitolo, nella bio e nell'HTML: è il testo che si legge *prima* di
  comprare, ed è lì che "sembra scritto dall'AI" costa una vendita. Blocca.
- **Il prezzo viene confrontato col prezzo medio misurato nella nicchia.** Non blocca, ma se
  è più del doppio o meno della metà lo dice: quel numero è già stato rilevato su Amazon e
  sta in `ispirazione.json`, non va deciso a sentimento.

### 8. Quando il libro è su KDP
```
python -m engine.kdp pubblicato <slug> --asin B0XXXXXXXX [--prezzo 13.99]
```
Archivia il pacchetto in `libri_pubblicati/`, ci copia dentro i sorgenti (capitoli, outline,
riassunti, metriche) verificandoli byte per byte, registra ASIN e prezzo in
`pubblicazione.json`, aggiunge il libro alla nicchia del catalogo, chiude l'argomento in
magazzino e cancella la cartella di lavorazione.

**Da fare sempre**: è il passo che chiude il ciclo e che alimenta il "Also by" in fondo ai
libri successivi. Finché non viene fatto, ogni libro nuovo esce senza sapere che gli altri
esistono.

---

## Riprendere un libro interrotto

Niente si perde, i capitoli sono file.

```
python -m engine.kdp stato            # tutti i libri
python -m engine.kdp stato <slug>     # a che punto è questo
```

Poi rileggo `outline.md` e `riassunti.md` e riparto dal capitolo indicato.

**Il caso reale da cui viene questa regola**: `the-ninth-winter` è rimasto fermo a 8/24
capitoli con il suo `riassunti.md` **mai aggiornato**, e con i capitoli a ~1.040 parole invece
di 1.600. Se i riassunti mancano o sono vuoti, **li ricostruisco rileggendo i capitoli già
scritti** prima di proseguire: scrivere il capitolo 9 senza sapere cosa è successo nei primi
8 produce un libro incoerente. Oggi entrambi i difetti li prende `kdp blocco` al primo giro,
ma quel libro è costato quattro riprese perché sono stati scoperti al capitolo 24.

`kdp stato <slug>` mostra anche le **metriche di produzione**: quanto tempo è passato, quante
volte il gate ha bocciato e perché, quante riconsegne. È lì che si vede dove va il tempo —
il codice, cronometrato, ne prende meno di un minuto.

---

## Regole non negoziabili

1. **Mai dichiarare finito un libro sotto le 115 pagine reali.** Il controllo blocca da solo;
   `--forza` serve solo per ispezionare una bozza, mai per consegnare.
2. **Mai un capitolo identico o quasi a un altro.** Da oggi lo controlla
   `valida_ripetizioni`, sia al gate di blocco sia alla consegna, e **blocca**: era l'unica
   di queste regole che nessuna funzione faceva rispettare.
3. **Mai copiare da un concorrente.** La ricerca serve a capire il mercato, non i testi.
4. **La coerenza viene da `outline.md` + `riassunti.md`**, non dalla memoria della sessione.
5. **Il codice non chiama modelli.** Se una modifica futura lo reintroduce, è un passo
   indietro verso tre fallimenti già pagati.
6. **Un libro si scrive nella nicchia del catalogo.** `kdp nuovo` rifiuta una nicchia diversa
   da quella attiva senza `--motivo`. I primi tre libri sono usciti in tre nicchie diverse,
   con tre nomi d'autore diversi: nessuno dei tre aiuta a vendere gli altri, ed è il modo
   più caro di fare tre libri.

---

## Comandi, tutti

```
python -m engine.kdp magazzino                       # argomenti pronti
python -m engine.kdp magazzino --aggiungi f.json     # inserisce una ricerca
python -m engine.kdp magazzino --prendi              # il prossimo da scrivere
python -m engine.kdp nicchie --keywords "..." "..."  # misura nicchie su Amazon
python -m engine.kdp nicchia-stato                   # la nicchia del catalogo
python -m engine.kdp nicchia-confronta --keywords "..." [--applica]
python -m engine.kdp nuovo "<Titolo>" --nicchia "<n>" [--autore "<nome>"] [--motivo "..."]
python -m engine.kdp blocco <slug>                   # DOPO OGNI BLOCCO. <1 secondo.
python -m engine.kdp stato [slug]                    # avanzamento + metriche di produzione
python -m engine.kdp copy <slug> --file copy.json    # il copy KDP, validato prima di salvarlo
python -m engine.kdp consegna <slug> [--cover <png>] [--scrivi-titolo] [--forza]
python -m engine.kdp pacchetto <slug>                # i tre artefatti sono nella cartella?
python -m engine.kdp pubblicato <slug> --asin B0XXXXXXXX [--prezzo 13.99]
```

Exit code: `0` ok · `1` non pubblicabile · `2` parametri sbagliati · `3` errore di sistema.
