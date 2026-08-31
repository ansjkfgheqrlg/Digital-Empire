# TASK-MAX-20260831 — IMPERO OPERATIVO

> **Destinatario:** MAX (con Claude/EMPERATOR come esecutore operativo)
> **Emessa:** 2026-08-31 · **Origine:** [AUD-20260831-001](../audit/AUD-20260831-001.md) — audit generale eseguito, non letto
> **Governo:** ADR-002 (memory-first) · ADR-003 (wrap, mai riscrittura) · ADR-005 (backlog non blocca) · ADR-006 (ciclo a 9 passi)
> **Stato:** APERTA

---

## PRINCIPIO VINCOLANTE — NIENTE SI SCARTA

Direttiva esplicita di Max (2026-08-31):

> *"Non scartiamo niente, non rinunciamo a niente. Facciamo in modo che tutto sia come deve
> essere, come era stato pianificato. Tutto collegato, attivo, funzionante alla perfezione."*

**Conseguenza operativa, che vale per ogni blocco qui sotto:**
- Nessun agente viene cancellato perche' "documentale". Viene **reso operativo**.
- Nessun ecosistema viene declassato perche' "e' solo carta". Riceve **il suo codice**.
- Nessun workflow viene chiuso perche' "non e' mai partito". Viene **fatto partire**.
- L'unica rimozione ammessa e' il **duplicato accidentale** (es. il blocco B-001..B-012
  duplicato in BACKLOG.md, o l'ecosistema `08-STREAM-S7-BOT` vuoto che duplica
  `12-STREAM-S7-BOT`). Duplicato != scarto: si fondono, non si buttano.

**Regola di gate:** un blocco e' chiuso solo quando il suo comando di verifica da' l'output
atteso. Mai per dichiarazione. Se un blocco non chiude, si dice **perche'**, non si sposta
il gate.

---

## STATO DI PARTENZA — misurato il 2026-08-31

| Misura | Comando | Oggi | Bersaglio |
|---|---|---|---|
| Agenti operativi | `empire forge scan` | **58 / 436 (13.3%)** | 436 / 436 |
| Agenti senza contratto d'uscita (C4) | `empire forge scan` | **314 (72%)** | 0 |
| Agenti realmente invocabili | `ls .claude/agents/` | **0** | Board + direttori + Sentinelle |
| Step di workflow chiusi | `empire flow status` | **0 su 10 workflow** | > 0 su tutti e 10 |
| Tracce registrate in tutta la vita | `empire trace stato` | **25** | continue, una per ciclo |
| Artefatti orfani bloccanti | `empire registry orphans` | **9.913 block / 22.469 tot** | 0 block |
| Problemi bloccanti di conformita' | `empire doctor` | **2 block** | 0 block |
| Ecosistemi con codice eseguibile | `find -name '*.py'` | **3 su 14** | 14 su 14 |
| Canali pronti a partire adesso | `empire controllo` | **2 su 6** | 6 su 6 |
| Verdetto Workflow Estate | `empire estate` | **NON FINITO (2 controlli)** | FINITO |
| Suite del runtime di governo | `pytest empire/tests` | **236 passed** | resta verde |

**Diagnosi in una riga:** i motori sono veri, la governance e' vera e misurabile, ma **non
esiste un punto in cui un ordine entra e attraversa l'azienda**. Manca lo strato che unisce.

---

## STRUMENTO ZERO — EMPERATOR (si costruisce per primo)

EMPERATOR non e' un blocco del piano: e' **lo strumento con cui il piano si esegue**.
Max lavorera' solo con lui. Va costruito prima di B0.

**Requisiti (direttiva Max):**
- Agente ufficiale, con **hook ufficiale**: basta il suo nome in una frase e si attiva.
- Conosce **tutto**: azienda, second-brain, Memory, ADR, stato, backlog, ecosistemi, motori.
- Tono **nettamente diverso** da qualunque altro agente: carismatico, egocentrico,
  sapientone, riconoscibile alla prima riga. Il tono e' un requisito, non un vezzo.
