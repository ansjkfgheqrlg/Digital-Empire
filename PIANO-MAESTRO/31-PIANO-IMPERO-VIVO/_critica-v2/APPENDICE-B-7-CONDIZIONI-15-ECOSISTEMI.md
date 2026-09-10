# Appendice B — le 8 condizioni sui 15 ecosistemi

Sentinella indipendente (opus), 2026-09-10 — ricognizione in sola lettura

---

## Cosa è stato fatto, e come

Chiusura di **V3 §7**: le otto condizioni di V2 §4.1 (VIVO: V-a..V-d) e §4.2 (COLLEGATO:
C-a..C-d) sono state provate **una per una sui 15 ecosistemi** di `company/Ecosistemi/`, perché
`empire vivo --json` non deve pubblicare uno stato mai valutato per 15 nodi su 54.

**Le otto condizioni** (testo di V2 §4.1-4.2, non riformulato):

| | Condizione | Come si prova |
|---|---|---|
| V-a | si invoca con un comando dichiarato | il comando esiste ed esce 0 |
| V-b | produce un'uscita conforme a un contratto scritto | l'uscita valida contro lo schema |
| V-c | l'uscita finisce in un posto stabilito | il percorso è dichiarato e il file c'è |
| V-d | un test lo prova, ed è rilanciabile | il test esiste ed è verde |
| C-a | un ingresso dichiarato | il contratto in ingresso esiste |
| C-b | un'uscita dichiarata verso un destinatario che esiste come casella | il contratto nomina il destinatario **e la sua cartella/coda esiste su disco** |
| C-c | la traccia nasce da sola nel formato unico e nel registro dell'Impero | `trace stato --origine hook` la vede |
| C-d | ha servito un consumatore reale almeno una volta | esiste il fatto: file consegnato, lead passato di stato, euro incassato |

**Metodo** (L7 — si scrive ciò che si è misurato):
- Fonti primarie: `Read`/`Grep`/`Glob` su `company/Ecosistemi/<NN>-<nome>/`, `ECOSISTEMA.md`,
  `BACKBONE.md`, `NAMESPACE.md`, il codice dei motori fuori da `company/`, e
  `dati/censimento-01a-ecosistemi.md` (rilevazione del 2026-09-06, 1.256 righe).
- Comandi lanciati: **solo in sola lettura** (`ls`, `find`, `grep -c`, `test -f`). Nessun comando
  che scrive, invia, committa o spende.
- **Nessun test è stato eseguito.** Dove V-d dice PASSA, la prova è *l'esistenza del file di test
  più il verde già registrato da una fonte citata*; dove il verde non è documentato, l'esito è
  NON VALUTATO e lo dichiara la colonna Prova. Un test che esiste ma non è mai stato visto verde
  **non è un PASSA** (V2 §4.1: «il test esiste **ed è verde**»).
- **PASSA** = prova trovata. **NON PASSA** = verificato e manca. **NON VALUTATO** = non
  verificabile con certezza in tempo ragionevole, e il perché è scritto.

**Perimetro:** le 15 cartelle-ecosistema censite in `censimento-01a-ecosistemi.md`. Nota di
perimetro: sul disco oggi le cartelle sono **16** (`ls company/Ecosistemi/` → 16 + `REGISTRO-NUMERI.md`),
perché `15-LANCI` è nata **dopo** il censimento del 06/09 (ADR-025, 08/09). Le 15 schede qui
sotto seguono il censimento; `15-LANCI` è aggiunta come **scheda 16 fuori quota** in coda, per L1
(niente si scarta) e per non falsare il totale di 120 = 15×8 che V3 §7 si aspetta.

---

## Due verdetti trasversali, misurati una volta e validi per tutti

Prima delle schede, due fatti che decidono la stessa condizione su ogni nodo. Si dichiarano qui
per non ripeterne la prova quindici volte.

### C-c — NON PASSA su tutti e 15, e la ragione non è «non l'abbiamo ancora fatto»

C-c chiede che *«la traccia nasca da sola nel formato unico e nel registro dell'Impero»*, provato
da `trace stato --origine hook`. Misurato:

1. **Il comando non esiste.** `empire` ha esattamente 7 sottocomandi
   (`empire/cli.py:118-147`): `status`, `paths`, `links`, `art8`, `adr001`, `conform`, `doctor`.
   Non c'è `trace`, non c'è `stato`.
