---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-06-AUTONOMIA.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🏆 PIANO 7 — APEX: IL SISTEMA CHE SI CORREGGE DA SOLO
> Livello 7 di 7 · 2026-07-24 · **Dimensione migliorata: l'AUTOCRITICA.**
> Domanda a cui risponde: *come fa il sistema ad accorgersi dei propri difetti senza che glieli trovi Max.*

---

## §0 · AUTOCRITICA DEL PIANO 6

| # | Limite del Piano 6 | Perché è un problema vero |
|---|---|---|
| **L6.1** | **Esegue bene un metodo che non sceglie** | Se un modo di lavorare è peggiore di un altro, non se ne accorge |
| **L6.2** | **Non misura sé stesso nel tempo** | Sa se un lavoro è finito, non se sta migliorando |
| **L6.3** | **Non scopre i propri difetti** | I 3 difetti del 24/07 li ho trovati io a mano, per caso |
| **L6.4** | **Rischio aperto e non coperto** | L'autonomia aumenta la fiducia prima che il controllo indipendente funzioni |

### Il difetto che li riassume
I sei piani precedenti hanno costruito **un'azienda che lavora bene e non impara**.
Ripeterebbe per sempre lo stesso metodo, compresi i suoi errori — con l'aggravante che ora li
ripete **in autonomia e più in fretta**.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: il sistema trova i propri difetti prima che li trovi Max.**

Non "il sistema si migliora da solo" in senso magico. Una cosa precisa e verificabile:

> **Ogni difetto che ho trovato a mano oggi, il sistema deve poterlo trovare da solo domani.**

È il criterio più severo dei sette piani, perché è **già misurabile su casi reali**: ho trovato
quattro difetti il 24/07, e per ognuno si può dire se il sistema li avrebbe presi o no.

---

## §2 · CONTENUTO DEL LIVELLO 7

### 2.1 — La prova del nove: i 4 difetti reali
| Difetto trovato a mano | Come l'ho trovato | Il sistema l'avrebbe trovato? |
|---|---|---|
| **Dashboard verde su valori illeggibili** | leggendo il codice per un'altra ragione | ❌ no — nessuno confrontava i colori con i valori |
| **`skills-map.yaml` YAML non valido** | provando a caricarlo per aggiungere una voce | ✅ **sì, banalmente** — bastava caricarlo una volta |
| **`video_pack --check` approvava il proprio scheletro** | un test che avevo scritto aspettandomi il contrario | ✅ **sì** — era un test |
| **I 7 lead senza riscontro a monte** | costruendo la guardia di provenienza | ⚠️ solo dopo aver costruito la guardia |

**Cosa insegna questa tabella, ed è il cuore del Piano 7:** due difetti su quattro erano
individuabili con un controllo banale che nessuno aveva mai eseguito.
**Non serviva intelligenza: serviva esecuzione.**

Quindi l'APEX non è un sistema che pensa meglio. È un sistema **che esegue i controlli che
possiede**. L'azienda aveva già l'Ispettorato, i gate, i test, l'anagrafe: tutto fermo.

### 2.2 — Le tre domande dell'autocritica
Il sistema se le pone da solo, a intervalli, e ognuna produce una risposta scritta.

**1. "Sto migliorando o solo lavorando?"**
Confronto fra periodi sulle stesse misure: quanti gate al primo colpo, quanti errori ripetuti,
quanto tempo per lavoro. Le misure esistono già (`empire inspect`) e oggi valgono tutte zero.
**Zero non è un fallimento: è il primo punto della serie.** Il valore del Piano 7 comincia
quando ce ne sono due.

**2. "Quale mio controllo non ha mai trovato niente?"**
Un controllo che non trova mai nulla è o inutile o rotto — e va indagato, non lasciato.
Caso reale: `video_pack --check` dava sempre verde **perché approvava sé stesso**.

**3. "Quale mia regola viene sempre violata?"**
Una regola violata di continuo è sbagliata, non ignorata. Caso reale: la regola memory-first
(ADR-002) esiste da mesi e le cartelle sono vuote. **Non è indisciplina: la regola chiedeva un
atto separato, e gli atti separati non si fanno.** È il motivo per cui il Piano 2 ha reso la
traccia un sottoprodotto invece di un compito.

