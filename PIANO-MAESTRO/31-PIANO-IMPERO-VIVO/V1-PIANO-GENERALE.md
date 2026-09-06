# 🜂 V1 — PIANO GENERALE PER RENDERE VIVA DIGITAL EMPIRE

> **Versione:** 1 di 4 · **Data:** 2026-09-06 · **Autore:** EMPERATOR · **Committente:** Max
> **Stato:** DA CRITICARE — questa versione esiste per essere demolita, non per essere eseguita
> **Leggi vincolanti:** le sette leggi in [`00-LEGGIMI.md`](00-LEGGIMI.md) §2
> **Ripresa:** EMP-MCC4
>
> **Fonti:** 5.042 righe di censimento misurato prodotte nella notte del 6 settembre da otto
> doom bot, in `dati/`. Ogni numero di questo piano viene da lì o da un comando che ho
> lanciato io. Dove c'è un giudizio e non una misura, è scritto.

---

# PARTE 0 — COME SI LEGGE QUESTO PIANO

## 0.1 Cosa è

È la **prima** delle quattro versioni ordinate da Max. Contiene: la diagnosi, le definizioni
operative, l'architettura della soluzione, l'organizzazione delle forze, il lavoro diviso in
scaglioni con gate eseguibili.

## 0.2 Cosa NON è

Non è esecutivo. Non contiene ancora ogni file da toccare né ogni prompt da scrivere: quello è
V4. **Non va eseguito.** Va criticato, e la critica dirà dove si romperebbe.

## 0.3 Le fonti, con le righe misurate

| Censimento | Righe | Cosa ha stabilito |
|---|---|---|
| `dati/censimento-01a-ecosistemi.md` | 1.256 | i 15 ecosistemi scheda per scheda: 2.547 file, 5 con codice, **2 vivi su 4 condizioni** |
| `dati/censimento-01b-organi.md` | 1.096 | i 14 organi di governo: Board, Guilds, Sentinelle, Mandato, Ispettorato, MAXIMILIAN, Backbone |
| `dati/censimento-02-collegamenti.md` | 363 | l'infrastruttura: bus, contratti, registri, motore di flusso, tracce |
| `dati/censimento-02b-mappa-collegamenti.md` | 208 | i passaggi di consegne progettati nei dossier (parziale) |
| `dati/censimento-03a-popolazione.md` | 1.426 | 439 agenti, la specifica C4 esatta, 5 ondate, **un guasto vero in `census.py`** |
| `dati/censimento-03b-regolamento-forze.md` | 113 | la gerarchia delle forze già in vigore (ADR-015) |
| `dati/censimento-03b2-cadute.md` | 384 | **33 cadute reali · 6 famiglie di recidiva · 29 regole** |
| `dati/censimento-04-motori.md` + `04b` | 196 | i motori reali fuori da `company/` (parziale) |

**Tre censimenti sono incompleti** (`02b`, `04`+`04b`, e le sintesi di `01b`): i doom bot sono
caduti sul limite di sessione dell'account alle 01:45. È dichiarato qui e ripreso in §30.

---

# PARTE I — LA DIAGNOSI

## 1. Il verdetto in una pagina

**Digital Empire è costruita al 92% sulla carta e viva al 18%.** Dentro i 15 ecosistemi ci sono
2.547 file; **5 nodi su 15 contengono codice**, e **2 su 15 sono vivi su tutte e quattro le
condizioni** (`11-APEX-7-CORE` e `12-STREAM-S7-BOT`), più il solo workflow libri dentro
`02-INFO-BUSINESS`. Il 18% misurato dall'esterno e il 2-su-15 misurato dall'interno dicono la
stessa cosa da due direzioni.

Ma il verdetto vero non è la percentuale. È questo:

> **L'Impero non è incompleto. È scollegato.**
> I motori esistono e girano. Il governo esiste ed è scritto bene. Gli agenti esistono e sono
> 439. Quello che non esiste è **il filo che li unisce** — e senza quel filo ogni pezzo, per
> quanto perfetto, è un pezzo fermo.

## 2. La malattia, e ha un nome solo

**Ogni atto di collegamento in questa azienda è un atto separato e volontario. E gli atti
separati non si fanno.**

Non è una mia diagnosi: è scritta nel nostro codice. Il commento in testa a `empire/trace.py`
dice, testualmente: *«scrivere la traccia era un atto separato, e gli atti separati non si
fanno»* — e prometteva *«qui la traccia è un sottoprodotto, non un compito in più»*. Chi l'ha
scritta aveva capito tutto. Poi ha costruito esattamente la cosa che aveva descritto: 25 tracce
in tutta la vita del sistema, perché sono 25 atti volontari.

