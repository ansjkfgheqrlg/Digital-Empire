# 🜂 V3 — PIANO ASSESTATO: LE 13 CORREZIONI DI CRITICA 2

> **Versione:** 3 di 4 · **Data:** 2026-09-10 · **Autore:** EMPERATOR · **Committente:** Max
> **Base:** `V2-PIANO-AMPLIATO.md` (1.085 righe) — **non riscritta da zero**. Dove V2 regge, V3 la
> tiene identica e non la ripete qui: si legge V2 per il corpo, questo documento per le 13 correzioni.
> **Origine delle correzioni:** `_critica-v2/CRITICA-2-1-DOMANDE-EREDITA.md` (4 rilievi, 3 FATALI) +
> `_critica-v2/CRITICA-2-2-SCELTE-ARCHITETTURALI.md` (11 rilievi, 1 FATALE + 6 GRAVI + 4 MEDI, 2 reggono)
> **Verdetto della critica, riportato per intero:** nessuna delle cinque inversioni di V2 va invertita
> di nuovo. La direzione è giusta in tutti e cinque i casi, in entrambi i giudizi indipendenti. Il
> vizio è che V2 **ha scelto bene e specificato a metà**. V3 chiude le specifiche mancanti.
> **Ordine di Max che governa questo documento (2026-09-10):** *«finisci tutto facendo in modo che
> Gael possa lavorare sempre senza problemi»* — vale come lente su ogni riga sotto, non solo su §19.
> **Divieto ancora in vigore** (EMP-MCC4 §1): nessuna modifica costruttiva al repository. Questo è
> ancora un documento di piano. Le uniche scritture fuori da questa cartella sono lo stesso genere
> di ricognizione in sola lettura che ha prodotto i censimenti — dichiarate dove compaiono.

---

# PARTE 0 — MAPPA DELLE 13 CORREZIONI

| # | Rilievo | Grado | Cosa cambia in V3 | Sezione |
|---|---|---|---|---|
| 1 | Consumatore quotidiano: F1/F3 vietate dalla forma del battito | FATALE | LC si sdoppia (LC-vivo/LC-portata), riga di battito diventa deliverable esplicito di E4-F1 | §1 |
| 2 | Consumatore quotidiano: misura il rapporto, non il flusso servito | FATALE | stessa correzione del #1 — angolo diverso, stessa cura | §1 |
| 3 | Fusibile R5 scatta per costruzione: 23/26 pezzi senza prezzo | FATALE | E0 spaccato in E0a/E0b, nuovo E0.9 Atto di vendita, R5 riscritto | §2 |
| 4 | Nessuna legge di nascita per i nodi NUOVI (extra) | GRAVE | H13 + LC-1 promossa a legge di ogni artefatto nuovo + denominatore dinamico | §3 |
| 5 | A-1: innesto senza contratto d'innesto | GRAVE | contratto d'innesto in ogni scheda di nascita + F3 estratta in §22 | §4 |
| 6 | A-3: stato-prima-dell'invio crea il danno gemello (lead perso) | GRAVE | stato a due tempi SENDING→CONTACTED + riconciliazione umana + dry-run prima del vero | §5 |
| 7 | A-4: E0 usa gate che nascono dopo + merce senza venditore | GRAVE | stessa correzione del #3 (E0a/E0b) + riconciliazione con LANCI in §26 | §2 |
| 8 | A-5: «fonte di verità» è proprietà della coppia, non registrata | GRAVE | campo `fonte_di_verita` per coppia + guardia simmetrica + percentuali doppie | §6 |
| 9 | B-6: `empire vivo --json` nasce sopra dati mai valutati | GRAVE | tre esiti (PASSA/NON PASSA/NON VALUTATO) + lista 7×15 condizioni fatta ORA | §7 |
| 10 | **B-7: riconciliazione con Gael non negoziata — il più pericoloso** | GRAVE | **§19 riscritta per intero: i 3 carichi di Gael, nessuno lo blocca mai (ADR-028)** | **§8** |
| 11 | A-6: hook senza protocollo di deroga | MEDIO | `deroghe.jsonl` per hook, deroga puntuale firmata a scadenza | §9.1 |
| 12 | B-1/B-2/B-3: rimandi a costruzione invece che a ricognizione | MEDIO | destinazioni contate ORA, tetto provvisorio E6 + decisione gate APSOC, mappa 10 schemi letta ORA | §9.2-9.4 |
| — | B-4, B-5 | REGGE | nessun cambiamento | — |

---

# §1 — LA LEGGE CENTRALE SI SDOPPIA: LC-VIVO E LC-PORTATA

**Il difetto, nelle parole di entrambe le sentinelle.** La legge del consumatore quotidiano (V2 §1)
misura *l'età dell'ultimo rapporto*, non *l'età dell'ultimo fatto servito*. Un sistema morto che si
rapporta puntualmente passa il gate per sempre — è l'Ispettorato con un nome nuovo. E, per due delle
cinque funzioni, la riga che LC pretende dentro il battito **è oggi vietata dalla macchina che
sorveglia il battito**: `verifica_recap.py` rifiuta contenuto extra dopo la voce Potere (8º giro,
2026-09-09) — le sei voci sono chiuse per costruzione, non c'è una settima riga per F1/F3.

**La correzione — due leggi dove V2 ne aveva una:**

- **LC-vivo** (quello che V2 chiamava LC, invariato per le funzioni che non sono un flusso: F4, F5):
  il rapporto è fresco, gate a 24 ore, come in V2 §1.
