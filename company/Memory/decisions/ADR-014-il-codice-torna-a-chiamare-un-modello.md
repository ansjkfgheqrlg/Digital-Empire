# ADR-014 — Il codice del flusso libro torna a chiamare un modello (tentativo #4, con i guasti chiusi)

- **Data:** 2026-08-30
- **Stato:** ATTIVO
- **Decisori:** richiesta esplicita di Max ("un comando che avvia la produzione di un libro
  completo senza dovermi chiedere niente dopo che lo avvio"); scelta del modello e del tetto
  di spesa fatta da Max in sessione.
- **Ribalta:** la decisione del 2026-08-15 (`_archivio_automazione_modelli/LEGGIMI.md`):
  *"il libro lo scrive Claude in sessione; il codice non chiama nessun modello"*.

## Contesto — perché quella decisione era giusta allora

Il progetto aveva provato **tre volte** a far scrivere i libri a un programma, fallendo sempre:

1. **LM Arena via Playwright** (lug-ago) — captcha. Il capitolo 1 andato in captcha **4 volte
   di fila**, ogni volta risolto a mano e ripresentatosi.
2. **Claude Code CLI + Haiku** (13 ago) — due guasti silenziosi in fila: il wrapper
   `claude.CMD` **troncava i prompt multiriga alla prima riga** *e* faceva **sparire
   `--model`**, quindi si pagava un modello diverso da quello scelto. Poi il piano ha
   raggiunto il **limite di spesa mensile**.
3. **Di nuovo LM Arena** (15 ago) — fermato prima di ripercorrere la stessa strada.

Nessuno dei tre ha mai prodotto un libro finito. L'unico libro completo di allora
(*The Quiet Hours*) era stato scritto in sessione, a costo esterno zero.

## Decisione

Il codice torna a chiamare un modello, **ma solo perché i tre guasti sono stati verificati
chiusi uno per uno il 2026-08-30**, con prove eseguite, non con la speranza che "stavolta
vada meglio":

| Guasto storico | Come è stato chiuso | Prova |
|---|---|---|
| captcha | non applicabile: nessun browser, si chiama la CLI | — |
| prompt multiriga troncati | il prompt si passa da **stdin**, mai in argv | prompt di 3 righe, risposta esatta dalla riga 3 |
| modello sbagliato pagato in silenzio | si passa l'**ID esplicito** e si **verifica** `modelUsage` nella risposta | `--model sonnet` restituisce `claude-sonnet-4-6`, **non** Sonnet 5: l'alias mente ancora oggi |
| limite di spesa sfondato | `--output-format json` dà `total_cost_usd` per chiamata; `Budget.verifica()` gira **prima** di ogni chiamata e solleva | test: budget esaurito → `BudgetSuperato`, flusso fermo e lavoro salvato |

**Scelte operative** (Max, 2026-08-30): modello **`claude-sonnet-5`** (ID esplicito),
tetto **5 $ per libro**.

**Scrittura a blocchi, non a capitolo.** Misurato: ogni invocazione di `claude -p` costa
~0,08-0,11 $ di solo harness. A capitolo singolo sarebbero ~2,4 $ di sola tassa su 24
capitoli; a blocchi di 4 diventano ~0,5 $. Il blocco è anche l'unità che il gate già usa.

**Il gate resta il padrone.** Dopo ogni blocco gira `kdp blocco`: se boccia, il flusso
**riscrive quel blocco** passando al modello il motivo esatto del rifiuto, fino a 3 volte.
Non tira mai dritto. È la differenza fra correggere 4 capitoli e correggerne 24.

## Cosa NON cambia

- **La scrittura in sessione resta possibile e valida.** `kdp auto` è una strada in più,
  non una sostituzione: il flusso manuale (`nuovo` → capitoli scritti da Claude → `blocco`
  → `copy` → `consegna`) è intatto e non è stato toccato.
- **I due passi umani restano umani**: l'immagine di copertina (serve un generatore di
  immagini) e l'upload su KDP (irreversibile verso l'esterno).
- **La disciplina di catalogo vale anche qui.** `kdp auto` chiama `BookProject.crea`
  direttamente e quindi saltava il controllo nicchia di `kdp nuovo`: corretto. Non potendo
  chiedere niente dopo l'avvio, lo scarto dalla nicchia attiva non si vieta, si **dichiara**
  in `progetto.json`. B-018 resta aperto e questa decisione non lo chiude.

## Conseguenze

- Un libro costa ora **denaro misurabile** oltre che tempo. Il costo per libro va guardato
  in `kdp diagnosi`, che lo legge dal log reale delle chiamate e non da una stima.
- Se il tetto viene raggiunto, il libro resta **a metà ma salvato**: si riprende, non si
  ricomincia.
- La qualità del testo passa da Claude-in-sessione a Sonnet 5 via CLI. **Non è ancora
  misurata su un libro intero**: il primo libro prodotto così va letto da una persona prima
  di scalare a 5-10 libri/settimana.

## Alternative scartate

- **SDK Anthropic diretto** — tecnicamente migliore a regime (niente tassa di harness per
  chiamata, prompt caching sul contesto ripetuto: circa un terzo del costo), ma il
  2026-08-30 su questa macchina non esistevano né `ANTHROPIC_API_KEY`, né il pacchetto
  `anthropic`, né la CLI `ant`. Richiederebbe a Max di creare una chiave: non parte oggi.
  `ScrittoreClaudeCLI` ha un'interfaccia minima (`genera()`) apposta per essere sostituita.
- **Restare alla scrittura in sessione** — non soddisfa la richiesta ("senza dovermi chiedere
  niente"): un umano deve restare davanti per tutto il libro.
- **Haiku per il testo** — è il modello del fallimento del 13 agosto e su 40.000 parole di
  narrativa la resa cala molto. Scartato da Max.

## Contradiction-check

Nessun conflitto con ADR-001/002/005. Coerente con **ADR-003** (wrap, mai riscrittura): il
motore esistente non è stato toccato, `auto.py` lo orchestra e basta. Coerente con ADR-013
(gli artefatti pesanti non entrano nella storia git).

## Connessioni

- Archivio dei tre fallimenti: `_archivio_automazione_modelli/LEGGIMI.md`
- Referto del flusso: `python -m engine.kdp diagnosi`
- Le tre lezioni dell'archivio, ora in codice: `engine/scrittore.py`
