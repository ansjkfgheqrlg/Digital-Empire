# PreventivoForge - Analisi e Guida Semplificata

## 1. Cos'è e cosa fa?
**PreventivoForge** è un sistema automatizzato (un workflow multi-agente) progettato per le concessionarie d'auto che importano veicoli dalla Germania. 

**Cosa fa in pratica?** Prende l'URL di un annuncio di un'auto dal sito tedesco **mobile.de** e lo trasforma in modo totalmente automatico in un **preventivo in PDF in italiano**, pronto per essere consegnato al cliente finale. 

Fa da solo tutto il lavoro manuale noioso: scarica le foto, traduce gli optional, ricalcola il prezzo (aggiungendo costi di trasporto e ricarichi) e impagina il documento.

---

## 2. Come funziona il flusso (I 5 Passaggi)
Il lavoro è suddiviso in 5 step principali, eseguiti in sequenza:

1. **Scraping (Recupero Dati):** Il sistema visita l'annuncio su mobile.de, fa finta di essere un utente reale per non farsi bloccare (usando Playwright) e copia tutte le informazioni e le foto.
2. **Parsing (Riordino Dati):** Prende le informazioni disordinate appena scaricate e le converte in uno standard ordinato, pulito e facile da leggere (un file JSON strutturato).
3. **Traduzione e Copy:** Prende il testo e gli optional in tedesco e li traduce in un italiano corretto, ottimizzandone la forma per renderlo più "commerciale" e accattivante.
4. **Pricing (Prezzo Finale):** Applica le formule matematiche della concessionaria per calcolare il prezzo di vendita italiano (ad esempio: aggiunge il 3% al prezzo esposto, più 1500€ di costi fissi, ecc.).
5. **Creazione PDF:** Prende tutti questi elementi (foto, testi tradotti, prezzo finale) e li impagina all'interno di un template pulito ed elegante, salvando il PDF.

Tra questi step, ci sono dei **"Gate" (Cancelli di sicurezza)**: sono dei controlli di qualità intermedi che bloccano il processo se notano anomalie (es. "Mancano delle foto", oppure "Il prezzo non è stato calcolato bene").

---

## 3. Gli Agenti, la Struttura e la Gerarchia
Il sistema non è un unico grande programma, ma un team di **Agenti specializzati** che lavorano insieme, strutturati secondo una chiara gerarchia.

### Il Capo: Il "Conductor" (Regia)
*   **Chi è:** Il file `run.py` e il modulo *conductor*.
*   **Ruolo:** È il direttore dei lavori. Non traduce né scarica foto, ma decide **chi** fa **cosa** e **quando**. Avvia gli agenti uno dopo l'altro, controlla i cancelli di sicurezza (Gate) e gestisce gli eventuali problemi.

### Il Team Operativo (I Lavoratori)
Sono gli agenti che "si sporcano le mani" e fanno il lavoro vero e proprio:
*   **`op-scraper`**: L'esperto di ricerca. Visita il sito tedesco e scarica materiali (Step 1).
*   **`op-parser`**: L'archivista. Mette in ordine i dati grezzi (Step 2).
*   **`op-translator-copy`**: Il traduttore/venditore. Traduce e migliora il testo per vendere l'auto (Step 3).
*   **`op-pricer`**: Il ragioniere. Prende la calcolatrice e definisce il prezzo finale (Step 4).
*   **`op-pdf-renderer`**: Il grafico. Inserisce testi e foto nella grafica e stampa il documento (Step 5).

### Il Team di Verifica (I Controllori Qualità - QA)
Lavorano nei "Gate" e bloccano il lavoro del Team Operativo se non rispetta gli standard:
*   **`qa-extraction-verifier`** (Gate A): Controlla che lo scraper non si sia dimenticato foto o dati fondamentali.
*   **`qa-translation-verifier`** (Gate B): Si assicura che la traduzione sia perfetta, senza pezzi in tedesco dimenticati o accessori inventati.
*   **`qa-price-verifier`** (Gate C): Ricalcola il prezzo da zero per verificare che il ragioniere non si sia sbagliato.
*   **`qa-output-reviewer`** (Gate D): Guarda l'anteprima del PDF per controllare che sia tutto impaginato bene.

---

## 4. Come è organizzato il progetto (Lo Split 50/50)
Per gestire la complessità, lo sviluppo è stato diviso in due "metà" affidate a due figure distinte (Max e Gael):
*   **Half A (Max):** Si occupa della parte tecnica, di acquisizione e dei numeri. Gestisce Scraping, Parsing, Pricing e il direttore d'orchestra (`run.py`).
*   **Half B (Gael):** Si occupa della parte qualitativa e visiva. Gestisce la Traduzione, la generazione del PDF e coordina *tutti* gli agenti di controllo (il Team di Verifica QA).

Per comunicare tra di loro, usano un **Data Contract** (un file di base chiamato `listing.schema.json`). È come un modulo prestampato: Max lo riempie con i dati base dell'auto, Gael lo prende e lo usa per fare traduzioni e PDF.

---

## 5. Come va utilizzato
L'utilizzo è estremamente semplice e avviene tramite linea di comando (Terminale), dalla cartella del progetto:

**A. Uso Normale (Automatico):**
Basta dare al sistema il link dell'annuncio.
```bash
python run.py "https://suchen.mobile.de/auto-inserat/..."
```

**B. Per una concessionaria specifica:**
Se gestisci più clienti (multi-tenant), puoi specificare per chi è il preventivo.
```bash
python run.py "link-annuncio" --dealer prof-autocad
```

**C. Uso Manuale (Se il sito blocca il robot):**
Se *mobile.de* attiva dei sistemi anti-bot particolarmente aggressivi, l'utente può scaricare la pagina web e le foto manualmente, dicendo al programma di partire da lì saltando lo step di estrazione web.
```bash
python run.py --manual annuncio.html --foto ./cartella_foto
```

**Il Risultato Finale:**
Alla fine del processo, PreventivoForge crea una cartella `runs/` dove all'interno troverai log, dati temporanei, ma soprattutto il **PDF Finale**, pronto e impaginato perfettamente.
