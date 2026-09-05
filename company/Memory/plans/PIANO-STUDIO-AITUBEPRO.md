# PIANO DI STUDIO — AI TUBE PRO (Smart Tube) + Bonus Esclusivi
## v4 — architettura operativa, contratti e gate

> **Stato: PROPOSTA. Non si parte senza il via di Max** (ordine esplicito, 2026-09-04).
> Autore: Emperator · Fonte: `corsi.muccarossa.com` — Mirko Delfino
> **Scopo, in una riga:** trasformare 167 lezioni in **regole eseguibili** che facciano
> pubblicare alla `YOUTUBE-AUTOMATION-FACTORY` più video, migliori, con più CTR — e poterlo
> **dimostrare con numeri**, non raccontare.

---

# PARTE I — IL TERRENO

## 1. Censimento reale (misurato entrando nel portale, non stimato)

| Corso | Lezioni | Perimetro |
|---|---|---|
| **AI TUBE PRO — SMART TUBE** | **116** | ✅ |
| **Bonus Esclusivi** | **51** | ✅ |
| Google Automation Platinum | 181 | ❌ fuori perimetro (ordine di Max) |
| **DA STUDIARE** | **167** | |

### 1.1 AI TUBE PRO — 11 categorie

| # | Categoria | Lez. | Bersaglio nella fabbrica |
|---|---|---|---|
| A1 | Intelligenza Artificiale | 12 | catalogo strumenti, `04-SKILLS-E-REFERENCE/references` |
| A2 | Le Basi di YouTube | 7 | WF1 · `niche-gate.md` · `regolatore-nicchia` |
| A3 | YouTube Setup & Launchpad | 15 | WF1 · branding canale · `channel-scout` |
| A4 | **Metodo AI Tube** | **21** | **WF3 · `fliki_client.py` · `script-writer` · `voice-caster`** |
| A5 | Smart Tube (smartphone) | 16 | quasi nulla — §5.3, dichiarato |
| A6 | **YouTube Viral Mastery** | **13** | **WF4 · `seo-gate` · `thumbnail-designer` · `metadata-optimizer`** |
| A7 | YouTube Masterclass | 7 | strategia · multicanale · `capo-strategia` |
| A8 | Liveclass Studenti | 11 | casi reali, correzioni di rotta |
| A9 | BONUS | 9 | masterclass verticali |
| A10 | Interviste Speciali | 3 | ads, engagement |
| A11 | Workshop | 3 | scaling, dietro le quinte |

### 1.2 Bonus Esclusivi — 3 categorie

| # | Categoria | Lez. | Nota |
|---|---|---|---|
| B1 | **Masterclass 2026** | 8 | **il materiale più fresco**: Fliki 4.0, miniature ad alto CTR, video automatici infiniti |
| B2 | **Nicchia Criptovalute** | 11 | verticale completo end-to-end: è il **modello replicabile** per aprire una nicchia |
| B3 | Masterclass Storiche 2019-2025 | 32 | archivio; valore che decade col tempo |

## 2. Vincoli tecnici accertati (aperta una lezione vera, non dedotto)

| Fatto | Conseguenza sul piano |
|---|---|
| Video serviti a pezzi (HLS) da `content.apisystem.tech`, **gettone a scadenza**, fino a 1080p | serve ingest dedicato: browser → cattura indirizzo+gettone → scarico **una lezione per volta**, mai code lunghe |
| **Nessun testo, nessun sottotitolo, nessun allegato** | la conoscenza sta **solo** in parlato + schermo → trascrizione **obbligatoria**, non accessoria |
| `ffmpeg` 8.1.1 ✅ · `yt-dlp` 2026.08.19 ✅ | scaricamento e frame coperti da strumenti già in casa |
| **nessun trascrittore installato** (`whisper`, `faster-whisper` assenti) | **unica installazione richiesta dal piano** — senza, guardo il corso muto |
| Il lettore espone durata reale (es. 14:24 sulla prima) | il censimento durate è possibile e va fatto **prima** di stimare qualunque tempo |

