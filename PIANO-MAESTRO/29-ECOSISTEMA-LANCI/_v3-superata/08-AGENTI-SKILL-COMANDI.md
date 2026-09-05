---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #agenti #skill #ufficializzazione
Created: 2026-09-05
---

# 11 — AGENTI, SKILL E COMANDI

> Terza versione. Tre scoperte della critica hanno cambiato il progetto degli agenti, e una ha
> invalidato una procedura intera. Sono dichiarate nel paragrafo 1, prima di tutto il resto,
> perché chi costruisce deve saperle **prima** di cominciare.

---

## 1. TRE SCOPERTE CHE CAMBIANO IL PIANO

### 1.1 🔴 Nessun comando dell'Impero può oggi verificare che un agente sia ufficiale

**La versione precedente prescriveva:** *"esegui `empire forge scan` e `empire registry orphans`;
un artefatto che non compare non è ufficiale"*.

**Verificato nel codice, e la procedura non funziona:** il censimento marca ogni percorso sotto
`.claude/` come materiale di terze parti, il controllo degli orfani salta quel materiale, e la
scansione della forgia guarda **solo dentro `company/`**. La prova è secca: cercare un agente del
Board che esiste ed è caricato **non restituisce nulla**.

**Cioè: gli strumenti dell'Impero non guardano nella cartella dove l'ufficialità vive.**

| | |
|---|---|
| **Cosa costa se resta** | la procedura di ufficializzazione dà un falso negativo su ogni agente: chi costruisce la esegue, non trova niente, e conclude che ha sbagliato lui |
| **La correzione** | l'ecosistema **si porta il proprio verificatore**: `scripts/registro.py`, che guarda dove serve. E la verifica con i comandi dell'Impero resta come controllo aggiuntivo, **non come prova** |
| **Cosa va segnalato all'Impero** | è un difetto degli strumenti di censimento, non di questo piano. Va in arretrato, non risolto qui |

### 1.2 🔴 Vietare il campo degli strumenti toglie al piano il suo unico vincolo meccanico

**La versione precedente scriveva:** *"nessun campo inventato nel frontmatter"*, e metteva il
campo `tools` fra quelli da non usare.

**È sbagliato, ed è stato verificato:** diciotto agenti dell'Impero usano quel campo e funzionano
perfettamente. Non è un campo inventato: è un campo **previsto**, che limita gli strumenti a cui
un agente ha accesso.

**Perché conta più di un dettaglio di sintassi.** Senza quel campo, un agente eredita **tutti**
gli strumenti — compresi quelli di scrittura. Quindi la regola *"un gate non produce mai
l'artefatto che giudica"* resta **prosa**: `lan-qlt-gate` potrebbe riscrivere il file che sta
valutando, e niente glielo impedirebbe se non la sua buona volontà.

**La correzione, ed è la più importante di tutto questo dossier:**

| Tipo di agente | Strumenti concessi | Cosa gli diventa impossibile |
|---|---|---|
| **Gate** | sola lettura e ricerca | **non può scrivere**: la regola "chi giudica non produce" diventa meccanica |
| **Sentinella** | sola lettura e ricerca | non può agire: segnala e basta |
| **Ricercatore** | lettura, ricerca, rete | non può modificare il repo |
| **Archivista** | lettura e scrittura **limitata alla propria cartella di memoria** | non può toccare gli artefatti del lancio |
| **Operatore** | lettura e scrittura | — |
| **Direttore** | tutti | è lui che orchestra |

**Il principio:** *una regola scritta in prosa viene disobbedita; una regola imposta dagli
strumenti disponibili, no.* Il piano aveva scritto sei regole di comportamento e si stava
togliendo l'unico modo di farle rispettare.

### 1.3 🔴 Il numero 15 non è "libero": va riservato con una decisione registrata, prima

**Verificato:** una decisione già in vigore impone che **ogni ecosistema dal quattordicesimo in
poi richieda una decisione registrata *prima* di poter essere inserito**, e un controllo di
conformità lo verifica davvero. Il registro dei numeri dice che il 15 è libero, **ma alla voce
"riservati" non c'è nessuno**.

**Conseguenza operativa, e va rispettata alla lettera:** la decisione registrata (dossier 13)
**non è l'ultimo passo del piano: è il primo passo della costruzione.** Senza, la cartella
dell'ecosistema nasce fuori norma.

**E c'è un secondo fatto da dichiarare, scomodo:** il controllo di conformità dell'Impero **oggi
esce in errore** per due bloccanti che non riguardano i lanci. Finché restano, il passo *"finché
le verifiche non passano non è ufficiale"* è insoddisfacibile per ragioni estranee a questo
lavoro. Va saputo prima, non scoperto dopo.

---

## 2. I SETTE PRINCIPI

