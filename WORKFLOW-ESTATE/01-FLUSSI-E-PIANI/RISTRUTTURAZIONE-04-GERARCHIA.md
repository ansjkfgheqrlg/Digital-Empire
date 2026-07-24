---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-03-WORKFLOW.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🏛️ PIANO 4 — REPARTI E GERARCHIA VERA
> Livello 4 di 7 · 2026-07-24 · **Dimensione migliorata: l'AUTORITÀ.**
> Domanda a cui risponde: *chi comanda chi, chi controlla chi, e chi decide quando due hanno ragione.*

---

## §0 · AUTOCRITICA DEL PIANO 3

| # | Limite del Piano 3 | Perché è un problema vero |
|---|---|---|
| **L3.1** | **Nessuno decide in caso di conflitto** | Due agenti dello stesso stream danno risposte opposte: il sistema si ferma o sceglie a caso |
| **L3.2** | **Nessun carico di lavoro** | Un agente può risultare su sei stream insieme e nessuno se ne accorge. Assegnare senza contare è finzione |
| **L3.3** | **I reparti esistono e non comandano** | `empire departments` li elenca. Nessuno di loro ha autorità su un workflow |
| **L3.4** | **Rischio dichiarato non chiuso: i collegamenti di facciata** | Scrivere `agenti: [A2]` in un file non fa lavorare A2. Il Piano 3 l'ha ammesso |

### Il difetto che li riassume
Il Piano 3 ha assegnato il lavoro **senza dare a nessuno il potere di farlo rispettare**.
Un'organizzazione in cui tutti hanno un compito e nessuno ha autorità non è un'azienda: è una lista.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: ogni lavoro ha una catena di comando, e ogni conflitto ha un giudice.**

Max ha scelto esplicitamente la forma: *"come un'azienda vera — direttori, capi reparto,
specialisti, controllori"*. Non una squadra di pari.

La differenza pratica sta in una domanda sola, che oggi non ha risposta:
> **Se un lavoro va male, chi ne risponde?**

---

## §2 · CONTENUTO DEL LIVELLO 4

### 2.1 — La gerarchia esiste già: va collegata, non creata
Vincolo additivo. Tutto questo è **già su disco**:

```
company/
  MAXIMILIAN/       il gate 5-bis: approva o boccia, incarna Max
  Board-CSuite/     CEO · COO · CTO · CMO · CRO · CFO · Chief-Forge
  Ecosistemi/       13 ecosistemi, ognuno con un direttore
    ├─ 01-AGENCY/   reparti A1-Ricerca … A10-QA-Cliente
    ├─ 02-INFO-BUSINESS/  IB-L2-STRA · PROD · VEND · LANC · COMM
    └─ 03-CONTENT-FACTORY/ CF-R0-Director … CF-R6-QA
  Guilds/           competenze trasversali
  Sentinels/        vigilanza continua
  Ispettorato/      11 agenti + 5 workflow — organo di autocritica, indipendente
```

**Il pezzo mancante non è un organigramma: è il legame fra l'organigramma e il lavoro.**
Oggi un workflow non sa a quale reparto appartiene, e un reparto non sa quali workflow governa.

### 2.2 — I quattro livelli di autorità
| Livello | Chi | Cosa può fare | Cosa NON può fare |
|---|---|---|---|
| **Comando** | Max · MAXIMILIAN (5-bis) | approvare, bocciare, cambiare la rotta | eseguire al posto degli altri |
| **Direzione** | Board C-Suite · direttori di ecosistema | assegnare lavoro, arbitrare i conflitti, spostare risorse | approvare il proprio lavoro |
| **Reparto** | capi reparto (A1…A10, IB-L2, CF-R…) | organizzare gli specialisti, rispondere dell'esito | cambiare gli obiettivi |
| **Esecuzione** | i 439 agenti | fare il lavoro, produrre le tracce | giudicare sé stessi |
| **Controllo** | Ispettorato · Sentinelle | verificare, misurare, segnalare | costruire ciò che verifica |

**La regola che rende viva questa tabella:**
> **Nessuno approva il proprio lavoro. Nessun controllore costruisce ciò che verifica.**

Non è teoria: è già scritto nell'Ispettorato (*"organo indipendente da chi produce"*) e nel
`Gate Agent` del documento APEX-7 di Max (*"io non creo, io giudico"*). Il Piano 4 la rende la
regola generale dell'azienda, non una nota di due organi.

### 2.3 — La catena di un workflow (risolve L3.1 e L3.3)
Ogni workflow guadagna tre righe, oltre ai sei elementi del Piano 3:

```
reparto:      chi lo governa            → un capo reparto esistente
arbitro:      chi decide se ci si blocca → il direttore sopra quel reparto
controllore:  chi verifica l'esito       → uno dell'Ispettorato, MAI del reparto stesso
```

Esempio su S1, lo stream che porta i soldi:
```
reparto:     A2-Acquisizione            (governa il lavoro)
arbitro:     direttore 01-AGENCY        (decide se A2 e A8 non concordano)
controllore: Ispettorato                (verifica che i lead siano veri — vedi §2.5)
```

### 2.4 — Il carico di lavoro (risolve L3.2)
Una sola domanda nuova, con risposta numerica:
> **Quanti workflow attivi ha questo agente adesso?**

