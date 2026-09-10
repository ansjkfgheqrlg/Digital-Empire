# Appunti — A6/L06 · «Automazione della pubblicazione Video su YouTube»

- **Corso:** AI TUBE PRO · **Categoria:** YouTube Viral Mastery · **Ordine nel corso:** 6
- **Durata:** 07:20 · **id:** `a48bfb41-2b71-4be9-a9a4-4141c6ee0e23` · parlato **1.164 parole**
- **Materiale:** 226 frame densi (1 ogni 2s) → **27 unici** (-88,1%), guardati **7** (tutorial a
  schermo condiviso su YouTube Studio, profondità ORO)
- **Docente:** Pietro Gangemi

---

## 00:06 — 01:16 · Quando ha senso automatizzare la pubblicazione

Consiglio in apertura: se si sta avviando il **primo** canale, seguirlo manualmente il più
possibile; la programmazione automatica ha senso quando **ci sono già tanti video prodotti** da
smaltire, o con più canali attivi (00:17-00:37). Motivazione generale (00:37-01:12): pubblicare
programmato evita di dover stare al computer al momento esatto della pubblicazione — utile per
chi pubblica più volte al giorno ma ha un altro lavoro.

## 01:16 — 02:05 · Caricamento multiplo + stato bozza

Dimostrazione: caricamento di più video insieme (01:16-01:39), che finiscono automaticamente in
stato **"Bozza"** nell'elenco contenuti (01:44). `frame-052.png @ 1:42` mostra la finestra
"Caricamento di 2 su 4" con 4 video in coda di upload — coerente col piano editoriale citato (due
video al giorno). Prima di programmare, resta comunque necessario completare copertina, titolo,
playlist, descrizione, tag per ciascun video (01:48-01:59, "tutte quelle cose che abbiamo già
fatto").

## 02:05 — 03:31 · ⭐ Il vero contenuto tecnico: orario in base agli analytics del pubblico

Passaggio centrale della lezione: *"su YouTube Studio [...] se noi andiamo su Analytics nella
sezione pubblico, abbiamo la possibilità di vedere a che ora e in quale giorno il nostro pubblico
è presente"* (02:15-02:30). Metodo: **scheduling orario data-driven, non a intuito** — se
l'analytics mostra pubblico presente alle 10:00 e alle 18:00, si programma per quegli orari;
se un giorno (l'esempio è la domenica) il pubblico si collega solo la sera, si programma **solo
la sera** quel giorno specifico (02:39-02:58). Motivazione (03:04-03:19): *"una delle cose più
importanti che guarda YouTube quando pubblichiamo un video è l'interazione nelle prime ore [...]
se pubblichiamo quando c'è tanta gente collegata [...] abbiamo più probabilità di fare più
visualizzazioni"* — lo scheduling ottimale serve a massimizzare il segnale di interazione
immediata che l'algoritmo usa per decidere quanto spingere il video.

## 03:31 — 04:57 · Come si programma (wizard nativo YouTube Studio)

Percorso pratico: scheda **Visibilità** → tasto **Programmazione** → si sceglie data (esempio "25
aprile") e ora (esempio 10:00, poi un secondo video lo stesso giorno alle 18:00) (03:44-04:26).
`frame-125.png @ 4:08` e `frame-140.png @ 4:38` mostrano l'elenco Contenuti del canale con due
righe in stato **"Programmato"** (colonna Visibilità), con data "29 apr 2023" e "21 apr 2023"
programmate — coerente col parlato, la funzione è quella nativa dello stepper "Visibilità" di
YouTube Studio, non uno strumento esterno.

## 04:57 — 06:14 · Pubblicare manuale vs programmato — differenza minima, batch consigliato

Chiarimento (05:03-05:41): pubblicare manualmente ha un solo vantaggio pratico — poter
condividere subito sui social e mettere il primo commento nello stesso momento (esistono comunque
"strumenti appositi che fanno [la condivisione] in automatico", non nominati). A parte questo, la
differenza in termini di visualizzazioni fra pubblicazione manuale e programmata è dichiarata
**minima**, e il rischio di errore di YouTube nella pubblicazione automatica è stimato **0,01%**
("nel 99,99% dei casi non sbaglia"). Consiglio operativo (05:41-06:02): non caricare/pubblicare
giorno per giorno, ma **dedicare 2-3 ore una volta e programmare tutta la settimana**.

## 06:14 — 07:20 · Eccezione: contenuto flash/trend va pubblicato subito, non programmato

*"Se ci sono dei video che devi fare extra [...] li puoi pubblicare in quel momento specifico"*
(06:14-06:20) — esempio: un canale di notizie che deve coprire un evento improvviso (06:24-06:44,
"muore un personaggio famoso") **non può essere programmato per la settimana dopo**, va
pubblicato subito. La pre-programmazione del contenuto evergreen/pianificato lascia comunque
spazio per inserire contenuti trend fuori piano, spostando in avanti un contenuto già
programmato (06:47-06:57). Chiusura con rimando alle prossime due lezioni (guadagni, community).

---

## Confronto col nostro codice

`YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py:432-451`
imposta **sempre** la visibilità a **"Privato"** ("Impostazione visibilità (Privato per
sicurezza)..."), incondizionatamente. Verificato con grep: **zero** occorrenze di scheduling,
data/ora di programmazione, o lettura degli analytics "quando è online il pubblico". La fabbrica
non pubblica mai, né subito né programmato — coerente con `BASELINE.md` §4 ("solo 2 video su 8
hanno una destinazione tracciata") e con `ADR-016` (Ultimo Metro: prodotto e mai pubblicato). Vedi
`report.md` per il delta completo — è il gap più operativamente pesante fra le quattro lezioni di
questo giro, perché tocca esattamente il collo di bottiglia già misurato.