2. **Il campo non esiste.** `empire/trace.py` definisce `@dataclass Traccia` con
   `tipo · titolo · autore · prova · quando · contesto · tags · id`. **Non c'è `origine`**
   (`grep -rn "origine" empire/*.py empire/*/*.py` → nessuna occorrenza in `trace.py`), quindi
   nessuna traccia può essere marcata come nata da un hook nemmeno volendo.
3. **Il registro è fermo.** `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/`: **25 tracce in tutto**
   (6 `decisions` · 6 `errors` · 7 `performances` · 4 `reasoning-bank` · 2 `sessions`), tutte con
   `"autore": "Claude"`, tutte datate **24-29 luglio 2026**, **nessuna riferita a un ecosistema**.

Non è quindi un «non valutato»: la condizione è verificata e manca, su tutti e quindici. È il
numero da cui V2 §5 causa 1 parte (*«25 tracce in tutta la vita»*), confermato oggi identico.

### C-b — la casella dei destinatari non esiste in `company/`

`find company -type d \( -name inbox -o -name outbox -o -name archive \)` → **0 risultati**. Le
uniche cartelle `handoffs/` di tutto `company/` sono cinque:
`company/01-agency/A{1,2,3,4}-*/handoffs/` (che contengono **4 contratti**, non istanze) e
`company/Backbone/Bus/handoffs/`, che contiene **solo `.gitkeep`** — coda esistente e mai usata.
`company/runtime/` e `company/metrics/` **non esistono** (verificato: `ls` → nessuna voce), come
già scriveva V2 §5 causa 2.

Conseguenza: ogni nodo che dichiara un'uscita verso un altro ecosistema la dichiara **verso una
casella che non c'è**. C-b è NON PASSA ovunque, con una sola eccezione discussa nella scheda 15.

### Nota di metodo su C-d — quando è NON VALUTATO e non NON PASSA

C-d chiede *«ha servito un consumatore reale almeno una volta»*, con esempi tutti rivolti
**all'esterno** (file consegnato, lead passato di stato, euro incassato). Dove il mestiere
dell'ecosistema è svolto ogni giorno ma **il consumatore sarebbe interno** (l'Impero che consuma
le proprie skill, la propria wiki) o dove **manca il registro che attribuisca il fatto al nodo**,
l'esito è **NON VALUTATO**, non NON PASSA: l'assenza di registro non è prova di assenza del fatto.
Dove invece un registro misurato dice che il pezzo *non* è mai uscito
(`company/Memory/ULTIMO-METRO.md`, rigenerato da `scripts/ultimo_metro.py`), l'esito è NON PASSA.

---

<!-- SCHEDE -->

## 01-AGENCY

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | `find company/Ecosistemi/01-AGENCY \( -name "*.py" -o -name "*.bat" -o -name "*.sh" -o -name "*.js" \)` → **0**. Il solo «punto d'ingresso ufficiale» è prosa (`Workflow/outreach-wrapper.md`) e rimanda a `Outreach/AVVIA-EMAIL-LIVE.bat` (verificato presente, con altri 5 `.bat`): comando di un motore esterno che non legge un solo file del nodo. |
| V-b | **NON PASSA** | I contratti `HC-AG-IB-01`…`HC-AG-OP-01` (`BACKBONE.md` §3, 8 righe di tabella) sono prosa. L'unico schema eseguibile del repo è `company/Backbone/Bus/contracts/HC-template.json` (`"_schema": "empire-handoff-contract-v1"`), fuori dal nodo, e nessuna uscita di 01 gli è validata contro. |
| V-c | **NON PASSA** | `NAMESPACE.md` fissa `agency/a1..a10` su AgentDB: nessun file del nodo vi scrive. `Reparti/A1-Ricerca/state/` contiene **un solo file, `README.md`** (`find … -type f` → 1); idem gli altri 9 reparti. |
| V-d | **NON PASSA** | 0 file di test nel nodo (`find … -name "test_*"` → 0). I 7 «DONE WHEN» di `ECOSISTEMA.md` §2 sono verifiche a occhio. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli ingressi, e — **unico caso del perimetro** — esistono 4 contratti come file JSON veri: `company/01-agency/A1-RICERCA/handoffs/HC-A1-A2-leads.json` (`"_schema": "HC-v1"`, `_created: 2026-06-11`), più `HC-A2-A3-call.json`, `HC-A3-A4-contratto.json`, `HC-A4-A6-testimonianza.json`. |
| C-b | **NON PASSA** | Il contratto nomina 8 destinatari; `BACKBONE.md` §3 consegna in `handoffs/{inbox,outbox,archive}/` «create in fase B2» — **mai create** (verdetto trasversale). E la coda dei 4 contratti veri, `"queue": "leads_ready"`, non esiste come cartella: `find . -type d -name leads_ready` → **0**. |
| C-c | **NON PASSA** | Verdetto trasversale: comando, campo e registro assenti. |
| C-d | **PASSA** | `EmpireDesk/state/preventa_leads.json` (1.313.918 byte, 31/08): **22 occorrenze di `CONTACTED`** = 22 lead passati di stato con messaggio realmente inviato. *Il fatto esiste ma è del motore Preventa fuori dal nodo, e il nodo non lo registra da nessuna parte.* |