## 3. Cosa esiste già e NON va riscritto (ADR-003: si avvolge, non si riscrive)

**Empire Studio** ha la pipeline a 9 stage, gli invarianti giusti (*il video va visto*,
*no-finto*, tracciabilità `video-id#ts + frame-NNN.png`), `frame_extractor.py`,
`scene_detector.py`, `wiki_writer.py`, `save_to_memory_empire.py`, `validator.py`.
**Manca solo l'ingest**: `yt_ingest.py` parla YouTube/TikTok, non una piattaforma a login con
flusso protetto. → si **affianca** `corso_ingest.py`. Zero righe tolte a ciò che gira.

**La fabbrica** ha 5 flussi (WF1 nicchia → WF5 audit), **33 agenti** su 4 livelli e
**5 regolatori** con soglie dure in `regolatori.py`. È il bersaglio: le lezioni atterrano lì.

> ⚠️ **Incoerenza già in casa, trovata oggi producendo i video** — due soglie di durata che
> si contraddicono: `regolatori.DURATA_MINIMA_S = 480` (8 min) contro
> `apex7_orchestrator.PAROLE_MINIME_SCRIPT = 2220` (~12 min). Una lezione del corso sulla
> durata ottimale (A6) è l'occasione per **chiuderla con un numero motivato**, non per
> lasciarne due.

---

# PARTE II — L'ARCHITETTURA

## 4. Il reparto nuovo: `corso-lab`

Non un mucchio di script: un reparto con confini netti, dentro Empire Studio.

```
SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/
└── corso_ingest.py          NUOVO — login, cattura flusso+gettone, scarica 1 lezione
                             (--lezione <id> | --categoria <slug>), idempotente

company/Memory/studi/aitubepro/
├── PIANO.md                 questo documento
├── BASELINE.md              lo stato della fabbrica PRIMA di studiare (§7)
├── DURATE.md                censimento durate reali delle 167 lezioni
├── CONFLITTI.md             dove il corso contraddice ciò che facciamo, e chi ha vinto
├── <CAT>/L<NN>-<slug>/
│   ├── appunti.md           grezzi, integrali, ogni riga col minuto esatto
│   ├── report.md            la lezione digerita (§6.2)
│   ├── frame-scelti.md      quali frame ho guardato e PERCHÉ
│   └── stato.json           avanzamento macchina-leggibile (ripresa, idempotenza)
├── <CAT>/REPORT-CATEGORIA.md    ← a fine categoria (ordine di Max)
├── <CAT>/APPUNTI-CATEGORIA.md   ← a fine categoria (ordine di Max)
└── regole/
    ├── registro.py          carica, interroga, verifica TUTTE le regole
    ├── schema.py            il contratto (§6.3) — una regola non conforme non entra
    └── <CAT>/L<NN>_<slug>.py    uno script per lezione (ordine di Max)
```

**Video e frame restano fuori da git** — ADR-013, e non è teoria: un push è già morto a
899 MB e un `git stash pop` ha quasi spedito 13,4 GB su un repo pubblico.

## 5. Le forze — chi fa cosa

| Grado | Nome | Missione |
|---|---|---|
| **SENTINELLA** | `sentinella-durate` | passo zero: apre le 167 lezioni, legge le durate, scrive `DURATE.md`. Non guarda, non giudica |
| **SENTINELLA** | `sentinella-ingest-<cat>` | scarica + trascrive le lezioni di **una** categoria. Non interpreta |
| **SCAGNOZZO** | `scagnozzo-verifica-<cat>` | dopo ogni categoria: rilegge a campione 3 regole e controlla che la prova (frame/minuto) esista davvero |
| **io** | — | guardo i frame, scrivo appunti e report, decido le regole, tocco la fabbrica |

**Cosa non delego mai:** la visione dei frame, la decisione, la modifica alla fabbrica, la
parola a te. Una sentinella che "ha guardato" non è una prova: è un self-report, e in questa
casa i self-report hanno già mentito una volta (recupero EMP-QQ2R).

