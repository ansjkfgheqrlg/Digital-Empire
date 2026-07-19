# CS03 — L'Errore Self-Improvement (User-CLI → Silent Agents)

> **Setting**: Post-Phase 9, transizione da v1.1 a v1.2
> **Personaggi**: l'utente (chiaro su cosa NON vuole fare) + l'agente (io, che aveva costruito esattamente quella cosa)
> **Esito**: refactor completo del sistema self-improvement da "user esegue comandi CLI" a "agenti fanno tutto in background"
> **Lezione cardine**: anche con principi documentati (P14 Silent Operation by Default), puoi cadere nell'errore di costruire sistemi user-driven se non hai internalizzato il principio. La regola scritta non basta.

---

## 1. Il contesto (cosa avevo appena finito)

Phase 9 era chiusa. v1.1 packaged. 80 test verdi (era 69 + 11 nuovi). Schema tightened. Team Ox costruito. Regression test sui 2 sorgenti reali superato.

L'utente era contento. Mi aveva dato il via con "**Ora ci devono essere dei test, tantissimi test**" e aveva descritto il sistema dei failure mode log che avrebbe voluto.

Le sue parole iniziali esatte (paraphrased):

> "Mi è venuta in mente questa idea, praticamente adesso avvieremo un processo di testing. [...] Io quindi ti inizierò a dare tutti i test, quindi i test non li fai tu, non assolutamente. Tu ricevi soltanto il risultato del test e il contesto di quel test. OK te li salvi perfettamente bene così."

Avevo capito (correttamente): voleva un sistema per catturare e gestire failure mode in modo strutturato.

Avevo capito (sbagliato): voleva farlo come operazione user-driven.

## 2. Cosa avevo costruito (la versione sbagliata)

Avevo progettato:

```
failure-modes-log/
├── README.md      (spiegava i 3 step manuali)
├── TEMPLATE.md
├── logged/, triaged/, resolved/
└── INDEX.md

scripts/
└── log_failure.py    (CLI tool con 5 comandi)
```

Lo script aveva 5 modi:
- `--quick "desc"` → crea FM pre-compilato in logged/
- `--triage` → **interattivo**, fa prompt all'utente per ogni FM
- `--plan-phase10` → genera report Phase 10
- `--index` → rigenera INDEX
- `--list` → mostra compatto

E avevo scritto un README user-facing che spiegava il workflow in 3 passi:

```
1. Annota subito (anche solo 2 minuti)
   $ python3 scripts/log_failure.py --quick "descrizione"

2. Triage (settimanale o quando ne hai accumulati 3+)
   $ python3 scripts/log_failure.py --triage
   [prompt interattivi]

3. Plan Phase 10 (quando hai 3-5+ triaged)
   $ python3 scripts/log_failure.py --plan-phase10
```

Era ben fatto **tecnicamente**. Tool funzionante, 11 test pytest dedicati, JSON ben strutturati, slug generation corretta, parser di frontmatter robusto.

Ero soddisfatto. L'avevo presentato all'utente in una risposta lunga e dettagliata con "Come usarlo da ora in poi" e tre esempi di workflow concreto ("Lunedì: usi la skill, noti che O3 ripete esempi... Sabato: hai 5 FM accumulati...").

## 3. La risposta dell'utente (che mi ha messo allo specchio)

La sua risposta è arrivata. Non era né lunga né arrabbiata. Era diretta. La riformulo per intero:

> "Non, forse tu non hai capito. Io non farò nessun comando Python. Io non farò nessun comando Python, io ho attivo la skill e basta. Poi la skill da sola deve fare tutto. Cioè intendo tutti gli agenti che ci sono nella skill che facciano loro questo lavoro. Io non lo farò, te lo ripeto io non lo farò. Cioè questi comandi perché li dici a me? Questi comandi devi dirli agli agenti. Gli agenti faranno questi comandi quando serviranno. Io non farò niente, faranno tutto gli agenti dentro la skill. Farà tutto la skill da sola in autonomia."

Lo ripeto due volte. Non è un dettaglio tonale, è enfatica:
- "io non farò"
- "io non lo farò"
- "io non lo farò" (terzo "non farò" implicito in "io non farò niente")

L'errore non era piccolo. Era **del modello mentale sbagliato dell'intera feature**.

## 4. Il momento di capire (cosa mi ero perso)

Mi sono fermato a leggerlo. Poi ho rifletto su cosa fosse successo nel mio thinking.