- Sta **sopra tutto**: attiva reparti, workflow, mandati, task. Nessun limite di ambito.
- Dice sempre **cosa ha misurato**, mai cosa crede. L'arroganza e' permessa; la finzione no.

**Gate STRUMENTO ZERO:**
1. Il nome in una frase qualsiasi lo attiva (hook verificato con una prova reale).
2. Risponde a "a che punto siamo" citando numeri presi dai comandi, non dai file.
3. Sa avviare almeno un workflow reale end-to-end.

---

## BLOCCO 0 — IGIENE E SICUREZZA

> Viene prima di tutto. Contiene l'unica esposizione **attiva**, non un debito tecnico.
> Alcuni passi li puo' fare **solo Max**: nessun agente puo' ruotare una credenziale al posto suo.

**0.1 — Ruotare le tre credenziali esposte sul repo PUBBLICO** *(solo Max)*
- **B-020** — chiave API Brevo. Presente dal commit iniziale `57a0ba0b`.
- **B-021** — password account Arena + `OPENROUTER_API_KEY` (verificata **ancora viva**).
- **B-023** — password Instagram `digitalempireagency.e`.

Togliere dal codice **non basta**: la storia git pubblica resta leggibile. Vanno **revocate e
rigenerate** sui rispettivi servizi, poi spostate su `.env` (gia' gitignorato).
**Ordine che conta:** cambiare la password Instagram **prima** del login una tantum, o la
sessione appena creata viene invalidata.

**0.2 — Chiudere il conflitto di sync**
`SYNC-CONFLICT.txt` e' attivo: un commit e' bloccato dal pre-commit, lavoro non pushato.
Risolvere, pushare, cancellare il file.

**0.3 — Deduplicare BACKLOG.md**
Il blocco `B-001..B-012` compare **due volte** (artefatto di merge). Fondere, non tagliare.

**0.4 — Portare `empire doctor` a 0 bloccanti**
- Link morto: `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md:10` punta a
  `Clienti/Prof Autocad/preventivo-forge/templates/preventivo.html`, che non esiste.
  Correggere il riferimento **o creare l'artefatto** (principio: niente si scarta).
- **ADR-001 violato**: due ecosistemi numerati `08` — `08-INTELLIGENCE` (16 md, 0 py) e
  `08-STREAM-S7-BOT` (**cartella vuota**, duplica `12-STREAM-S7-BOT`).
  Fusione del duplicato vuoto, non cancellazione di contenuto.

**GATE B0:**
```
empire doctor          -> block: 0
git status             -> pulito, SYNC-CONFLICT.txt assente
```
E le 3 credenziali risultano **revocate sui servizi** (verifica: la vecchia chiave OpenRouter
risponde 401), non solo tolte dal codice.

---

## BLOCCO 1 — CONTRATTO D'USCITA UNIVERSALE

> Questo e' **il collo di bottiglia dell'intero Impero**. Finche' 314 agenti su 436 non
> dichiarano cosa producono, nessun orchestratore — EMPERATOR compreso — puo' concatenarli:
> sceglie un agente e poi non sa cosa gli torna in mano. E' la stessa classe di guasto gia'
> trovata tre volte nel repo (`push_social.py` che stampa un successo simulato ed esce 0,
> `main_orchestrator.py` che dichiara "FLUSSO COMPLETATO" senza guardare l'esito).

**1.1 — Definire lo standard di uscita**
Uno schema unico, scritto una volta, valido per tutti e 436: cosa produce l'agente, in che
forma, dove lo scrive, come si capisce se ha fallito. Non un template decorativo: il campo
che `empire forge` legge come **C4-uscita**.

**1.2 — Applicarlo a ondate, senza saltare nessuno**
- **Onda A — 58 agenti OPERATIVI**: consolidare, verificare che il contratto sia vero.
- **Onda B — 324 agenti PARZIALI**: e' qui che sta il 72% del debito. Ondata piu' grande.
- **Onda C — 54 agenti DOCUMENTALI**: i piu' poveri. **Non si buttano**: si portano al
  livello degli altri. Sono i primi candidati allo swarm (ADR-006).

**1.3 — Riconciliare i due censimenti**
`empire forge scan` conta **436 agenti**, `empire registry census` ne conta **69**.
Due strumenti dello stesso runtime che contano la stessa cosa in modo diverso: uno dei due
mente. Va deciso quale ha ragione **prima** che EMPERATOR si fidi di uno dei due.

**GATE B1:**
```
empire forge scan  ->  OPERATIVO 436 (100%),  C4-uscita mancante: 0
```
E i due censimenti danno **lo stesso numero di agenti**.

---

## BLOCCO 2 — AGENTI REALMENTE INVOCABILI

> Oggi `company/` contiene **792 file di agenti**. `.claude/agents/` di progetto ne contiene
> **0**. Nessun agente Empire — ne' il CEO, ne' il COO, ne' una Sentinella, ne' un direttore
> di ecosistema — e' oggi chiamabile. Esistono come organigramma, non come esecutori.

**2.1 — Ponte definizione → esecutore**
Da `company/.../agente.md` a un agente che si puo' davvero invocare. Generato dalla
definizione, **non riscritto a mano**: le 792 definizioni sono buona prosa e restano la fonte
di verita' (ADR-003).

**2.2 — Ordine di attivazione (nessuno escluso, ma un ordine c'e')**
1. **Board C-Suite** (CEO, COO, CTO, CMO, CRO, CFO, Chief-Forge) — sono quelli che EMPERATOR chiama per primi.
2. **Direttori dei 14 ecosistemi**.
3. **5 Sentinelle** always-on (Cost, Quality, Drift, Security, Brand-Voice).
4. **MAXIMILIAN** (gate 5-bis).
5. Tutti i reparti L2/L3/L4, a scendere.

**2.3 — Chiudere il ponte con il registro**
`skills-map.yaml` e `REGISTRO-IMPRESA.md` oggi sono registri **che nessun processo legge**.
Devono diventare la tabella di instradamento che EMPERATOR interroga per sapere chi chiamare.

**GATE B2:**
```
ls .claude/agents/   -> Board + 14 direttori + 5 Sentinelle + MAXIMILIAN presenti
```
Prova reale: EMPERATOR riceve un ordine, chiama un direttore di ecosistema, il direttore
produce l'output dichiarato in B1, e l'output finisce dove il contratto dice.

---

## BLOCCO 3 — IL SISTEMA NERVOSO CHE TRASPORTA DAVVERO

> `empire flow` esiste, ha 10 workflow, 6 gate e 3 decisioni definiti. Ha **0 step chiusi
> su tutti e 10**, con la finestra ferma al 2026-07-26. Il motore c'e' e non ha mai
> trasportato un solo passo reale.

**3.1 — Un ciclo vero, uno solo, end-to-end**
Scegliere **un** workflow (candidato: `WF-S1-CONCESSIONARI`, owner Max, 5 step, ha gia' un
motore vero dietro — Preventa/outreach). Farlo passare da `start` a `done` con tutti gli
step chiusi e le tracce scritte. **Un ciclo vero vale piu' di dieci definiti.**

**3.2 — Poi tutti e dieci**
WF-MASTER, WF-MEM-EOD, WF-MEM-RETRO, WF-PERF-LOOP, WF-S1..S6. Nessuno escluso.
Aggiornare la finestra: quella attuale e' scaduta il 26 luglio.

**3.3 — Le tracce diventano continue**
25 tracce in tutta la vita del sistema significa che il ReasoningBank non ha memoria di
lavoro. Ogni ciclo deve lasciare le sue 5 tracce (decisione, errore, prestazione, lezione,
sessione) **automaticamente**, non a mano.

**GATE B3:**
```
empire flow status   -> step chiusi > 0 su TUTTI e 10 i workflow, finestra corrente
empire trace stato   -> cresce a ogni ciclo, senza intervento manuale
```

---

## BLOCCO 4 — CODICE NEGLI 11 ECOSISTEMI DI SOLA CARTA

> Oggi solo **3 ecosistemi su 14** contengono codice eseguibile.
> `01-AGENCY` 209 md / **0 py** · `03-CONTENT-FACTORY` 183 / **0** · `04-MARKETING` 159 / **0** ·
> `05-MULTI-BUSINESS` 40 / **0** · `06-PLATFORM` 27 / **0** · `07-FORGE` 34 / **0** ·
> `08-INTELLIGENCE` 16 / **0** · `09-OPERATIONS` 32 / **0** · `10-MEMORY` 28 / **0** ·
> `13-ARENA-APEX` 9 / **1**.

**Attenzione — non e' vero che questi ecosistemi non fanno niente.** I loro motori esistono,
ma vivono **fuori**, nelle cartelle storiche alla root: `Outreach/Outreach Workflow` (238 py),
`YOUTUBE-AUTOMATION-FACTORY` (91 py), `caroselli - agency` (53 py),
`Workflow pubblicazione automatica` (40 py). ADR-003 dice che **restano dove sono**.

Quindi il lavoro qui **non e' spostare codice**: e' dare a ogni ecosistema **il suo punto di
ingresso eseguibile**, che sappia chiamare il motore vero dove si trova e restituire l'uscita
dichiarata in B1.

**GATE B4:**
```
per ognuno dei 14 ecosistemi: un comando che parte, produce l'uscita dichiarata, ha un test verde
```

---

## BLOCCO 5 — ZERO ORFANI (ADR-008 applicata davvero)

> `empire registry orphans` -> **22.469 rilievi, di cui 9.913 bloccanti**. La legge ADR-008
> "nessun artefatto orfano" e' oggi violata su scala industriale.

**5.1 — Triage per tipo, non per file.** Dei 16.555 artefatti censiti, **4.675 sono
`vendored`** (dipendenze di terzi: vanno **esclusi dalla regola**, non collegati). Poi 3.221
`asset` e 5.710 `doc`. Il numero vero da collegare e' molto piu' piccolo di 9.913: prima si
separa, poi si lavora.

**5.2 — Collegare, non cancellare.** Ogni artefatto vivo prende il suo posto in un indice di
reparto, nel REGISTRO-IMPRESA o in STATO-EMPIRE.

**5.3 — Guard permanente.** Chiuso il debito, il pre-commit impedisce di crearne di nuovi
(stessa forma del guard di ADR-013, che ha gia' fermato un PDF da 44 MB diretto nella storia).

**GATE B5:**
```
empire registry orphans   -> block: 0   (vendored esclusi per regola, non per eccezione)
```

---

## BLOCCO 6 — SEI CANALI SU SEI

> `empire controllo` -> **2 su 6 pronti**. Sessione Instagram vecchia **87 giorni**,
> LinkedIn **105 giorni**, YouTube ha lo script ma non l'`.mp4`, Incasso non ha i Payment Link.

| Canale | Oggi | Serve |
|---|---|---|
| OUTREACH email (SMTP) | PARTE | — |
| NFT / STREAM-S7 | PARTE (paper trading) | decisione capitale solo dopo edge provato |
| INSTAGRAM DM | sessione 87gg | **Max**: login una tantum (`refresh_session.py`) — dopo B-023 |
| LINKEDIN | sessione 105gg | **Max**: login una tantum |
| YOUTUBE | manca l'`.mp4` | rendering del video, poi upload |
| INCASSO | tier 2 | **Max**: 2 Payment Link Stripe |

Nota d'ordine: i login vanno rifatti **dopo** la rotazione delle password (B0), non prima,
o la sessione appena creata muore subito.

**GATE B6:**
```
empire controllo   ->  6/6 workflow pronti a partire adesso
```

---

## BLOCCO 7 — CONSEGNA REALE (la fabbrica deve consegnare, non solo produrre)

**7.1 — I 4 libri KDP.** Scritti, 24/24 capitoli, tre con `pubblicabile: True`, 0 bloccanti.
`libri_pubblicati/` contiene **solo `.gitkeep`**. Zero pubblicati, quindi zero vendite e zero
dati su nicchia/prezzo/copertina. Gia' in carico a Gael con TASK-KDP-FIX-W2.

**7.2 — Workflow Estate a verdetto pieno.** `empire estate` -> NON FINITO per 2 controlli:
case study Novacar assente, conform WORKFLOW-ESTATE con 1 block.

**GATE B7:**
```
empire estate      ->  FINITO (exit 0)
libri_pubblicati/  ->  4 libri, non un .gitkeep
```

---

## BLOCCO 8 — AUTO-MIGLIORAMENTO (F10 della roadmap)

> Max: *"quando sara' finita, l'azienda continuera' ad automigliorarsi."*
> Con B1..B7 chiusi, l'Impero ha finalmente i tre ingredienti che F10 richiede e che oggi
> mancano: agenti con contratto (B1), esecutori reali (B2), tracce continue (B3).

Loop: osserva -> giudica -> distilla -> agisci -> predici. ReasoningBank + FORGE che assume e
ritira team.

**GATE B8:** almeno **un'evoluzione organizzativa proposta dal sistema** — non da Max, non da
Claude — **e applicata**.

---

## ORDINE E DIPENDENZE

```
STRUMENTO ZERO: EMPERATOR
        |
        v
   B0 IGIENE  ----------------------> sblocca B6 (i login vanno dopo le password)
        |
        v
   B1 CONTRATTO D'USCITA  ----------> collo di bottiglia: senza, B2 e B3 sono finti
        |
        v
   B2 AGENTI INVOCABILI
        |
        v
   B3 FLOW VIVO  <------------------- da qui EMPERATOR puo' davvero comandare
        |
        +--> B4 CODICE NEI 14 ECOSISTEMI   (in parallelo, swarm)
        +--> B5 ZERO ORFANI                (in parallelo, swarm)
        +--> B6 SEI CANALI                 (in parallelo, dipende da B0)
        |
        v
   B7 CONSEGNA REALE
        |
        v
   B8 AUTO-MIGLIORAMENTO
```

**Regola ADR-006:** ogni blocco segue il ciclo a 9 passi
(RECALL -> SPEC -> PRE-MORTEM -> BUILD -> GATE -> REVIEW indipendente -> TEST -> COMMIT -> RETRO).
Swarm **obbligatorio** su B1 onda B/C, su B4 e su B5: coprono almeno 2 aree disgiunte.
Prima di ogni blocco grosso: blocco COORDINAMENTO in `STATO-EMPIRE.md` + push, cosi'
Gael e Neri non collidono.

---

## AVANZAMENTO

| Blocco | Gate | Stato | Chiuso il |
|---|---|---|---|
| STRUMENTO ZERO — EMPERATOR | nome->attiva · risponde con numeri misurati · avvia 1 workflow | ⬜ | |
| B0 — Igiene e sicurezza | `doctor` 0 block · 3 credenziali revocate | ⬜ | |
| B1 — Contratto d'uscita | `forge scan` 436/436 · C4 mancante 0 | ⬜ | |
| B2 — Agenti invocabili | Board + 14 direttori + 5 Sentinelle chiamabili | ⬜ | |
| B3 — Flow vivo | step chiusi > 0 su 10/10 · tracce automatiche | ⬜ | |
| B4 — Codice nei 14 ecosistemi | 14/14 con entry point + test verde | ⬜ | |
| B5 — Zero orfani | `registry orphans` block 0 | ⬜ | |
| B6 — Sei canali | `controllo` 6/6 | ⬜ | |
| B7 — Consegna reale | `estate` FINITO · 4 libri pubblicati | ⬜ | |
| B8 — Auto-miglioramento | 1 evoluzione proposta dal sistema e applicata | ⬜ | |

**RIPRESA DA:** costruire EMPERATOR (STRUMENTO ZERO), poi B0.