---

# PARTE III — IL PROTOCOLLO

## 6. Per OGNI lezione — 7 passi, criteri di uscita verificabili

### 6.1 I passi

| # | Passo | Fatto quando |
|---|---|---|
| 1 | **Scarico** il video | `video.mp4` esiste, durata ±2s da `DURATE.md` |
| 2 | **Trascrivo** il parlato | `parlato.txt` esiste, ≥ 60 parole/minuto di video (sotto = trascrizione fallita, non lezione silenziosa) |
| 3 | **Estraggo i frame** e tolgo i doppioni | `frames/` + `scenes.json`; scarto atteso 85-95% |
| 4 | **Guardo** i frame scelti | ogni frame guardato è **elencato** in `frame-scelti.md` col motivo |
| 5 | **Appunti** integrali | ogni blocco porta `mm:ss`; **mai riassunti** |
| 6 | **Report** della lezione | le 6 voci di §6.2, tutte compilate |
| 7 | **Script regole** | passa `schema.py`; ≥1 regola **oppure** la dichiarazione esplicita «nessuna regola nuova, e perché» |

### 6.2 Il report di lezione — sei voci obbligatorie

1. **Cosa insegna** — la sostanza, non il sommario.
2. **Cosa facciamo oggi** — lo stato reale della fabbrica su quel punto, con file e riga.
3. **Delta** — la distanza fra i due. È il cuore: se il delta è zero, si scrive zero.
4. **Conflitti** — dove il corso contraddice una nostra scelta. Va in `CONFLITTI.md`, con
   l'arbitrato: chi vince e **perché** (il corso non ha ragione per definizione).
5. **Regole estratte** — con id, prova, bersaglio, rischio.
6. **Applicabilità** — quanto di questo vale per un motore Python su PC. La risposta
   «poco» è ammessa e va scritta; inventare miglioramenti è finzione, ed è vietato.

### 6.3 Il contratto di una regola — se non lo rispetta, non entra

```python
# regole/A4-metodo-ai-tube/L07_text_to_speech.py
FONTE   = "AI TUBE PRO / A4 Metodo AI Tube / L07"
LEZIONE = "Text to speech cosa è, e come funziona"

REGOLE = [{
    "id":       "A4-L07-01",          # <categoria>-<lezione>-<progressivo>, univoco
    "tipo":     "parametro",          # parametro | procedura | vincolo | euristica | strumento
    "regola":   "...",                # in italiano, imperativa, una frase
    "prova":    "frame-0142.png @ 08:31",   # dove l'ho VISTA — o "solo parlato @ 08:31"
    "fonte":    "schermo",            # schermo | parlato | entrambi
    "tocca":    "02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py",
    "azione":   "modifica",           # modifica | nuovo | conferma | scarta
    "binario":  "B",                  # A = subito · B = fine categoria (§8)
    "rischio":  "medio",              # basso | medio | alto
    "misura":   "durata media video +15%",  # come si vede se ha funzionato
}]

def verifica(fabbrica) -> dict:
    """Dice se la fabbrica rispetta GIÀ questa regola. Nessun effetto collaterale."""
```

**Perché un contratto e non prosa libera:** 167 documenti in libertà sono 167 documenti che
nessuno rilegge. Con lo schema, `registro.py` risponde a domande vere —
*«quante regole toccano `fliki_client.py`?»*, *«quante ad alto rischio sono ancora da
applicare?»*, *«quali regole non hanno una prova?»* — e le regole diventano **interrogabili**.

### 6.4 Regola di discrepanza: **lo schermo batte il parlato**

Quando la voce dice una cosa e lo schermo ne mostra un'altra, **vince lo schermo** e la
discrepanza si annota. Motivo misurato oggi su un altro studio: un relatore dice «9%» mentre
la dashboard mostra 9,09% — il numero vero è quello a schermo. Se non ho guardato il frame,
scrivo *«solo parlato»* e la regola nasce con rischio più alto.

