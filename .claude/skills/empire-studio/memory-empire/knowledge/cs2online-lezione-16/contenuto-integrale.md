# Lezione 16 — Copy per primary text (ads) con Claude (Claude Speedrun 2)

**Fonte:** panoramica ufficiale + "Cosa hai imparato" (18 bullet) + 40 frame video visionati nativamente (nessuna trascrizione .md).

---

## Panoramica ufficiale

In questa lezione impari un workflow per scrivere primary text, headline e description per ads Meta con Claude, quando hai poco tempo e budget bassi. Il processo: unisci i video delle ad in un'unica timeline, esporti l'audio in MP3, trascrivi con ElevenLabs e dai tutto a Claude insieme alla sales page. Impari a strutturare il prompt — contesto, problema, richiesta — specificando USP, CTA e punti da citare, senza delegare la strategia all'AI. Più tre modi per passare una sales page a Claude: link diretto, copia-incolla del testo o markdown con MarkEdit.

## "Cosa hai imparato" (ufficiale, integrale)

- Quando ha senso fare copy "fast" invece di perfetto: valutare il budget del cliente (se spende 10-20€/giorno in ads, non ha senso spendere un'ora a scrivere i primary text)
- Cos'è un primary text, headline e description nelle ads di Meta
- Workflow completo: scaricare le creative → metterle in una timeline → esportare solo l'audio → trascrivere → dare tutto a Claude per fargli scrivere i primary text
- Usare SnapTik.app per scaricare video da TikTok senza watermark
- Usare DaVinci Resolve (o qualsiasi editor video) per unire più video in una timeline unica ed esportare solo la traccia audio in MP3
- Perché conviene unire tutto in un unico file audio: eviti di caricare e trascrivere ogni video separatamente
- Alternativa se non hai un editor video: cercare "converti da video a MP3" su Google e usare un converter online
- Usare ElevenLabs (Speech to Text) per trascrivere audio in testo velocemente
- Come esportare la trascrizione da ElevenLabs: togliere timestamps e speaker, scaricare solo il testo pulito
- Struttura del prompt quando hai contesto limitato: contesto → problema → richiesta
- Dire a Claude quante versioni vuoi (es. cinque versioni di primary text) perché Meta ti permette di usare più varianti nella stessa ad
- Inserire nel prompt il punto unico di vendita (USP) del prodotto, la CTA che vuoi e gli elementi strategici specifici — non lasciare che Claude decida la strategia, usalo solo per la forma
- Perché è fondamentale ragionare prima su cosa vuoi dire (USP, obiezioni da gestire, motivo per scegliere te) invece di chiedere a Claude "fai copy" e basta
- Come dare contesto a Claude su un prodotto senza scrivere un papiro: fargli vedere la sales page
- Tre modi per passare una sales page a Claude: incollare direttamente il link, copiare tutto il testo della pagina a mano (selezione completa + Ctrl C/V), oppure usare un tool online come totheweb.com per convertire una pagina web in testo
- Usare l'estensione Chrome "GoFullPage" per fare uno screenshot PDF di un'intera pagina web
- Limite di GoFullPage: il PDF generato a volte non viene letto bene da Claude, quindi meglio passare testo o markdown
- Come installare estensioni Chrome su Arc (funziona perché Arc gira su Chromium)
- Usare MarkEdit per trasformare velocemente il testo copiato di una pagina in un file markdown da allegare a Claude
- Dare al file allegato un nome descrittivo (es. "Copywriting Mentorship Sales Page Copy") per aiutare Claude a capire il contesto
- Possibilità di aggiungere ancora più contesto: recensioni, sito personale, brand guide, file da GitHub
- Se l'output di Claude non ti piace nel formato, chiedergli di riformattarlo (es. "mettimelo come markdown")

## Prompt osservato verbatim (frame t7m15s)

> "Ciao Claude, come stai, amore? Senti, sto facendo le ad per questo mio cliente e vorrei che tu scrivessi per me le primary text headline e description per le pubblicità su Meta. Voglio che tu segua le linee guida Meta e voglio che tu le scriva 5 versioni per ogni una."

File allegato: `_contestoi_per_cliente_per_fare_primary_text_pu...txt` (25 righe). Modello: Opus 4.6 Extended.

## Timeline demo (sintesi, vedi lesson-analysis.md per dettaglio)

DaVinci Resolve (import + export audio unificato) → Claude (prompt + file trascrizione) → sales page reale (esempio esterno + sales page propria) → GoFullPage (screenshot pagina intera) → MarkEdit.

## Workflow ufficiali citati

1. Creare primary text, headline e description per Meta Ads usando Claude
2. Dare contesto a Claude su un prodotto/servizio senza scrivere tutto a mano
3. Esportare video come MP3 senza software di editing

## Link utili

Claude, Meta Ads Manager, SnapTik, TikTok, DaVinci Resolve, ElevenLabs Speech-to-Text, GoFullPage (Chrome Web Store), totheweb.com, MarkEdit, Arc browser, Chrome, Chrome Web Store, GitHub.