- **LC-portata** (nuova, per le funzioni di classe *flusso*: F1, F2, F3): il gate legge il **delta
  di fatti serviti nella finestra**, non l'età del rapporto.
  - `bus eta --max-ore 24` → **`bus portata --min 1 --finestra 7g`** (un bus vuoto non passa più
    banalmente: deve aver smaltito almeno 1 evento in 7 giorni, non solo non avere code vecchie).
  - La riga di F1 nel battito, oggi impossibile per costruzione, **non si finge**: diventa un
    deliverable esplicito e quotato di E4-F1 (vedi §22 aggiornata, riga F1), che estende
    `verifica_recap.py` e `gate_battito_hook.py` per accettare una settima voce condizionale
    (`🟩 **Portata:** <n> archi percorsi / <m> sorvegliati`), validata a macchina come le altre sei.
    **Non si costruisce ora** (divieto in vigore): si scrive come lavoro nominato, con le sue ore,
    dentro E4 — non più una riga di scheda che nessun codice può eseguire.
  - **C-d per la classe flusso** si coniuga al presente: non *«ha servito un consumatore reale
    almeno una volta»* (V2 §4.2), ma **campo `ultimo_servito_il: <data>`**, aggiornato ogni volta
    che F1/F2/F3 passano un fatto vero. Un flusso che ha servito una volta a maggio e mai più non
    passa C-d in V3.

**Il corno dei falsi allarmi (segnalato dalla sentinella A-2 come giudizio, non misura, e qui
sciolto per decisione):** la finestra di LC-portata non è fissa a 24 ore per tutte le classi-flusso:
si tara sul **ritmo reale del business** dichiarato dal proprietario nella scheda di nascita (F3 su
Preventa: 24h nei giorni feriali, come il ciclo outreach; F1/F2 infrastrutturali: 7 giorni). Un
weekend o una pausa di Max non genera un falso rosso.

**Gate di §1 (sostituisce il gate implicito di V2):**
```
python -m empire bus portata --min 1 --finestra 7g         → exit 0 (dopo che F2 esiste, E4)
python -m empire trace stato --origine hook --finestra 24h → ≥ 1 (dopo che F3 esiste, E4)
python -m verifica_recap --schema                            → accetta la voce Portata condizionale
```

---

# §2 — E0 SI SPACCA IN E0a/E0b, NASCE E0.9 (L'ATTO DI VENDITA), R5 SI RISCRIVE

