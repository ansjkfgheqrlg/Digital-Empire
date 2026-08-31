# Lezione 10 — Cliente manda audio Claude fa revisioni (Claude Speedrun 2)

**Fonte:** panoramica ufficiale + "Cosa hai imparato" (14 bullet) + 9 frame video visionati nativamente. Trascrizione .md NON disponibile (link rotto, punta alla pagina stessa).

---

## Panoramica ufficiale

In questa lezione impari un workflow completo per gestire le revisioni dei clienti con Claude. Scarichi l'audio che il cliente ti manda su WhatsApp, lo trascrivi con Eleven Labs (speech to text), esporti il testo e lo alleghi a Claude dentro un project insieme al contesto necessario: copy, brand guidelines, business plan. Claude processa le richieste del cliente e ti genera l'output. Il punto chiave: fai front loading del contesto — investi ore all'inizio per creare il miglior contesto possibile, così ogni conversazione futura parte già con tutto quello che serve. Eleven Labs costa circa 20€/mese; alternative gratuite nella descrizione.

## "Cosa hai imparato" (ufficiale, integrale)

- Come scaricare un audio WhatsApp sul Mac per poterlo usare in un workflow AI
- Usare ElevenLabs (speech to text) per trascrivere audio dei clienti in testo, perché è più preciso di altri tool su punteggiatura e riconoscimento parole
- Perché la qualità della trascrizione conta: shit in, shit out — se la trascrizione è sbagliata, l'output di Claude sarà sbagliato
- Come caricare un file audio su ElevenLabs, selezionare la lingua italiana e ottenere la trascrizione
- Esportare la trascrizione come file di testo (.txt) e pulirla rimuovendo timestamp e label speaker se non servono
- Se serve un file markdown invece di .txt, cercare su Google un convertitore da TXT a MD
- Allegare la trascrizione come file di testo a Claude, dato che non puoi allegare direttamente un audio
- Insieme alla trascrizione, allegare tutto il contesto utile: copy esistente, brand guidelines, business plan, task, urgenze
- Fare tutto dentro un Project di Claude dedicato a quel cliente, così non devi ridare il contesto ogni volta
- Ogni Project su Claude ha la sua memory separata — Claude si ricorda cose specifiche di quel progetto, e questo migliora la qualità degli output
- Il workflow completo: scaricare audio → trascrivere con ElevenLabs → caricare su Claude nel Project giusto con il contesto → ottenere le modifiche richieste dal cliente
- Fare front loading del context creation: quando parti con un progetto nuovo, la prima cosa è spendere ore a creare il miglior contesto possibile (file, documenti, info)
- Riutilizzare quel contesto in ogni conversazione futura: rialleghi i file, li aggiorni, oppure sono già dentro il Project o nella cartella Cowork
- Esistono alternative gratuite a ElevenLabs per la trascrizione, anche se secondo Andrei sono meno precise

## Alternative a ElevenLabs (fonte primaria, integrale)

- **YouTube trick**: carica il video (anche audio su sfondo nero) su YouTube, usa la trascrizione automatica gratuita
- **Whisper** (open source): forte su più lingue, rumore e accenti
- **Buzz**: app desktop offline basata su Whisper, esporta TXT/SRT/VTT
- **Handy STT**: open source, offline, cross-platform, locale
- **oTranscribe**: gratis, open source, ma manuale (no trascrizione automatica)
- **MacWhisper**: locale, solo ecosistema Apple, free limitata

## Nota tecnica

Link "Scarica .md" della lezione punta all'URL della pagina stessa (non a un file reale) — anomalia della piattaforma, non della nostra pipeline. Contenuto comunque coperto adeguatamente.

## Link utili

Claude, Claude Projects, Claude Memory (docs), Claude Cowork, ElevenLabs, ElevenLabs Speech to Text, WhatsApp, WhatsApp Mac, Arc browser.
