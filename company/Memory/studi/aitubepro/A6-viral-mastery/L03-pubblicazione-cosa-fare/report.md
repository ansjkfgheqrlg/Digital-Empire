# Report — A6/L03 «Pubblicazione Video + cosa da fare» (4:04)

- **Durata:** 4:04 · ~510 parole · **profondità ORO** (breve ma densa di procedura)
- **Letta:** parlato integrale + 7/30 frame unici (campione motivato, vedi `frame-scelti.md`)
- **Rapporto grezzo:** [`appunti.md`](appunti.md) · frame: [`frame-scelti.md`](frame-scelti.md)

---

## 1. Cosa insegna

L'ultimo passo del wizard di pubblicazione (miniatura, verifica elementi video/playlist,
visibilità, pubblica) e poi — questo è il contenuto nuovo — quattro azioni da fare **subito dopo**
la pubblicazione: mettere like al proprio video, lasciare e mettere in evidenza (pin) un commento
pensato per generare risposte, mettere like al proprio commento, condividere il link su
Facebook/Twitter per segnalare a YouTube traffico esterno. Chiude con la personalizzazione del
canale: trailer per i non iscritti, video in primo piano per gli iscritti, entrambi aggiornabili
dopo ogni pubblicazione.

## 2. Cosa facciamo oggi

`youtube_uploader_playwright.py` copre il wizard fino alla pubblicazione (verificato in `A6-L00`
e arricchito da `A6-RC-01`: zero occorrenze di sottotitoli nativi, schermata finale, schede).
Verificato oggi con un grep mirato e diverso: **zero occorrenze** di "pin", "like", "commento",
"in evidenza" nello stesso script — lo script pubblica e si ferma, non esegue mai nessuna delle
azioni post-pubblicazione insegnate qui. Le uniche occorrenze di "facebook"/"social" nella
cartella `02-AUTOMAZIONI-E-SCRIPTS` sono in file di pianificazione editoriale
(`assemble_piano_editoriale.py`, `generate_calendario_md.py`), non in un passo automatico legato
all'upload. Nessuno dei tre agenti di setup canale (`ytl-channel-architect`, `ytl-brand-designer`,
`ytl-channel-seo`) tratta trailer/video in primo piano come passo ricorrente.

## 3. Delta

**Il delta è un buco diverso da quello già a registro con `A6-RC-01`.** `A6-RC-01` riguarda i tab
del wizard di caricamento (sottotitoli, schermata finale, schede, playlist) — un problema "dentro"
la pubblicazione. Questa lezione mostra che il lavoro **non finisce quando il video diventa
pubblico**: ci sono quattro azioni immediate di engagement (like, commento pinnato, like al
commento, condivisione social) che oggi non hanno alcuna automazione, e un passo periodico di
manutenzione canale (trailer/video in primo piano) mai messo a playbook. Verificato con codice,
non assunto: grep dedicato conferma zero righe sull'argomento in
`youtube_uploader_playwright.py`.

Un dettaglio minore ma onesto (dichiarato dal docente stesso): la "scheda" (card) creata nel
video risulta ancora vuota al momento della pubblicazione (01:03-01:10) — coerente con
`A6-L00-01`, non un delta nuovo.

## 4. Conflitti

Nessuno. Le azioni insegnate non contraddicono nulla della fabbrica: sono passi mancanti, non
passi da correggere.

## 5. Regole estratte

Tre: una **costruttiva** (le azioni post-pubblicazione, priorità medio-alta perché è free reach
senza costo), una **costruttiva** minore (manutenzione canale), una procedurale di conferma.

| id | regola in una riga | tipo | tocca |
|---|---|---|---|
| `A6-L03-01` | Costruire un passo post-pubblicazione nell'uploader: self-like del video, pubblicazione e pin di un commento con CTA a rispondere, like al proprio commento | **funzione** — costruisci | `02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py` |
| `A6-L03-02` | Aggiungere alla manutenzione periodica del canale l'aggiornamento di trailer (per non iscritti) e video in primo piano (per iscritti) dopo ogni pubblicazione rilevante | **funzione** — costruisci | `03-AGENTI-E-RUOLI/operatori/ytl-channel-architect.md` |
| `A6-L03-03` | Conferma: assegnare almeno due playlist a ogni video prima della pubblicazione, coerente con `A6-L01-02` | procedura | `04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md` |

## 6. Applicabilità

**Medio-alta su `A6-L03-01`**: leva a costo zero (nessun credito API, solo azioni sulla stessa
pagina appena pubblicata) con un meccanismo dichiarato e plausibile (segnale di engagement precoce
all'algoritmo) — priorità dietro `A6-L04-01`/`A6-L07-01` (Analytics/ricavi) perché quelle sbloccano
altri due buchi già a registro, ma comunque a basso rischio da implementare. **Media su
`A6-L03-02`**: utile ma periodica, non per-video — si presta a un job separato, non all'uploader.
**Bassa su `A6-L03-03`**: già coperta in sostanza da `A6-L01-02`, qui solo confermata con un
frame aggiuntivo (`frame-025.png`).
