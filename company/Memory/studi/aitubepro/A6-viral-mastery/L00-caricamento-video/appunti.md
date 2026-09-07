# Appunti — A6/L00 · «Caricamento video su YouTube»

- **Corso:** AI TUBE PRO · **Categoria:** YouTube Viral Mastery · **Ordine:** 0
- **Durata:** 12:05 · **id:** `3b60d164-1199-4aa3-88c0-a35b09c2d776` · parlato **1.801 parole**
- **Materiale:** 363 frame (1 ogni 2s) → **42 unici** (-88,4%) · **profondità ORO**
- **Strumento:** YouTube Studio (upload wizard completo, canale monetizzato mostrato dal vivo)

> Il valore non è "come si clicca Crea → Carica" (ovvio): è il **wizard di pubblicazione per
> intero**, confrontato riga per riga col nostro `youtube_uploader_playwright.py`. L'autocertificazione
> di idoneità per gli annunci (quasi 4 dei 12 minuti di lezione) **è già automatizzata** — lo
> scoprivo solo perché ho ricontrollato in inglese dopo un primo grep sbagliato in italiano.
> Il delta vero sono **tre elementi video mai automatizzati**: sottotitoli nativi, schermata
> finale, schede — verificati assenti in entrambe le lingue, non per una singola stringa mancata.

---

## 00:06 — 01:45 · Consiglio di canale monetizzato, poi il tasto Crea

Il relatore mostra il flusso con **un canale già monetizzato** (00:45) e consiglia esplicitamente
di partire con un canale monetizzato "soprattutto per questo genere di canali creati interamente
con l'intelligenza artificiale" (00:56) — vende un servizio di canali pronti, non riguarda la
nostra fabbrica (canali già di proprietà). Poi il tasto **Crea → Carica video**.

## 01:45 — 02:53 · Caricamento file e naming da SEO

`frame-070.png @ 2:18`, `frame-085.png @ 2:48` — l'esploratore file mostra il video sorgente
rinominato **prima** del caricamento con parole chiave: nell'esempio, il file si chiama
`vecchioni morte figlio` (visibile anche nel titolo del dialog di upload, `frame-101.png @ 3:20`).
Il consiglio esplicito (02:18): *"rinominare il file quando lo carichiamo, utilizzando la parola
chiave [...] non c'è una cosa specifica che ci fa capire che questa cosa funziona realmente ma
noi la facciamo praticamente su tutti i video"* — pratica dichiarata **non provata dal docente
stesso**, applicata per abitudine.

## 02:53 — 04:20 · Dettagli e Monetizzazione — tipi di annuncio

`frame-131.png @ 4:20` — tab **Monetizzazione**: tre tipi di annuncio (Display, **Annunci video
ignorabili** ✓, **Annunci video non ignorabili**) e tre posizionamenti (prima/durante/dopo il
video). Nel frame entrambi gli "annunci video" risultano selezionati. **Sono due controlli reali
distinti, ed entrambi già automatizzati da noi**, in due punti diversi: il dropdown "Monetization
On/Off" del wizard (`_gestisci_step_monetization`, riga 48 — sceglie "On", regola permanente di
Max 2026-09-03) e il toggle separato "Watch Page ads & YouTube Premium" (`ads_on_after_upload`,
riga 225, chiamato **dopo** l'upload perché Google lo lascia spento di default anche a
monetizzazione On — bug reale trovato il 2026-09-03). Non lo stesso controllo del tipo/posizione
annunci mostrato qui a schermo (quello resta ai default YouTube), ma zero delta sulla sostanza:
il video guadagna in entrambi i casi.

## 04:20 — 08:20 · ⭐ Idoneità per gli annunci — l'autocertificazione che non facciamo mai

Quasi **4 minuti su 12** — un terzo della lezione — sono questa schermata sola. `frame-146.png
@ 4:50` fino a `frame-251.png @ 8:20`: undici categorie, ciascuna con 2-3 livelli di gravità a
radio button, poi un checkbox finale "Nessuno dei contenuti precedenti" (`frame-251.png`):

| Categoria (schermo) | minuto |
|---|---|
| Linguaggio inappropriato | 04:50 |
| Contenuti per adulti | 05:03 |
| Violenza | 05:09 |
| Contenuti scioccanti | 06:04 |
| Azioni dannose o pericolose | 06:09 |
| Contenuti relativi a droghe per uso ricreativo | 06:26 |
| Incoraggiamento di comportamenti fraudolenti | 06:39 |
| Contenuti dispregiativi e che incitano all'odio | 06:51 |
| Contenuti correlati alle armi da fuoco | 07:04 |
| Eventi sensibili | 07:12 |
| Questioni controverse | 07:51 |