## 3. Le sei prove

| # | Prova | Misura | Fonte |
|---|---|---|---|
| 1 | **Chiudere uno step di workflow** si può fare solo a mano da riga di comando. `done_step()` è chiamato da **un solo punto**, `empire/flow/cli.py:115`. Fuori da `empire/flow/` e dai test: **0 chiamanti** | 0 step chiusi su 10 workflow | `02` §3.4 |
| 2 | **Scrivere una traccia**: un solo scrittore automatico in tutto l'Impero (`empire/avvia.py:82`), e produce **1 tipo su 5**. Gli altri quattro solo a mano | 25 tracce in tutta la vita | `02` §4.2 |
| 3 | **I registri**: 16 letture di codice sull'anagrafe. **16 su 16 sono verifiche. 0 sono decisioni di instradamento** | 16 / 0 | `02` §2 |
| 4 | **Il Bus** non ha mai trasportato un carico: `company/Backbone/Bus/handoffs/` contiene solo `.gitkeep`. **Nessun file `.py` del repo legge un contratto di handoff** | 0 istanze | `02` §1.1, §1.5 |
| 5 | **L'Osservabilità** è al 100% documentazione: 0 righe di codice, e il suo README rimanda a `company/metrics/` e `costs.sh` che **non esistono** | 0 emettitori | `02` §4.4 |
| 6 | **Tre formati diversi** per lo stesso evento (13 campi / 8 / 10). Finché restano tre, nessuna funzione sola può alimentarli | 3 schemi | `02` §4.5 |

**Il caso limite che chiude la dimostrazione.** L'11 giugno 2026, dalle 18:13:12 alle 18:14:10 —
**58 secondi** — tutti e quattro i contratti dell'Agency sono stati attraversati: 4 invii, 4
ricezioni, 3 gate passati, tutto tracciato. Con `dry_run: true` e cliente
`DryRun-Client-01 (TEST - non reale)`, per far passare un gate. **La traccia c'è, il carico no.**
Da allora: 87 giorni di silenzio, `updated_at` fermo.

L'Impero **sa** attraversare la sua catena. L'ha fatto una volta, a vuoto, per un esame.

## 4. I quattro errori di misura scoperti stanotte

Questi contano più della diagnosi, perché sono i punti in cui il piano precedente stava per
lavorare su dati falsi.

### 4.1 `registry census` è rotto — un guasto vero, con prova aritmetica

`empire forge scan` contava 439 agenti, `empire registry census` ne contava 69. Non era una
questione di opinioni fra due strumenti: **uno era rotto.** In `empire/registry/census.py` il
corpo del ciclo `for fname in filenames:` finisce a riga 189, e le righe 191-240 — `artifacts.append`
compreso — stanno a 8 spazi, cioè nel ciclo `for dirpath` esterno. **Salva un solo file per
cartella.** Prova: artefatti totali **21.682**, directory visitate **21.682**, identici.

### 4.2 I 439 e i 164 sono due popolazioni diverse — e si toccano in DUE nomi

Questo demolisce il blocco B1 della task del 31 agosto.

I **439** che `forge scan` giudica sono **schede** dentro `company/`. I **164** che si possono
davvero invocare stanno in `.claude/agents/` (129 di progetto + 35 globali). **L'intersezione è
di due nomi.** Portare i 439 al 100% di contratto d'uscita — 30-45 ore dichiarate — **non
renderebbe concatenabile un solo agente che gira davvero.**

### 4.3 La «cartella vuota» conteneva un bot che ha girato

`company/Ecosistemi/08-STREAM-S7-BOT`, dichiarata vuota dall'audit del 31 agosto e mostrata come
`0 agenti, ECOSISTEMA.md=NO` da `empire doctor`, contiene `S7_NFT_BOT.zip` con **14 voci** —
5 moduli Python, `requirements.txt`, `.env.example`, e un `paper_trade_log.csv` **con sei
operazioni reali** — più quattro `.pyc` datati **2026-07-23, 08:47-08:48**: prova che quel
codice **ha girato su questa macchina**.

### 4.4 Trentasei nomi esistono in due copie divergenti

Nessuna copia identica: **tutte divergono**. Diciannove in `04-MARKETING` sono contate due
volte nei 439. Dieci `frg-*` stanno sia in `Ecosistemi/07-FORGE` sia in `Genesi-Core/FORGE`, e
**la copia buona — 10 su 10, perfetta — è invisibile allo strumento**, mentre quella contata e
giudicata è 6,7 e parziale. Stavamo per migliorare la versione peggiore di agenti già a posto.

