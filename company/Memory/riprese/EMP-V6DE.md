# EMP-V6DE — Studio corso AI TUBE PRO: 167 lezioni → regole dentro la fabbrica YouTube

- **Codice di ripresa:** `EMP-V6DE`
- **Aperto:** 2026-09-04
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-V6DE` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

Studiare **167 lezioni** (AI TUBE PRO 116 + Bonus Esclusivi 51, portale
`corsi.muccarossa.com`, autore Mirko Delfino) e trasformare ogni lezione in **regole
eseguibili** applicate alla `YOUTUBE-AUTOMATION-FACTORY`. Piano approvato da Max il
2026-09-04: [PIANO-STUDIO-AITUBEPRO](../plans/PIANO-STUDIO-AITUBEPRO.md).

---

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
  **Registro: 20 regole, tutte a norma, 17 applicate, 3 in attesa del gate A4 (binario B).**
- **Ingestione riparata**: portava a casa il video sbagliato (L02 arrivata due volte con un altro
  video). Ora la durata si chiede al lettore vero, i flussi si misurano con ffprobe PRIMA di
  scaricare, e un file fuori tolleranza diventa `1-sospetto` e non si trascrive.
- **Il nastro gira**: `corso_prepara.py` lanciato il 2026-09-04 alle 21:48 ha già scaricato e
  trascritto **6 lezioni** di A4. Non va rilanciato: guarda `runs/corso-aitubepro/*/stato.json`.

**Cosa è cambiato nella fabbrica finora:**
- nuovo `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` (criterio di scelta, prima assente)
- `03-AGENTI-E-RUOLI/supporto/self-improver.md` §8 — sorveglianza settimanale col tetto di tempo
- `03-AGENTI-E-RUOLI/operatori/niche-scout.md` §8 — cataloghi AI come fonte di nicchie
- `03-AGENTI-E-RUOLI/operatori/transcript-collector.md` §8-§9 — sufficienza del materiale
  (conta le parole, sotto soglia pretende ≥2 fonti esterne) e via di riserva coi due guasti distinti
- `03-AGENTI-E-RUOLI/capi/capo-strategia.md` §8 — leva multilingua col suo costo dichiarato

## 3. COSA È RIMASTO A METÀ

- **162 lezioni su 167 da studiare** (3,0% fatto). Fatte `A4/L00`, `L01`, `L02`, `L03`, `L04`;
  A4 al 23,8% (5/21).
- **Verifica aperta assegnata al gate A4** (da `A4-L04-04`): ascoltare un MP4 già prodotto in
  `06-DASHBOARD-E-METRICHE/video-generati/` e stabilire **se i nostri video contengono musica**.
  Finché non si sa, il criterio «Bilanciamento Volumi» di `qa-audio-video` resta sospeso.
- **La fabbrica oggi non può produrre Shorts**: `aspectRatio` è la costante `"16:9"` a
  `fliki_client.py:258` (regola `A4-L04-02`, binario B).
- `corso_prepara.py` **eseguito il 2026-09-04**: 6 lezioni di A4 già pronte a nastro.
- **DURATE.md non esiste**: il censimento delle durate previsto dal piano non è stato fatto
  (la durata si legge lezione per lezione durante lo scaricamento, e finisce in `stato.json`).
- **CONFLITTI.md non esiste ancora**: nessun conflitto trovato nella prima lezione.

## 4. IL PROSSIMO PASSO ESATTO

**A4/L05** — annunciata a 30:19 della L04 come suo seguito diretto: «se volessi creare un video
**da zero**, cosa devo fare? Ve lo spiego nel prossimo tutorial». Le lezioni già scaricate e
trascritte si vedono in `runs/corso-aitubepro/<id>/stato.json` al passo `2-trascritto`
(`completata` = già chiusa).

```bash
cd "SKILL & Agenti/Empire Studio Suite/empire-studio/scripts"
# le lezioni pronte si vedono qui (passo = 2-trascritto):
#   runs/corso-aitubepro/<lesson_id>/stato.json
# per ognuna, prima delle frame: serve --input con l'URL preso da mappa.json
PYTHONIOENCODING=utf-8 py -3 frame_extractor.py --run "corso-aitubepro/<id>" --interval 4 --input "<url>"
PYTHONIOENCODING=utf-8 py -3 scene_detector.py  --run "corso-aitubepro/<id>" --threshold 6.0 --interval 4 --max-gap 24
# se il nastro si e' fermato, si rilancia (idempotente, salta le lezioni gia' fatte):
PYTHONIOENCODING=utf-8 py -3 corso_prepara.py --categoria "Metodo AI Tube"
```

Poi, per ogni lezione: appunti → report a sei voci → script regole → applicare il binario A.
A fine categoria: `REPORT-CATEGORIA.md`, `APPUNTI-CATEGORIA.md`, gate a 7 condizioni (piano §9).

**Ordine delle categorie** (piano §10): A4 Metodo AI Tube (21) → A6 Viral Mastery (10) →
B1 Masterclass 2026 (7) → B2 Crypto (10) → poi le altre.

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