### 6.5 Campionamento dei frame — soglie, non «a occhio»

| Tipo di lezione | Passo di estrazione | Quanti frame guardo |
|---|---|---|
| tutorial a schermo condiviso (la maggioranza) | 4s | **tutti** i frame unici dopo lo scarto |
| talking-head / liveclass | 10s | i soli frame unici, più i minuti dove il parlato cita qualcosa di visivo |
| lavagna / diagrammi | 6s | tutti gli unici + i fotogrammi di transizione |

Il tipo lo decido **dopo** aver visto i primi due minuti, mai prima: tre formati diversi
osservati in altri studi hanno già smentito ogni regola fissa decisa a tavolino.

---

# PARTE IV — L'APPLICAZIONE

## 7. Baseline — senza questa, «migliorato» è una parola

**Prima di studiare una sola lezione** fotografo la fabbrica, e i numeri finiscono in
`BASELINE.md`:

| Metrica | Come la misuro |
|---|---|
| test della fabbrica verdi | `python test_youtube_apex7.py` (oggi dichiarati 11/11 — **da riverificare**, non da credere) |
| soglie dei gate | i valori attuali in `regolatori.py` e `apex7_orchestrator.py`, copiati esatti |
| video prodotti / pubblicati | `memory/video_prodotti.json` (8 voci a oggi) |
| CTR e visualizzazioni per video | YouTube Studio, i video già pubblicati |
| durata media, parole medie | dai video reali, non dai template |
| quanti dei 33 agenti hanno criteri numerici | conteggio su `03-AGENTI-E-RUOLI/` |

A fine di ogni categoria, gli stessi numeri. **Il piano si giudica sul movimento di questi
numeri**, non su quante lezioni ho visto.

## 8. I due binari — il punto su cui ti contraddico

**Il tuo ordine:** dopo ogni lezione, migliorare il workflow.
**Il fatto:** la fabbrica **sta producendo video veri adesso** (tre oggi). 167 modifiche di
fila al motore in produzione, senza collaudo in mezzo, è il modo più rapido per romperla —
e ADR-003 vieta di riscrivere un sistema attivo senza sostituto validato.

| | **BINARIO A — dopo OGNI lezione** | **BINARIO B — a fine categoria** |
|---|---|---|
| Tocca | agenti (`03-AGENTI-E-RUOLI/`), regolatori documentali, reference, skill, script delle regole, wiki | il motore (`02-AUTOMAZIONI-E-SCRIPTS/`), le soglie dei gate, `fliki_client.py`, l'orchestratore |
| Rischio | **zero** — nessun video in produzione ci passa | reale — di lì passano i video |
| Collaudo | `schema.py` + `registro.py --verifica` | test della fabbrica verdi **+ un video di prova end-to-end** |
| Reversibile | sì, commit singolo | sì, ma il video sbagliato l'hai già pagato in crediti |

**Dopo ogni lezione la fabbrica migliora davvero**: il binario A non è un contentino, gli
agenti e i regolatori **sono** il cervello della fabbrica. Il motore cambia quando c'è una
batteria coerente di regole e un collaudo che le regge.

**Se vuoi il rischio, lo prendo:** una tua parola e applico tutto subito, motore compreso.

## 9. Il gate di fine categoria — cinque condizioni, tutte verificabili

Una categoria è **chiusa** solo se:

1. `REPORT-CATEGORIA.md` + `APPUNTI-CATEGORIA.md` scritti (tuo ordine).
2. Ogni lezione ha `stato.json` a `completata` — nessun «quasi».
3. `registro.py --verifica <CAT>` → **zero** regole senza prova, zero fuori schema.
4. Le regole di binario B **applicate**, con test della fabbrica **verdi** e un video di prova.
5. **Baseline riletta**: i numeri di §7 aggiornati, con il delta scritto in chiaro.
6. `scagnozzo-verifica-<cat>` ha ricontrollato 3 regole a campione e le prove esistono.
7. **Checkpoint di ripresa** `EMP-XXXX` + commit + push.