| # | Principio | Perché |
|---|---|---|
| 1 | **Un agente = un mestiere** | un agente che fa due cose le fa entrambe peggio, e quando sbaglia non si sa quale delle due |
| 2 | **Ingresso e uscita tipizzati, o non esiste** | chi non dichiara cosa restituisce non può stare in una catena |
| 3 | **Chi produce non approva** — *e adesso è imposto dagli strumenti* | un reparto che si autocertifica non ha un gate: ha un timbro |
| 4 | **Nessun agente compie da solo un'azione irreversibile** — *imposto dagli strumenti* | un'email spedita non si richiama |
| 5 | **Quando non sa, si ferma e lo dichiara** | un agente che riempie i buchi produce output plausibili e falsi: i peggiori, perché nessuno li controlla |
| 6 | **Ogni "fatto" si ricalcola dai file** | tre casi reali in questo repo di codice che dichiara successo senza aver eseguito niente |
| 7 | **Il grado giusto per il lavoro giusto** | un controllo su un modello pesante è denaro buttato; una progettazione su uno leggero è lavoro da rifare |

---

## 3. LA TASSONOMIA

| Ruolo | Cosa fa | Cosa non può fare | Strumenti | Modello |
|---|---|---|---|---|
| **Direttore** | orchestra un flusso, parla con la persona | non produce artefatti col proprio nome; non approva i suoi | tutti | pesante |
| **Operatore** | produce **un** artefatto | non valida il proprio lavoro | lettura, scrittura | media |
| **Gate** | valuta e blocca | **non può scrivere: glielo impediscono gli strumenti** | sola lettura | leggera |
| **Ricercatore** | raccoglie fatti esterni con la fonte | non interpreta, non conclude | lettura, rete | media |
| **Archivista** | scrive nella memoria | non tocca gli artefatti del lancio | lettura, scrittura **circoscritta** | leggera |
| **Sentinella** | vigila su una soglia | **non agisce: segnala** | sola lettura | leggera |

**La regola del grado:** *chi progetta è pesante, chi produce è medio, chi controlla è leggero.*
Invertirla è il modo più comune di sprecare denaro in un sistema multi-agente.

---

## 4. IL CENSIMENTO — 41 agenti, e stavolta il conto torna

> ⚠️ La versione precedente si intitolava "41 agenti", ne sommava 41 in una tabella e ne elencava
> 52 nelle altre. **Qui il conto è stato rifatto e verificato riga per riga.**

| Reparto | Agenti | Nomi |
|---|---:|---|
| Direzione | 1 | `lan-direttore` |
| Strategia | 3 | conductor · filtro · obiettivi |
| Intelligence | 4 | conductor · ascoltatore · osservatore · analista |
| Prodotto | 5 | conductor · inventariante · architetto · produttore · collaudatore |
| Offerta | 3 | conductor · prezzo · struttura |
| Copy | 6 | conductor · fondamenta · vendita · derivati · email · bibliotecario |
| Funnel | 4 | conductor · costruttore · verificatore · ottimizzatore |
| Traffico | 3 | conductor · campagne · misuratore |
| Editoriale | 4 | conductor · magazziniere · redattore · sentinella |
| Tesoro | 3 | conductor · registratore · sentinella |
| Regia | 4 | conductor · calendarista · tracciatore · prova-a-secco |
| Qualità | 4 | gate generico · gate fonti · gate copy · gate costi |
| Memoria | 2 | distillatore · bibliotecario |
| **Sentinelle trasversali** | **4** | scadenze · memoria · sospesi · irreversibili |
| **TOTALE** | **50** | *(41 di reparto + 4 sentinelle di reparto già contate + 4 trasversali + 1 direzione)* |

**Il numero onesto è 50, non 41.** Dichiararlo giusto conta più di dichiararlo basso: chi
costruisce deve sapere quanto lavoro ha davanti.

**Ma il numero che governa la costruzione è un altro: 11.** Sono gli agenti dello scaglione
minimo (dossier 01 §5), gli unici senza cui il primo lancio non esce. Gli altri 39 si costruiscono
dopo che quegli 11 hanno fatto uscire qualcosa.

---

## 5. IL FRONTMATTER — corretto

```yaml
---
name: lan-qlt-gate
description: Esegue un criterio di controllo scritto in un file e produce un verbale di superamento o blocco, senza mai produrre l'artefatto che giudica. Invocalo per far valutare un output di un lancio contro il suo criterio, per capire perché un gate ha bloccato, o per rieseguire un controllo dopo una correzione.
tools: Read, Grep, Glob
model: haiku
color: red
---
```