## 5. Cosa cambia rispetto ai piani che esistono

| Documento | Cosa resta | Cosa cade |
|---|---|---|
| `TASK-MAX-20260831` (B0..B8) | i nove blocchi restano il perimetro del lavoro | **B1 come concepito cade**: i 439 non sono la popolazione che va resa concatenabile (§4.2). E le sue misure di partenza vanno riverificate: ha già mentito una volta (§4.3) |
| `Dossier 30` (S1..S7) | la misura 92/18 e i sette scaglioni restano validi | **copre «vivo», non copre «collegato»** — ed è il motivo per cui esiste questo piano |
| `Dossier 08` (roadmap F1..F12) | F1-F3 sono fatte (la carta), F4-F12 sono la vita | nulla cade: questo piano è il modo di attraversare F4-F12 |

---

# PARTE II — LE DEFINIZIONI OPERATIVE

Senza queste, «vivo» e «collegato» restano parole e ognuno le userà a suo comodo. Con queste,
diventano comandi.

## 6. VIVO — quattro condizioni, tutte e quattro

Un artefatto è vivo se e solo se:

| | Condizione | Come si prova |
|---|---|---|
| **V-a** | **Si invoca** con un comando dichiarato | il comando esiste ed esce 0 |
| **V-b** | **Produce un'uscita conforme a un contratto scritto** | l'uscita esiste e valida contro lo schema |
| **V-c** | **L'uscita finisce in un posto stabilito** | il percorso è dichiarato e il file c'è |
| **V-d** | **Un test lo prova**, e si può rilanciare | il test esiste ed è verde |

Meno di quattro su quattro: **non è vivo, è descritto.** Oggi passano tutte e quattro: 2 nodi su 15.

## 7. COLLEGATO — tre condizioni, e non è un extra

| | Condizione | Come si prova |
|---|---|---|
| **C-a** | ha almeno **un ingresso dichiarato** (chi lo chiama, con che carico) | il contratto in ingresso esiste |
| **C-b** | ha almeno **un'uscita dichiarata verso un destinatario reale** | il contratto in uscita nomina un destinatario esistente |
| **C-c** | ogni passaggio **lascia una traccia scritta da sola** | la traccia compare senza che nessuno l'abbia scritta a mano |

**Un nodo che passa V-a..V-d ma fallisce C-a..C-c non conta come chiuso.** È la legge L3, e va
detta in numeri: oggi **nessun nodo dell'Impero passa C-c**, perché non esiste un solo punto in
cui una traccia nasca da sola come sottoprodotto di un lavoro.

## 8. Il contratto d'uscita (C4) — specifica esatta, misurata

Questa è la specifica su cui si baseranno centinaia di riscritture. È stata letta nel codice di
`empire/forge.py`, non dedotta.

**Regola:** il file dell'agente deve contenere una **riga autonoma `## Output`** — livello 2, la
parola `Output` subito dopo i cancelletti. Sotto, per ogni artefatto prodotto: **che cos'è e dove
finisce** (tabella `Artefatto | Destinazione | Sempre?`, oppure JSON con campo destinazione).

**Vietato:**
- `## Input / Output` — **commesso 274 volte**. Soddisfa C3-ingresso e **fallisce** C4.
- `**Output prodotto:**` — **commesso 228 volte**. La parola in mezzo rompe entrambi i pattern.

**Collaudo per singola riscrittura:** `python -m empire forge agente <id>` deve stampare
`prova: ## Output`. Una prova diversa è un passaggio accidentale, non un contratto — e 26 dei 61
agenti oggi «operativi» passano proprio da quella porta accidentale.

**La conseguenza che cambia il piano:** dei 314 senza contratto, **274 il contratto ce l'hanno
già scritto**, sotto il titolo sbagliato. E **174 agenti (39,6% della popolazione) sono a un
solo criterio dal punteggio pieno**. La prima ondata **non è scrittura: è rinomina di un
titolo**, e da sola porta gli operativi dal 13,9% al **53,5%**.

## 9. Il contratto di handoff (HC-v2) — i dieci campi che mancano

`HC-v1` è un buon **descrittore di consegna**. Non è un **indirizzo**. Perché un router possa
prendere un handoff e sapere dove metterlo, mancano:

| Campo | Perché serve |
|---|---|
| `_instance_id` | oggi `_id` è l'id del *contratto*, non del *messaggio*: due handoff dello stesso tipo si sovrascriverebbero |
| `created_at` reale | ordinare la coda, misurare l'età di un pendente |
| `status` mutabile (`pending→accepted→done→rejected`) | dire a che punto è; oggi è la costante `"template"` in tutti e quattro |
| `queue` come **percorso**, non come nome | `"queue": "leads_ready"` non è una cartella esistente: il destinatario non ha una casella |
| `scope` (`intra` / `inter`) | il Bus è a due livelli e HC-v1 non dice a quale appartiene |
| `brand_kit` / `icp` | il README del Bus li dichiara **obbligatori** nell'inter-ecosistema: 4 contratti su 4 sarebbero invalidi per la regola del Bus stesso |
| `note_correttive` su reject | regola del Bus: un rifiuto **deve** dire perché |
| `retry` / `escalation_count` | regola del Bus: due rifiuti → escalation automatica |
| firma di chi ha accettato | audit: chi ha detto sì |
| **criterio di accettazione valutabile a macchina** | oggi sono frasi italiane (*«qualifier_score >= soglia ICP attiva»*): nessun codice può dire se è passato |

L'ultimo è il più grave: **un criterio che nessuna macchina può valutare non è un gate, è
un'opinione.**

## 10. La traccia — un formato solo, non tre

Oggi convivono `Observability/README.md` (13 campi), `empire/trace.py` (8), e
`agency/trace.jsonl` (10). Il piano ne impone **uno**, e gli altri due diventano viste di quello.
Finché sono tre, nessuno può scrivere la funzione unica che li alimenta — ed è per questo che
nessuno l'ha scritta.

---

# PARTE III — L'ARCHITETTURA DELLA SOLUZIONE

## 11. Il principio, uno solo

> **Il collegamento non si chiede: si ottiene per costruzione.**
> Ogni cosa che oggi è un atto separato e volontario diventa un **sottoprodotto** di un lavoro
> che comunque si fa, oppure un **hook che blocca** se manca.

È la medicina che ha già funzionato una volta in questo Impero: la forma del mio battito, ceduta
cinque volte quando era una regola scritta, si è chiusa in un giorno quando è diventata un hook
che impedisce la consegna. **Le regole cedono. Le macchine no.**

Da qui discende tutto il resto: non «costruire il bus» (il bus c'è), ma **far sì che nessun
lavoro possa concludersi senza aver lasciato il suo passaggio**.

## 12. Il pezzo che manca davvero: NEXUS

L'Impero ha quindici ecosistemi che **fanno**, e nessuno che **colleghi**. La proposta è il
sedicesimo — e il numero è **16**, perché il 15 è riservato ai LANCI in `REGISTRO-NUMERI.md`.

> **PROPOSTA (decide Max, richiede un ADR — ADR-009 impone un ADR per ogni ecosistema dal 14 in su).**

**`16-NEXUS` — l'ecosistema che connette. Non produce niente di suo. Esiste solo perché gli
altri quindici si parlino.**

### 12.1 I suoi cinque organi

| Organo | Cosa è | Sostituisce / completa |
|---|---|---|
| **N1 — La Tabella di Instradamento** | l'unica fonte che dice *chi chiamare per ottenere cosa*: da agente/reparto → capacità → contratto d'ingresso → contratto d'uscita | oggi i registri dicono **dove** sta ogni cosa, mai **cosa si passano** (`skills-map.yaml`: 650 voci, **zero** campi `consuma`/`produce`) |
| **N2 — Il Bus vero** | code reali su disco, una per destinatario, con `HC-v2` e lo stato mutabile | oggi `handoffs/` è vuota e `queue` non è un percorso |
| **N3 — L'Emettitore Unico di Eventi** | **una sola funzione** che scrive la traccia, chiamata da dentro le operazioni, mai a parte | oggi 3 formati, 1 scrittore automatico, 1 tipo su 5 |
| **N4 — Il Ledger** | il libro unico dei fatti misurabili: costi, produzioni, incassi, cadute | oggi **non esiste**: `ruflo/` è vuota e in tutto il repo non c'è un file *ledger*, mentre `09-OPERATIONS` lo esige come sua prima condizione |
| **N5 — Il Guardiano dei Collegamenti** | l'hook che impedisce di chiudere un lavoro senza il suo passaggio, e il gate che valuta a macchina i criteri di accettazione | oggi il criterio è una frase italiana che nessun codice legge |

### 12.2 Cosa NEXUS non fa

Non produce copy, non produce video, non manda messaggi, non decide strategie. **Se NEXUS
comincia a fare il lavoro di un altro ecosistema, è fallito.** Va scritto nel suo Mandato come
divieto, non come raccomandazione.

### 12.3 Perché un ecosistema e non una cartella

Perché deve avere un proprietario, un controllore indipendente, un Mandato e un posto
nell'anagrafe (legge L6). Un pezzo di infrastruttura senza padrone è esattamente ciò che è
successo all'Osservabilità: un README che descrive file che nessuno ha mai creato.

## 13. Il ponte fra le schede e gli esecutori

**Il problema (§4.2): 439 schede, 164 esecutori, 2 nomi in comune.**

La soluzione non è scegliere una delle due popolazioni e buttare l'altra — sarebbe contro L1.
È **generare** l'esecutore dalla scheda, tenendo la scheda come fonte di verità (ADR-003: si
avvolge, non si riscrive).