Parlato (08:06): *"se il vostro video rispecchia [...] tutti questi aspetti, dobbiamo mettere
nessuno dei contenuti precedenti [...] da questo momento il [...] youtube va a valutare se il mio
video può essere realmente o no monetizzato."* — l'autocertificazione è quindi **un prerequisito
dichiarato dal docente per la valutazione di monetizzazione**, non un passo opzionale.
**Correzione a un mio primo controllo sbagliato:** avevo grep-ato solo in italiano e concluso
"non gestito" — falso. `youtube_uploader_playwright.py:129-138` (`_gestisci_step_monetization`)
lo gestisce **in inglese** (la UI Studio automatizzata è in EN): rileva `"Inappropriate
language"` (prima categoria del questionario, la stessa vista a schermo qui) e clicca `"None of
the above"` — **esattamente la stessa mossa mostrata dal docente**, automatizzata. Zero delta su
questo punto, verificato leggendo il codice per intero, non per assenza di una singola stringa.

## 08:20 — 09:38 · Elementi video: sottotitoli, schermata finale, schede

- **Sottotitoli** (`frame-264.png @ 8:46`, `frame-265.png @ 8:48`): tre opzioni — carica file,
  "riconoscimento automatico" (quello che il relatore usa, 09:00: *"faccio fine, e in automatico
  youtube adesso [...] trascrive tutto"*), o scrittura manuale. **Sono sottotitoli YouTube nativi
  (traccia CC separata), non i sottotitoli karaoke bruciati nel video da Fliki** — due cose
  diverse: i nostri non hanno mai una traccia CC nativa.
- **Schermata finale** (`frame-274.png @ 9:06`, `frame-280.png @ 9:18`): editor con timeline,
  elementi trascinabili (video/iscriviti), durata configurabile sugli ultimi secondi.
- **Schede** (`frame-283.png @ 9:24`, `frame-285.png @ 9:28`): quattro tipi — Video, Playlist,
  Canale, Link — agganciabili a un punto preciso della timeline.

Nessuno dei tre è nel nostro uploader (grep vuoto su "scheda", "schermata final", "sottotitol" in
`youtube_uploader_playwright.py`).

## 09:38 — 11:37 · Dettagli finali, pubblico (bambini), controlli

- **Playlist** (`frame-305.png @ 10:08`): creazione al volo dal wizard stesso.
- **Pubblico — dichiarazione "per bambini"** (`frame-309.png @ 10:16`): radio "Sì, il contenuto è
  stato realizzato per bambini" / "No, non è stato creato per bambini" + "Limite di età
  (impostazioni avanzate)". **Questo il nostro uploader lo fa già** (`youtube_uploader_playwright.py`
  riga ~395-398, "Dichiarazione non per bambini — valore reale verificato dal vivo il
  2026-08-17") — nessun delta qui, confermato con prova nel codice, non assunto.
- **Licenza, incorporamento, categoria, commenti** (`frame-313.png @ 10:24`): licenza YouTube
  standard, "consenti incorporamento" ✓, categoria (Intrattenimento nell'esempio), moderazione
  commenti. Non verificato se il nostro uploader imposti questi campi o lasci i default YouTube.
- **Controlli automatici** (`frame-343.png @ 11:24`): due check pass/fail prima della
  pubblicazione — Copyright ("Nessun problema trovato") e **Idoneità per gli annunci** ("Nessun
  problema trovato") — quest'ultimo si popola comunque, anche senza aver compilato a mano la
  scheda "Idoneità" (coerente con l'ipotesi che YouTube scansioni il contenuto in autonomia in
  parallelo all'autocertificazione umana, ma **resta un'osservazione da un solo caso**, non una
  regola generale).

## 11:37 — 12:05 · Chiusura in bozza

Il relatore chiude la finestra senza pubblicare (11:31): *"la cosa che vi consiglio di fare [...]
ho privato o in elenco il video per poterlo modificare e programmare dopo"* — il video resta in
**Bozza** (`frame-351.png @ 11:40`, riga "Bozza" visibile nella lista contenuti). Titolo e
descrizione restano da scrivere: rimandato al video successivo del corso.
