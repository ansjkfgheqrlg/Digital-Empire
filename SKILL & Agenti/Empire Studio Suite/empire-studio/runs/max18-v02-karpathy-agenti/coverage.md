# Coverage — max18-v02-karpathy-agenti

> Tutti i numeri di questo file sono **contati da me in questa sessione** interrogando i file
> su disco (`frames/manifest.json`, `scenes.json`, `atoms.json`, il `.vtt` deduplicato), non
> ripresi da altri documenti né stimati. Il comando di conteggio è riportato in fondo.

## Numeri (copertura TOTALE dei frame unici, campionamento aggiuntivo dichiarato)

- Video: **25m03s (1.503s)**, id `LCNk5e5EiCA`, canale Giovanni Beggiato. Scaricato a 360p
  (**13,91 MB**) con `frame_extractor.py --interval 3 --height 360`.
- Frame densi estratti (1 ogni 3,0s): **501** (`frame-001.png` → `frame-501.png`, 0:00:00 →
  0:25:00). Verificati contro `frames/manifest.json`: 501 PNG su disco = 501 voci nel manifest,
  nessun frame fallito.
- Frame unici (`scene_detector.py --threshold 6 --interval 3`): **69/501 (−86,2%)**.
- **Frame guardati nativamente in questa sessione: 80 su 501 totali (16,0%)**, così composti:
  - **69 su 69 frame unici — 100%.** Nessun frame unico è rimasto chiuso (verificato per
    differenza di insiemi contro `scenes.json`: lista vuota in entrambe le direzioni).
  - **+ 11 frame aggiuntivi fuori dalla lista unici**, scelti a mano per una ragione specifica
    documentata sotto (`frame-345` e i 10 frame della lavagna 19:57→24:27).
- **Trascrizione audio: 100% letta.** Sorgente `LCNk5e5EiCA.it.vtt` (1.837 righe di testo grezze,
  formato rolling-caption di YouTube con ogni riga ripetuta in costruzione) deduplicata con uno
  script Python locale in **612 righe uniche con timestamp**, lette per intero in **2 blocchi**
  (righe 1-310 e 310-613) da 0:00:02 a 0:24:59. Letta anche la coda della traccia `en-US`
  (557 righe uniche) per completare la frase finale troncata.
- **Atomi estratti in `atoms.json`: 43** — 41 osservati, 2 inferiti (marcati `inferito`);
  39 con riferimento a un frame preciso, 4 solo audio.

Questa **è** una copertura totale delle scene uniche. Il campione aggiuntivo di 11 frame **non**
è un ripiego: è una correzione di un difetto dello strumento, spiegata sotto.

## Perché questa strategia è proporzionata a QUESTO video

Il formato è **misto, ma con un baricentro visivo forte** — molto diverso da `max17-v16` (evento
dal vivo, contenuto quasi tutto nell'audio) e da `max17-v17` (4h17, dove il campionamento era
inevitabile):

1. **~9 minuti concettuali (0:00→8:52)** — talking-head + slide Excalidraw preparate + tre
   screen-share brevi (post X di Karpathy, vault Obsidian, sito gentes.ai). Le slide restano
   ferme a lungo (`scenes.md` registra schermate da 93s, 99s, 60s), quindi qui i frame unici
   coincidono quasi 1:1 col contenuto.
2. **~10 minuti di screen-share denso (8:53→19:21)** — Antigravity IDE, Claude Code, Notion,
   PandaDoc. **Qui ogni frame porta informazione che l'audio non trasmette**: il testo integrale
   dei due prompt, l'output di verifica di Claude, i limiti delle chiavi API, il transcript della
   call, il listino stampato sul PDF. Nessuno di questi contenuti è pronunciato a voce.
3. **~5 minuti di lavagna disegnata dal vivo (19:22→24:41)** — vedi il problema qui sotto.

Con 501 frame totali e 69 unici, guardarli **tutti** costava poco più che campionarli, e la
sezione 2 rendeva il campionamento sbagliato in linea di principio: su uno screen-share, saltare
frame significa saltare testo. Per questo la copertura unici è al 100% e non c'è nessuna
dichiarazione di campionamento da giustificare per il grosso del video.

