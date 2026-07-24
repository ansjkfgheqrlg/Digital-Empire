---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-04-GERARCHIA.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🔍 PIANO 5 — SESSIONI, DEBUG, RIPRESA
> Livello 5 di 7 · 2026-07-24 · **Dimensione migliorata: la CONTINUITÀ.**
> Domanda a cui risponde: *come si riprende dopo un'interruzione, e come si capisce perché è andato storto.*

---

## §0 · AUTOCRITICA DEL PIANO 4

| # | Limite del Piano 4 | Perché è un problema vero |
|---|---|---|
| **L4.1** | **La catena di comando non sa riprendere** | Sa chi comanda, non da dove ricominciare dopo un'interruzione |
| **L4.2** | **C'è chi risponde del fallimento, non come si indaga** | Sapere di chi è la colpa non dice cosa è successo |
| **L4.3** | **Aggiunge peso a un'azienda che deve fatturare** | Riconosciuto nel suo stesso score |
| **L4.4** | **L2.2 aperto da tre piani: nessuno legge le tracce** | Si registra da due livelli e non si è mai letto niente |

### Il difetto che li riassume
I primi quattro piani hanno progettato un'azienda **che funziona solo se non viene mai interrotta**.
La realtà è l'opposto — e ho le prove in questa stessa sessione, §2.1.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: l'interruzione è normale, non un'emergenza.**

Un sistema progettato per andare a buon fine funziona finché tutto va bene, cioè quasi mai.
Il Piano 5 progetta per il caso vero: **il lavoro si interrompe a metà, e deve riprendere senza
perdere niente e senza rifare niente.**

E siccome per riprendere bisogna sapere cos'è successo, questo è anche il piano che **finalmente
fa leggere le tracce** — il limite aperto da tre livelli.

---

## §2 · CONTENUTO DEL LIVELLO 5

### 2.1 — Le interruzioni non sono ipotesi: ecco quelle di oggi
Tutte reali, tutte in questa sessione del 24/07:

| # | Interruzione | Cosa è successo | Costo |
|---|---|---|---|
| 1 | **Limite di spesa** | 4 agenti dello swarm morti insieme: `You've hit your monthly spend limit` | lavoro parziale da recuperare a mano |
| 2 | **Rete caduta ×2** | `Failed to connect to github.com port 443` durante i push | 2 commit fermi in locale |
| 3 | **Sessione parallela** | un'altra sessione ha pushato mentre scrivevo: `cannot lock ref` | merge necessario |
| 4 | **Crediti bassi** | Max ferma il lavoro a metà e chiede di salvare tutto | pianificazione troncata |

**Quattro tipi diversi in una sola giornata.** Un sistema che non li prevede è un sistema che
funziona solo nelle giornate che non esistono.

**La difesa che ha funzionato oggi**, e che va resa regola: *salvare dopo ogni pezzo, non alla fine.*
Quando Max ha detto "salva tutto", i piani 1 e 2 erano già su GitHub. Non per fortuna: perché ho
committato dopo ognuno.

### 2.2 — Lo stato di sessione (risolve L4.1)
Tre domande, che sono le stesse tre che Max ha chiesto di poter fare in dieci secondi:

| Domanda di Max | Cosa deve rispondere il sistema |
|---|---|
| *"cosa devo fare adesso"* | la cosa aperta che vale di più, e da cosa è bloccata |
| *"vedere lo stato vero di tutto"* | cosa è finito **con la prova**, cosa è fermo e perché |
| *"lanciare un lavoro e fidarmi"* | il lavoro riparte esattamente da dove si era fermato |

Il meccanismo **esiste già e ha funzionato**: `STATO-EMPIRE.md` con "RIPRESA DA", i checkpoint,
e `python -m empire estate` che dà il verdetto in un comando.
Il Piano 5 aggiunge una cosa sola che manca: **il punto di ripresa dentro una fase**, non solo fra
una sessione e l'altra. Oggi si sa "il Piano 3 è fatto, il 4 no". Non si sa "il Piano 4 era al §2.3".

### 2.3 — Il debug in parole semplici (risolve L4.2)
Max ha chiesto: *se sbaglia, "riprova, poi si ferma e mi spiega"*. Tre parti, tutte necessarie.

**RIPROVA** — un fallimento non è subito una notizia. Si ritenta con una strada diversa, non con la
stessa: ritentare identico è superstizione.

**SI FERMA** — dopo i tentativi previsti ci si ferma. Il numero è dichiarato prima, non deciso sul
momento. La regola esiste già nei gate: *tre fallimenti → salita di livello*.

**SPIEGA** — ed è la parte che oggi manca del tutto. Una spiegazione utile risponde a quattro
domande, in italiano:
```
1. cosa stavo facendo        (la fase, non il comando)
2. cosa mi aspettavo
3. cosa è successo invece    (l'errore vero, citato)
4. cosa serve per sbloccarlo (chi deve fare cosa)
```
Il modello riuscito esiste: `AZIONI-MAX.md`. Non dice "Gate-CONTATTI FAILED": dice che i 7 lead non
hanno riscontro a monte, che i 61 dichiarati non esistono su disco, e le due strade possibili.
**Quella è una spiegazione. Un codice di errore no.**

### 2.4 — 🔑 Finalmente qualcuno legge le tracce (risolve L4.4, aperto da 3 piani)
Le tracce del Piano 2 servono a rispondere a **quattro domande**, e se non rispondono vanno tolte.

