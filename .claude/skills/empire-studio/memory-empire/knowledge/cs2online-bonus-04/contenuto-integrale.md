# Bonus 4 — Claude Skills (Claude Speedrun 2)

**Fonte:** panoramica ufficiale + "Cosa hai imparato" (18 bullet) + 23 frame video visionati nativamente. Nessuna trascrizione .md.

---

## Panoramica ufficiale

In questa lezione impari cosa sono le Claude Skills, perché esistono e come crearle da zero. Andrei ti spiega il problema che risolvono: ogni volta che ripeti un processo con Claude devi riallegare le stesse istruzioni, sprecando context window e soldi. Le Skills risolvono questo perché Claude legge solo il "front matter" (la copertina) di ogni skill e carica le istruzioni complete solo quando servono davvero. Impari la struttura esatta di una skill (file SKILL.md con front matter + istruzioni + references opzionali), come crearla sul tuo computer, zipparla e caricarla su Claude.

## "Cosa hai imparato" (ufficiale, integrale)

- Il problema del metodo tradizionale: riallegare ogni volta gli stessi file/prompt a Claude spreca context window, token e soldi
- Perché allegare troppi documenti può far "skippare" a Claude informazioni importanti a causa dei limiti di context
- Come funzionano le Claude Skills: Claude legge solo la "copertina" (front matter) di ogni skill e apre il contenuto completo solo se serve
- L'analogia dei 4 livelli: risposta da memoria, ricerca online, documenti allegati (con limite di tempo/context), e skills (con selezione intelligente)
- L'analogia del ragazzino con la bancarella e i libri con le copertine per capire il meccanismo di selezione
- Cosa sono le Claude Skills tecnicamente: documenti Markdown con front matter YAML + istruzioni specifiche, salvati come SKILL.md
- La struttura del front matter: tre trattini, name (con trattini al posto degli spazi), description (cosa fa + quando usarla), tre trattini per chiudere
- Perché la description nel front matter è la parte più importante: è ciò che fa decidere a Claude se caricare quella skill o no
- Come scrivere le istruzioni sotto il front matter: step by step come hai sempre fatto nel corso
- Cosa sono le references: cartella opzionale con file aggiuntivi (Markdown, TXT, PDF) che la skill può richiamare per step specifici
- Cosa sono gli asset: cartella opzionale per immagini o altri file di supporto
- Cosa sono i codici eseguibili: file opzionali più avanzati (non approfonditi nella lezione)
- Come creare fisicamente la cartella della skill sul Mac con SKILL.md e la cartella references
- Come zippare la cartella e caricarla su Claude tramite Customize > Skills > Upload Skill
- Quando usare le Skills: processi che si ripetono frequentemente e devono essere seguiti in modo specifico
- Esempio pratico: skill per onboarding cliente con references multiple (discovery call, onboarding, overview)
- Il metodo in 2 step per partire: (1) identifica i processi ripetitivi dove usi l'AI, (2) per ognuno crea una skill

## Requisiti ufficiali osservati (verbatim, frame t19m00s)

Dialog "Upload skill" su Claude:
- ".md file must contain skill name and description formatted in YAML"
- ".zip or .skill file must include a SKILL.md file"

## Timeline demo (sintesi, vedi lesson-analysis.md per dettaglio)

Whiteboard/motion-graphic (analogia libri/copertine) → Excalidraw (introduzione SKILL.md) → MarkEdit (cartella reale "Skill Test" con esempio "skill-onboarding-cliente" + zip) → file references esempio "Struttura.md" → Claude Settings → Skills (lista con "skill-creator" di Anthropic incluso) → dialog Upload skill con requisiti ufficiali.

## Workflow ufficiali citati

1. Creare una Claude Skill da zero
2. Usare una Claude Skill caricata
3. Metodo per implementare le Skills nel tuo lavoro

## Link utili

Claude.ai.