## Il problema trovato in `scene_detector.py`, e come l'ho corretto

`scene_detector.py --threshold 6 --interval 3` dichiara che il tratto **19:24 → 24:45 è UNA SOLA
schermata di 321 secondi** (riga `frame-389` di `scenes.md`, colonna "schermata dura": 321.0s).

**È falso.** In quei 321 secondi l'autore costruisce a mano, su una lavagna Excalidraw bianca,
l'intero ragionamento sul value-based pricing: due parole, due cifre di costo, una formula, un
ramo ROI e due risultati cerchiati. Il detector non lo vede perché confronta miniature in scala di
grigi **64×64**: qualche tratto di penna nera su fondo bianco non muove la media dei pixel sopra
soglia 6,0.

Me ne sono accorto perché **la trascrizione descriveva calcoli che nessun frame unico mostrava** —
il parlato parlava di una formula, di 10 ore, di 2.500 € a cliente e di 5.000 €/mese, e nella
lista dei 69 unici non c'era una sola schermata con quei numeri. Invece di scrivere quei contenuti
"da trascrizione" (che sarebbe stato legittimo ma povero), ho **campionato a mano quel tratto ogni
10 frame (30 secondi)**: `frame-400, 410, 420, 430, 440, 450, 460, 470, 480, 490`. Tutti e dieci
mostrano stati diversi della lavagna. La ricostruzione dell'evoluzione è la tabella in
`video-analysis.md` §"PARTE 8".

**Conseguenza da registrare per le prossime run**: `scene_detector.py` è affidabile su
screen-share e slide, **non** su lavagne disegnate a mano dal vivo. Su un video con
whiteboard live va o abbassata molto la soglia solo su quel tratto, o campionato a mano. Non è un
bug da correggere alla cieca — abbassare la soglia globale farebbe esplodere il conteggio sullo
screen-share — è un limite del metodo da conoscere.

L'undicesimo frame extra, `frame-345` (17:15), l'ho aperto perché `frame-344` (unico, 17:09)
mostrava l'Explorer dell'IDE ancora senza la skill generata, e volevo verificare **a schermo** la
struttura reale di `.claude/skills/genera-proposta/` invece di dedurla dalla slide di
architettura. La struttura letta coincide con la slide (KA-019).

## Come è stata condotta la copertura

