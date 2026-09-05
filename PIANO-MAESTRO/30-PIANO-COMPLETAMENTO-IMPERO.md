# 🏛️ DOSSIER 30 — PIANO DI COMPLETAMENTO DELL'IMPERO

> **Emesso:** 2026-09-05 · **Autore:** EMPERATOR su ordine di Max
> **Origine:** [TASK-MAX-20260831-IMPERO-OPERATIVO](../company/Memory/tasks/TASK-MAX-20260831-IMPERO-OPERATIVO.md)
> **Governo:** ADR-002 (memory-first) · ADR-003 (wrap, mai riscrittura) · ADR-005 (backlog non blocca)
> · ADR-006 (ciclo a 9 passi) · ADR-008 (nessun artefatto orfano) · ADR-016 (ultimo metro)
> **Stato:** PROPOSTO — attende il via di Max
>
> **Tutti i numeri di questo dossier sono stati MISURATI il 2026-09-05 lanciando i comandi.**
> Nessuna cifra è ricordata, stimata o copiata dalla task di agosto. Dove un numero è un
> giudizio e non una misura, è scritto che lo è.

---

## 1. LA RISPOSTA IN UNA RIGA

**Digital Empire è costruita al 92% sulla carta e viva al 18%.**

Il 92% è l'organigramma: 15 ecosistemi, 82 reparti, 77 workflow definiti, 853 file di agente,
il Mandato, il Board, le Guilds, le Sentinelle, la Memory, i registri. Esiste, è coerente,
è navigabile.

Il 18% è quanto di quell'organigramma **esegue davvero** quando gli si dà un ordine.

La distanza fra i due numeri **è** l'enorme task che Max ricordava. Ha già un nome e un
documento: `TASK-MAX-20260831-IMPERO-OPERATIVO`, nove blocchi B0..B8. Questo dossier non la
sostituisce: la **misura oggi**, ne **corregge l'ordine** dove l'ordine sbagliato costerebbe
settimane, e la trasforma in un piano con scaglioni, gate e ore.

---

## 2. IL FATTO PIÙ SCOMODO, DETTO PER PRIMO

La task fu emessa il **31 agosto**. Sono passati **cinque giorni di lavoro pieno**.
Ecco le stesse misure allora e adesso, lanciate con gli stessi comandi:

| Misura | Comando | 31/08 | **05/09** | Bersaglio |
|---|---|---|---|---|
| Agenti operativi | `empire forge scan` | 58/436 (13,3%) | **61/439 (13,9%)** | 439/439 |
| Agenti senza contratto d'uscita (C4) | `empire forge scan` | 314 (72%) | **314 (71,5%)** | 0 |
| Agenti invocabili | `ls .claude/agents/` | 0 | **129** ✅ | Board+direttori+Sentinelle |
| Step di workflow chiusi | `empire flow status` | 0 su 10 | **0 su 10** | >0 su tutti e 10 |
| Tracce registrate in tutta la vita | `empire trace stato` | 25 | **25** | continue |
| Artefatti orfani bloccanti | `empire registry orphans` | 9.913 | **9.911** | 0 |
| Problemi bloccanti di conformità | `empire doctor` | 2 block | **2 block** | 0 |
| Ecosistemi con codice eseguibile | `find -name '*.py'` | 3 su 14 | **4 su 15** | 15 su 15 |
| Canali pronti a partire adesso | `empire controllo` | 2 su 6 | **2 su 6** | 6 su 6 |
| Verdetto Workflow Estate | `empire estate` | NON FINITO (2) | **NON FINITO (2)** | FINITO |
| Suite del runtime di governo | `pytest empire/tests` | 236 passed | **236 passed** ✅ | resta verde |

**Nove misure su undici sono ferme. Una sola si è mossa davvero: gli agenti invocabili,
da 0 a 129** — ed è esattamente il lavoro che Max ricorda («abbiamo preso ufficiali tutte le
skill e tutti gli agenti»). Quel lavoro è reale e vale: ha prodotto `verify-agents.py`,
`verify-skills.py`, `registro-agenti.yaml`, `skills-map.yaml` e ha chiuso metà del blocco B2.

Gli altri cinque giorni sono andati in **studio, PDF, brand guidelines, piano LANCI v4,
Tesoreria, Ultimo Metro**. Nessuna di quelle cose è sprecata. Ma **nessuna di quelle cose
sposta l'ago dell'azienda viva**, ed è la stessa forma di guasto che ADR-016 ha già chiamato
per nome: *si produce e non si consegna*. La carta cresce più veloce del motore.