**Se una categoria chiude con zero regole applicate, è una categoria fallita** e lo scrivo
in chiaro. Non si finge un raccolto.

## 10. Priorità — l'ordine è una decisione, non una comodità

Studiare 167 lezioni tutte alla stessa profondità è **esso stesso un errore**: spendere su
«Come registrarsi alla community» ciò che serve a «SEO YouTube manuale operativo».

| Profondità | Cosa faccio | Categorie |
|---|---|---|
| **ORO** | 7 passi pieni, frame fitti, regole complete | A4 · A6 · B1 · B2 · A7 |
| **ARGENTO** | 7 passi, frame più radi | A2 · A3 · A1 · A9 · A10 |
| **BRONZO** | parlato + soli frame unici; regole solo se emerge davvero qualcosa | A8 · A11 · A5 · B3 |

**Ordine di attacco** — dal più vicino al collo di bottiglia:

| Ord. | Categoria | Lez. | Perché prima |
|---|---|---|---|
| 1 | **A4 Metodo AI Tube** | 21 | è il cuore della produzione: script, voce, montaggio, Fliki |
| 2 | **A6 YouTube Viral Mastery** | 13 | SEO, copertine, CTR, pubblicazione — dove non stiamo pubblicando |
| 3 | **B1 Masterclass 2026** | 8 | il più recente: Fliki 4.0 e miniature ad alto CTR |
| 4 | **B2 Nicchia Crypto** | 11 | un verticale intero: il modello per aprire una nicchia nuova |
| 5 | A7 + A2 + A3 | 29 | strategia, basi, impostazione canale |
| 6 | A1 + A9 + A10 | 24 | strumenti, bonus, interviste |
| 7 | A8 + B3 + A5 + A11 | 62 | archivio e smartphone, valore più basso |

**Onestà su A5 «Smart Tube» (16 lezioni):** insegna a fare tutto da telefono. La nostra
fabbrica è un motore Python su PC: quasi nulla si trasferisce. Le studio in BRONZO per non
perdere le idee di metodo (nicchie, ottimizzazione canale) e **non fingerò** miglioramenti
tecnici che non esistono.

---

# PARTE V — PARTENZA, RISCHI, PROVE

## 11. Passo zero — tre cose, prima di qualunque lezione

| # | Cosa | Fatto quando | Costo |
|---|---|---|---|
| 0.1 | **`BASELINE.md`** — la fabbrica fotografata | tutte le metriche di §7 scritte, test rieseguiti davvero | ~15 min |
| 0.2 | **Trascrittore** installato e collaudato su 1 lezione | `parlato.txt` leggibile e coerente col video | ~20 min |
| 0.3 | **Prova completa su UNA lezione** (A4-L01) | i 7 passi chiusi, 1 regola a schema, gate simulato | ~30 min |

**Se i sette passi reggono su una lezione, reggono su 167. Se non reggono, l'ho scoperto al
primo video e non al centesimo.** Solo dopo questi tre, e col tuo via, parte lo studio.

## 12. Pre-mortem — è il giorno dopo, il piano è fallito. Perché?

| Causa | Prob. | Disinnesco |
|---|---|---|
| Il gettone scade a metà scaricamento | alta | una lezione per volta, gettone catturato subito prima; se scade, riapro e ricatturo. Mai code lunghe |
| Trascrizione lenta o inaffidabile | media | collaudata al passo 0.2 su lezione vera; se la macchina non regge scendo di modello **e lo dichiaro** |
| **Il contesto della chat finisce a metà corso** | **certa** | checkpoint `EMP-XXXX` a **ogni** categoria chiusa: la chat nuova riparte esatta, con trappole e decisioni già prese |
| Le modifiche rompono la fabbrica | media | binario B + test verdi + video di prova prima del commit |
| **Studio tutto e non cambia niente** | media | ogni regola ha `misura:`; a fine categoria conto le regole applicate. Zero = categoria fallita, scritto |
| Regole in conflitto fra due lezioni | media | `CONFLITTI.md` con arbitrato scritto; l'ultima lezione non vince per anzianità |
| Disco pieno | media | 360p, video **cancellato dopo l'estrazione**, restano solo i frame scelti |
| Io mi convinco che una cosa vista male sia oro | media | §6.4 (schermo batte parlato) + scagnozzo di verifica a campione (§5) |

