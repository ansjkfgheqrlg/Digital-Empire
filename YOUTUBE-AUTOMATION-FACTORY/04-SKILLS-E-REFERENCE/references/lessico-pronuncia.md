# Lessico di pronuncia — le parole che la voce sintetica sbaglia

> **Regola `A4-L03-03`** (studio AI TUBE PRO, lezione A4/L03, 2026-09-04).
> Questo file è **vivo**: cresce ad ogni errore trovato, e non si svuota mai.

## Perché esiste

Le voci sintetiche sbagliano sempre le stesse parole: i termini inglesi dentro una frase
italiana, i nomi propri, e gli accenti tonici (*iscrìviti* letto *iscrivìti*). L'errore non è
casuale — è **sistematico**: la stessa parola verrà sbagliata identica nel prossimo video, e nel
successivo, finché qualcuno non scrive da qualche parte come va letta.

Il buco che questo file chiude, misurato il 2026-09-04: `qa-audio-video` §7 ha l'ordine di
registrare gli errori di pronuncia in `memory/decisions`. In **125 decisioni registrate non ce
n'è nessuna sulla pronuncia**. Il giro esisteva sulla carta e non ha mai prodotto una riga: ogni
errore trovato moriva nel rapporto del video in cui era stato trovato.

## Come si usa (le due metà del giro)

**Chi genera** (`script-writer`, `video-producer`): prima di mandare il testo a Fliki, sostituisci
nel **testo dello script** ogni parola della colonna «si scrive» con la grafia della colonna «si
scrive per farla leggere bene». Si corregge nel testo, **non** nel pannello «Pronunciation»
dell'interfaccia Fliki: quel pannello è a mano, e una fabbrica che genera via API non lo apre mai
(`fliki-avanzato.md` §2 descrive una procedura che la nostra catena non esegue).

**Chi ascolta** (`qa-audio-video`): ogni volta che senti una parola letta male, **aggiungi una
riga qui sotto** con il minuto del video in cui l'hai sentita. Una correzione che resta nel
rapporto e non finisce in questa tabella si ripeterà identica.

## Il lessico

| si scrive | si legge male così | si scrive per farla leggere bene | trovata in | data |
|---|---|---|---|---|
| Cash Cow | *cash cow* all'inglese | `Cescau` | `fliki-avanzato.md` §2 (scheda) | prima del 2026-09-04 |
| VPH | *vi-pi-acca* | `Viu per ora` | `fliki-avanzato.md` §2 (scheda) | prima del 2026-09-04 |
| SEO | *se-o* incerto | `Seo` (all'italiana) oppure `Esse-E-O` | `fliki-avanzato.md` §2 (scheda) | prima del 2026-09-04 |
| Automation | *automation* all'inglese | `Automescion` | `fliki-avanzato.md` §2 (scheda) | prima del 2026-09-04 |
| Fliki | *flaiki* | `Flichi` | `fliki-avanzato.md` §2 (scheda) | prima del 2026-09-04 |

**Le cinque righe qui sopra vengono dalla scheda, non da un ascolto reale.** Sono un punto di
partenza, non un lessico: un lessico vero si riempie sentendo i nostri video. La prossima riga
deve avere un minuto e un video accanto.

## Perche' il pannello di Fliki non e' un'alternativa (A4-L19-02 - 2026-09-06)

Chiudo qui una speranza che L03 aveva lasciato aperta: *«e se le pronunce le configurassimo una
volta sola dentro Fliki, invece di riscriverle in ogni script?»*. **Non si puo', ed e' dimostrato
a schermo.**

Il pannello `More -> Pronunciation map` dichiara, testualmente:
**«Manage pronunciation of words ... to apply while generating audio for this video»**
(`frame-123.png @ 08:12`). Le tre conseguenze, in ordine di peso:

1. **Vale per UN video solo.** Non e' una configurazione di account: non si eredita fra progetti,
   e ogni video ripartirebbe da zero.
2. **Una generazione via API non la vede.** La nostra catena non apre mai il progetto: manda un
   payload e riceve un MP4.
3. **E' case-sensitive** (lo dice il pannello stesso): `Fliki` e `fliki` sarebbero due voci
   diverse, quindi anche a mano sarebbe una mappa fragile.

**Il docente del corso dice il contrario** — che le pronunce «rimangono salvate su Fliki». Vince
lo schermo (piano di studio, 6.4): quello che si legge nel pannello batte quello che si sente nel
parlato.

### Confermato, e peggiorato, da A4/L20 (A4-L20-03 · 2026-09-06)

Una seconda lezione, settantasei minuti sullo stesso strumento, dice **come** la mappa si propaga
davvero — e la risposta chiude l'ultimo spiraglio.

Il relatore ammette di non averla mai usata sul serio [40:54-41:24] e spiega che le pronunce
«restano» **solo se si lavora così**: ci si costruisce **un file campione, un demo**, e poi si fa
**duplica**. Nella domanda finale di una studentessa [71:52-73:41] lo dice ancora più chiaro:
correggere una pronuncia **sul file di lavoro non basta**, la stessa correzione va **incollata
anche sul file demo**, altrimenti i prossimi video non la ereditano.

**Cosa vuol dire per noi.** La propagazione non è una funzione: è **la duplicazione di un
progetto**. La nostra catena **non duplica nulla** — `fliki_client.py` crea ogni video da zero con
una chiamata. Quindi non solo la mappa vale per un video: **nei nostri video non si applica mai**,
nemmeno per eredità.

**Conclusione operativa: la correzione si fa nel TESTO dello script, con la tabella qui sopra.**
Non e' un ripiego in attesa di una via migliore: la via migliore non esiste.

## Le due famiglie di errore, e la cura

1. **Parola straniera in frase italiana** — si riscrive in grafia italiana (`Cescau`).
2. **Accento tonico sbagliato** — si sposta l'accento scrivendolo:
   *iscrìviti* invece di *iscriviti*. È il caso mostrato nella lezione, ed è quello che la voce
   sbaglia più spesso sui verbi con pronome attaccato (*iscrìviti*, *ascòltalo*, *guàrdalo*).

## Connessioni
- [[fliki-avanzato]] — pause, enfasi, velocità di narrazione
- [[qa-audio-video]] — chi trova gli errori e scrive qui
- [[script-writer]] — chi applica il lessico prima di generare