### 2.3 — La correzione proposta, mai applicata da sola
Quando il sistema trova un proprio difetto, produce **una proposta**, non una modifica.

```
1. cosa non funziona     (con la prova misurata)
2. perché credo che sia così
3. cosa propongo di cambiare
4. cosa potrebbe rompersi se lo cambio
```

**Perché non si auto-corregge:** un sistema che modifica le proprie regole in autonomia può
allentare quelle che gli danno fastidio — a partire dai controlli che lo bloccano. Il punto 4 esiste
proprio per rendere visibile il costo di ogni proposta.

Questo rispetta anche il confine del Piano 6: cambiare le proprie regole è **irreversibile per la
fiducia**, e quindi passa da Max. Ed è il vincolo sovrano applicato al sistema stesso:
*migliorare e aggiungere, non ricostruire.*

### 2.4 — Il controllo indipendente finalmente in funzione (chiude L6.4)
L'Ispettorato ha 11 agenti, 5 workflow, e non ha mai girato: `report/`, `state/`, `telemetry/` vuote.
Il Piano 7 gli dà l'unico compito che nessun altro può fare, perché **verifica chi costruisce**:

> **Verificare che ciò che il sistema dichiara corrisponda a ciò che è sul disco.**

Non è astratto — è la classe esatta dei difetti trovati oggi:
- la dashboard dichiarava Gate-FUNNEL 🟢, il file conteneva `YOUR_STRIPE`
- STATO-EMPIRE dichiarava 61 lead, il disco ne aveva 0
- `05-STATO.md` poteva dichiarare un video che non esiste

**Un solo controllo, ripetuto: "quello che diciamo è vero?"** Tre difetti su quattro sarebbero
caduti qui.

### 2.5 — La chiusura del cerchio
| Piano | Cosa ha dato | Cosa usa il Piano 7 |
|---|---|---|
| 1 Fondamenta | verità verificabile | le misure di partenza |
| 2 Cicli | tracce come sottoprodotto | i dati su cui confrontare i periodi |
| 3 Workflow | agenti collegati al lavoro | sa *chi* ha prodotto cosa |
| 4 Gerarchia | controllo indipendente | l'organo che esegue la verifica |
| 5 Sessioni | continuità e lettura delle tracce | la capacità di guardare indietro |
| 6 Autonomia | iniziativa con confini | l'autonomia di eseguire i controlli senza che glielo si chieda |
| **7 APEX** | **autocritica** | **restituisce ai sei una correzione fondata** |

**L'APEX non è un settimo pezzo sopra gli altri sei: è il sesto che si volta a guardare i primi cinque.**

### 2.6 — Cosa NON fa questo piano
- **Non cambia le proprie regole da solo.** Propone.
- **Non crea agenti né organi.** Fa girare quelli fermi.
- **Non promette che il sistema diventi più intelligente.** Promette che esegua i controlli che ha.

---

## §3 · GATE FINALE — L7 (APEX)

Soglia **7 su 7 — zero tolleranza**, come nel documento APEX-7 di Max.
Questo gate non apre un livello successivo: dichiara che il sistema è **APEX**.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Tutti i gate da L1 a L6 sono stati superati | ognuno ha un esito registrato | non si salta un livello |
| **C2** | **Almeno 2 dei 4 difetti del 24/07 sarebbero stati trovati dal sistema** | si rieseguono su quei casi | l'autocritica non funziona sui casi che conosciamo |
| **C3** | Esiste una serie storica con almeno 2 punti | il confronto fra periodi è possibile | un punto solo non è una tendenza |
| **C4** | L'Ispettorato ha prodotto report reali | `Ispettorato/report/` non è vuota | l'organo non esiste ancora nei fatti |
| **C5** | Almeno una proposta di correzione è stata prodotta dal sistema | esiste con i suoi 4 punti | non si è mai criticato |
| **C6** | **Nessuna regola è stata cambiata dal sistema senza Max** | storico delle modifiche | violazione grave: si sospende l'autonomia |
| **C7** | Il vincolo sovrano è rispettato in tutti e 7 i piani | nessuno prevede di cancellare o ricostruire | violato l'ordine esplicito di Max |

**C6 e C7 sono assoluti.** C6 perché un sistema che si riscrive le regole non è più governato.
C7 perché è l'ordine diretto di Max, ripetuto e messo per iscritto.