Questa è la diagnosi. Il piano che segue esiste per invertirla.

---

## 3. COME È CALCOLATO IL 18% (nessun numero regalato)

Dieci gate, peso uguale, ognuno misurato col suo comando.

| Blocco | Gate | Misura di oggi | % |
|---|---|---|---|
| **STRUMENTO ZERO** — EMPERATOR | nome→attiva · risponde coi numeri misurati · avvia 1 workflow reale | 2 su 3: attiva ✅, misura ✅, **non ha mai avviato un workflow end-to-end** ❌ | **67%** |
| **B0** — Igiene e sicurezza | `doctor` 0 block · 3 credenziali revocate | SYNC-CONFLICT chiuso ✅ · doctor ancora **2 block** · BACKLOG **ancora duplicato** (B-001 compare 2 volte) · **3 credenziali ancora vive sul repo pubblico** | **20%** |
| **B1** — Contratto d'uscita | `forge scan` C4 mancante = 0 | **314 agenti su 439 non dichiarano cosa producono** | **0%** |
| **B2** — Agenti invocabili | Board + 15 direttori + 5 Sentinelle + MAXIMILIAN chiamabili | Board 7/7 ✅ · Sentinelle 5/5 ✅ · EMPERATOR ✅ · CONOSCENZA-EMPIRE ✅ · **direttori 0/15** ❌ · **MAXIMILIAN 0** ❌ · **i registri non li legge nessun processo** ❌ | **40%** |
| **B3** — Flow vivo | step chiusi >0 su 10/10 · tracce automatiche | **0 step chiusi su 10 workflow**, finestra ferma al **26 luglio**, 25 tracce in tutta la vita del sistema | **0%** |
| **B4** — Codice nei 15 ecosistemi | 15/15 con punto d'ingresso + test verde | codice presente in **4** (02: 566 py · 11: 161 · 12: 31 · 13: 1). **Zero ecosistemi con un comando dichiarato che parte e ha un test** | **7%** |
| **B5** — Zero orfani | `registry orphans` block 0 | **9.911 bloccanti su 22.466 rilievi** | **0%** |
| **B6** — Sei canali | `controllo` 6/6 | **2/6.** Instagram sessione **93 giorni**, LinkedIn **110 giorni**, YouTube senza `.mp4`, Incasso senza Payment Link | **33%** |
| **B7** — Consegna reale | `estate` FINITO · 4 libri pubblicati | 2 controlli rossi (case study Novacar assente, 1 block di conform) · `libri_pubblicati/` contiene **solo `.gitkeep`** | **10%** |
| **B8** — Auto-miglioramento | 1 evoluzione proposta dal sistema e applicata | non iniziato | **0%** |

**Media: 177 / 10 = 17,7% → 18%.**

Il 92% della carta è misurato a parte: 13 ecosistemi su 15 hanno `ECOSISTEMA.md` + `BACKBONE.md`
(mancano `08-STREAM-S7-BOT`, che è un duplicato vuoto, e `14-TESORERIA`), 170 skill su 172
censite in `skills-map.yaml`, 158 agenti su 164 censiti in `registro-agenti.yaml`.

---

## 4. IL DIFETTO NELL'ORDINE DELLA TASK DI AGOSTO

