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

1. **Finire `max18-v01` e `max18-v03`** ripartendo dai loro `video-analysis.md` parziali.
2. **Poi i sei mai iniziati**, a giri da massimo 2-3 sentinelle in parallelo.
3. **Poi la FASE 2 — e' quella che Max chiama "la cosa piu' importante in assoluto".**
   Implementare i consigli raccolti in tutti gli studi. Il primo e il piu' importante e'
   gia' identificato, vedi §5.

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