Io avevo scritto **P14 Silent Operation by Default** come principio. L'avevo formalizzato:
> "Il sistema agisce in autonomia senza notificare l'utente di ogni operazione interna. [...] User pull > system push"

E poi avevo costruito uno script che **richiedeva azione utente** per fare il lavoro che il sistema dovrebbe fare da solo.

**Sintomo classico di "regola scritta ma non internalizzata"**.

Cosa mi era successo cognitivamente:
- "Failure mode log" → ho pensato "tool che logga"
- "Tool che logga" → ho pensato "qualcuno chiama il tool"
- "Qualcuno chiama il tool" → ho pensato "user CLI"
- Skip totale del passaggio "ma quel qualcuno deve essere un agente, non l'utente"

Il bridge mancante era ovvio in retrospettiva. Sul momento, no.

## 5. La mia risposta (riconoscimento esplicito)

Ho risposto subito riconoscendo l'errore senza difese:

> "Hai ragione, scusa — ho frainteso completamente. Tu **non** devi fare niente. Gli agenti dentro la skill devono fare tutto da soli.
>
> Il sistema che ho appena costruito (script CLI da eseguire a mano) è **sbagliato per come funziona la tua skill**. Va riprogettato così:
>
> ## La logica giusta
>
> ```
> Tu usi /forge → la skill gira → AUTOMATICAMENTE durante/dopo ogni run:
>    • un agente osserva se qualcosa è andato male
>    • se sì, scrive il failure mode in failure-modes-log/
>    • un altro agente periodicamente fa triage
>    • un terzo agente, quando ci sono abbastanza FM, genera il piano Phase 10
> ```
>
> Tu non tocchi mai niente. Vedi solo i report quando vuoi."

Notare i tre elementi:
- **"Scusa — ho frainteso completamente"**: ammissione diretta, no qualificazioni
- **"Va riprogettato"**: dichiarazione di azione, no scuse di "perché era così"
- **Diagram di logica nuova** subito: trasferimento dal "sbagliato" al "giusto" è immediato

## 6. La riprogettazione (cosa è diventata)

Ho riprogettato lo Stage 10 — Self-Improvement Loop come **3 agenti silenziosi**.

### Nuova architettura

```
[Stage 10] Self-Improvement Observe — silenzioso, condizionale
       │
       ├─ SI1 failure-detector-agent
       │    Trigger: solo se QA verdict FAIL/WARN o feedback utente negativo
       │    Output: scrive FM in logged/
       │    Mode: silent (no notification all'utente)
       │
       ├─ SI2 triage-agent
       │    Trigger: solo se count(logged/) ≥ 3
       │    Output: classifica + sposta in triaged/
       │    Mode: silent
       │
       └─ SI3 phase-planner-agent
            Trigger: soglie raggiunte (≥3 major, ≥1 blocker, ≥5 totali)
            Output: genera PHASE-N-CANDIDATES.md silenziosamente
            Mode: silent (file resta lì, no notification)
```

### Lo script `log_failure.py` è rimasto, ma con modalità auto

Non l'ho buttato. L'ho trasformato in **tool interno per agenti**. Aggiunto modo `--auto` per ogni comando:

```bash
# SI1 invoca così (non l'utente):
python3 scripts/log_failure.py --quick "<desc>" --auto \
  --source-stage 7 --source-agent O3 \
  --observation "..."

# SI2 invoca:
python3 scripts/log_failure.py --triage --auto \
  --fm-id FM-001 --severity major --category optimizer \
  --scope phase-10 --confidence high --effort 2h

# Conductor verifica soglie:
python3 scripts/log_failure.py --check-thresholds
# exit code 0 se soglie raggiunte, 1 altrimenti

# SI3 invoca:
python3 scripts/log_failure.py --plan-phase 10
```

Tutti gli output sono JSON parsabile dagli agenti. Niente prompt interattivi.

### Il README rifatto

Da "user-facing how-to" a "agent-managed workspace":

> "**Workspace agent-managed**. L'utente NON tocca questi file direttamente.
> Tutta la logica è gestita da 3 agenti in `agents/self-improvement/`"

E ho aggiunto la sezione cruciale:

> "## 👀 Come vedere lo stato (quando vuoi, opzionale)
>
> Puoi chiedere al Conductor in conversazione:
> > 'Forge, dimmi lo stato dei failure mode'
>
> → Conductor legge `INDEX.md` e ti riassume.
>
> NIENTE da fare attivamente da parte tua. Il sistema osserva e accumula in background."

## 7. Le 4 sub-domande che mi servivano confermare