```
company/**/agente.md   ──generazione──▶   .claude/agents/<nome>.md
   (la prosa, la fonte)                       (l'esecutore invocabile)
        │                                            │
        └──────────── N1 Tabella di Instradamento ───┘
                 (chi chiamare per ottenere cosa)
```

**Ordine di attivazione** (dal più alto, perché sono quelli che EMPERATOR chiama per primi):
Board C-Suite (già invocabile, 7/7) → **15 direttori di ecosistema (oggi 0)** → 5 Sentinelle
(già invocabili) → **MAXIMILIAN (oggi 0)** → reparti L2/L3/L4 a scendere.

## 14. Il punto d'ingresso per ecosistema

Ogni ecosistema deve avere **un comando che parte, chiama il motore vero dov'è, e restituisce
l'uscita dichiarata**. Non si sposta codice (L4): i motori restano nelle cartelle storiche.

**Il caso che dimostra il problema:** `YOUTUBE-AUTOMATION-FACTORY`, **136 file Python**, il
motore video più grosso dell'Impero, **non è nominato da nessuno dei due ecosistemi che
dovrebbero usarlo** — zero occorrenze in `05-MULTI-BUSINESS`. Il pezzo più grande dell'azienda
è orfano rispetto alla sua stessa organizzazione.

## 15. Gli hook: rendere meccanico ciò che oggi è volontario

Dodici delle ventinove regole ricavate dalle cadute sono marcate **[MECCANICA]**, e il criterio
non è severità: è **recidiva**. La loro famiglia di errore si è già ripetuta, quindi scriverle in
un regolamento sarebbe la sesta riga inutile.

| Cosa deve bloccare | Errore che ha già colpito |
|---|---|
| chiudere un lavoro senza traccia | 25 tracce in tutta la vita |
| accettare il rapporto di un agente senza verifica su disco | 6 episodi di lavoro dichiarato e mai fatto — difetto **qualificato «da controllare strutturalmente» e mai controllato** |
| un dato senza sorgente riscontrabile in un rapporto | i «61 lead reali» che non esistono come file |
| un controllo che passa sul proprio scheletro vuoto | `--check` che approvava il template · selftest che verificava il path e non l'argomento |
| un indicatore che diventa verde nel ramo d'errore | KPI verde su valore illeggibile |
| un frontmatter di agente rotto che degrada in silenzio | **4 agenti morti in silenzio per due caratteri** |
| un numero di checkpoint scelto a mano | ceduto **4 volte in 13 giorni** |
| due forze che scrivono lo stesso oggetto | 6 episodi, git bloccato incluso |

---

# PARTE IV — LE FORZE

## 16. La gerarchia, già in vigore

ADR-015 definisce i gradi (scagnozzo / sentinella / doom bot su haiku / sonnet / opus), chi può
attivarli, e l'obbligo di **dichiarare per iscritto ogni attivazione**. Non si tocca: si completa.

## 17. Il regolamento — ventinove regole, ognuna pagata

Ricavate da **33 cadute reali** censite nei checkpoint dell'Impero. Nessuna inventata a tavolino:
ognuna porta il caso da cui nasce. Qui la forma breve; l'elenco integrale con le fonti è in
`dati/censimento-03b2-cadute.md` §B.

**Prima di delegare (7):** dichiara e verifica il grado prima di lanciare · **[M]** un solo
swarm pesante per volta con blocco di coordinamento scritto · dimensiona le teste sul budget
residuo, non sui compiti · **quando una causa di caduta è dichiarata permanente, smetti di
delegare in quella forma** · in dubbio, sequenziale · misura il carico contro i limiti
dell'ambiente prima di assegnarlo · confronta la coda con gli artefatti su disco.

