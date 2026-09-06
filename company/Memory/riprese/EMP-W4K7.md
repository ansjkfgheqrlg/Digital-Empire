# EMP-W4K7 — Lotto max18 - 9 video nuovi + Fase 2 implementazione

- **Codice di ripresa:** `EMP-W4K7`
- **Aperto:** 2026-09-04 14:25
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-W4K7` in una chat nuova dentro Digital Empire.
- **Ordine di Max che governa tutto:** *"vai avanti, studia chirurgico. Poi la Fase 2:
  implementare tutta la conoscenza."* Delega piena, nessuna approvazione da chiedere.
- **Predecessore:** `EMP-QQ2R` (lotto max17) — **Fase 1 chiusa**, tutti i video studiati.

---

## 1. IL LAVORO IN UNA FRASE

Studiare i 9 video del lotto **max18** consegnati da Max il 2026-09-04, e poi fare la
**Fase 2**: implementare dentro l'azienda i consigli raccolti in tutti gli studi (max17 +
max18), che finora sono solo scritti e mai applicati.

---

## 2. DOVE SIAMO — cosa e' FATTO davvero

**Chiusi end-to-end: 3 su 10** (9 video + 1 documento)

| Fonte | id | Stato |
|---|---|---|
| Documento Justin Sung | *(testo, no video)* | ✅ CP-20260904-004, wiki `Source_Justin_Sung_Guida_Apprendimento.md` |
| `max18-v02-karpathy-agenti` | `LCNk5e5EiCA` | ✅ CP-20260904-005, wiki `Source_Giovanni_Beggiato_Company_Brain_Karpathy.md` |
| `max18-v03-belli-token` | `1Dyld3y-V7Y` | ✅ CP-20260904-007, wiki `Source_Riccardo_Belli_Risparmiare_Token_Claude_Code.md` |

**`max18-v03` e' il modello da imitare per tutti i prossimi run.** Belli Contarini, 36:01,
screen-recording denso: **copertura totale 138/138 frame unici (100%)**, non campionamento —
e motivato, perche' le cifre chiave stanno sulla lavagna e **non vengono mai dette a voce**.
Ha prodotto il **primo `atoms.json` dell'Impero con gli archi**: 47 atomi, **96 archi
tipizzati, 0 rotti, 0 orfani**. E' la lezione di Justin Sung applicata lo stesso giorno.

**Il documento di Max ha chiuso il buco di Justin Sung** (`Pictures/materiale/Agency 2026 (1).md`,
510KB): conteneva la guida integrale sull'apprendimento. Trattato come **fonte testuale, non
video** — zero frame, dichiarato ovunque (`video_guardato: false`, 88 atomi con `frame: null`).

---

## 2-bis. AGGIORNAMENTO 2026-09-05 — ripresa in chat nuova

**Errore in apertura, registrato perche' non si ripeta:** ho dedotto il checkpoint dalle date
dei file del repo invece di leggere questo file, e sono partito su un lavoro sbagliato
(ecosistema LANCI). Due agenti hanno fatto in tempo a scrivere
`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/02-PREVISIONE-E-DENARO.md` e `03-FLUSSO-OFFERTA.md`:
restano su disco non committati, appartengono a `EMP-ECGA`, non a questo checkpoint.
**Regola:** il codice di ripresa si LEGGE, non si deduce.

**Fatto oggi su `max18-v01`:**
- I frame erano a **640x360** mentre `video.mp4` sul disco e' **1920x1080**: ci accecavamo da
  soli. Ri-estratti in `frames-hd/` a **1280x720** i **310 frame** delle scene 43-352
  (ffmpeg locale, nessun nuovo download, 310/310 riusciti). `frames/` non e' stato toccato.
- `_scene_index.json`: indice JSON delle 352 scene `{n, frame, ts}`, generato da `scenes.md`.
- Tre sentinelle schierate in parallelo sulle scene **43-145 / 146-250 / 251-352**, ognuna
  scrive il proprio `_parte-A|B|C.md` in append ogni 8 scene. L'unione in `video-analysis.md`
  la faccio io, per non far scrivere tre teste sullo stesso file.

**Ordine nuovo di Max, gia' chiuso nel codice (commit `fe35ab17`):** nessun identificativo di
checkpoint e' piu' progressivo. `CP-YYYYMMDD-XXXX` con quattro caratteri sorteggiati, unicita'
verificata su disco **e su tutta la storia git di ogni ramo**, file creato nell'istante del
conio. Comando: `python scripts/checkpoint.py cp --titolo "..."`. Vale anche per Gael
(`CLAUDE.md` aggiornato). La trappola "collisione di numeri checkpoint" del §6 e' chiusa.

---

## 2-ter. AGGIORNAMENTO 2026-09-06 sera - chat satura, si riparte da qui

**Chiuse end-to-end: 5 su 10.** Dettaglio completo in
[CP-20260906-23RG](../checkpoints/CP-20260906-23RG.md).

| Fonte | Visione | Atomi | Wiki | Archivio |
|---|---|---|---|---|
| doc Justin Sung · `v01` · `v02` · `v03` · `v07` | 100% | si | si | si |
| **`v06` corso agenti AI** | **209/376 = 55%** | -- | -- | -- |
| `v04` mindset · `v05` bot crypto · `v08` Cowork · `v09` vocali | 0% | -- | -- | -- |

**RIPRENDI DA QUI, in quest'ordine:**
1. `max18-v06-JTn5pqm9ecM`, buchi **211-376 e la scena 21** (167 scene). Sentinelle da 21 scene,
   scrittura ogni 5, **mai aprire `transcript.md` intero**.
2. Unione: `python scripts/unisci_parti.py --run max18-v06-JTn5pqm9ecM --scene 376`
3. Atomi a blocchi, poi `python scripts/unisci_atomi.py --run max18-v06-JTn5pqm9ecM`, poi
   **saldare le isole** del grafo (gli atomizzatori in parallelo non si vedono fra loro).
4. Wiki + `knowledge/JTn5pqm9ecM/` sul modello di `knowledge/RnoC5IlOUhs/`.
5. Poi `v08` (393 scene), `v09` (104, **senza sottotitoli: nessun VTT**), `v05` (98), `v04` (120).
6. Poi la **Fase 2**, poi il **Libro dell'Agency** (§4-bis).

**Strumenti nuovi, gia' pronti in `empire-studio/scripts/`:**
`vtt_to_transcript.py` (i transcript ci sono gia' per tutti tranne `v09`), `unisci_parti.py`,
`unisci_atomi.py`. Non riscriverli dentro i run.

**Leggi nuove di questa giornata:** i codici di checkpoint si **sorteggiano**
(`python scripts/checkpoint.py cp --titolo "..."`), e la percentuale del battito e'
l'avanzamento della **missione**, non del pezzo: 100% solo a lavoro finito.

---

## 3. COSA E' RIMASTO A META'

**Due run con i frame gia' estratti e l'analisi solo parziale.** Le sentinelle sono morte
per cause esterne, non per errore di merito:

| Run | id | Cosa c'e' su disco | Cosa manca |
|---|---|---|---|
| `max18-v01-second-brain-obsidian` | `RnoC5IlOUhs` | 1.390 frame, `scenes.json/md` (352 scene), `transcript.md`, `video-analysis.md` **parziale** | atoms, coverage, wiki, memory close |

**PRIMA DI RILANCIARLE: leggere cosa c'e' gia' nei loro `video-analysis.md`.** Il download e
l'estrazione dei frame sono la parte piu' cara e sono gia' fatti: non si rifanno mai.

**Sei video mai iniziati** (nessun run, nessun download):
`140FuW7b9pk` · `RnNSRF4s9nk` · `JTn5pqm9ecM` · `O2IDhISyy8Y` · `DI5aWJiFAt8` · `NmoOZVTrTXA`
Tutti verificati unici il 2026-09-04, nessun doppione col lotto max17.

---

## 4. IL PROSSIMO PASSO ESATTO

1. **Finire `max18-v01`** ripartendo dal suo `video-analysis.md` parziale (`max18-v03` e'
   gia' chiuso, vedi §2: la riga vecchia lo dava a meta' ed era sbagliata).
2. **Poi i sei mai iniziati**, a giri da massimo 2-3 sentinelle in parallelo.
3. **Poi la FASE 2 — e' quella che Max chiama "la cosa piu' importante in assoluto".**
   Implementare i consigli raccolti in tutti gli studi. Il primo e il piu' importante e'
   gia' identificato, vedi §5.
4. **PASSO FINALE — IL LIBRO DELL'AGENCY**, vedi §4-bis: il documento pubblico ufficiale in
   `.md` + `.py` + `.pdf` con il metodo Digital Empire e TUTTA la formazione acquisita.

---

## 4-bis. PASSO FINALE — IL LIBRO DELL'AGENCY (ordine di Max, 2026-09-05)

**Aggiunto da Max come ultimo pezzo della missione: viene DOPO la Fase 2, e chiude EMP-W4K7.**

### Cos'e'

Un **documento pubblico ufficiale** che contiene, in un corpo solo:

1. **IL METODO DIGITAL EMPIRE per scalare un'agenzia** — il nostro, preciso, operativo: come si
   acquisisce, come si vende, come si consegna, come si scala, con i numeri e i passi reali.
2. **TUTTA la formazione e la conoscenza acquisita** da cui quel metodo nasce — **ogni appunto,**
   **ogni dettaglio, integrale, mai riassunto** (regola di casa). Non un'appendice di rimandi:
   il materiale dentro il documento.

### In quali formati (tutti e tre, obbligatori)

| Formato | Dove | Note |
|---|---|---|
| `.md` | la sorgente, nella casa canonica del documento | e' la fonte di verita' del testo |
| `.py` | lo script che costruisce il PDF | sopra `PIANO-MAESTRO/scripts/pdf_engine_empire.py`, come `build_dossier28_pdf.py`. Mai stile scritto a mano |
| `.pdf` | generato dallo script | standard-oro dossier 28 (`emperator.md` §6.19): niente istruzioni di stile da chiedere |

**Piu' il doppione**, legge `emperator.md` §6.17: copia identica in
`documentazione Empire/Piani/Agency/` (la cartella esiste gia'). Mai spostare, copiare.

### Da dove esce il contenuto — materiale gia' sul disco, misurato il 2026-09-05

| Fonte | Quanto |
|---|---|
| `second-brain-vault/wiki/sources/` | **64 pagine fonte**, di cui **15** parlano di agenzia, acquisizione clienti, outreach, closing, prezzi |
| `empire-studio/memory-empire/knowledge/` | **70 cartelle** di contenuto integrale archiviato |
| `atoms.json` sparsi nei run | **147 file** di atomi |
| studi max17 (`EMP-QQ2R`) + max18 (questo) | tutti i `video-analysis.md` e le pagine wiki prodotte |
| skill `agency-scalping` | il metodo gia' codificato in casa, da confrontare e assorbire |

### Regole di costruzione — non negoziabili

- **Mai riassunti.** Il documento ESPANDE: ogni atomo di conoscenza entra piu' ricco, non piu'
  corto. Chi taglia per brevita' ha sbagliato lavoro.
- **Ogni affermazione porta la fonte esatta** (fonte + minuto/riga), come fa CONOSCENZA-EMPIRE.
- **Il metodo nostro sta separato** dalla formazione grezza: due parti dichiarate, non un
  impasto in cui non si capisce piu' cosa e' nostro e cosa e' di un altro.
- **Documento pubblico:** niente credenziali, niente nomi di clienti, niente numeri interni non
  destinati a uscire. Passa dal vaglio prima di essere dichiarato pubblico.
- Serve il **conteggio di copertura** alla consegna: quante fonti sono entrate su quante
  esistono. Si conta sul disco, non si dichiara.

---

## 5. DECISIONI GIA' PRESE — non ridiscuterle

- **Fase 1 = solo studio. Fase 2 = implementazione, e parte solo quando Max lo dice.**
  Ordine esplicito di Max, ripetuto due volte. Nessuna patch applicata durante gli studi:
  i consigli restano scritti nelle pagine wiki e nei checkpoint, in attesa.
- **Il primo lavoro della Fase 2, gia' individuato e misurato:** i nostri `atoms.json`
  **non hanno archi**, e `atomizer.py` non conosce `edge`/`relates_to`/`cluster`. Nel
  vocabolario di Justin Sung l'Impero produce **mappe di livello 1**, quelle che lui
  dimostra essere inutili. E' l'intervento a resa piu' alta di tutti.
- **Stessa classe, da controllare a tappeto in Fase 2:** `cf-knowledge-graph-agent`
  **dichiara** di costruire "edges, cluster" che nel codice non esistono; `book-to-skill`
  genera "summaries" mentre la regola di casa e' "mai riassunti". Capacita' dichiarate e
  mai implementate — stesso schema gia' segnato in EMP-QQ2R §3.
- **Zero learning science in tutto l'ecosistema di studio DE** (grep-verificato: gli unici
  match sono falsi positivi). Empire Studio, Memory Empire e CONOSCENZA-EMPIRE non
  applicano niente di cio' che l'Impero ha appena archiviato sull'apprendimento.

**Altri quattro lavori di Fase 2, trovati da `max18-v03` e tutti misurati sul codice:**
- **`frame_extractor.py:133` scarica a `--height default=360`: ci accechiamo da soli.** Non
  e' un limite di YouTube, e' la nostra pipeline che chiede il formato peggiore. Il flag
  `--height 720` esiste gia' e nessuno lo usa. Spiega perche' le sentinelle faticano a
  leggere il testo nei frame.
- **`scripts/peso_skill.py` misura il costo sbagliato**: pesa il corpo delle skill ma la
  parola `description` ha **0 occorrenze** nel file — non conta mai la voce che si paga a
  **ogni sessione per tutte le skill**. La misura dell'81% del peso va rifatta.
- **Decisione che spetta a Max — autocompact**: `agente-max/knowledge/K05-context.md:531`
  raccomanda Autocompact **ON**; il video lo chiama l'errore piu' grosso. In tutta
  `company/Memory` la parola "compact" ha **0 occorrenze**: non abbiamo mai deciso davvero.
- **L'auto-sync committa i file delle sentinelle mentre lavorano** (visto in diretta:
  commit `10c3b356` e `b71bef6d`). L'ordine "non fare git commit" dato alle sentinelle e'
  aggirato da un demone. Da sapere quando si ragiona su chi ha scritto cosa.
- **Fonte testuale ≠ video.** Quando il materiale arriva come testo si dichiara: nessun
  frame visto, `frame: null` sugli atomi. Mai lasciar intendere di aver guardato un video.

---

## 6. TRAPPOLE — errori gia' fatti, non rifarli

- **SCRIVI I FILE MAN MANO, MAI ALLA FINE.** Una sentinella e' morta con **175 scene su 352
  gia' guardate e zero scritte su disco**: buttato il lavoro piu' caro. Le altre due che
  scrivevano a blocchi hanno perso quasi niente.
- **Il limite di sessione dell'account uccide tutte le sentinelle nello stesso secondo**
  (successo il 2026-09-04 alle ~14:05, reset alle 14:10). Non e' un errore loro. Se muoiono
  tutte insieme con un `rate_limit`, guarda l'ora e aspetta il reset invece di rilanciare.
- **Massimo 5-6 immagini per messaggio a una sentinella**: con piu' vengono scartate tutte
  in silenzio.
- **I numeri di copertura si contano, non si ereditano.** Due sentinelle avevano dichiarato
  coperture false (182/270 dichiarati contro 108/270 reali; patch "applicate" mai esistite).
  Ogni cifra va ricontata sul disco.
- **Regola anti-invenzione che funziona** (provata su 88 atomi, ne ha presi 2 in fallo):
  ogni atomo tiene un'**ancora letterale** dal testo/frame, verificata con una ricerca prima
  di salvare. Chi cita a memoria sbaglia.
- **Le rielaborazioni AI di un documento contengono roba inventata**: nel documento di Max
  comparivano "Ikigai" e "Ignorance Tax" con **0 occorrenze** nella trascrizione vera. Si
  marcano come non dette dal relatore, non si cancellano.
- **`wiki/log.md` e' LF puro, non CRLF** — la nota vecchia in EMP-QQ2R diceva il contrario.
  Verifica i fine-riga reali del file invece di fidarti.
- **Collisione di numeri checkpoint**: Gael scrive sullo stesso repo in parallelo. Ricontrolla
  l'ultimo `CP-YYYYMMDD-NNN` libero **subito prima** di salvare, non all'inizio del lavoro.
- **`git add` solo dei propri file.** Sul repo girano in parallelo il lavoro YouTube e KDP di
  Gael + un auto-sync che committa da solo ogni ~10 minuti.

---

## 7. COMANDI PER RIPARTIRE

```bash
# dove eravamo
python scripts/checkpoint.py leggi EMP-W4K7
cat company/Memory/STATO-EMPIRE.md | head -60