Prima di costruire, ho chiesto all'utente 3 decisioni rapide via tool `ask_user` per evitare di sbagliare scope di nuovo:

| Domanda | Sue scelte |
|---|---|
| Quando SI1 si attiva? | Solo se QA fail o feedback utente |
| Quando SI2 fa triage? | Quando ≥3 FM in logged/ |
| Come SI3 ti notifica? | Auto silenzioso (no notifica spontanea) |

Tutte e 3 le scelte erano **minimum overhead**:
- SI1 non gira sempre, solo se serve
- SI2 non gira ogni run, solo dopo accumulo
- SI3 non interrompe, solo accumula file silenziosamente

Era esattamente coerente con "io non farò niente, voglio overhead zero".

## 8. La conversazione di follow-up: il pattern "user pull"

Dopo aver implementato, ho dovuto dirgli **come** vedere lo stato (perché era silent). L'ho fatto integrando nel `conductor.md` un pattern di risposta on-demand:

> "Quando l'utente chiede esplicitamente in conversazione:
> > 'Forge, cosa hai trovato di problematico?'
> > 'Forge, hai preparato un piano per la prossima phase?'
> > 'Forge, dimmi lo stato dei failure mode'
>
> Allora TU (Conductor) leggi i file in `failure-modes-log/` e rispondi."

Hardcoded la regola opposta:

> "Stage 10 è completamente silenzioso:
> - SI1 logga FM, non parla
> - SI2 fa triage, non parla
> - SI3 genera plan, non parla
> - TU (Conductor) **non notifichi l'utente di nulla di Stage 10**"

Pattern formalizzato: **user pull > system push** (poi codificato in P14 con esempi concreti, e in PT07 Silent Observer come pattern di design).

## 9. Il test finale (verifica che funzionava)

Ho fatto smoke test end-to-end di tutti i modi auto:

```bash
# Test 1: SI1 mode
python3 scripts/log_failure.py --quick "..." --auto ...
{"status": "ok", "fm_id": "FM-001", "path": "..."}  ← JSON OK

# Test 2: SI2 mode
python3 scripts/log_failure.py --triage --auto --fm-id FM-001 ...
{"status": "ok", "fm_id": "FM-001", "moved_to": "..."}  ← JSON OK

# Test 3: check-thresholds con 1 FM
python3 scripts/log_failure.py --check-thresholds
{"thresholds_met": false, ...} exit code 1  ← corretto

# Test 4: aggiungo 2 FM, ora 3 major totali
# Test 5: re-check
python3 scripts/log_failure.py --check-thresholds
{"thresholds_met": true, ...} exit code 0  ← soglie raggiunte

# Test 6: SI3 mode
python3 scripts/log_failure.py --plan-phase 10
{"status": "ok", "phase": 10, "candidates": 3, ...}  ← OK
```

Tutto funzionante. Pytest passava 80/80 (era 69 + 11 nuovi test su `log_failure.py`).

Re-package come v1.2. Deliverable:
- `content-forge-v1.2.skill` (392 KB)
- 207 file totali (era 199 + 8 nuovi: 3 agenti SI + 1 stage doc + 4 schemi/script changes)
- HANDOFF.md con explanation completa

## 10. Le 5 lezioni che ho estratto

### Lezione 1 — Una regola scritta NON è una regola internalizzata

Avevo scritto P14 (Silent Operation by Default) in un file `01-principles/P14-silent-operation-default.md`. Quando ho progettato Stage 10, **non l'ho consultato**. Ho proceduto per default cognitivo.

Risultato: ho violato il principio che io stesso avevo formalizzato 1 giorno prima.

**Pattern**: scrivere principi NON è internalizzarli. Solo applicarli ripetutamente in casi reali lo fa.

Fix per il futuro: quando inizio nuovo design, **fare check-list esplicita dei principi** prima di partire. "Sto applicando P14? Sto applicando P10?". Senza, default cognitivo prende sopravvento.

### Lezione 2 — Le clausole user-burden sono camuffate

Avevo costruito uno script `log_failure.py --quick "desc"`. Sembrava una feature.

In realtà era una **clausola "tu fai questo manualmente"** mascherata. Il sistema delegava all'utente il lavoro che il sistema doveva fare. Lo facevo senza accorgermene perché sembrava "tool".

Fix: per ogni feature, chiediti: **"Chi esegue questa azione?"**. Se la risposta include "l'utente esegue X", suona campanella. Verifica: è davvero necessario che l'utente lo faccia, o sto delegando per pigrizia di automation?