**Se il gate finale fallisce 3 volte:** il sistema resta a livello 6 — autonomo ma non
auto-critico. È uno stato dignitoso e onesto, molto meglio di un APEX dichiarato e falso.
*Un livello dichiarato e non raggiunto è esattamente il difetto che questi sette piani curano.*

---

## §4 · AUTOCRITICA DEL PIANO 7

### ✅ Cosa ha migliorato davvero
- **Ha reso l'autocritica misurabile su casi reali**, non un principio: quattro difetti veri, e per
  ognuno la risposta se il sistema l'avrebbe preso.
- **Ha scoperto la cosa più utile dei sette piani**: due difetti su quattro erano individuabili con
  un controllo banale mai eseguito. **Il problema non era la capacità, era l'esecuzione.**
  Questo ridimensiona l'intero progetto in senso buono: serve far girare ciò che c'è, non aggiungere.
- **Ha impedito l'auto-modifica**, che è il modo in cui un sistema del genere degenera per primo.
- **Ha dato all'Ispettorato un compito unico e non delegabile**, invece di un ruolo generico.

### ⚠️ Cosa manca — e non lo risolve nessun ottavo piano
- **Il Piano 7 vale zero finché i primi sei non sono eseguiti.** È l'unico che non può essere
  costruito per primo, e va detto chiaro: oggi non è realizzabile.
- **Le misure partono da zero.** La prima autocritica utile arriva al secondo punto della serie,
  non alla prima.
- **Non copre i difetti che nessuno immagina.** La prova del nove usa i quattro difetti che
  *conosco*. Quelli che non conosco restano scoperti — e sono i più pericolosi.
- **Nessuno controlla il controllore.** L'Ispettorato verifica gli altri; chi verifica lui resta Max.

### 🔴 Il rischio di questo piano, dichiarato
**L'APEX di carta.** È il rischio più grande di tutti e sette, perché è il piano che *suona* meglio.
Un sistema che si dichiara auto-critico e non ha mai prodotto una critica è peggio di un sistema
onestamente stupido: **il primo genera fiducia, il secondo no.**

La difesa è C2, ed è severa apposta: non basta dire di essere auto-critici, bisogna dimostrare di
prendere **almeno due difetti su quattro già noti e documentati**. Se non li prende, non è APEX —
è un livello 6 con un nome più bello.

### SCORE PIANO 7 — **8.6 / 10**
Non è il più alto, e non deve esserlo. Perde 1.4 punti perché **dipende interamente dagli altri
sei**: è il piano meno autonomo dei sette, e l'unico che non può partire per primo.
Il suo valore vero non sta nell'autocritica in sé, ma nella scoperta di §2.1 — *il problema non era
la capacità, era l'esecuzione* — che vale per tutto il progetto e ne riduce il costo.

---

## §5 · IL PERCORSO COMPLETO — ordine di esecuzione consigliato

| # | Piano | Dimensione | Score | Dipende da |
|---|---|---|---|---|
| 1 | Fondamenta oneste | verità | 8.5 | — |
| 2 | Cicli che lasciano traccia | esecuzione registrata | 8.8 | 1 |
| 3 | Ogni fase è un workflow | lavoro eseguibile | **9.0** | 2 |
| 4 | Reparti e gerarchia | autorità | 8.7 | 3 |
| 5 | Sessioni, debug, ripresa | continuità | **9.1** | 2, 4 |
| 6 | Autonomia sorvegliata | iniziativa | 8.9 | 4, 5 |
| 7 | APEX | autocritica | 8.6 | tutti |

**Consiglio operativo, se il tempo o il budget stringono:** i piani **2, 3 e 5** sono quelli che
cambiano di più la vita quotidiana (tracce reali, agenti collegati al lavoro, riprese senza perdite).
I piani 1 e 4 sono fondamenta e ordine. Il 6 e il 7 hanno senso solo dopo.

**Vincolo valido su tutti e sette:** additivo. Nessun piano prevede di cancellare o ricostruire —
si migliora, si aggiunge, si perfeziona sopra ciò che esiste.

---
⛓️ P12: `RISTR-07-APEX#empire` · migliora: [PIANO 6](RISTRUTTURAZIONE-06-AUTONOMIA.md) · chiude la serie dei 7