| Campo | Regola |
|---|---|
| `name` | **identico al nome del file**. Un disallineamento e l'agente non si trova |
| `description` | **una riga**, e deve dire **quando invocarlo**, non cosa fa. È il testo su cui il sistema decide se chiamarlo |
| `tools` | **si usa**, ed è il vincolo che rende meccaniche le regole di comportamento. *(La versione precedente lo vietava per errore.)* |
| `model` | `haiku` per i controlli · `sonnet` per le missioni · `opus` per chi progetta |
| `color` | **consigliato, non bloccante**: tre agenti ufficiali dell'Impero ne sono privi e funzionano |

**I campi che fanno scartare il file in silenzio** — mai scriverli: `agent_id`, `stage`, `family`,
`spawned_by`, `version`, `owner`, `department`, `inputs`, `outputs`.

**La trappola dei due punti:** una descrizione che contiene due punti seguiti da spazio dentro uno
scalare piatto **rompe il frontmatter**, e l'agente sparisce senza un messaggio d'errore. È
successo davvero.

---

## 6. LO SCHELETRO DEL CORPO

```markdown
# <NOME>

> Reparto · ecosistema 15-LANCI · Fase che esegue: <sigla>
> Proprietario: <capo reparto> · Controllore: <il gate che lo giudica>

## 1. Chi sei            una frase, un mestiere solo
## 2. Contratto d'ingresso   cosa ricevi, in che formato, cosa fai se manca un campo
## 3. Contratto d'uscita     cosa restituisci, con quale schema
## 4. Come lavori            i passi, concreti
## 5. Le regole
## 6. Cosa non fai mai       almeno: azioni irreversibili · approvare il tuo lavoro · inventare un dato
## 7. Quando ti fermi        le condizioni in cui smetti e dichiari, invece di indovinare
## 8. Connessioni            da chi ricevi, a chi passi, chi ti giudica
```

**La sezione 7 distingue un agente utile da uno pericoloso.** Un agente che non sa fermarsi
produce output plausibili e falsi, ed è peggio di uno che non produce niente: il secondo si nota.

---

## 7. LA PROCEDURA DI UFFICIALIZZAZIONE — corretta

```
1.  Scrivi la specifica in 15-LANCI/Reparti/<REPARTO>/agenti/<nome>.md
2.  Scrivi l'agente vero in .claude/agents/<nome>.md
      · frontmatter: name, description (una riga, dice QUANDO), tools, model, color
      · nessun campo inventato · nessun ": " nella descrizione piatta
3.  Verifica che nome del file e campo name coincidano
4.  Verifica che gli strumenti concessi siano quelli del suo ruolo (§3)
5.  Registra in company/REGISTRO-IMPRESA.md: nome, proprietario, controllore, origine
6.  Registra in company/skills-map.yaml sotto 15-LANCI
7.  Aggiungi la voce in 15-LANCI/REGISTRO.md
8.  Aggiungi la pagina in wiki con almeno due collegamenti
9.  ESEGUI LA VERIFICA (sotto)
10. Checkpoint in memoria con lo strumento ufficiale, mai a mano
```

### La verifica, e perché non usa i comandi dell'Impero come prova

```bash
# LA PROVA — guarda dove l'ufficialità vive davvero
python "…/15-LANCI/scripts/registro.py" verifica --ecosistema 15-LANCI

# controlli aggiuntivi dell'Impero: utili, ma NON sono la prova (§1.1)
PYTHONIOENCODING=utf-8 python -m empire forge scan
PYTHONIOENCODING=utf-8 python -m empire registry orphans
```

`registro.py` verifica quattro cose che nessun altro strumento verifica oggi:

| # | Controllo |
|---|---|
| 1 | **La coppia esiste**: specifica e agente vero, nessuno dei due orfano |
| 2 | Il frontmatter è valido, `name` coincide col nome del file, nessun campo inventato |
| 3 | **Gli strumenti concessi corrispondono al ruolo** — un gate con permessi di scrittura viene segnalato |
| 4 | Il reparto è **abilitato** (dossier 01 §2): un agente di un reparto non ancora abilitato viene rifiutato |

**Su Windows:** `PYTHONIOENCODING=utf-8` davanti a ogni comando. Senza, la console italiana muore
su qualunque accento o freccia, e il comando sembra rotto quando è solo muto.

---

## 8. LE SKILL