Con una soglia dichiarata e un comportamento definito al superamento: **oltre il limite, il capo
reparto deve riassegnare o dichiarare esplicitamente il sovraccarico.** Nessun agente
silenziosamente su sei stream.

Vale anche per gli esecutori umani: Max, Gael, Gemini. Il piano P7 assegnava a Max *"massimo 90
minuti al giorno"*: era già un limite di carico, mai misurato.

### 2.5 — Il controllo indipendente, con un caso reale
L'Ispettorato esiste (11 agenti, 5 workflow, M1 e M3 fatti) **e non ha mai girato**: le sue
cartelle `company/Ispettorato/report`, `company/Ispettorato/state` e
`company/Ispettorato/telemetry` sono vuote.

Il Piano 4 gli assegna il primo compito vero, che è già stato individuato misurando:

> **I 7 lead di `lead.csv` hanno 0/7 riscontri in una sorgente a monte.**

Nessuno di chi ha costruito l'outreach l'ha notato: l'ho trovato io costruendo la guardia di
provenienza, per caso. **È esattamente il lavoro dell'Ispettorato**: verificare che ciò che il
sistema dichiara corrisponda alla realtà. Un organo di controllo che non ha mai controllato niente
è un titolo, non un organo.

### 2.6 — Cosa NON fa questo piano
- **Non crea nuovi organi.** Ce ne sono già più di quanti ne lavorino.
- **Non decide su `08-`/`12-STREAM-S7-BOT`.** È materia di Max (ADR-009).
- **Non dice come si riprende dopo un'interruzione.** È il Piano 5.

---

## §3 · GATE DI PASSAGGIO L4 → L5

Soglia **5 su 6**.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Ogni workflow ha reparto, arbitro e controllore | le 3 righe non sono vuote | catena incompleta |
| **C2** | **Il controllore non appartiene al reparto che verifica** | confronto fra i due campi | è il criterio che rende reale l'indipendenza |
| **C3** | Ogni capo reparto citato esiste in `empire departments` | verifica per id | ruolo inventato |
| **C4** | Il carico di ogni agente è un numero interrogabile | un comando lo stampa | assegnazione ancora cieca |
| **C5** | L'Ispettorato ha prodotto **almeno un report vero** | `company/Ispettorato/report` non è più vuota | l'organo continua a non esistere nei fatti |
| **C6** | Nessun organo nuovo è stato creato | confronto con l'elenco di prima | violato il vincolo additivo |

**C2 e C5 obbligatori anche a 5/6.** C2 perché senza indipendenza il controllo è teatro.
C5 perché è la prova che questo piano ha cambiato qualcosa invece di riordinare nomi.

**Se il gate fallisce 3 volte:** si applica la catena a **un solo workflow** (S1), la si fa
funzionare davvero, e si estende solo dopo.

---

## §4 · AUTOCRITICA DEL PIANO 4

### ✅ Cosa ha migliorato davvero
- **Ha dato un giudice a ogni conflitto** e un responsabile a ogni esito: la domanda *"se va male
  chi ne risponde?"* ora ha risposta.
- **Ha generalizzato una regola che esisteva in due angoli** (Ispettorato indipendente, Gate Agent
  che non crea) e l'ha resa legge d'azienda: *nessuno approva il proprio lavoro*.
- **Ha dato all'Ispettorato un compito vero e già trovato**: i lead non tracciabili. Non un compito
  inventato per giustificarne l'esistenza.
- **Ha messo un numero sul carico**, che è l'unico modo di distinguere un'assegnazione da un desiderio.

### ⚠️ Cosa manca ancora (compito del Piano 5)
- **Non dice cosa succede quando il lavoro si interrompe a metà** — e in questa sessione è successo
  tre volte: agenti morti per limite di spesa, rete caduta due volte durante i push.
- **La catena di comando non sa riprendere.** Sa chi comanda, non da dove ricominciare.
- **Le tracce del Piano 2 continuano a non essere lette da nessuno** (L2.2 è aperto da due piani).
- **Nessun modo di capire *perché* qualcosa è andato storto**: c'è chi ne risponde, non come si indaga.

### 🔴 Il rischio di questo piano, dichiarato
**La burocrazia dell'autorità.** Aggiungere reparto + arbitro + controllore a ogni workflow può
trasformare un lavoro di due ore in una pratica da approvare. Il sistema diventa più ordinato e
più lento — e l'obiettivo dell'estate sono i soldi, non l'organigramma.

La difesa è nella regola P7 §7.1, già in vigore: **i conflitti si risolvono per €/h.**
L'arbitro non arbitra in astratto: sceglie ciò che porta più soldi per ora di lavoro.
E vale il tetto già scritto nel Piano 3: **zero organi nuovi.**

### SCORE PIANO 4 — **8.7 / 10**
Alto perché risolve tre limiti su quattro del Piano 3 usando solo pezzi esistenti. Perde 1.3 punti
perché **aggiunge peso** in un'azienda che deve fatturare entro settembre, e perché non tocca il
limite più vecchio ancora aperto: nessuno legge le tracce.

---
⛓️ P12: `RISTR-04-GERARCHIA#empire` · migliora: [PIANO 3](RISTRUTTURAZIONE-03-WORKFLOW.md) · migliorato da: [PIANO 5](RISTRUTTURAZIONE-05-SESSIONI.md)
