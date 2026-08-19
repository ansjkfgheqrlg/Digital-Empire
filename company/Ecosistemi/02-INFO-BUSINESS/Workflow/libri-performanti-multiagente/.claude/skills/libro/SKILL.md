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
- **4-6 capitoli per volta**, mai tutti insieme: la qualità cala e la sessione si appesantisce
- **~1650 parole a capitolo** (24 × 1650 = 39.600 = ~124 pagine reali).
  **Mai 1500**: 36.000 parole impaginate fanno 112 pagine, *sotto* il minimo di 115.
  La misura vera è **320 parole a pagina**, non 300.
- **Verifico la lunghezza media già dopo il primo blocco di 4-6 capitoli.** Se sto sotto
  1.500 a capitolo il libro chiuderà corto e a fine libro non si recupera senza riscrivere.
  (*The Ninth Winter*: primi 8 capitoli a ~1.030 parole, scoperto al capitolo 24.)
- **Dopo ogni blocco aggiorno `riassunti.md`**: 2-3 righe per capitolo scritto
- **Prima di ogni blocco rileggo `outline.md` + `riassunti.md`** — la continuità viene da lì,
  non dalla memoria della sessione
- Ogni capitolo chiude su un gancio che tira al successivo
- **Nessun capitolo finisce a metà frase.** Sembra ovvio e invece è il difetto che passa:
  parole a posto, pagine a posto, e va in stampa un capitolo mozzo. Dopo ogni blocco:
  ```
  python -c "from pathlib import Path; from engine import validators as v;     [print(x) for c in sorted(Path('LIBRI/in_lavorazione/<slug>/capitoli').glob('cap_*.md'))      for x in v.valida_troncamento(c.read_text(encoding='utf-8'), c.stem)]"
  ```
  Silenzio = tutti chiusi. La consegna lo ricontrolla e **blocca**.
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
  Controllo rapido su un blocco appena scritto:
  ```
  grep -c "—" LIBRI/in_lavorazione/<slug>/capitoli/cap_*.md
  ```
  Deve dare **0 ovunque**. Verificalo a ogni blocco, non a fine libro.

Controllo l'avanzamento quando serve:
```
python -m engine.kdp stato <slug>
```

### 5. La copertina torna da Gael
Gli chiedo il PNG. Poi:
```
python -m engine.kdp consegna <slug> --cover <percorso.png>
```
Il codice porta l'immagine a norma KDP (2:3, 1800×2700), **senza riscriverci sopra il
titolo** — quello l'ha già disegnato il modello seguendo il prompt.

> Se l'immagine arriva **senza testo** o col titolo **sbagliato**, e solo in quel caso:
> `--scrivi-titolo` lo stampa sopra con un font vero. È la rete di sicurezza, non la norma.

### 6. Consegna
`consegna` produce il `.docx` KDP, il PDF, conta le **pagine vere rileggendo il PDF** e
scrive `REPORT.md` + `validazione.json`. Se è sotto le 115 pagine **si ferma e dice quanti
capitoli mancano**.

Il pacchetto finito esce in `LIBRI/libri_pronti/<Titolo>/`. Da lì lo carica Gael a mano.

---

## Riprendere un libro interrotto

Niente si perde, i capitoli sono file.

```
python -m engine.kdp stato            # tutti i libri
python -m engine.kdp stato <slug>     # a che punto è questo
```

Poi rileggo `outline.md` e `riassunti.md` e riparto dal capitolo indicato.

**Attenzione a un caso reale**: `the-ninth-winter` è fermo a 8/24 capitoli e il suo
`riassunti.md` **non è mai stato aggiornato** — contiene solo il segnaposto. Se i riassunti
mancano o sono vuoti, **li ricostruisco rileggendo i capitoli già scritti** prima di
proseguire. Scrivere il capitolo 9 senza sapere cosa è successo nei primi 8 produce un libro
incoerente, e il controllo automatico non se ne accorge.

Stesso libro: i capitoli esistenti sono ~1.040 parole invece di 1.500. Se il conto finale
resta sotto le 115 pagine, servono capitoli più lunghi o più capitoli — lo dice `stato`.

---

## Regole non negoziabili

1. **Mai dichiarare finito un libro sotto le 115 pagine reali.** Il controllo blocca da solo;
   `--forza` serve solo per ispezionare una bozza, mai per consegnare.
2. **Mai un capitolo identico o quasi a un altro.** Se succede è un errore di processo:
   si riscrive.
3. **Mai copiare da un concorrente.** La ricerca serve a capire il mercato, non i testi.
4. **La coerenza viene da `outline.md` + `riassunti.md`**, non dalla memoria della sessione.
5. **Il codice non chiama modelli.** Se una modifica futura lo reintroduce, è un passo
   indietro verso tre fallimenti già pagati.

---

## Comandi, tutti

```
python -m engine.kdp magazzino                       # argomenti pronti
python -m engine.kdp magazzino --aggiungi f.json     # inserisce una ricerca
python -m engine.kdp magazzino --prendi              # il prossimo da scrivere
python -m engine.kdp nicchie --keywords "..." "..."  # misura nicchie su Amazon
python -m engine.kdp nicchia-stato                   # la nicchia del catalogo
python -m engine.kdp nicchia-confronta --keywords "..." [--applica]
python -m engine.kdp nuovo "<Titolo>" --nicchia "<n>"
python -m engine.kdp stato [slug]
python -m engine.kdp consegna <slug> --cover <png> [--scrivi-titolo] [--forza]
```

Exit code: `0` ok · `1` non pubblicabile · `2` parametri sbagliati · `3` errore di sistema.
