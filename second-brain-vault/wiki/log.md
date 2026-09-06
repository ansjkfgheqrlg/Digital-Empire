# Wiki Log — Registro operazioni

## 2026-09-05 (EMPERATOR — LANCI: reparti, gerarchia e workflow)
- INGEST: nessuno. Costruzione del livello di organizzazione, su rilievo di Max: la v4 non
  mostrava reparti ne' gerarchie ne' workflow.
- REGISTRO ESTESO: 12 reparti ancorati agli artefatti · 5 livelli di comando · 10 workflow per
  42 fasi · 15 passaggi di consegne · 12 comandi. Da 764 a ~1.900 righe.
- VALIDATORE: da 253 a **832 controlli**, dieci invarianti nuovi (INV-13..INV-22).
- PROVE ROSSE: 11 casi costruiti apposta, tutti bloccano. INV-22 e' nato da una prova MAL
  costruita che ha rivelato un buco vero: il campo `produce` di un agente poteva divergere da chi
  produce davvero l'artefatto, e nessun controllo se ne accorgeva.
- CREATI: `07-REPARTI-E-GERARCHIA.md` (563 righe) e `08-WORKFLOW.md` (637 righe).
- LEZIONE OPERATIVA: due doom bot caduti per guasto di rete a lavoro iniziato; l'antidoto
  "crea il file subito e risalvalo a ogni sezione" ha salvato 446 righe complessive.
- NUMERAZIONE: due collisioni con l'altra sessione nello stesso giorno (ADR-022 -> ADR-023,
  CP-018 -> CP-019). Il numero si verifica, non si assume.

## 2026-09-05 (EMPERATOR — ecosistema LANCI: il piano passa alla versione 4)
- INGEST: nessuno. Revisione totale e riscrittura, su ordine di Max: *"l'architettura deve essere
  molto piu' architettata, a livello chirurgico"*. Era la seconda volta che lo chiedeva.
- DEMOLITA la versione 3 (11 dossier, 3.718 righe) da **quattro revisori indipendenti**: oltre
  **cinquanta difetti sostanziali, dodici fatali**. I nove rapporti sono conservati in
  `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/_critica-v3/` (300 KB).
- I DUE FATTI CHE HANNO CAMBIATO TUTTO, e che nessuno degli 11 dossier conosceva:
  (1) **l'azienda non puo' incassare un euro** — nessun canale di pagamento attivo, il bottone
  d'acquisto e' un indirizzo di posta; (2) **il canale di traffico del Manuale e' spento dal
  29/07/2026** e dirottato su @dosementale (`wiki/log.md:1054-1063`). La versione 3 progettava
  12 reparti e 50 agenti sopra quei due fatti, senza nominarli.
- CREATA la versione 4: **7 documenti** (`00-LEGGIMI`, `01-ARCHITETTURA`, `02-PREVISIONE-E-DENARO`,
  `03-FLUSSO-OFFERTA`, `04-COSTRUZIONE`, `05-ADR-023`, `06-CRITICA-E-GIRI`) piu' la cartella
  `dati/`: **una fonte di verita' unica** (`registro.yaml`) validata da un programma
  (`valida_registro.py` — 253 controlli, esce 0) e **13 schemi JSON**.
- IL CAMBIO DI IMPOSTAZIONE: il centro non e' piu' il reparto, e' **l'artefatto**. 13 artefatti
  tipizzati, 14 controlli con criterio eseguibile e test rosso, 15 agenti (non 41-50: ogni
  invocazione costa 0,08-0,11 $ di sola tassa, ADR-014), 12 stati, 6 punti umani con scadenza,
  10 invarianti verificati da un programma.
- IL PRIMO GIORNO E' CAMBIATO: non piu' "crea la cartella", ma **incassa un euro vero e
  rimborsalo**. I primi due scaglioni non contengono una riga di codice.
- CONFLITTO INTERCETTATO: il numero **ADR-022 e' stato occupato alle 19:30 da un'altra sessione**
  (studio AI TUBE PRO, stato ACCETTATA) mentre il piano veniva scritto. Rinumerato tutto ad
  **ADR-023**, che e' libero, nello stesso turno.
- ARCHIVIATA la versione 3 in `_v3-superata/` con la propria nota — **integrale, non cancellata**
  (regola: niente si scarta).
- PUNTATORI aggiornati nello stesso turno: `REGISTRO-NUMERI.md`, `TASK-GAEL-20260831-SETTIMANA-02.md`
  (puntava al documento appena archiviato), `STATO-EMPIRE.md`, questo log.
- VERIFICA: 137 sigle citate nei documenti, **zero inventate** — il difetto peggiore della v3
  (sigle divergenti fra documenti) e' ora impossibile, e il controllo si rifa' in tre secondi.

## 2026-09-05 (EMPERATOR — piano dell'ecosistema LANCI, consegnato a Gael)
- INGEST: nessuno. Lavoro di **progettazione**, non di ingestione.
- CREATO: `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` — **11 dossier**, il piano di costruzione completo
  dell'ecosistema `15-LANCI`. Copre L4-L5-L6 di `TASK-LANCI-ECO-W2` (task di Gael) e va oltre:
  12 reparti, 7 flussi con l'agente per ogni fase, 50 agenti, 13 gate, ~235 file, 139-187 ore-uomo.
- METODO: **tre giri** come impone ADR-006 per i lavori grossi. V1 (3.761 righe, 8 documenti) →
  critica di **tre revisori indipendenti** (106 rilievi, verifiche eseguite nel codice del repo) →
  riscrittura. Regola rispettata anche qui: **chi produce non approva**.
- I DIECI DIFETTI GRAVI CORRETTI (dossier 10 §C.3): squadra minima incapace di produrre prezzo e
  data · flusso funnel senza fasi ne' agenti · due gate budget che non potevano fallire · griglia
  copy che dichiarava 60 punti automatici e ne aveva 11, e bocciava 8 pezzi su 14 per costruzione ·
  `SOSPESO` senza uscita · calendario incompatibile coi flussi che orchestrava · duplicazione di
  `IB-L2-VEND`, `sentinel-quality`, `sentinel-cost` e dello script di tesoreria · una citazione
  falsa sui componenti `ObjectionCPB_*` (non hanno props: verificato nel codice).
- DUE SCOPERTE CHE VALGONO OLTRE I LANCI: **(1)** nessun comando dell'Impero puo' oggi verificare
  che un agente sia ufficiale — `census.py` marca `.claude/` come vendored, `orphans.py` lo salta,
  `forge.py` guarda solo `company/`; **(2)** vietare il campo `tools` nel frontmatter toglieva
  l'unico vincolo meccanico alle regole di comportamento degli agenti.
