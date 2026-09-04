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

## Le due famiglie di errore, e la cura

1. **Parola straniera in frase italiana** — si riscrive in grafia italiana (`Cescau`).
2. **Accento tonico sbagliato** — si sposta l'accento scrivendolo:
   *iscrìviti* invece di *iscriviti*. È il caso mostrato nella lezione, ed è quello che la voce
   sbaglia più spesso sui verbi con pronome attaccato (*iscrìviti*, *ascòltalo*, *guàrdalo*).

## Connessioni
- [[fliki-avanzato]] — pause, enfasi, velocità di narrazione
- [[qa-audio-video]] — chi trova gli errori e scrive qui
- [[script-writer]] — chi applica il lessico prima di generare
