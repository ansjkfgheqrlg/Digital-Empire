# EMP-V6DE — Studio corso AI TUBE PRO: 167 lezioni → fabbrica YouTube migliorata in tutto

- **Codice di ripresa:** `EMP-V6DE`
- **Aperto:** 2026-09-04
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-V6DE` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

Studiare **167 lezioni** (AI TUBE PRO 116 + Bonus Esclusivi 51, portale
`corsi.muccarossa.com`, autore Mirko Delfino) e usarle per **migliorare la
`YOUTUBE-AUTOMATION-FACTORY` in tutto cio' che serve**. Piano approvato da Max il
2026-09-04: [PIANO-STUDIO-AITUBEPRO](../plans/PIANO-STUDIO-AITUBEPRO.md).

## ▶️ RIPRESA — leggi prima [CP-20260911-FHFZ](../checkpoints/CP-20260911-FHFZ.md), poi torna qui

**Stato al 2026-09-11 sera:** missione al **21%**. A4 e A6 chiuse (33/167 lezioni). **11 script
nuovi** nella fabbrica, 4 bug di produzione corretti e provati, 3 agenti e 2 skill nuovi.

**LA PRIMA COSA DA FARE:** il primo caricamento vero dei 5 video pronti (`video-02,03,04,06,07`,
copertina di Max, fermi da 7-19 giorni). Il comando era rotto — rifaceva il video su Fliki invece
di caricarlo — ed e' **riparato e provato**. Si fa con `carica_pronti.py --conferma`, uno per
volta, **solo con il si' esplicito di Max** perche' tocca il canale. Dettaglio completo, tabella
dei video, trappole nuove e ordine dei passi successivi: nel checkpoint.

**Poi:** run reale di `youtube_studio_reader.py` (primi euro in Tesoreria), regole di binario B
rimaste, categoria `Intelligenza Artificiale` (12 lezioni, mai iniziata).

## ⚠️ MANDATO CORRETTO DA MAX — 2026-09-10. Vale sopra ogni riga precedente di questo file.

**Ordine testuale di Max:** *"non solo delle regole, ma proprio delle vere implementazioni...
sulla base dello studio e di tutto il corso deve migliorare il workflow tutto — non soltanto
mettere delle regole, anche fare agenti se servono, skill, flussi, miglioramento dei flussi,
miglioramento di funzionalita' o funzioni, script, Python, tutto: miglioramento generale di
tutto il workflow YOUTUBE AUTOMATION FACTORY."*

**Perche' l'ordine e' arrivato — il numero che lo ha fatto scattare:** al 2026-09-10 il registro
contava **69 regole, di cui 64 su file `.md` e 5 sul codice; zero agenti nuovi, zero skill nuove,
zero script nuovi, zero flussi ridisegnati.** Lo studio stava producendo documentazione, non
fabbrica.

**Causa strutturale, gia' rimossa:** `regole/schema.py` ammetteva solo
`TIPI = parametro|procedura|vincolo|euristica|strumento` e
`AZIONI = modifica|nuovo|conferma|scarta`. Non esisteva la casella per «qui manca un agente»,
«qui serve uno script», «questo flusso va rifatto»: chi studiava poteva solo chiedersi *quale
documento cambio*. Il contratto ora ammette anche `agente|skill|flusso|script|funzione` come
tipi e `costruisci|ridisegna` come azioni, e pretende che un tipo costruttivo dichiari quale
file NASCE. Le 69 regole vecchie restano valide (verificato: 69/69 a norma).

**La domanda che ogni lezione deve ricevere da adesso, tutte e sei:**
1. Cambia un parametro o una procedura? *(era l'unica che facevamo)*
2. **Ci manca un agente** che questa lezione dimostra necessario?
3. **Ci manca una skill** o un comando?
4. **Un flusso va ridisegnato**, non ritoccato?
5. **Serve codice** — script nuovo, funzione nuova, funzione esistente da rifare?
6. Contraddice qualcosa che facciamo? → `CONFLITTI.md`

**Debito aperto da questo cambio:** le **21 lezioni di A4 gia' chiuse** sono state lette con
il contratto vecchio, quindi le domande 2-5 non gliele ha mai poste nessuno. Vanno **ripassate
all'indietro** sui report e sugli appunti gia' su disco — **senza riguardare i video**, il
materiale c'e' tutto. E' il primo lavoro alla ripresa.

---


## 2-bis. AGGIORNAMENTO 2026-09-10 — ripasso costruttivo CHIUSO (CP-20260910-EVX2)

**Il debito del mandato vecchio e' saldato.** Le 23 lezioni gia' chiuse (21 A4 + 2 A6) sono state
ripassate all'indietro con le quattro domande nuove, sul materiale testuale gia' su disco —
nessun video riguardato, 3 sentinelle in parallelo.

- **19 regole costruttive** a registro in `regole/*/RIPASSO_COSTRUTTIVO.py` (file separati dalle
  regole per lezione, di proposito: non sono cio' che la lezione diede la prima volta, sono cio'
  che avrebbe dato se le avessimo fatto la domanda giusta — mescolarle cancellerebbe la prova).
- **Registro da 69 a 88 regole, 0 non a norma.** Binario A 5, binario B 14.
- **I 5 pezzi di binario A sono costruiti**: `regolatore-fatti.md`, `compliance-gate.md`,
  `regolatore-capacita-fliki.md`, skill `scan-strumenti-ai` e `fliki-capability-audit`. Agganciati
  in `ORGANIGRAMMA.md` e `script-writer.md`.
- **[ADR-029](../decisions/ADR-029-doppio-binario-studio-fabbrica.md)** scritto: la legge del
  doppio binario non aveva ADR, era attribuita ad ADR-024 (che e' Fabbrica Siti). 10 citazioni
  corrette in blocco.

**Le 12 lezioni BRONZO ri-giudicate hanno prodotto 5 script e 1 agente** — erano archiviate come
«non si trasferisce nulla». Una sola, L07, e' rimasta a vuoto, dichiarata onestamente.

**Trappola nuova, da non ripetere:** due sentinelle sono cadute di fila sullo stesso compito (le
due skill) perche' invitavano a navigare cataloghi esterni e si sono appese provando a ESEGUIRE
il lavoro invece di scriverne le istruzioni. **Un compito che tocca fonti esterne non si delega,
se il prodotto atteso e' un documento.**

**RIPRENDI DA QUI:** le 14 regole di binario B al gate A6 (le tre piu' gravi: `A6-RC-02` i 15
punti SEO falsi, `A4-RC-01`+`A4-RC-02` la verifica dei fatti, `A4-RC-11` il livello audio), poi
le 8 lezioni A6 rimaste — che partono gia' col contratto nuovo, senza debito.

## 2. DOVE SIAMO — cosa è FATTO davvero

**Passo zero: CHIUSO.** La catena regge su una lezione vera, quindi regge su 167.

- **Motore di ingestione costruito** (nuovo, non tocca `yt_ingest.py` — ADR-003):
  - `empire-studio/scripts/corso_ingest.py` — login SSO, mappa, scaricamento a 360p
  - `empire-studio/scripts/corso_trascrivi.py` — parlato via faster-whisper, ogni riga col minuto
  - `empire-studio/scripts/corso_prepara.py` — **prepara in blocco** una categoria intera
- **Mappa completa**: `empire-studio/runs/corso-aitubepro/mappa.json` — 167 lezioni,
  16 categorie, ogni lezione con identificativo e indirizzo esatto.
- **Baseline della fabbrica**: `company/Memory/studi/aitubepro/BASELINE.md` — i numeri
  PRIMA dello studio, per poter dimostrare il delta.
- **Contratto e registro delle regole**: `studi/aitubepro/regole/schema.py` + `registro.py`.
  Una regola senza prova (frame + minuto) **non entra**.
- **Lezione A4/L00 chiusa end-to-end** (commit `6f56588b`): appunti, report a sei voci,
  3 regole estratte **e già applicate** alla fabbrica, riverificate 3/3, test 11/11 verdi.
- **Lezione A4/L01 chiusa end-to-end** (CP-20260904-008): 4 regole, 3 applicate (binario A),
  1 in attesa del gate A4.
- **Lezioni A4/L02 e A4/L03 chiuse** (CP-20260905-009): 8 regole, 6 applicate.
- **Lezione A4/L04 chiusa** (CP-20260905-020): 5 regole, 4 applicate. È la lezione su **Fliki**,
  lo strumento che usiamo in produzione: ha scoperto che `video-producer.md` ordinava un
  montaggio a mano abbandonato da mesi («lo fa l'utente in Fliki»), che 4 dei suoi 6 ordini sono
  ineseguibili via API, e che `qa-audio-video` — **gate bloccante** — bocciava i video sul volume
  di una musica che nel payload non esiste.
- **Lezione A4/L05 chiusa** (CP-20260905-021): 4 regole, tutte applicate. È la **lezione madre**
  (il metodo intero in 5 minuti) e la prima che ci contraddice: aperto il primo `CONFLITTI.md`
  con tre arbitrati. Il migliore, **C-001**: la nostra soglia «scarta tutto sotto le 24 ore» era
  un vincolo **temporale** messo a difesa di un problema di **volume** — corretta in ≥10.000
  viste sotto le 24 h, e ci sblocca le nicchie di attualità.
- **Lezioni A4/L06, L07, L08, L10 chiuse** (CP-20260906-001): 10 regole, tutte applicate.
  Il trovato che conta non viene da una lezione ma dal **leggerne quattro di fila**: **i quattro
  miti del camuffamento** (fair use come regola di YouTube · i filtri che rendono «irriconoscibile»
  · le clip protette sotto i 5 secondi · il logo coperto), tutti in
  `references/monetizzazione-compliance.md` §5. Da L06 il regalo migliore: la velocity di un video
  giovane **misura la base iscritti**, non l'appeal.
  **Registro: 34 regole, tutte a norma, 31 applicate, 3 in attesa del gate A4 (binario B).**
- **Ingestione riparata**: portava a casa il video sbagliato (L02 arrivata due volte con un altro
  video). Ora la durata si chiede al lettore vero, i flussi si misurano con ffprobe PRIMA di
  scaricare, e un file fuori tolleranza diventa `1-sospetto` e non si trascrive.
- **Il nastro gira**: `corso_prepara.py` lanciato il 2026-09-04 alle 21:48 ha già scaricato e
  trascritto **6 lezioni** di A4. Non va rilanciato: guarda `runs/corso-aitubepro/*/stato.json`.

- **Lezioni A4/L09, L13, L14, L16 chiuse** (CP-20260906-49XK): il blocco del copia-incolla
  avanzato, 14.499 parole, BRONZO dichiarato. **9 regole, tutte applicate.** Da L14 il raccolto
  migliore: **~1 ora a video** contro i «~5 minuti» promessi da L05 (arbitrato `C-006`, fattore
  12×), i **miti del camuffamento da 4 a 6**, e i due principi di script che mancavano
  (l'apertura come **ritenzione**, la **CTA di chiusura**). Due porte chiuse nuove: l'aggiramento
  di licenza (L13) e la separazione audio di brani altrui (L16). Due buchi **nostri**: il criterio
  di scelta strumenti non chiedeva la licenza, `niche-scout` non chiedeva su cosa si reggesse un
  canale portato a esempio.
  **Registro: 47 regole, tutte a norma, 44 applicate, 3 in attesa del gate A4 (binario B).**
- **Le due regole di L19 rimaste in sospeso sono innestate**: `A4-L19-02` in `lessico-pronuncia.md`
  (la mappa Fliki vale «for this video») e `A4-L19-03` in `fliki-avanzato.md` (la fonte del 10%).

**Cosa è cambiato nella fabbrica finora:**
- nuovo `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` (criterio di scelta, prima assente)
- `03-AGENTI-E-RUOLI/supporto/self-improver.md` §8 — sorveglianza settimanale col tetto di tempo
- `03-AGENTI-E-RUOLI/operatori/niche-scout.md` §8 — cataloghi AI come fonte di nicchie
- `03-AGENTI-E-RUOLI/operatori/transcript-collector.md` §8-§9 — sufficienza del materiale
  (conta le parole, sotto soglia pretende ≥2 fonti esterne) e via di riserva coi due guasti distinti
- `03-AGENTI-E-RUOLI/capi/capo-strategia.md` §8 — leva multilingua col suo costo dichiarato

## 3. COSA È RIMASTO A METÀ

- **146 lezioni su 167 da studiare** (12,6% fatto). **La categoria A4 e' CHIUSA: 21 su 21.**
  Registro: **62 regole, tutte a norma, tutte applicate** (0 in attesa). Gate A4: **6 condizioni
  su 7** — manca solo il **video di prova** della condizione 4, che costa minuti di piano. Sette lezioni chiuse in
  **BRONZO dichiarato** (L07, L08, L10 + L09, L13, L14, L16: tutorial di editor manuali e manovre
  su materiale altrui, parlato letto integralmente, zero frame — piano §10).
- **In A4 non resta più nulla da leggere: le tre trascritte (L15, L17, L20) sono chiuse** il
  2026-09-06 da tre sentinelle in parallelo (CP-20260906-JYGA). Restano **solo 3 lezioni in
  stato `1-fallito`**: **L11** (Premiere SENSEI), **L12** (sottotitoli automatici), **L18**
  (voice over con Audacity), tutte HTTP 403 da gettone scaduto: si riscaricano con un gettone
  nuovo, non si forzano.
- **Lo stato delle lezioni chiuse oggi è stato allineato** in `runs/corso-aitubepro/*/stato.json`
  (`2-trascritto` → `completata` per L09, L13, L14, L16): il nastro non le ripropone più.
- **Musica (`A4-L04-04`): CHIUSA il 2026-09-06** — L20 mostra che in Fliki la musica non è
  automatica e nel payload non c'era un campo musica: criterio «Bilanciamento Volumi» passato da
  sospeso a **inapplicabile** (`A4-L20-01`). ⚠️ **Sfumatura aggiunta il 2026-09-07** (CP-PG43): la
  vera API Fliki HA un campo `bgMusicVolume` mai usato dal nostro client — "non possiamo" era
  "non abbiamo ancora deciso". Candidato binario B in coda al gate A6, non applicato.
- **Restano da fare:** cronometrare una produzione vera end-to-end (`A4-L05-04`) — il corso ha un
  metro di 5 minuti, noi nessuno; ⭐ **compilare il campo `YouTube channel ID(s)` nel profilo
  Fliki** per `dosementale` e `legamidiamore` (`A4-L19-01`) — è gratuito, protegge dai reclami
  sulle clip che Fliki ci fornisce, e **non è mai stato fatto** (richiede l'interfaccia Fliki, non
  l'API).
- **Tre verifiche payload da L20: CHIUSE il 2026-09-07** (CP-PG43, vedi
  `studi/aitubepro/A4-metodo-ai-tube/VERIFICA-PAYLOAD-L20-GATE-A4.md`): SFX via API **sì**
  (`generateSfx`) · timing per-media **no** · tetto 50 scene **non verificabile dallo schema**
  (resta l'unica delle tre non chiusa del tutto — serve una chiamata reale).
- **La fabbrica oggi non può produrre Shorts**: `aspectRatio` è la costante `"16:9"` a
  `fliki_client.py:258` (regola `A4-L04-02`, binario B).
- `corso_prepara.py` **eseguito il 2026-09-04**: 6 lezioni di A4 già pronte a nastro.
- **DURATE.md non esiste**: il censimento delle durate previsto dal piano non è stato fatto
  (la durata si legge lezione per lezione durante lo scaricamento, e finisce in `stato.json`).
- **`CONFLITTI.md`**: sei arbitrati (C-001..C-006). L'ultimo, **C-006**, è il secondo caso in cui
  il corso contraddice sé stesso — e riguarda il costo del suo stesso metodo.

## 3-bis. ✅ IL LAVORO CHE ERA A METÀ — CHIUSO IL 2026-09-06

**L09, L13, L14, L16 erano lette ma non chiuse. Ora sono chiuse** (CP-20260906-49XK): appunti per
lezione, [`REPORT-BLOCCO-COPIA-INCOLLA.md`](../studi/aitubepro/A4-metodo-ai-tube/REPORT-BLOCCO-COPIA-INCOLLA.md),
9 regole a registro tutte applicate, arbitrato `C-006`.
I rapporti grezzi degli scagnozzi restano come **materiale d'origine** in
[`RAPPORTI-GREZZI-L09-L13-L14-L16.md`](../studi/aitubepro/A4-metodo-ai-tube/RAPPORTI-GREZZI-L09-L13-L14-L16.md).

**Nessun lavoro a metà aperto in questo momento.**

## 4. IL PROSSIMO PASSO ESATTO

**A4 CHIUSA** (CP-20260907-JVY2): 21/21, 62 regole, gate 6/7 (manca solo il video di prova, costa
minuti di piano, decide Max). Le tre verifiche payload di L20 sono state chiuse il giorno dopo
(CP-PG43), fuori dal conteggio delle 7 condizioni.

**In corso ORA: categoria A6 «Viral Mastery» (10 lezioni)**, dove si chiudono anche **D-1** e
**D-2**. `corso_prepara.py` per questa categoria è stato lanciato in background il 2026-09-07 e
scarica+trascrive tutte e 10 le lezioni (nessuna letta prima d'ora, tutte partivano da `da-fare`).

```bash
cd "SKILL & Agenti/Empire Studio Suite/empire-studio/scripts"
# stato vero di ogni lezione (unica fonte, non l'aritmetica):
#   runs/corso-aitubepro/<lesson_id>/stato.json   -> passo: completata | 2-trascritto | 1-fallito
PYTHONIOENCODING=utf-8 py -3 corso_prepara.py --categoria "Viral Mastery"   # idempotente, in corso

# poi, per lezione, i frame (l'URL sta in runs/corso-aitubepro/mappa.json):
python scripts/frame_extractor.py --run corso-aitubepro/<lesson_id> --input <url> --interval 2
```

Poi lettura via sentinelle (max 2-3 in parallelo — regola di risparmio token, non aggirarla),
regole a registro, **gate A6 a 7 condizioni** (stesso schema di A4, piano §9) che stavolta include
anche la chiusura di D-1 (`DURATA_MASSIMA_S` vs `PAROLE_MINIME_SCRIPT` impossibile) e D-2
(`verifica_qualita()` mai invocata dalla catena).

A fine categoria: `REPORT-CATEGORIA.md`, `APPUNTI-CATEGORIA.md` per A6, poi la categoria successiva
del piano.

## 4-bis. IL PEZZO FINALE — come si chiude la missione (ordine di Max, 2026-09-05)

Lo studio **non si chiude con le 167 lezioni**: si chiude con un'opera pubblica,
`IL METODO YOUTUBE AUTOMATION`, in **tre formati** (`.md` fonte di verità · `.py` metodo
interrogabile dagli agenti · `.pdf` impaginato, stile minimal AP Sales via HTML+Chromium).

Struttura fissa: **1) parte finanziaria e modello di business · 2) sintesi stretta di tutte le
fasi · 3) parte estesa integrale** — regole primarie, tutte le fasi, tutti i metodi e poi il
metodo migliore dichiarato e motivato, tutta la SEO, tutta la ricerca, tutte le analisi,
l'intera formazione. Ogni affermazione tracciabile a lezione + minuto. Si assembla **a nastro**
da ogni categoria chiusa, mai scritto a memoria alla fine.

Piano: §16. Decisione: [ADR-022](../decisions/ADR-022-opera-finale-metodo-youtube-automation.md).
**Finché mancano i tre formati, la missione è APERTA.**

## 5. DECISIONI GIÀ PRESE — non ridiscuterle

- **Doppio binario.** Binario A (agenti, regolatori, reference, regole) si applica **dopo ogni
  lezione**; binario B (il motore in `02-AUTOMAZIONI-E-SCRIPTS/`) **solo a gate di categoria**,
  con test verdi e un video di prova. La fabbrica sta producendo video veri: ADR-003.
- **Modello di trascrizione `base`**, non `small`: i modelli più grandi non si scaricano su
  questa macchina (vedi trappole). `base` dà 137 parole/minuto, sopra la soglia di 60.
- **Qualità video 360p.** Verificato: il testo a schermo si legge perfettamente. Su 167
  lezioni è la differenza fra ~5 GB e ~40 GB.
- **Le 16 lezioni «Smart Tube» (da smartphone) restano in profondità BRONZO**: sulla nostra
  fabbrica Python non si trasferisce quasi nulla, ed è dichiarato nel piano.
- **Google Automation Platinum (181 lezioni) resta FUORI perimetro** — ordine di Max.

## 6. TRAPPOLE — errori già fatti, non rifarli

- **Il portale serve anche video che NON sono la lezione** (promo, webinar di vendita). Il
  2026-09-04 la lezione `81e4e28a` e' arrivata a casa due volte col video sbagliato. La difesa
  e' gia' nel codice — durata dal lettore, flussi misurati con ffprobe prima di scaricare, stato
  `1-sospetto` — ma se una lezione risulta sospetta **non forzarla**: si riscarica.
- **Non fidarsi dell'elenco di `scene_detector.py` su una lezione operativa.** Il 2026-09-04 ha
  dichiarato «schermo fermo per 96 secondi» mentre passavano cinque schermate diverse, fra cui il
  secondo strumento della lezione: la miniatura in scala di grigi confonde le pagine a fondo
  bianco (delta 2.0 fra due siti completamente diversi). È stato aggiunto il presidio `--max-gap`,
  che **riduce** la finestra cieca (96 s → 24 s) ma non la azzera: **campionare sempre a mano**
  dentro le finestre lunghe.
- **`frame_extractor.py` sulle lezioni del corso vuole `--input`**: il video è già su disco, ma
  senza URL lo script esce con «nessun URL». L'indirizzo sta in `mappa.json`. (`corso_prepara.py`
  non scrive `ingest.json`.)

- **Il modello del trascrittore NON si scarica da solo su questa macchina.** Tre fallimenti di
  fila: uno con `CAS Client Error` (trasferimento accelerato di HuggingFace), due con
  `SSL: DECRYPTION_FAILED_OR_BAD_RECORD_MAC` — firma tipica di un antivirus che ispeziona il
  traffico cifrato. **Soluzione già in casa:** il modello sta in `modelli/faster-whisper-base/`
  e `corso_trascrivi.py` lo usa da lì senza toccare la rete. Per aggiungerne un altro:
  `curl -sSL --retry 8 --retry-all-errors -C - -o model.bin https://huggingface.co/Systran/faster-whisper-<nome>/resolve/main/model.bin`
  (più `config.json`, `tokenizer.json`, `vocabulary.txt`).
- **L'indirizzo di una lezione richiede ANCHE la categoria**:
  `/courses/products/<corso>/modules/<categoria>/lessons/<lezione>`. Senza `modules/` la
  pagina si apre ma il lettore non carica nulla, e sembra «video assente» quando è solo un
  indirizzo incompleto. L'indirizzo giusto è già dentro `mappa.json`.
- **La barra laterale del portale naviga in JavaScript, senza collegamenti.** Non mappare a
  click: si intercetta la chiamata interna `user-purchase/categories`, che restituisce
  l'indice completo in un colpo.
- **⚠️ IL SALVATAGGIO AUTOMATICO DI FINE TURNO METTE IN STAGE TUTTO** (`git add -A`). Il
  2026-09-04 sono arrivato a un commit con **514 file in stage, compreso il profilo del
  browser con i cookie della sessione del portale a pagamento**. Escluso in `.gitignore`, ma
  **controllare `git diff --cached --name-only | wc -l` prima di ogni commit** resta
  obbligatorio: un push su repo pubblico non si annulla.
- **Video, frame e profilo browser NON vanno in git** (ADR-013): già esclusi. Il valore dello
  studio sono appunti, report e regole, che restano versionati.
- **Il gettone del video scade**: si cattura e si usa subito, una lezione per volta. Mai code.

- **✅ RISOLTO IL 2026-09-06 — il «gettone scaduto» non era un gettone scaduto.** Per due giorni
  tre lezioni (L11, L12, L18) sono rimaste in `1-fallito` con l'etichetta «HTTP 403, gettone
  scaduto». Era una diagnosi sbagliata scritta a memoria: il gettone era valido, **mancavano le
  intestazioni**. Il CDN del portale rifiuta chi non si presenta come il lettore della pagina.
  Due guasti in fila, e due correzioni in `corso_ingest.py`:
  1. **`ffprobe` non riusciva a misurare i flussi** (tutte le durate «?») e `scegli_flusso`
     rinunciava: ora ffprobe passa `Referer`, `Origin` e `User-Agent`, e se **nessun** candidato
     è misurabile non si rinuncia più — si prende l'ultimo visto, perché il controllo che conta
     (`durata_reale` sul file scaricato, che marca `1-sospetto`) resta attivo dopo.
  2. **`yt-dlp` prendeva 403 sul manifesto**: ora si presenta con le stesse intestazioni.
  Esito: **L11 scaricata, 1357 s attesi contro 1357 s reali.** Lezione di metodo: *un messaggio
  d'errore copiato in una nota non è una diagnosi — e una diagnosi non verificata invecchia
  peggio di nessuna diagnosi.*

## 7. IL CONTESTO CHE SERVE ALLA CHAT NUOVA

- **Assetto:** GOD EMPEROR DOOM, dichiarato all'apertura del lavoro.
- **Blocco ⚠️ COORDINAMENTO attivo** in `STATO-EMPIRE.md`: dice a Gael e Neri quali cartelle
  non toccare finché questo lavoro è in corso.
- **Credenziali del portale:** `~/.claude/corso-credenziali.json`, **fuori dal repository**.
  Nel codice non ci vanno mai (B-020/B-021/B-023).
- **Due difetti della fabbrica trovati e ancora APERTI di proposito** (in `BASELINE.md`):
  - **D-1** — `DURATA_MASSIMA_S=600` contro `PAROLE_MINIME_SCRIPT=2220` (=720 s): la fabbrica
    chiede l'impossibile. I due video del 2026-09-04 durano 826 s e sforano del 38%.
  - **D-2** — `verifica_qualita()` non è mai invocata dalla catena di produzione: per questo
    D-1 è rimasto invisibile.
  **Si chiudono al gate della categoria A6**, con il numero motivato dalla lezione sulla
  durata ottimale. Non tapparli prima con una toppa scelta a caso.

## 8. FILE TOCCATI

- `SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/corso_{ingest,trascrivi,prepara}.py` (nuovi)
- `company/Memory/plans/PIANO-STUDIO-AITUBEPRO.md` (v4, approvato)
- `company/Memory/studi/aitubepro/**` (baseline, regole, prima lezione)
- `YOUTUBE-AUTOMATION-FACTORY/04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` (nuovo)
- `YOUTUBE-AUTOMATION-FACTORY/03-AGENTI-E-RUOLI/{supporto/self-improver,operatori/niche-scout}.md`
- `.claude/agents/emperator.md` (riga `Assetto` nel battito), `scripts/emperator_boot.py` (impronta percorso)
- `.gitignore` (media dello studio + profilo browser)

- `SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/scene_detector.py` (presidio `--max-gap`)
- `company/Memory/studi/aitubepro/regole/registro.py` (`--da-applicare` ora interroga la fabbrica)

**Commit di riferimento:** `3f7b3136` (motore + baseline) · `6f56588b` (prima lezione chiusa)
· CP-20260904-008 (seconda lezione chiusa + due strumenti riparati)

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-V6DE`*
