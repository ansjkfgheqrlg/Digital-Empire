# SOP — Scrivere e pubblicare un libro KDP

> **Questo file non contiene più la procedura.** La procedura vive in **UN SOLO POSTO**:
> [`.claude/skills/libro/SKILL.md`](.claude/skills/libro/SKILL.md) — la skill `/libro`, cioè
> quella che viene *eseguita*.
>
> **Perché (2026-08-23).** La stessa procedura era scritta per esteso in tre file, e i tre
> file si erano messi a dire cose diverse:
>
> | | SKILL (eseguita) | SOP | ARCHITETTURA |
> |---|---|---|---|
> | parole per capitolo | **1600** | 1650 | 1650 |
> | capitoli per blocco | **8** | 4-6 | 4-6 |
> | `kdp blocco` (il gate) | 3 volte | **mai nominato** | **mai nominato** |
>
> Il gate che ferma i difetti al capitolo 8 invece che al 24 — il pezzo più importante
> costruito il 19 agosto — non esisteva in due documenti su tre. Un documento che mente è
> peggio di un documento che manca: chi riprende segue quello sbagliato in buona fede.
>
> Da qui in avanti: **la procedura si scrive nella skill**, l'architettura del codice in
> [`ARCHITETTURA.md`](ARCHITETTURA.md), e questo file tiene solo i comandi.

---

## In due righe

Il libro lo scrive **Claude in sessione**. Il codice non chiama nessun modello: misura le
nicchie, impagina, conta le pagine vere sul PDF, valida, impacchetta (cartaceo **e** ebook).
Gael genera la copertina e carica su KDP.

Tre tentativi di far scrivere i libri a un programma sono falliti (LM Arena → captcha ×2,
CLI di Claude → prompt troncati e limite di spesa); il codice di allora sta in
[`_archivio_automazione_modelli/`](_archivio_automazione_modelli/) con un LEGGIMI.

---

## Tutti i comandi, in ordine di flusso

```bash
# --- una volta, per iniziare -------------------------------------------------
pip install -r requirements.txt
python -m playwright install chromium

# --- FASE 0: magazzino argomenti (una volta a settimana) ---------------------
python -m engine.kdp nicchie --keywords "cozy mystery cats" "dark academia"
python -m engine.kdp magazzino                       # cosa c'è di pronto
python -m engine.kdp magazzino --aggiungi ricerca.json
python -m engine.kdp magazzino --prendi              # il prossimo da scrivere

# --- la nicchia del catalogo (si sceglie UNA volta) --------------------------
python -m engine.kdp nicchia-stato
python -m engine.kdp nicchia-scegli --keywords "cozy fantasy bookshop"
python -m engine.kdp nicchia-confronta --keywords "..." [--applica]

# --- FASI 1-4: il libro ------------------------------------------------------
python -m engine.kdp nuovo "<Titolo>" --nicchia "<nicchia>" [--autore "<nome>"]
python -m engine.kdp blocco <slug>       # DOPO OGNI BLOCCO DI CAPITOLI. <1 secondo.
python -m engine.kdp stato [slug]        # avanzamento + metriche di produzione

# --- FASE 5: il copy KDP (validato PRIMA di essere salvato) ------------------
python -m engine.kdp copy <slug> --file <copy.json>

# --- FASI 6-7: copertina e consegna -----------------------------------------
python -m engine.kdp consegna <slug> [--cover <copertina.png>] [--scrivi-titolo] [--forza]
python -m engine.kdp pacchetto <slug>    # i tre artefatti sono nella stessa cartella?

# --- FASE 8: quando il libro è su KDP ---------------------------------------
python -m engine.kdp pubblicato <slug> --asin B0XXXXXXXX [--prezzo 13.99]
```

**Exit code** (uguali per tutti): `0` ok · `1` non pubblicabile · `2` parametri sbagliati ·
`3` errore di sistema.

---

## Le sei regole non negoziabili

Sono le stesse della skill. Cinque su sei hanno una funzione che le fa rispettare e
**blocca**; la sesta è una decisione, non un controllo.

| | Regola | Chi la fa rispettare |
|---|---|---|
| 1 | Mai un libro sotto le **115 pagine reali** | `conta_pagine_pdf` + verdetto: blocca |
| 2 | Mai un capitolo identico o quasi a un altro | `valida_ripetizioni`: blocca |
| 3 | Mai copiare da un concorrente | nessun controllo: è una scelta di chi scrive |
| 4 | La coerenza viene da `outline.md` + `riassunti.md` | `kdp blocco`: blocca se i riassunti mancano |
| 5 | Il codice non chiama modelli | nessun import verso un modello in `engine/` |
| 6 | Un libro incompleto si finisce prima di aprirne un altro | `kdp stato` lo dice, `--forza` resta dichiarato |

E la regola che vale per tutto il testo stampato: **niente lineette lunghe** `—` `–` `--`
nella narrazione e nel copy KDP. `valida_lineette` e `valida_copy_kdp` bloccano entrambi.

---

## Se qualcosa non torna

- **`ModuleNotFoundError`** → `pip install -r requirements.txt` (l'elenco è completo e
  verificato; servono anche **Microsoft Word** per il PDF e **Tesseract** per l'OCR della
  copertina, che pip non installa).
- **"Pagine reali NON CONTATE"** → manca Word: senza PDF non si conta niente, e un numero
  non misurato non vale come misurato.
- **`validazione.json` con `verifiche_non_eseguite`** → quel controllo *non ha detto di sì*:
  non è un via libera, è un'assenza. Guarda cosa manca prima di caricare.