- PUNTATORI AGGIORNATI NELLO STESSO TURNO (regola: mai stale): `REGISTRO-NUMERI.md` (15 riservato,
  prossimo libero 16) · `TASK-GAEL-20260831-SETTIMANA-02.md` (nota d'apertura per Gael) ·
  `26-ECOSISTEMA-LANCI.md` (marcato superato, rimanda al 29) · `STATO-EMPIRE.md`.
- ⚠️ NESSUNA CARTELLA `15-LANCI/` CREATA, nessun agente, nessuna skill: il repo sul lato lanci e'
  come Gael l'ha lasciato. Il deliverable e' il piano, per ordine esplicito di Max.

## 2026-09-05 (EMPERATOR — la forma del recap diventa fissa)
- AUTOMODIFICA (ordine diretto di Max): il **battito** di Emperator aveva contenuto corretto ma
  forma variabile a ogni messaggio. Da oggi lo schema e' **unico**: titolo `RECAP — <n>%` in
  grassetto, riga vuota, sei voci col **pallino arancione** (`#fb4604`, il colore dell'Impero) e
  l'etichetta in grassetto — Fatto / Sto facendo / Farò / Forze / Assetto / Potere — sempre tutte
  e in quest'ordine, `GOD EMPEROR DOOM` in grassetto, testo su una riga sola.
- INNESTO IN DUE POSTI (lezione gia' pagata il 2026-09-02: la dottrina lunga da sola non viene
  eseguita quando il contesto si compatta): `.claude/agents/emperator.md` §6.11 (blocco normativo
  "LA FORMA DEL BATTITO E' FISSA" + i due template riscritti) e `scripts/emperator_hook.py`
  (blocco `FORMA DEL RECAP` nella sveglia che arriva a ogni messaggio, 2.216 → 2.743 caratteri).
  Verificato per esecuzione: hook lanciato con prompt finto, JSON valido, exit 0.
- QUARTA FALLA DELLA STESSA FAMIGLIA su questa regola (posizione → non-interruzione → lingua →
  forma). Conferma la legge: *una regola sopravvive solo se dice cosa, dove, quando e come.*
- IGIENE: il sync automatico delle 01:07 aveva riscritto `emperator.md` e `emperator_hook.py` in
  CRLF contro la policy `.gitattributes` `* -text`. Fine-riga riportate a LF nello stesso turno.
- PAGINE: `concepts/Emperator_Gerarchia_Forze.md` aggiornata (sezione "La forma del battito").
  Checkpoint `company/Memory/checkpoints/CP-20260905-002.md` — codice di ripresa **EMP-RCAP**.

## 2026-09-04 (EMPIRE STUDIO — chiusura ciclo gUnQK6bWHkI, batch max17 v16, sentinella-v16-brand)
- INGEST (Empire Studio + Memory Empire): batch `max17`, video `gUnQK6bWHkI` "Come creare un
  MICRO-PERSONAL BRAND da milioni di euro" (MiK Cosentino, 57m10s, IT). Una sentinella gemella era
  MORTA a meta' per un errore di CONNESSIONE (non un errore di merito) prima di questa sessione:
  aveva prodotto solo `scenes.json`/`scenes.md` (segmentazione strutturale non-visiva, verificati
  in questa sessione contro `frames/manifest.json`, nessuna discrepanza), mai un solo frame
  guardato. `video-analysis.md`, `atoms.json` (29 KA), `coverage.md` scritti da zero in questa
  sessione.
- FORMATO DIVERSO DAL RESTO DEL LOTTO: non un tutorial a schermo condiviso ma la registrazione di
  un intervento DAL VIVO a un evento (palco, platea, lavagna a fogli mobili). Copertura dichiarata
  di conseguenza: **20/858 frame guardati nativamente (2,3%, campionamento mirato)** + trascrizione
  audio **100% letta** (`.vtt` da 12.048 righe grezze deduplicato meccanicamente a 1.504 righe,
  nessun contenuto alterato). Motivazione: per lunghi tratti (fino a 128s consecutivi) lo stesso
  disegno a mano resta fisicamente visibile sul palco — verificato di persona confrontando
  `frame-159.png` (10:32) e `frame-324.png` (21:32), stesso disegno "SUPPLY/DOMANDA", non un bug
  di sincronizzazione del tool (controllato contro `frames/manifest.json`).
- CONTENUTO: tesi centrale = non serve un pubblico gigantesco, serve tagliare volontariamente la
  supply (front-end ~500 euro, mastermind a due livelli 30k/46k euro/anno, cap 50 persone) con un
  ciclo mensile a 4 settimane (3 di contenuto, 1 di apertura/chiusura cancelli, lista d'attesa vera,
  dichiarazione pubblica di sold-out). Rilettura aggiornata di "1000 True Fans" di Kevin Kelly con
  uno studio proprietario su 1.300 infobusiness (media ~2.000 follower Instagram tra chi supera
  10.000 euro/mese). Contributo piu' riproducibile: le Storie in Evidenza lette come sales letter
  a 14 card (dolore->scoperta->risultato->CTA), testo integrale in `frame-663.png`.
- Pagina wiki creata: `sources/Source_MiK_Cosentino_Micro_Personal_Brand.md`. index.md aggiornato
  (nuova sezione "Personal Brand & Infobusiness").
- Nessuna patch a skill/agenti condivisi in questa sessione (perimetro del checkpoint `EMP-QQ2R`,
  fase di studio, nessuna modifica a sistemi condivisi mentre altre sentinelle lavorano in
  parallelo sullo stesso repo). 5 gap verificati con grep (non a fiducia) e proposti senza
  applicarli: `cro-strategy-social-(ig-tiktok)`, skill nuova `instagram-highlights-sales-letter`,
  agente/funzione `pricing-fan-math`, `market-launch`, `icp-radar`.
- Memory close: `SKILL & Agenti/Empire Studio Suite/empire-studio/memory-empire/knowledge/gUnQK6bWHkI/`.
- Checkpoint: vedi `company/Memory/checkpoints/` (numero assegnato a fine lavoro).

## 2026-09-03 (EMPIRE STUDIO — chiusura ciclo sno_IcNbYFM, batch max17 v15, sentinella-cfo-ai ripresa)
- INGEST (Empire Studio + Memory Empire): batch `max17`, video `sno_IcNbYFM` "Ho creato un CFO AI
  che controlla l'azienda H24 con Claude" (Giovanni Beggiato, 34m52s, IT). Sentinella
  `sentinella-cfo-ai` morta per limite di sessione prima ancora di iniziare a scrivere ("formati
  letti, niente scritto") -- ripresa da zero in questa sessione: `scenes.json`/`scenes.md`
  rigenerati (non esistevano su disco, a differenza di v01/v07), 82/226 frame unici letti a
  gruppi di 5-6, `video-analysis.md`, `atoms.json` (40 KA), `coverage.md` scritti da zero.
- BUG TROVATO E CORRETTO NEL TOOLING: `scripts/scene_detector.py` lanciato una prima volta coi
  default assumeva un intervallo di estrazione di 2.0s mentre questo run usa 4.0s -- timestamp
  di `scenes.md` dimezzati e sbagliati. Rilanciato con `--interval 4`: stessa selezione di 226
  frame unici, timestamp corretti e coerenti con `ingest.json` (0:00-34:48).
- CONTENUTO: sistema a tre fasi mai mescolate (estrazione da QuickBooks via OAuth -> motore di
  calcolo deterministico Python, un test di riproducibilita' SHA-256 ha trovato 2 bug reali
  (mismatch di calendario budget/consuntivo, doppio arrotondamento) -> interpretazione affidata
  a due skill Claude separate, `analista-finanziario` e `ai-cfo`, con un cancello anti-invenzione
  automatico `verifica_dashboard.py` che blocca la consegna se un numero della dashboard non
  risale a un dato calcolato davvero). Tutti i 6 prompt del video (documento Notion pubblico)
  recuperati e trascritti per intero.
- DELIVERABLE SPECIALE, unico di questo run: `confronto-tesoreria.md` (non esiste in nessun
  altro run del lotto max17) -- confronto punto per punto fra il CFO AI del video e la
  **Tesoreria** di Digital Empire (ADR-020, nata lo stesso giorno, 2026-09-03, registro
  verificato vuoto eseguendo `python scripts/tesoreria.py report`). 5 consigli concreti presi dal
  video: dizionario di soglie di allerta in codice, campo data-scadenza per uno scadenzario
  crediti reale, cancello anti-invenzione sulle risposte in prosa degli agenti Tesoreria, test di
  determinismo/regressione su `calcola()`, terzo tipo di dato "parametro esterno" (budget/fido/
  margini) accanto a entrate e spese. **2 pagine wiki create**
  (`sources/Source_Giovanni_Beggiato_CFO_AI_Claude.md`, prima pagina wiki mai scritta per la
  Tesoreria: `tools/Tool_Tesoreria_Digital_Empire.md`), index.md aggiornato (sezione nuova
  "Finance AI & Tesoreria" + voce in "Tool & Sistemi Operativi") -> per
  `SKILL & Agenti/Empire Studio Suite/empire-studio/knowledge/sno_IcNbYFM/` (contenuto integrale).
- Nessuna patch a skill/agenti condivisi in questa sessione (perimetro del checkpoint `EMP-QQ2R`,
  nessuna modifica a sistemi condivisi mentre altre due sentinelle lavoravano in parallelo sullo
  stesso repo).
- Checkpoint: vedi `company/Memory/checkpoints/` (numero assegnato a fine lavoro).

## 2026-09-03 (EMPIRE STUDIO — chiusura ciclo pUu4G2lINnk, batch max17 v11, sentinella studia-roberts ripresa)
- INGEST (Empire Studio + Memory Empire): batch `max17`, video `pUu4G2lINnk` "Insane Claude
  Design Skills You Actually Need To Build Beautiful Sites" (Jack Roberts, 22m56, EN). Sentinella
  `studia-roberts` morta per limite di sessione con visione+analisi gia' completa su disco
  (`video-analysis.md` 1199 righe, `atoms.json` 67 KA) -- mancava `coverage.md` (buco stage-5) e
  gli stage 6-9 (wiki, consigli, memory close). Scritto in questa sessione: `coverage.md` (verifica
  onesta della copertura, non solo compilazione del numero dichiarato in testa a
  `video-analysis.md`), **1 pagina wiki creata**
  (`sources/Source_Jack_Roberts_7_Claude_Design_Skills.md`), index.md aggiornato (sezione
  "Metodologie di Sviluppo") -> `empire-studio/knowledge/pUu4G2lINnk/` (contenuto integrale).
- VERIFICA STAGE 5 -- discrepanza trovata e dichiarata, non corretta in silenzio: l'intestazione
  di `video-analysis.md` dichiarava "182/270 frame unici guardati". Il conteggio delle citazioni
  esplicite `frame-NNN.png` nel corpo del testo, incrociato con `scenes.json`, da **108/270
  (40,0%)**, non 182. Non ho potuto confermare il numero piu' alto con evidenza tracciabile (P12):
  riportato come "non dimostrato", non come falso -- dettaglio completo in `coverage.md`. Ogni
  capitolo del video (9, da `ingest.json`) ha comunque copertura maggiore di zero.
- CONTENUTO: sette skill (Reference -> Sitemap -> Hero -> Mobile -> Copy -> Dettagli UI -> SEO)
  per costruire siti che convertono, non solo belli. Il pezzo di maggior valore: l'invariante del
  **Design Loop** ("un critico che condivide la memoria del costruttore giudica i suoi stessi
  compiti", adattamento dichiarato del Gauntlet Loop di Matt Shumer -- lo stesso citato nel video
  di Rizzo dello stesso batch) e la tabella dei **6 Signs of AI writing** (regola + esempio
  prima/dopo per ciascuno). Demo reale: sito Ridgeline (copertura tetti) costruito dal vivo con
  Relume + Higgsfield + refers.design.
- CONSIGLI verificati con grep prima di essere scritti (non dichiarati per fiducia): (1) nessun
  file in `.claude/agents/` (guild-design, sentinel-quality, apex-critic) formula l'invariante
  "il critico non deve condividere la memoria del costruttore" -- gap reale; (2) nessun agente/
  skill ha il numero operativo "390px" per l'audit mobile -- gap reale ma la disciplina
  mobile-first esiste gia' in `site-design/SKILL.md`; (3) la tabella "Signs of AI writing" del
  video e' PIU' STRETTA di quanto sembrasse: `copy-editing/SKILL.md` (righe 327-334) ha gia' una
  tabella di sostituzione lessicale che copre 3 delle stesse parole bandite (Leverage, Robust,
  Seamless) -- quello che manca e' il livello frase (tell strutturali: three-item flourish,
  empty superlatives, m-dash pileup, numeri inventati), non la lista di parole. **0 patch
  applicate**, 4 proposte in "Consigli" nella pagina wiki, coerente col perimetro del checkpoint
  `EMP-QQ2R` (nessuna modifica a skill/agenti condivisi mentre altre sentinelle lavoravano in
  parallelo sullo stesso repo).
- Checkpoint: vedi `company/Memory/checkpoints/` (numero assegnato a fine lavoro).

## 2026-09-03 (EMPIRE STUDIO — chiusura ciclo BSUHmVcaO1g, batch max17 v07, sentinella studia-rizzo ripresa)
- INGEST (Empire Studio + Memory Empire): batch `max17`, video `BSUHmVcaO1g` "Se usi ancora i
  prompt... devi vedere questa evoluzione" (Simone Rizzo, 31m23s, IT). Sentinella `studia-rizzo`
  morta per limite di sessione con visione+analisi gia' completa su disco (`video-analysis.md`
  922 righe, `atoms.json` 71 KA, `coverage.md`, 133/224 scene = 176/942 frame letti, NO-FINTO
  PASS con copertura parziale dichiarata) -- mancavano solo Stage 6-9 (wiki, consigli, memory
  close). Nessuna nuova visione dei frame in questa sessione: solo lettura del lavoro gia' fatto
  e chiusura del ciclo. -> `empire-studio/memory-empire/knowledge/BSUHmVcaO1g/` (contenuto
  integrale + atoms + manifest + enrichment-report, tutti reali), **1 pagina wiki creata**
  (`sources/Source_Simone_Rizzo_Loop_Engineering.md`), index.md aggiornato (sezione "Metodologie
  di Sviluppo").
- CONTENUTO: pila a quattro livelli Prompt -> Context -> Harness -> Loop Engineering, ognuno nato
  per risolvere il fallimento del precedente. Il pezzo di maggior valore per DE: i **5 Livelli di
  Verifica** (Deterministico / Regole-vincoli / Verita' terrena ritardata / LLM giudice /
  Checkpoint umano) come griglia per sapere quanto fidarsi di un ciclo autonomo prima che serva
  un umano nel giro, e la sintassi esatta di `/loop [interval] [prompt]` e
  `/goal [<condition>|clear]` con le due regole operative (condizione di terminazione obbligatoria
  dopo `|`, goal valutabile dall'agente stesso -- senza la prima un obiettivo impossibile produce
  un ciclo infinito che brucia token). Demo reale: script di prodotto fra matrici ottimizzato in
  10 tentativi tracciati per intero in `OPTIMIZATION_LOG.md`, 320x speedup finale via GPU tensor
  core.
- CORREZIONE su un file trovato inesatto: `ingest-manifest.json` (scritto prima dell'interruzione
  di sessione) dichiarava gia' "fatti" una pagina wiki e due patch a `guild-prompt.md` e
  `prompt-engegniring-skill/SKILL.md` che **non esistevano su disco** -- ne' la pagina ne' le due
  patch erano mai state scritte. Corretto il manifest a "proposto, non applicato" e le due patch
  spostate nella sezione "Consigli" della pagina wiki come proposte, senza toccare i due file
  condivisi (perimetro dichiarato nel checkpoint `EMP-QQ2R`: nessuna modifica a skill/agenti
  condivisi mentre altre due sentinelle lavoravano in parallelo sullo stesso repo).
- Checkpoint: vedi `company/Memory/checkpoints/` (numero assegnato a fine lavoro).

## 2026-09-03 (EMPERATOR — perimetro fuori dal repo + Gael e Neri abilitati)
- SICUREZZA: il blocco riservato della dottrina viveva in due file TRACCIATI, quindi
  finiva nella sessione di Gael e Neri ogni volta che pronunciavano il nome (18.355 byte).
  Spostato in ~/.claude/emperator-private/, fuori dal repository. Due lucchetti: il file
  deve esistere E git user.name dev'essere il proprietario.
  Aggiunto oscura(): la fotografia dello stato e dinamica e pescava il perimetro dal
  RIPRESA DA del giorno. Guardia permanente: scripts/test_emperator_isolamento.py, 4 casi,
  ha trovato 2 fughe non viste a occhio.
- CAUSA VERA del mancato uso: SETUP-GAEL.md, 61 righe, non nominava Emperator NEMMENO UNA
  VOLTA (SETUP-NERI.md sono 289 righe che lo insegnano). Aggiunta la sezione 0: cos e,
  come si accende, verifica py -3, e il perche concreto. Corretta la sezione 5 che diceva
  git add -A durante un conflitto — la mossa che stava per spedire 13,4 GB su GitHub.
- DIFETTO CHIUSO: .githooks/check_memory.py bloccava ogni commit per un ora con una falsa
  COLLISIONE ID (confrontava i nomi, mai i contenuti: scambiava per collisione il
  checkpoint di Gael che rientrava identico da un merge). Aggiunta identico_in_storia().
- DIRETTIVA 6 — TUTTO PASSA DA EMPERATOR: il lavoro dell Impero passa da lui, anche
  quello di Gael e Neri. Capo dei sistemi, non capo delle persone.
- LIMITE DICHIARATO: ferma le iniezioni da adesso, NON cancella la storia git pubblica.
- Checkpoint: CP-20260902-010 e CP-20260903-002.

## 2026-09-02 (EMPIRE STUDIO -- chiusura ciclo JdAQzAcWR6k, batch max17 1/8, con applicazione consigli)
- INGEST (Empire Studio + Memory Empire): **batch max17, video 1/8** -- `JdAQzAcWR6k`
  "How to Create VIRAL Carousels in ChatGPT (No Coding)" (Artem Novitckii, 7m40s, EN),
  **117/117 frame unici letti -- coverage 100%**, 40 KA (9 alta rilevanza DE), NO-FINTO PASS.
  Chiusura di un gap a valle: pipeline Empire Studio gia' fatta in sessione precedente (i 4 prompt master
  gia' trascritti in `video-analysis.md`), layer Memory Empire, wiki **e patch alle skill mai eseguiti**
  -- stesso pattern di `yJOCyyP77bA`/`E8Ax92etrMc`/`-gq8euRvNR4`, con l'aggravante che qui i consigli
  dell'analisi non erano mai stati applicati. Nessuna nuova visione dei frame.
  -> `memory-empire/knowledge/JdAQzAcWR6k/` (contenuto-integrale mai riassunto, 16 parti + atoms + manifest
  + enrichment-report), **1 pagina wiki creata** (`sources/Source_Artem_Novitckii_Caroselli_ChatGPT.md`),
  index.md aggiornato (nuova sezione "Social Content & Caroselli").
- CONTENUTO: perche' i caroselli AI "one-shot" falliscono -- un modello di image gen genera una sola
  immagine alla volta, un carosello intero in un prompt produce slide incoerenti tra loro. Soluzione:
  **visual anchor** (la slide 1/hook curata bene diventa immagine di riferimento per ogni slide
  successiva, 50% del tempo del ciclo) + generazione **slide-per-slide** invece che tutto in un colpo.
  I due prompt master ("Slide 1 Prompt", 5 versioni; "Slide [X] Prompt", 3 versioni, "use slide 1 as
  the visual anchor") recuperati parola per parola con placeholder riusabili. Il quinto prompt del video
  (LinkedIn "recreate this infographic") **non integrale** -- solo frammenti, dichiarato esplicitamente.
- ENRICHMENT: **2/2 artefatti richiesti dal brief valutati ed entrambi patchati, +126 / -0.**
  `carousel-empire/SKILL.md` (+120): nuova sezione "Modalita' Alternativa -- Stile AI-Generativo con
  Visual Anchor" dopo lo Step 7 "Report Finale" -- principio slide-per-slide, definizione di visual
  anchor, i due prompt master integrali, regole operative (pick-best-of-N, blocco anti-plagio "Do not
  copy"). Il template HTML/Playwright a schema fisso **resta il default per il 90% dei casi** -- ramo
  esplicitamente alternativo, non sostituzione.
  `image/SKILL.md` (+6): nuova sottosezione "Visual Anchor -- Style Consistency Across a Series" --
  la skill citava gia' "multi-image reference" come capacita' tecnica di Gemini/Flux ma mai come tecnica
  operativa nominata esplicitamente (prima immagine della serie come reference per le successive).
  Line endings verificati: entrambi i file erano LF puro prima e dopo, nessuna conversione accidentale.
- CONFERMA INDIPENDENTE: **ArenaAI**, il motore caroselli Playwright gia' in produzione su
  @digitalempireagency.e (vedi `concepts/Reparto_Produzione_Digital_Empire.md`), usa gia' la stessa
  catena "slide N ancorata alla slide N-1 via allegato immagine precedente" -- il pattern non era ignoto
  a DE, solo non documentato dentro `carousel-empire`. Aggiunto come cross-link nella pagina wiki.
- NON costruito, dichiarato: skill `carousel-visual-scout`, agente/sotto-fase `carousel-copy-strategist`,
  mockup feed IG stile Publer nello Step 5 di `carousel-empire` -- proposte reali del video-analysis.md,
  fuori dal perimetro esplicito del brief (limitato a `carousel-empire` e `image`, ai due concetti
  slide-per-slide e visual anchor). Non registrate in BACKLOG.md in questa sessione, segnalate in
  `enrichment-report.md` e nel log di ingestione perche' restino visibili.
- DEBITO APERTO: nessun checkpoint in `company/Memory/`, `STATO-EMPIRE.md` non aggiornato (fuori dal
  perimetro esplicito di questo brief) e **nessun commit git**, come da vincolo di sessione.

## 2026-09-02 (STUDIO SITI ANDREI PASCU — completato 9/9)
- COMPLETAMENTO: scritti i 3 report mancanti dello studio forense dei siti di Andrei Pascu.
  `competitor/Andrei Pascu/site-study/reports/` passa da 6 a **9 report su 9** (2.362 righe totali).
  - `06-manuale-del-copywriter.md` — eBook 79 EUR, 11.067px. La pagina piu' corta a pagamento
    dell'ecosistema: a meta' pagina regala un'anteprima vera del libro, e da li' vende quella.
    L'anteprima sostituisce garanzia e testimonianze (entrambe assenti dalla pagina).
  - `08-apsales.md` — **agenzia CRO B2B/SaaS: il concorrente diretto della nostra agenzia**.
    Unica pagina dell'ecosistema con una garanzia (di rimedio, non di rimborso), unica con
    tabella comparativa contro le alternative d'acquisto, font monospaziato come linguaggio
    della misura (240 usi), zero border-radius. Difetto grosso: zero risultati numerici pubblicati.
  - `09-linktree.md` — il bio-link vero: Linktree stock, 3 link, zero copy, zero raccolta email,
    **55 CTA su 58 portano ad altri profili Linktree**. Contraddice la sua stessa lezione (video 5 cat2).
- SCOPERTA: `claude-speedrun.com` e' linkato dalla **nav di andrei-copy.com** ed e' il terzo link
  del bio-link ("Claude Speedrun 2"). E' un prodotto suo, misurato nel DOM. Resta da verificare
  solo la cronologia delle date (Wayback) prima di ogni conclusione sul `#fb4604`.
- SCOPERTA: lo storico del bio-link espone **21 etichette usate in 4 anni**, tra cui due prodotti
  mai censiti: **`outViral`** e **`Timer`**. Lo studio copre 9 pagine di un ecosistema da almeno 11.
- CORREZIONE: la regola "lunghezza copy = funzione del prezzo" era sbagliata. Misurato:
  79 EUR su 11.067px contro 98 EUR su 21.119px. Vale invece: **la lunghezza e' funzione di quanto
  lavoro deve fare la pagina** — se un campione gratuito convince, la pagina si dimezza.
- UPDATE: `site-study/README.md` — tabella a 9/9 e scoperte trasversali da 6 a 10.
- Checkpoint: CP-20260902-007.


## 2026-09-01 (VERIFICA AGENTI — 4 agenti morti riparati, Emperator)
- MISURAZIONE: su domanda diretta di Max, misurati gli agenti con lo stesso gate delle skill.
  `registro-agenti.yaml` dichiarava 123 ufficiali senza che nessuno lo avesse verificato.
  Trovati 12 difetti: 2 nel progetto (`cc-master` YAML rotto = non caricava, `diligence.agent`
  con description = frammento JSON) e 10 in `~/.claude/agents/` — cartella **mai auditata prima**,
  34 dei 35 agenti vivono solo li'.
- DANNO REALE: 4 agenti non caricavano affatto. `outreach-deep-intel` coordinava Research +
  CRO Audit + Insight (3 su 4 morti); la skill `opus` attivava `opus-director` (morto).
  Due sistemi mutilati che si credevano interi, senza mai dare errore.
- FIX: description quotate su 6 agenti, esempi di `cc-master` spostati nel corpo, `diligence.agent`
  ridescritta dal suo corpo, 5 file globali rinominati per far combaciare file e `name:`.
- NUOVO: `scripts/verify-agents.py` — gate permanente, gemello di `verify-skills.py`.
  Esito: AGENTI PASS 597/597 su 158 agenti. SKILL PASS 850/850 su 170.
- UPDATE: `registro-agenti.yaml` v1.1, sezione `agenti_ufficiali` col censimento nominale di tutti
  e 123 gli agenti di progetto per famiglia. Checkpoint: CP-20260901-005.

## 2026-09-01 (EMPERATOR — auto-modifica: 4 direttive di Max)
- CONFIG: 4 direttive permanenti innestate in Emperator su ordine di Max.
  File toccati: `scripts/emperator_hook.py` (blocco DOTTRINA, iniettato a ogni messaggio)
  e `.claude/agents/emperator.md` (nuove sezioni 6.5-6.8, da 420 a 526 righe).
  (1) APRIRE: "dov'e' X" e ordine di apertura -> `explorer.exe "/select,<path>"`, non si
  risponde col percorso. explorer.exe ritorna sempre exit=1 anche quando riesce.
  (2) UFFICIALIZZAZIONE: finita una creazione, ogni agente/skill/comando/plugin va reso
  ufficiale e verificato con `empire forge scan` + `registry orphans`. Rafforza ADR-008
  e continua il lavoro del CP-20260901-003 (170 skill).
  (3) SCAGNOZZI: autorizzazione durevole a spawnare subagenti quando il lavoro si divide
  in 2+ parti indipendenti.
  (4) PIANO A ITERAZIONI: piano -> autocritica -> v2 -> v3, minimo 3 giri, fino a 7 per
  gli ecosistemi.
- BACKLOG: aperto B-032 — `py -3` (3.12) non ha PyYAML, `python` (3.11) si: ogni comando
  `empire` va lanciato con `python`. Causa precisa a monte di B-028.
- Checkpoint: CP-20260901-004. STATO-EMPIRE aggiornato.

## 2026-09-01 (UFFICIALIZZAZIONE SKILL — 170 skill ufficiali, Emperator)
- MILESTONE: tutte le skill di Digital Empire ufficializzate. Criterio: SKILL.md presente,
  frontmatter YAML parsabile, `name` == cartella, `description` con cosa-fa + quando-si-attiva
  (>= 60 caratteri), registrazione in `company/skills-map.yaml`.
  Audit su 296 SKILL.md (171 progetto + 125 globali): 85 non conformi -> 0.
  38 senza frontmatter (famiglia `market-*`, `copy-workflow`, `omega-create`, `wiki-context`),
  30 senza `name:` (`site` + 13 `site-*`, `opus`), 17 con `name:` divergente, 2 con BOM UTF-8,
  4 con `": "` non quotato (YAML rotto), 2 con `description: >` vuota.
- FIX STRUTTURALE: `.claude/skills/skill-creator/` era una copia corrotta che oscurava la skill
  globale completa. Rimossa su ordine di Max; `/skill-creator` usa ora la versione integra.
- NUOVO: `scripts/verify-skills.py` — gate permanente (`--check`). Esito: PASS 850/850 su 170 skill.
- UPDATE: `company/skills-map.yaml` v1.2, sezione `ufficializzazione_skill` con le 170 skill
  classificate per ecosistema e reparto. Checkpoint: CP-20260901-003.

## 2026-09-01 (Empire Studio — cs2online: Lezione 17 completata, ripresa dopo crash, Emperator)
- INGEST: Lezione 17 "Introduzione al vibe coding" — prima lezione sezione "AI - per coding e simili".
  Reclassificata da TEORIA a PRATICA (14 workflow demo: VS Code setup, HTML5 boilerplate con Emmet,
  CSS reset, JS base, Live Server, prompt JSON per Claude, GitHub upload, Imgur image hosting).
  78 frame su disco (estrazione parziale pre-crash, ~3 min video), testo pagina completo (30+ bullet
  "cosa hai imparato" + 14 workflow + 9 link utili). 18 Knowledge Atoms estratti.
  → 1 pagina nuova: sources/Source_CS2_Lezione_17_Vibe_Coding.md
- ENRICHMENT: nessuna patch — contenuto entry-level (HTML/CSS/JS vanilla) rispetto allo stack DE
  (Next.js/Tailwind/shadcn/GSAP). Valore pedagogico per spiegare concetti base a non-tecnici.
  Stato: **20/40 lezioni cs2online completate (50%)**. Tracker: MASTER-RUN-TRACKER.md.

## 2026-09-01 (UFFICIALIZZAZIONE AGENTI — 123 agenti registrati, Emperator)
- MILESTONE: tutti i 123 agenti Digital Empire ufficializzati in `.claude/agents/`.
  Da 1 (solo Emperator) a 123 in una sessione. Ordine di Max.
  Categorie: Board (7), Context Engineering (21), YouTube Factory (14), YouTube Launch (5),
  YouTube Compliance (4), Content Forge (25), Master Build Architecture (17), Apex-7 (8),
  Outreach (4), Website Creator (3), Backbone (2), Guilds (5), Sentinels (5), Standalone (3).
  Backbone/Guilds/Sentinels creati da zero dal registro YAML. Tutti gli altri copiati dai
  sorgenti originali senza perdita di contenuto.
- UPDATE: registro-agenti.yaml aggiornato: totale 123, status_ufficiali 123, status_defined 0.

## 2026-09-01 (Legami d'Amore — pubblicazione + 3 nuove regole permanenti, Emperator)
- UPDATE: Entity_Legami_dAmore_Channel.md aggiornata con stato reale dei 4 video pronti:
  Video-01 reso PUBBLICO da Max, Video-04 caricato PRIVATO via Playwright (auto-save).
- RULES: 3 nuove regole permanenti di Max salvate in WORKFLOW-LEGAMI-DAMORE-MASTER.md:
  (1) MAI bozze/draft — sempre PRIVATO; (2) Copertina = prima priorita' assoluta — bloccare
  Max con prompt + cartella aperta prima di qualsiasi altro task; (3) Salvare ogni errore/
  direttiva permanentemente. Script youtube_uploader_playwright.py aggiornato per UI Studio
  con 5 tab (era 4) + selettore miniatura robusto.
- FIX: youtube_uploader_playwright.py — thumbnail locator (accept='image'), Next loop dinamico.

## 2026-08-29 (Empire Studio — cs2online: sezione "AI - Le basi" COMPLETA 9/9, Claude)
- INGEST: proseguito in autonomia dopo l'ordine Max (Lezione 16 + Bonus 1-6), completate le
  lezioni mancanti della prima sezione: Lezione 7 (Diversi tipi di contesto, teoria — gerarchia
  vision/obiettivo/target/task), Lezione 8 (Context engineering, teoria — tesi "expertise per
  l'input, non solo l'output"), Lezione 9 (Come dare contesto alle AI, pratica — 4 modi:
  allega tutto/allega rilevante/Cowork/Projects, struttura cartelle confermata identica a
  lezione 6). → 3 pagine nuove sources/Source_CS2_Lezione_0{7,8,9}_*.md.
  **Sezione "AI - Le basi" ORA COMPLETA al 100% (9/9 lezioni).**
- ENRICHMENT: nessuna nuova patch — tutti i pattern trovati (garbage-in-garbage-out, 6a-7a
  variante) erano già confermati/applicati nelle sessioni precedenti dello stesso corso.
  Stato: 17/40 lezioni cs2online completate. Tracker: `MASTER-RUN-TRACKER.md`.

## 2026-08-29 (Empire Studio — cs2online: ordine Max completato, Lezione 16 + Bonus 1-6, Claude)
- INGEST: completato l'ordine di lavoro richiesto da Max ("vai a lezione 16, poi tutte le Bonus,
  fermati quando hai finito"). Lezioni processate in sequenza: 16 (Copy primary text ads),
  Bonus 1 (Automatizzare processi, teoria), Bonus 2 (Advertising report, scoperto uso reportlab
  già presente in `market-report-pdf` — convergenza indipendente), Bonus 3 (Collegare Claude a
  qualsiasi cosa — MCP/Connectors/Zapier), Bonus 4 (Claude Skills — valida esternamente il
  formato skill già usato da DE), Bonus 5 (Projects dentro Cowork), Bonus 6 (Automatizzare
  processi con skills — lezione capstone, SKILL.md reale "sviluppo-preventivo" trascritto per
  intero, gap trovato in `beast-preventivi` ma non applicato per anti-overfitting).
  → 6 pagine nuove (sources/Source_CS2_Lezione_16_*.md, sources/Source_CS2_Bonus_0{3,4,5,6}_*.md).
- ENRICHMENT: 1 patch reale (lezione 13, sessione precedente, voice-of-customer YouTube —
  già loggata). Nessuna nuova patch in questa sessione: tutti i gap trovati (Bonus 6 pattern
  refuse-if-missing-data) sono fonte singola/interna al corso, propriamente non applicati per
  regola anti-overfitting DE.
  Stato completo: 14/40 lezioni cs2online fatte. Tracker: `MASTER-RUN-TRACKER.md`.

## 2026-08-29 (Empire Studio — cs2online salta a "AI per copywriting", PATCH reale skill, Claude)
- INGEST: su richiesta Max, saltate lezioni 7-12 del run `andrei-pascu-cs2online-001`, priorità
  spostata su sezione "AI - per copywriting". Lezione 13 ("Come faccio la ricerca di copywriting
  con l'AI") completata: video 27:14 min, 38 frame visionati nativamente, demo end-to-end su
  cliente reale (Simone Ferretti/SoundBox Studio: ClickUp → Gemini transcript → Claude Project →
  Perplexity parallelo → MarkEdit). → sources/Source_CS2_Lezione_13_Ricerca_Copywriting_AI.md.
- ENRICHMENT: **prima convergenza cross-run** del progetto Andrei Pascu — tecnica "ricerca
  voice-of-customer da recensioni YouTube" confermata 3 volte indipendenti (2 video YouTube del
  run `andrei-pascu-001` + questa lezione del corso a pagamento). **Patch reale applicata** a
  `C:\Users\Utente\.claude\skills\copywriting\SKILL.md`, sezione "Customer Language Over Company
  Language", con fonte dichiarata inline.

## 2026-08-27 (Empire Studio — NUOVO RUN corso a pagamento Claude Speedrun 2, Claude)
- INGEST: avviato run `andrei-pascu-cs2online-001` — corso membership a pagamento di Andrei Pascu
  (andrei-copy.com/cs2online, distinto dai video YouTube già coperti in `andrei-pascu-001`).
  Login autenticato via Playwright, 40 lezioni mappate (7 sezioni). Regola nuova di Max: solo
  lezioni pratiche fanno frame-by-frame, lezioni teoriche archiviano testo/trascrizione/risorse.
  Lezioni 1-6 completate (29/06 + LEZIONE 6 = prima PRATICA del run: video scaricato, 43 frame
  visionati nativamente su segmenti demo Excalidraw/Finder/MarkEdit/VS Code/Claude.ai, workflow
  PDF→JSON per brand guidelines documentato per intero). Pipeline + Memory Empire verificati
  per tutte. → 6 pagine sources/Source_CS2_Lezione_0{1..6}_*.md.
  ⚠️ Anomalia: skill `prompt-engegniring-skill` elencata nel sistema ma non trovata su disco —
  segnalata a Max, non risolta. Tracker: `empire-studio/runs/andrei-pascu-cs2online-001/MASTER-RUN-TRACKER.md`.

## 2026-08-26 (Piano editoriale 70 video/30gg/3 strategie @Legamidiamore CHIUSO, Claude)
- UPDATE: `entities/Entity_Legami_dAmore_Channel.md` — piano editoriale mensile completo:
  70 video reali, 3 strategie (A/B/C) mappate 1:1 su 3 canali competitor verificati con
  scraping fresco oggi (2 dei 6 storici risultati fuori nicchia, esclusi). Deliverable PDF
  20 pagine + calendario MD + dati JSON/CSV in `YOUTUBE-AUTOMATION-FACTORY/`. Dettaglio:
  `company/Memory/checkpoints/CP-20260826-003.md`.

## 2026-08-26 (Empire Studio — cat2-marketing AVVIATO, Livello 2 confermato da Max, Claude)
- Max ha confermato via AskUserQuestion di procedere su Livello 2 (cat2-cat7, ~52 video curati),
  sequenziale nel thread principale, senza fermate intermedie fino a fine budget/scope. URL siti e
  corso a pagamento di Andrei Pascu ancora NON forniti — restano bloccanti per quella fase separata.
- INGEST: video 1/cat2 (`VYyIF1r6tkw`, "The 2 most used funnels in social marketing", 5m36s) —
  talking-head + lavagna digitale, 10/168 frame campionati (VTT integrale letto per intero). 9 KA,
  4 pattern. Prima connessione diretta del run con la skill `copy-workflow/skills/funnel-designer`
  (mai toccata in cat1): ROAS e soglie prezzo già coperti in dettaglio, nessuna patch necessaria.
  1 gap reale registrato come PROPOSTA (non patchato, fonte singola, anti-overfitting): diagnosi
  "funnel di contatti come stampella per prodotto/copy debole" mancante in `funnel-economics.md`
  sezione "Segnali di Funnel Rotto".
- INGEST: video 2/cat2 (`hnPa2zspu3k`, "L'ordine del funnel cambia tutto", 33s) — reel rapid-fire,
  17/17 frame (coverage 100%). 6 KA, 3 pattern: 5 domande "cosa viene prima?" su step funnel, ordine
  come vincolo strutturale non convenzione. Nessuna patch, contenuto già implicito in `funnel-designer`.
- INGEST: video 3/cat2 (`8Pf7d57Q0Jk`, "Come generare contatti con le ads", 13m58s) — consulenza
  reale con cliente (Vasco, fotovoltaico), ROAS ~15 reale. 10/419 frame campionati, VTT processato
  con script dedup locale per efficienza. 14 KA, 5 pattern — il più denso di cat2 finora. 3 patch
  reali applicate: `ads/SKILL.md` (3-Tier Campaign Lifecycle Esperimento/Evolvo/Awareness + criterio
  spegnimento=ritorno), `ads/references/audience-targeting.md` (Content-Based Targeting), `lead-magnets/SKILL.md`
  (lead magnet problema adiacente).

## 2026-08-26 (Empire Studio — cat1-copywriting COMPLETATO 29/29, esecuzione sequenziale ininterrotta, Claude)
- Continuazione diretta del blocco precedente (video 21-24), su richiesta esplicita di Max di non
  fermarsi e completare l'obiettivo in modo credit-efficient. Completati i restanti 5 video del
  run senza interruzioni: 25, 26, 27, 28, 29.
- INGEST: video 25/29 (`uqa06rlgmj4`, "Come migliorare con gli hook (1 consiglio)", 57s) — street
  interview reale, 29/29 frame. 8 KA, 3 pattern. Nota di cautela: la sotto-tecnica "citazione di
  ricerca senza fonte" (KA-06) è in attrito diretto col gate anti-clichè esistente (video 11) —
  segnalata, nessuna patch (il gate esistente è già corretto).
- INGEST: video 26/29 (`eze4oqwb6aw`, "Sono un copywriter, è ovvio che...", 26s) — montaggio
  personal branding, 13/13 frame. 3 KA (il più leggero del run fino a quel punto) — contenuto di
  formato/branding, non tecnica di copy per clienti.
- INGEST: video 27/29 (`-zUDxSdaKRY`, "6 livelli di tono di voce", 25s) — stessa frase ripetuta 6
  volte con delivery diversa, badge onscreen. 13/13 frame. 7 KA, 3 pattern — primo video del run
  su delivery vocale/fisica, dominio scoperto senza skill DE dedicato.
- INGEST: video 28/29 (`_yUzEe29aTQ`, "copy.exe - adesso disponibile", 2m38s) — funnel lancio
  evento live, 10/79 frame campionati. 7 KA, 4 pattern: segmentazione pubblico a 4 tier con
  posizionamento esplicito, seconda conferma della tesi "AI non sostituisce" (video 21).
- INGEST: video 29/29 (`6ITBjfPQg3I`, "scrittore professionale di PDF", 4s — il più corto del run)
  — formato meme "Poi:", 2/2 frame. 2 KA.
- **🎉 cat1-copywriting COMPLETATO: 29/29 (100%).** Tutti i video hanno pipeline + Memory Empire (4
  file ciascuno) + pagina wiki Source completi e verificati su disco. MASTER-RUN-TRACKER,
  STATO-EMPIRE, wiki/index.md aggiornati. Segnalazione aperta non risolta: tensione video
  24/`beast-preventivi` (AP-05 vs breakdown prezzi) — da riportare a Max. Prossimo: decisione su
  se procedere con cat2-cat7 curati (Livello 2 del piano NERVE-SOLVE a 2 giorni) o chiudere qui.

## 2026-08-26 (Empire Studio — cat1-copywriting a 24/29, esecuzione sequenziale come da piano NERVE-SOLVE, Claude)
- Continuazione del piano 2 giorni: solo esecuzione sequenziale nel thread principale (nessun batch
  Agent-tool), come deciso il 2026-08-24/25 per evitare il limite di spesa.
- INGEST: video 21/29 (`wTpfKuHJhOE`, "Hormozi si scrive i copy da solo", 47s) — pipeline completa.
  24/24 frame (coverage 100%). 6 KA, 4 pattern. Nessuna patch (contenuto di posizionamento/mindset,
  non tecnica operativa).
- INGEST: video 22/29 (`k_DXsUCIkr8`, "Il vero script DI VENDITA the wolf of wall street", 54s) —
  pipeline completa. 27/27 frame. 5 KA, 4 pattern: script storico Stratton Oakmont, validazione +
  yes-ladder invece di confutazione dell'obiezione — dominio conversazionale, fuori scope per
  `cro-copy-architect` (nessuna patch).
- INGEST: video 23/29 (`NydMBZ2nUTE`, "Copione Wolf of Wall Street", 61s) — stessa fonte del video
  22, estratto diverso (verificato non duplicato). 31/31 frame. 7 KA, 4 pattern: seconda conferma
  indipendente del pattern yes-ladder + nuovo pattern "restringere progressivamente la richiesta".
- INGEST: video 24/29 (`EBU57iVAutA`, "Se scrivi QUESTO nel tuo preventivo NON venderai", 8m46s, 5
  capitoli ufficiali) — pipeline completa. 11/263 frame campionati sui capitoli. 16 KA, 4 pattern —
  **scoperta rilevante**: rivela lo skill DE esistente `beast-preventivi`, molto più maturo su
  questo stesso dominio. La maggior parte del video CONFERMA quello skill (specialmente "mostralo
  in call" e "silenzio post-prezzo", quasi identici). **Tensione reale trovata e segnalata, non
  risolta automaticamente**: la Regola 4 del video (breakdown prezzi per componente su servizi
  complessi) è in apparente contraddizione con l'anti-pattern AP-05 di `beast-preventivi`
  ("preventivo formato fattura" = bloccante). Dettaglio e ipotesi di riconciliazione (non
  verificata) in `memory-empire/knowledge/EBU57iVAutA/enrichment-report.md`.
- RISULTATO: cat1-copywriting **24/29 completati** (5 rimanenti: 25-29). MASTER-RUN-TRACKER,
  STATO-EMPIRE, wiki/index.md aggiornati. Prossimo: video 25 (`uqa06rlgmj4`).

## 2026-08-25 (Empire Studio — cat1-copywriting completato a 20/29, piano 2 giorni NERVE-SOLVE, Claude)
- CONTESTO: Max ha chiesto un piano "one-shot" per finire l'intera missione (~81 video curati) in
  2 giorni. Applicato NERVE-SOLVE (D2): identificato che il vincolo dominante è il limite di spesa
  account (colpito 2 volte in <24h, sempre dentro Agent-tool paralleli, mai nel thread principale
  sequenziale) — dichiarata onestamente l'impossibilità di garantire "100% certo" senza sapere se
  il limite è mensile-esaurito o a finestra ricorrente (solo Max può verificarlo). Piano a 2 livelli:
  Livello 1 (quasi certo) = cat1 completo; Livello 2 (stretch) = cat2-7 secondo budget disponibile.
  Decisione: STOP batch paralleli, solo esecuzione sequenziale da qui in avanti.
- INGEST: video 18/29 (`VbxTgp_fz8Y`, "Revisione copy oF girl", 82s) — completato in sessione
  sequenziale (video-analysis.md già scritto da batch 2, Memory Empire + wiki costruiti da zero).
  41/41 frame (coverage 100%). 10 KA, 4 pattern. Terza conferma nel run del Pain Point Implicito;
  prima volta con "APSOC" mostrato letteralmente a schermo nel materiale sorgente esterno.
- INGEST: video 19/29 (`3zJpI8-7TW4`, "Pulsanti che vendono: ecco come fare i CTA", 7m14s) —
  pipeline completa da zero (solo Stage 1-2 fatti dal batch 2). 13/218 frame campionati. 17 KA,
  5 pattern — primo video del run focalizzato solo su CTA, con guest expert (Gaia, designer).
  Enrichment applicato: 2 patch a `cro-copy-architect/framework-apsoc-operativo.md` (formula CTA
  superficiale/profondo + meccanismo; design visivo del pulsante — primo contenuto UI/UX nello
  skill, con dato quantitativo ghost-button marcato DA VERIFICARE).
- VERIFICATO: video 20/29 (`IYd-VOngDog`) risultava già completo per intero (pipeline+ME+wiki) da
  un agente del batch 2 paralleli del 2026-08-24, sopravvissuto al limite di spesa prima di essere
  interrotto — verificato su disco, aggiunto a index.md (non ancora fatto in precedenza).
- RISULTATO: cat1-copywriting **20/29 completati** (9 rimanenti: 21-29). MASTER-RUN-TRACKER,
  STATO-EMPIRE, wiki/index.md aggiornati. Prossimo: video 21 (`wTpfKuHJhOE`, Hormozi writes his
  own copy), poi 22-29, poi cat2-cat7 curati.
## 2026-08-27 (task SECONDARIE W1 — infrastruttura Impero, Claude)
- Settimana 1 chiusa **6/6** (3 primarie + 3 secondarie).
- TASK-MEMORY-SYNC-W1: nuovo controllo pre-commit (`.githooks/`) che BLOCCA le collisioni
  di ID checkpoint e i CRLF nella memoria. Gate dimostrato con una collisione vera su due
  branch: `git commit exit = 1`. Scoperto che il fix di luglio non veniva usato perche
  `empire mem write` era rotto (`No module named yaml`), non per pigrizia.
- TASK-GITLFS-W1: **ADR-013** — gitignore mirato + guard 5MB, NON Git LFS. Il 70% dei 3,1 GB
  di repo sono PNG, e il motore della crescita sono le copertine KDP (~15 MB a libro), non
  gli screenshot come diceva B-008.
- TASK-ARENA-SESSION-W1: `shared/arena_session.py`, un solo motore di sessione per caroselli
  e arena_thumbnail (run reali su entrambi). Sbloccato il Ramo D dei caroselli, che moriva
  all'import su `playwright_stealth`.
- Nuova pagina: `concepts/Concept_Guardrail_Che_Si_Fanno_Rispettare.md` — il principio
  ricavato: una regola che dipende dalla buona volonta non e un controllo.


## 2026-08-27 (TASK-PUBLISHER-W1 — workflow di pubblicazione consolidato, Claude)
- INGEST: `Workflow pubblicazione automatica/` documentato per la prima volta in wiki →
  1 pagina creata (`tools/Tool_Workflow_Pubblicazione_Automatica.md`).
- Nuovo comando unico `pubblica.py`: una cartella di caroselli già pronti → dry-run
  verificato (default) o pubblicazione reale con `--live`. Gate chiuso sul ramo dry-run:
  6 slide + caption validate, canale dedotto, browser reale su instagram.com, exit 2
  (PASS PARZIALE — manca solo il login una tantum). Nessun post reale creato.
- Verifica onesta dello stato del folder: `push_social.py` era una SIMULAZIONE dichiarata
  obbligatoria dal CLAUDE.md locale, `main_orchestrator.py` non parte proprio, e il
  `publish()` di Instagram ingoiava ogni eccezione. Tutto documentato in
  `DIAGNOSI-PUBLISHER.md` + backlog B-023..B-027, invece di far finta che funzioni.
- Collegamento reale con [[Progetto_Preventa_Carousel]]: la cartella pubblicata è
  l'output di TASK-CAROSELLI-W1 chiuso lo stesso giorno.


## 2026-08-24 (Empire Studio — batch 1 chiuso: video 15/16/17 completati in ripresa, Claude)
- INGEST: video 15/29 (`yX0XZh2PSYo`, "Merge Tag nell'email marketing", 91s) — completato:
  mancava solo `enrichment-report.md` (video-analysis.md e wiki page già presenti da batch 1).
  46/46 frame (coverage 100%). 7 KA, 3 pattern. Enrichment applicato: patch a
  `emails/copy-guidelines.md` (fallback chaining generalizzato oltre il nome).
- INGEST: video 16/29 (`L5_Z63nxXjI`, "Ho rivisto i VOSTRI copy", 11m55s) — Memory Empire
  completo (4 file) + pagina wiki Source, partendo dal video-analysis.md già scritto dal batch 1.
  20/358 frame campionati (coverage 100% dei 6 copy mostrati). 19 KA, 4 pattern — il più denso
  del run cat1 fino a quel punto. Enrichment applicato: patch a
  `cro-copy-architect/pattern-persuasione-cro.md` (nota scarsità/registro brand di lusso).
- INGEST: video 17/29 (`Pv5uzIxp96U`, "Correggo i vostri copy", 33m00s) — pipeline completa da
  zero (Stage 1-2 erano gli unici già fatti dal batch 1): video-analysis.md scritto da transcript
  + 13/991 frame campionati, poi Memory Empire completo + pagina wiki Source. 24 KA, 5 pattern —
  il più denso del run cat1. Conferma indipendente della REGOLA 1 APSOC ("mai soluzione in
  headline") già esistente nel framework DE. Enrichment applicato: patch a
  `cro-copy-architect/pattern-persuasione-cro.md` (ancoraggio multi-livello / tre scatole).
- CHIUSURA BATCH 1: video 14-17/29 tutti completi (14 dal batch parallelo del 2026-08-23, 15-17
  completati in questa sessione di ripresa). cat1-copywriting: 17/29 completati. Checkpoint di
  chiusura: `company/Memory/checkpoints/CP-20260824-001.md` (verificare numerazione prima di
  scrivere).

## 2026-08-23 (Empire Studio — batch 1 paralleli: limite spesa colpito, video 14/29 completo, seconda collisione checkpoint riparata, Claude/Max)
- INGEST: video 14/29 (`nP4ojCzvjr8`, "L'email marketing dal POV dei lettori", 28s) completato
  da un agente parallelo — 14/14 frame letti, 6 KA, nessun concept nuovo (motivato). 1 pagina
  Source nuova.
- ESITO BATCH: lanciati 4 agenti paralleli (video 14-17), solo 1 completato per intero — gli
  altri 3 terminati a metà per limite di spesa mensile dell'account (non un problema di
  architettura: zero collisioni sui file condivisi tra i 4 agenti, isolamento verificato).
  Stato esatto di ripresa per video 15/16/17 in `MASTER-RUN-TRACKER.md` e
  `company/Memory/checkpoints/CP-20260823-010.md`.
- COLLISIONE CHECKPOINT (2ª di oggi, causa diversa): `CP-20260823-001.md` sovrascritto da
  un'altra sessione parallela (contenuto Fliki/YouTube non correlato) — riparato: originale
  ripristinato da git history, contenuto Fliki spostato in `CP-20260823-009.md`. Nessun
  contenuto perso.
- WATCH-001: N_video=14 (solo video 14 pienamente confermato Memory Empire completo in questo
  passaggio; 15/16/17 in stato intermedio, non ancora contati). Checkpoint: CP-20260823-010.

## 2026-08-23 (Empire Studio — Andrei Pascu cat1-copywriting video 13/29 chiuso, avvio batch parallelo, Claude/Max)
- INGEST: pipeline completa per `fGpz-uOgr4k` ("email marketing povero, email marketing ricco",
  29s, 15/15 frame letti = coverage 100%). 4 KA, 1 pagina Source nuova (nessun Concept nuovo:
  video ricicla pattern già catalogati nei video 11-12, non introduce contenuto tecnico nuovo).
  Attribuzione riga-personaggio (povero/ricco) segnalata esplicitamente come non verificata dai
  frame statici — nessuna caption on-screen, solo audio/VTT (principio NO-FINTO rispettato: non
  si inventa un'attribuzione che non si può confermare).
- DECISIONE MAX: scope missione confermato = ~81 video curati del tracker (non i 323 del canale
  intero). Approvato passaggio a batch paralleli di agenti (3-4 video insieme) per velocizzare le
  sessioni rimanenti, con architettura anti-collisione (agenti isolati per cartella video, nessuna
  scrittura su file condivisi da parte loro, serializzazione dei tracker fatta dal conduttore).
- WATCH-001: N_video=13, N_MemoryEmpire=13 → MATCH ✅. Checkpoint: CP-20260823-008.

## 2026-08-23 (Ponte memory-wiki-bridge + /sync-wiki-totale, Claude/Max)
- BUILD: Max ha chiesto conferma se tutto finisce automaticamente in wiki → no, solo Empire
  Studio ci arrivava (wiki-syncer). company/Memory (checkpoint/ADR/STATO-EMPIRE, REGOLA ZERO)
  non aveva nessun percorso verso la wiki — causa identica al buco 16gg trovato piu' sotto in
  questo stesso log (entry `## 2026-08-23` backfill). Costruito nuovo agente 7-file
  **memory-wiki-bridge** (gemello di wiki-syncer, reparto ingestion-archive di Memory Empire) +
  comando **`/sync-wiki-totale`** (zero domande, report MATCH/GAP, verifica grafo senza pagine
  orfane via knowledge-cartographer). ADR-012 registrato. Backlog storico B-019 (pre-luglio
  2026) lasciato esplicitamente fuori scope, richiede via libera Max. → 1 pagina wiki nuova
  (tools/Tool_Memory_Wiki_Bridge.md) + index.md aggiornato. CP-20260823-007.

## 2026-08-23 (Empire Studio continua — Andrei Pascu cat1-copywriting video 12/29, Claude/Max)
- INGEST: pipeline completa per `hb89lccIacY` ("10 strategie PROVATE per EMAIL copywriting per
  vendere sempre", 11m49s, 355 frame, 13 letti nativamente su 10 capitoli + outro dopo verifica
  formato uniforme talking-head). 20 KA, 4 pattern, 1 nuova Source page + 1 nuovo Concept page
  (CTR vs CR — trappola di lettura metriche, generalizzabile oltre l'email).
- ENRICHMENT REALE (non solo proposto): skill `emails` (`references/copy-guidelines.md`) patchata
  2 volte — sezione "Subject Lines" nuova (limite caratteri, no nome iniziale, no clickbait, emoji)
  + distinzione CR/CTR e caveat click-per-link aggiunti a "Metrics to Track".
- NOTA TECNICA: yt-dlp 2026.7.4 dava 403 Forbidden su questo video — aggiornato a 2026.8.19,
  risolto. Segnalato per sessioni future.
- WATCH-001: N_video=12, N_MemoryEmpire=12 → MATCH ✅. Checkpoint: CP-20260823-005 (004 era già preso da Cursor Grok, mappa Digital Empire — collisione risolta, nessun contenuto perso).

## 2026-08-23 (Empire Studio ripreso — Andrei Pascu cat1-copywriting video 11/29, Claude/Max)
- INGEST: run andrei-pascu-001 ripreso dopo blocco (mancava Python/yt-dlp/ffmpeg in sessione
  precedente, ora verificato presente). Pipeline completa per `nRm7JLsP1bc` ("Basta usare
  formule clichè di copywriting"): Stage 1-5 + Stage 7 + Memory Empire C-H. 23/23 frame letti
  (video 46s, coverage totale). 8 KA P12-traced. 1 nuova Source page + 1 nuovo Concept page
  (checklist anti-clichè hook, generalizzabile a tutto il copy/ads DE).
- ENRICHMENT-RESEARCH: vedi `company/Memory/memory-empire/memory/ingestions/2026-08-23-*.md`
  per proposta d'uso del contenuto nella skill `cro-copy-architect` (gate Attenzione/APSOC).
- WATCH-001: N_video=11, N_MemoryEmpire=11 → MATCH ✅. Checkpoint: CP-20260823-003.

## 2026-08-23 (Mappa root Digital Empire, Cursor/Max)
- MAPPA: censimento 49 cartelle di primo livello (~35k file, vendor escluso) + alberi di company, PIANO-MAESTRO, DIGITAL-EMPIRE, empire, wiki, fabbriche.
- ARTEFATTO: canvas `digital-empire-mappa.canvas.tsx` (schema a livelli, catalogo filtrabile, openFile sui file di verità).
- CP: `company/Memory/checkpoints/CP-20260823-004.md`

## 2026-08-06 (Primo carosello Preventa reale: Agent workspace Arena, non il motore grezzo, Claude/Max)
- CORREZIONE: `projects/Preventa/Progetto_Preventa_Carousel.md` descriveva il motore
  sbagliato (Playwright grezzo `ArenaAI/arena_generator.py`, 3 slide gradiente
  hardcoded). Il sistema reale "perfetto" di Max è un Agent workspace dentro Arena
  stessa, raggiungibile via una chat archiviata + comando `/inizio-generazione`.
  Pagina riscritta con il flusso verificato passo-passo.
- INGEST: primo carosello Preventa reale generato e scaricato (8 slide 4K + copy.json,
  11.35MB), verificato con unzip + ispezione visiva. 4 script Playwright riusabili
  scritti. Dettaglio in `company/Memory/checkpoints/CP-20260805-013.md`.

## 2026-08-05 (Pivot @Legamidiamore: audit reale sblocca blocco 07-22, Claude/Max)
- UPDATE: `entities/Entity_Legami_dAmore_Channel.md` — status da "⚠️ Da riconciliare — accessi
  ignoti" a "✅ Riconciliato". Login reale in YouTube Studio (credenziali fornite da Max in chat,
  mai salvate su disco) conferma: canale suo, monetizzato, 14.793 iscritti, revenue €44,02/28gg
  (quasi nulla nonostante i numeri — confermata la diagnosi del 07-22). Corretto anche un dato
  vecchio: non è inglese, è quasi tutto italiano (scrape reale, 60 video). → 1 pagina aggiornata.
- CONTESTO: Max ha messo in pausa il progetto Dose Mentale-copia per dare priorità a questo
  canale esistente. Dettaglio tecnico in `company/Memory/checkpoints/CP-20260805-009.md`.

## 2026-08-05 (Secondo incarico a Neri: fabbrica strategie S7 via Arena, Claude/Max)
- PLAN: Max ha chiesto un prompt completo e autosufficiente per Neri, da usare in Arena.ai per
  progettare una "fabbrica" che genera un agente-strategia dedicato per ogni strategia di
  trading di Stream S7 (oggi: memecoin + NFT, entrambe già costruite). Riusato il metodo
  esistente `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md`, non reinventato. Scritto
  `company/Memory/tasks/TASK-NERI-20260805-S7-STRATEGY-FACTORY-ARENA.md` (fuori wiki, artefatto
  operativo di Memory — qui solo il log e l'aggiornamento di [[entities/Neri]]). Segnalata
  esplicitamente la tensione con l'altro task di Neri (Go/No-Go non ancora consegnato): la
  progettazione via Arena procede in parallelo (zero capitale/esecuzione), gli agenti generati
  restano paper-trading-by-default finché Max non decide.

## 2026-08-03 (Fase 1 + Fase 3 outreach Preventa: filtro import reale + Reparto Produzione, Claude/Max)
- INGEST: chiusura Fase 1 (filtro solo-import reale, bug `categoria` vacuo trovato e
  corretto, verificato su Areus reale 8/29 lead) — CP-20260803-005, nessuna pagina wiki
  nuova (dettaglio tecnico, vive nel checkpoint).
- INGEST: Fase 3, mappati 3 motori caroselli reali sul disco (confusi tra loro fino ad
  oggi) e confermato con Max quale intendeva. Creato Progetto Preventa sotto un nuovo
  concetto "Reparto Produzione" → 2 pagine create:
  [[concepts/Reparto_Produzione_Digital_Empire]], [[projects/Preventa/Progetto_Preventa_Carousel]].
  Sicurezza segnalata (non risolta): credenziali Arena/API in chiaro in
  `caroselli - agency/config.py`, committate in git.

## 2026-08-03 (Primo incarico reale a Neri: strategia Stream S7, Claude/Max)
- PLAN: Max ha chiesto un piano strategico per Stream S7 e di passare l'iniziativa a Neri
  (ricerche, report, architetture). Scritti `company/Ecosistemi/12-STREAM-S7-BOT/
  PIANO-STRATEGICO-S7.md` + `company/Memory/tasks/TASK-NERI-20260803-STREAM-S7-STRATEGIA.md`
  (fuori wiki, sono artefatti operativi di Memory/ecosistema — qui solo il log e l'aggiornamento
  di [[entities/Neri]]). Convergenza notata con CP-20260803-001 (sessione diversa, stessa
  diagnosi indipendente: "non manca codice, manca una decisione"). Interpretazione segnalata:
  passa lo strato strategico a Neri, non l'esecuzione tecnica (resta di Gael).

## 2026-08-03 (Metodo Arena → Workflow Completo, Claude/Max)
- INGEST: Max ha chiesto un piano dettagliato per usare Arena + skill `master-build-architecture`
  + motore APEX-7 (`11-APEX-7-CORE`, ADR-010) per costruire workflow completi (agenti/skill/
  flussi/automazioni). Recuperato dossier 26 (Arena: contratto operativo) da git — perso dal
  disco in un rebase, mai ripristinato — e riletto `13-ARENA-APEX/ECOSISTEMA.md` (Regola APEX:
  nessun agente esce dall'Arena senza APEX-7 integrato/testato). Creato
  `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md` — metodo riusabile in 3 fasi (Arena
  progetta → Claude Code costruisce nel ciclo 9 passi → APEX-7 gate obbligatorio), con prompt
  di apertura pronto e checklist di accettazione. 1 entry aggiunta in index.md
  (Metodologie di Sviluppo).

## 2026-07-30/31 (Bibbia dei Messaggi Outreach + team agenti, Claude/Max)
- INGEST via `/content-forge`: trascrizione video + 2 rielaborazioni di Max sul framework
  LinkedIn cold outreach (Barnum Effect, Rainbow Effect, 5 Pilastri, sequenza follow-up
  3-step) → sorgente grezzo `Outreach/knowledge/raw_linkedin-cold-outreach-framework_2026-07-30.md`
  (7.288 parole). Pipeline completa (KG 16 atomi/6 cluster → MKD → team) in
  `Outreach/forge-run-2026-07-30T-outreach-bible/`.
- BUILD: MKD pubblicato come **Bibbia dei Messaggi** (regola non derogabile, richiesta
  esplicita di Max) in `Outreach/knowledge/bibbia-messaggi-outreach.md` (+glossario+FAQ+schemi).
  Team di 4 agenti (`rule-keeper` gatekeeper, `message-writer`, `case-study-forge`,
  `followup-sequencer`, 7 file canonici ciascuno) in `Outreach/agents/outreach-message-team/`.
- 3 pagine wiki create: [[concepts/Framework_Cold_Outreach_APSOC]] (colmato link dangling
  già presente in index.md), [[concepts/Framework_Barnum_Rainbow_5Pilastri]],
  [[tools/Tool_Outreach_Message_Team]]. index.md sezione Framework aggiornata.
- Cross-link con lavoro già in produzione: `personalizza_messaggi.py` (campagna
  concessionari-preventa) aveva già un Gancio 4 "import" che applica lo stesso principio
  (variabile hard-coded di nicchia) — la Bibbia lo rende esplicito/canonico invece che
  implicito in un singolo script.

## 2026-07-30 (Nuovo membro team: Neri, Claude/Max)
- INGEST: Neri si è unito al team (gestione organizzativa/piani/metodi, non operativo) →
  1 pagina creata [[entities/Neri|Neri]], linkata a [[projects/Piano_Maestro_EMPIRE_OS]],
  [[concepts/SPARC_Methodology]], [[projects/Preventa/Preventa_Logica_Completa_Metodo]].
  Aggiunta sezione "Team" in index.md. Specchio anche in `company/Memory/STATO-EMPIRE.md`
  (nota organi/coordinamento) e memoria persistente Claude (`project_team_neri.md`).

## 2026-07-30 (CORREZIONE — Stream S7: logica completa documentata, Claude/Max)
- Max ha corretto: la richiesta era sul bot S7 (NFT/memecoin Solana), non su Preventa
  (voce sotto, lasciata perché comunque valida ma fuori bersaglio). Letto codice reale
  (`main.py`, `data_manager.py`, `analysis_engine.py`, `risk_manager.py`,
  `execution_engine.py`, `position_monitor.py`, `report-studio.md`, `APEX-7.md`,
  checkpoint CP-20260728-006) → file creato direttamente in
  `company/Ecosistemi/12-STREAM-S7-BOT/LOGICA-COMPLETA-S7.md` (non in wiki: doc tecnico
  legato al codice, resta accanto ad esso). Punto centrale: `report-studio.md` boccia
  già il live trading (expectancy negativa, >85% rischio perdita capitale primo mese) —
  S7 è R&D speculativo 0€ revenue, non un percorso di incasso attuale.

## 2026-07-30 (Preventa: logica completa documentata, Claude/Max)
- INGEST: mappata e documentata tutta la logica del sistema Preventa (scraping import-focus →
  qualificazione → Areus → ganci → invio WhatsApp reale → follow-up), letta dal codice reale
  (`outreach_giornaliero.py`, `run.py`, `checker.py`, `areus.py`, `personalizza_messaggi.py`,
  `send_message.py`, `refresh_session.py`) + checkpoint CP-20260729-007. → 1 pagina creata:
  [[projects/Preventa/Preventa_Logica_Completa_Metodo|Preventa — Logica Completa del Sistema]].
  Obiettivo: base per fissare il Metodo prima di scalare l'operativo.

## 2026-07-23 (Task board Gael operativo + prompt Gemini S7 pronto, Claude/Max)
- PLAN: dossier 25 = task board Gael autorevole. Scoperta chiave: **il lavoro è cablaggio, non costruzione**.
  Asset già su disco: `Outreach/preventa-outreach-pack/` (6 script APSOC concessionari già scritti),
  `Outreach/Outreach Workflow/` (motore live empire_auto_v3.py), `.claude/skills/youtube-automation-factory/`
  (skill completa con conductor+6 operatori+4 gate, mai eseguita). Ordine: G-A outreach concessionari 100%
  auto → G-C sito Preventa+PROVE → G-B YouTube 100% auto → G-D manutenzione.
- BLOCCHI nuovi per Max: M-EST-8 canale YouTube + credenziali API (blocca upload auto), M-EST-9 province scraping.
- S7: prompt copia-incolla per Gemini pronto (`GEM-07-PROMPT-DA-INCOLLARE-S7.md`), paper-trading first.

## 2026-07-23 (Calendario esecutivo V2 + S7 NFT bot delegato Gemini, Claude/Max)
- PLAN: dossier 24 = calendario giorno-per-giorno dal 23/07 (Opzione B outbound). Task Gael (G-EST-1..5) +
  Max (M-EST-4,6,7) sui giorni. Sostituisce il calendario 21→26 del P7.
- DECISIONE D-EST-007: bot NFT/memecoin (S7) APPROVATO come R&D delegato a Gemini, paper-trading first,
  €0 nel piano revenue estate, esecuzione 100% Gemini (isola S1/S2). Brief: `Antigravity-Briefs/GEM-07-S7-NFT-BOT-BRIEF.md`.
  Report S7 analizzato: tecnicamente solido e onesto, ma framing vecchio (Manuale/€131k) riallineato.

## 2026-07-23 (Analisi prodotti DE + IG morto, Claude/Max)
- ANALISI: dossier 23 (potenziale prodotti). Dato reale dal codice `agency-empire/`: i workflow costano
  **€5.000-15.000** (non SaaS). 1 vendita workflow > tutti i 7 concessionari settembre. Riprioritizzazione:
  🥇 Outreach Factory via dogfooding (usare la ns macchina outreach su noi stessi per prenotare demo) ·
  🥈 Preventa (cash veloce volume, sezione sito separata) · 🥉 Content Factory · Corso/Second Brain giù.
- FATTO: IG `crea.illtuo_impero` a zero → fork D-EST-006 risolto in Opzione B (tutto outbound freddo),
  Corso CCM parcheggiato per l'estate. Blocco n.1 = lead freddo + 1 prova (Novacar case study), non altri prodotti.

## 2026-07-23 (Piano Estate V2 diversificato + dati YouTube reali, Claude/Max)
- ANALISI/PLAN: dossier 22 (piano estate V2). Corretti 2 errori miei: prodotto = Corso CCM (non "Manuale"
  = lead magnet); 7 concessionari = settembre non luglio. 5 stream diversificati (Preventa-freddo, Corso
  lean, prodotti sito agency-empire + sezione Preventa, NFT lane speculativa separata, YouTube funnel).
  Fork strategico D-EST-006. Task board Gael (G-EST-1..4) + Max (M-EST-1..5). Verificati su disco:
  `Lancio corso skill beast/` (infra corso completa) + `agency-empire/` (Next.js, 2 workflow live).
- DATI: 2ª estrazione yt-dlp Dose Mentale + Legami d'amore → conferma dossier 20. Prova decisiva sul
  canale-90€: Legami ha già 14.700 iscritti (14× i 1.000 comprabili) e rende ~nulla → gli iscritti non
  sono l'ingrediente mancante, è la view-per-video. Titoli duplicati/ri-uploadati = macchina a churn.
- NFT: 4 video queued per Empire Studio (lane speculativa, capitale a rischio, fuori piano principale).

## 2026-07-22 (Gate-FUNNEL: 4 blocchi reali trovati, Gael/Claude)
- AUDIT: verifica diretta post-CP-023 (che dichiarava "checkout integrato") — trovato invece che
  i link Stripe in `Crea siti/Siti CCM/manuale.html` sono placeholder mai sostituiti (bottone finto),
  l'audit pagine prerequisito non è mai stato fatto, la landing non è deployata su alcun dominio.
  Chiarita con Gael l'identità di `crea.illtuo_impero` (sua pagina personale) — password fornita in
  chat NON salvata in nessun file (regola chiavi solo .env). Preparato il testo bio pronto da
  incollare (manca solo l'URL live). → CP-20260722-003 + STATO-EMPIRE aggiornati con dettaglio
  esatto per ogni blocco.

## 2026-07-22 (Analisi YouTube reale + piano chirurgico estate, Claude/Max)
- RESEARCH/INGEST: estrazione dati REALI via yt-dlp di 3 canali (Dose Mentale @dosementale 198k iscritti
  ma video recenti 649-3300 view = ratio 0,3% gonfiato; Legami d'amore @Legamidiamore 14.7k iscritti,
  471 video, GIÀ attivo inglese — NON il "canale dormiente" che Max ricordava; Andrei Pascu @andreipascu
  solo 8.040 iscritti YouTube, 100-500 view/video). SCOPERTA CHIAVE: Andrei guadagna da PRODOTTI (ebook
  €79 + corso €434), non da adsense — modello autorità→prodotto rende ~100× per spettatore vs faceless→view.
  YouTube-adsense NON è leva cash-7gg; YouTube-funnel-verso-Manuale sì. → 3 pagine: Entity_Dose_Mentale_Channel,
  Entity_Legami_dAmore_Channel, correzione entities/Andrei_Pascu (270k era TikTok/IG, YouTube reale 8k).
  Deliverable: PIANO-MAESTRO/20-ANALISI-YOUTUBE-PIANO-CHIRURGICO.md (piano con confidenza dichiarata per
  riga, pre-mortem) + 19-ARENA-BUILD-LIST.md (8 build + 6 prompt pronti per Arena). DEC-EST-001 sbloccata
  (Manuale €67, veto scaduto). Confidenza onesta ≥1 incasso entro 26/07: ~65-80%, non 99%.

## 2026-07-21 (YouTube Automation Factory — nuova skill, Max)
- INGEST + BUILD: trasformato il workshop YouTube Automation (Video IQ · SEO/certificazione ·
  Fliki · teoria hook/intro/CTA) nella skill operativa `.claude/skills/youtube-automation-factory/`
  (comando `/yt-factory`). Costruita con le 2 skill clonate `ansjkfgheqrlg/master-build-architecture`
  (struttura: 3 livelli, memoria dal passo zero) + `ansjkfgheqrlg/content-forge2.0` (espansione, MKD).
  29 file: kernel (SKILL/MKD/ARCHITECTURE) + 11 agenti (conductor + 6 operatori + 3 gate/audit +
  memory-keeper) + 5 workflow (pipeline 6 fasi con feedback) + 4 reference + 2 tool Python testati
  (`seo_score.py` 0-100, `cashcow_check.py` indice cash cow) + evals + memoria. Serve la linea
  revenue **S5 YouTube-Fliki auto** (dossier 16). → 1 pagina wiki: Concept_YouTube_Automation_Factory.

## 2026-07-21 (Empire Desk B2/B3/B4 — verificati a runtime, Gael)
- BUILD/TEST: `modules/notify.py` (toast Windows nativo PowerShell/WinRT, zero dipendenze pip) +
  `modules/taskboard.py` (task board Max/Gael, seed 18 task reali da dossier 16). Sbloccato Python
  3.12/Node 24 (già installati da sessione precedente via winget, serve solo l'export PATH giusto)
  → primo test a runtime REALE di tutto il seam B1-B4: selftest 15/15 sia in dev sia dall'.exe
  frozen già esistente (senza ricostruirlo). Test funzionale diretto delle routes ha trovato 2 bug
  reali (non visibili dal solo selftest): validazione tile saltata in scheduler.aggiungi con host
  non pronto, id collidenti nello stesso secondo — entrambi corretti e ri-verificati.
  → CP-20260721-001 + REGISTRO-ERRORI EDE-9/10/11 + STATO-EMPIRE aggiornati.

## 2026-07-20 (Empire Studio — video 10/29, Gael)
- INGEST: Empire Studio — video Ahp_6rHSOsU (Andrei Pascu, cat1-copywriting, video 10/29). Formato tutorial screen-share 11m08s — Google Docs (macOS) + talking head PiP. Stage 1-5 completati: 334 frame @2s (3-digit naming), 16 frame letti nativamente, NO-FINTO PASS. 16 VP schermo: doc diviso pagine→senza pagine, menu File Impostazione pagina, Google Drive file list, outline heading popolato, note gialle "[inserire logo]"/"[inserire capibara]", menu dropdown stato, badge [in corso]/[da iniziare], indice+segnalibro, pannello Stili "Aggiorna Intestazione", contatore parole live, outro CTA. VTT 2505 righe letto integralmente (9 capitoli ufficiali del video). 20 KA P12-traced. Concepts: pulizia formato no-pagine, heading→outline navigabile, aggiorna stile in blocco, note colorate come heading dedicato, dropdown stato = mini-kanban, segnalibri+link, conteggio caratteri live, sistema cartelle Clienti visibile/non-visibile. → 2 pagine create: Source_Andrei_Pascu_Google_Docs_Copywriter, Concept_Google_Docs_Copywriter_Workflow. index.md +2 entry sezione Copywriting. WATCH-001: N_video=10 = N_MemoryEmpire=10 → MATCH ✅

## 2026-07-19 (Empire Desk — collisione UI risolta, Gael)
- FIX/COORD: scoperta al pull una collisione reale — Max ha ridisegnato `EmpireDesk/ui/index.html`
  in parallelo (nav-tab "Empire Premium") con lo stesso obiettivo del mio switcher pannelli, ma
  un contratto di rete diverso (`/api/modules` vs il mio `/api/panels`). Risolto merge manuale
  (8 blocchi): tenuto il design di Max, `app.py` riallineato al suo contratto esatto
  (`modules_public()`, route `api/modules`, chiave `panel_html`). STATO-EMPIRE aggiornato da Max
  nel frattempo: ownership `ui/index.html` passata a Max — confermato, Gael non lo tocca più.
  → CP-20260719-008 + REGISTRO-ERRORI EDE-8.

## 2026-07-19 (Empire Desk B1 — seam moduli, Gael)
- BUILD: `EmpireDesk/app.py` — loader `modules/*.py` (contratto dossier 17 §5.3): import isolato
  per file (un modulo rotto si segnala e si salta, mai crash dell'app), validazione schema tile
  anti-KeyError, dispatcher routes condiviso HTTP/pywebview, `global_selftest()` che include ogni
  modulo. `ui/index.html`: switcher "Pannelli" (tab per modulo) + CSS per le classi già usate dai
  3 pannelli di Max (metrics/revenue/licenze) — senza sarebbero apparsi senza stile. Fix grafico
  proattivo: header da posizionamento assoluto calcolato a mano a `display:flex` (eliminato rischio
  sovrapposizione bottoni). 2 bug trovati e corretti in autorevisione prima di ogni lancio (EDE-6/7).
  **NON eseguito**: sessione senza Python/Node → verifica reale rimandata a macchina con l'ambiente
  giusto. → CP-20260719-007 + STATO-EMPIRE aggiornati.

## 2026-07-19 (Empire Desk v0.1 — P1-P3, Gael)
- BUILD: nuova cartella `EmpireDesk/` — app launcher `.exe` di tutte le automazioni Digital Empire
  (ordine Max, dossier `PIANO-MAESTRO/17-EMPIRE-DESK-APP.md`). `app.py` con 3 motori GUI in
  fallback (Chrome-app → pywebview → Tkinter, applicato subito il pattern anti-WebView2 di
  CP-20260715-001), `TileManager` (subprocess reale su 8 automazioni + poll log-live + selftest),
  `ui/index.html` premium slate+argento+arancio `#fb4604`. 3 bug reali trovati e corretti in
  revisione statica del codice (sys.executable da frozen rilanciava l'app invece dello script;
  WinError193 su .bat senza cmd.exe /c; pause-hang su AVVIA-EMAIL-LIVE.bat/_avvia_ig.bat senza
  stdin=DEVNULL). Trovato ma non toccato: path hardcoded di un'altra macchina nei bat Outreach
  (ADR-003, fuori scope). **P4 (selftest+build exe) bloccato**: sessione senza Python/Node
  installati → da completare su macchina reale. → CP-20260719-002 + STATO-EMPIRE aggiornati.

## 2026-07-19 (V2-2 Lotto 3 — Gael)
- INGEST/BUILD: PIANO-MAESTRO, 5 dossier V2 nuovi via swarm 3 agenti paralleli: `05-ECOSISTEMA-MULTIBUSINESS-V2.md` (12 reparti, 72 agenti, nuovo reparto trasversale MB-Portfolio) + split del v1 `06-ECOSISTEMI-CORE.md` in `06a-ECOSISTEMA-PLATFORM-V2.md` (45 agenti), `06b-ECOSISTEMA-FORGE-V2.md` (40 agenti), `06c-ECOSISTEMA-INTELLIGENCE-V2.md` (35 agenti), `06d-ECOSISTEMA-OPERATIONS-V2.md` (37 agenti). Decisione: naming `06a/06b/06c/06d` per evitare collisione con dossier 07/08/09 già esistenti. Gate automatico verde (0 stub, 13/13 sezioni), review a campione fatta. `V2-INDEX.md` e `STATO-EMPIRE.md` aggiornati. → CP-20260719-001.

## 2026-07-11 (Empire Studio — video 9/29)
- INGEST: Empire Studio — video IWCHN_mE2Vo (Andrei Pascu, cat1-copywriting, video 9/29). Formato live session 1h02min — screen share Meta Ads Library + talking head PiP. Stage 1-5 completati: 1858 frame @2s (4-digit naming), 14 frame letti nativamente, NO-FINTO PASS. 12 VP schermo: Meta Ad Library homepage (Latvia location), gaming search Italy, filter stack ~98 results Laurea Online, real estate ads, EU Transparency Women 30-55 Reach 1770, shoe store owner DIY ad, Carisma shoes lifestyle, Andrei nighttime, palestra A/B test boxing, royal costume supermarket food ad, Corte CAB VANIGLIA dessert. VTT 11730 righe letto integralmente. 25 KA P12-traced. Concepts: Meta Ads Library stack, EU Transparency intelligence, Video vs Photo rule, Template Ads detection, Dan Lock Gap, Chiarezza > Creativita, email=staple ecommerce. → 2 pagine create: Source_Andrei_Pascu_Ads_Library_Live, Concept_Meta_Ads_Library_Competitor_Research. WATCH-001: N_video=9 = N_MemoryEmpire=9 → MATCH ✅

## 2026-07-09 (Empire Studio — video 8/29)
- INGEST: Empire Studio — video lQMO0LdeI2c (Andrei Pascu, cat1-copywriting, video 8/29). Formato live session 44:55 — screen share McFit+Dyson + talking head PiP. Stage 1-5 completati: 1348 frame @2s (4-digit naming), 13 frame letti nativamente, NO-FINTO PASS. 6 VP schermo: McFit Hero "SEMPLICEMENTE IN FORMA", Google search "simply fit", McFit+ loyalty, Dyson Airwrap headline errore, Dyson trust badges, Dyson v15s scarcity. VTT 8545 righe letto integralmente. 29 KA P12-traced. Concetti: Hero Section, Brand Famoso Rule, Headline NEQ Nome Prodotto, CLV, CPA leva, Slogan Vibes vs DR, loss leader, knowledge=pricing leva. → 2 pagine create: Source_Andrei_Pascu_Copywriter_Analizza_Live, Concept_CLV_Customer_Lifetime_Value. WATCH-001: N_video=8 = N_MemoryEmpire=8 → MATCH ✅

## 2026-07-09 (Empire Studio — video 7/29)
- INGEST: Empire Studio — video iy13HC9M8z0 (Andrei Pascu, cat1-copywriting, video 7/29). Formato screencast live ChatGPT. Stage 1-5 completati: 255 frame @--interval 2, 13 frame letti nativamente, NO-FINTO PASS. 4 VP ChatGPT screen documentati: warm-up, Prompt 1 tazze (3 frame continui), Prompt 2 specifico. VTT 8:29 letto integralmente. 26 KA P12-traced. Concetti estratti: GPT Ceiling Effect, AI-as-Floor Strategy, Prompt-Quality Law. → 2 pagine create: Source_Andrei_Pascu_Ho_Corretto_ChatGPT_Copywriting, Concept_AI_vs_Copywriter_Limiti_e_Usi. WATCH-001: N_video=7 = N_MemoryEmpire=7 → MATCH ✅

## 2026-07-09 (Empire Studio — video 6/29)
- INGEST: Empire Studio — video 6WMkz5Q8g6g (Andrei Pascu, cat1-copywriting, video 6/29). Stage 1-5 completati: 131 frame @--interval 2, 11 frame letti nativamente, NO-FINTO PASS. Props fisici documentati: Beats headphones (VP-001) + action cam GoPro-like (VP-002) + end card (VP-003). VTT 4:21 letto integralmente. 22 KA P12-traced. Nuovo concept: Feature vs Benefit (formula operativa + checklist audit). → 2 pagine create: Source_Andrei_Pascu_4_Consigli_Testi_Persuasivi, Concept_Feature_vs_Benefit_Copy. WATCH-001: N_video=6 = N_MemoryEmpire=6 → MATCH ✅

## 2026-07-09 (Empire Studio — video 5/29)
- INGEST: Empire Studio — video sTCwYnWmgcQ (Andrei Pascu, cat1-copywriting, video 5/29). Stage 1-5 completati: 375 frame @--interval 2, 12 frame letti nativamente (1 black screen, NO-FINTO PASS), VTT 12m29s + 5 capitoli. 22 KA P12-traced. Nuovo concept: "valore anticipato" nella freelance acquisition. → 2 pagine create: Source_Andrei_Pascu_Copywriter_Zero_Esperienza, Concept_Valore_Anticipato_Freelance. WATCH-001: N_video=5 = N_MemoryEmpire=5 → MATCH ✅

## 2026-07-09 (Empire Studio — video 4/29)
- INGEST: Empire Studio — video t67-j2LiXgQ (Andrei Pascu, cat1-copywriting, video 4/29). Stage 1-5 completati: 399 frame estratti @--interval 2, 11 frame letti nativamente (NO-FINTO PASS), VTT 13m17s letto integralmente, 22 knowledge atoms P12-traced. Visual passages: frame-079 (email Parola di Librai), frame-085 (ad Torpado MTB direct response). → 2 pagine create: Source_Andrei_Pascu_Copywriting_Freelance_Autonomo, Concept_Pain_Amplification_Urgency_Copy. index.md +2 entry sezione Copywriting. WATCH-001: N_video=4 = N_MemoryEmpire=4 → MATCH ✅

## 2026-07-09 (Empire Studio — video 3/29)
- INGEST: Empire Studio — video jgIgOPAnYNY (Andrei Pascu, cat1-copywriting, video 3/29). Stage 1-5 completati: 611 frame estratti @--interval 2, 12 frame letti nativamente, VTT 20:21 letto integralmente, 24 knowledge atoms P12-traced. NO-FINTO: PASS. → 3 pagine create: Source_Andrei_Pascu_Copywriting_Tutorial_Completo, Concept_APSOC_Formula, Concept_Briefing_Checklist_Copywriter. index.md +3 entry sezione Copywriting.

## 2026-07-15
- FIX CRITICO GUI (E11): PreventivoForge — la GUI premium non dipende più da WebView2. Nuovo motore `main_chrome_app()`: `ui/index.html` servita da mini-server locale + finestra Google Chrome `--app` (Chrome già richiesto → sempre presente). Bridge JS↔Python via POST /api/. Ordine motori: Chrome-app → pywebview → Tkinter. Causa: sul PC cliente mancava WebView2 → pywebview ripiegava in silenzio su Tkinter (GUI vecchia); non riproducibile da Max (WebView2 presente sul suo PC). Verificato estraendo lo zip come Novacar → premium OK. Consegna: `CONSEGNA-NOVACAR-NUOVA/PreventivoForge-v2.1-13lug.zip` (cartella interna PreventivoForge-v2.1, LEGGIMI-PRIMA, bollino versione). → REGISTRO-ERRORI E11 + regole 12-13.

## 2026-07-09
- GUI: PreventivoForge — freccia "indietro" archivio spostata in alto a DESTRA e centrata nel quadratino (flex, `.hbtn.back.show`), non più sopra il titolo. Zip consegna ripulito 117.4 MB (svuotato `_internal/Memory/storico-preventivi/` dai test). CHECKLIST-CONSEGNA aggiornata.
- REGOLA GLOBALE PREZZO: PreventivoForge — `render_pdf.py::_price_novacar`: UNA voce "Immatricolazione, pratiche e trasporto" (1.500); il 2° fisso (1.500) = guadagno, SOMMATO alla voce "Prezzo autovettura" (listed+fixed_2) → voci visibili tornano col totale. Vale per ogni preventivo. Totale invariato. → CP-20260709-002 + STATO-EMPIRE.
- BUILD: PreventivoForge — archivio si svuota a ogni chiusura app (`archivio.clear()` cablata in `app.py` webview+Tkinter). Exe consegna ribuildato (2026-07-09 10:15), zip rigenerato 117.4 MB. → CP-20260709-001 + STATO-EMPIRE aggiornati.

## 2026-07-05
- DIRETTIVA: Max concede a Gael **libero arbitrio 2026-07-06 → 2026-07-08 compresi** (PreventivoForge/test/fix/Impero — decide lui). Oggi non attiva; dal 09-07 torna ordine Impero. → CP-20260705-002 + STATO-EMPIRE + memory aggiornati.
- INGEST: Empire Studio — video qOK4WP82Bvo (Andrei Pascu, cat1-copywriting, video 2/29). Stage 1-5 completati: 515 frames estratti, VTT 3999 righe letto integralmente, 22 knowledge atoms P12-traced. → 3 pagine create/aggiornate: Source_Andrei_Pascu_Copywriting_Intro, Concept_Value_Gap_Copywriter, Concept_Conversion_Rate_Moltiplicatore. index.md aggiornato.

## 2026-07-04
- INGEST: Direttiva Max — nuovo organo **ISPETTORATO GENERALE** (Performance & Autocritica).
  Piano completo → `PIANO-MAESTRO/15-DOSSIER-ISPETTORATO.md` (report dopo ogni run, daily
  autocritica, REGISTRO-ERRORI + gate anti-recidiva, riporta a Board/MAXIMILIAN/Max).
  Owner build: Max, fasi M1→M5. CP-20260704-001 + STATO-EMPIRE aggiornati. → 1 dossier creato.

## 2026-07-19
- INGEST: PIANO ESTATE REVENUE (dossier 16) — strategia fatturato 7gg: S1 concessionari anticipati (≥95%), S2 Manuale CC (B-003 da chiudere G1), S3 pagine lancio, S4 mentalita.brutale (solo se auto 100%, carousel-factory wrap), S5 YouTube-Fliki auto (API in .env locale) → 1 dossier + task board Max/Gael in STATO

## 2026-07-24
- BUILD: **WORKFLOW ESTATE completato** — `python -m empire estate` → exit 0 (11 controlli su 13;
  conform 0 block, 207 test). Piano a 3 livelli L1→L2→L3 (ognuno corregge i limiti dichiarati del
  precedente) + `ARCHITETTURA-COMPLETAMENTO.md` + swarm a 6 lotti con perimetri disgiunti.
  Nuovi: `empire/estate.py` (verdetto unico), `flow/decisions.py` (default-più-veto ADR-EST-006),
  `flow/evidence.py` (guardia di provenienza sui dati), `inspect/metrics.py` (6 KPI telemetria),
  `tools/video_pack.py`, landing Preventa. CP-20260724-001.
- LEZIONE (trasversale, vale oltre l'estate): **un controllo che in caso di dubbio rassicura è
  peggio di nessun controllo.** Tre difetti indipendenti della stessa famiglia trovati in un giorno:
  la dashboard coloriva di verde i valori che non sapeva leggere; l'anagrafe ADR-008
  (`skills-map.yaml`) era YAML non valido perché letta solo a occhio, mai da una macchina;
  `video_pack --check` approvava il proprio scheletro. Corollario operativo: ogni registro va
  caricato da un parser almeno una volta, o non è un registro.
- FINDING aperto: i 7 lead di `lead.csv` hanno **0/7** riscontri nelle sorgenti `Outreach/`; i 61
  lead reali dichiarati il 23/07 non esistono su disco. Gate-CONTATTI lasciato rosso di proposito.
  → 0 pagine wiki nuove, 1 lezione registrata.

## 2026-08-03
- INGEST: studio copy @dosementale rigenerato su 36 video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Dose_Mentale.md)

## 2026-08-05
- INGEST: studio copy @dosementale rigenerato su 36 video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Dose_Mentale.md)

## 2026-08-06
- INGEST: studio copy @Legamidiamore + 4 competitor rigenerato su 176 video reali → 1 pagina aggiornata (synthesis/Studio_Copy_Legamidiamore.md)

## 2026-08-22
- INGEST: NERVE-SOLVE (Orchestration Layer 1 — Problem Solving Engine) estratto da `SKILL & Agenti/Orchestracion Layer - Problem solving.zip`, distillato architettura v2.2 in skill Claude Code operativa `.claude/skills/nerve-solve/` (mirror `.agents/skills/`), scartato kernel Python crittografico orfano della fonte. Registrato in `company/skills-map.yaml` (ADR-008) sotto 08-INTELLIGENCE/Cognitive-Control. → 1 pagina wiki nuova (tools/Tool_Nerve_Solve_Orchestration_Layer.md) + index.md aggiornato.

## 2026-08-23
- BACKFILL (buco reale trovato, non simulato): `log.md` non aveva NESSUNA entry tra 2026-08-06 e 2026-08-22 (16 giorni), mentre `company/Memory/checkpoints/` ha 16 checkpoint reali nello stesso periodo (libro KDP, primo video YouTube pubblicato, wrapper IG Preventa, fix self-healing WhatsApp, ecc.) — la causa è l'esistenza di due sistemi di memoria paralleli: `company/Memory/` (REGOLA ZERO) è stato rispettato sempre, la wiki (REGOLA FONDAMENTALE) no. Colmato lo scope concordato con Max (solo il gap 06→22 agosto, non tutta l'estate): 2 pagine nuove (entities/Entity_The_Quiet_Hours_Libro_KDP.md, tools/Tool_Pipeline_Libri_KDP.md — primo libro KDP mai completato, prima non aveva NESSUNA pagina) + 3 pagine aggiornate (entities/Entity_Legami_dAmore_Channel.md: primo video reale pubblicato + 3 in produzione + 4 bug fix; projects/Preventa/Preventa_Logica_Completa_Metodo.md: fix self-healing rete su invio WhatsApp; projects/Preventa/Progetto_Preventa_Carousel.md: wrapper pubblicazione IG dry-run) + index.md aggiornato. Il resto dell'estate (prima di giugno-luglio) NON è stato auditato — richiede via libera esplicita separata.

---

# BACKFILL STORICO 2026-06-10 → 2026-08-20 (eseguito 2026-08-24, `/sync-wiki-totale`, permesso esplicito di Max)

Colma le 30 date con checkpoint reale in `company/Memory/checkpoints/` (228 checkpoint su 47
date di lavoro reale) ma senza nessun riscontro in questo log — il gap storico lasciato
esplicitamente fuori scope dal backfill del 2026-08-23 (B-019). Ordine cronologico
(vecchio→nuovo). Dettaglio checkpoint per checkpoint in `company/Memory/checkpoints/CP-*.md`.

## 2026-06-10 (Piano Maestro EMPIRE OS + GitHub monorepo, Claude/Max)
- BUILD: prodotto il piano fondativo `PIANO-MAESTRO/` (10 dossier ecosistema via swarm 7
  agenti paralleli) + scaffolding iniziale `company/Memory/` (ADR-001 EMPIRE OS 10
  ecosistemi, ADR-002 memory-first, ADR-003 wrap-non-riscrittura). Workspace intero portato
  su GitHub monorepo privato con sync bidirezionale Max↔Gael (ADR-004, `scripts/empire-sync.ps1`).
  Skill `empire-context` creata e installata a livello progetto. → 1 pagina aggiornata
  (projects/Piano_Maestro_EMPIRE_OS.md). CP-20260610-001/002/003.

## 2026-06-11 (F1-F4 scaffolding + Backbone + metodo 9 passi, Gael/Max)
- BUILD: F1 scaffolding `company/` completo (92 check gate verde) — organigramma, Mandato,
  Board C-Suite v1, 10 ecosistemi, Backbone, Guilds/Sentinels. F2 Backbone operativo
  (ruflo/claude-flow installato, BUS/BRAIN/Identity-HR). F3 migrazione asset (51
  skill/workflow mappati, 8 wrapper L3). F4 AGENCY B1 infrastruttura + B2 wrap dei 4
  workflow outreach esistenti (ADR-003) + gate F4 verde su ciclo dry-run end-to-end.
- DECISIONE: **ADR-006** — Ciclo di Fase a 9 passi (RECALL→SPEC→PRE-MORTEM→BUILD→GATE→
  REVIEW→TEST→COMMIT→RETRO), metodo ufficiale per Max e Gael. **ADR-007** — Piano V2,
  direttiva di scala di Max (reparti=team CF-grade, organo MAXIMILIAN, ecosistema-Mandato).
  CP-20260611-001..008.

## 2026-06-13 (Errore Memory Empire riconosciuto e corretto, Max)
- FIX: durante lo studio Andrei Pascu (Empire Studio), il pipeline comunicato a Max ometteva
  gli stage Memory Empire — errore critico (invariante non negoziabile). Corretto: Memory
  Empire reso invariante #0 nel session-init protocol di Empire Studio, agenti
  compliance-auditor/error-triage/silent-observer aggiornati. Apre **ADR-008**. CP-20260613-001.

## 2026-06-16 (Genesi Core: organi ARCHITETTURA+FORGE+MAXIMILIAN, dossier v2, Gael/Max)
- BUILD: fix collisione git case-insensitive; F1-bis chiuso (0 cartelle vuote, gate verde).
  V2-2 avviata: dossier **MAXIMILIAN** (12) + **MANDATO-ecosistema** (13); primi due lotti
  dossier v2 scala (01-AGENCY, 04-MARKETING, 03-CONTENT-FACTORY, 02-INFO-BUSINESS).
- BUILD: **Genesi Core** costruito in 4 STEP dallo stesso giorno — organo **ARCHITETTURA**
  (30 file, progetta la forma di ogni artefatto), organo **FORGE** (34 file, costruisce il
  contenuto attorno al blueprint), organo **MAXIMILIAN** (15 file, review-gate 5-bis "Max
  approverebbe?"), blueprint Board C-Suite (70 agenti progettati su 7 figure). → 1 pagina
  nuova (tools/Tool_APEX7_Core_Motore_Condiviso.md riferisce a questo lavoro indirettamente;
  dettaglio Genesi Core in projects/Piano_Maestro_EMPIRE_OS.md, sezione Evoluzione V2).
  CP-20260616-001..010.

## 2026-06-17 (Board C-Suite V2: CEO/Chief-Forge/CTO/COO/CMO/CRO, Gael)
- BUILD: STEP 4-heavy — FORGE costruisce il contenuto delle figure Board dai blueprint.
  Batch 1 (CEO-Empire-Conductor, Chief-Forge), batch 2 (CTO, COO), batch 3 (CMO, CRO) — ogni
  figura 10 agenti + 3 workflow CF-grade, review 5-bis MAXIMILIAN APPROVA su tutte.
  CP-20260617-001..003.

## 2026-06-18 (CFO chiude Board C-Suite 7/7 + 04-MARKETING completo 6/6, Max/Gael)
- BUILD: CFO completato (Max) → **Board C-Suite V2 7/7 figure complete** (~70 agenti CF-grade).
  STEP 5: costruiti tutti i 6 reparti di 04-MARKETING (L2.6 Conversion Architecture, L2.5
  Brand & Creative, L2.2 Advertising, L2.3 Email & Lifecycle, L2.4 Analytics, L2.1
  Copywriting — wrap del Copy Workflow Orchestration Layer attivo, ADR-003) →
  **04-MARKETING primo ecosistema V2 intero** (114 file/44 agenti/22 workflow).
  CP-20260618-001..007.

## 2026-06-19 (03-CONTENT-FACTORY completo 9/9 reparti, Gael)
- BUILD: costruiti gli 8 reparti CF-R0..CF-R8 del mega-reparto 03-CONTENT-FACTORY (Director,
  Strategia&Brief, Brand-Kit Registry, Produzione Video, Produzione Testuale, Visual&Design/
  Caroselli, QA&Gate, Pubblicazione, Apprendimento — CF-R5/CF-R6 chiusi il 06-23, CF-R8 il
  06-30) → **9/9 reparti completi**, wrap di 3 motori attivi (hf-studio/heygen-studio,
  carousel-factory, orchestratori Python pubblicazione, tutti ADR-003). CP-20260619-008..016.

## 2026-06-22 (02-INFO-BUSINESS completo 5/5 + 01-AGENCY batch-1, Max)
- BUILD: STEP 5 — 02-INFO-BUSINESS chiuso 5/5 reparti (PROD/LANC/VEND/COMM/STRA, 94 file/42
  agenti/12 workflow). 01-AGENCY batch-1: A1-Ricerca, A2-Acquisizione (wrap del runtime
  outreach LIVE — Outreach Workflow/LinkedIn/Instagram, ADR-003 esemplare), A3-Preventivi →
  3/10 reparti. CP-20260622-001/002.

## 2026-06-23 (01-AGENCY batch-2, A4-A6, Max)
- BUILD: A4-Delivery, A5-Copywriting-Interno, A6-Marketing-Interno&Proof → **01-AGENCY 6/10**.
  CP-20260623-001.

## 2026-06-30 (primo video Andrei Pascu ingerito + PreventivoForge avviato, Max)
- INGEST: Empire Studio — primo video della run andrei-pascu-001 ingerito integralmente
  (9CuQI0Cr4Pg, FB Ads pannelli fonoassorbenti) → 2 pagine wiki (già presenti in index.md,
  sezione Copywriting).
- BUILD: primo cliente reale **PreventivoForge** avviato (Prof Autocad, poi rinominato
  Novacar srl) — Half A (Max: scraper/parser/pricer/dealers, prezzo 18.000→21.540€
  verificato) completata con agenti CF-grade + regole RBI + orchestration. → 1 pagina
  aggiornata (01 - Projects/Project_Prof_Autocad_PreventivoForge.md). CP-20260630-001/002/003.

## 2026-07-01 (PreventivoForge: Half B + scraping live risolto, Gael/Max)
- BUILD: Half B completata (Gael — traduzione/copy deterministica, render PDF, QA Gate
  A/B/C/D, 42 file agenti). Scraping LIVE mobile.de risolto: bypass Akamai Bot Manager via
  Chrome reale + CDP invece di Playwright puro, parser sui dati veri
  (`window.__INITIAL_STATE__`). Prova reale: Mercedes GLA 47.490€→51.915€, 4 gate verdi.
  REGOLE-SACRE (14 regole PDF) + template Novacar + dealer reale + ecosistema Memory propri.
  CP-20260701-001..004.

## 2026-07-02 (PreventivoForge: App Desktop + PDF via CDP + .exe, Gael)
- BUILD: App Desktop GUI (prima Tkinter), motore PDF migrato a CDP/Chrome (no Playwright,
  .exe-ready). PDF rifatto sul modello Novacar (Gate IMG + Gate R, 14 REGOLE), primo .exe
  costruito e validato con `--selftest`. CP-20260702-001..003.

## 2026-07-03 (PreventivoForge: GUI premium + kill-switch + consegna, Gael/Max)
- BUILD: GUI premium via pywebview (WebView2, priorità #1 di Max) con fallback Tkinter.
  Kill-switch abbonamento (`licenza.py`, controllo remoto via Gist) cablato in run.py+app.py.
  Storico automatico preventivi. **Consegna abbonabile pronta** — `CONSEGNA-NOVACAR.md`, .exe
  frozen ri-testata 6/6 gate + 14/14 REGOLE. CP-20260703-001/002.

## 2026-07-25 (Refinement agenti operativi APEX-7: misuratore + primi 2 promossi, Max)
- BUILD: `empire/forge.py` — misuratore di quanto un agente è OPERATIVO vs DOCUMENTALE (6
  criteri). Fotografia: 439 agenti, 55 operativo/324 parziale/60 documentale. Primi due
  agenti promossi a operativo: AGENTE-CLOSER-A8, AGENTE-CRO-COPY-ARCHITECT. Filtro corredi
  aggiunto (evals/failure-modes non contati come agenti). CP-20260725-001/002.

## 2026-07-27 (Sync/preventa-agents Phase A-B, APEX-7 Level 2, audit YT-Factory + F1-F3 reali, Claude/Gael/Max)
- FIX: conflitto sync GitHub risolto; `preventa-agents` ricostruito nel pattern
  cartella-per-agente (8 agenti, facade `agents.py` riparata, 13/13 test) dopo un wipe
  lasciato a metà; bug scraper multi-città (sovrascriveva invece di accumulare) fixato,
  19 lead ALTA reali generati, Gate-CONTATTI chiudibile onestamente.
- BUILD: APEX-7 portato a Level 2 operativo end-to-end su Stream S7 (Event Bus, memoria,
  6 gate a rubrica, meta-agent, orchestrator — test 8/8 sezioni verdi).
- AUDIT: YOUTUBE-AUTOMATION-FACTORY — scaffolding APEX-7 reale e testato ma **tutte e 6 le
  fasi hardcoded** (canale/video/script/critic sempre gli stessi, gate strutturalmente
  incapace di fallire). Corrette nella stessa giornata: F1 (scouting su dati reali, gate
  Cash Cow bloccante), F2 (fetch live YouTube reale con cache), F3 (script da materiale
  reale). Agente ANDREI-PASCU-MINER promosso a operativo. → 1 pagina aggiornata
  (concepts/Concept_YouTube_Automation_Factory.md). CP-20260727-001..015.

## 2026-07-28 (ADR-010 fusione APEX-7 + Preventa→Areus + Stream-S7 trading reale + YT-Factory F4-F7, Claude/Gael/Max)
- DECISIONE: **ADR-010** — fusione delle implementazioni APEX-7 divergenti su un motore
  condiviso multi-tenant (`11-APEX-7-CORE`), pilota su YouTube + Stream-S7-Bot.
- BUILD: Preventa — prezzo €2.000 una tantum chiuso, migrazione da Google Sheets ad Areus
  (CRM interno), modulo EmpireDesk `preventa.py`. Comando unico `/avvia-estate-wk`.
  Stream S7: loop trading collegato al bus reale (bug doppia esecuzione fix, RiskManager
  riscritto, feedback loop reale), poi parser Solana reale + position manager + fix spam
  segnali (Gael, verificato su transazioni mainnet vere).
- BUILD: YOUTUBE-AUTOMATION-FACTORY — F4 (spec Fliki multi-scena reale), F5 (metadati/tag
  reali), F6 (audit onesto, mai metriche finte), dashboard riflette l'esito vero, decisione
  motivata di **non migrare** Stream-S7-Bot al motore condiviso (implementazione più matura
  su alcuni assi). → 1 pagina nuova (tools/Tool_APEX7_Core_Motore_Condiviso.md).
  CP-20260728-001..013.

## 2026-07-29 (Centro di comando empire-wide + outreach WhatsApp reale + pivot @dosementale, Claude/Gael/Max)
- BUILD: `empire controllo` (porta d'uscita, modello Playwright non OAuth) e `empire
  cantiere` (porta di costruzione, guida i 3 modelli operativi). TASK-YT-002..007 chiuse
  (YouTube Factory: tutte le fasi P1 reali).
- BUILD: Outreach Preventa — invio WhatsApp reale automatizzato (profilo Chromium
  persistente, non storage_state: le chiavi di sessione WhatsApp Web vivono in IndexedDB),
  flusso giornaliero `/avvia-outreach-preventa` con Gancio 4 import-focus.
- CORREZIONE: il primo contenuto YouTube reale generato era ancora sul funnel morto
  "Manuale Claude Code" — pivot deciso da Gael a **@dosementale** come canale sorgente
  (replica per un canale da vendere già monetizzato, zero funnel). → 1 pagina aggiornata
  (entities/Entity_Dose_Mentale_Channel.md). CP-20260729-001..010.

## 2026-07-31 (Motore YouTube riscritto su @dosementale + Bibbia Messaggi Outreach, Gael/Claude/Max)
- BUILD: `apex7_orchestrator.py` (F1-F5) riscritto per intero su @dosementale — prima era
  solo il contenuto ad essere cambiato, il motore restava cablato sul Manuale Claude Code
  (rischio concreto di sovrascrittura). Config Fliki bloccata `NON MODIFICARE` su richiesta
  di Gael dopo un video approvato.
- BUILD: **Bibbia dei Messaggi Outreach** (Effetto Barnum, Rainbow, 5 Pilastri) + team di 4
  agenti + enforcement reale (`rule_keeper_lint.py`, lint deterministico agganciato prima di
  ogni invio WhatsApp). → 3 pagine wiki già presenti in index.md (sezione Framework).
  CP-20260731-001..005.

## 2026-08-04 (Audit YOUTUBE-AUTOMATION-FACTORY: 6 claim verificati riga per riga, Claude/Max)
- AUDIT: verificate riga per riga (non sui checkpoint) le 6 capacità che Max ricordava
  "implementate perfettamente" — 2 reali ma isolate (mai chiamate dall'orchestratore), 2
  rimosse per scelta (non mancanti), 2 parziali. Rilevata collisione live con una sessione
  Gael attiva sugli stessi file → **pausa su richiesta esplicita di Max** (crediti).
  Nessun file di produzione modificato. CP-20260804-001.

## 2026-08-07 (PIANO KDP: LM Arena abbandonato per il testo, Gael)
- DECISIONE: dopo 2 giorni di debug reale (captcha non aggirabile oltre il primo messaggio
  di una sessione, anche con profilo persistente), Gael decide di abbandonare LM Arena per
  la scrittura dei libri — resta solo per le copertine. Nuovo piano V2-Claude-Code (10
  checkpoint). CP-20260807-001.

## 2026-08-08 (Aureus pulsante YouTube + primo libro KDP completo, Gael/Claude)
- BUILD: Aureus/EmpireDesk — pulsante unico "Produci video + copertina" per YouTube Factory
  (`produci_video_completo.py`, incatena F1-F5 + Arena + Fliki).
- BUILD: **primo libro KDP completo, "The Quiet Hours"** — 115 pagine reali + copertina,
  pacchetto pronto (già in wiki, entities/Entity_The_Quiet_Hours_Libro_KDP.md). CP-20260808-001/002.

## 2026-08-12 (Wrapper pubblicazione Instagram caroselli Preventa, Claude/Max)
- BUILD: `publish_instagram.py` — wrappa il publisher IG reale esistente (ADR-003), dry-run
  verificato sulle 8 slide del carosello #1. Già documentato in
  projects/Preventa/Progetto_Preventa_Carousel.md (sezione "Aggiornamento 2026-08-12").
  CP-20260812-001.

## 2026-08-13 (Outreach self-healing + APEX-7 su 3 stream + orchestration layer 7 gate, Claude)
- FIX: retry self-healing su `page.goto` in `send_message.py` (3 tentativi, 45s) per errori
  di rete intermittenti nell'invio WhatsApp.
- BUILD: i 3 consumatori di produzione (skill-forge, carousel-machine, cold-outreach)
  passano ora dai 7 gate del motore condiviso; `main.py` di APEX-7-CORE riparato su Windows
  (non partiva). **ADR-011** — censimento ADR-010 incompleto, 6 implementazioni APEX-7 non 4.
  Layer di orchestrazione generalizzato innestato in `11-APEX-7-CORE/orchestration/` (audit
  di uno zip di Max trovato con gate che non bloccavano nulla di reale — es. rendimento 500%
  certificato). → 1 pagina nuova (tools/Tool_APEX7_Core_Motore_Condiviso.md). CP-20260813-001..003.

## 2026-08-14 (Workflow KDP 4 step riparato + APEX-7 Calc Layer, Claude)
- FIX: CLI Claude era uno stub mai installato; una volta riparato, il wrapper `.cmd` di npm
  troncava i prompt multi-riga e ignorava silenziosamente `--model haiku` (si pagava il
  modello di default). Flusso corretto per rispettare i 4 step dichiarati (nicchia scelta
  una volta sola, comando `riprendi` per non perdere capitoli già scritti/pagati).
- BUILD: APEX-7 Calc Layer — 16 moduli di calcolo puro (probabilità, royalty KDP, rendimenti)
  dietro un'interfaccia JSON pensata per parlare con altri orchestration layer; corretti 2
  errori finanziari reali trovati nello zip di Max. CP-20260814-001..003.

## 2026-08-15 (Legami d'Amore wiring reale + decisione finale modello scrittura libri, Claude/Gael)
- BUILD: YouTube Factory cablata su @Legamidiamore (voce femminile, upload, tag SEO a 4
  livelli, agente permanente `credential-keeper`).
- DECISIONE: dopo 3 tentativi di automazione falliti (Claude CLI/Haiku, LM Arena ×2), Gael
  decide che **il libro lo scrive Claude in sessione** — il Python smette di chiamare
  modelli e diventa attrezzatura di misura/impaginazione. 3 automazioni archiviate con `git
  mv` (ADR-003, niente cancellato). → 1 pagina aggiornata (tools/Tool_Pipeline_Libri_KDP.md).
  CP-20260815-001..003.

## 2026-08-16 (Primo test reale F1→F5 legamidiamore, Claude)
- BUILD: run reale end-to-end su @Legamidiamore, script scritto da Claude su materiale
  reale (3 iterazioni fino a 12,6 min/critic 8.08), bug tag SEO inquinati da etichette
  interne di pattern copy trovato e fixato. CP-20260816-001.

## 2026-08-17 (Secondo libro KDP "The Ninth Winter" + bug calibrazione pagine, Claude)
- BUILD: **"The Ninth Winter" completato** (24/24 capitoli, 34.897 parole) — prima verifica
  end-to-end del modello "lo scrivo io" su un caso reale imperfetto. Scoperto e corretto un
  bug di calibrazione: 300 parole/pagina dichiarate, 320 reali misurate su due libri veri —
  il PDF viene ora generato sempre, non solo su richiesta. → 1 pagina nuova
  (entities/Entity_The_Ninth_Winter_Libro_KDP.md). CP-20260817-001/002.

## 2026-08-18 (Primo video YouTube pubblicato + regola niente lineette lunghe, Max/Claude)
- MILESTONE: **primo video reale pubblicato dalla YouTube Automation Factory**, su
  @Legamidiamore (youtu.be/2t4BZR3KAiU) — upload finale completato a mano da Max dopo che
  l'automazione Playwright si è scontrata con "Verify it's you" di Google (blocco non
  aggirabile per design). Scelta deliberata di Max: Public, non Private. Già in wiki
  (entities/Entity_Legami_dAmore_Channel.md).
- BUILD: regola "niente lineette lunghe" nei libri (Gael) applicata a mano su 193 righe —
  The Ninth Winter e The Quiet Hours entrambi PUBBLICABILE con copertina/PDF/copy.
  CP-20260818-001/002.

## 2026-08-19 (3 video in produzione + piano "un libro in mezz'ora" CP1-6, Claude)
- BUILD: 3 nuovi video @Legamidiamore in produzione (bug `duration: 720` bloccava ogni
  generazione Fliki, fixato).
- BUILD: piano "un libro in mezz'ora" — bersaglio pagine spostato al centro della finestra,
  gate di blocco in 0,06s, riassunti a formato fisso, codice sceso da 41 a 27,6s (CP-1..6
  verificati con misure reali). Piano concorrente di Gael (`kdp_workflow/`) valutato: presi
  3 pezzi buoni (validatore troncamento, copy KDP arricchito, scheda ispirazione), rifiutata
  l'architettura (già archiviata il 08-15 dopo 3 fallimenti, 5 bug reali trovati nel piano).
  CP-20260819-001..003.

## 2026-08-20 (Terzo libro KDP "The Second-Hand Spellbook", prova cronometrata, Claude)
- BUILD: **CP-7 chiuso** — terzo libro completo in 48 minuti (non i 30 pianificati: il gate
  ha bocciato 3 volte lo stesso difetto, capitoli scritti corti in fretta). L'assunzione
  "320 parole/pagina" è stata falsificata dal libro stesso (stile diverso, scarto di 4,3
  pagine) — corretta la regola: generare il PDF reale prima della consegna finale, non
  fidarsi solo della stima. → 1 pagina nuova
  (entities/Entity_The_Second_Hand_Spellbook_Libro_KDP.md). CP-20260820-001.

## RIEPILOGO backfill 2026-08-24
30/30 date con checkpoint reale coperte (log.md). 6 pagine wiki nuove (tools/
Tool_APEX7_Core_Motore_Condiviso.md, concepts/Concept_Decisioni_Architetturali_ADR.md,
entities/Entity_The_Ninth_Winter_Libro_KDP.md, entities/Entity_The_Second_Hand_Spellbook_Libro_KDP.md)
+ 6 pagine aggiornate (projects/Piano_Maestro_EMPIRE_OS.md, tools/Tool_Pipeline_Libri_KDP.md,
concepts/Concept_YouTube_Automation_Factory.md, entities/Entity_Dose_Mentale_Channel.md,
entities/Entity_The_Quiet_Hours_Libro_KDP.md, 01 - Projects/Project_Prof_Autocad_PreventivoForge.md).
Dettaglio completo: `company/Memory/checkpoints/CP-20260824-*.md`.

## 2026-08-25 (Sync monorepo: build CCM + skill empire-premium-style su GitHub, Claude)
- INGEST: assorbito nel monorepo tutto il lavoro non tracciato del working tree — 103 file,
  ~2,8 MB di soli sorgenti (`.gitignore` ha tenuto fuori `node_modules/`, `.next/`, `dist/`,
  `*.zip`). Tre filoni: **skill `empire-premium-style`** (10 file: design system ccm-premium,
  token congelati, stack Next.js 16 + Tailwind v4 + Lenis + Framer Motion + GSAP),
  **build CCM** (`ccm-sale-page-empire` completo, `ccm-elite-ultimate`, `ccm-full-empire`
  parziale, + pipeline Jinja2 `builder.py` → `index.html` rigenerato),
  **`Landing Page/`** (`ccm-empire` home/masterclass/thank-you + export statico + varianti
  thank-you). → 1 pagina nuova (tools/Tool_Empire_Premium_Style.md) + index.md aggiornato.
- BUILD: `Landing Page/ccm-empire/` era un **repo Git annidato senza remote** (1 solo commit):
  committarlo avrebbe prodotto un gitlink vuoto, non clonabile da nessuno. Assorbito nel
  monorepo dopo backup in doppia copia della sua storia (bundle + copia `.git`).
- ⚠️ SICUREZZA: trovata **chiave API Brevo in chiaro su repo PUBBLICO** — non nuova, era in
  `HEAD` dal commit iniziale `57a0ba0b` in 3 file già tracciati. Va **ruotata su Brevo**, non
  solo rimossa dal codice (storia pubblica già indicizzabile). → backlog B-020.
  CP-20260825-001.

## 2026-08-25 (TASK-KDP-W1: il ciclo KDP si chiude end-to-end, quarto libro, Claude)
- BUILD: chiusi i **tre buchi** che impedivano al flusso KDP di consegnare i suoi tre output
  insieme. (1) Il copy Amazon non aveva **nessun comando**: `salva_copy()` c'era dal 15/08 ma
  nel flusso vivo non lo chiamava nessuno, e nei primi tre libri il copy è stato scritto **a
  mano dentro `progetto.json`** senza validazione (è così che sono passate le lineette lunghe
  nelle descrizioni di due libri già consegnati). Ora `kdp copy <slug> --file copy.json` valida
  prima di salvare e rifiuta senza scrivere. (2) La cartella finale nasceva **solo** col .png
  di copertina: ora nasce comunque, con bloccante esplicito "Copertina assente" in
  `validazione.json`. (3) `COPERTINA-PROMPT.md` ora entra sempre nel pacchetto. Nuovo
  `kdp pacchetto <slug>`: COMPLETO (exit 0) contro CARICABILE SU KDP. 135 test verdi (erano
  127, 8 nuovi). SKILL e SOP allineate nello stesso commit.
- INGEST: **quarto libro prodotto**, "The Winter Term" (dark academia mystery, Maren Ashcroft):
  24/24 capitoli, 39.668 parole, **116 pagine reali contate sul PDF**, 43,2 minuti dal primo
  comando all'ultimo. → pagina `tools/Tool_Pipeline_Libri_KDP.md` aggiornata.
- LEZIONE: il gate di blocco ha bocciato **2 volte su 7** e aveva ragione entrambe (capitoli a
  1.440 e 1.467 parole contro il bersaglio 1.600). La stima a 320 parole/pagina ha sbagliato di
  nuovo, 120,9 stimate contro 113 reali: solo il PDF conta. Scoperto anche che allungare un
  libro finito può rompere la continuità (conflitto Dunleavy cap 17/18, riparato).
  CP-20260825-002.

## 2026-08-27 (TASK-CAROSELLI-W1: un comando, un argomento, carosello nell'Arsenale, Claude)
- BUILD: nuovo comando unico `SKILL & Agenti/Workflow agency creative/caroselli.py`.
  Prima il flusso esisteva ma era in cinque pezzi da lanciare a mano (avvio browser,
  controllo stato, eventuale resume, download separato, scompattamento e `copy.json`
  scritti a mano). Ora: argomento → copy via API → **validazione del copy prima del
  render** (max 7 parole, accent presente nel testo, niente lineette lunghe: un copy
  sbagliato viene rigenerato, non renderizzato) → render locale → deposito ordinato →
  gate automatico che conta i PNG e ne controlla peso e dimensioni reali. 20 test verdi.
- INGEST: primo carosello del Ramo C in `Arsenale Caroselli/Preventa/2026-08-27_quanto-tempo-perdi-a-fare-un-preventivo/`
  (6 slide 1080x1080 + copy.json + caption). Nuovo brand `preventa` in carousel-factory,
  con i colori reali già documentati (#101E3E, #FF4D00, #F6F7F9), non inventati.
- BUILD: **cambio di motore dichiarato**. Il Ramo D (Arena browser), indicato dalla task,
  è verificato fermo: `playwright_stealth` non installato, `session_data/` assente (serve
  login Google interattivo), e comunque non compatibile con "nessun passaggio manuale".
  Usato il Ramo C (render locale), progettato a giugno e mai costruito fino a oggi.
  Reparto CF-R5 aggiornato: nuovo ordine `CF-2026-PREVENTA-002` + `ARCHITETTURA.md`.
- LEZIONE: il renderer produceva slide sbagliate **in silenzio da sempre**. Tre bug reali,
  zero errori nel log, visibili solo aprendo il PNG: `@font-face` su percorso disco
  (Chrome blocca le sottorisorse `file://` da una pagina creata con `page.setContent()`,
  quindi il font non si caricava mai), parola accent concatenata fuori dal ciclo delle
  parole (spazi mangiati, "funzionail render"), screenshot scattato prima dei webfont.
  Conferma diretta della regola in `ArenaAI/KNOWN-ISSUES.md`: un run senza eccezioni non è
  un run riuscito. Trovato anche che `npm install` può uscire con **exit 0** lasciando
  `node_modules/puppeteer` senza `package.json`.
- ⚠️ SICUREZZA (B-021): `caroselli - agency/config.py` è tracciato sul repo **pubblico** con
  `ARENA_EMAIL`, `ARENA_PASSWORD` e due API key in chiaro. Peggio di B-020: qui c'è la
  password di un account. Chiave OpenRouter **viva**. CP-20260825-003.

## 2026-08-31 (audit W1 Gael + task W2, Claude)
- AUDIT: W1 di Gael verificata rieseguendo il codice (135 test verdi, 4 libri 24/24 capitoli,
  `kdp pacchetto` exit 0/1 corretti). 6/6 task chiuse davvero.
- INGEST: 6 difetti misurati non coperti dalle sue task — 0 libri pubblicati su 4 scritti,
  B-018 aggravato (4 nicchie/3 autori, "Also by" vuota), 66 falsi positivi trattino, stima
  pagine sbagliata, magazzino a 1 argomento, reparto Lanci senza file eseguibili.
- TASK: emesse 4 task W2 per Gael (FIX -> PIANO -> 5LIBRI -> LANCI) in
  `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md`.
- SYNC: sesta collisione ID checkpoint (B-009) risolta rinumerando; hook pre-commit ADR-013
  attivati sulla macchina di Max (hanno bloccato un PDF da 44 MB al primo giro).

## 2026-08-31 (audit generale Impero + nascita EMPERATOR, Claude)
- AUDIT: stato dell'Impero misurato eseguendo i comandi, non leggendo i checkpoint
  ([[AUD-20260831-001]]). 436 agenti, **58 operativi (13,3%)**, C4-uscita mancante su 314;
  `.claude/agents/` vuoto contro 792 definizioni; `empire flow` con **0 step chiusi su 10
  workflow**; 9.913 orfani bloccanti; `doctor` 2 block; `controllo` 2/6 canali; solo 3
  ecosistemi su 14 con codice eseguibile. Runtime di governo sano: 236 test verdi.
- SINTESI: motori veri e governance vera, ma i due strati **non si toccano a runtime** —
  manca il punto in cui un ordine entra e attraversa l'azienda (F9 mai iniziata).
- TASK: emessa `TASK-MAX-20260831-IMPERO-OPERATIVO` — STRUMENTO ZERO + 9 blocchi B0..B8,
  ognuno con gate a comando. Direttiva di Max: **NIENTE SI SCARTA**, tutto va reso operativo.
- TOOL: nato **EMPERATOR** (`.claude/agents/emperator.md` + `scripts/emperator_hook.py`),
  primo agente realmente invocabile dell'Impero. Si attiva quando il suo nome compare in
  una frase. → [[Tool_Emperator]]
- FIX: due hook globali `UserPromptSubmit` erano scritti in sintassi bash (`pwd | grep`) e
  **fallivano a ogni messaggio su Windows** — erano loro le righe "hook error". Contenuto
  (WIKI-FIRST/Empire Studio/Memory Empire + NERVE-SOLVE) preservato parola per parola in
  `~/.claude/hooks/empire_context/*.txt` e riparato. Backup dei settings prima di toccarli.
- LEZIONE: un due-punti seguito da spazio in uno scalare YAML piatto rompe il frontmatter di
  un agente, e Claude Code lo scarta **in silenzio**. Nessun errore, l'agente semplicemente
  non esiste. Vale per ogni agente che verrà creato nel Blocco 2.

## 2026-08-31 (rifinitura EMPERATOR + task Neri SaaS, Emperator)
- BUILD: `.claude/agents/emperator.md` + `scripts/emperator_hook.py` rifiniti su direttiva Max —
  ego alzato, tono umano (ogni termine tecnico con glossa, ogni problema con la sua conseguenza),
  postura coach col team con l'errore di pigrizia come nemico n.1 (esposti: Neri > Gael > Max),
  perimetro privato PROGETTO EMPIRE, frase unica per gli estranei, auto-modifiche sempre dichiarate.
- MISURA: Gael 193 commit (ultimo 27/08), **Neri 0 commit in assoluto** con 4 task dal 30/07.
  Il suo lavoro non e' mai entrato nel repo: BLOCCO 0 = installazione, `SETUP-GAEL.md` non riusabile
  (l'installazione ci sta in una riga sola, inservibile per chi non e' tecnico).
- TASK: emessa `TASK-NERI-20260831-SAAS-YOUTUBE-AUTOMATION.md` — primo SaaS di Digital Empire,
  6 blocchi: installazione, sales page, lead magnet + landing, logo, asset social, caroselli.
  Skill `empire-premium-style`, riferimento aureo `Lancio corso skill beast/Leanding Page CCM/ccm-premium`.
  Scritta in lingua semplice con glossa a ogni termine e una sezione su come si scrive un ordine buono.
- APERTO per Max: nome piattaforma, prezzo abbonamento, scelta lead magnet (3 opzioni, consigliata
  la terza: mini-strumento), 3 dati per l'installazione di Neri, cartella e dominio dei siti.
- SETUP: consegnata `SETUP-NERI.md` (8 passi, Windows, linguaggio non tecnico, verifica
  esplicita dopo ogni passo). Dati da Max: Windows, account condiviso in attesa di posti
  individuali, nessun tentativo precedente. `SETUP-GAEL.md` resta valido per Gael, gia'
  operativo (193 commit). Segnalato a Max il rischio dell'account condiviso: limiti d'uso
  in comune (si tolgono la corrente a vicenda) e sospensione possibile per condivisione
  credenziali -> fermerebbe tutti insieme. Consigliati posti separati subito.
- FIX: `SETUP-NERI.md` era incompleto — non installava **Python**, ma
  `.claude/settings.json` ha 14 automatismi che lo richiedono (`py -3`), incluso il grilletto
  di Emperator e il controllo pre-commit della memoria. Senza, gli hook non partono **in
  silenzio**: sembra tutto a posto e non lo e'. Aggiunto passo 2b con l'avvertenza sulla
  casella "Add python.exe to PATH". Stessa lacuna presente in `SETUP-GAEL.md` (Gael e' gia'
  operativo, quindi Python ce l'ha: nessuna azione).
- VERIFICATO che l'Emperator migliorato arriva a Gael e Neri: `.claude/agents/emperator.md`,
  `scripts/emperator_hook.py` e `.claude/settings.json` (con la registrazione del grilletto)
  sono tutti e tre tracciati e pushati, piu' 314 file di skill. Le migliorie arrivano al loro
  **prossimo avvio di sessione**, non durante. Restano fuori dal repo, per scelta: il file
  privato del Progetto Empire e la memoria personale sulla macchina di Max.

## 2026-09-01
- INGEST (Empire Studio + Memory Empire): Andrei Pascu cat2-marketing **video 4/15** —
  `j4UInmM9kKA` "Usa questi 10 lead magnet per generare contatti (senza spendere 1 euro)",
  20m32s, 616 frame @2s, 17 KA, 5 pattern, NO-FINTO PASS.
  -> 1 pagina wiki creata (`sources/Source_Andrei_Pascu_10_Lead_Magnet.md`), index.md aggiornato.
- SCOPERTA: il `MASTER-RUN-TRACKER.md` dava il video come "Stage 1 da fare da zero". Falso —
  la pipeline Empire Studio era gia' stata eseguita il 2026-08-26 (`video-analysis.md` 20 KB).
  Il gap vero era a valle: **Memory Empire e wiki mai chiusi**. Stesso mezzo-lavoro del batch 2.
  Il tracker e' stato corretto con lo stato reale misurato su disco.
- ENRICHMENT: **9 patch applicate, 0 cancellazioni** (+26 / -0 su git diff).
  `lead-magnets/SKILL.md` (7): informazione gratis / implementazione a pagamento (Hormozi),
  nuovo principio "Free Quality Is Read as Paid Quality", 4 format nuovi in tabella
  (calcolatrice AI, challenge 7-14gg, GPT custom su WhatsApp, source files), anti-pattern
  ebook lungo, calibrazione proporzionalita' dei campi optin, optin trattata come sales page
  + vincolo strutturale a monte, distribuzione keyword-in-commenti -> DM.
  `market-funnel/SKILL.md` (2): criteri Opt-in balance e Opt-in copy nello scoring, nota di
  lettura sul ranking dei format.
- NON arricchite, dichiarato: `cro-copy-architect` (gia' copre le opt-in page con APSOC),
  `popups`, `signup`, `cro`, `free-tools`, `emails`, `ads`, `ad-creative`.
- WATCH-001: 33 video Andrei processati = 33 cartelle `memory-empire/knowledge/` -> MATCH.

- INGEST (Empire Studio + Memory Empire): Andrei Pascu cat2-marketing **video 5/15** —
  `-a0uuA1lbSI` "L'importanza di avere una buona landing", 51s, **26/26 frame letti — coverage 100%**,
  7 KA, 4 pattern, NO-FINTO PASS. Pipeline e Memory Empire chiusi nella stessa sessione, nessun gap.
  -> 1 pagina wiki creata (`sources/Source_Andrei_Pascu_Importanza_Landing.md`), index.md aggiornato.
- ENRICHMENT: **3 patch, +24 / -0.** `cro-strategy-social-(ig-tiktok)/SKILL.md`: nuova sezione
  "Il gradino zero: dove porta il link in bio" — il funnel documentato della skill andava
  Video -> commento keyword -> DM -> email -> call, **senza nessuna landing**, pur usando
  "link in bio" come CTA in piu' punti della stessa skill. `market-landing/SKILL.md`: nuovo tipo
  di pagina "Creator / Bio-Link Landing" (benchmark CR lasciati n/d — la fonte non ne da', non si
  inventano) + nota sul riequilibrio dei pesi del framework a 7 punti.
- SCOPERTA TRASVERSALE (registrata, non patchata): sta emergendo una catena nel run cat2 —
  contenuto (reach) -> landing bio-link -> optin -> sales page. Video 5 riempie i primi due
  gradini, video 4 (Regola 5) il terzo, video 2 aveva gia' stabilito che l'ordine e' un vincolo
  strutturale. Se cat2 la conferma ancora, vale un ADR + pagina wiki di framework.
- WATCH-001: 34 video Andrei = 34 cartelle `memory-empire/knowledge/` -> MATCH.

## 2026-09-02
- STUDIO COMPETITOR (nuovo reparto): avviato lo **studio forense dei siti di Andrei Pascu** su ordine di
  Max — grafica, colori con hex esatti, tipografia misurata, posizione elementi, teardown del copy
  sezione per sezione col perche'. Cartella `competitor/Andrei Pascu/site-study/`.
- CATTURATE 9 pagine su 9: andrei-copy.com (hub), /funnel-operator, /outheadline, /outfunnel, /copy,
  /manuale-del-copywriter, claude-speedrun.com, apsales.eu, linktr.ee/andrei.bsns.
  **371 screenshot** desktop+mobile, **1.832 blocchi di copy** estratti dal DOM con colore, font,
  dimensione, peso e posizione y di ognuno. Strumento nuovo e riusabile: `scripts/site_capture.py`.
- REPORT SCRITTI: **6 su 9** — 01 hub, 02 funnel-operator (434 EUR), 03 outheadline (98 EUR),
  04 outfunnel, 05 copy/Mentorship (349-999 EUR), 07 claude-speedrun (249 EUR).
  Mancano 06 manuale, 08 apsales, 09 linktree: materiale grezzo gia' pronto.
- 🔴 SCOPERTA: **claude-speedrun.com e' un concorrente diretto di Claude Code Mastery** e usa
  **`#fb4604` + font Onest**, cioe' esattamente il design system che `empire-premium-style/SKILL.md`
  dichiara per `ccm-premium`. Corso su Claude per marketer italiani, 249 EUR, v2, 21 lezioni +
  6 bonus, rilascio giornaliero, sezione "Skills", 4,9/5 su 14 recensioni verificate.
  **Chi sia arrivato prima non e' stato misurato**: servono le date (Wayback). Tre azioni per Max
  nel checkpoint CP-20260902-001.
- SCOPERTE DI SISTEMA: un prodotto = una pelle cromatica dentro griglia comune (blu istituzionale,
  rosso/verde, teal, giallo-ambra, arancione), col blu `#0062ff` come colore costante dell'azione;
  la lunghezza del copy e' funzione del prezzo; nessuna garanzia di rimborso su nessuna pagina;
  piu' la pagina e' lunga piu' grassetta (dal 13% all'80% del corpo); incoerenza numerica diffusa
  sulla prova sociale (sei cifre per tre metriche).



- INGEST (Empire Studio + Memory Empire): **batch max17, video 3/8** — `E8Ax92etrMc`

  "Steal My Claude Code Keyword Research System to Rank #1 on Google" (Nico | AI Ranking, 13m20s, EN),

  **400/400 frame letti — coverage 100%**, 58 KA (27 alta rilevanza DE), NO-FINTO PASS.

  Chiusura di un gap a valle: pipeline Stage 1-5 gia' fatta, layer Memory Empire e wiki mai chiusi

  — stesso pattern di `j4UInmM9kKA` il 2026-09-01. Nessuna nuova visione dei frame.

  -> `memory-empire/knowledge/E8Ax92etrMc/` (contenuto-integrale 41 KB mai riassunto + atoms + manifest + enrichment-report),

  **1 pagina wiki creata** (`sources/Source_Nico_AI_Ranking_Claude_Keyword_Research.md`), index.md aggiornato (nuova sezione "SEO & AI Search").

- CONTENUTO: keyword research che parte dalle 5 fonti dove le domande sono gia' scritte (Reddit, recensioni

  proprie **e di fino a 5 competitor**, People Also Ask, autocomplete, fan-out) invece che dai keyword tool.

  **15 domande canoniche su 37 a volume di ricerca zero**, tutte da linguaggio cliente reale. Routing a 4

  destinazioni (FAQ terminale / FAQ che linka fuori / pagina propria / video). Stack: Claude Opus 5 +

  DataForSEO + Zernio MCP per Reddit, $0,59 a run, cadenza consigliata 1 volta ogni 6 mesi.

- ENRICHMENT: **6 skill SEO valutate, 4 patchate, +70 / -0.**

  `ai-seo/SKILL.md` (+27): la sezione "Query Fan-Out" diceva solo "brainstorm the 5-10 related queries" —

  aggiunto il fan-out come **dato recuperabile** (AI Overview structure) con la soglia **1 blocco = FAQ /

  2+ sezioni = pagina propria**, il box "currently cited" come set competitivo reale, il volume zero

  non-scartabile con le convenzioni `0` vs `n/a`, e la tabella di routing a 4 destinazioni.

  `market-seo/SKILL.md` (+27): il Content Gap Analysis usava due sole fonti Google — aggiunte Reddit,

  recensioni proprie e dei competitor, autocomplete, deduplica in canonical questions, piu' la **gap

  analysis 1-2 stelle vs 5 stelle** (gap ampio = differenziatore, gap stretto = table stakes).

  `seo-audit/SKILL.md` (+12): "no major gaps in coverage" non e' falsificabile con un keyword tool.

  `programmatic-seo/SKILL.md` (+4): il volume e' il gate giusto per il *pattern*, sbagliato per le *pagine

  dentro* il pattern — col proprio freno anti-thin-content.

- NON arricchite, dichiarato: `site-seo` (opera su contenuto gia' deciso: meta tag, JSON-LD, sitemap — il

  video non tocca quel perimetro) e `schema` (il video non parla **mai** di structured data; l'unica

  connessione immaginabile e' gia' coperta dalla riga `FAQPage | FAQ content | mainEntity`).

- RISERVA SULLA FONTE: nessun risultato di ranking o traffico mostrato, fonte singola e autopromozionale,

  e il report scorso in video ("Roofing, Dallas") **non e' l'output del prompt digitato in demo**

  ("plumbing, Austin") — numeri diversi. Registrato in manifest, atoms (KA-056) e pagina wiki.

- DEBITO APERTO: RULES §6 non eseguita (nessun checkpoint in `company/Memory/`, `STATO-EMPIRE.md` non

  aggiornato) e **nessun commit git**, come da vincolo di sessione. Le altre 5 run del batch max17

  (v04-trivellato, v05-jaye, v06-belli, v07-rizzo, v08-herk) hanno lo stesso gap: verificato, layer

  Memory Empire assente per tutte.


- AGENTE CREATO: **CONOSCENZA-EMPIRE** (`.claude/agents/conoscenza-empire.md`, ID registro
  `KNOW-EMPIRE-001`), direttiva Max 2026-09-02. Gerarchia **LX -- accanto al Mandato e all'organo
  MAXIMILIAN, sopra il Board C-Suite**, supervisore EMPERATOR. Biblioteca vivente dell'Impero:
  possiede le 7 fonti di conoscenza (archivio video vivo, wiki, formazione su disco, framework
  proprietari, piani/ADR, competitor, skill/agenti) e le distribuisce a qualunque agente/skill/
  workflow sempre con la fonte esatta -- legge della fonte + 3 divieti (non inventa, non confonde
  fatto e inferenza, non appiana contraddizioni). Secondo mestiere: quando arriva conoscenza nuova,
  dice le 5 destinazioni (cosa migliorare / skill nuova / agente nuovo / workflow nuovo / esistente
  da potenziare, con nomi veri). Registrazione in `company/REGISTRO-IMPRESA.md` sezione ORGANI gia'
  fatta (riga KNOW-EMPIRE-001). **1 pagina wiki creata**: `tools/Tool_Conoscenza_Empire_Agente.md`
  (cross-link a Piano Maestro EMPIRE OS, indice ADR, memory-wiki-bridge, Memory Empire, NERVE-SOLVE),
  index.md aggiornato (sezione "AI Orchestration").

- INGEST (Empire Studio + Memory Empire): **batch max17, video 2/8** -- `yJOCyyP77bA`
  "Ho creato un intero team di marketing AI con Claude Code in 20 minuti" (Giovanni Beggiato / Gentes AI, 19m54s, IT),
  **165/165 frame unici letti -- coverage 100%**, 77 KA (21 alta rilevanza DE), NO-FINTO PASS.
  Chiusura di un gap a valle: pipeline Empire Studio gia' fatta in sessioni precedenti, layer Memory
  Empire e wiki mai chiusi -- stesso pattern di `E8Ax92etrMc` oggi. Nessuna nuova visione dei frame.
  -> `memory-empire/knowledge/yJOCyyP77bA/` (contenuto-integrale mai riassunto + atoms + manifest + enrichment-report),
  **1 pagina wiki creata** (`sources/Source_Giovanni_Beggiato_Team_Marketing_AI.md`), index.md aggiornato
  (nuova sezione "Marketing AI & Agency Teams").
- CONTENUTO: team di 6 agenti Claude Code specialisti (Stratega, Analista Concorrenza, Specialista SEO,
  Copywriter, Esperto Conversioni, Media Buyer) + 1 orchestratore. Da un solo URL e un solo prompt
  ("attiva il mio marketing team su questo URL") produce pagella, mappa opportunita', campagne ads,
  funnel, piano SEO, sequenza email, calendario social, piano 90 giorni + PDF cliente in 20 minuti.
  Regola di squadra: ogni voto cita il sito, mai numeri inventati, difetti provati nel browser vero.
  Verifica dal vivo dimostrata sul caso reale (Marco Calzature): browser renderizzato (Chrome via MCP)
  smentisce claim del fetch statico (hreflang, traduzioni JS, spedizioni), voto Conversione ricalcolato
  6.0->6.5 dentro lo stesso deliverable dopo la verifica.
- ENRICHMENT: **2 artefatti reali valutati (`market-audit`, `market-competitors`) + 1 dichiarato assente
  (`market-competitive` come file standalone -- non esiste, verificato con `find` su `.claude/skills/`
  e `.claude/agents/`). 2 file patchati, +22 / -0.**
  `market-audit/SKILL.md` (+18): nuovo paragrafo 1.1b "Live Verification Pass (Browser Reale)" subito
  dopo 1.1 "Fetch the Target URL" (che oggi usa solo `WebFetch`) -- cosa controllare nel browser reale
  (rendering vs statico, CTA cliccabili, checkout/contatto fino in fondo, elementi solo-JS), come
  registrare l'esito (liste "Verificato dal vivo" / "Smentito dal vivo"), dichiarazione esplicita che
  oggi `.mcp.json` di progetto non ha un MCP browser configurato (solo `claude-flow`, disconnesso).
  `market-audit/SKILL.md` (+2): dentro "Subagent 3: market-competitive", regola "mai concorrenti
  inventati -- fonte verificabile obbligatoria per ogni competitor citato".
  `market-competitors/SKILL.md` (+2): stessa regola, applicata a `COMPETITOR-REPORT.md`.
- NON costruito, dichiarato: skill nuova `live-verification` e agente nuovo `competitor-kyc` --
  proposte reali del video, non costruite di iniziativa. Registrate **B-034** e **B-035** in
  `company/Memory/BACKLOG.md`, da approvare da Max.
- DEBITO APERTO: nessun checkpoint in `company/Memory/`, `STATO-EMPIRE.md` non aggiornato (fuori dal
  perimetro esplicito di questo brief) e **nessun commit git**, come da vincolo di sessione.

- INGEST (Empire Studio + Memory Empire): **batch max17, video 4/8** -- `-gq8euRvNR4`
  "I grew my agency to $1.2M ARR using only LinkedIn.. (copy me)" (Paolo Trivellato, 18m49s, EN),
  **105/105 frame unici letti -- coverage 100%**, 60 KA (31 alta rilevanza DE), NO-FINTO PASS.
  Chiusura di un gap a valle: pipeline Empire Studio gia' fatta in sessione precedente, layer Memory
  Empire e wiki mai chiusi, consigli dell'analisi mai applicati -- stesso pattern di `yJOCyyP77bA` e
  `E8Ax92etrMc` oggi. Nessuna nuova visione dei frame.
  -> `memory-empire/knowledge/-gq8euRvNR4/` (contenuto-integrale mai riassunto + atoms + manifest),
  **1 pagina wiki creata** (`sources/Source_Paolo_Trivellato_LinkedIn_Agency_1M.md`), index.md aggiornato
  (nuova sezione "LinkedIn & Outreach Growth").
- CONTENUTO: sistema a 3 componenti (contenuto che attrae buyer non follower, profilo come sales page,
  due meccanismi di conversione) dietro $1.294.700/anno attribuiti interamente a LinkedIn, 31.000
  follower, $0 ads, zero cold outreach. Metrica centrale: buyer concentration (92% ICP match su 31K
  follower vs 2% su un'audience generica di 200K) al posto del follower count. Tabella Mistake/Fix
  completa per il profilo (headline/custom button/featured section), meccanismo Lead Magnet Post
  (300-1.000 connessioni ICP qualificate per post) e meccanismo Profile View Outreach (script esatto
  word-for-word, tasso di risposta riportato con discrepanza dichiarata: 40-50% a schermo vs 20-50%
  a voce, non risolta a favore dell'una o dell'altra).
- ENRICHMENT: **2 skill reali patchate (`avvia-linkedin`, `icp-radar`), 1 skill candidata letta per
  intero e scartata come non pertinente (`cold-email`). 2 file patchati, +29 / -0.**
  `avvia-linkedin/SKILL.md` (+13): nuova sezione "Fase 0 -- Il profilo come sales page" con la tabella
  Mistake/Fix completa, a monte delle 20 connessioni/20 messaggi/30 commenti giornalieri gia' eseguiti.
  `avvia-linkedin/SKILL.md` (+9): nuova sezione "Fase 0b -- Segnale profile-view", script esatto e
  tasso di risposta con entrambe le cifre dichiarate nel video.
  `avvia-linkedin/SKILL.md` (+5): nuova sezione "Gate di qualita' sui post -- The One-Sentence Post Test".
  `icp-radar/SKILL.md` (+2): principio "audience piccola e precisa batte una grande e generica",
  inserito nello Scopo dello skill che definisce i criteri di qualifica ICP per nicchia.
- NON costruito, dichiarato: skill nuova `linkedin-profile-audit`, agente nuovo `outreach-profile-signal`
  e workflow "Lead Magnet Post -> Connessione -> DM" -- proposte reali del video, non costruite di
  iniziativa. Registrate **B-036**, **B-037** e **B-038** in `company/Memory/BACKLOG.md`, da
  approvare da Max.
- DEBITO APERTO: nessun checkpoint in `company/Memory/`, `STATO-EMPIRE.md` non aggiornato (fuori dal
  perimetro esplicito di questo brief) e **nessun commit git**, come da vincolo di sessione.

- INGEST (Empire Studio + Memory Empire): **batch max17, video 8/8** -- `DTCyvo6cC54`
  "Every Level of a Claude Second Brain Explained" (Nate Herk | AI Automation, 30m59, EN),
  **130/130 frame unici letti -- coverage 100%**, 55 KA (20 alta rilevanza DE), NO-FINTO PASS.
  Chiusura di un gap a valle: pipeline Empire Studio gia' fatta in sessione precedente, layer Memory
  Empire e wiki mai chiusi, consigli dell'analisi mai applicati -- stesso pattern di `yJOCyyP77bA`,
  `E8Ax92etrMc` e `-gq8euRvNR4` gia' chiusi oggi. Nessuna nuova visione dei frame.
  -> `memory-empire/knowledge/DTCyvo6cC54/` (contenuto-integrale mai riassunto + atoms + manifest +
  enrichment-report), **1 pagina wiki creata**
  (`sources/Source_Nate_Herk_Claude_Second_Brain_Levels.md`), index.md aggiornato (nuova sezione
  "Second Brain & Knowledge Architecture").
- CONTENUTO: tassonomia a 5 livelli di retrieval per un second brain su Claude Code (L1 parola
  esatta/nome file, L2 wiki curata con router+auto-memory, L3 ricerca semantica/embeddings, L4
  knowledge graph tipizzato, L5 always-on/gbrain), ognuno risposta a una domanda diversa non a un
  budget diverso: "reverse engineer based on the question", "your whole project doesn't fit into
  one level". Ogni livello ha una cartella demo con CLAUDE.md integrale mostrato a schermo (letti
  parola per parola). Confronto verificato sulla wiki reale DE (1.831 pagine, non solo dichiarato):
  DE opera prevalentemente a Livello 1-2 (company/Memory + second-brain-vault/wiki), oltre la soglia
  in cui il video consiglia di valutare il salto al Livello 3 -- nessuna ricerca semantica
  configurata sulla wiki DE oggi.
- ENRICHMENT: **2 artefatti reali valutati e patchati (`sync-wiki-totale`, `conoscenza-empire`),
  perimetro limitato esplicitamente dal brief a questi due soli file. 2 file patchati, +28 righe
  nette / -0 cancellazioni di contenuto (1 rinumerazione di marcatore di lista, non una rimozione).**
  `.claude/skills/sync-wiki-totale/SKILL.md` (+12): nuovo step di valutazione del "livello di
  maturita' per area della wiki" sulla scala a 5 livelli del video, aggiunto al report MATCH/GAP
  standard prima dello step "Report finale all'utente" -- dice quando un'area ha superato la soglia
  in cui cercare per nome file non basta piu'.
  `.claude/agents/conoscenza-empire.md` (+16): nuovo box "Onesta' epistemica" nella sezione COSA
  POSSIEDI -- la ricerca su 1.800+ pagine della wiki DE e' oggi lessicale non semantica; prima di
  dichiarare un vuoto di conoscenza va provata piu' di una formulazione della domanda (esempio dal
  video: "posting frequency" -> 0 risultati lessicali su una nota che dice "content cadence").
- NON costruito, dichiarato: nessuna skill/agente nuovo proposto in questo ciclo (il brief chiedeva
  solo le due patch sopra). Registrate **B-040** (ricerca semantica sulla wiki, plugin Obsidian Smart
  Connections gratuito) e **B-041** (logica di pruning two-bucket della wiki) in
  `company/Memory/BACKLOG.md`, da approvare da Max.
- NOTA METODOLOGICA: il grafo LightRAG di produzione dell'autore (24:22-25:10) e' volutamente
  sfocato dall'autore stesso per privacy aziendale, dichiarato a voce prima del blur -- annotato
  esplicitamente in ingest-manifest.json come intervento editoriale intenzionale, non un limite di
  estrazione frame di Empire Studio.
- DEBITO APERTO: nessun checkpoint in `company/Memory/checkpoints/`, `STATO-EMPIRE.md` non
  aggiornato -- fuori dal perimetro esplicito di questo brief (che elencava Stage C/D-F/G/H/Backlog
  come le uniche consegne richieste), coerente col pattern gia' registrato su `E8Ax92etrMc` e
  `yJOCyyP77bA`. **Nessun commit git**, come da vincolo di sessione.

## 2026-09-03
- DOTTRINA: gerarchia forze Emperator (scagnozzo/sentinella/doom bot) + assetto God Emperor Doom -> 1 pagina concept creata, ADR-015, emperator.md §6-bis/§6-ter, hook DOTTRINA allineata

## 2026-09-03 — Delega piena di Max: costruito l'apparato che mancava

- **COSTRUITO**: organo ULTIMO METRO (ADR-016) — l'occhio che vede il lavoro finito e mai
  uscito. Prima misura: 25 pezzi fermi, 2.137 MB, il piu' vecchio da 135 giorni.
  → `scripts/ultimo_metro.py`, skill `ultimo-metro`, `company/Memory/ULTIMO-METRO.md`
- **COSTRUITO**: motore di ricerca della memoria con sinonimi del mestiere
  → `scripts/cerca_wiki.py` — 1.547 pagine indicizzate, chiude parzialmente B-040
- **COSTRUITO**: misura del costo delle skill → `scripts/peso_skill.py`
  (377 skill, 81% dei gettoni concentrati nelle 129 sopra soglia)
- **ARRICCHITI**: 10 guardiani (5 sentinelle + 5 guild) + 6 dirigenti del Board — da gusci
  vuoti a organi che possiedono i criteri e i numeri del proprio perimetro
- **DECISIONI**: ADR-016 (ultimo metro), ADR-017 (revisione con motore di famiglia diversa,
  in pilota), ADR-018 (conflitto ADR-012 dichiarato)
- **SCOPERTO**: due motori di orchestrazione entrambi canonici da 8 giorni; i criteri delle
  sentinelle esistevano gia' in `company/Sentinels/` ma nessun agente li citava; Digital
  Empire non misura un solo euro

## 2026-09-03 (secondo turno) — Nasce la Tesoreria, chiuso il conflitto sul motore

- **COSTRUITO**: reparto TESORERIA (ADR-020), quattordicesimo ecosistema. Digital Empire
  non misurava un solo euro: ne' incassi, ne' costi effettivi, ne' una metrica di vendita.
  Ora ha un motore che registra ogni movimento e da' il quadro in qualunque momento.
  -> `scripts/tesoreria.py`, skill `tesoreria`, 5 agenti, `company/Ecosistemi/14-TESORERIA/`
- **DECISO**: ADR-019, il motore di orchestrazione canonico e' `orchestration-layer`
  (133 file contro 28, 24 test contro 3). Scoperta che ha chiuso la questione: nessuno
  script dell'azienda chiamava nessuno dei due motori.
- **PRINCIPIO NUOVO**: un canone senza consumatori non e' un canone, e' un'opinione con un
  numero d'ordine. Prima di dichiarare qualcosa ufficiale, chiedersi chi lo chiamera'
  lunedi'.

## 2026-09-03 — Chiusura ciclo Will Barron (l'ultimo video rimasto a meta')

- INGEST: Will Barron — "If You Don't Understand Sales Systems, You Don't Understand Business"
  (5swDtQFyIws, 24m06, EN, batch max17 v10) → 1 pagina wiki creata
  `sources/Source_Will_Barron_Sistema_Vendita_5_Fasi.md`, `index.md` e `log.md` aggiornati.
  Il video era stato guardato per intero e analizzato il 2026-09-02 (218/218 frame unici,
  NO-FINTO PASS) ma il ciclo non era mai stato chiuso: mancavano l'archivio in Memory Empire e la
  pagina in biblioteca. Era l'unico degli 8 video del batch rimasto a meta'.
- ARCHIVIO INTEGRALE (nell'UNICA memory-empire viva, quella dentro `empire-studio/` — trappola
  B-033 rispettata, le due copie morte ferme al 2026-07-09 non sono state toccate):
  `empire-studio/memory-empire/knowledge/5swDtQFyIws/` con `contenuto-integrale.md` (40 KB, 10
  parti: walkthrough cronologico, le 5 fasi una per una, ogni schema riprodotto, i testi mostrati
  a schermo verbatim, tutti i numeri con fonte, i 7 errori, le regole operative, cosa il video NON
  mostra, confronto con DE, indice atomi), `atoms.json` (55 KA), `ingest-manifest.json`,
  `enrichment-report.md`.
- CONTENUTO: sistema di vendita a 5 fasi ICP → Meetings → Indoctrinate → Discovery Call →
  Business Case; i 6 passaggi della discovery call (Pain, Trigger, Future Reality, ROI, Budget,
  Next Step); "Questions first, Solutions later"; il business case che apre con le parole esatte
  del prospect (bias di coerenza cognitiva) e chiude con "Fast, Easy, Cost effective".
- PATCH APPLICATE (3 file, +64 righe, 0 cancellazioni di contenuto, frontmatter mai toccato,
  line endings preservati: LF dove era LF, CRLF dove era CRLF):
  `.claude/skills/cro-call/SKILL.md` (+24): nella Pagina 2 del documento strategico, la citazione
  diretta fra virgolette diventa obbligatoria in apertura, con il motivo (bias di coerenza
  cognitiva), il caso del socio/capo/coniuge che non era in call, e l'errore di tradurre le parole
  del prospect in linguaggio da agenzia.
  `.claude/skills/icp-radar/SKILL.md` (+29): nuovo campo `trigger_evento` nella scheda ICP (il
  profilo diceva CHI e' il cliente, non QUANDO diventa comprabile) + sezione "Test del
  riconoscimento in 1 secondo".
  `.claude/skills/discovery-call-brief/SKILL.md` (+11): campi `trigger_evento`,
  `prossimo_passo_data_ora`, `prossimo_passo_in_calendario` e due nuovi punti di gate — senza data
  e ora precise in calendario la discovery call non e' chiusa.
- NON PATCHATO, DICHIARATO: `proposal-gate` (il suo criterio 1 impone gia' il problema descritto
  con le parole del cliente: un criterio quasi-duplicato avrebbe allungato il gate senza
  stringerlo) e tutto il blocco copy/outreach (APSOC, Barnum/Rainbow, Bibbia dei Messaggi): su
  quel terreno l'Impero e' gia' piu' avanti della fonte, che dà principi senza testi.
- IL BUCO VERO TROVATO (verificato leggendo i file, non dedotto): fra "il prospect ha prenotato" e
  "il prospect e' in call" Digital Empire non fa nulla — la checklist pre-call di `cro-call` ha 10
  punti tutti lato nostro. E nessuno misura il tasso di conversione per fase del funnel di vendita.
- NON costruito, dichiarato: **B-042** skill `pre-call-indoctrination`, **B-043** agente
  `sales-funnel-auditor`, **B-044** workflow post-call → business case + next step in calendario,
  **B-045** decisione candidata ad ADR (pubblicare il prezzo prima della call, come fa Barron con
  gli $8.000 in FAQ, contro la Regola Assoluta #6 di `cro-call`). Da riportare in
  `company/Memory/BACKLOG.md` al primo passaggio su Memory: fuori dal perimetro di questo brief.
- DEBITO APERTO: nessun checkpoint in `company/Memory/checkpoints/`, `STATO-EMPIRE.md` non
  aggiornato — fuori dal perimetro esplicito del brief, coerente col pattern gia' registrato su
  `DTCyvo6cC54`, `E8Ax92etrMc` e `yJOCyyP77bA`. **Nessun commit git.**

- ADR-016: dottrina integrale all apertura (67k una volta) + sveglia leggera (2k a messaggio); Emperator al 100% per Max, Gael e Neri

## 2026-09-03
- INGEST: **Brand Guidelines CCM** costruite e archiviate → 1 pagina wiki creata
  (`concepts/Concept_CCM_Brand_Guidelines.md`), index aggiornato, `conoscenza-empire`
  alimentato con la fonte 8 (sistemi di marca) e con la regola di marca operativa.
- SCOPERTA che vale oltre CCM: `claude-speedrun.com` usa il **nostro identico `#fb4604`,
  il nostro identico Onest e i nostri identici raggi 12px/9999px** — misurato dal DOM.
  Non ha la famiglia argento. Da qui la regola: l'arancione è il colore dell'azione
  (≤10% dell'area), l'argento su inchiostro è la firma.
- CORREZIONE a una convinzione precedente: **non** è vero che i concorrenti sono senza
  texture. Speedrun usa un reticolo appena percettibile, il sito hub di Andrei Pascu una
  mezzatinta quasi invisibile. La differenza vera è di intenzione: loro la nascondono,
  noi la dichiariamo.
- METODO riusabile: PDF via HTML + Chromium `page.pdf()`, contenuto separato dal motore,
  verifica automatica del riempimento pagina (18/18 in norma). Grana come PNG ripetuto,
  mai filtro SVG (Chromium lo rasterizza: oltre 16 MB).

## 2026-09-03 (EMPIRE STUDIO — chiusura ciclo P-BQ-AGS0ck, batch max17 v14)
- INGEST (Empire Studio + Memory Empire): batch `max17`, video `P-BQ-AGS0ck` "Become a Master
  Storyteller (The Dopamine Trick Elite Speakers Use)" (Vishen Lakhiani, 25m55, EN), processato
  da zero — nessun lavoro precedente esisteva per questo run. `scene_detector.py` rilanciato con
  `--interval 4.0`: 338/389 frame unici (riduzione solo 13,1%, la più bassa del lotto max17 —
  video quasi interamente talking-head con gesti continui, non uno screen-recording con
  schermate ferme). Campionamento **sistematico dichiarato** (78 frame ogni 20s esatti + 5
  verifiche mirate), non un tentativo di 100%: **83/338 frame guardati (24,6%)**, copertura
  non-zero su tutti i 10 capitoli (17,6%-40,0% per capitolo). `transcript_clean.txt` scritto da
  zero (script Python di dedup del `.vtt`, 674 righe pulite) e letto per intero.
  `video-analysis.md`, `atoms.json` (35 KA, tutti `osservato`), `coverage.md` scritti da zero
  con numeri contati sul disco in questa sessione.
- CORREZIONE a `company/Memory/riprese/EMP-QQ2R.md`: il checkpoint dichiarava che "il video vero
  di Vishen (Mindvalley) non risulta scaricato da nessuna parte" e andava recuperato con un task
  di ricerca a parte. **Falso**: questo video *è* il video di Vishen — confermato sia a voce
  ("my name is Vishen Lakhiani, I'm the founder of Mindvalley") sia dai metadati YouTube
  (`P-BQ-AGS0ck.info.json`: `uploader`/`channel` = "Vishen", `uploader_id` = "@vishen").
  `max17-v09-vishen-story` (30MB, parziale) e questo run `max17-v14` (78MB, completo) sono lo
  stesso identico video, non due video diversi.
- CONTENUTO: framework di storytelling a 5 passi **HSTSS** — mnemonica ufficiale "Heroes Start
  Their Stories Somewhere", mnemonica "edgy" per gli studenti "Holy Sh*t That's So Smart" →
  Hook/Stake(s)/Turn/Scene/Shatter, rivelata a video una riga per capitolo tramite un effetto di
  reveal progressivo (pixelato → leggibile). Illustrato con la storia reale del fondatore
  (quasi-senzatetto a Berkeley dopo la bolla dot-com, poi scoperta dell'intuizione tramite un
  corso di meditazione oggi rivenduto da Mindvalley come "Silva Ultramind" per 40M$/anno).
  Tecnica di hook più riusabile: **"idea collision"** (scontrare due idee incompatibili nella
  stessa frase). Identità reali confermate a video correggono la trascrizione automatica: il
  figlio di Naveen Jain citato è **Ankur Jain, Founder/CEO of Bilt Rewards** (non "Uncle Jane"),
  l'autore di "Executive ESP" citato è **Prof. John Mihalasky** (non "Mihalaski").
- **0 patch applicate** a skill/agenti esistenti (perimetro del checkpoint `EMP-QQ2R`, nessuna
  modifica a sistemi condivisi mentre altre sentinelle lavoravano in parallelo su v16) — 5
  proposte in "Consigli" della pagina wiki, verificate con grep prima di essere scritte (skill
  `mnemonic-forge`, agente di story-mining per `case-study-forge`, workflow "fatto aziendale →
  storia HSTSS", potenziamento di `cro-copy-architect` con la tecnica idea collision).
- WIKI: 1 pagina creata (`sources/Source_Vishen_Lakhiani_Master_Storyteller_HSTSS.md`), cross-link
  a 3 pagine esistenti ([[Concept_Hook_Anti_Cliche_Checklist]], [[Framework_Barnum_Rainbow_5Pilastri]],
  [[Source_Artem_Novitckii_Caroselli_ChatGPT]]), `index.md` aggiornato con nuova sezione
  "Storytelling & Public Speaking".

## 2026-09-04 (EMPIRE STUDIO — chiusura ciclo rvpRQD43wdY, batch max17 v17, il video piu' lungo del lotto)

- INGEST: nuovo run `runs/max17-v17-beggiato-agenzia` creato da zero — nessun run precedente
  esisteva per questo video (4h17m00s, il piu' lungo del lotto max17). Trascrizione gia' pronta
  riutilizzata da `runs/max-17-2026-09/subs/` (44.552 righe grezze `.vtt`, deduplicate a 5.550
  righe uniche con script Python locale, lette per intero in 12 blocchi = 100% audio). Video
  scaricato a 360p (158 MB) con `frame_extractor.py --interval 8`: 1.928 frame densi ->
  `scene_detector.py --threshold 10` -> 158 frame unici (-91,8%).
- FORMATO VERIFICATO (misto, non presunto): ~2h53m talking-head+whiteboard Excalidraw (disegni
  fissi a schermo fino a 31,5 minuti consecutivi, come nei video precedenti del lotto) + ultimi
  ~80 minuti screen-share denso reale (documento Whimsical, GoHighLevel, Meta Ads Manager) — il
  62/158 (39%) dei frame unici cade nei soli 2.503s (16,5% della durata) del capitolo
  GoHighLevel, confermando la scelta di concentrare li' il campione visivo.
- **24/1.928 frame guardati nativamente (1,2%), campionamento mirato dichiarato e concentrato
  sulle sezioni a screen-share reale** — dettaglio completo con motivo di ciascuna scelta in
  `coverage.md`. 31 KA estratti in `atoms.json`, NO-FINTO PASS con copertura frame parziale
  dichiarata. `video-analysis.md` scritto capitolo per capitolo sui 14 capitoli ufficiali del
  video, tutti i contenuti a schermo citati sempre con `frame-NNNN.png` di riferimento.
- CONTENUTO: guida end-to-end per costruire un'agenzia AI — Blue/Red Ocean per la nicchia
  (verificato a schermo l'esempio Tesla), matrice di pricing **DIY/DWY/DFY x Tempo/Unita'/
  Risultato** (verificata a schermo), golden rule del **close rate al 30%**, **6 metodologie di
  acquisizione clienti ranked a schermo** (Warm Network con catena testimonial+2 referral,
  Upwork, Strategie Cold con funnel a cascata e tecnica "cold reading", Ads, Fiverr, Organico),
  flowchart Whimsical reale di fulfillment (kickoff call, under-promise-overdeliver, scope creep,
  policy "credenziali sempre del cliente, mai dell'agenzia"), demo GoHighLevel (custom values vs
  custom fields, workflow con tecnica "taking in charge"), regola di hiring "CTO prima del
  commerciale, per bisogno non per crescita" con grafico salario/fatturato verificato a schermo.
- CURIOSITA' documentata (non un errore): il primo frame del video (`frame-0001.png`) non mostra
  il relatore ma una clip di repertorio giornalistico (Presidente del Consiglio Giorgia Meloni a
  un podio istituzionale) usata come B-roll editoriale per il tema "cambiamento epocale" —
  verificato contro `frames/manifest.json`, non un bug di estrazione.
- **0 patch applicate** a skill/agenti esistenti (perimetro del checkpoint `EMP-QQ2R`, fase di
  studio) — 5 gap verificati con `Grep` prima di essere scritti in "Consigli": `agency-scalping`
  (SKILL.md operativa senza close rate/scope creep/niche hopping/DFY-DWY/warm network, presenti
  solo in PDF grezzi non distillati), `client-handover` e `delivery-playbook` (nessun match per
  scope creep/kickoff/under promise/SOP), nessuna skill DE menziona GoHighLevel (zero match),
  "cold reading" e "taking in charge" mai codificate in nessuna skill di outreach/copy, `pricing`
  senza la matrice DIY/DWY/DFY.
- WIKI: 1 pagina creata (`sources/Source_Giovanni_Beggiato_Guida_Agenzia_AI.md`), cross-link a
  3 pagine esistenti ([[sources/Source_Giovanni_Beggiato_Team_Marketing_AI]],
  [[sources/Source_Giovanni_Beggiato_CFO_AI_Claude]], [[tools/Tool_Tesoreria_Digital_Empire]]) +
  [[sources/Source_MiK_Cosentino_Micro_Personal_Brand]], `index.md` aggiornato con nuova sezione
  "Agency Operations & Scaling".
- MEMORY EMPIRE: `memory-empire/knowledge/rvpRQD43wdY/` chiuso (ingest-manifest.json, atoms.json,
  contenuto-integrale.md) — path live confermato in questa sessione, non le cartelle morte B-033.

## 2026-09-04 (EMPIRE STUDIO — Justin Sung, fonte TESTUALE, chiude l'ultimo buco di EMP-QQ2R)

- INGEST: `Agency 2026 (1).md` riga 366 — guida completa all'apprendimento di **Justin Sung**,
  4 capitoli (retrieval, encoding, mind mapping, skill acquisition). **NON è un video: è un
  documento di testo consegnato da Max.** Zero frame estratti, **zero frame guardati** — il video
  "Justin Sung 4h55" non è disponibile e il link non esiste nel repo, esattamente come dichiarato
  in `EMP-QQ2R` §3. Copertura reale: **285.119/285.119 caratteri = 100% del testo letto**
  (12 blocchi, nessuno saltato). Copia integrale **byte-identica** verificata con round-trip SHA-256.
- RUN: `empire-studio/runs/max18-doc-justin-sung/` — `contenuto-fonte.md` (copia integrale +
  mappa capitoli con offset misurati), `analisi.md` (9 sezioni), `atoms.json` (**88 KA**, campo
  `frame` sempre `null` perché non applicabile), `coverage.md` (dichiarazione NO-FINTO esplicita
  sulla natura testuale).
- CONTROLLO QUALITÀ INTERNO: lo script di build degli atomi calcola l'offset cercando nel testo
  reale un'**ancora** letterale, e scarta l'atomo se non la trova. **Ha intercettato 2 miei errori
  su 88** (citazioni fatte a memoria invece che dal testo), corretti prima della scrittura su disco.
  Esito: 88/88 atomi con offset verificato, zero citazioni non verificate.
- WIKI: 1 pagina creata (`sources/Source_Justin_Sung_Guida_Apprendimento.md`), cross-link a 4 pagine
  esistenti verificate ([[tools/Tool_Conoscenza_Empire_Agente]], [[tools/Tool_Memory_Wiki_Bridge]],
  [[sources/Source_Giovanni_Beggiato_Guida_Agenzia_AI]], [[sources/Source_Nate_Herk_Claude_Second_Brain_Levels]]).
  `index.md`: nuova sezione "Learning Science & Metodo di Studio".
- WIKI (correzione su pagina esistente): `sources/Source_Giovanni_Beggiato_Guida_Agenzia_AI.md`
  aggiornata — lo stesso file conteneva la trascrizione grezza Beggiato (riga 1) e **tre
  rielaborazioni AI** (righe 3-364) non viste prima. Materiale nuovo **verificato sulla trascrizione
  grezza** prima di essere accettato: dati Eurostat/mercato, **released capacity**, le 7 fasi, i 3
  pilastri, niche hopping col tetto dei ~€3.000/mese, meccanica esatta dello speed to lead.
  **Corrette le soglie del close rate**: sono tre (60% troppo basso / 30% golden rule / 20% troppo
  alto), la pagina le schiacciava in una sola. Segnalate come **NON dette dal relatore** quattro
  aggiunte delle rielaborazioni (Ikigai, "Ignorance Tax", la tabella a fasce della released capacity,
  la soglia di hiring a €10.000/mese) — zero occorrenze nella trascrizione.
- CONSIGLI (7, tutti verificati con `Grep` prima di essere scritti, **nessuna patch applicata**
  — perimetro `EMP-QQ2R` Fase 1 = studio): **zero learning science in tutto l'ecosistema di
  conoscenza di DE** (gli unici match su `**/SKILL.md` sono falsi positivi: costo dei modelli, UX
  writing, chunking di date); `book-to-skill` non ha nessuno step di **emphasis/backbone** ed eredita
  in blocco il raggruppamento dell'autore; **contraddizione interna** fra `book-to-skill` ("Generate
  chapter *summaries*") e `conoscenza-empire`/`content-forge` ("mai riassunti / never summarizes");
  **`atoms.json` non ha archi** (schema senza relazioni, `atomizer.py` senza `edge|relates_to|
  cluster`) mentre il catalogo agenti dichiara un knowledge-graph agent che li costruirebbe — DE
  produce mappe di **livello 1**, quelle che Sung dichiara inutili; Empire Studio non ha uno stage di
  **digestione/consolidamento**; **PACER** come triage di ingestione oggi assente; il **theory
  overload** spiega il dato già misurato da `peso_skill.py` e dà un criterio per la Fase 2 di
  `EMP-QQ2R` (applicare i consigli **1-2 alla volta**, non tutti insieme).
- MEMORY EMPIRE: `memory-empire/knowledge/justin-sung-learning-guide/` chiuso
  (`ingest-manifest.json`, `atoms.json`, `contenuto-integrale.md`) — path live dentro
  `empire-studio/`, non le cartelle morte B-033.
- NOTA FINE-RIGA: `log.md` e `index.md` verificati **LF puro** su disco prima di scrivere
  (0 CRLF, misurati byte per byte), non CRLF come indicherebbe la regola generica — preservato
  lo stato reale, coerente con quanto già trovato e documentato in CP-20260904-003.

## 2026-09-04 (EMPIRE STUDIO — chiusura ciclo LCNk5e5EiCA, batch max18 v02, sentinella max18-v02)

- INGEST (Empire Studio + Memory Empire): batch `max18`, video `LCNk5e5EiCA` "Claude Code +
  Karpathy = Agenti AI da 10.000€" (Giovanni Beggiato / Gentes AI, 25m03s, IT, 16 capitoli).
  Video **genuinamente nuovo**: nessun run preesistente per questo id, verificato prima di
  partire. Pipeline eseguita da zero in questa sessione: `yt_ingest.py` → `frame_extractor.py
  --interval 3 --height 360` → `scene_detector.py --threshold 6` → visione nativa →
  `video-analysis.md` + `atoms.json` (43 KA) + `coverage.md`.
- COPERTURA: **501 frame densi estratti, 69 unici, 80 frame guardati nativamente (16,0% del
  totale) di cui 69/69 unici = 100%.** Trascrizione **612/612 righe uniche lette (100%)**,
  deduplicate da 1.837 righe grezze del `.vtt` italiano, da 0:00:02 a 0:24:59 (gli ultimi ~4
  secondi non hanno sottotitoli in nessuna delle due tracce). Tutti i numeri ricontati in
  sessione contro `frames/manifest.json`, `scenes.json` e `atoms.json`, comandi riprodotti in
  fondo a `coverage.md`.
- DIFETTO DI STRUMENTO TROVATO E CORRETTO: `scene_detector.py` a soglia 6 dichiara il tratto
  19:24→24:45 come **una sola schermata di 321 secondi**. È falso — in quei 5 minuti l'autore
  costruisce a mano su lavagna Excalidraw tutto il ragionamento sul pricing. Il detector
  confronta miniature 64x64 in scala di grigi, e tratti di penna nera su fondo bianco non
  superano la soglia. Me ne sono accorto perché la trascrizione descriveva calcoli che nessun
  frame unico mostrava; ho campionato quel tratto a mano ogni 30s (`frame-400` → `frame-490`,
  10 frame) e ricostruito l'evoluzione. **Lo strumento è affidabile su screen-share e slide, non
  su lavagne disegnate dal vivo** — registrato in `coverage.md` per le prossime run.
- CONTENUTO: il **pattern LLM Wiki di Andrej Karpathy** (post originale su X letto integralmente
  a schermo) calato su un'azienda come **Company Brain** — tre strati (fonti grezze immutabili /
  wiki di note collegate mantenuto dall'AI / schema di regole) e tre operazioni (INGEST, QUERY
  con citazione obbligatoria delle note, LINT su contraddizioni-dati vecchi-note orfane).
  Dimostrazione A/B dal vivo con due Claude Code affiancati, stesso transcript di discovery call:
  **la differenza dimostrata non è estetica ma di verificabilità** — quello senza cervello chiude
  chiedendo all'umano di confermare cifre che ha inventato, quello col cervello dichiara cinque
  controlli superati contro `offerta/offerta.md` e registra una nota di memoria. Recuperati parola
  per parola: i due prompt integrali, le tre regole del `CLAUDE.md` (i prezzi vivono SOLO in
  offerta.md · nessuna proposta senza nota · mai mostrare .env), il transcript-fonte della call,
  il pattern di integrazione API (interroga il template prima di scrivere il codice + il ciclo
  `uploaded` → attesa → `draft`), e il value-based pricing con proxy `tempo persona × proposte al
  mese`, calcolo ROI e criterio del retainer.
- CAUTELA DICHIARATA: a voce l'autore liquida l'output senza cervello come "quasi AI slop" e dice
  "non ha nemmeno il nostro logo". Guardando davvero il frame, l'artifact è impaginato e porta
  "Gentes.AI" come testo; manca il logo immagine, il template brandizzato e il canale di firma.
  Il claim è retorica dell'autore, non un fatto verificato a schermo — riportato come tale in
  `video-analysis.md`, in `coverage.md` e nell'atomo inferito KA-042.
- **0 patch applicate** a skill/agenti esistenti (perimetro del checkpoint `EMP-QQ2R`, fase di
  studio, ordine esplicito di Max) — 7 consigli verificati con `Grep`/`find`/`ls` prima di essere
  scritti: (1) il listino DE compare in **68 file markdown** e **nessun `offerta.md` o
  `listino.md` canonico esiste nel repo**; (2) `/lint-wiki`, `/query-wiki`, `/synthesis`,
  `/research-topic` sono documentati in `second-brain-vault/CLAUDE.md` ma **nessuna delle quattro
  skill esiste** — puntatore che manda a sbattere, mentre il motore per costruirlo
  (`skill-contradiction-analyzer`) e il controllo orfani (`sync-wiki-totale:31-32`) ci sono già;
  (3) `proposal-gate` e `beast-preventivi` hanno **zero** match per memoria/registro/checkpoint,
  quindi DE ha "nessun task senza Memory" ma non "nessun preventivo senza nota"; (4)
  `beast-preventivi/references/stages/02-pricing.md:19-31` ha già il valore-vs-costo — il gap
  reale è più stretto: manca la proxy del tempo salvato per i deliverable di tipo agente e la
  variante a 2 opzioni non pre-evidenziate contro le 3 imposte in `SKILL.md:83`; (5)
  **contraddizione sul retainer** fra `agency-scalping:68` ("Retainer > one-shot"),
  `cro-call:1293/2234/3776` ("Non vendiamo retainer" / "Sprint, non retainer") e
  `proposal-gate:46` ("EUR 0 canoni mensili", BLOCCA) — il video dà un criterio invece di uno
  slogan; (6) il pattern async `uploaded → draft` non è codificato in nessuna SKILL.md operativa
  ma è già implementato in `fliki_client.py` (`poll_status()`), cioè DE l'ha imparato una volta e
  non l'ha scritto; (7) **zero PandaDoc in DE** (1 solo match, in un raw-source non distillato) e
  `preventivo-auto` si ferma al PDF senza firma, pagamento né nota di ritorno.
- CORREZIONE DI STATO: il brief di questa sentinella chiedeva di preservare il CRLF di
  `second-brain-vault/wiki/log.md`. Verificato con Python: il file ha **0 CRLF e 1.690 LF**, ed è
  già interamente LF (stesso esito per `index.md`: 0 CRLF, 1.743 LF). Scritto in LF, che è ciò
  che i file hanno davvero. Segnalato perché un'istruzione basata su uno stato superato può far
  introdurre proprio il file misto che il guardiano vuole evitare.
- WIKI: 1 pagina creata (`sources/Source_Giovanni_Beggiato_Company_Brain_Karpathy.md`), cross-link
  a 5 pagine esistenti ([[sources/Source_Nate_Herk_Claude_Second_Brain_Levels]],
  [[sources/Source_Justin_Sung_Guida_Apprendimento]],
  [[sources/Source_Giovanni_Beggiato_Guida_Agenzia_AI]],
  [[sources/Source_Giovanni_Beggiato_CFO_AI_Claude]], [[tools/Tool_Tesoreria_Digital_Empire]]),
  `index.md` aggiornato nella sezione "Second Brain & Knowledge Architecture".
- MEMORY EMPIRE: `empire-studio/memory-empire/knowledge/LCNk5e5EiCA/` chiuso
  (ingest-manifest.json, atoms.json, contenuto-integrale.md) — path live dentro `empire-studio/`,
  non le cartelle morte fuori (B-033).

## 2026-09-04
- INGEST: studio a fondo di **Higgsfield** ed **ElevenLabs** su ordine di Max ("abbiamo budget").
  Siti letti direttamente con Playwright sul DOM renderizzato (entrambe le pagine prezzi sono SPA:
  il fetch semplice le vede vuote e restituisce listini di terze parti, spesso sbagliati). Estratti
  i listini veri in EUR e USD, la tabella crediti per singolo modello, il funzionamento reale di
  "Unlimited", MCP/CLI, API Cloud, ElevenAgents. Incrociato con normativa italiana ed europea.
  -> 2 pagine create: `PIANO-MAESTRO/28-DOSSIER-HIGGSFIELD-ELEVENLABS.md` (dossier completo) e
  `wiki/tools/Tool_Higgsfield_ElevenLabs.md` (scheda), cross-link a 4 pagine esistenti.
- SCOPERTA CHE CAMBIA IL PIANO (1/3): Higgsfield **non sostituisce Fliki** — tetto di 15 secondi
  per clip, fa il girato non il film. E il blocco della fabbrica YouTube non viene da Fliki:
  21 fallimenti identici in `memory/` nascono da un gate nostro,
  `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/quality_gate.py:93` (sezioni HOOK, CORPO,
  CTA mancanti). Stavamo attribuendo a un fornitore un blocco costruito in casa.
- SCOPERTA CHE CAMBIA IL PIANO (2/3): l'**Unlimited di Higgsfield non e' automatizzabile**. I
  Termini vietano esplicitamente l'uso automatizzato, e l'unlimited non esiste su MCP, CLI, Canvas
  o Supercomputer. Si usa a mano, in sprint di 7 giorni a inizio mese; l'automazione legittima
  passa da MCP e API, a crediti.
- SCOPERTA CHE CAMBIA IL PIANO (3/3): le **chiamate a freddo automatiche in Italia oggi sono
  bloccate**. Legge 49/2026 (opt-in obbligatorio dal 19 giugno), RPO esteso alle utenze aziendali,
  AI Act articolo 50 operativo dal 2 agosto (obbligo di dichiarare l'AI dentro la conversazione,
  non nella privacy policy), sanzioni fino a 20 milioni o 4% del fatturato in solido tra mandante
  e contact center. Riprogettato il flusso vocale sul lead caldo che ha gia' risposto su WhatsApp
  in Preventa: consenso tracciabile, conversione piu' alta, circa 0,21 euro a chiamata.
- CONSIGLI (obbligatori dopo ogni studio): (a) riparare `quality_gate.py:93` PRIMA di comprare
  qualsiasi cosa, e' mezz'ora contro 21 fallimenti; (b) innestare Nano Banana Pro nella skill
  `carousel-empire` con le reference come parametro, non come upload manuale — e' li' che Arena
  fallisce sempre; (c) nuova skill `promo-video` da costruire sopra l'MCP Higgsfield; (d) tetto di
  spesa scritto nel codice (mai sopra 50 crediti senza via libera di Max), perche' l'MCP non ne ha
  uno nativo; (e) candidare Digital Empire allo Startup Grant ElevenLabs prima di pagare.

## 2026-09-04 (EMPIRE STUDIO — chiusura ciclo 1Dyld3y-V7Y, batch max18 v03, sentinella max18-v03)
- INGEST: "Dammi 36 Minuti e Ti Faro' Risparmiare MILIONI di Token su Claude" di Riccardo Belli
  Contarini (Martes AI), 36m01s, 20 capitoli ufficiali. Ripresa di una run gia' avviata: frame,
  scenes e transcript erano gia' su disco, la sentinella gemella e' morta per **limite di sessione
  dell'account** mentre iniziava a guardare i frame — non per un suo errore. Nessuna estrazione
  rifatta.
- COVERAGE: **138/138 frame unici guardati (100%)** su 721 frame densi @3s; **950/950 righe di
  `clean_transcript.txt` lette (100%)**, dalle 7.616 righe del `.vtt` grezzo. 12 frame ingranditi
  con crop+upscale LANCZOS (27 ritagli aperti) perche' contenevano numeri, tabelle o codice.
  Strategia opposta a quella di `max17-v16`: la' campionamento rado motivato (talk dal vivo, il
  contenuto sta nell'audio), qui copertura totale motivata (screen-recording denso, le cifre della
  lavagna **non vengono mai dette a voce**).
- VINCOLO DICHIARATO: il `video.mp4` gia' scaricato e' **640x360 av1** (verificato con `ffprobe`),
  quindi i PNG non possono contenere piu' informazione di cosi'. Provato crop+upscale 4x-8x: le
  lettere non ci sono nei pixel. Regola applicata: **una card e' citata testualmente solo se letta
  in una vista ravvicinata**; dalle viste d'insieme ho preso solo la struttura. **CAUSA TROVATA, e
  non e' YouTube: e' un default nostro.** `empire-studio/scripts/frame_extractor.py:133` ha
  `--height default=360` e la riga 51 lo passa a yt-dlp come `bv*[height<=360]` — e' l'Impero a
  chiedere il formato peggiore, per ogni video. Sensato per i talk dal vivo, sbagliato per gli
  screen-recording dove il contenuto **e'** il testo a schermo. Il flag `--height 720` esiste gia'
  e nessuno lo usa. Non applicato: e' una decisione di costo (piu' banda, frame piu' pesanti), non
  una svista da correggere di nascosto.
- TRE ERRORI DI LETTURA MIEI, trovati e messi a verbale invece che nascosti: "ADESSO, SUBITO" era
  **"GRATIS, SUBITO"**; "-19.000 a sessione" era **"-47.000"** (26.000 GitHub + 21.000 Slack);
  "IL MODELLO ADATTO" era **"IL MODELLO GIUSTO"**. In tutti e tre i casi **l'audio confermava
  plausibilmente la lettura sbagliata**: e' il modo tipico in cui una sagoma di parola a bassa
  risoluzione produce una citazione falsa che suona giusta.
- CONTROLLO SULLA CIFRA DEI TOKEN (appunto lasciato dalla gemella, verificato e non preso per
  buono): **confermato, e la prova sta nel video stesso**. La cifra "tra i 1.500 e 3.000 token per
  pagina PDF" e' detta a [00:17:41]; cinque secondi prima, in `frame-353.png`, si vede la fonte:
  una ricerca Google a cui risponde un **AI Overview**, con il chip di citazione **"GitHub"** sulla
  frase stessa e le voci di dettaglio citate a **Reddit r/ClaudeAI** e **Medium**. Catena reale:
  relatore -> AI Overview -> GitHub/Reddit/Medium, **nessuna documentazione primaria Anthropic**.
  Riportata ovunque come "detta dal relatore" (KA-037), mai come dato verificato. Nota di equita':
  l'autore **non nasconde** la fonte (12 secondi a schermo), semplicemente non dice a voce che sta
  citando un riassunto generato da un'AI — difetto di etichettatura, non di occultamento. Tenuta
  separata la cifra "3-4x sui PDF", che e' dichiarata come misurazione **propria** dell'autore.
- TROVATA PIU' INTERESSANTE: nel pannello `/usage` che il relatore mostra a 3:36 per dimostrare le
  sue tesi, Claude Code stesso consiglia "**Usa /compact a meta' attivita'**" — cioe' esattamente il
  comando che il video definisce "la cavolata piu' grossa". L'autore non lo nota e non lo confuta.
  Per DE il conflitto non e' "uno YouTuber contro l'Impero", e' **il relatore contro il vendor**.
- ATOMI: 47 in `atoms.json`, con **96 archi tipizzati** (`discende-da`, `quantifica`, `sostituisce`,
  `contraddice`, `corregge`, `motiva`, `specializza`, `istanza-di`, `generalizza`), validati a
  macchina: **0 archi rotti, 0 atomi orfani, 0 atomi senza ancora letterale**. E' il primo
  `atoms.json` di DE con relazioni fra atomi — difetto noto dell'Impero. Compatibilita' scelta a
  ragion veduta: **il file resta un array piatto** come `max17-v01-artem/atoms.json` e le relazioni
  stanno **dentro** ogni atomo, cosi' i lettori del vecchio schema continuano a funzionare.
  Errore mio corretto qui: 14 archi puntavano a ID inesistenti (avevo scritto relazioni verso atomi
  "DE" che non esistono, perche' le osservazioni sulla codebase **non sono atomi del video**) —
  rimossi o ripuntati, validazione rieseguita.
- WIKI: 1 pagina creata (`sources/Source_Riccardo_Belli_Risparmiare_Token_Claude_Code.md`),
  cross-link a 5 pagine esistenti ([[sources/Source_Riccardo_Belli_Claude_Codex_Setup]] — stesso
  autore, verdetto opposto; [[sources/Source_Giovanni_Beggiato_Company_Brain_Karpathy]] — seconda
  fonte DE sullo stesso pattern Karpathy, ma questo video **sbaglia i fatti sull'autore**;
  [[sources/Source_Jay_E_Agentic_OS_Claude5]] — da cui viene la soglia 150 righe di
  `peso_skill.py`; [[concepts/Emperator_Gerarchia_Forze]] — haiku/sonnet/opus;
  [[tools/Tool_Memory_Wiki_Bridge]]), `index.md` aggiornato nella sezione "Dev Tooling &
  Cross-Model Review". Fine-riga verificati prima di scrivere: `log.md` e `index.md` sono **LF
  puro** (0 CR), scritto in LF.
- CONSIGLI (grep-verificati, nessuna patch applicata — Fase 1 = solo studio):
  (a) **`/compact`**: DE ha una raccomandazione **opposta** scritta in
  `.claude/skills/agente-max/knowledge/K05-context.md:531` ("tenete Autocompact su on... potrete
  sempre usare /compact manualmente"), e in tutta `company/Memory` "compact" ha **0 occorrenze** —
  l'Impero non ha una posizione. Serve una decisione di Max, da scrivere come ADR, non una patch
  di iniziativa;
  (b) **gap piu' preciso trovato**: `scripts/peso_skill.py` pesa il **corpo** di ogni `SKILL.md`
  (costo di **attivazione**) ma la stringa `description` ha **0 occorrenze** nel file — cioe' non
  misura mai la voce che si paga **a ogni sessione per tutte le skill installate**, che e'
  esattamente quella di cui parla il video. Estensione suggerita: una seconda colonna che sommi i
  gettoni delle sole `description`;
  (c) **hook PDF->testo assente ma infrastruttura pronta**: `pdftotext` = 0 occorrenze in
  `scripts/`, `.claude/agents/`, `.claude/skills/empire-studio/`, `company/`; pero'
  `.claude/settings.json` dichiara gia' `PreToolUse`. Miglior rapporto valore/sforzo del video per
  un Impero che ingerisce PDF di continuo;
  (d) **caveman, distinguo onesto**: DE ha il plugin in `SKILL & Agenti/caveman-extracted/` e
  `emperator.md:1098` raccomanda `caveman:cavecrew-investigator`; il video **non boccia quello**,
  boccia il *Caveman Proxy* (compressore di contesto). Resta vero il punto (b): le ~7 skill
  `caveman:*` pagano la `description` a ogni sessione;
  (e) **conferme, che valgono quanto i gap**: `CLAUDE.md` root = **153 righe** (<200 gia'
  rispettato), **48 `CLAUDE.md`** nel repo (pattern per-cartella gia' adottato), root `.mcp.json`
  con **1 solo server** e `autoStart: false`, gerarchia haiku/sonnet/opus gia' allineata; la soglia
  "~500 file" sui grafi **non tocca DE**, che conta **166.534 file**, quindi `graphify` resta
  giustificato;
  (f) il consiglio piu' trasferibile non e' tecnico: "**ogni 'ricordati di' e' un candidato hook**",
  perche' una regola scritta a parole nel CLAUDE.md resta un prompt e il modello puo' non
  eseguirla. Domanda aperta per l'Impero: quali regole di prosa meritano di diventare
  deterministiche.
- TRAPPOLA EVITATA, documentata perche' si ripresentera': `frame-334` mostra un diagramma ASCII
  pieno di numeri appetitosi (`p = 0.004`, `-30%`, `-17,9%`, `-8,5%`) che sembrano misure di questo
  video. Non lo sono: appartengono a un **altro** lavoro dell'autore sui plugin, usato qui solo
  come esempio della tecnica ASCII-first. Quei numeri **non sono entrati in `atoms.json`**. Un
  ingest distratto li avrebbe attribuiti con tanto di timestamp, e sarebbero sembrati verificati.
- MEMORY EMPIRE: `empire-studio/memory-empire/knowledge/1Dyld3y-V7Y/` chiuso (ingest-manifest.json,
  atoms.json, contenuto-integrale.md) — path live dentro `empire-studio/`, non le cartelle morte
  fuori (B-033).
- REVISIONE 2 (stesso giorno, dopo richiamo di Max: "credi che tu non ti sia studiato abbastanza
  bene Higgsfield... guarda tutto"). Scansione completa: **60 pagine di higgsfield.ai** lette con
  Playwright sul DOM renderizzato. **Due conclusioni della revisione 1 erano sbagliate e sono state
  corrette nel dossier 28**, dichiarate come CORREZIONE e non riscritte di nascosto:
  (1) **Higgsfield SOSTITUISCE Fliki** — esiste `AI Long Video Generator`, che dichiara alla lettera
  il nostro caso d'uso ("Build YouTube and long-form content, faceless channels, full episodes").
  Script in ingresso, video multi-scena da minuti, audio nativo, character lock, scene extension,
  fino a 12 reference per scena, upscale 4K, export MP4. Conto verificato: un video da 10 minuti in
  modello misto (8 clip Kling 3.0 1080p + 60 immagini Soul 2.0) costa ~71 crediti = €2,78, quindi
  ~16 video al mese col piano Plus. Il mio errore era aver calcolato il video come se fosse tutto
  video, quando Max aveva detto immagini + qualche clip + voce + sottotitoli.
  (2) **I caroselli restano su Arena** — ho guardato le slide di Max in `Lancio corso skill beast/
  Page/caroselli - Agency`: sono un sistema di design coerente (tag pre-headline in pillola, grana,
  arancione <10% come accento, grotesque + corsivo serif, card argento, numerazione 2/8, firma),
  allineato alle Brand Guidelines CCM. Nano Banana Pro genera la fotografia di una slide, non un
  layout. Avevo confrontato sul prezzo quando l'asse vero era il tetto di qualita'.
- SCOPERTA PRINCIPALE: **il Text-to-Speech di Higgsfield usa ElevenLabs v3 come modello di default**
  (con MiniMax, Seed Speech, Vibe Voice). Comprando Higgsfield le voci ElevenLabs sono gia' dentro,
  pagate in crediti Higgsfield. ElevenLabs si restringe a 3 compiti: speech-to-speech sulla
  recitazione di Max, clonazione professionale certificata, agente telefonico.
- MAPPA MODULI (verificata, non dedotta): Long Video Generator, Popcorn (storyboard 8 scene),
  Supercomputer (AI Employees con skill, Orchestrator, ragionamento su Claude Opus/Sonnet 4.6,
  30+ connettori Slack/Drive/Notion, workflow ricorrenti), Canvas a nodi con template riusabili,
  Marketing Studio (6 formati, carica il prodotto dalla URL, 100+ avatar, layer modificabili),
  AI Ad Generator (URL -> annuncio in 2 minuti), Layers (immagine piatta -> livelli modificabili,
  testo compreso), Genjutsu, Mixed Media, Fashion Factory, Soul ID, MCP/CLI, API Cloud, plugin
  Photoshop/After Effects/Premiere/DaVinci/**Figma**/Blender, Games con deploy.
  Lacune reali: **nessun generatore di sottotitoli nativo** (/subtitles e' 404) e **costo crediti
  del TTS non pubblicato** — unico numero non verificabile da fuori, dichiarato come tale.
- CONSIGLI: (a) `quality_gate.py:93` resta da riparare comunque, la migrazione non lo risolve;
  (b) nuova skill `video-youtube-higgsfield` al posto del ramo Fliki; (c) **Layers e' la cosa da
  provare sui caroselli** — rigenerare solo il testo di una slide Arena gia' perfetta invece di
  ritirare i dadi sul layout; (d) riparare il ramo Arena resta prioritario, e' li' che si vince;
  (e) plugin Figma da valutare sul comparto visivo dei siti.
- WIKI: `wiki/tools/Tool_Higgsfield_ElevenLabs.md` aggiornata alla revisione 2. Report professionale
  pubblicato come artifact: https://claude.ai/code/artifact/24fb95f3-f393-4566-b014-2b8e307d2335
- REVISIONE 3 (stesso giorno, dopo secondo richiamo di Max: "sei sicuro che basti? fai il conto su
  5 video YouTube al giorno + 10 corti al giorno"). **Terza conclusione mia sbagliata e corretta**:
  avevo calcolato il costo di UN video (EUR 2,78) e mi ero fermato li'. Al volume vero di DE —
  450 video e 2.100 minuti finiti al mese — **nessun piano self-serve regge**: servono da 57.000
  (scenario magro) a 216.000 crediti/mese (ricco) contro un tetto acquistabile di 9.000.
  Costo reale: EUR 2.473 / 5.592 / 9.866 al mese. Scarto dal tetto nello scenario medio: **14x**.
- LISTINO COMPLETO estratto (prima avevo solo Plus e Ultra 3.000): Ultra 6.000 EUR 194/mese annuale,
  **Ultra 9.000 EUR 270/mese annuale** (= EUR 0,030/credito, il piu' economico del listino e il
  massimo acquistabile senza commerciale). **Team ed Enterprise sono i crediti PIU' CARI**: Team
  5.000 crediti a EUR 65 PER POSTO x 5 posti = EUR 325 (EUR 0,065/cr), Scale 12.500 a EUR 150 x 5 =
  EUR 750 (EUR 0,060/cr) — comprano posti, coda prioritaria, controllo spesa, SSO e manleva, non
  crediti convenienti. Team NON ha modelli unlimited, Scale si' (7 giorni).
- **VIBE MOTION trovato** — e' quello che Max ricordava come "motion design o graphics". Motore
  code-to-video: kinetic typography, infografiche animate, loghi, **Kinematic Captions**, HEX/RGB
  esatti (quindi il nostro #fb4604 alla lettera), safe zone social per i sottotitoli, curve di
  easing su cursori, upload di loghi/SVG/footage, render 4K. **L'uscita e' un asset strutturato e
  modificabile, non un video piatto** — quindi un template si riusa N volte cambiando solo il testo.
- **CANVAS studiato a fondo** (ordine esplicito di Max): ogni modello e' un nodo; costruire e
  collegare e' GRATIS, i crediti si scalano solo quando un nodo genera; run in parallelo e confronto
  affiancato (8 job su Ultra) = leva contro il tasso di riprova; template riutilizzabili.
  Dettaglio che fa sbagliare tutti: **i nodi Seedance leggono le reference collegate solo se il
  prompt ne dichiara il ruolo; i nodi Kling trattano l'immagine collegata come PRIMO FOTOGRAMMA e
  per il personaggio serve il tag @nome-elemento**.
- VOCE A VOLUME: 2.100 min/mese = ~2,1M caratteri. Creator copre il 6%. Serve ElevenLabs **Scale
  $299 + ~$51 di eccedenza**. Lo Startup Grant (33M caratteri) vale ~15 mesi del nostro consumo,
  cioe' EUR 4-5.000: e' la mezz'ora meglio spesa del dossier.
- CONSIGLI: (a) **aprire subito la trattativa Enterprise** — e' l'unico livello con sconti a volume
  per modello e **crediti che si riportano al mese dopo**, e richiede settimane; (b) partire da
  Ultra 3.000 (EUR 99) come **mese di taratura**, non dal tetto, per misurare le 3 incognite (costo
  crediti del TTS, costo di un progetto Vibe Motion, nostro tasso di riprova reale); (c) **il tasso
  di riprova vale meta' del conto** — da 2x a 1,3x lo scenario medio scende da EUR 5.592 a 3.778,
  quindi la libreria di prompt e reference e' il lavoro che rende di piu'; (d) **un secondo di clip
  Kling costa 66 volte un'immagine Soul 2.0** — il lungo faceless va costruito su immagini mosse in
  montaggio; (e) 5 template Canvas + 5 template Vibe Motion trasformano 450 produzioni in 10 stampi.
- OBIEZIONE SOLLEVATA A MAX (non un blocco, un fatto): DE ha 25 pezzi finiti mai pubblicati, il piu'
  vecchio da 135 giorni (dossier ULTIMO METRO). Dimensionare l'abbonamento sul volume che ENTRA
  invece che su quello che ESCE e' il modo piu' caro di non risolvere il collo di bottiglia.
- NUOVO STRUMENTO: `PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py` — calcolatore
  riproducibile, accetta --yt-giorno --corti-giorno --riprova. I numeri si rifanno, non si ricordano.
- REVISIONE 4 (stesso giorno, Max ha dato i volumi definitivi: "forse ho un po' esagerato").
  Volume vero: **70 video lunghi al mese** (cadenza 3-2-3-2 alternata, 2 giorni di stop) e
  **102 corti** (3 al giorno, 6 una volta a settimana), piu' **3.000 chiamate** (100/giorno).
  Totale 172 video e 904 minuti finiti al mese.
- **CORREZIONE 3 mia**: avevo costato i corti come 12 clip generative a testa. Sbagliato — Max li
  ha descritti senza avatar e senza soggetto, con sottotitoli al centro ed elementi che si
  spostano: **sono progetti Vibe Motion, non video generati**. Da 239 a 109 crediti l'uno, e li'
  se ne andava meta' del conto.
- CONTO FINALE: Higgsfield €635 / **€1.496** / €2.768 al mese nei tre scenari (magro/medio/ricco),
  ElevenLabs ~€617 tutto compreso. **Totale ~€2.113 al mese, ~€25.400 l'anno.** Con tasso di
  riprova 1,3x invece di 2x scende a €1.604 al mese: **seimila euro l'anno stanno nella qualita'
  dei nostri prompt**, non nel piano scelto.
- **SCOPERTA CHE VALE $510/MESE**: i piani ElevenAgents sono **perfettamente lineari a $0,08 al
  minuto**, quindi salire di livello NON fa risparmiare sulle chiamate — cambia solo i crediti
  voce e la concorrenza. Creator/Pro/Scale costano tutti $480 al nostro volume; Business $990.
  Si prende **Pro $99**, il piu' basso che copra i 204k crediti voce. Concorrenza: 100 chiamate
  al giorno sono meno di UNA in parallelo, i 20 canali di Pro sono venti volte il necessario.
- VIBE MOTION documentato a fondo (dossier A.4-BIS): HEX/RGB esatti (il nostro #fb4604 alla
  lettera), safe zone social per i sottotitoli, curve di easing su cursori, upload di loghi/SVG/
  footage, Motion Preset, render 4K, categorie Infografiche/Presentazioni/Kinematic Captions.
  CANVAS documentato a fondo (A.4-TER) su ordine esplicito di Max.
- CONSIGLI: (a) partire da **Ultra 3.000 + ElevenLabs Pro come MESE DI TARATURA**, non dal livello
  a regime; (b) 3 mosse a costo zero prima di pagare — Startup Grant ElevenLabs (33M caratteri =
  oltre dieci anni di voce dei corti), trattativa Enterprise Higgsfield (rollover crediti, conta
  con una cadenza non piatta), riparazione `quality_gate.py:93`; (c) **mai Team ne' Scale di
  Higgsfield**: sono i crediti piu' cari del listino perche' il prezzo e' per posto con minimo 5.
- VINCOLO SOLLEVATO: 3.000 chiamate/mese richiedono 3.000 contatti con **consenso tracciabile**.
  In Preventa il consenso nasce dalla risposta WhatsApp: la domanda non e' quanto costa l'agente,
  e' se generiamo cento risposte al giorno da richiamare.
- Report pubblicato (revisione 4): https://claude.ai/code/artifact/24fb95f3-f393-4566-b014-2b8e307d2335
  Calcolatore aggiornato: `PIANO-MAESTRO/scripts/costo_produzione_higgsfield.py`

## 2026-09-05
- REVISIONE 5 — **MESE DI PROVA definito** (decisione di Max: "faremo un acquisto di prova solamente
  per un mese, il minimo indispensabile per fare tutte le prove possibili, pero' considera che le
  prime prove saranno scarti"). **Higgsfield Ultra 3.000 MENSILE (EUR 129) + ElevenLabs Creator
  (primo mese $11) = ~EUR 139.**
  - **Regola non negoziabile: MENSILE, mai annuale.** L'annuale sconta il 30% ma blocca 12 mesi e
    annullerebbe il senso della prova. Si perde lo sconto: e' il prezzo dell'opzione di dire di no.
  - **Nove prove con budget crediti dichiarato e tasso di scarto 3x invece di 2x** (le prime volte
    si sbaglia prompt, reference o formato — messo nel conto, non sperato via): video YouTube 664,
    corti Vibe Motion 552, misura del TTS 150, Canvas 330, Layers su slide Arena 80, avatar UGC 372,
    promo prodotto 144, confronto modelli premium 248, MCP 100. Somma 2.640 + 25% margine = ~3.300.
  - Ultra ne da' 3.000, ma **i 7 giorni di Kling 3.0 unlimited coprono a mano ~900 crediti** delle
    prove 1, 2, 7 e parte della 4: **la finestra unlimited va usata per PRIMA, non per ultima.**
  - Perche' Ultra e non Plus: Plus (EUR 59 + EUR 66 di pacchetti = EUR 125) costa uguale ma con 6 job
    paralleli invece di 8 e **zero margine per gli scarti**. A parita' di spesa si prende quello che
    non finisce a meta' prova.
  - Regole di condotta: tetto di 50 crediti per generazione senza via libera di Max; registro delle
    prove (senza registro il mese produce impressioni, non numeri); data del rinnovo sul calendario
    il giorno stesso dell'acquisto; i crediti non si riportano, quindi le prove si fanno tutte.
- CHECKPOINT: `company/Memory/checkpoints/CP-20260905-001.md`. **Codice di ripresa: EMP-HGFD.**
- Report finale (revisione 5): https://claude.ai/code/artifact/24fb95f3-f393-4566-b014-2b8e307d2335
- CONSIGLI (chiusura dello studio): (a) le tre mosse a costo zero si possono fare **prima** di
  comprare — Startup Grant ElevenLabs (33M caratteri = oltre dieci anni di voce dei corti),
  riparazione `quality_gate.py:93`, apertura trattativa Enterprise; (b) la prova 3, la misura del
  costo in crediti del TTS, va fatta per prima perche' senza quel numero nessun conto e' chiuso;
  (c) skill nuove da costruire dopo la prova: `video-youtube-higgsfield` (al posto del ramo Fliki) e
  `corto-vibe-motion`; (d) la conoscenza di Canvas e Vibe Motion va dentro CONOSCENZA-EMPIRE, perche'
  serve a qualunque agente che tocchi produzione video.

## 2026-09-05 — STATO DELLA COSTRUZIONE DELL'IMPERO: 92% carta / 18% vivo (EMP-MCC4)

- ANALISI: misurata con tredici comandi del runtime di governo (`empire doctor`, `forge scan`,
  `flow status`, `trace stato`, `registry orphans`, `controllo`, `estate`, `pytest empire/tests`,
  `verify-agents.py`, `verify-skills.py`) la distanza fra l'Impero descritto e l'Impero che
  esegue. **92% sulla carta, 18% vivo** — il 18% su dieci gate a peso uguale, non stimato.
- SCOPERTA: dalla task madre del 31 agosto, **nove misure su undici sono ferme in cinque
  giorni**. L'unica mossa reale: agenti invocabili da 0 a 129 (l'ufficializzazione di skill e
  agenti). Il resto del tempo è andato in carta — è ADR-016 (ultimo metro) applicata alla
  costruzione, non solo ai contenuti.
- SCOPERTA TECNICA: la finestra di `empire flow` è **scaduta il 26 luglio**. È questa, non la
  mancanza di motore, la ragione per cui il contatore degli step è a zero da luglio.
- SCOPERTA TECNICA: `empire forge scan` conta 439 agenti, `empire registry census` ne conta 69.
  Uno dei due mente, e va deciso quale prima di scrivere 314 contratti d'uscita.
- CREATO: `PIANO-MAESTRO/30-PIANO-COMPLETAMENTO-IMPERO.md` — sette scaglioni S1..S7 con gate
  eseguibili, 127-189 ore, dipendenze, tre rischi e l'obiezione più forte con risposta.
  Correzione strutturale alla task di agosto: la fetta verticale (un workflow vero) viene prima
  del contratto d'uscita su 439 agenti.
- MEMORY: `CP-20260905-NUJJ` + ripresa `EMP-MCC4` + voce in `STATO-EMPIRE.md`.
- CONSIGLI (chiusura): (a) i quattro atti di Max valgono più di quaranta ore di macchina — 45
  minuti portano `empire controllo` da 2/6 a 5/6 e aprono l'incasso; (b) LANCI non parte prima
  che un workflow vero abbia chiuso un ciclo, o si aggiunge carta a un'azienda viva al 18%;
  (c) skill/agenti da potenziare dopo S3: tutti quelli che oggi non dichiarano cosa producono
  (314 su 439) — la conoscenza dello standard C4 va dentro CONOSCENZA-EMPIRE, perché serve a
  qualunque agente che debba essere concatenato.

## 2026-09-06

- INGEST: "CORSO COMPLETO SECOND BRAIN 2h: Claude + Obsidian" di Giovanni Beggiato (RnoC5IlOUhs,
  2h18m50s, lotto max18 video 1) — costruzione dal vivo di una Company Brain completa (11 cartelle,
  canon/override, gate_qualita.py a 6 regole, genera_llms.py/llms.txt, genera_showcase.py, soluzione
  `_index` agli orfani, skill journal sessioni/daily, cruscotto HTML + Notion via MCP, 14 prompt del
  canovaccio), 205 atomi / 333 archi / 1 componente connessa / 0 orfani → 1 pagina wiki creata
  (sources/Source_Giovanni_Beggiato_Second_Brain_Obsidian_Claude.md).
