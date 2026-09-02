# Coverage — max17-v05-jaye-agenticos

## Range guardato
Intero video, dal primo frame denso (`frame-001.png @0:00`) all'ultimo (`frame-649.png @21:36`), su una durata totale di 1298s (21m38).

## Copertura
- Frame densi estratti (1 ogni 2.0s): **649**
- Frame unici individuati da `scenes.md` (soglia 3.0, deduplica per cambio schermo reale): **181**
- Frame guardati in questo run: **181/181 (100%)**
- Frame duplicati esclusi (sotto soglia, identici a un frame già guardato): **468**

## Criterio di selezione
`scenes.md` è stato generato confrontando ogni frame denso col precedente e scartando (dall'elenco da guardare, non dal disco) quelli con un delta visivo sotto la soglia **3.0**. Il campo `delta` per ogni riga indica la distanza dal frame precedente nell'elenco unico; il campo `schermata dura` indica per quanto tempo quella schermata è rimasta stabile prima del cambio successivo. Nessun frame è stato cancellato dal disco — tutti i 649 restano in `frames/`.

## Metodo di lettura
I 181 frame sono stati letti in ordine cronologico, a blocchi di 5 (rispettando il limite di 5 immagini per messaggio), incrociando ogni frame con i sottotitoli `.en.vtt` (letti per intero nella porzione iniziale 0:00–2:37 per calibrare il tono/contesto) e con i capitoli dichiarati in `ingest.json`. Nessun frame è stato descritto "alla cieca": ogni riga del walkthrough in `video-analysis.md` cita il frame realmente osservato.

## Frame illeggibili o a bassa confidenza (dichiarati)
Nessun frame è tornato `[media removed: request limit]` in modo permanente in questo run (tutte le letture sono andate a buon fine all'unico tentativo). Tuttavia alcuni frame contengono testo a **risoluzione troppo bassa per una trascrizione certa al 100%** — marcati `inferito` in `atoms.json` e segnalati esplicitamente nel testo di `video-analysis.md`:

- `frame-011`–`frame-012` (@0:20–0:22): illustrazioni pixel-art, nessun testo tecnico da trascrivere oltre "FASTER"/"CHEAPER".
- `frame-064` (@2:06): prima vista d'insieme del Second Brain — etichette dei cluster leggibili solo parzialmente (poi confermate con precisione più avanti in frame-372/374).
- `frame-242` (@8:00): valori esadecimali dei colori del "brand book" (font molto piccolo) — trascritti a bassa confidenza.
- `frame-326`, `frame-336`, `frame-363`, `frame-384`, `frame-395` (@10:50–13:06): griglia cartelle root `C:\ROBO` in Esplora File — nomi di molte cartelle secondarie non leggibili con certezza; riportati solo i nomi chiaramente distinguibili.
- `frame-373`–`frame-374`, `frame-378`–`frame-381` (@12:24–12:40): conteggi numerici dei cluster dipartimentali del Second Brain (Content/Business/Personal/Community) — cifre riportate come indicative, non certe.
- `frame-387`, `frame-394`, `frame-400` (@12:52–13:18): contenuto di `CONTENT.md` — struttura ad alta confidenza, singole parole a media confidenza per la dimensione del font.
- `frame-577` (@19:12): `SKILL.md` di `search-connectors` — struttura e workflow ad alta confidenza, alcune frasi di dettaglio a media confidenza.

## Frame senza contenuto informativo aggiuntivo (talking-head / transizioni / loghi puri)
Un sottoinsieme dei 181 frame è puro flavor visivo (volto di Jay in camera, mascotte robot, logo RoboNuggets, dissolvenze) senza testo tecnico da trascrivere: `frame-004,005,014,015,016,021,022,023,071,098-104,154,221,222,248,251,290,293,294,296,298,302,303,305,333,363,395,412,420,423,426,428,434,436,469,471,478,500,508,523,524,525,533,575,592,610,614,618,619,620,623,631,639,643,645,646,647,649`. Sono comunque tutti stati aperti e verificati come "nessun nuovo contenuto" prima di essere classificati così — nessuno è stato saltato.

## Esito
**181/181 frame unici guardati, 0 non processati.** Copertura dichiarata completa rispetto alla lista di deduplica fornita in `scenes.md`.