| Domanda | Traccia che risponde | Quando serve |
|---|---|---|
| *"L'ho già deciso?"* | DECISIONE | prima di ridiscutere una cosa chiusa |
| *"Ho già sbagliato così?"* | ERRORE | prima di ritentare una strada |
| *"Quanto costa davvero?"* | PRESTAZIONE | quando si stima un lavoro nuovo |
| *"Dove eravamo rimasti?"* | SESSIONE | ogni apertura di sessione |

**Regola di sopravvivenza delle tracce:** una traccia che in tre mesi non ha mai risposto a una
domanda **non serve e va tolta**. Meglio due tracce lette che cinque scritte e mai aperte.
È la difesa contro il rischio dichiarato del Piano 2: registrare per burocrazia.

### 2.5 — Il costo del recupero (risolve L4.3)
Il Piano 4 aggiunge peso. Il Piano 5 lo restituisce, e si può dimostrare con oggi:

- Il recupero degli agenti morti è costato **tempo di ricostruzione a mano**, perché non c'era
  un punto di ripresa dentro le loro fasi.
- Il push fallito **non è costato niente**, perché il commit era già stato fatto.

**La differenza fra i due casi è tutto questo piano.** Il costo della continuità si ripaga alla
prima interruzione, e le interruzioni sono quattro al giorno.

### 2.6 — Cosa NON fa questo piano
- **Non rende il sistema autonomo.** Sa riprendere; non decide da solo se procedere. È il Piano 6.
- **Non impedisce le interruzioni** — non si può. Le rende non distruttive.
- **Non tocca le ~350 cartelle `RESIDUO`/`MAI-PARTITO`.** Vincolo sovrano.

---

## §3 · GATE DI PASSAGGIO L5 → L6

Soglia **5 su 6**.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Ogni fase interrotta ha un punto di ripresa dentro di sé | si riprende senza rifare la parte già fatta | ripresa solo fra sessioni: insufficiente |
| **C2** | **Ogni fallimento produce una spiegazione a 4 domande in italiano** | nessun errore lasciato come codice | è il criterio che Max ha chiesto esplicitamente |
| **C3** | Le 3 domande di Max hanno risposta in un comando | "cosa fare adesso" · "stato vero" · "riparti" | il piano non serve a chi lo usa |
| **C4** | **Almeno una traccia è stata letta e ha cambiato una decisione** | esiste un caso documentato | le tracce restano peso morto: L2.2 ancora aperto |
| **C5** | Il numero di tentativi è dichiarato prima, non deciso dopo | scritto nel workflow | si ritenta a sentimento |
| **C6** | Salvataggio dopo ogni pezzo, non a fine lavoro | i pezzi finiti sopravvivono a un'interruzione | è la difesa provata oggi |

**C2 e C4 obbligatori anche a 5/6.** C2 è una richiesta diretta di Max. C4 perché chiude un limite
aperto da tre piani: se fallisce ancora, il Piano 2 va ridotto da cinque tracce a due.

**Se il gate fallisce 3 volte:** si tiene solo la traccia SESSIONE e la spiegazione a 4 domande.
Sono il minimo che rende un'interruzione non distruttiva.

---

## §4 · AUTOCRITICA DEL PIANO 5

### ✅ Cosa ha migliorato davvero
- **Ha smesso di progettare per la giornata perfetta.** Le quattro interruzioni di §2.1 sono
  successe davvero, oggi, mentre scrivevo questi piani.
- **Ha chiuso L2.2, aperto da tre livelli**, e non con una promessa: con quattro domande concrete e
  la regola che una traccia mai letta va tolta.
- **Ha reso il debug una spiegazione, non un codice.** Con un modello già riuscito (`AZIONI-MAX.md`)
  invece di un formato inventato.
- **Ha restituito il peso aggiunto dal Piano 4** mostrando il conto reale: il push fallito non è
  costato niente, gli agenti morti sì.

### ⚠️ Cosa manca ancora (compito del Piano 6)
- **Il sistema sa riprendere, non sa decidere.** Aspetta comunque che qualcuno dica "vai".
  Max ha chiesto *"fa tutto e mi riporta alla fine"*: qui non c'è ancora.
- **Nessun limite all'autonomia.** Se procedesse da solo, oggi niente gli impedirebbe di mandare
  email a concessionari veri.
- **Le tracce si leggono a richiesta, non da sole.** Nessuno controlla i vecchi errori *prima* di
  ripetere una strada: bisogna ricordarsi di chiedere.

### 🔴 Il rischio di questo piano, dichiarato
**Il teatro della ripresa.** Un punto di ripresa scritto male è peggio di nessuno: fa ricominciare
da un punto sbagliato, e si perde più tempo a capire cos'era stato fatto che a rifarlo.
La difesa è C1 nella sua forma severa: la ripresa vale solo se **non si rifà la parte già fatta**.
Se ricominciando si rifà del lavoro, il punto di ripresa non funziona e va corretto, non tollerato.

### SCORE PIANO 5 — **9.1 / 10**
Il più alto finora: chiude un limite aperto da tre piani, risponde a due richieste diverse di Max
(le tre domande dei dieci secondi, e il "riprova poi spiega"), e ogni sua affermazione è appoggiata
a un'interruzione realmente avvenuta oggi. Perde 0.9 perché il sistema resta **passivo**: sa
riprendere solo quando qualcuno glielo chiede.

---
⛓️ P12: `RISTR-05-SESSIONI#empire` · migliora: [PIANO 4](RISTRUTTURAZIONE-04-GERARCHIA.md) · migliorato da: [PIANO 6](RISTRUTTURAZIONE-06-AUTONOMIA.md)
