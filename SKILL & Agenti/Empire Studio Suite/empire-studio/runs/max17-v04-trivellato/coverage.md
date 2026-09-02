# Coverage — max17-v04-trivellato

## Range frame guardati
Tutti i **105 frame unici** elencati in `scenes.md` sono stati guardati, in ordine cronologico, dal primo all'ultimo:

`frame-001` → `frame-002` → `frame-003` → `frame-004` → `frame-007` → `frame-008` → `frame-009` → `frame-010` → `frame-011` → `frame-012` → `frame-014` → `frame-015` → `frame-018` → `frame-019` → `frame-022` → `frame-023` → `frame-024` → `frame-025` → `frame-026` → `frame-027` → `frame-028` → `frame-029` → `frame-030` → `frame-031` → `frame-032` → `frame-034` → `frame-035` → `frame-036` → `frame-038` → `frame-039` → `frame-040` → `frame-041` → `frame-044` → `frame-045` → `frame-064` → `frame-077` → `frame-078` → `frame-079` → `frame-082` → `frame-083` → `frame-096` → `frame-106` → `frame-107` → `frame-108` → `frame-109` → `frame-111` → `frame-112` → `frame-114` → `frame-116` → `frame-118` → `frame-119` → `frame-120` → `frame-135` → `frame-149` → `frame-201` → `frame-239` → `frame-240` → `frame-241` → `frame-269` → `frame-270` → `frame-279` → `frame-280` → `frame-281` → `frame-289` → `frame-290` → `frame-295` → `frame-296` → `frame-297` → `frame-298` → `frame-299` → `frame-313` → `frame-315` → `frame-316` → `frame-328` → `frame-329` → `frame-339` → `frame-353` → `frame-355` → `frame-356` → `frame-360` → `frame-361` → `frame-381` → `frame-382` → `frame-397` → `frame-398` → `frame-400` → `frame-401` → `frame-403` → `frame-404` → `frame-419` → `frame-420` → `frame-435` → `frame-441` → `frame-443` → `frame-444` → `frame-474` → `frame-476` → `frame-477` → `frame-513` → `frame-514` → `frame-515` → `frame-516` → `frame-524` → `frame-558` → `frame-565`

**Copertura: 105/105 unici (100%)** — copertura temporale continua da 0:00 a 18:48 (fine video a 18:49).

## Criterio di selezione
- Frame densi estratti ogni 2.0s dal video sorgente: **565 totali**.
- Deduplicazione per soglia di cambiamento visivo **3.0**: frame sotto soglia rispetto al precedente frame "unico" sono considerati identici e non elencati (ma **non cancellati** — restano tutti in `frames/`).
- Frame unici risultanti da guardare: **105** (riduzione dell'81.4% rispetto ai 565 densi).
- La colonna "schermata dura" di `scenes.md` indica per quanti secondi ogni schermata resta stabile prima del prossimo cambio rilevato — usata qui per capire dove l'autore si ferma a spiegare (es. hold di 104s a `frame-149`, 76s a `frame-201`, 72s a `frame-477`, 68s a `frame-524`, tutti punti di spiegazione prolungata sulla board Miro).

## Fonte supplementare usata (dichiarata)
Contrariamente a quanto indicato nelle istruzioni originali ("non esiste transcript scaricato"), la run dir contiene effettivamente un file di sottotitoli auto-generati scaricato da yt-dlp (`-gq8euRvNR4.en.vtt`, referenziato in `ingest.json.subs`). È stato deduplicato (formato rolling-caption con righe ripetute) e usato **esclusivamente** per:
1. confermare la formulazione esatta delle frasi pronunciate a voce (numeri, esempi, regole) quando non scritte a schermo;
2. distinguere i dati "solo audio" da quelli "osservati a schermo" nella tabella numeri e negli atomi.
Ogni atomo/numero riporta comunque il frame-NNN.png più vicino nel tempo come riferimento visivo di contesto, anche quando il dato specifico è stato pronunciato solo a voce — questo è dichiarato esplicitamente in `video-analysis.md` (sezione "Numeri solo dichiarati a voce") e non presentato come osservato a schermo se non lo era.

## Frame illeggibili o parzialmente illeggibili (dichiarati)
- **frame-018.png** (@0:34): la riga di headline sopra "...days using LinkedIn alone." è tagliata fuori dal bordo superiore del frame — testo iniziale non recuperabile da questo frame.
- **frame-030.png / frame-031.png** (@0:58-1:00): griglia fitta di 10 screenshot di post LinkedIn in miniatura — buona parte del body-copy dei singoli post è troppo piccolo/compresso per essere trascritto parola per parola (solo headline/numeri principali sono stati letti con confidenza).
- **frame-034.png** (@1:06): stessa limitazione — testo dei post secondari (Nick Nihalos, Eugenio Zaibell) parzialmente illeggibile per dimensione.
- **frame-419.png** (@13:56): la citazione "The profile is not a resume..." è parzialmente coperta dall'interfaccia/cursore Miro nella parte finale della frase — riportata in `video-analysis.md` con troncamento dichiarato ("[...] this?").
- **frame-476.png / frame-477.png** (@15:50-15:52): l'etichetta del secondo box numerico ("Warm...") è tagliata dal bordo destro del frame — solo "Warm" e "Before the conversation" sono risultati leggibili, il resto della frase non è recuperabile da questi frame.
- Nessun frame è risultato completamente illeggibile/nero/corrotto.

## Note metodologiche
- I 105 frame includono sia inquadrature "talking head" pure (nessun testo, usate solo per il ritmo del walkthrough) sia le schermate Miro con il contenuto operativo — entrambe le categorie sono state guardate e classificate.
- Diversi frame consecutivi mostrano la stessa card Miro a zoom/scroll leggermente diverso (es. `frame-315/316/328/329` tutti sulla tabella Mistake/Fix): sono stati usati in combinazione per ricostruire il testo integrale quando un singolo frame aveva parte del testo tagliata dai bordi dello schermo o coperta dalla webcam dell'autore in basso a destra.