## 13. Le decisioni che questo piano prende (ADR da emettere al via)

| ADR | Decisione |
|---|---|
| **ADR-022** | Nasce `corso-lab`: ingest per piattaforme a login con flusso protetto, **affiancato** a `yt_ingest.py`, mai sostitutivo (ADR-003) |
| **ADR-023** | Le conoscenze da corso entrano nella fabbrica **solo** come regole a contratto (§6.3). Niente prosa applicata a mano |
| **ADR-024** | Doppio binario A/B (§8): il motore in produzione si tocca solo a gate di categoria superato |

## 14. L'obiezione più forte contro questo piano — e cosa rispondo

> *«Stai per spendere settimane su un corso mentre l'azienda ha 25 pezzi finiti mai
> pubblicati (ADR-016) e non misura un euro. Il collo di bottiglia non è sapere: è
> pubblicare. Questo piano è colto e inutile.»*

**È l'obiezione giusta, e non la addolcisco.** Tre risposte, e sono verificabili:

1. **L'ordine di attacco è costruito su quell'obiezione**: le prime due categorie (A4, A6)
   sono produzione, copertine, CTR e pubblicazione — esattamente il collo di bottiglia.
   Non ho messo per prime le lezioni più interessanti: ho messo quelle che sbloccano.
2. **La baseline (§7) rende il fallimento visibile.** Se dopo A4 e A6 la fabbrica non
   pubblica più e meglio di oggi, il piano ha fallito la prova e **si ferma** — invece di
   proseguire per inerzia fino alla lezione 167.
3. **Il costo è recuperabile, l'ignoranza no**: le prime due categorie sono 34 lezioni su
   167, cioè il 20% dello sforzo, e producono la parte di conoscenza che tocca i soldi.

**Punto di uscita dichiarato:** chiuse A4 e A6, ti porto i numeri del §7 a confronto con la
baseline. Se non si sono mossi, **sono io a proporti di fermare il piano.**

---

# PARTE VI — IL PEZZO FINALE (ordine di Max, 2026-09-05)

## 16. `IL METODO YOUTUBE AUTOMATION` — l'opera che chiude la missione

Alla fine dello studio — **non prima**, non a rate — si consegna **un documento ufficiale e
pubblico** che contiene **tutta** la formazione e la conoscenza del corso, organizzata. Non è
un riassunto del corso: è **il corpus**, ordinato meglio dell'originale.

**Tre formati obbligatori, stesso contenuto, un solo sorgente:**

| Formato | File | A cosa serve |
|---|---|---|
| **Markdown** | `IL-METODO-YOUTUBE-AUTOMATION.md` | la fonte di verità, versionata in git |
| **Python** | `il_metodo_youtube_automation.py` | il metodo **interrogabile dalla macchina**: fasi, regole, soglie, checklist come strutture dati che agenti e script possono leggere (stessa forma dei file in `regole/`) |
| **PDF** | `IL-METODO-YOUTUBE-AUTOMATION.pdf` | il documento da leggere e da consegnare — **standard-oro dossier 28** (`emperator.md` §6.19), costruito col motore `PIANO-MAESTRO/scripts/pdf_engine_empire.py` (classe `PDFDoc`) |