**Dentro il prompt (7):** **[M]** file d'uscita creato vuoto al primo minuto e risalvato a ogni
sezione · WRITE-EARLY, massimo 2-3 letture prima della prima scrittura · scrivi per primo il
pezzo più costoso, non il più facile · nessuna chiave di stato nasce in un prompt · la
convenzione dei nomi si scrive nel prompt · marcatore obbligatorio per l'ignoto (`[DM]`) ·
l'idempotenza si sospende contro i residui della versione precedente.

**Alla consegna (6):** **[M]** nessun rapporto si accetta senza verifica su disco · il test
empirico batte la dichiarazione · **[M]** guardia di provenienza su ogni dato · un agente è
consegnato quando ha servito un consumatore reale, non quando esiste · distingui la caduta
onesta da quella bugiarda · chi riprende ispeziona il disco file per file.

**Sui controlli (6):** **[M]** ogni controllo va provato contro il proprio scheletro vuoto ·
**[M]** l'errore non è mai verde · **[M]** una configurazione agenti deve avere un test che
dimostri chi la legge · **[M]** un gate valida il frontmatter di ogni agente e fallisce
rumorosamente · chi giudica non scrive · **[M]** una regola ceduta due volte diventa un hook.

**Sulla convivenza (3):** **[M]** il codice del checkpoint si conia con lo script · non si
committa mai la metà distruttiva di un rifacimento · quando cade la sessione, controlla se gli
agenti sono vivi prima di rilanciare.

## 18. La regola parallelo/sequenziale, corretta stanotte

L'Impero aveva già misurato: **9 su 9 in sequenziale contro 1 su 4 in parallelo**, e ne aveva
tratto *«in dubbio, sequenziale»*. Stanotte ho lanciato otto doom bot in parallelo e ne sono
caduti sette. **Ho rifatto l'errore che il mio stesso Impero aveva già pagato.**

Ma la notte ha anche prodotto il dato che mancava, e la regola va **spaccata in due**:

| Tipo di lavoro | Regola | Prova |
|---|---|---|
| **Produzione** (scrive, consuma budget, tocca gli stessi file) | **sequenziale**, sempre | 9/9 contro 1/4 |
| **Ricognizione** (sola lettura, aree disgiunte, ripartibile) | **parallelo ammesso**, con scrittura incrementale obbligatoria | stanotte: 7 cadute su 8, e **5.042 righe salve** |

La differenza non è la fortuna: è che nella ricognizione **la scrittura incrementale rende la
caduta quasi gratuita**. Nella produzione no, perché il lavoro perso è lavoro che ha già speso.

## 19. L'addestramento

