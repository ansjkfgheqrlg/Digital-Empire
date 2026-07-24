---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-01-FONDAMENTA.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🔄 PIANO 2 — CICLI CHE LASCIANO TRACCIA
> Livello 2 di 7 · 2026-07-24 · **Dimensione migliorata: l'ESECUZIONE che si registra.**
> Domanda a cui risponde: *come fa ogni lavoro a scrivere da solo cosa ha deciso, sbagliato e imparato.*

---

## §0 · AUTOCRITICA DEL PIANO 1

Il Piano 1 ha fatto bene una cosa e ne ha lasciate quattro aperte. Le prendo una per una.

| # | Limite del Piano 1 | Perché è un problema vero |
|---|---|---|
| **L1.1** | **Descrive senza accendere** (l'ha ammesso da solo nello score) | Un censimento è una fotografia. Fra un mese la fotografia è vecchia e siamo di nuovo al buio. Il Piano 1 non ha nessun meccanismo che si aggiorna da solo |
| **L1.2** | **Le tre regole anti-bugia sono scritte, non applicate** | "In caso di dubbio mai rassicurare" è una frase in un file markdown. Niente impedisce al prossimo che scrive codice di violarla. Una regola senza esecutore è un desiderio |
| **L1.3** | **Le cartelle `SENSORE-SPENTO` sono etichettate, non accese** | Sapere che 25 cartelle sono vuote e sapere *perché* non le riempie |
| **L1.4** | **Il vocabolario non ha conseguenze** | §2.1 dice che un WORKFLOW deve avere `agenti:` non vuoti. Ma nessuno controlla i file: oggi i 6 stream violano tutti la definizione e nessuno se ne accorge |

### Il difetto che li riassume
Il Piano 1 ha prodotto **conoscenza senza meccanismo**. Sa tutto e non fa niente.
È esattamente la malattia che ha diagnosticato — *progettato, non eseguito* — applicata a sé stesso.
Se il Piano 2 non risolve questo, i 7 piani diventano il settimo dossier che nessuno esegue.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: ogni lavoro lascia una traccia, senza che nessuno se lo ricordi.**

Non "dobbiamo registrare di più". **La registrazione non deve dipendere dalla buona volontà.**
Se scrivere la traccia è un atto separato che qualcuno deve ricordarsi di fare, non verrà fatto —
la prova è che esiste già la regola memory-first (ADR-002), esistono le cartelle, esiste
`memory_manager.py`, ed è tutto vuoto lo stesso.

**Principio del Piano 2:** *la traccia è un sottoprodotto del lavoro, non un compito in più.*

---

## §2 · CONTENUTO DEL LIVELLO 2

### 2.1 — Le 5 tracce (cosa si registra, e dove va)
Ogni fase di lavoro produce al massimo cinque cose. Non di più: cinque tipi che coprono tutto.

| Traccia | Quando nasce | Dove vive oggi (cartella già esistente, vuota) | Perché serve |
|---|---|---|---|
| **DECISIONE** | quando si sceglie fra due strade | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/decisions` | per non ridiscutere la stessa cosa fra un mese |
| **ERRORE** | quando qualcosa fallisce | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/errors` | per non ripetere lo stesso sbaglio |
| **PRESTAZIONE** | quando una fase si chiude | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/performances` | per sapere quanto costa davvero il lavoro |
| **LEZIONE** | quando si capisce un pattern | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/reasoning-bank` | per migliorare il metodo, non solo il risultato |
| **SESSIONE** | apertura e chiusura di una finestra di lavoro | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/sessions` | per riprendere esattamente dove si era rimasti |

**Nota importante:** queste cinque cartelle **esistono già e sono vuote**. Il Piano 2 non crea
struttura nuova — vincolo sovrano rispettato: si aggiunge il meccanismo, non si sposta niente.

### 2.2 — La regola del sottoprodotto (risolve L1.1 e L1.3)
Il punto centrale di tutto il livello.

> **Una fase non può essere dichiarata chiusa se non ha prodotto la sua traccia.**

Non "bisognerebbe scrivere il checkpoint". **Chiudere = scrivere la traccia.** Sono la stessa azione.
Chi chiude una fase senza traccia non ha chiuso: ha abbandonato.

Questo è già implementato in un punto e funziona: `empire flow done` registra una transizione con
attore ed evidenza, e `--evidence` vuoto viene rifiutato in `mark_on_red_applied` (*"senza prova,
'applicato' è solo una parola"*). Il Piano 2 estende quel comportamento, già provato, a tutte e cinque
le tracce.

### 2.3 — Il rito di sessione (risolve L1.1, e serve a Max direttamente)
Due momenti obbligatori, uno all'inizio e uno alla fine. Sono i due punti in cui il sistema
guadagna o perde memoria.

**APERTURA** — cosa deve sapere chi arriva:
```
1. cosa è rimasto aperto dalla sessione scorsa
2. qual è la cosa che vale di più adesso
3. cosa è cambiato mentre non c'ero (altre sessioni, altri soci)
```
**CHIUSURA** — cosa deve lasciare chi va via:
```
1. cosa ho chiuso davvero (con la prova)
2. cosa ho lasciato a metà e a che punto è
3. da dove si riparte, in una riga
```

Questo rito **esiste già di fatto**: `STATO-EMPIRE.md` con "RIPRESA DA" è la chiusura, la regola
memory-first è l'apertura. Il Piano 2 lo rende **una fase con un gate**, non un'abitudine.
La differenza si è vista oggi: quando Max ha detto "salva tutto", la ripresa era pronta in un file
solo — perché la chiusura era stata fatta bene.

### 2.4 — Gli esecutori delle regole (risolve L1.2 e L1.4)
Le tre regole anti-bugia del Piano 1 e il vocabolario diventano **controlli**, non frasi.

| Regola del Piano 1 | Chi la fa rispettare | Cosa controlla |
|---|---|---|
| In caso di dubbio, mai rassicurare | il calcolo dello stato dei KPI | un valore illeggibile è ⚪, mai 🟢 *(già attivo dal 24/07)* |
| Ogni registro dev'essere letto da un parser | un controllo sui file di registro | `skills-map.yaml` e simili si caricano davvero *(bug trovato e corretto il 24/07)* |
| Un controllo non usa come criterio ciò che ha scritto lui | il controllo stesso | rifiuta gli scheletri non compilati *(già attivo in `video_pack --check`)* |
| **Un WORKFLOW ha `agenti:` non vuoti** (vocabolario §2.1) | **nuovo** | i 6 stream oggi **violano tutti** questa definizione |

L'ultima riga è la più importante: è il ponte verso il Piano 3. Il Piano 2 introduce il controllo,
il Piano 3 fa il lavoro per superarlo.

### 2.5 — Cosa NON fa questo piano (deciso, non dimenticato)
- **Non riempie le cartelle a mano.** Riempirle con l'archeologia darebbe l'illusione di storico
  senza garantire che domani si riempiano da sole. Si riempiono lavorando, da zero, e la prima
  traccia sarà datata oggi.
- **Non tocca le ~350 cartelle `RESIDUO` e `MAI-PARTITO`.** Vincolo sovrano.
- **Non crea agenti nuovi.** È il Piano 3.

---

## §3 · GATE DI PASSAGGIO L2 → L3

Soglia **4 su 5** — tolleranza di 1, perché un livello di meccanismo ammette che un pezzo arrivi
dopo, purché il nucleo giri.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Le 5 tracce hanno ognuna un modo di essere scritta | esiste un comando per ciascuna | manca il meccanismo: rifare §2.1 |
| **C2** | **Chiudere una fase senza traccia è impossibile** | tentare di chiudere senza evidenza → rifiutato | è il criterio non negoziabile: senza questo il piano non esiste |
| **C3** | Almeno una cartella `SENSORE-SPENTO` ha dentro un record vero, prodotto lavorando | `ls` di quella cartella non è vuoto, e il record è di oggi | il ciclo non gira davvero |
| **C4** | Il rito di sessione ha apertura e chiusura, entrambe con un gate | una sessione chiusa male viene segnalata | il rito è ancora un'abitudine |
| **C5** | Le 4 regole hanno un esecutore, non solo una frase | ognuna ha una colonna "chi la fa rispettare" piena | scrivere l'esecutore mancante |

**C2 è obbligatorio anche in caso di 4/5**: è il cuore del livello. Se si può chiudere senza
traccia, tutto il resto è decorazione.

**Se il gate fallisce 3 volte:** il problema è che si stanno chiedendo troppe tracce. Si scende da
5 a 2 (decisione + errore), si fa girare quello, e si risale.

---

## §4 · AUTOCRITICA DEL PIANO 2

### ✅ Cosa ha migliorato davvero
- **Ha reso la traccia un sottoprodotto**, non un compito. È l'unica correzione che poteva
  funzionare: la regola memory-first esisteva già ed è stata disattesa per mesi proprio perché
  era un atto separato.
- **Ha dato un esecutore a ogni regola del Piano 1.** Le frasi sono diventate controlli.
- **Si appoggia su cose già provate**, non su idee: `flow done` con evidenza obbligatoria e il
  rifiuto degli scheletri funzionano già oggi. Il piano li estende, non li inventa.
- **Ha rifiutato la scorciatoia dell'archeologia**: niente cartelle riempite a mano per far scena.

### ⚠️ Cosa manca ancora (compito del Piano 3)
- **Le tracce non hanno ancora un autore vero.** Si registra *che* una decisione è stata presa, ma
  non *quale agente* l'ha presa — perché gli agenti non sono ancora collegati al lavoro.
- **Il rito di sessione è per una persona sola.** Con Max, Gael e Gemini in parallelo servirà dire
  chi ha aperto cosa. Non è affrontato qui.
- **Nessuna gerarchia**: se due tracce si contraddicono, non c'è chi decide quale vale.
- **Le tracce si accumulano senza mai essere lette.** Un archivio che cresce e nessuno interroga è
  peso morto: manca il momento in cui il sistema *usa* ciò che ha registrato. (Piano 5)

### 🔴 Il rischio di questo piano, dichiarato
**Burocrazia.** Se registrare pesa più che lavorare, la gente aggira il sistema — e aggirare un
sistema di tracce è facilissimo: basta non chiudere le fasi. La difesa è il numero cinque: cinque
tracce, non quindici. E il gate C2 accetta il fallimento: se non regge, si scende a due.

Secondo rischio, più sottile: **tracce vere ma inutili**. Registrare che "la fase è finita alle
14:32" non serve a nessuno. Il Piano 5 dovrà dimostrare che qualcuno le legge, altrimenti il
Piano 2 avrà solo creato lavoro.

### SCORE PIANO 2 — **8.8 / 10**
Sale rispetto al Piano 1 perché **accende** invece di descrivere, e perché poggia su meccanismi già
funzionanti anziché su idee nuove. Perde 1.2 punti perché produce tracce che **nessuno ancora
legge**, e perché non sa chi le ha scritte.

---
⛓️ P12: `RISTR-02-CICLI#empire` · migliora: [PIANO 1](RISTRUTTURAZIONE-01-FONDAMENTA.md) · migliorato da: [PIANO 3](RISTRUTTURAZIONE-03-WORKFLOW.md)