**Il PDF ha due case, non una** (legge §6.17, CP-20260905-012/013): resta nella sua casa
canonica `company/Memory/studi/aitubepro/` **e** riceve un doppione identico in
`documentazione Empire/Piani/YouTube Automation Factory/`. Il doppione si copia, non si sposta,
e si riallinea ad **ogni** rigenerazione: un doppione vecchio è peggio di nessun doppione.
Qualità non negoziabile: quel PDF sta accanto al dossier 28 e agli altri, e deve reggere il
confronto — impaginazione, grana, colori, tipografia dello standard, mai un PDF "di servizio".

**Struttura del documento — in quest'ordine, non negoziabile:**

1. **Parte finanziaria** — il modello di business per intero: da dove vengono i soldi, quanto
   costa produrre, i numeri dichiarati nel corso, quelli veri nostri, e il confronto fra i due.
2. **Sintesi** — tutte le fasi in forma stretta: il quadro completo che si legge in una volta.
3. **Parte estesa** — tutto il resto, senza tagli: ogni regola primaria, ogni fase con la sua
   procedura, **tutti i metodi** e poi **il metodo migliore** (dichiarato, motivato, scelto),
   tutta la SEO, tutta la ricerca (nicchie, argomenti, parole chiave), tutte le analisi
   (metriche, retention, CTR, performance), l'intero apparato di formazione e conoscenza.

**Regole di costruzione:**

- **Si costruisce dai materiali già prodotti**, non a memoria: gli `appunti.md`, i `report.md`,
  i `REPORT-CATEGORIA.md` e il registro delle regole sono le fonti. Ogni affermazione del
  documento è **tracciabile** a una lezione e a un minuto.
- **Zero riassunti al posto della conoscenza**: dove il corso spiega una procedura in dieci
  passi, il documento ha dieci passi. La sintesi sta nella §2, e solo lì.
- **Il metodo migliore va dichiarato**: fra più metodi che il corso presenta, il documento dice
  quale vince, perché, e a quali condizioni cade.
- **Ciò che il corso sbaglia o che è invecchiato resta scritto**, marcato come tale: un corpus
  che nasconde i punti deboli non è un corpus, è una brochure.
- **Costruzione a nastro, non in un colpo**: il documento si assembla dalle parti di categoria
  già chiuse — a ogni categoria chiusa la sua sezione è già scrivibile. L'ultima categoria
  chiusa fa scattare l'assemblaggio finale, la parte finanziaria e la sintesi.

**Criterio di uscita — cinque condizioni, tutte verificabili:**

1. I tre file esistono e dicono la stessa cosa (nessuna divergenza fra `.md`, `.py` e PDF).
2. Ogni sezione della parte estesa **cita la lezione e il minuto** da cui viene.
3. Il PDF è costruito col motore `pdf_engine_empire.py` e regge il confronto col dossier 28.
4. Il **doppione** è in `documentazione Empire/Piani/YouTube Automation Factory/` e ha lo
   stesso identico contenuto della copia canonica (stessa data di build).
5. Il PDF viene **aperto davanti a Max**, non solo consegnato come percorso.

Finché manca uno dei cinque, **la missione non è chiusa**.

---

## 15. Cosa è cambiato nei giri

| Giro | Difetto trovato | Correzione |
|---|---|---|
| v1 → v2 | 167 lezioni tutte uguali; motore in produzione toccato a ogni lezione | tre profondità (§10) + due binari (§8) |
| v2 → v3 | davo per scontato di poter scaricare i video; non sapevo la durata del corso | vincoli tecnici accertati (§2) + passo zero (§11) |
| v3 → v4 | *«migliorare il workflow»* non era misurabile: nessuno avrebbe potuto dire se stavo migliorando qualcosa | **baseline (§7)**, `misura:` obbligatoria in ogni regola (§6.3), **gate a 7 condizioni** (§9), punto di uscita dichiarato (§14) |
| v3 → v4 | le regole erano prosa: 167 documenti morti | **contratto formale** (§6.3) + `registro.py` che le interroga |
| v3 → v4 | nessuna difesa contro «ho visto male» o «il corso contraddice noi» | schermo batte parlato (§6.4), `CONFLITTI.md` con arbitrato, scagnozzo di verifica a campione (§5) |
