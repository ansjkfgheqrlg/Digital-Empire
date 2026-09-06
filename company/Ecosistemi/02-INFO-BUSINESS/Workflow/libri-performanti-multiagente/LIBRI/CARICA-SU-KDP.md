# Kit di caricamento su KDP — chiude FIX-1 e con esso TASK-KDP-FIX-W2

> Preparato il 2026-09-06 per Gael. Serve a rendere meccanico l'unico pezzo di
> TASK-KDP-FIX-W2 che una sessione non puo' fare: l'upload su un account Amazon.
>
> **Stato oggi: 5 gate su 6 PASS, `libri_pubblicati/` contiene solo `.gitkeep`, 0 ASIN.**
> Al primo ASIN registrato FIX-1 si chiude e con esso l'intera task.

---

## ⚠️ PRIMA DI CARICARE: una decisione irreversibile

I libri hanno **quattro nomi d'autore diversi**:

| Libro | Autore oggi | Nicchia |
|---|---|---|
| The Ninth Winter | **Rebecca Miller** | amish romance suspense |
| The Quiet Hours | **Digital Empire** | psychological thriller |
| The Second-Hand Spellbook | **Maren Ashcroft** | cozy fantasy bookshop |
| Proof of Murder | **Emma Hartwell** | cozy mystery bakery |
| The Winter Term | **Maren Ashcroft** | dark academia mystery |
| The Coven of Lost Ember | **Maren Ashcroft** | found family witch coven |

FIX-2 ha deciso **un autore unico: Maren Ashcroft**, per chiudere B-018. Ma quei tre nomi
diversi sono su libri di **quattro generi diversi**.

**Finche' non carichi, cambiare autore costa niente**: si modifica `autore` in
`progetto.json` e si rilancia `consegna`, che rigenera paratesto, docx, EPUB e
`KDP_METADATA.txt`. **Dopo l'assegnazione dell'ASIN non si torna indietro**: la pagina
autore su Amazon e' legata al nome con cui il libro e' nato.

**La mia raccomandazione: NON unificare tutto sotto Maren Ashcroft.** Il nome d'autore su
Amazon e' per **nicchia**, non per azienda: chi compra amish suspense non compra cozy
fantasy, e un catalogo che mescola i due sotto lo stesso nome confonde l'algoritmo invece di
aiutarlo. La decisione di FIX-2 ("una nicchia, un autore") ha senso **da qui in avanti**, sul
catalogo nuovo, dove Maren Ashcroft ha gia' tre libri coerenti fra loro (Spellbook, Winter
Term, Coven). I tre vecchi sono di altre nicchie e restano quello che sono.

**Se invece vuoi unificare, dimmelo e lo faccio in dieci minuti** (3 modifiche + 3
riconsegne). Ma decidilo **prima** di aprire KDP.

---

## PARTE 1 — I tre libri pronti da caricare adesso

Nessuno dei tre richiede altro lavoro. Verdetto `pubblicabile: true`, zero bloccanti.

### 1. The Ninth Winter — 119 pagine

| Campo KDP | Valore |
|---|---|
| Titolo | `The Ninth Winter` |
| Sottotitolo | `An Amish Suspense Novel` |
| Autore | `Rebecca Miller` *(vedi decisione sopra)* |
| Prezzo | **$12.99** (sopra $9.99 = royalty 60% sul cartaceo) |
| Trim size | 6.0 x 9.0 in |

**Cartella:** `LIBRI/libri_pronti/The_Ninth_Winter/`
**File da caricare:** `The_Ninth_Winter.pdf` (interno) · `Cover_The_Ninth_Winter.png` (copertina)
**Descrizione, 7 keyword, 3 categorie, 3 codici BISAC, bio autore e descrizione HTML:**
tutto pronto da copiare in `KDP_METADATA.txt` nella stessa cartella. La versione HTML si
incolla cosi' com'e' nel campo descrizione di KDP.

### 2. The Quiet Hours — 118 pagine

| Campo KDP | Valore |
|---|---|
| Titolo | `The Quiet Hours` |
| Sottotitolo | `A Psychological Thriller with a Twist You Won't See Coming` |
| Autore | `Digital Empire` *(vedi decisione sopra)* |
| Prezzo | **$11.99** |
| Trim size | 6.0 x 9.0 in |

**Cartella:** `LIBRI/libri_pronti/The_Quiet_Hours/`
**File:** `The_Quiet_Hours.pdf` · `Cover_The_Quiet_Hours.png`

### 3. The Second-Hand Spellbook — 119 pagine

| Campo KDP | Valore |
|---|---|
| Titolo | `The Second-Hand Spellbook` |
| Sottotitolo | `A Cozy Fantasy Novel` |
| Autore | `Maren Ashcroft` |
| Prezzo | **$13.99** |
| Trim size | 6.0 x 9.0 in |

**Cartella:** `LIBRI/libri_pronti/The_Second-Hand_Spellbook/`
**File:** `The_Second-Hand_Spellbook.pdf` · `Cover_The_Second-Hand_Spellbook.png`

---

## PARTE 2 — Dopo ogni caricamento, un comando

Appena KDP assegna l'ASIN, per **ogni** libro:

```bash
cd "company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente"

python -m engine.kdp pubblicato the-ninth-winter          --asin B0XXXXXXXX --prezzo 12.99
python -m engine.kdp pubblicato the-quiet-hours           --asin B0XXXXXXXX --prezzo 11.99
python -m engine.kdp pubblicato the-second-hand-spellbook --asin B0XXXXXXXX --prezzo 13.99
```

**Non e' un passaggio burocratico.** Quel comando archivia il pacchetto in
`libri_pubblicati/`, ci copia dentro i sorgenti verificandoli byte per byte, registra ASIN e
prezzo, **aggiunge il libro alla nicchia del catalogo** e chiude l'argomento in magazzino.
Finche' non lo lanci, ogni libro nuovo esce senza sapere che gli altri esistono: e' il motivo
per cui la pagina "Also by" e' vuota su tutti e tre.

---

## PARTE 3 — I due libri che aspettano solo una copertina

Verdetto `pubblicabile: false` con **un solo bloccante**: manca l'immagine.

| Libro | Pagine | Prompt gia' pronto in |
|---|---|---|
| Proof of Murder | 116 | `LIBRI/libri_pronti/Proof_of_Murder/COPERTINA-PROMPT.md` |
| The Winter Term | 116 | `LIBRI/libri_pronti/The_Winter_Term/COPERTINA-PROMPT.md` |

I prompt sono completi: scena, luce, palette, stile, composizione e **il testo del titolo
lettera per lettera**. Si danno a un generatore di immagini cosi' come sono. Poi:

```bash
python -m engine.kdp consegna proof-of-murder --cover <file.png>
python -m engine.kdp consegna the-winter-term --cover <file.png>
```

Il codice porta l'immagine a norma KDP (2:3, 1800x2700) **senza riscriverci sopra il titolo**,
perche' il titolo lo ha gia' disegnato il modello seguendo il prompt. Se l'immagine tornasse
senza testo, e solo in quel caso, si aggiunge `--scrivi-titolo`.

Dopo la consegna il verdetto diventa `pubblicabile: true` e i due libri entrano nella Parte 1.

---

## Verifica finale, quando hai finito

```bash
python -m engine.kdp stato          # deve mostrare i libri archiviati, non piu' in lavorazione
ls LIBRI/libri_pubblicati/          # non deve contenere solo .gitkeep
```

Al primo ASIN registrato **FIX-1 si chiude** e TASK-KDP-FIX-W2 passa da `in_corso` a `fatto`.
