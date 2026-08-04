# PreventivoForge — Analisi e Guida Semplificata

> Ultimo aggiornamento: 2026-07-01 · Stato: **funziona end-to-end LIVE sul primo annuncio reale.**

## 1. Cos'è e cosa fa?
**PreventivoForge** è un sistema automatico per le concessionarie che importano auto dalla Germania.

**Cosa fa in pratica?** Prende l'URL di un annuncio dal sito tedesco **mobile.de** e lo trasforma
in modo automatico in un **preventivo PDF in italiano**, pronto da consegnare al cliente finale.
Scarica le foto, traduce gli optional, ricalcola il prezzo di vendita e impagina il documento.

**Multi-concessionaria:** lo stesso programma serve tante concessionarie (ognuna ha la sua config
con prezzo/logo/contatti). La prima è **Prof Autocad**.

---

## 2. Come funziona il flusso (i 5 passaggi + i controlli)

1. **Scraping (recupero dati):** apre l'annuncio usando il **Google Chrome vero del PC** (collegato
   via "CDP"). Questo è fondamentale: mobile.de è protetto da **Akamai** (anti-bot) che blocca i
   robot normali → usando il browser reale su una connessione normale, il blocco **viene superato in
   automatico**. Il programma legge i dati veri dell'auto (nascosti nella pagina, in
   `window.__INITIAL_STATE__`) e scarica **tutte le foto**.
2. **Parsing (riordino dati):** trasforma i dati grezzi in uno standard pulito (file JSON) —
   marca, modello, km, potenza, prezzo esposto, 60+ optional, descrizione.
3. **Traduzione + Copy:** traduce optional e testo dal tedesco all'italiano (glossario dedicato,
   **senza AI a pagamento**) e scrive una descrizione commerciale.
4. **Pricing (prezzo finale):** applica la formula della concessionaria
   `finale = esposto × 1,03 + 1500 + 1500` e scrive il prezzo nel titolo.
5. **Creazione PDF:** impagina foto + testi + prezzo in un template elegante e salva il PDF.

Tra gli step ci sono **4 "Gate" (cancelli di sicurezza)**: controlli automatici che **bloccano** il
processo se qualcosa non va (foto mancanti, tedesco rimasto nella traduzione, prezzo non
ricalcolabile, PDF incompleto). Se un gate è rosso, il preventivo NON esce sbagliato: si ferma.

---

## 3. Gli agenti, la struttura e la gerarchia
Non è un unico programma, ma un **team di agenti specializzati** con una gerarchia chiara.

**Il capo — "Conductor" (regia):** il file `run.py`. Non traduce e non scarica: decide **chi** fa
**cosa** e **quando**, controlla i gate e gestisce i problemi (retry, fallback).

**Team operativo (i lavoratori):**
- `op-scraper` → visita mobile.de e scarica dati+foto (Step 1)
- `op-parser` → mette in ordine i dati grezzi (Step 2)
- `op-translator-copy` → traduce e migliora il testo (Step 3)
- `op-pricer` → calcola il prezzo finale (Step 4)
- `op-pdf-renderer` → impagina e crea il PDF (Step 5)

**Team di verifica (controllori qualità):**
- `qa-extraction-verifier` (Gate A) → controlla che non manchino foto/dati
- `qa-translation-verifier` (Gate B) → niente tedesco rimasto, niente optional inventati
- `qa-price-verifier` (Gate C) → ricalcola il prezzo da zero per conferma
- `qa-output-reviewer` (Gate D) → verifica che il PDF sia completo e impaginato bene

**Motore tecnico:** `implementation/cdp.py` pilota il Chrome del PC (scraping + stampa PDF) senza
dipendenze pesanti — così l'app finale sarà leggera e affidabile.

---

## 4. Come è organizzato il progetto (Split 50/50 Max ↔ Gael)
- **Half A (Max):** parte tecnica, acquisizione e numeri → scraping, parsing, pricing, regia
  `run.py`, motore browser (`cdp.py`), multi-tenant.
- **Half B (Gael):** parte qualità e visiva → traduzione, generazione PDF, i 4 controlli QA, e
  **la futura App con interfaccia grafica** (vedi §6).

Comunicano tramite un **Data Contract** (`schema/listing.schema.json`): Max lo riempie coi dati
base dell'auto, Gael lo usa per traduzione e PDF. È la "cucitura" congelata tra le due metà.

---

## 5. Come si usa OGGI (semplice)

**Modo super-semplice — 1 click:**
1. Doppio click su **`avvia-preventivo.bat`**
2. Incolli il **link mobile.de** e premi INVIO
3. Aspetti ~30 secondi → **il PDF si apre da solo** (lo trovi anche nella cartella `runs/`)

Si aprirà una finestra di Chrome durante il lavoro: è normale, lasciala fare.

**Modo tecnico (terminale), equivalente:**
```bash
python run.py "https://suchen.mobile.de/auto-inserat/..." --dealer prof-autocad
python run.py --list-dealers
python run.py --manual annuncio.html --foto ./foto   # fallback se serve
```

**Serve solo:** Google Chrome installato + connessione internet normale (di casa/ufficio).
**Non serve:** nessun account AI, nessuna chiave, nessun costo per preventivo (traduzione offline).

---

## 6. Prossimo passo — l'App .exe (in costruzione, la fa Gael)
Per consegnare il tutto al concessionario **senza fargli installare niente di tecnico** (né Python
né Claude), diventerà una **App Windows (.exe)**: la copi sul suo PC, doppio click, incolla il link,
esce il PDF. Interfaccia **minimal, argento, elegante e professionale**. In arrivo.

Consegna al cliente finale = **solo il PDF** (un file, via WhatsApp/email). Il programma resta sul PC,
non si "consegna".

---

## 7. Stato attuale (prova reale fatta)
✅ **Testato LIVE** sull'annuncio reale **Mercedes-Benz GLA 220** (mobile.de):
- 26 foto scaricate, dati reali, 0 residui tedeschi, 4 gate verdi.
- Prezzo: esposto **47.490 €** → finale **51.915 €** (×1,03 +1500 +1500).
- PDF **810 KB** con foto vere, ispezionato = perfetto.

**Il risultato finale** è sempre nella cartella `runs/<id>/`: log, dati e soprattutto il **PDF pronto**.
