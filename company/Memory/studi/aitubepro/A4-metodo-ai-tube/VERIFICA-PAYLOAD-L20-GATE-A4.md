---
Tipo: VERIFICA
Stato: Chiuso
Autore: Emperator (ricerca diretta, non sentinella)
Data: 2026-09-07
---

# Verifica payload Fliki — le tre domande assegnate al gate A4 da L20

Mandato: le "tre verifiche nuove contro il payload reale" assegnate al gate A4 da
`L20-aggiornamento-fliki/report.md` §6 e mai chiuse (restate aperte in `REPORT-CATEGORIA.md` §6
anche dopo CP-20260907-JVY2). **Non richiedono una sentinella sul video**: sono domande sull'API
reale, non sul corso. Fonte: documentazione ufficiale `developer.fliki.ai`, letta live (non dal
client `fliki_client.py`, che riflette solo cio' che GIA' usiamo — leggere il nostro codice
avrebbe risposto "cosa facciamo", non "cosa si puo' fare"). Ogni campo sotto e' stato letto
**due volte, con prompt diversi**, su pagine diverse (`/docs/api/generate/video` due letture
indipendenti + riscontro incrociato) prima di essere dato per accertato.

---

## Le tre risposte

| # | domanda | risposta | prova |
|---|---|---|---|
| 1 | SFX generati esistono via API? | **SÌ** | campo `generateSfx` (boolean) in `POST /v1/generate/video`, doc ufficiale: *"Automatically generate contextual sound effects for each scene"* |
| 2 | timing per-media (inizio/fine in secondi su un layer) è supportato? | **NO** | non esiste nello schema documentato del payload. Resta vero: una scena = i suoi media, nessun controllo fine come nell'editor |
| 3 | il tetto di 50 scene vale anche via API? | **NON VERIFICABILE DALLO SCHEMA** | nessuna menzione di limiti di scena in `/docs/api/generate/video` né in `/docs/api/generate/status`. Puo' essere un vincolo di piano applicato silenziosamente in fase di generazione (come i minuti, vedi `fliki_client.py:312-318` sul campo `duration`) — non escludibile senza una chiamata reale, che costa credito. **Resta aperta**, a differenza delle prime due: nessuna chiamata di prova fatta oggi. |

## ⭐ La scoperta che nessuna delle tre domande cercava

Leggendo lo schema completo per rispondere (tabella intera, non i tre campi cercati), **il payload
reale ha un campo che il nostro codice non manda mai**: `bgMusicVolume` (number, 0-100,
*"Background music volume from 0 (muted) to 100 (full)"*).

Questo non è un dettaglio minore: **A4-L20-01** (registrata, applicata, condizione 4 del gate
citata come "il risultato singolo più utile" di tutta la categoria A4) dice *"nel nostro payload
non esiste un campo musica [...] il criterio Bilanciamento Volumi è INAPPLICABILE"*. La prova
citata a suo tempo era la lettura di `fliki_client.py:252` — **corretta**, quel campo non c'è nel
payload che **costruiamo noi**. Ma l'API lo accetta. La regola A4-L20-01 resta vera nella sua
premessa stretta (il NOSTRO payload di oggi non ha musica) e nella sua conclusione operativa (il
criterio del gate resta inapplicabile finché non decidiamo di mandarlo) — **ma la ragione è una
scelta non ancora fatta, non un limite dell'API.** La sfumatura conta: "non possiamo" e "non
abbiamo ancora deciso" sono due frasi diverse, e la seconda va scritta prima che qualcuno la legga
come la prima.

**Non toccato `fliki_client.py` oggi** — ADR-029 (citato in `schema.py`): *"il motore si tocca
solo a gate di categoria."* A6 non è ancora chiuso. Due candidati nuovi in coda al prossimo gate
binario B, non applicati ora:

- **aggiungere `generateSfx: true`** al payload — SFX automatici per scena, gratis via API (nessun
  costo extra dichiarato nella doc oltre alla generazione stessa);
- **valutare `bgMusicVolume`** — decisione di prodotto, non solo tecnica: significa che i video
  POSSONO avere musica di sottofondo, cosa che oggi la fabbrica non fa per scelta implicita
  mai dichiarata come tale. Serve un ascolto A/B prima di attivarlo su un canale vero (stesso
  principio della verifica A4-L04-04: non si crede, si ascolta).

## Esito sul gate A4

**Le tre verifiche di L20 sono chiuse** (due risposte accertate, una dichiarata non verificabile
senza spesa reale — onesto, non forzato). `REPORT-CATEGORIA.md` §6 aggiornato di conseguenza.
Non riapre il gate A4 (già chiuso 6/7 in CP-20260907-JVY2, condizione 4 ferma sul video di prova
che resta decisione di Max): questa era conoscenza mancante fuori dal conteggio delle 7
condizioni, non una di esse.

**Restano aperte, invariate:** il tempo per video (`A4-L05-04`) e il campo `YouTube channel
ID(s)` su Fliki (`A4-L19-01`, gratis, 5 minuti, richiede l'interfaccia Fliki).