# lo stato reale dei run max18
cd "SKILL & Agenti/Empire Studio Suite/empire-studio/runs"
for d in max18-*; do
  echo "$d frame:$(ls $d/frames 2>/dev/null|wc -l) analisi:$([ -f $d/video-analysis.md ] && echo SI || echo --) atomi:$([ -f $d/atoms.json ] && echo SI || echo --)"
done

# i sei video mai iniziati
# 140FuW7b9pk RnNSRF4s9nk JTn5pqm9ecM O2IDhISyy8Y DI5aWJiFAt8 NmoOZVTrTXA
```

## 8. FILE TOCCATI

`empire-studio/runs/` → `max18-doc-justin-sung`, `max18-v01-second-brain-obsidian`,
`max18-v02-karpathy-agenti`, `max18-v03-belli-token`
`empire-studio/memory-empire/knowledge/` → `justin-sung-learning-guide`, `LCNk5e5EiCA`
`second-brain-vault/wiki/sources/` → `Source_Justin_Sung_Guida_Apprendimento.md`,
`Source_Giovanni_Beggiato_Company_Brain_Karpathy.md`, + correzione a
`Source_Giovanni_Beggiato_Guida_Agenzia_AI.md` (soglie close rate)
`company/Memory/checkpoints/` → CP-20260904-004, CP-20260904-005
`company/Memory/riprese/` → `EMP-QQ2R.md` (Fase 1 chiusa), questo file
`.claude/agents/emperator.md` → due autocritiche registrate (§6-bis.4 e §6.11)

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-W4K7`*