**Il difetto, sommato da tre rilievi (F-3, A-4, e il rischio R5 di V2 §24).** Tre fatti, tutti
misurati il 2026-09-10: (a) 23 dei 26 pezzi caricabili sono video senza prezzo per natura — i libri
(gli unici a prezzo) stanno in E8, non in E0; (b) i due Payment Link di E0 non hanno un prodotto
prezzato dietro — il prezzo del Manuale (B-002/B-003) è sparito fra V1 e V2, e la regola aziendale
vieta di deciderlo a mano; (c) E0 usa due gate (`gate_rotazione.py`, l'HTTP ai Payment Link) che
**nascono in E0.5**, cioè dopo E0 stesso. Conseguenza: il fusibile R5 (*«se dopo E3 `entrate.jsonl`
è 0 byte, il piano si ferma»*) scatterebbe **per costruzione**, non per un verdetto di mercato — e
scavalcarlo al primo scatto ucciderebbe la credibilità di ogni altro default del piano (§25-26).

**La correzione, in tre pezzi:**

**1. E0 si spacca in due, stesso giorno per chi può, giorni diversi per il rischio:**
- **E0a — LA MERCE** (giorno uno, nessun prerequisito, invariato da V2): i 2 Payment Link, il
  caricamento dei primi 5 pezzi. Rischio zero, non aspetta nessun gate che non esista ancora.
- **E0b — LA ROTAZIONE** (subito **dopo** E0.5, quando `gate_rotazione.py` e il gate INCASSO via
  HTTP esistono davvero): le 3 credenziali esposte. Si perde mezza giornata sulla sicurezza — le
  chiavi restano esposte qualche ora in più su un repo già pubblico da mesi — si guadagna la
  garanzia che il gate che dice «la vecchia chiave non risponde più» esista quando serve, invece
  di verificarsi «a mano e dichiararlo» (V2 §21-E0, la frase fra parentesi che L9/L5 vietano).
  Nel blocco gate di E0b: **ordine dei tre servizi esplicito** e **copertura obbligatoria per
  tutti e tre**, non un elenco di comandi senza sequenza (il buco che la sentinella A-4 ha trovato).

**2. Nasce E0.9 — L'ATTO DI VENDITA** (nuovo scaglione, 2-4 h, *chi: Max decide, EMPERATOR esegue*,
dopo E0.5, prima di E1):
- **Prezzo per decreto**: il Manuale a un prezzo dichiarato da Max ora, con la stessa forma dei
  default di §26 — *«il Manuale a X€ finché il team prezzi (B-003) non esiste; quando nascerà, lo
  rivede lui, non annulla la vendita nel frattempo»*. Non è una violazione della regola «non si
  decide a mano»: è la stessa figura retorica che §26 usa già per 7 decisioni più grosse (ADR-024,
  l'albero canonico, `cp_id`...) — un default reversibile, non una decisione definitiva.
- Il Payment Link di E0a si aggancia a quel prezzo (oggi non aggancia a niente).
- **Collegamento minimo video→prodotto**: un link nella descrizione dei 23 video, mentre escono in
  E0a/E8. Costo quasi zero (è testo), e trasforma il top-of-funnel in qualcosa che può — non deve —
  generare un euro.

**3. R5 si riscrive** (sostituisce V2 §24 R5): non più *«se `entrate.jsonl` è 0 byte dopo E3»*
(criterio aggirabile: una riga di *spesa* qualunque lo disinnesca senza un euro entrato — bug
trovato dalla sentinella, corretto qui) ma:
> **R5 — se dopo E3 non esistono ENTRAMBI (a) pezzi fuori ≥ soglia dichiarata E (b) almeno un
> canale di vendita apparecchiato (prodotto prezzato + Payment Link vivo + collegato a pezzi
> usciti), il piano si ferma e si riapre la domanda «cosa vendiamo, a chi».** L'euro incassato
> resta un esito di mercato che si misura e si riporta — non un gate del piano, perché il piano può
> costruire la capacità di vendere, non comprare la vendita stessa.

**Gate di §2:**
```
<E0a, invariato da V2>                                       → 2 Payment Link vivi, 5 pezzi caricati
python scripts/gate_rotazione.py                              → (E0b, dopo E0.5) vecchia chiave 401 su tutti e 3
curl <payment link base>                                      → risponde, prezzo = decreto di Max (E0.9)
grep -c "link prodotto" <23 video usciti>                    → tende a 23 durante E0a/E8
test -s company/Memory/tesoreria/entrate.jsonl \
  -o -f <prodotto prezzato + link vivo>                       → R5: almeno una delle due condizioni
```

---

# §3 — H13: LA LEGGE DI NASCITA VALE PER OGNI NODO NUOVO, NON SOLO PER QUELLI DI V2

**Il difetto (rilievo extra, sentinella 1).** LC-1 (*«la scheda di nascita di ogni pezzo di V2»*)
governa solo ciò che *il piano* costruisce. Il denominatore del 100% (V2 §3) è una lista congelata
al censimento del 6/9. Ma l'azienda continua a produrre nodi mentre il piano gira — misurato: il
magazzino è passato da 25 a 31 pezzi in 5 giorni (7→10/9), Preventa è nata ad agosto fuori da ogni
contatore. Il giorno in cui `empire vivo --json` stampa 100%, sarà vero solo della fotografia del
6/9: la stessa fabbrica di nodi (mai fermata, giustamente — L1) avrà ripopolato l'Impero di
descritto-non-vivo mentre il gate resta verde.

**La correzione:**

1. **LC-1 è promossa** da regola dei pezzi di V2 a **legge di ogni artefatto nuovo dell'Impero** —
   non scade con la chiusura del piano.
2. **H13 — la regola di nascita** (tredicesimo hook, si aggiunge a E0.7 insieme agli altri 12 di
   V2 §17): il pre-commit intercetta ogni file nuovo nelle classi censite (motore, agente, skill,
   organo, workflow) e pretende la scheda di nascita minima — la riga `Consumatore quotidiano` di
   LC-1 più l'ingresso in anagrafe — o **respinge**. Stesso costo di configurazione degli altri 12
   (righe in `.githooks/pre-commit`), stesso principio: sottoprodotto o hook che blocca (V1 §11,
   mai smentito).
3. **`nodi_censiti` (V2 §3) diventa una query dinamica sull'anagrafe** — *«tutti i nodi delle
   classi X registrati alla data del calcolo»* — non più la lista nominale del 6/9. Ogni nodo nuovo
   abbassa il numeratore finché non è vivo lui stesso, e `empire vivo --json` resta un termometro
   invece di diventare, con le parole della sentinella, *«una lapide commemorativa del giorno in
   cui si arrivò al 100%»*.

**Gate di §3:** `git commit` con un file nuovo in una classe censita, senza riga
`Consumatore quotidiano` → **RESPINTO** (H13, stesso schema di test degli altri 12: caso finto
contro lo scheletro vuoto, H4).

---

# §4 — IL CONTRATTO D'INNESTO (obbligatorio per le cinque funzioni)

**Il difetto (A-1).** L4 ha due metà — *«i motori restano dove sono»* e *«un sistema attivo non si
tocca finché il sostituto non è validato»* — e V2 applica solo la prima. I sei gate di E4 provano
la funzione nuova, mai l'ospite: un innesto che rompe `trace.py` passa tutti e sei. Il campo `costi`
obbligatorio in `checkpoint.py` (girato 303 volte, ogni sessione lo usa) non ha una finestra di
migrazione: il giorno dell'innesto, ogni sessione parallela che chiude un checkpoint col vecchio
formato fallisce senza sapere perché. E `trace.py` sta nei percorsi in scrittura di due scaglioni
(E3 ed E4) con l'ordine reale (F3 prima di E3) scritto solo in una nota, non nella tabella §22.

**La correzione — tre righe nuove nella scheda di nascita di V2 §10, per ognuna delle cinque
funzioni:**

```
FUNZIONE:               F<n> — <nome>            [le righe di V2, invariate]
INNESTO:                <file/cartella esistente>
POLITICA DI GUASTO:      fail-open | fail-closed  [NUOVA — vedi §5, criterio: danno peggiore]
GATE DI REGRESSIONE:     <comando di test già esistente dell'ospite>, rilanciato dopo l'innesto
PIANO DI RIENTRO:        <come si disinnesta in un commit se il gate di regressione fallisce>
MIGRAZIONE CHIAMANTI:    <se l'innesto cambia un contratto esistente (es. `costi` obbligatorio):
                          finestra warning-poi-blocco, avviso in STATO-EMPIRE.md ⚠️ COORDINAMENTO>
PROPRIETARIO / CONTROLLORE / CONSUMATORE / GATE / DIVIETO   [invariate da V2]
```

**Applicazione concreta ai due casi misurati:**
- **`checkpoint.py` campo `costi`**: finestra di 3 giorni con warning (accetta senza, stampa
  `⚠️ manca costi`) prima di passare a rifiuto — avviso in `STATO-EMPIRE.md` il giorno dell'innesto,
  perché ogni sessione (Gael, il daemon, una chat aperta di Max) lo veda prima di chiudere un
  checkpoint alla cieca.
- **`trace.py`**: F3 esce dalla riga «E4» della tabella di comando e diventa una riga propria
  (vedi §22 aggiornata), con ordine esplicito **prima** di E3 e proprietario dichiarato, invece che
  in una nota che corregge la tabella principale.

**Gate di §4:** i sei gate di E4 (V2) **più**, per ciascuna funzione: `<gate di regressione
dell'ospite>` → verde dopo l'innesto quanto lo era prima.

---

# §5 — PREVENTA: STATO A DUE TEMPI, IL DANNO GEMELLO SI CHIUDE, RIACCENSIONE PRIMA DEL FILO

**Il difetto (A-3, e il rilievo 2 della sentinella gemella sulla stessa scelta).** V2 §21-E3 cablava
*«si scrive lo stato PRIMA di inviare»* per curare il ricontatto (R7). Ma questo crea il danno
gemello mai nominato: se la sessione cade **fra** la scrittura dello stato e l'invio, il lead risulta
`CONTACTED` e il messaggio non è mai partito — alla ripresa, quel lead è perso per sempre, e il gate
di E3 (`CONTACTED > 22`) lo conta come un contatto vero. È un danno più invisibile del ricontatto: il
cliente ricontattato lo sa; il lead perso in silenzio non lo scopre nessuno. In più, il flusso che
E3 doveva «strumentare, non costruire» **è fermo dal 22 agosto** — misurato oggi (19 giorni), stato
e log identici da 4 giorni di misure diverse — e nessun censimento ha detto perché.

**La correzione:**

1. **Stato a due tempi**: `NEW → SENDING (scritto prima dell'invio) → CONTACTED (scritto dopo la
   conferma d'invio)`. Alla ripresa da `state.json`, ogni lead in `SENDING` è **ambiguo per
   definizione**: entra in una lista di riconciliazione umana (Neri verifica su WhatsApp se il
   messaggio è partito — al massimo 1-2 lead per caduta, non tutti i 1.045), mai risolto d'ufficio
   né come «già contattato» né come «da ricontattare».
2. **Il gate di E3 conta i `CONTACTED` con conferma d'invio**, non lo stato grezzo.
3. **Prima corsa strumentata a `dry_run: true` obbligatoria**, la corsa vera solo dopo — oggi il
   primo collaudo dell'innesto avviene su un cliente reale; con questa riga, avviene a vuoto.
4. **Nuovo scaglione E3.0 — «riaccendere e capire»**, prima di qualunque filo: diagnosticare perché
   Preventa è ferma dal 22/8 (sessione Chromium scaduta come IG/LinkedIn? blocco WhatsApp? Neri
   fermo su altro?) e riaccenderla. Ore proprie, non sottratte al filo di E3.

**Gate di §5 (sostituisce il gate di V2 §21-E3):**
```
python -m empire flow status                                → WF-S1: 5/5 step chiusi
<log Preventa ultimi 24h>                                    → run attivo (E3.0 chiuso)
jq '[.[]|select(.stage=="SENDING")]|length' state.json       → riconciliati entro 1h dalla ripresa
jq '[.[]|select(.stage=="CONTACTED" and .invio_confermato)]' → > 22 (con conferma, non stato grezzo)
<prima corsa>  dry_run=true                                   → tracciata, zero invii veri
```

---

# §6 — IL PONTE: CAMPO `fonte_di_verita` PER COPPIA, GUARDIA SIMMETRICA, PERCENTUALI DOPPIE

**Il difetto (A-5).** Con la freccia inversa (E5-bis, giusta: senza, il ponte scartava l'azienda che
lavora), «fonte di verità» smette di essere una proprietà del sistema e diventa una proprietà della
singola coppia — e nessun campo lo registra. Tre conseguenze misurate: (1) la guardia
anti-divergenza (V2 §14 pilastro 4) protegge solo la direzione scheda→esecutore, non quella
adottata; (2) E7 (le ondate) arriva dopo E5-bis nella tabella ma non dichiara se tocca le schede
adottate — se le tocca, riscrive un artefatto la cui fonte è l'esecutore (divergenza da manuale); se
non le tocca, restano fuori dal percorso verso il contratto pieno senza che nessuna riga lo dica;
(3) il denominatore delle percentuali agente si muove sotto i gate: da 439 a ~601 schede dopo
l'adozione dei 162, e lo stesso 235/439 (53,5%) diventa 39,1% sulla popolazione nuova — nessuna
sezione di V2 dice su quale popolazione si misura dopo E5-bis.

**La correzione:**

1. **Campo `fonte_di_verita: scheda|esecutore`** nell'anagrafe unica (pilastro 1 di V2 §14), scritto
   all'atto della generazione (E5a) o dell'adozione (E5-bis).
2. **Guardia simmetrica**: la marcatura anti-divergenza (V2 §14 pilastro 4) legge quel campo e
   blocca l'edit diretto del **lato generato**, qualunque esso sia — non solo l'esecutore.
3. **E7 dichiara il perimetro**: le ondate toccano **solo** le coppie `fonte_di_verita: scheda`. Le
   adottate (`fonte: esecutore`) si migliorano rigenerando dall'esecutore, mai riscrivendo la scheda
   a mano.
4. **Percentuali doppie, sempre**: ogni riga «OPERATIVO %» nel cruscotto (§23) e nei gate per ondata
   (E7) si riporta come `x/439-baseline` **e** `x/popolazione-corrente`, con la data del denominatore
   accanto — mai un solo numero.

**Gate di §6:** `python -m empire anagrafe --senza-fonte` → 0 (ogni coppia ha il campo);
`git diff` su una scheda adottata modificata a mano → **respinto** (guardia simmetrica).

---

# §7 — `empire vivo --json`: TRE ESITI, NON DUE — NON VALUTATO ESISTE

**Il difetto (B-6).** V2 §28.6 ammette onestamente che le sette condizioni (V-a..V-d, C-a..C-d) non
sono mai state provate una per una sui 15 ecosistemi, e rimanda la lista a V3. Ma `empire vivo
--json` (V2 §3, deliverable di E0.5, 2-3 h) nasce **prima** che quella lista esista, e legge lo
stato dei nodi dal registro — cioè legge un dato che per 15 nodi su 54 non è mai stato valutato. Il
numero che ne esce finisce ogni giorno nel cruscotto (§23) sotto gli occhi di Max: è la versione a
scala d'Impero dei «61 lead reali» che non esistevano come file (H3) — non numeri vecchi rimessi a
nuovo, ma **numeri mai nati esibiti come misure**.

**La correzione, doppia:**

1. **La lista per-nodo delle sette condizioni sui 15 ecosistemi si fa ORA, dentro V3** — è
   ricognizione in sola lettura (il divieto costruttivo non la tocca, come non ha toccato gli 8.120
   righe di censimento): condizione di chiusura di questo stesso documento, non rimandata oltre.
   *(Eseguita: vedi Appendice B.)*
2. **`empire vivo --json` nasce con TRE esiti per nodo**, non due: `PASSA | NON PASSA | NON
   VALUTATO`. I `NON VALUTATO` **non entrano né al numeratore né al denominatore**, e si stampano
   per nome in coda all'output. Un comando che sa dire «non lo so» è l'unica versione compatibile
   con L7 (*«si scrive ciò che si è misurato»*).

**Gate di §7 (corretto dopo l'esecuzione dell'Appendice B — vedi sotto):** non
`non_valutati=0` (irraggiungibile: 6 NON VALUTATO su 120 esiti sono definizioni mancanti, non
misure omesse) ma **`ogni NON VALUTATO ha una riga scritta che dice perché`** — soddisfatta oggi
6/6 dall'Appendice B stessa.

---

# §8 — §19 RISCRITTA: I TRE CARICHI DI GAEL, E NESSUNO LO BLOCCA MAI

**Questa è la sezione che risponde direttamente all'ordine di Max del 2026-09-10.** Il difetto
(B-7) è il più pericoloso dei 15 per una ragione già pagata in questa stessa azienda: un blocco
lasciato scritto e non negoziato ha tenuto LANCI fermo **3 giorni** (ADR-025/026). V2 §19 riconcilia
un solo conflitto — «due lavori #1», EMPIRE DESK contro il piano — e lo risolve. Ma
`29-ECOSISTEMA-LANCI/00-LEGGIMI.md` è diventato **Attivo, esecutore Gael, ADR-025 firmato il giorno
DOPO V2** (08/09, V2 è del 07/09): V2 conosce solo 2 dei 3 carichi veri di Gael. E dietro c'è un
fork architetturale reale, non una firma di cortesia: V2 chiede ai motori di EmpireDesk di esporre
`register(sub)` (il disegno "plugin" di `empire/`), mentre EmpireDesk **è lui stesso l'involucro**
(disegno "subprocess") — se il disegno B0-B4 di Gael è incompatibile, lo si scopre a E5b aperto
(15-45 ore, con Gael dentro), non con un messaggio oggi.

## §19 (sostituisce interamente V2 §19)

**I tre carichi di Gael, oggi — misurati, non dedotti:**

| Carico | Cos'è | Stato | Si ferma mai? |
|---|---|---|---|
| **EMPIRE DESK B0-B4** | l'app di tutto, split Max/Gael | in corso, «lavoro #1» dichiarato | **MAI** |
| **Costruzione LANCI v4** | `29-ECOSISTEMA-LANCI`, esecutore Gael | **Attivo**, ADR-025 firmato 08/09 | **MAI** |
| **E5b di questo piano** (i punti d'ingresso, dove EmpireDesk incontra `empire/`) | 15-45 h, la parte più chirurgica di E5 | ⬜ non iniziato | **SÌ, per ordine di ADR-028 e di questo paragrafo** |

**La legge, per iscritto — ADR-028 applicata al proprio interno:**

> **E5b è l'UNICO scaglione di tutto il piano che aspetta un atto di Gael prima di partire — e
> aspettarlo non ferma nient'altro.** Nessun altro scaglione (E0-E4, E5a, E5c, E6, E7, E8) dipende
> da E5b: la tabella dei percorsi in scrittura (§22) lo conferma, E5b non è mai un prerequisito a
> monte di un altro scaglione. **Gael non aspetta il piano**: EMPIRE DESK e LANCI procedono alla
> sua velocità, sui suoi percorsi, senza nessuna riga di questo documento che li tocchi o li
> rallenti.

**Cosa si chiede a Gael, esattamente — non una firma, una domanda tecnica precisa:** *«i motori che
agganci a EmpireDesk (B0-B4) possono esporre `register(sub)` per diventare sottocomandi di
`python -m empire <x>`, restando comunque lanciabili da EmpireDesk come oggi — o il tuo disegno a
subprocess lo rende incompatibile?»* — portata in cima a `STATO-EMPIRE.md` lo stesso giorno di
chiusura di questa critica (fatto: 2026-09-10, vedi la voce sopra questa in STATO-EMPIRE.md), non
lasciata scritta qui ad aspettare che Gael la trovi.

**Default se Gael non risponde — scadenza esplicita, come impone §25.2:**
- **Scadenza:** prima della chiusura di V4 (non prima della chiusura di V3: non è una decisione che
  serve per scrivere il piano esecutivo, serve solo per *costruire* E5b).
- **Default se silenzio:** **E5b NON si costruisce.** È l'unico default ammissibile verso chi ha
  piena autorità sul proprio terreno (`[[feedback_ordini_gael_assoluti]]`): non si decide per lui
  come agganciare i suoi motori. Si ripianifica in V4 col suo input quando arriva, senza che il
  resto del piano abbia perso un'ora ad aspettare.
- **Se Gael risponde «incompatibile»**: E5b si riprogetta (classe B — la skill come punto
  d'ingresso, V2 §15 — invece della classe A `register(sub)`) prima di V4, non a scaglione aperto.

**Ordine fra i tre carichi — chi decide, dichiarato (nuova riga in §26, vedi sotto):** l'ordine fra
EMPIRE DESK, LANCI ed E5b nelle giornate di Gael **lo decide Max**, non EMPERATOR per deduzione
(V2 lo deduceva: «vince EMPIRE DESK»). Default se Max tace: **l'ordine che Gael sta già seguendo
oggi** — EMPIRE DESK e LANCI, entrambi in corso, hanno priorità naturale su E5b che non è ancora
iniziato.

**Gate di §8:** nessun comando — è un gate documentale come V2 §0.6, dichiarato tale: il
deliverable è la domanda portata a Gael (fatto) e la sua risposta (aperta). La sua assenza non
blocca `python -m empire vivo --json` sul resto dei nodi: E5b, se non risposto, entra come
`NON VALUTATO` (§7), non come `NON PASSA`.

---

# §9 — LE CORREZIONI MEDIE (A-6, B-1, B-2, B-3)

## 9.1 — A-6: protocollo di deroga per gli hook

**Il difetto:** con 29 regole, 328 passaggi, 10 schemi, la probabilità di una collisione non ancora
censita (oltre le 3 note di V2 §21-E0.6) non è trascurabile. Quando un hook di E0.7 bloccherà lavoro
legittimo per una collisione ignota, V2 offre solo due vie, entrambe già condannate dal proprio
testo: spegnerlo (*«la fine del principio»*) o derogare in massa.

**Correzione:** ogni hook di E0.7/H13 nasce con un file `deroghe.jsonl` accanto. Una deroga = riga
firmata con motivo + scadenza ≤ 7 giorni + rilievo automatico nel battito. Due deroghe sulla stessa
regola in finestra → **ADR obbligatorio** (stessa legge «ceduta due volte diventa un hook»,
applicata alle deroghe stesse). Costo: 10 righe per hook in E0.7, nessuna ora nuova aggiunta allo
scaglione (rientra nel tetto già stimato).

## 9.2 — B-1: le destinazioni mancanti si contano ORA, non in E2

**Il difetto:** V2 §28.1 rimanda il conteggio a *dentro* E2, ma è mezz'ora di script in sola lettura
— la stima di E2 resta una forchetta da 8-14 a 23-36 ore (quasi ×3) per un numero che costava 30
minuti oggi.

**Correzione:** conteggio eseguito in V3 (ricognizione, non costruzione — L7). *(Risultato:
Appendice C.)* La stima di E2 in §22 aggiornata si chiude su quel numero, non su una forchetta.

## 9.3 — B-2: E6 ha un tetto provvisorio, e il gate APSOC è una decisione, non una stima

**Il difetto:** E6 è l'unico scaglione senza tetto (§25 «tetto ore» non può applicarsi dove non c'è
stima) — può sfondare in silenzio proprio nel piano che ha reso lo sfondamento silenzioso un
divieto. E dietro «da stimare dopo E4» si nasconde un sospetto più serio: i gate APSOC ≥80/≥85 non
hanno una sola funzione che li calcoli in tutto il repo — potrebbero non essere esprimibili come
comando+condizione+exit code deterministico (L9), e allora il lavoro non è «stimare», è «decidere
cosa significa calcolare».

**Correzione:** (a) tetto provvisorio E6 = tetto di E4 (30 h), si corregge dopo la prima misura
reale; (b) nuova riga in §26: **gate APSOC — funzione deterministica, giudizio umano firmato, o
modello con soglia: decide Max, default = giudizio umano firmato finché una funzione deterministica
non esiste ed è collaudata contro il proprio scheletro.**

## 9.4 — B-3: la mappa dei 10 schemi si legge ORA, prima di congelare HC-v2 a valle

**Il difetto:** V2 §12 congela HC-v2 a 11 campi *prima* di aver confrontato gli altri nove schemi
sorgente (solo APEX-7 è stato confrontato, ed è risultato non convertibile senza adattatore — 1 su
1). L'ordine giusto di un'unificazione è censire prima, congelare dopo; V2 ha fatto l'inverso.

**Correzione:** la mappa 10→1 (schema · campi · conversione o esclusione motivata) si scrive **in
V3**, leggendo `02d` §C.1 (già censito, nessuna costruzione). **Fatta — Appendice D**: 8 dei 10
schemi convertibili, 1 esclusione confermata (APEX-7), e **HC-v2 non regge a 11 campi**: servono
**13**, `due_at` (scadenza) e `costi` (oggetto costo/token/tier, confermato da due fonti
indipendenti — Observability e i contratti `HC-ME-*` della MEMORY). Zero migrazioni da disfare:
nessuna istanza viva dei 4 contratti reali oggi. La certezza è comprata prima di E4-F3, non dopo.

---

# §10 — LA TABELLA DI COMANDO, AGGIORNATA (sostituisce V2 §22 dove cambia)

| Scaglione | Ore V2 | Ore V3 | Tetto | Chi | Cosa cambia |
|---|---|---|---|---|---|
| **E0a** | (dentro E0: 2-3) | 1-1,5 (Max) | 2,5 | Max | merce + Payment Link, nessun prerequisito |
| **E0.9** | — (nuovo) | 2-4 | 6 | Max decide, EMPERATOR esegue | prezzo per decreto, aggancio Payment Link, link video→prodotto |
| **E0.5** | 4-6 | 4-6 | 9 | EMPERATOR | invariato |
| **E0.6** | 2-3 | 2-3 | 4,5 | EMPERATOR+Max | invariato |
| **E0.7** | 6-10 | 6-10 | 15 | EMPERATOR | +H13, +`deroghe.jsonl` per hook (§9.1), nessuna ora in più |
| **E0b** | (dentro E0: incluso) | 0,5-1 (Max) | 1,5 | Max | rotazione, DOPO E0.5, ordine+copertura esplicite |
| E1 | 13-20 | 13-20 | 30 | EMPERATOR | invariato |
| E2 | 8-14 (+15-22 da misurare) | **47-73** (Appendice C: 235/391 schede senza destinazione, misurato) | 110 | EMPERATOR | forchetta chiusa, peggio del previsto |
| **E3.0** | — (nuovo) | 3-6 | 9 | Neri+EMPERATOR | riaccendere e capire perché Preventa è ferma dal 22/8 |
| E3 | 12-18 | 12-18 | 27 | Neri+EMPERATOR | stato a due tempi, dry-run prima del vero (§5) |
| **F3** (estratta da E4) | (dentro E4) | 3-5 | 7,5 | EMPERATOR | prima di E3, proprietario proprio (§4) |
| E4 (F4,F5,F2,F1 restanti) | 12-20 | 9-15 | 22,5 | EMPERATOR | −F3, +riga Portata (§1), +politica di guasto (§4) |
| E5a | 8-15 | 8-15 | 22 | EMPERATOR | +campo `fonte_di_verita` (§6) |
| E5-bis | 20-40 | 20-40 | 60 | EMPERATOR | +campo `fonte_di_verita` (§6) |
| **E5b** | 15-45 | 15-45 (⬜ **in attesa di Gael, non bloccante — §8**) | 67 | EMPERATOR+Gael | default: non si costruisce se Gael non risponde entro V4 |
| E5c | 10-20 | 10-20 | 30 | EMPERATOR | invariato |
| E6 | da stimare | **da stimare, tetto provvisorio 30** | 30 | EMPERATOR | tetto provvisorio (§9.3) |
| E7 | 69-109 | 69-109 | 163 | EMPERATOR | perimetro: solo `fonte=scheda` (§6) |
| E8 | 10-20 | 10-20 | 30 | Max+EMPERATOR | invariato |
| **Totale** | ~190-320 h | **~230-395 h** (+7-15 h correzioni, **+25-46 h da Appendice C misurata**, −0 rimosso) | | | 12-24 settimane — la coda di E2 misurata allunga il calendario, non solo il conto |

**Percorsi in scrittura, nuove righe:** E0.9 → `checkout.config.json`, negozi esterni · F3 →
`empire/trace.py` (unica, non più contesa con E4) · E3.0 → `Outreach/preventa-*` (stato, non filo).

---

# §11 — §26, LE DECISIONI DI MAX: DUE RIGHE NUOVE

| # | Decisione | Default se Max tace | Quando serve |
|---|---|---|---|
| 8 | **Prezzo del Manuale** (B-002/B-003) | X€ per decreto (Max lo dichiara in E0.9), il team prezzi lo rivede quando nasce, non annulla la vendita nel frattempo | E0.9 |
| 9 | **Riconciliazione con LANCI v4** (attivo, esecutore Gael) — chi vende i pezzi usciti in E0a/E8, dentro quale funnel | i pezzi escono comunque (l'inventario non aspetta), LANCI li adotta appena il suo primo flusso chiude | prima di E1 |
| 10 | **Ordine fra i tre carichi di Gael** (EMPIRE DESK, LANCI, E5b) nelle sue giornate | l'ordine che Gael sta già seguendo oggi (EMPIRE DESK e LANCI, entrambi in corso, prima di E5b) | subito, non bloccante |
| 11 | **Gate APSOC** — funzione deterministica, giudizio umano, o modello con soglia | giudizio umano firmato finché la funzione deterministica non esiste e non è collaudata | E6 |

*(Le 7 decisioni di V2 §26 restano identiche e non si ripetono qui.)*

---

# §12 — R5 IN §25, RISCRITTO (vedi anche §2)

Sostituisce V2 §25 punto 3 relativo a R5: **«se dopo E3 non esistono pezzi fuori ≥ soglia dichiarata
E almeno un canale di vendita apparecchiato, il piano si ferma e si riapre la domanda: cosa
vendiamo, a chi»** — non più il criterio «0 byte» aggirabile da una riga di spesa qualsiasi.

---

# APPENDICE B — LE OTTO CONDIZIONI SUI 15 ECOSISTEMI (chiusura di §7) — ✅ FATTA

**Completata il 2026-09-10** (sentinella opus, 507 righe) —
[`_critica-v2/APPENDICE-B-7-CONDIZIONI-15-ECOSISTEMI.md`](_critica-v2/APPENDICE-B-7-CONDIZIONI-15-ECOSISTEMI.md).

**Il risultato, misurato: 0 ecosistemi su 15 passano tutte e otto le condizioni.** Su 120 esiti
(15×8): **28 PASSA · 86 NON PASSA · 6 NON VALUTATO**. I due nodi che il censimento dava per
"vivi" (11-APEX-7-CORE, 12-STREAM-S7-BOT) lo sono davvero su V-a..V-d (4/4), ma **nessuno dei due
supera COLLEGATO**: 11 fa 1/4, 12 fa **0/4**. Il "13% vivo" diventa **0% chiuso** quando si
contano anche i fili — è la misura esatta di L3, dichiarata da V2 §3 ma mai verificata riga per
riga fino ad ora.

**Cinque cose che né V2 né le prime 13 correzioni di V3 sapevano — integrate qui come sesta e
settima area di correzione:**

1. **Il gate di §1/§7 (`trace stato --origine hook`) non è eseguibile oggi** — corretto il
   2026-09-11 rimisurando: `python -m empire trace` **esiste** (sottocomandi `scrivi`, `elenco`,
   `cerca`, `stato`; `trace stato` stampa 25 tracce per tipo). L'Appendice B lo dava assente:
   errore di misura della sentinella, il disco vince. Quello che **manca davvero** è più stretto:
   il campo `origine` nella dataclass `Traccia` (`empire/trace.py:57-66`: tipo, titolo, autore,
   prova, quando, contesto, tags, id — nessun `origine`) e i filtri `--origine`/`--finestra`/
   `--json` su `trace stato`. **F3 (`09-F3-EMETTITORE.md`) costruisce campo e filtri PRIMA che
   §1/§7 abbiano un gate reale** — è un innesto su un comando vivo, non un comando da zero.
2. **`13-ARENA-APEX` non è "a metà", è rotta**: `orchestrator.py --help` → **exit 1**,
   `UnicodeEncodeError` cp1252 (misurato, non dedotto dal censimento). `11-APEX-7-CORE` ha già la
   riga che risolve lo stesso difetto — è un fix di un file, non uno scaglione.
3. **C-a passa 10 volte su 15 per un motivo che non regge**: lo stesso template JSON con
   `"payload": {}` vuoto, copiato in ogni `BACKBONE.md`. Se V4 lo lascia così, `empire vivo
   --json` mostrerà 10 nodi "collegati in ingresso" che non sanno cosa ricevono — un C-a vero
   richiede il payload compilato, non solo il campo presente.
4. **`ultimo_metro.py` ha reso C-d misurabile invece che opinabile per 2 ecosistemi**: NON PASSA
   (non NON VALUTATO) per `02-INFO-BUSINESS` (7 libri pronti, `libri_pubblicati/` vuota) e
   `05-MULTI-BUSINESS` (video-01/02/03 fra i pezzi mai usciti).
5. **`15-LANCI`, nata da 4 giorni e fuori dal censimento originale, fa meglio di APEX-7 sui
   collegamenti** (5/8, 2/4 su COLLEGATO): il suo schema — artefatto tipizzato, 13 JSON Schema,
   verbale automatico a ogni transizione — è codice funzionante oggi, ed è il modello da
   generalizzare per F1 (V2 §9), non solo un ecosistema da misurare come gli altri 14.
6. **Il perimetro "15 ecosistemi" è scaduto**: sul disco ce ne sono **16**, e il numero **08 è
   occupato due volte** — violazione REGOLA PUNTATORI (`CLAUDE.md`). Un comando che indirizza i
   nodi per numero (`empire vivo --json`, per costruzione) non può nascere prima che
   `REGISTRO-NUMERI.md` sia sanato, o produce due righe con la stessa chiave.
7. **6 dei 6 NON VALUTATO sono C-d** (5) **o V-b** (1), non per misura mancata ma per definizione
   mancante (*"un consumatore interno conta come reale?"*) — il gate di §7 (*"non_valutati=0"*)
   **non è raggiungibile da nessuna ricognizione**: si riscrive come *«ogni NON VALUTATO ha una
   riga che dice perché»* (qui soddisfatta 6/6). Corretto in §7 sopra.

**Limite dichiarato (L7):** nessun test è stato rilanciato in questa ricognizione (sola lettura
pura); i due PASSA su V-d (11, 12) poggiano su verdi datati e citati (ADR-012 26/08, `STATO-
RIPRESA.md` 03/08), non su un'esecuzione di oggi — se V4 vuole quel numero a prova di errore,
servono due `pytest` veri, gli unici due comandi che questa ricognizione non poteva permettersi.

# APPENDICE C — LE DESTINAZIONI MANCANTI NELLE 174 SCHEDE (chiusura di §9.2) — ✅ FATTA

**Eseguita il 2026-09-10, in sola lettura** (`grep`/regex su `company/**/*.md`, nessuna scrittura).

**Il conteggio reale è peggiore della stima di V2 §28.1** (*"se manca nella metà dei casi, +15-22
h"*): delle **391** schede con intestazione `## Input / Output` (V2 aveva già il numero giusto, non
174 — il ×2 già segnalato in V2 §28.1 stesso), **235 non hanno una destinazione riconoscibile**
(percorso file, o una delle 16 parole chiave: "finisce in", "destinazione", "salvato in", "scrive
in", "consegnato", "invia a", "va in", "archiviato", "pubblicato in", ecc.), **156 ce l'hanno già**.

**Costo reale della coda, a 10-15 min per riga: 39-59 ore**, non 15-22. Il conto di V2 assumeva
metà (~87 mancanti); la misura reale ne trova 235 — più del doppio.

**Limite dichiarato del metodo (L7):** è un'euristica testuale, non una lettura umana riga per
riga — può classificare come "senza destinazione" una scheda che la descrive in prosa senza una
delle parole chiave cercate (es. "il risultato torna al chiamante"). Il numero è un limite
superiore difendibile, non un conteggio a prova di errore: **235 va trattato come "almeno 235 su
391 vanno controllate"**, non come verità assoluta senza rilettura a campione.

**Conseguenza per §10 (tabella di comando):** la riga E2 si aggiorna da *"8-14 + N misurato"* a
**8-14 (rinomina) + 39-59 (destinazioni) = 47-73 ore**, tetto 110. È il singolo aggiornamento di
stima più grande prodotto da questa critica — e la ragione per cui B-1 era un MEDIO ben speso: 30
minuti di script hanno chiuso un'incognita da 40+ ore prima che lo scaglione partisse, non a metà.

# APPENDICE D — LA MAPPA DEI DIECI SCHEMI (chiusura di §9.4) — ✅ FATTA

**Completata il 2026-09-10** (sentinella fable, interrotta a metà da rate-limit di sessione e
finita da EMPERATOR nello stesso turno, stessa disciplina di fonte-citata) —
[`_critica-v2/APPENDICE-D-MAPPA-DIECI-SCHEMI.md`](_critica-v2/APPENDICE-D-MAPPA-DIECI-SCHEMI.md).

**Risultato: HC-v2 non regge a 11 campi — servono 13, non 12.** 8 dei 10 schemi sono convertibili
(3 lisci, 5 con adattatore già mappato campo-per-campo), 1 esclusione confermata (APEX-7, già
nota da V2). Ma **due campi mancano**, trovati da fonti indipendenti: **`due_at`** (scadenza —
Schema 2, il template del Bus) e **`costi`** (oggetto costo/token/tier — visto in DUE schemi
indipendenti: l'evento Observability e i contratti `HC-ME-*` della MEMORY, che lo rende
obbligatorio per legge propria). Correzione a basso costo, nessuna migrazione da disfare (zero
istanze vive dei contratti reali oggi). **HC-v2 in V4 nasce a 13 campi**, non 11: i dieci di V2
§12 più `due_at` (opzionale) e `costi` (obbligatorio per esecutori-agente).

> **Nota di metodo sulle tre appendici:** sono dichiarate qui come lavoro aperto, non finto chiuso —
> è la stessa regola che il piano stesso impone (L5, L9): un gate non si dichiara, si esegue. Le tre
> vanno chiuse prima che V3 si dica «finita», o restano tre rilievi di sola-lettura non fatti dentro
> il documento che diceva di farli. *(Prossimo passo di questa stessa sessione o della successiva.)*

---

# AVANZAMENTO DI QUESTO DOCUMENTO

| Tappa | Stato |
|---|---|
| Le 13 correzioni scritte | ✅ |
| Appendice B (8×15 condizioni) | ✅ 0/15 ecosistemi passano tutto; 28/86/6 su 120 esiti; 7 correzioni nuove integrate |
| Appendice C (conteggio destinazioni) | ✅ 235/391 senza destinazione, E2 aggiornata |
| Appendice D (mappa 10 schemi) | ✅ HC-v2 serve 13 campi, non 11 (`due_at` + `costi`) |
| **Critica 3** (opzionale — si salta se V3 regge) | ⬜ |
| V4 — piano esecutivo | ⬜ |

**Garanzia esplicita richiesta da Max, verificata riga per riga in questo documento:** nessuno
scaglione di V3, in nessun punto, rende il lavoro di Gael (EMPIRE DESK, LANCI) dipendente da questo
piano. L'unico punto dove il piano dipende da Gael (E5b) ha un default che non lo blocca e non
blocca nient'altro. È l'applicazione di ADR-028 dentro il documento che il suo stesso ordine ha
generato.