La task mette **B1 (contratto d'uscita su 439 agenti)** subito dopo l'igiene, e lo chiama
«il collo di bottiglia dell'intero Impero». La diagnosi è giusta. **L'ordine no.**

B1 su 439 agenti è il blocco **più lungo di tutti** — 314 file da toccare, decine di ore, con
uno standard che **nessuno ha ancora provato su un caso vero**. Metterlo per primo significa
scrivere 314 contratti prima di sapere se il contratto funziona. Se lo standard è sbagliato,
lo si scopre alla fine e si riscrive tutto.

E la task stessa contiene già la contro-mossa, scritta in B3.1: *«un ciclo vero vale più di
dieci definiti»*. **Un solo workflow end-to-end tocca ~8-10 agenti**, non 439: basta dare il
contratto a quei dieci per provare l'intera catena — contratto → esecutore → flow → traccia →
uscita — e per chiudere il terzo gate di EMPERATOR, oggi l'unico aperto.

**Correzione, ed è l'unica modifica strutturale che questo dossier fa alla task:**
la fetta verticale (un workflow vero) viene **prima** della scala orizzontale (439 contratti).
Prima si prova che la catena regge sotto peso, poi la si allarga con lo swarm.

Costo ombra della correzione, dichiarato: si ritarda di ~2 settimane il momento in cui tutti
gli agenti sono concatenabili. Si guadagna la certezza che lo standard sia giusto prima di
applicarlo 314 volte, e un ciclo di revenue vero acceso settimane prima.

---

## 5. IL SECONDO FATTO CHE CAMBIA LE PRIORITÀ

**L'azienda oggi non può incassare un euro.** Non è una metafora: `empire controllo` dice
INCASSO = *tier 2, solo ordine via mail*, nessun Payment Link. È lo stesso fatto che ha
demolito le prime tre versioni del piano LANCI e che ha fatto scrivere nella v4 che il primo
giorno non è «crea la cartella» ma **«incassa un euro vero e rimborsalo»**.

Ne discendono due conseguenze operative:

1. **I quattro atti di Max valgono più di quaranta ore mie.** 2 Payment Link Stripe, login
   Instagram, login LinkedIn, rotazione di 3 credenziali: **circa 45 minuti delle sue mani**
   portano `empire controllo` da 2/6 a 5/6 e chiudono metà di B0. Nessun agente li può fare al
   posto suo. Vanno in cima al piano, non in fondo.
2. **I primi due scaglioni del piano LANCI e il blocco B6 sono la stessa cosa.** LANCI
   scaglione 1-2 non contiene una riga di codice: è esattamente «apri il canale di incasso e
   provalo». Farli due volte sarebbe lavoro doppio. **Si fondono qui, in S1.**

---

## 6. IL PIANO — SETTE SCAGLIONI

> Regola: uno scaglione è chiuso **solo** quando il suo comando dà l'output atteso.
> Mai per dichiarazione. Se non chiude, si dice **perché** — non si sposta il gate.
> Ogni scaglione segue il ciclo a 9 passi (ADR-006). Prima di ogni scaglione con swarm:
> blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md` + push, così Gael e Neri non collidono.

### S1 — I QUATTRO ATTI DI MAX + IGIENE (chiude B0, porta B6 a 5/6)
**Ore: 45 min di Max · 4-6 h mie · nessuna dipendenza — parte oggi**

**Solo Max, in quest'ordine (l'ordine conta):**
1. **Ruotare le 3 credenziali esposte sul repo PUBBLICO** — B-020 chiave Brevo (in `HEAD` dal
   commit iniziale), B-021 password Arena + `OPENROUTER_API_KEY` (**verificata ancora viva**),
   B-023 password Instagram. Toglierle dal codice **non basta**: la storia git pubblica resta
   leggibile, vanno **revocate e rigenerate sui servizi**.
2. **Login Instagram** (`refresh_session.py`) — *dopo* il cambio password, o la sessione appena
   creata nasce morta.
3. **Login LinkedIn** — 1 minuto.
4. **2 Payment Link Stripe** — è l'unico atto che trasforma l'azienda in una che può incassare.

**Mie, in parallelo:** riparare il link morto in `preventivo-template.md:10`; fondere
`08-STREAM-S7-BOT` (cartella vuota) in `12-STREAM-S7-BOT` — sana la violazione ADR-001 e il
duplicato di numerazione; deduplicare il blocco `B-001..B-012` in `BACKLOG.md`; censire
`tesoreria` e `ultimo-metro` in `skills-map.yaml` e i 6 agenti mancanti in
`registro-agenti.yaml` (fa tornare verdi anche `verify-skills` e `verify-agents`).

```
GATE S1:  empire doctor      -> block: 0
          empire controllo   -> 5/6  (resta solo YOUTUBE, che aspetta l'.mp4)
          verify-agents.py   -> GATE AGENTI: OK
          verify-skills.py   -> GATE SKILL: OK
          la vecchia chiave OpenRouter risponde 401
```

---

### S2 — LA FETTA VERTICALE: un ciclo vero, uno solo (chiude B3.1, chiude EMPERATOR)
**Ore: 12-18 · dipende da S1 · nessuno swarm (è una fetta stretta e profonda)**

Un workflow, scelto: **`WF-S1-CONCESSIONARI`** — owner Max, 5 step, ha già un motore vero
dietro (Preventa/outreach, che gira davvero) ed è l'unico che tocca il denaro.

1. Riaprire la finestra di `empire flow` (è scaduta il **26 luglio**: finché resta scaduta
   nessuno step può chiudersi, ed è il motivo per cui il contatore è a zero da luglio).
2. Scrivere il **contratto d'uscita C4 solo per gli agenti che questo workflow tocca** (~8-10),
   secondo uno standard unico che qui nasce e qui viene provato.
3. Farlo passare da `start` a `done`, tutti e 5 gli step, con le 5 tracce scritte
   **automaticamente** — non a mano.
4. **EMPERATOR lo avvia lui**, per ordine, dall'inizio alla fine: è il terzo gate dello
   STRUMENTO ZERO, oggi l'unico aperto dal 31 agosto.

```
GATE S2:  empire flow status  -> WF-S1-CONCESSIONARI 5/5 step chiusi, finestra corrente
          empire trace stato  -> totale > 25, cresciuto senza intervento manuale
          EMPERATOR riceve un ordine e il ciclo parte, gira e finisce
```

**Perché è lo scaglione più importante dei sette:** è il primo momento nella storia
dell'Impero in cui un ordine entra da una parte ed esce dall'altra. Tutto il resto del piano
è replicare questo su scala.

---

### S3 — CONTRATTO D'USCITA A ONDATE (chiude B1)
**Ore: 30-45 · dipende da S2 (lo standard dev'essere già provato) · SWARM OBBLIGATORIO**

**Passo zero, prima di toccare un file:** `empire forge scan` conta **439** agenti,
`empire registry census` ne conta **69**. Due strumenti dello stesso runtime che contano la
stessa cosa in modo diverso: **uno dei due mente**. Va deciso quale ha ragione prima che
EMPERATOR si fidi di uno dei due — altrimenti si scrivono 314 contratti dentro un censimento
sbagliato.

Poi lo standard di S2 si applica a ondate, **senza saltare nessuno** (principio di Max:
niente si scarta):
- **Onda A — 61 agenti OPERATIVI:** consolidare, verificare che il contratto sia vero.
- **Onda B — 324 PARZIALI:** qui sta il 72% del debito. L'ondata più grande, tutta a swarm.
- **Onda C — 54 DOCUMENTALI:** i più poveri. Non si buttano: si portano al livello degli altri.

```
GATE S3:  empire forge scan  -> C4-uscita mancante: 0   ·   OPERATIVO 439/439
          forge scan e registry census danno lo STESSO numero di agenti
```

---

### S4 — ESECUTORI E PUNTI D'INGRESSO (chiude B2 e B4)
**Ore: 25-35 · dipende da S3 · SWARM OBBLIGATORIO (aree disgiunte)**

Due lavori che si tengono per mano e vanno fatti insieme:

**B2, la metà che manca.** Oggi sono invocabili Board (7), Sentinelle (5), EMPERATOR e
CONOSCENZA-EMPIRE. Mancano i **15 direttori di ecosistema** e **MAXIMILIAN** (il gate 5-bis).
Vanno **generati dalle definizioni**, non riscritti a mano: le **853** definizioni in `company/`
(misurate oggi: file `.md` il cui percorso contiene «agent») sono buona prosa e restano la fonte
di verità (ADR-003). E `skills-map.yaml` +
`REGISTRO-IMPRESA.md` devono smettere di essere registri che nessun processo legge: diventano
**la tabella di instradamento che EMPERATOR interroga per sapere chi chiamare**.

**B4, il punto d'ingresso.** Non è vero che gli 11 ecosistemi di sola carta non fanno niente:
i loro motori esistono e vivono **fuori**, nelle cartelle storiche (`Outreach Workflow` 238 py,
`YOUTUBE-AUTOMATION-FACTORY` 91 py, `caroselli - agency` 53 py). ADR-003 dice che **restano
dove sono**. Il lavoro non è spostare codice: è dare a ogni ecosistema **un comando che parte,
chiama il motore vero dov'è, e restituisce l'uscita dichiarata in S3**.

```
GATE S4:  ls .claude/agents/  -> 15 direttori + MAXIMILIAN presenti
          per ognuno dei 15 ecosistemi: un comando che parte, produce l'uscita, test verde
          prova reale: EMPERATOR ordina -> un direttore esegue -> l'uscita finisce dove il contratto dice
```

---

### S5 — TUTTI E DIECI I WORKFLOW (chiude B3)
**Ore: 20-30 · dipende da S4**

Quello che S2 ha fatto su uno, qui si fa su tutti: WF-MASTER, WF-MEM-EOD, WF-MEM-RETRO,
WF-PERF-LOOP, WF-S1..S6. Nessuno escluso. E le tracce diventano continue: **25 tracce in tutta
la vita del sistema** significa che il ReasoningBank non ha memoria di lavoro. Ogni ciclo deve
lasciare le sue 5 tracce da solo.

```
GATE S5:  empire flow status  -> step chiusi > 0 su TUTTI e 10, finestra corrente
          empire trace stato  -> cresce a ogni ciclo, senza intervento manuale
```

---

### S6 — CONSEGNA REALE E ZERO ORFANI (chiude B7 e B5)
**Ore: 25-40 · B7 dipende da S1 · B5 in parallelo, SWARM**

**B7 — la fabbrica deve consegnare, non solo produrre** (è ADR-016 applicata):
- **4 libri KDP** scritti, 24/24 capitoli, tre con `pubblicabile: True`, zero bloccanti — e
  `libri_pubblicati/` contiene **solo `.gitkeep`**. Zero pubblicati = zero vendite = zero dati
  su nicchia, prezzo, copertina.
- **`empire estate` a verdetto pieno**: mancano il case study Novacar e 1 block di conform.
- Il video YouTube renderizzato in `.mp4` — è l'ultimo canale che resta a 5/6 dopo S1.

**B5 — zero orfani, ma per triage, non per forza bruta:** dei 22.466 rilievi, **4.675 sono
`vendored`** (dipendenze di terzi: vanno **esclusi dalla regola**, non collegati). Il numero
vero da collegare è molto più piccolo di 9.911. Prima si separa per tipo, poi si collega, poi
il pre-commit impedisce di crearne di nuovi (stessa forma del guard di ADR-013, che ha già
fermato un PDF da 44 MB diretto nella storia).

```
GATE S6:  empire estate            -> FINITO (exit 0)
          libri_pubblicati/        -> 4 libri, non un .gitkeep
          empire controllo         -> 6/6
          empire registry orphans  -> block: 0  (vendored esclusi per regola, non per eccezione)
```

---

### S7 — AUTO-MIGLIORAMENTO (chiude B8, è F10 della roadmap)
**Ore: 10-15 · dipende da S3+S4+S5**

Max: *«quando sarà finita, l'azienda continuerà ad automigliorarsi.»* Con S1..S6 chiusi
l'Impero ha finalmente i tre ingredienti che F10 richiede e che **oggi mancano tutti e tre**:
agenti con contratto (S3), esecutori reali (S4), tracce continue (S5).
Loop: osserva → giudica → distilla → agisci → predici.

```
GATE S7:  almeno un'evoluzione organizzativa proposta DAL SISTEMA — non da Max, non da me — e applicata
```

---

## 7. ORDINE, DIPENDENZE, TEMPI

```
  S1  ATTI DI MAX + IGIENE            45 min di Max  +  4-6 h        [parte oggi]
   |
   v
  S2  FETTA VERTICALE (un ciclo vero) 12-18 h        [qui EMPERATOR comanda davvero]
   |
   +-------------------+
   v                   |
  S3  CONTRATTI 439    | 30-45 h  swarm
   |                   |
   v                   |
  S4  ESECUTORI + PUNTI D'INGRESSO  25-35 h  swarm
   |                   |
   v                   v
  S5  TUTTI I WF   20-30 h      S6  CONSEGNA + ORFANI  25-40 h  swarm   [in parallelo da S1]
   |                   |
   +--------+----------+
            v
  S7  AUTO-MIGLIORAMENTO  10-15 h
```

| Scaglione | Ore | Chiude | Effetto misurabile |
|---|---|---|---|
| S1 | 45 min Max + 4-6 h | B0, metà B6 | doctor 0 block · controllo 2/6 → **5/6** · l'azienda **può incassare** |
| S2 | 12-18 h | B3.1, EMPERATOR 3/3 | flow **0 → 1 workflow chiuso** · tracce ripartono |
| S3 | 30-45 h | B1 | C4 mancante **314 → 0** · censimenti riconciliati |
| S4 | 25-35 h | B2, B4 | direttori **0 → 15** · ecosistemi eseguibili **4 → 15** |
| S5 | 20-30 h | B3 | step chiusi **0 → >0 su 10/10** |
| S6 | 25-40 h | B7, B5 | libri **0 → 4** · orfani **9.911 → 0** · estate FINITO · controllo **6/6** |
| S7 | 10-15 h | B8 | l'azienda si migliora da sola |
| **Totale** | **127-189 h** | **B0..B8** | **18% → 100%** |

**A regime di lavoro pieno: 4-6 settimane.** A regime attuale — cinque giorni per zero misure
mosse — non finisce mai. La differenza non è la capacità: è **cosa si sceglie di aprire ogni
mattina**. Per questo S1 è di 45 minuti e va fatto oggi.

---

## 8. COSA NON ENTRA IN QUESTO PIANO, E PERCHÉ

- **ECOSISTEMA LANCI (15°, piano v4, 118-174 h).** Il piano è pronto e buono e aspetta l'ok di
  Max su ADR-023. **Non parte prima di S2.** Motivo: aggiungerebbe un quindicesimo ecosistema
  di carta sopra un'azienda viva al 18%, cioè peggiorerebbe esattamente il rapporto che questo
  piano esiste per raddrizzare. I suoi **scaglioni 1-2 sono già dentro S1** (sono il canale di
  incasso), quindi la parte che produce valore subito **non è rimandata**: è solo chiamata con
  un altro nome.
- **Lo studio delle 167 lezioni AI TUBE PRO (EMP-V6DE, 5/167 = 3%).** Va avanti, ma è
  formazione, non costruzione. Non compete per le stesse ore di S1-S2.
- **La Fase 2 di EMP-QQ2R** (implementare i consigli dei 17 video): resta rimandata per ordine
  esplicito di Max. Molti di quei consigli **cadranno dentro S3/S4** in modo naturale.
- **Le 4 decisioni aperte del piano LANCI** (prezzo del Manuale, chiave di posta, ADR-023,
  ADR-019): la seconda è dentro S1. Le altre tre restano decisioni di Max, non lavoro mio.

---

## 9. I TRE RISCHI, DETTI PRIMA E NON DOPO

1. **Lo standard C4 nasce sbagliato e ce ne si accorge alla 314ª applicazione.**
   *Mitigazione:* è precisamente perché questo rischio esiste che S2 viene prima di S3. Lo
   standard si prova su 10 agenti veri dentro un ciclo vero prima di toccarne 314.
2. **Le sessioni scadono di nuovo mentre si costruisce.** Instagram e LinkedIn sono già a 93 e
   110 giorni. Se S1 slitta di altre settimane, i login vanno rifatti due volte.
   *Mitigazione:* S1 oggi, 45 minuti.
3. **Le sessioni parallele collidono.** Il 5 settembre sono già collisi due numeri nello stesso
   giorno (ADR-022 e CP-018), fra questa chat e un'altra.
   *Mitigazione:* blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md` + push **prima** di ogni
   scaglione, e numero verificato libero **nel momento in cui si scrive**, mai a memoria.

---

## 10. L'OBIEZIONE PIÙ FORTE A QUESTO PIANO

*«Stai proponendo 127-189 ore per far girare una macchina che nessun cliente ha chiesto.
In quelle stesse ore Max potrebbe fare outreach a mano e incassare davvero.»*

È vera in parte, e va risposta con onestà: **S1 e S6 producono denaro, S3-S4-S5-S7 producono
capacità.** Se l'obiettivo fossero i prossimi mille euro, il piano giusto sarebbe S1 + S6 e
basta, ~30 ore.

Ma l'ordine di Max del 31 agosto era esplicito e non è cambiato: *«non scartiamo niente, non
rinunciamo a niente, tutto collegato, attivo, funzionante alla perfezione»* — e
*«quando sarà finita, l'azienda continuerà ad automigliorarsi»*. Quello non si compra con
trenta ore di outreach manuale.

**La sintesi che tiene insieme le due cose, ed è la forma in cui il piano è ordinato sopra:**
S1 apre l'incasso in 45 minuti, S2 prova la catena in due giorni, e **da S2 in poi ogni
scaglione successivo gira mentre l'azienda incassa**, non prima che incassi.

---

## 11. IL PRIMO PASSO, ADESSO

**Max, quattro atti tuoi. Quarantacinque minuti. Nessuno li può fare al posto tuo:**

1. Revocare e rigenerare la **chiave Brevo** (B-020) — è in `HEAD` dal commit iniziale.
2. Cambiare **password Arena + chiave OpenRouter** (B-021) — la OpenRouter è **viva adesso**.
3. Cambiare **password Instagram** (B-023) → **poi** rifare il login IG, in quest'ordine.
4. Creare **2 Payment Link Stripe** → l'azienda passa da «non può incassare» a «può».

Nello stesso tempo io chiudo l'igiene mia e porto `empire doctor` a zero bloccanti.
Da lì, S2: **il primo ordine nella storia dell'Impero che entra da una parte ed esce
dall'altra.**