- **Ingest**: `python scripts/yt_ingest.py --input "https://www.youtube.com/watch?v=LCNk5e5EiCA"
  --run max18-v02` → `ingest.json` (16 capitoli ufficiali, usati per strutturare
  `video-analysis.md`), `LCNk5e5EiCA.info.json`, due tracce sottotitoli (`it`, `en-US`),
  thumbnail. La cartella è stata poi rinominata `max18-v02-karpathy-agenti` una volta noto il
  titolo. ⚠️ Nota: i percorsi dentro `ingest.json` (`"subs"`, `"thumbnails"`) puntano ancora a
  `runs\max18-v02\` — **stringhe stale lasciate come sono**, i file sono nella cartella
  rinominata; `frame_extractor.py` non le usa (legge `url`), quindi non hanno rotto nulla.
- **Frame**: `python scripts/frame_extractor.py --run max18-v02-karpathy-agenti --input "<url>"
  --interval 3 --height 360`. Scelta dell'intervallo fatta **dopo** aver letto `duration_sec:
  1503` in `ingest.json`: 25 minuti è la fascia media, ma la presenza di 10 minuti di
  screen-share con codice e prompt ha spinto verso l'estremo denso della fascia (3s invece di
  4-6s) → 501 frame, ben sotto il tetto di ~2.000.
- **Scene**: `python scripts/scene_detector.py --run max18-v02-karpathy-agenti --threshold 6
  --interval 3`. Soglia 6 invece della default 3 perché il video ha molte transizioni di taglio
  video (camera → schermo) che a soglia 3 avrebbero moltiplicato i falsi positivi.
- **Trascrizione**: script `clean_vtt.py` salvato nello scratchpad di sessione (non nel repo),
  che tiene solo le righe di testo **senza** tag `<c>` (le righe "settlement" del cue, non quelle
  ancora in costruzione parola-per-parola), scarta le ripetizioni identiche alla riga precedente e
  preserva il timestamp di ogni cue. Nessun contenuto riscritto o riassunto — solo compressione
  meccanica del formato.
- **Frame guardati**: 16 chiamate di lettura da 4-5 immagini l'una, mai più di 5 per messaggio
  (limite noto: sopra 5-6 le immagini vengono scartate in silenzio).
- **Verifica contro la codebase DE**: prima di scrivere la sezione "Consigli" della pagina wiki
  ho verificato con `Grep`/`ls` — non a fiducia — l'esistenza e il contenuto di:
  `.claude/skills/proposal-gate/SKILL.md`, `beast-preventivi/SKILL.md` +
  `references/stages/02-pricing.md`, `pricing/SKILL.md`, `preventivo-auto/SKILL.md`,
  `memory-empire/SKILL.md`, `sync-wiki-totale/SKILL.md`, `skill-contradiction-analyzer/SKILL.md`,
  `agency-scalping/SKILL.md`, `cro-call/SKILL.md`, `second-brain-vault/CLAUDE.md`,
  `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py`. Risultati e comandi nella
  sezione "Consigli" della pagina wiki, riportati come esito di ricerca e non come impressione.

## Frame illeggibili o parzialmente illeggibili

- **Nessun frame è risultato corrotto o vuoto**: 501/501 estratti, 501/501 apribili.
- **Testo parzialmente illeggibile in 3 punti, tutti dichiarati anche in `video-analysis.md`:**
  1. `frame-005` / `frame-204` — l'ultima riga della Regola 3 del Prompt 1 esce dal bordo inferiore
     dello schermo. La parola finale (`chiavi`) è **ricostruita per senso, non letta**.
  2. `frame-387` — alcune righe del transcript della discovery call sono coperte dal pannello
     Explorer sulla sinistra. È riportato solo ciò che è leggibile con certezza; la barra di stato
     dichiara `Ln 33`, quindi il file è di ~33 righe e la porzione recuperata ne copre la sostanza
     ma non la totalità carattere per carattere.
  3. `frame-008` / `frame-022` — il contatore delle note del vault Obsidian legge **"3515 notes"**,
     ma il testo è molto piccolo: **confidenza media**, dichiarata come tale sia in
     `video-analysis.md` sia nell'atomo KA-043.
- **Mai ingrandito a schermo, quindi mai descritto** (regola NO-FINTO): il contenuto di
  `pandadoc.py`, `create_proposal.py`, `inspect_template.py` (solo nomi di file in `frame-345`) e
  il contenuto del `CLAUDE.md` generato (noto solo dal prompt che lo commissiona e dal riassunto
  che Claude ne fa — due fonti concordi, nessuna delle due è il file). Entrambe le lacune sono
  registrate come atomo KA-041, non nascoste.

## Correzioni / cautele di lettura documentate per trasparenza

- **Il claim "AI slop" dell'autore non regge al frame.** A 7:37 l'autore liquida l'output senza
  cervello come *"quasi AI slop"* e dice *"non ha nemmeno il nostro logo"*. Guardando davvero
  `frame-155`, quell'artifact è un documento impaginato con gerarchia tipografica e "Gentes.AI"
  presente come testo. Manca il **logo immagine**, il template brandizzato e il canale di
  firma/pagamento. Registrato come atomo `inferito` KA-042 e come cautela in `video-analysis.md`:
  la differenza reale dimostrata dal video è **funzionale**, non estetica.
- **Nessuna incoerenza di prezzo nel video** — verificata attivamente, non assunta. Le cifre
  (1.000 setup + 500×2 = 2.000 standard; 600 + 80/meeting performance; 50/50 di pagamento)
  compaiono in **tre punti indipendenti** — il transcript-fonte in `frame-387`, il check
  dell'agente in `frame-162`, il PDF finale in `frame-383` — e coincidono esattamente. Anche il
  frame di anteprima dell'hook (`frame-004`, 0:09) mostra gli stessi 2.000 €/600 €.
- **Coerenza parlato/lavagna verificata numero per numero**: `$200`/`$59` in `frame-420` = i costi
  detti a 20:28; `5.000 €/mese` in `frame-460` = il calcolo 2 clienti × 2.500 € detto a 22:43;
  `6.000 €/mese` in `frame-480` = la conclusione detta a 23:12; `EN/IT/FR/DE` in `frame-490` =
  l'esempio dei macchinari multi-mercato detto a 24:12. Nessuna deriva.
- **La data del video è luglio 2026, non settembre.** Il documento in dashboard PandaDoc è datato
  `Jul 22, 2026`, la proposta `23 luglio 2026`, la call-fonte `10 luglio 2026`. La community Skool
  mostra scadenze "entro 26/30 luglio" e "entro 15 agosto". Il video è quindi stato registrato
  intorno al 23 luglio 2026, non è materiale del giorno dell'ingest (2026-09-04).
- **`wiki/log.md` non ha CRLF.** Il brief di questa sentinella chiedeva di "mantenere il CRLF
  esistente" in `second-brain-vault/wiki/log.md`. Verificato con Python (`d.count(b'\r\n')`):
  il file ha **0 CRLF e 1.690 LF**, cioè è già interamente LF; stesso esito per `wiki/index.md`
  (0 CRLF, 1.743 LF). Ho quindi scritto in **LF**, che è ciò che il file ha davvero. Segnalato
  perché un'istruzione basata su uno stato superato può far introdurre a un'altra sentinella
  proprio il file misto che il guardiano vuole evitare.
- **Nessun numero dichiarato dall'autore è stato verificato indipendentemente da me** oltre a
  quanto confermato a schermo: $4M+ di risparmi in Amazon, top 2% dei dipendenti, team da 40
  persone e progetti da $100M in P&G, clienti "da €10.000 al mese fino ai 50 milioni di euro
  l'anno". Sono riportati sempre come *dichiarazione dell'autore / claim letto sul sito*, mai come
  fatto.

## Riepilogo finale

- **Frame guardati nativamente: 80/501 (16,0%) — di cui 69/69 frame unici (100%).** Copertura
  totale delle scene uniche, più 11 frame extra scelti per una ragione dichiarata.
- **Trascrizione audio: 612/612 righe uniche lette (100%)**, corrispondenti a tutte le 1.837 righe
  grezze del `.vtt`, in 2 blocchi, da 0:02 a 24:59 (gli ultimi ~4 secondi del video non hanno
  sottotitoli in nessuna delle due tracce).
- **Atomi: 43** (41 osservati, 2 inferiti; 39 con riferimento frame, 4 solo audio).
- **Nessun frame è stato descritto senza essere stato realmente aperto e guardato in questa
  sessione** (regola NO-FINTO). Dove un contenuto è noto ma non è stato visto (codice degli script,
  `CLAUDE.md` generato, righe coperte del transcript, ultima parola della Regola 3) è **sempre**
  qualificato come tale, in `video-analysis.md`, in `atoms.json` e qui sopra.
- **Cosa ho trovato di sospetto**: (a) il detector di scene dà per statico un tratto di 5 minuti
  in cui l'autore scrive tutto il ragionamento sul pricing — limite di metodo, non del video;
  (b) la retorica "AI slop" non corrisponde a ciò che il frame mostra; (c) il brief chiedeva di
  preservare un CRLF che in `wiki/log.md` non esiste più. Nel **contenuto** del video, invece,
  non ho trovato incoerenze: tutti i numeri controllabili tornano su fonti multiple.

## Comandi di conteggio usati (riproducibili)

```python
# dalla cartella runs/max18-v02-karpathy-agenti
import json, glob
len(glob.glob('frames/frame-*.png'))                       # 501
len(json.load(open('frames/manifest.json'))['frames'])     # 501
s = json.load(open('scenes.json')); s['frame_unici_da_guardare']   # 69
a = json.load(open('atoms.json')); len(a)                  # 43
sum(1 for x in a if x['confidenza'] == 'osservato')         # 41
sum(1 for x in a if x.get('frame'))                         # 39
# differenza di insiemi: unici da scenes.json vs frame effettivamente aperti -> vuota
```
