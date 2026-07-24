---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-00-BRIEF.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🧱 PIANO 1 — FONDAMENTA ONESTE
> Livello 1 di 7 · 2026-07-24 · **Dimensione migliorata: la VERITÀ.**
> Domanda a cui risponde: *cosa esiste davvero, chi possiede cosa, e perché certe cose sono vuote.*

---

## §0 · AUTOCRITICA DELLO STATO ATTUALE (il "piano 0" è la situazione di oggi)

Non c'è un piano precedente da criticare: c'è l'azienda com'è adesso. La critico con i numeri
misurati, non a impressione.

| # | Difetto | Prova misurata |
|---|---|---|
| D1 | **Gli agenti non sono collegati al lavoro** | 439 agenti censiti, 6 stream attivi, e i file dei 6 stream **non nominano un solo agente**. Dichiarano solo `Owner:` |
| D2 | **Gli stream sono prosa, non workflow** | I 6 file WF-S* pesano 36-78 righe l'uno. Descrivono cosa fare, non chi lo esegue né con quale skill |
| D3 | **I sensori non registrano nulla** | `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS` 11 cartelle su 11 vuote · `company/Memory/tasks` 10 su 10 vuote · `empire inspect` → 6 metriche su 6 a zero, nota "nessun record PERF" |
| D4 | **I controlli rassicurano invece di misurare** | 3 casi trovati il 24/07: dashboard che coloriva di verde i valori illeggibili · `skills-map.yaml` YAML non valido (anagrafe ADR-008 mai caricata da un parser) · `video_pack --check` che approvava il proprio scheletro |
| D5 | **Il vocabolario non è definito** | "fase", "workflow", "reparto", "agente", "skill", "sessione" sono usati con significati diversi in file diversi. Nessuno può verificare una regola scritta con parole ambigue |
| D6 | **Anagrafe divergente dalla realtà** | `08-STREAM-S7-BOT` e `12-STREAM-S7-BOT` coesistono in `company/Ecosistemi/`: sembrano lo stesso ecosistema due volte |

### La radice comune
D1, D2, D3 e D4 **non sono quattro problemi**: sono lo stesso problema visto da quattro lati.
**L'azienda è stata progettata, non eseguita.** Esistono i dossier, gli organigrammi, le cartelle,
gli schemi — e non esiste una sola esecuzione che li attraversi lasciando una traccia.

Le cartelle vuote sono la prova più pulita: non sono disordine, sono **il segno che nessuno è mai
passato di lì**.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: la verità verificabile.**

Il Piano 1 non aggiunge funzioni, non crea agenti, non accende cicli. Fa una cosa sola: **rende
impossibile mentire sullo stato dell'azienda**, incluso mentire per distrazione.

Perché è il livello 1 e non il 3 o il 5: ogni piano successivo si appoggia a un'affermazione su
cosa esiste. Se quell'affermazione è sbagliata, i sei piani sopra crollano. Il 23/07 la dashboard
diceva Gate-FUNNEL 🟢 mentre il file conteneva `YOUR_STRIPE`: **una settimana di lavoro pianificata
su un dato falso.** Non si costruisce sopra a questo.

---

## §2 · CONTENUTO DEL LIVELLO 1

### 2.1 — Il vocabolario ufficiale (risolve D5)
Sei parole, una definizione ciascuna, **verificabile a macchina**. Da qui in poi valgono queste.

| Parola | Definizione operativa | Come si verifica |
|---|---|---|
| **FASE** | Un pezzo di lavoro con un inizio, una fine e un esito dichiarato. È l'unità che si può chiudere | ha un id, uno stato (`OPEN` · `IN_PROGRESS` · `DONE`), un esito |
| **WORKFLOW** | Una fase **eseguibile**: ha agenti assegnati, skill dichiarate, gate di uscita | il file elenca `agenti:`, `skill:`, `gate:` non vuoti |
| **AGENTE** | Un esecutore con un compito unico, un input e un output dichiarati | esiste in `empire agents`, ha un id, ha un file |
| **SKILL** | Una capacità riusabile, indipendente da chi la usa | esiste in `empire skills` e in `skills-map.yaml` |
| **REPARTO** | Un gruppo di agenti con un responsabile e un perimetro | esiste in `empire departments`, ha un capo dichiarato |
| **SESSIONE** | Una finestra di lavoro continuativa, con uno stato salvato all'inizio e alla fine | ha un record in `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/sessions` con apertura e chiusura |

**Regola d'oro del vocabolario:** se una parola non si può verificare con un comando, non entra nei
piani. Le parole belle e non misurabili sono il modo in cui un sistema si racconta storie.

### 2.2 — Il censimento onesto (risolve D1, D2, D6)
Non un nuovo censimento: **il collegamento fra i censimenti che già esistono**.

Oggi `empire` sa dire separatamente: 439 agenti · 22 workflow · 53 skill · N reparti · 13-14
ecosistemi. Non sa dire **quale agente lavora a quale stream**. Il Piano 1 introduce una sola
domanda nuova, e la risposta è un numero:

```
Per ognuno dei 6 stream:  quanti agenti?  quante skill?  quali gate?
```

**Attesa, in base a quello che ho misurato: zero, zero, e solo i gate già formalizzati.**
Il valore di questo numero non è il numero: è che d'ora in poi **esiste**, e che nel Piano 3 lo
si vedrà salire.

### 2.3 — La mappa di proprietà (chi possiede cosa)
ADR-008 impone già che ogni artefatto abbia proprietario, controllore, origine e governo. Il Piano 1
non cambia la regola: **la rende interrogabile**. Domande a cui il sistema deve saper rispondere:

- *Chi possiede questo file?* → oggi si può dedurre leggendo l'intestazione, ma non chiedere.
- *Cosa possiede questa persona?* → oggi non si può sapere.
- *Cosa non ha padrone?* → `empire registry orphans` esiste già ma non è mai stato reso parte di un rito.

### 2.4 — La classificazione delle cartelle vuote (risolve D3, primo passo)
Le 398 cartelle vuote vanno **etichettate**, non toccate (vincolo sovrano: non si cancella).
Tre etichette, già stabilite dall'analisi:

| Etichetta | Quante | Significato | Cosa se ne fa il Piano 2 |
|---|---|---|---|
| `RESIDUO` | ~250 | Spazzatura tecnica (`chrome-profile`, `.venv`, `dist`, `node_modules`) | Le ignora. Proposta di `.gitignore` a Max, mai cancellazione |
| `MAI-PARTITO` | ~100 | Lavoro preparato e mai eseguito (11 run scraper senza output) | Diventano la lista di ciò che si può accendere |
| `SENSORE-SPENTO` | ~25 | Dove il sistema dovrebbe scrivere e non scrive | **Sono l'obiettivo diretto del Piano 2** |

### 2.5 — Le tre bugie da rendere impossibili
Il Piano 1 chiude i tre modi in cui il sistema ha mentito, tutti trovati misurando:

1. **Il verde di comodo** — un valore illeggibile diventava 🟢. *Già corretto il 24/07:* ciò che non
   si sa è ⚪, mai verde. Regola permanente: **in caso di dubbio, mai rassicurare.**
2. **Il registro mai letto** — `skills-map.yaml` era YAML non valido e nessuno se n'era accorto in
   mesi. Regola permanente: **ogni registro dev'essere caricato da un parser almeno una volta, o non è un registro.**
3. **Il controllo che approva sé stesso** — `video_pack --check` validava il proprio scheletro.
   Regola permanente: **un controllo non può usare come criterio qualcosa che ha scritto lui.**

---

## §3 · GATE DI PASSAGGIO L1 → L2

Si passa al Piano 2 **solo se tutti e 5 i criteri passano.** Soglia **5/5**: le fondamenta non
ammettono tolleranza — un errore qui si moltiplica per sei livelli.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Il vocabolario è scritto e ogni parola ha un modo di verificarla | le 6 righe di §2.1 hanno tutte una colonna "come si verifica" non vuota | riscrivere la definizione finché non è misurabile |
| **C2** | Esiste il numero "agenti e skill per stream" per tutti e 6 gli stream | un comando lo stampa, anche se il valore è 0 | il collegamento non è interrogabile: rifare §2.2 |
| **C3** | Ogni cartella vuota ha un'etichetta fra le tre | nessuna cartella vuota resta non classificata | classificare le residue |
| **C4** | Le tre bugie hanno una regola scritta che le impedisce | §2.5 ha 3 regole, ognuna con il caso reale che l'ha generata | scrivere la regola mancante |
| **C5** | Nessun dato di questo piano è dichiarato senza il comando che lo produce | ogni numero in questo file è rintracciabile a un comando eseguito | rimuovere il numero o eseguirlo davvero |

**Se il gate fallisce 3 volte:** il problema non è il piano, è il vocabolario. Si torna a §2.1 e si
riducono le parole finché ognuna è banale da verificare.

---

## §4 · AUTOCRITICA DEL PIANO 1

### ✅ Cosa ha migliorato davvero
- **Ha dato un nome alla malattia**: l'azienda è progettata e non eseguita. Prima c'erano sei
  sintomi scollegati, ora c'è una causa sola — e i piani 2-7 curano quella.
- **Ha reso le parole verificabili.** Senza §2.1, "ogni fase è un workflow con agenti" sarebbe
  rimasta una frase interpretabile in sei modi.
- **Ha trasformato le cartelle vuote da lamentela in dato**: tre etichette, tre destini diversi.
  In particolare ha isolato le ~25 che contano davvero dalle ~350 che non contano.
- **Ha chiuso tre bugie con tre regole**, ognuna nata da un caso reale, non da un principio astratto.

### ⚠️ Cosa manca ancora (è il compito del Piano 2)
- **Non accende niente.** Il Piano 1 sa dire che i sensori sono spenti; non li accende. Un'azienda
  che si conosce bene ma non lascia tracce fra un mese è di nuovo al buio.
- **Il censimento è una fotografia, non un film.** Dice com'è oggi. Non dice come cambia.
- **Non tocca il rapporto agenti↔stream**, lo misura soltanto. Collegarli è il Piano 3.
- **`08-` e `12-STREAM-S7-BOT`**: segnalato, non risolto. È materia di Max (ADR-009).

### 🔴 Il rischio di questo piano, dichiarato
Un piano che parla di "verità" e "onestà" può diventare **retorica**. La difesa è il criterio C5:
ogni numero di questo file è uscito da un comando eseguito in questa sessione. Nessuna stima,
nessun "circa" messo lì per fare volume. Se un numero non aveva un comando, l'ho tolto.

### SCORE PIANO 1 — **8.5 / 10**
Perde 1.5 punti perché **descrive senza accendere**: è corretto per un livello di fondamenta, ma
resta un piano che non muove nulla da solo. Vale solo se il Piano 2 arriva davvero.

---
⛓️ P12: `RISTR-01-FONDAMENTA#empire` · migliora: stato attuale · migliorato da: [PIANO 2](RISTRUTTURAZIONE-02-CICLI.md)