**4 NON PASSA su 4 in VIVO · 1 PASSA su 4 in COLLEGATO.** L'ecosistema col motore più grosso
dell'Impero (313 `.py` in `Outreach/`) è, come nodo, 209 file di prosa.

---

## 02-INFO-BUSINESS

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 567 eseguibili nel nodo, ma **tutti dentro un solo workflow**: `Workflow/libri-performanti-multiagente/`. Lì il comando esiste (`AVVIA-LOGIN-SESSIONI.bat` presente; `engine/book_project.py`, `engine/kdp.py`, `engine/niche_finder.py` con `argparse`). Per gli **altri 5 workflow** (`WF-CORSO`, `WF-LANCIO`, `WF-FUNNEL-EVERGREEN`, `WF-VALIDAZIONE`, `WF-EBOOK`) e per le 57 schede agente **non esiste nessun eseguibile**, e non esiste un comando d'ecosistema. *Non rilanciato: `session_manager` esegue un login Amazon/LM Arena, fuori dalla sola lettura.* |
| V-b | **NON PASSA** | Contratto eseguibile solo per i libri (`engine/gate_blocco.py`, `validators.py`, `story_validator.py` escono con codice d'errore). Per gli altri 5 workflow il «contratto» è una tabella in prosa. |
| V-c | **NON PASSA** | Per i libri la destinazione è dichiarata e **piena**: `LIBRI/libri_pronti/` contiene 7 titoli (`Proof_of_Murder`, `The_Coven_of_Lost_Ember`, `The_Midnight_Ledger`, `The_Ninth_Winter`, `The_Quiet_Hours`, `The_Second-Hand_Spellbook`, `The_Winter_Term`). Per corso/lancio/funnel **non esiste alcuna cartella di destinazione nel nodo**. |
| V-d | **NON PASSA** | 4 test veri, e solo per i libri: `tests/test_auto.py`, `test_flusso_manuale.py`, `test_kdp.py`, `test_qualita_pacchetto.py`. Zero test per i 5 reparti e per gli altri workflow. **Non eseguiti, e nessun verde documentato**: anche per il ramo libri V-d non arriverebbe a PASSA (V2 §4.1 esige «esiste **ed è verde**»). |
| C-a | **PASSA** | `BACKBONE.md` §BUS: *«Inbound (riceve): upsell lead ← AGENCY; copy finita ← MARKETING; contenuti ← CONTENT-FACTORY»*, con il contratto standard in JSON inline. Contratto sottile (`"payload": {}`) ma dichiarato. |
| C-b | **NON PASSA** | Verdetto trasversale: nessuna casella su disco per i destinatari nominati. |
| C-c | **NON PASSA** | Verdetto trasversale. Nota: `LIBRI/chiamate.jsonl` è una traccia privata del motore, non nel formato unico né nel registro. |
| C-d | **NON PASSA** | **Misurato, non dedotto:** `LIBRI/libri_pubblicati/` è **vuota** (`ls` → nessuna voce), e `company/Memory/ULTIMO-METRO.md` (rigenerato da `scripts/ultimo_metro.py` il 03/09) elenca `The_Winter_Term`, `The_Ninth_Winter`, `The_Quiet_Hours` fra i 25 pezzi finiti e mai usciti. 7 libri pronti, **zero consumatori reali**. |

**È l'ULTIMO METRO (ADR-016) misurato dentro un ecosistema:** il solo nodo non-APEX con un motore
proprio che produce davvero, e la sua uscita si ferma un metro prima del lettore.

---

## 03-CONTENT-FACTORY

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili nel nodo (verificato). Il comando reale esiste ed è preciso — `python "SKILL & Agenti/Workflow agency creative/caroselli.py" "<argomento>" --slide 6` (file verificato: 21.052 byte, 31/08) — ma nel nodo compare **solo dentro `orders/CF-2026-PREVENTA-002/state.json`, come consuntivo**, mai come scheda di comando. |
| V-b | **NON PASSA** | `ECOSISTEMA.md` DONE WHEN #1 esige `{committente, brand_kit, icp, formato, quantità, deadline, budget}`: l'ordine 001 ha `"brand_kit_path": null`. **Nessuno schema valida l'ordine** — è lo stesso «contratto auto-invalidante» di V2 §5 causa 4. |
| V-c | **NON PASSA** | `orders/` esiste **in 1 reparto su 9** — ed è l'unico `orders/` di tutto `company/` (`find company -type d -name orders` → 1 risultato). CF-R3-Produzione-Video, che ha il motore più grosso (`YOUTUBE-AUTOMATION-FACTORY/`, 136 `.py`), ha **zero ordini**; CF-R7-Pubblicazione zero. |
| V-d | **NON PASSA** | 0 test nel nodo. Le prove sono 2 `state.json` scritti a mano dopo il fatto. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli inbound e `ECOSISTEMA.md` DONE WHEN #1 fissa il contratto d'ordine a 7 campi. Dichiarato (per quanto non applicato: vedi V-b). |
| C-b | **NON PASSA** | Entrambi gli ordini registrano `"handoff-cf-r6": "non_eseguito" — CF-R6-QA-Gate non ancora costruito come reparto operativo`, e il 002 aggiunge che «la pubblicazione non è agganciata». Destinatario nominato, casella inesistente. |
| C-c | **NON PASSA** | Esiste `orders/CF-2026-PREVENTA-001/trace.jsonl` — ma è **una traccia privata dell'ordine**, scritta a mano dopo il fatto, fuori dal formato unico e assente dalle 25 tracce del registro. È esattamente il caso che V2 §4.2 cita per stringere C-c («qualunque motore con un log privato passava»). |
| C-d | **PASSA** | 3 consegne reali su disco in `SKILL & Agenti/Workflow agency creative/Arsenale Caroselli/Preventa/`: `2026-08-06_tempo-perso-import`, `2026-08-27_quanto-tempo-perdi-a-fare-un-preventivo`, `2026-08-27_tradurre-a-mano-un-annuncio-tedesco-e-ri`. Un ordine reale ha percorso brief → copy → render → gate automatico → consegna. |

---

## 04-MARKETING

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili nel nodo (159/159 `.md`). La skill `.claude/skills/copy-workflow/` **esiste** (verificata: `SKILL.md`, `README.md`, `agents/`) ma si invoca solo da un umano in chat: non è un comando che esca 0, e nessun altro ecosistema può chiamare MARKETING. |
| V-b | **NON PASSA** | `ECOSISTEMA.md` fissa 4 gate numerici (APSOC ≥80, sales page ≥85, brand gate binario, «−15 se P prima di S»): **nessuna funzione li calcola** — né nel nodo, né nei 189 file del motore esterno `SKILL & Agenti/Copy-Workflow-manuale/`, che contiene **0 `.py`**. È un giudizio a mano, senza registro. |
| V-c | **NON PASSA** | Nessuna cartella `orders/`, `output/` o `state/` popolata: `Reparti/*/state/` contiene solo prosa. A differenza di 03, qui **non esiste nemmeno un ordine tracciato**. |
| V-d | **NON PASSA** | 0 test nel nodo; `evals/` esiste nel motore esterno e non è agganciata a nulla. |
| C-a | **PASSA** | `BACKBONE.md` §BUS dichiara gli inbound (brief ← AGENCY / INFO-BUSINESS) con il contratto standard inline. |
| C-b | **NON PASSA** | Verdetto trasversale. |
| C-c | **NON PASSA** | Verdetto trasversale. |
| C-d | **NON VALUTATO** | Il copy prodotto da `copy-workflow` è quasi certamente finito in materiali reali dell'Impero, ma **non esiste su disco un registro che leghi un pezzo di copy consegnato a questo ecosistema**: zero `orders/`, zero `state/` popolato, nessun log. Non posso né provarlo né escluderlo. *Non valutato: manca il registro, non necessariamente il fatto.* |

---

## 05-MULTI-BUSINESS

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili (40/40 `.md`), nessuna skill registrata col nome dell'ecosistema, nessun runner per i 15 workflow. Il motore YouTube **esiste** (`YOUTUBE-AUTOMATION-FACTORY/`, 136 `.py`) ma il nodo **non sa che esiste**: `grep -r "YOUTUBE-AUTOMATION-FACTORY" company/Ecosistemi/05-MULTI-BUSINESS/` → **0 occorrenze** (censimento 01a, riverificato come dato di fonte). |
| V-b | **NON PASSA** | I 4 QA gate bloccanti di `ECOSISTEMA.md` §3.1 (script, audio, visual, SEO) non sono implementati né registrati da nessun file del nodo. |
| V-c | **NON PASSA** | Zero `orders/`, zero `state/`, zero `output/` nel nodo. Le uscite reali (video pronti, libri) finiscono in cartelle esterne che il nodo non nomina. |
| V-d | **NON PASSA** | 0 test. I DONE WHEN #3 e #4 («≥1 video che ha superato tutti e 4 i gate», «pipeline libro eseguita end-to-end») non hanno registro che li possa provare. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli inbound col contratto standard inline. |
| C-b | **NON PASSA** | Verdetto trasversale. |
| C-c | **NON PASSA** | Verdetto trasversale. |
| C-d | **NON PASSA** | **Misurato su tutti e tre i rami.** *YouTube:* `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/` contiene **8 cartelle `video-NN`** (`video-01` ha `video.mp4` + `copy.md` + copertina), e `company/Memory/ULTIMO-METRO.md` elenca `video-01`, `video-02`, `video-03` fra i **25 pezzi finiti e mai usciti** (il più vecchio fermo da 135 giorni, 2.137 MB totali). *Publishing:* i libri sono in 02 e `libri_pubblicati/` è vuota. *E-commerce:* nessun motore, dichiarato OUT OF SCOPE dallo stesso `ECOSISTEMA.md`. |

---

## 06-PLATFORM

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili nel nodo (27/27 `.md`). I comandi che farebbero il suo mestiere esistono e sono stati verificati alla radice — `scripts/verify-empire.ps1`, `verify-agents.py`, `verify-skills.py`, `empire-sync.ps1`, `gen-empire.py` (20 voci in `scripts/`) — ma **nessuna delle 27 pagine li dichiara come path eseguibile**: «verify-empire» compare nella prosa del reparto CI/CD, mai come comando. |
| V-b | **NON PASSA** | I 4 «siti attivi» sono elencati per solo URL (`ECOSISTEMA.md` §Siti attivi, riga 21-28): nessun formato di consegna, nessun manifest di build, nessuna regola su cosa contenga un sito finito. |
| V-c | **NON PASSA** | Zero `state/`, zero `orders/`, zero log di deploy nel nodo. Il namespace `platform/*` è dichiarato in `BACKBONE.md` e **non scritto da niente**. |
| V-d | **NON PASSA** | 0 test nel nodo, benché `scripts/verify-*.py|ps1` esistano già e potrebbero esserne la base immediata. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli inbound (feature request ← AGENCY via `HC-AG-PL-01`, che il lato 01 nomina esplicitamente). |
| C-b | **NON PASSA** | Verdetto trasversale. |
| C-c | **NON PASSA** | Verdetto trasversale. |
| C-d | **NON VALUTATO** | `ECOSISTEMA.md` righe 25-28 dichiara 3 siti live (`presentazione-empire.vercel.app`, `agency-empire-kohl.vercel.app`, `preventivo-exponium.vercel.app`) più una dashboard locale. **Verificarli richiede rete, fuori dal perimetro di sola lettura di questa ricognizione**; su disco esistono i sorgenti (`Crea siti/` 399 file, `agency-empire-landing/`), ma nessun registro di consegna lega un sito a questo nodo. *Non valutato: una tabella che dichiara «attivo» è un'affermazione, non una misura (L7).* |

---

## 07-FORGE

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili nel nodo (34/34 `.md`). Il mestiere è svolto da skill che si invocano **direttamente**, mai passando da 07. *Correzione a una fonte:* il censimento 01a dà `.claude/skills/skill-creator/` come presente — sul disco **non c'è** (`find .claude/skills -maxdepth 1 -name "skill*"` → solo `skill-builder`, `skill-contradiction-analyzer`); `skill-creator` è **globale**, in `C:/Users/Utente/.claude/skills/skill-creator` (verificato). |
| V-b | **NON PASSA** | `frg-contradiction-gate.md` e `frg-eval-runner.md` sono gate senza esecutore: il controllo reale (`scripts/verify-skills.py`, `scripts/peso_skill.py`, verificati presenti) vive altrove e **non è agganciato al gate**. |
| V-c | **NON PASSA** | `frg-hr-registrar.md` descrive un registro anagrafico degli agenti creati: **quel registro non esiste come file** nel nodo. Zero `state/`, zero `orders/`. |
| V-d | **NON PASSA** | 0 test e nessuna eval agganciata, benché `T-eval-runner.md` e `WF-SKILL-AUDIT.md` la presuppongano. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli inbound, e il contratto `HC-AG-FG-01` («richiesta organico: gap funzionale documentato + KPI che lo dimostra») è scritto per esteso dal lato mittente in `01-AGENCY/BACKBONE.md` §3. |
| C-b | **NON PASSA** | Verdetto trasversale. |
| C-c | **NON PASSA** | Verdetto trasversale. |
| C-d | **NON VALUTATO** | Le forgiature avvengono davvero — il catalogo skill del repo ne è la prova materiale — ma **nessun registro lega una forgiatura a questo nodo** (vedi V-c) e **il consumatore sarebbe interno**: C-d nomina «file consegnato, lead passato di stato, euro incassato», tutti esterni, e non dichiara se un consumatore interno valga. Doppia ambiguità → non valutato. *È una domanda che V4 deve chiudere per definizione, non per misura.* |

---

## 08-INTELLIGENCE

> ⚠️ Il numero **08 è occupato due volte** (`08-INTELLIGENCE` e `08-STREAM-S7-BOT`): collisione
> registrata e non risolta in `company/Ecosistemi/REGISTRO-NUMERI.md`. Da sanare prima di qualunque
> automazione che indirizzi gli ecosistemi per numero — `empire vivo --json` è esattamente una di quelle.

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili nel nodo (16/16 `.md`). Si invocano direttamente `memory-empire`, `wiki-context`, `sync-wiki-totale`, `nerve-solve` (skill verificate presenti); le 4 schede agente del nodo non sono registrate come invocabili da nessuna parte. |
| V-b | **NON PASSA** | Lo standard «ogni operazione logga in `second-brain-vault/wiki/log.md`» è un obbligo scritto nel `CLAUDE.md` di progetto, **non un controllo del nodo**: nessun file di 08 verifica che sia stato rispettato. |
| V-c | **PASSA** | **L'unico PASSA di V-c fra i dieci nodi di sola prosa.** `ECOSISTEMA.md` righe 22-31 dichiara i percorsi in tabella («Wiki second-brain → `second-brain-vault/wiki/`», «Wiki index → `…/index.md`», «Wiki log → `…/log.md`») e **i file ci sono**: `find second-brain-vault/wiki -type f` → **1.884 file**; `log.md` = 201.014 byte, modificato **oggi 2026-09-10 15:06**. Percorso dichiarato, uscita presente, aggiornata di recente. |
| V-d | **NON PASSA** | Nessun test, nessun controllo automatico di integrità della wiki (link morti, pagine orfane), benché `Workflow/wiki-wrapper.md` dichiari l'operazione «LINT». |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli inbound; `01-AGENCY/BACKBONE.md` nomina `HC-AG-IN-01` («dati campo: obiezioni reali, motivi di rifiuto… anonimizzati») come contratto verso questo nodo. |
| C-b | **NON PASSA** | Verdetto trasversale: i destinatari sono nominati, le caselle no. |
| C-c | **NON PASSA** | Verdetto trasversale. |
| C-d | **PASSA** | La wiki è consumata realmente e in modo obbligatorio: il `CLAUDE.md` di progetto ordina di leggerla **all'inizio di ogni sessione**, e `wiki/log.md` (201 KB, aggiornato oggi) è il registro delle operazioni servite. Il consumatore è interno, ma qui — a differenza di 07 — **il registro esiste e data i fatti**. |

---

## 08-STREAM-S7-BOT *(secondo occupante del numero 08)*

> Il nodo **senza documenti di governo**: `ECOSISTEMA.md` ASSENTE, `BACKBONE.md` ASSENTE, README
> ASSENTE (verificato: la cartella contiene **due sole voci**, `S7_NFT_BOT.zip` e `__pycache__/`).
> L'unico documento, `LEGGIMI.md`, è **dentro lo zip**.

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | Il comando è dichiarato con precisione dentro `LEGGIMI.md` (`cd company/Ecosistemi/08-STREAM-S7-BOT` → `pip install -r requirements.txt` → `python main.py`) e **fallisce da fermo**: `main.py` non esiste sul disco, è compresso; `ls` sulla cartella restituisce solo `S7_NFT_BOT.zip` e `__pycache__/`. Serve un `unzip` che il LEGGIMI non menziona. |
| V-b | **NON PASSA** | Il contratto d'uscita esiste ed è il più rigoroso del censimento (`LEGGIMI.md` esige «expectancy positiva su almeno 30 giorni di simulazione» prima di `TRADE_MODE=LIVE`), **e non è superato**: `paper_trade_log.csv` ha 6 righe di **un solo minuto** (23/07, 08:47-08:48), tutte BUY e **nessuna riga di chiusura** — l'expectancy non è calcolabile. |
| V-c | **NON PASSA** | La destinazione è stabilita (`paper_trade_log.csv` accanto al codice) ma **vive dentro lo zip**: ogni run futura scriverebbe in una cartella estratta non tracciata. Fuori dallo zip non c'è nessun file d'uscita. |
| V-d | **NON PASSA** | Nessun `test_*.py`, e `activate_kill_switch()` in `risk_manager.py` non ha alcuna prova che si attivi davvero. |
| C-a | **NON PASSA** | **Non esiste alcun contratto in ingresso**: senza `ECOSISTEMA.md` e senza `BACKBONE.md`, il nodo non dichiara né mittenti né formato. L'unico ingresso è un WebSocket esterno (`SOLANA_WSS_URL` in `.env.example`), che non è un contratto dell'Impero. |
| C-b | **NON PASSA** | Nessun destinatario dichiarato, quindi nessuna casella da verificare. |
| C-c | **NON PASSA** | Verdetto trasversale. Il nodo ha un log privato (`paper_trade_log.csv`), fuori dal formato unico e dal registro. |
| C-d | **NON PASSA** | 6 trade **simulati** (`_simulate_transaction` in `execution_engine.py`), zero reali, zero euro. Nessun consumatore. Il `__pycache__/` (4 `.pyc` del 23/07, 08:47-08:48) prova che il codice **è girato su questa macchina** — non che abbia servito qualcuno. |

**Il nodo dichiara da solo perché non ha consumatori**: `report-studio.md`, scritto dallo studio
stesso, conclude che l'edge del retail non esiste. **Rendere «vivo» questo nodo può voler dire
archiviarlo con onore, non collegarlo** — è una decisione di Max, non un lavoro tecnico.

---

## 09-OPERATIONS

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | 0 eseguibili nel nodo (32/32 `.md`). I comandi reali esistono come skill (`avvia-email`, `avvia-ig`, `avvia-parallel`, `avvia-scraper`, `avvia-linkedin`, `avvia-outreach-preventa`, `avvia-estate-wk`, tutte verificate in `.claude/skills/`) ma **non passano da OPERATIONS**: chi lancia una run non registra nulla qui. |
| V-b | **NON PASSA** | L'evento standard `{ecosistema, workflow, costo, durata, esito}` del DONE WHEN #1 **non esiste come formato in nessun file**: nessuno schema, nessun esempio compilato. |
| V-c | **NON PASSA** | Nessun posto dove finiscano le misure: zero `state/`, **nessun ledger in tutto il repo** (`find . -maxdepth 4 -iname "*ledger*"` → 0, dal censimento), nessuna dashboard. Il DONE WHEN #4 non ha alcun artefatto. |
| V-d | **NON PASSA** | 0 test. Fuori dal nodo esistono due hook eseguibili e attivi (`scripts/gate_battito_hook.py`, `scripts/verifica_recap.py`, verificati presenti): la prova che in questo repo un gate bloccante si sa scrivere — semplicemente non è stato scritto per OPERATIONS. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli inbound e `01-AGENCY/BACKBONE.md` scrive per esteso `HC-AG-OP-01` («job: nuovi job da schedulare… job idempotente, con kill-switch»). |
| C-b | **NON PASSA** | Verdetto trasversale. |
| C-c | **NON PASSA** | Verdetto trasversale — ed è il nodo che *dovrebbe* possedere quel registro. |
| C-d | **NON PASSA** | Il motore dichiarato **non esiste sul disco**: `find ruflo -type f` → **0 file** (cartella presente e completamente vuota, riverificato oggi), mentre `ECOSISTEMA.md` dichiara «ruflo installato»; il server MCP `claude-flow` non risponde nemmeno in questa sessione (timeout). Senza runtime, senza ledger e senza budget guard, **nessun consumatore può essere stato servito da questo nodo**. |

**8 NON PASSA su 7 condizioni misurabili + 1 PASSA (C-a).** È l'unico ecosistema il cui motore
dichiarato non esiste: qui non si collega, si costruisce da zero — e **ogni altro ecosistema
dipende da lui per essere misurato**, `empire vivo --json` incluso.

---

## 10-MEMORY

| | Esito | Prova |
|---|---|---|
| V-a | **NON PASSA** | Il comando esiste, è verificato ed è **usato ogni giorno** — `python scripts/checkpoint.py cp --titolo "..."` (`scripts/checkpoint.py`, 12.995 byte, 05/09), imposto dal `CLAUDE.md` di progetto («mai a mano e mai progressivo») — ma **nessuno dei 28 file del nodo lo cita come punto d'ingresso**. Il nodo non è invocabile: lo è il motore che gli sta accanto. |
| V-b | **NON PASSA** | Contratto d'uscita reale **solo per i checkpoint** (`company/Memory/templates/CP-template.md`, `ADR-template.md`, `session-template.md`, verificati). `WF-PRE-TASK-GATE.md` e `WF-AMNESIA-TEST.md` non hanno esecutore: il gate memory-first è applicato dalla disciplina in `CLAUDE.md`, non da un controllo. |
| V-c | **PASSA** | Destinazione stabilita **e rispettata, con la massima evidenza del perimetro**: `company/Memory/checkpoints/` → **358 voci** (erano 299 al censimento del 06/09: +59 in 4 giorni), `company/Memory/decisions/` → **32 ADR** (erano 25). Il percorso è dichiarato in `ECOSISTEMA.md` e nel `CLAUDE.md`, e i file ci sono. |
| V-d | **NON PASSA** | 0 test. `WF-AMNESIA-TEST.md` descrive la prova regina («una chat nuova riprende da dove eravamo?») e **non è mai stata resa eseguibile**. |
| C-a | **PASSA** | `BACKBONE.md` dichiara gli ingressi (2 righe di inbound, il valore più alto del perimetro) — è il nodo che riceve da tutti. |
| C-b | **NON PASSA** | Verdetto trasversale: i destinatari sono nominati, la casella `handoffs/{inbox,outbox,archive}` non esiste. |
| C-c | **NON PASSA** | Verdetto trasversale. Nota amara: **è l'ecosistema della memoria**, e le 25 tracce del registro dell'Impero sono ferme al 29 luglio mentre i suoi checkpoint sono 358 — due memorie parallele, una viva e una morta, e nessun collegamento fra loro. |
| C-d | **PASSA** | 358 checkpoint e 32 ADR consumati realmente e per legge interna: la REGOLA ZERO del `CLAUDE.md` obbliga ogni sessione a leggere `INDEX.md` + `STATO-EMPIRE.md` prima di qualsiasi task. Il fatto è datato, ripetuto e verificabile su disco. |

**3 PASSA su 8 — il punteggio più alto fra i dieci nodi di sola prosa**, e il solo che passa sia
V-c sia C-d. Ciò che manca è dichiarare *dentro il nodo* il comando che tutti già usano.

---