| Skill | Cosa fa | Comando | Se manca l'input |
|---|---|---|---|
| `lancio` | apre, mostra, fa avanzare | `/lancio` | dice quale campo manca **e chi lo produce** |
| `lancio-strategia` | le cinque domande | `/lancio-strategia` | chiede l'idea e lo stato delle linee |
| `lancio-ricerca` | la ricerca con le fonti | `/lancio-ricerca` | **rifiuta un pubblico generico** |
| `lancio-prodotto` | certifica | `/lancio-prodotto` | dice cosa manca al brief |
| `lancio-offerta` | prezzo e data istruiti | `/lancio-offerta` | **dichiara che serve una firma** |
| `lancio-copy` | tutti i testi | `/lancio-copy` | le fondamenta partono anche senza prezzo |
| `lancio-funnel` | pagine online e misurate | `/lancio-funnel` | dice quali testi mancano |
| `lancio-editoriale` | il piano dei contenuti | `/lancio-editoriale` | dice che serve la grande promessa |
| `lancio-budget` | budget e pareggio | `/lancio-budget` | dice che serve il prezzo |
| `lancio-regia` | calendario e tracciamento | `/lancio-regia` | dice che serve la data |
| `lancio-debrief` | consuntivo e schemi | `/lancio-debrief` | dice che la vendita è ancora aperta |

**Undici skill, undici comandi.** *(La versione precedente ne dichiarava 8 in un documento e 11 in
un altro, e i comandi erano 7, 9 o 11 a seconda della pagina. Adesso è un numero solo.)*

**La regola che vale per tutte:** *un comando che non trova l'input **non improvvisa**. Si ferma,
dice cosa manca, e dice quale comando produce ciò che manca.*

---

## 9. COSA NON VA DUPLICATO

Prima di costruire una capacità, si guarda qui. **Tutte queste esistono, verificate una per una.**

| Capacità | Cosa esiste già | Cosa fa l'ecosistema |
|---|---|---|
| Scrivere testi che convertono | la skill dedicata | **la invoca** |
| Vigilare sul punteggio dei testi e sugli output senza prova | **la sentinella della qualità, già ufficiale** | **le passa i punteggi** — la griglia diventa il suo criterio |
| Controllare claim senza prova e frasi generiche | la sentinella della voce del marchio | la chiama in fase di coerenza |
| Costruire e pubblicare pagine | tre skill dedicate | le orchestra |
| Stile visivo premium | la skill dedicata | la applica |
| Campagne e creatività a pagamento | due skill | le usa |
| Prezzi e paywall | due skill | le consulta; **la decisione resta del reparto Offerta** |
| Contare i soldi dell'azienda | l'ecosistema Tesoreria | **gli passa i dati** |
| Produrre video e caroselli | le fabbriche esistenti | **ordina**, non produce |
| La formazione dell'Impero | l'agente della conoscenza | **gli chiede**, non archivia metodi |
| Trovare il lavoro finito e mai uscito | la skill dedicata | **è il suo sbocco**: quella trova, questo chiude |

---

## 10. IL COSTO — stima, dichiarata tale

**Non è una misura.** Nessun lancio è mai stato eseguito, quindi non esiste un dato. Queste sono
**classi di modello e numeri di chiamate**, non euro: scrivere euro qui sarebbe scriverli falsi.

| Dove sta il costo | Peso |
|---|---|
| **La scrittura dei testi** — 11 pezzi × 1-2 giri su modello pesante | **dominante, tutto il resto messo insieme pesa meno** |
| Il giudizio sui testi | medio |
| I gate automatici, i controlli delle pagine, il tracciamento | trascurabile, e devono restare su modelli leggeri |

**Tre conseguenze operative:**

1. **I gate vanno su modelli leggeri.** Contano, confrontano, aprono indirizzi: non ragionano.
2. **Il ciclo di rifacimento dei testi è la voce da controllare.** Per questo il gate della pagina
   di vendita sta **prima** dello sprint: un errore nella promessa madre si moltiplica per undici.
3. **La ricerca si aggiorna, non si rifà.** È il secondo risparmio, e il motivo per cui il
   registro ha identificativi stabili.

**Come si misura sul serio:** al primo lancio si registra il numero di chiamate per agente e
classe. Al secondo esiste un dato vero e queste stime si buttano.

---

## 11. COSA È CAMBIATO

| Cambiamento | Contro quale obiezione |
|---|---|
| **Si usa il campo degli strumenti**, con un profilo per ruolo | *"vietandolo, il piano rinuncia al suo unico vincolo meccanico: un gate può riscrivere ciò che giudica"* |
| L'ecosistema **si porta il proprio verificatore** | *"nessun comando dell'Impero guarda nella cartella dove l'ufficialità vive — verificato nel codice"* |
| La decisione registrata è **il primo passo, non l'ultimo** | *"una norma in vigore impone la decisione prima dell'inserimento, e un controllo lo verifica"* |
| Il conto degli agenti è **50, dichiarato** | *"il documento si intitola 41, ne somma 41 e ne elenca 52"* |
| Skill e comandi sono **undici e undici** | *"tre numeri diversi in tre pagine"* |
| `color` diventa **consigliato**, non obbligatorio | *"tre agenti ufficiali ne sono privi e funzionano"* |
| Dichiarato che il controllo di conformità **oggi esce in errore** | *"il passo 9 è insoddisfacibile per ragioni estranee ai lanci"* |