Ogni forza riceve, prima di muovere un dito: **il minimo comune** (poche righe: le leggi L1-L7,
il divieto di inventare, l'obbligo della fonte, la lingua, la regola anti-caduta) e
**l'addestramento di terreno** (solo per chi tocca quel terreno). Il minimo comune deve restare
corto: ogni riga si paga a **ogni singolo ingaggio**, moltiplicata per il numero di forze.

La fonte della conoscenza esiste già ed è `CONOSCENZA-EMPIRE` — con un debito dichiarato e
aperto: *«l'agente esiste ma non ha ancora alimentato nessuno»*. **È il caso 30 delle cadute**, e
in questo piano si chiude: un organo di conoscenza che non ha servito nessuno non è consegnato.

## 20. Il modulo d'ingaggio

Forma fissa, riempibile, obbligatoria per ogni delega: identità e grado · perimetro esatto (cosa
può toccare, cosa non deve toccare mai) · contesto minimo · uscita attesa e dove va scritta ·
regola anti-caduta · idempotenza · **il gate, cioè il comando che dice se ha finito bene** ·
cosa fare se cade a metà · lingua · divieto di inventare.

Il dettaglio pieno con le tre varianti (scagnozzo / sentinella / doom bot) è rimandato a V2:
il doom bot che doveva progettarlo non è mai partito per il limite di sessione (§30).

---

# PARTE V — IL LAVORO

## 21. Il criterio d'ordine

Tre principi, in questo ordine di forza:

1. **Prima ciò che non costa e sblocca molto.** La rinomina di un titolo che porta gli agenti dal 13,9% al 53,5% viene prima di qualunque scrittura.
2. **Prima la fetta verticale, poi la scala orizzontale.** Un flusso vero che attraversa l'azienda prova la catena; 439 contratti scritti prima di quella prova sono 439 scommesse.
3. **Prima ciò che porta denaro.** L'azienda oggi non può incassare un euro, e questo non è un dettaglio del piano: è il primo scaglione.

## 22. Gli scaglioni

### E0 — LE MANI DI MAX (45 minuti, nessuno le fa al posto suo)
Rotazione delle 3 credenziali esposte sul repo pubblico (B-020 Brevo, B-021 Arena+OpenRouter
**viva adesso**, B-023 Instagram) → login Instagram **dopo** il cambio password → login LinkedIn
→ **2 Payment Link Stripe**.
**Gate:** `empire controllo` passa da 2/6 a 5/6 · la vecchia chiave OpenRouter risponde 401.

### E1 — IL PERIMETRO PULITO (4-6 h)
I 36 duplicati divergenti risolti **fondendo, mai cancellando** (la copia migliore vince, l'altra
diventa archivio d'origine con la ragione scritta) · `08-STREAM-S7-BOT` trattato come **archivio
d'origine** del bot, non come cartella vuota · il guasto di `census.py` riparato · i 5 ecosistemi
che puntano a reparti inesistenti corretti · `verify-agents` e `verify-skills` a verde ·
`empire doctor` a 0 bloccanti.
**Gate:** `empire doctor` block 0 · i due `verify-*` OK · `forge scan` e `registry census`
danno lo stesso numero.

### E2 — LA RINOMINA CHE VALE QUARANTA PUNTI (6-10 h)
Le 174 schede a un criterio dal pieno: `## Input / Output` → `## Ingresso` + `## Output`.
**Non è scrittura, è rinomina**, e va fatta con un programma che verifica una per una, non a mano.
**Gate:** `forge scan` → OPERATIVO ≥ 53,5% · nessun agente peggiorato (confronto prima/dopo).

### E3 — LA FETTA VERTICALE (12-18 h)
Un flusso solo, `WF-S1-CONCESSIONARI`: finestra di `empire flow` riaperta (è scaduta il 26
luglio, ed è **quella** la ragione per cui il contatore è a zero, non la mancanza di motore) ·
contratto C4 per i soli ~10 agenti che tocca · i 5 step da `start` a `done` · **le tracce scritte
da sole** · avviato da EMPERATOR per ordine.
**Gate:** `flow status` → 5/5 step chiusi · `trace stato` > 25 **senza intervento manuale** ·
un carico vero, non un `dry_run`.

### E4 — NEXUS (25-40 h, dopo l'ADR)
I cinque organi di §12. Prima N3 (l'emettitore unico) e N4 (il ledger), perché senza di loro
nessun altro scaglione è misurabile. Poi N1, N2, N5.
**Gate:** una traccia nasce da sola da un lavoro reale · il ledger registra il primo movimento ·
un handoff con carico vero attraversa il Bus.

### E5 — GLI ESECUTORI E I PUNTI D'INGRESSO (25-35 h)
15 direttori + MAXIMILIAN generati dalle schede · un comando per ecosistema che chiama il motore
vero · i registri diventano tabella di instradamento (N1) e smettono di essere solo verifica.
**Gate:** EMPERATOR ordina → un direttore esegue → l'uscita finisce dove il contratto dice.

### E6 — I TRE ECOSISTEMI SENZA MOTORE (da stimare in V2)
`09-OPERATIONS` (il ledger — ma se N4 è fatto, qui si aggancia) · `04-MARKETING` (**i gate APSOC
≥80/≥85 non hanno una sola funzione che li calcoli in tutto il repo**) · il ramo e-commerce di
`05-MULTI-BUSINESS`. Più le funzioni scoperte: A3/A4/A7/A8/A9/A10 di AGENCY, corso/lancio/funnel
di INFO-BUSINESS, CF-R6/CF-R7 di CONTENT-FACTORY, il registro forgiature di FORGE.

### E7 — LE ONDATE RESTANTI SUGLI AGENTI (30-45 h)
66 + 74 + 64 agenti, a ondate, con swarm **sequenziale per famiglia** (§18).

### E8 — LA CONSEGNA E GLI ORFANI (25-40 h)
I 4 libri KDP pubblicati (`libri_pubblicati/` contiene solo `.gitkeep`) · `empire estate` a
verdetto pieno · gli orfani per triage, con i 4.675 `vendored` esclusi per regola.

### E9 — L'AUTO-MIGLIORAMENTO
Solo quando E3+E4+E5 sono chiusi: prima non ci sono gli ingredienti.

## 23. La Tesoreria — fuori scaglione, perché è una riga

`entrate.jsonl` e `spese.jsonl` sono **zero byte tutti e due** dal 3 settembre, con motore, skill,
cinque agenti e tre leggi tutti presenti e funzionanti. **L'organo che deve dire quanto entra e
quanto esce è stato costruito e mai acceso.** Non serve uno scaglione: serve il primo movimento
registrato. Va agganciato a N4 (il ledger) e non va lasciato in fondo alla lista.

---

# PARTE VI — RISCHI, DECISIONI, AUTOCRITICA

## 24. I rischi

| # | Rischio | Mitigazione |
|---|---|---|
| R1 | **Il limite di sessione dell'account.** Nove episodi in tre mesi, e stanotte il decimo. `STATO-EMPIRE` lo dichiara condizione permanente | regola 4: **non si delega in quella forma finché la causa non è rimossa**. Produzione sequenziale, ricognizione parallela solo con scrittura incrementale |
| R2 | La specifica C4 sbagliata applicata 314 volte | è stata **letta nel codice**, non dedotta, e ha un collaudo per singolo agente (§8). E la fetta verticale (E3) la prova su 10 prima delle centinaia |
| R3 | NEXUS diventa un altro pezzo di carta | i suoi gate sono fatti reali: una traccia nata da sola, un movimento nel ledger, un carico vero nel Bus. Nessun gate documentale |
| R4 | Le sessioni parallele collidono | blocco ⚠️ COORDINAMENTO prima di ogni scaglione + numeri coniati dallo script |
| R5 | Si costruisce NEXUS e l'azienda continua a non incassare | E0 viene prima di tutto e dura 45 minuti |

## 25. Le decisioni che solo Max può prendere

1. **NEXUS nasce?** Serve un ADR (ADR-009 lo impone dal 14 in su). Senza, l'ecosistema non può essere creato.
2. **`08` e `12` sono lo stesso bot in due stadi**, e i loro documenti dicono di non andare live — aspettativa negativa, layer NFT bocciato 89 su 89. **Archiviare bene** è diverso da eliminare: è dargli il posto giusto e la ragione scritta. Decide Max.
3. Il prezzo del Manuale, ADR-023 sui LANCI, ADR-019 sul motore di orchestrazione: aperte da prima, non le sblocca questo piano.

## 26. L'obiezione più forte a questo piano

> *«Stai proponendo un sedicesimo ecosistema a un'azienda che non riesce a far funzionare i primi
> quindici. NEXUS sarà il sedicesimo pezzo di carta, e lo saprai fra tre mesi.»*

È l'obiezione giusta, ed è quella che questo Impero ha già meritato più volte:
l'Osservabilità è un README che descrive file mai creati; `14-TESORERIA` è una cartella con un
file e due sottocartelle vuote; lo swarm RuFLO **era teatro**, con i punteggi scritti a mano nel
generatore del rapporto.

**La risposta non è una promessa, è un vincolo:** NEXUS non ha un solo gate documentale. Non si
chiude quando i suoi file esistono — si chiude quando **una traccia è nata da sola**, quando
**il ledger ha registrato un movimento vero**, quando **un carico reale ha attraversato il Bus**.
Se quei tre fatti non accadono, NEXUS è fallito e va detto, non rinviato.

E c'è una prova a favore che non avevamo tre mesi fa: **la catena è già stata attraversata una
volta**, l'11 giugno, in 58 secondi. Manca il carico, non la strada.

## 27. Cosa V1 NON copre — materia per la critica

Dichiarato, non nascosto:

1. **La mappa completa dei passaggi di consegne** — `02b` è a 208 righe su un lavoro molto più grande. Non so ancora **quanti** collegamenti l'Impero abbia progettato, né quali ecosistemi siano isolati.
2. **Il censimento dei motori è al 20%** — `04` copre la sola famiglia Outreach, `04b` è a 115 righe. **Non so ancora quanti motori reali abbiamo, quanti girano, quanti sono orfani.** È un buco grosso: il piano parla di «avvolgere i motori» senza averli contati tutti.
3. **Le tre sintesi degli organi** (chi non è chiamato da nessuno, gli articoli del Mandato, le voci aperte del registro errori) mancano: il doom bot è caduto prima.
4. **Il modulo d'ingaggio e l'addestramento** sono abbozzati in §19-20, non progettati: il doom bot non è mai partito.
5. **Le ore degli scaglioni E6 e E7** sono stime grosse, non calcoli.
6. **Non ho ancora messo alla prova la definizione di «vivo»** contro i 15 ecosistemi uno per uno: so che 2 passano, non so esattamente cosa manca agli altri 13 in termini di V-a..V-d.

---

> **Fine di V1.** Ora questa versione va **demolita** da revisori indipendenti su modello diverso
> (ADR-017). Il critico non cerca lo stile: cerca il difetto che costerebbe caro, e per ogni
> rilievo deve dire **dove** il piano si romperebbe e **con quale conseguenza**.
