Questa cartella è "Progetto Preventa" dentro il Reparto Produzione (vedi
[[Reparto_Produzione_Digital_Empire]] nella wiki). Lavori solo qui per i
contenuti — puoi leggere `../caroselli - agency/` solo per riusare il motore
Arena (import diretto di `ArenaAI/arena_generator.py` e `Core/browser_manager.py`,
MAI copiarli né modificarli — sono di proprietà del progetto Agency, REGOLE.md
di quella cartella resta valido per quella cartella).

## Contesto prodotto (Preventa)
Preventa vende ai concessionari auto: incolli il link di un annuncio (anche
estero, es. tedesco) e ottieni un PDF preventivo brandizzato con prezzi
bloccati dal titolare, pronto da mandare su WhatsApp — invece di 20-30 minuti
su Excel/gestionale mentre il cliente scrive già ad altri 3.
**Prezzo: €2.000 una tantum, nessun canone.**
Target primario: concessionari che fanno import (vedi filtro Fase 1,
[CP-20260803-005](../../../company/Memory/checkpoints/CP-20260803-005.md)) — il
dolore specifico è tradurre annunci esteri e ricalcolare a mano.
Dettaglio completo: [[Preventa_Logica_Completa_Metodo]].

## Differenza dal progetto Agency
Il progetto Agency (`../caroselli - agency/`) genera contenuto per
@digitalempireagency.e con CTA "scrivimi X in DM per una call" — funnel
inbound via Instagram. Preventa NON vende per DM: il canale di vendita reale è
outreach WhatsApp diretto (già costruito e operativo, vedi
`Outreach/preventa-maps-scraper/`). I caroselli Preventa servono per
**social proof / brand awareness** verso concessionari — CTA punta al sito
Preventa o invita a scrivere in DM per una demo, mai una vendita diretta in
slide.

## Colori brand reali (da `Crea siti/Preventa/index.html`, non inventati)
- `--blu: #101E3E` — primario, fiducia/automotive premium
- `--arancio: #FF4D00` — SOLO per CTA/accenti, mai oltre il 10% della slide
- `--ghiaccio: #F6F7F9` — sfondo chiaro alternativo
- Font: minuscolo, frasi compatte (stessa regola del progetto Agency — max
  ~12 parole per slide, niente muri di testo)

## Struttura carosello (3 slide, come Agency — stesso pattern collaudato)
1. **Hook** — pain point concreto (tempo perso / annunci esteri da tradurre)
2. **Soluzione** — come funziona Preventa in una frase (link annuncio → PDF
   pronto in italiano)
3. **CTA** — verso il sito/demo, non verso una vendita diretta

## GESTIONE ERRORI / CAPTCHA ARENA
Stesse regole del progetto Agency (vedi `../caroselli - agency/REGOLE.md`):
nuova chat se errore, mai screenshot dell'errore nelle slide, captcha solver
automatico, attesa progressiva se blocco persistente.

## Nessuna chat Arena dedicata serve (verificato nel codice, non assunto)
`arena_generator.py::generate_carousel_visuals()` riapre `https://arena.ai/` da
zero per ogni slide — non riusa una chat salvata. La continuità stilistica tra
slide viene dal ricaricare l'immagine della slide precedente come allegato, non
da un URL di chat. `ARENA_CHAT_URL` in `config.py` (Agency) serve solo a
`read_arena_chat.py` (studio one-shot di una chat passata), non alla
generazione. Quello che DAVVERO isola Preventa da Agency è dove finiscono i
file e quali immagini di riferimento vengono allegate alla slide 1 — gestito
in `config_preventa.py` (`LOCAL_DOWNLOAD_DIR`, `ALLEGATI_DIR`), applicato da
`orchestrator_preventa.py` sovrascrivendo questi due attributi sul modulo
`config` condiviso subito prima di chiamare il generatore.

Stesso account Arena, stesso browser profile persistente (`session_data`,
condiviso via import — mai duplicato, è una sessione autenticata reale).

## Bootstrap prima slide
`ALLEGATI_DIR` di Preventa parte vuoto (nessun carosello Preventa esiste
ancora): il primo run non ha immagini di riferimento da allegare, lo stile
viene descritto solo a parole nel prompt (colori/regole sopra). Il PNG della
slide 1 del primo carosello reale può poi essere copiato in `ALLEGATI_DIR` per
dare consistenza ai caroselli successivi.