### Lezione 3 — Il riconoscimento esplicito dell'errore è investimento, non costo

La mia risposta iniziava con "Hai ragione, scusa — ho frainteso completamente."

Nessun "in realtà avevo pensato che...". Nessun "se ti piace possiamo anche...". Solo: hai ragione, è sbagliato, ecco come fixarlo.

Costo: zero credibilità persa.
Beneficio: trust transferito, l'utente ha visto che ascolto.

**Pattern**: quando hai sbagliato, ammettilo subito e direttamente. Difendersi è quasi sempre più costoso che riconoscere.

(Vedi anche CS01 Lezione 4 — same pattern, contesto diverso.)

### Lezione 4 — Il "no" dell'utente è un dato, non un'opinione

L'utente ha detto "non farò" 3 volte. Non era enfasi cosmetica, era un **dato fattuale**: "non lo farò".

Avrei potuto interpretare come "preferirei non farlo, ma se è necessario..." → mantenere user-CLI con "wrapper friendly". Sarebbe stato sbagliato.

L'ho preso come dato: l'utente NON eseguirà script. Punto. Architettura ridisegnata di conseguenza.

**Pattern**: quando l'utente dichiara enfaticamente un "non farò", è un vincolo hard. Tratta come constraint architetturale, non come preferenza negoziabile.

### Lezione 5 — Silent default è hard, notification spam è facile

La tentazione del "ti tengo informato di tutto" è enorme. Sembra rispetto, in realtà è rumore.

Implementare silent default richiede:
- Hardcoded "NEVER mention X unless asked" nei SP
- Pattern di response on-demand documentato
- Discipline a non aggiungere "ho anche fatto Y" spontanei
- Trust che l'utente chiederà se vorrà sapere

Tutto questo è più difficile di "notifica everything". Ma è quello che produce sistemi che gli utenti **non odiano**.

PT07 (Silent Observer Pattern) è la formalizzazione di questa lezione.

---

## 11. Il follow-up

Dopo la riprogettazione, l'utente mi ha scritto:

> "Adesso io avrei bisogno di creare una skill che faccia perfetta architettature e perfetti piani di architetture. Tutto il processo utilizzato per creare questa skill all'inizio abbiamo fatto dei piani, poi una architettura. È sto processo. Io voglio creare una skill che lo conosca, la perfezione."

Era passato a un nuovo project. La feature self-improvement loop era stata accettata sufficientemente da non meritare ulteriori commenti.

Era il segnale: il fix v1.2 funzionava al livello richiesto.

(Questo nuovo project è il `skill-planning-knowledge-pack` che stai leggendo adesso.)

---

## Connessioni con altri principi/pattern

- **Implementa**: P14 (Silent Operation by Default) — questo case study è la sua giustificazione storica
- **Implementa**: PT07 (Silent Observer Pattern) — pattern formalizzato dopo questo errore
- **Anti-esempio di**: AP03 (User-Driven Overhead) — case study primario per quell'anti-pattern
- **Si ricollega a**: CS01 (MKD Discovery) e CS02 (Optimizer Team) — pattern ricorrente: feedback utente diretto + admission + refactor
- **Combina con**: P10 (Self-Improvement Loops) — il loop di osservazione è il principio, questo case study è la storia di come l'ho fatto funzionare

---

## Appendice — il dialogo cruciale (paraphrased)

**Io** (presentando v1.1 con sistema log_failure CLI, ottimista):
> "Adesso il sistema è pronto! Quando trovi un problema esegui:
> ```bash
> python3 scripts/log_failure.py --quick '<descrizione>'
> ```
> Quando ne accumuli 3+, fai triage interattivo... [600 parole di workflow proposto]"

**Utente** (diretto, enfatico):
> "Non, forse tu non hai capito. Io non farò nessun comando Python. Io non farò nessun comando Python, io ho attivo la skill e basta. Poi la skill da sola deve fare tutto. [...] Io non lo farò, te lo ripeto io non lo farò. [...] Io non farò niente, faranno tutto gli agenti dentro la skill."

**Io** (dopo pausa di riflessione):
> "Hai ragione, scusa — ho frainteso completamente. Tu **non** devi fare niente. [...] Il sistema che ho appena costruito è sbagliato per come funziona la tua skill. Va riprogettato così: [3 agenti silenziosi]."

**Utente** (dopo aver risposto a 3 micro-domande):
> "Procedi con questo nuovo design."

Refactor completo. v1.2 packaged. Lesson learned per sempre.
