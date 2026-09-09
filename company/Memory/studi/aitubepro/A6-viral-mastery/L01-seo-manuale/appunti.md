# Appunti — A6/L01 · «SEO YouTube manuale operativo»

- **Corso:** AI TUBE PRO · **Categoria:** YouTube Viral Mastery · **Ordine:** 1
- **Durata:** 17:54 · **id:** `693226c5-040b-4117-bec5-16609efeedff` · parlato **2.477 parole**
- **Materiale:** 538 frame (1 ogni 2s) → **74 unici** (-86,2%), campione di 21 guardati (i più
  informativi: cambi di schermata con delta alto; i "presidio" su schermate di commenti/analytics
  laterali, ripetute più volte, non aggiungono sostanza nuova al metodo — dichiarato, non nascosto)
  · **profondità ORO**
- **Strumento:** ricerca YouTube nativa + estensione **vidIQ** (mistrascritta "BDQ" dal parlato) +
  ChatGPT per titolo/descrizione

> **Il raccolto migliore non è nel parlato: è nel nostro codice**, trovato confrontando cosa la
> lezione insegna su "sottotitoli = indicizzati da YouTube" con `seo_score.py`, che punteggia
> proprio quello — e scopre che il nostro motore **dichiara sempre `subtitles: true` senza
> averli mai creati**.

---

## 00:06 — 03:28 · Il metodo: keyword research nativa, non uno strumento a pagamento

Ricerca diretta nella barra di YouTube (`frame-036.png @ 1:10`, "notizie del giorno"): YouTube
autocompleta e posiziona in automatico i video con quella parola chiave nel titolo. Stesso
principio su "pasta alla carbonara" (`frame-057.png @ 1:52`): un video di 10 anni fa con
2,8M di visualizzazioni **grazie solo al posizionamento**, non alla viralità — distinzione
esplicita del docente (02:42): *"posizionamento"* vs *"diventare virali"* sono due leve diverse,
la prima costante nel tempo (evergreen), la seconda un picco.

## 03:28 — 08:00 · Copiare il metodo di un competitor con vidIQ

`frame-071.png @ 2:20` — ricerca "le 5 cose che mi hanno traumatizzato", **vidIQ** mostra un
punteggio SEO del video ("Overall score: Low 28/100") e suggerimenti di tag. Il docente apre un
canale competitor (`frame-108.png @ 3:34`, "Canale Gossip") e usa vidIQ per **vedere i tag di un
video specifico dei competitor** (08:00: *"grazie a vidIQ abbiamo la possibilità di vedere anche
i tag dei video"*) — non copia il titolo alla lettera (08:51: *"non voglio copiare interamente
il titolo del mio competitor [...] prendo spunto"*), riscrive: *"Rai in lutto a causa del grande
dolore..."* diventa *"Lutto in Rai, a causa del grande dolore..."* (09:03-09:14) — stesso senso,
parole riordinate.

## 08:00 — 10:16 · Tre hashtag + ChatGPT per titolo/descrizione

Tre hashtag inseriti in descrizione, scelti per rilevanza (09:37-09:59: "vecchioni", "rai",
"notizie di oggi"). Poi **ChatGPT** (`frame-180.png @ 5:58`) con prompt diretti: *"scrivimi un
titolo per questo testo"*, poi *"scrivimi 5 titoli"*, poi *"scrivimi il titolo più persuasivo che
puoi fare su questo testo"* (`frame-199.png @ 6:36`, risposta: *"Lutto inaspettato ferma la Rai:
perché non dovremmo mai dimenticare i nostri cari?"*), poi *"scrivimi una descrizione per un
video di YouTube che ha questo titolo"* (`frame-223.png @ 7:24`) — la descrizione generata viene
incollata **as-is** nel campo Dettagli (`frame-242.png @ 8:02`).

## 10:16 — 14:03 · ⭐ Playlist (almeno due), capitoli automatici, tag col nome canale

- **Playlist**: *"inserire il video in almeno due playlist, è consigliato da parte di YouTube"*
  (13:18-13:23) — non una raccomandazione mia, è **YouTube stesso** a consigliarlo secondo il
  docente. `frame-407.png @ 13:32` mostra **due playlist selezionate** ("Attualità" e "Notizie")
  nel pannello Playlist del wizard.
- **Capitoli automatici**: *"vi consiglio di mettere [i tempi] se non li fate voi manualmente"*
  (13:58-14:03) — YouTube li genera da solo se non forniti a mano, ma è meglio farli a mano.
- **Tag col nome del canale**: *"dobbiamo inserirlo anche nei tag [...] perché come tag avete
  inserito il nome del vostro canale"* così chi cerca il canale per nome trova tutti i video
  (16:32-17:04). `frame-445.png @ 14:48` mostra il pannello tag con chip multipli, comma-separated
  (confermato anche dal parlato @ 15:07-15:25: *"fatevi li fare sempre con la virgola"*).

## 14:03 — 17:54 · Punteggio finale, poi copertina

*"Come vedete qui c'è un punteggio [...] vi dice tutte le cose fondamentali che vanno fatte per
poter avere il massimo"* (17:07-17:18) — un pannello di checklist/punteggio nel wizard stesso
(non catturato in un frame dedicato in questo campione, ma descritto chiaramente a voce).
Chiusura: prossimo video sulla copertina — *"non vi consiglio mai di andare a pubblicare il video
senza copertina"* (17:35-17:43).

## ⭐ Confronto col nostro codice — il vero delta

`seo_score.py:26-31` pesa **5 elementi certificanti** (title 25 · description 25 · tags 20 ·
thumbnail 15 · **subtitles 15**), commento alla riga 30: *"presenti = indicizzati da YouTube"* —
cioè misura esattamente la traccia sottotitoli **nativa**, la stessa che L00 aveva già trovato
mai automatizzata (`A6-L00-01`). Cercato dove il campo `subtitles` viene popolato prima del
punteggio: **`apex7_orchestrator.py:1515`** lo scrive `True` **incondizionatamente**, a fianco di
`"thumbnail": not skip_thumbnail` (quello sì condizionale, quindi reale) — nessun controllo se
una traccia sottotitoli nativa esista davvero. **Il nostro gate SEO assegna sempre 15 punti su
100 per un elemento che non abbiamo mai creato.** Un secondo punto identico in `agents.py:222` è
**dichiaratamente un mock** ("dati finti, non usare in produzione") — non è lo stesso difetto,
è un simulatore che deve barare per definizione.

Non toccato il codice oggi (ADR-029, binario B solo a gate categoria) — regola registrata,
candidato per il gate A6.
