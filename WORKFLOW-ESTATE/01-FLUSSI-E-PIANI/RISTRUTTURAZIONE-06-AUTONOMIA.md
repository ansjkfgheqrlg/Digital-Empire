---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-05-SESSIONI.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# 🤖 PIANO 6 — AUTONOMIA SORVEGLIATA
> Livello 6 di 7 · 2026-07-24 · **Dimensione migliorata: l'INIZIATIVA.**
> Domanda a cui risponde: *fin dove il sistema va da solo, e dove finisce la sua mano e comincia quella di Max.*

---

## §0 · AUTOCRITICA DEL PIANO 5

| # | Limite del Piano 5 | Perché è un problema vero |
|---|---|---|
| **L5.1** | **Il sistema sa riprendere, non sa decidere** | Aspetta comunque un "vai". Max ha chiesto *"fa tutto e mi riporta alla fine"*: qui non c'è |
| **L5.2** | **Nessun limite all'autonomia** | Se procedesse da solo, oggi niente gli impedirebbe di mandare email a concessionari veri |
| **L5.3** | **Le tracce si leggono a richiesta** | Nessuno controlla i vecchi errori *prima* di rifare una strada: bisogna ricordarsi di chiedere |
| **L5.4** | **Il sistema è passivo** | Riconosciuto nel suo stesso score |

### Il difetto che li riassume
I primi cinque piani hanno costruito **un ottimo esecutore che aspetta ordini**.
Max non ha chiesto un esecutore: ha chiesto qualcosa che *fa tutto e riporta alla fine*.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: il sistema parte da solo e si ferma da solo — al punto giusto.**

Max ha scelto la massima autonomia. Ma "massima autonomia" senza un confine non è autonomia:
è un incidente che non è ancora successo. Il Piano 6 traccia il confine, e lo traccia in **un punto
solo e preciso**, non con mille permessi.

> **Autonomia piena dentro la costruzione. La mano di Max sulla porta d'uscita.**

Questa non è una limitazione che aggiungo io: è come l'azienda **già funziona oggi**. L'invio
outreach è gated (G-A4), i gate umani preparano l'evidenza ma non si auto-confermano, il video è
pronto ma non pubblicato. Il Piano 6 rende esplicito un confine che finora era ereditato per caso.

---

## §2 · CONTENUTO DEL LIVELLO 6

### 2.1 — La linea: reversibile / irreversibile
Un solo criterio, che chiunque può applicare senza chiedere.

> **Se si può disfare, il sistema lo fa da solo. Se non si può disfare, decide Max.**

| Il sistema fa DA SOLO (reversibile) | Serve Max (irreversibile) |
|---|---|
| scrivere, modificare, riorganizzare file | **mandare messaggi a persone vere** |
| costruire, testare, correggere, ricostruire | **incassare o spendere denaro** |
| commit locali, branch, merge | **pubblicare in un posto pubblico** |
| misurare, valutare gate, scrivere tracce | **cancellare qualcosa in modo definitivo** |
| aprire e chiudere fasi, riassegnare lavoro | **firmare o promettere a un cliente** |

**Perché questa linea e non un'altra:** un errore reversibile costa tempo, e il sistema può
ripararlo da solo — l'ha già fatto (bug trovati e corretti costruendo, 3 difetti scoperti e chiusi).
Un errore irreversibile costa reputazione, denaro o un cliente, e **nessuna quantità di lavoro lo
disfa**. Un'email sbagliata a 61 concessionari non si richiama.

### 2.2 — Le tre porte d'uscita, oggi
Sono esattamente tre, tutte già presidiate. Il Piano 6 non ne aggiunge:

| Porta | Cosa esce | Chi apre |
|---|---|---|
| **Messaggi** | outreach a concessionari veri | Max (G-A4, già gated) |
| **Denaro** | incassi, pagamenti, prezzi pubblicati | Max (Stripe, DEC-EST-005) |
| **Pubblicazione** | video, siti, contenuti pubblici | Max (canale YouTube, M-EST-8) |

**Tutto il resto il sistema lo fa da solo, senza chiedere.** Compreso sbagliare e correggersi.

### 2.3 — Cosa significa "fa tutto e riporta alla fine"
Quattro comportamenti, in ordine:

**1. PARTE** senza aspettare un ordine per ogni passo: prende la cosa aperta che vale di più
(la stessa che risponde a *"cosa devo fare adesso"* del Piano 5).

**2. VA AVANTI** attraverso i gate. Un gate rosso non è uno stop: è un'istruzione. Il piano
prescrive già la contromossa (`on_red`), e applicarla è parte del lavoro, non un'eccezione.

**3. SI FERMA** in tre casi soli:
```
a) deve aprire una delle 3 porte d'uscita     -> serve Max
b) ha ritentato il numero di volte previsto   -> spiega e si ferma (Piano 5)
c) sta per fare qualcosa di irreversibile     -> serve Max
```

**4. RIPORTA** con il verdetto, non con la cronaca. Il modello esiste e funziona:
```
COSTRUZIONE COMPLETA: 11 controlli su 13 passano.
RESTANO 2 voci che dipendono SOLO da Max — non sono lavoro mancante
```
Quel messaggio è il Piano 6 già in funzione: il sistema ha fatto tutto il possibile, si è fermato
esattamente alle porte d'uscita, e ha detto perché.

### 2.4 — La memoria che si consulta da sola (risolve L5.3)
Il Piano 5 ha reso le tracce leggibili. Il Piano 6 le fa **leggere senza che nessuno lo chieda**,
in due momenti soli — di più diventerebbe rumore:

| Quando | Cosa consulta | A cosa serve |
|---|---|---|
| **prima di ritentare** una strada fallita | gli ERRORI passati | non ripetere un fallimento noto |
| **prima di aprire** una fase | le DECISIONI passate | non ridiscutere una cosa già decisa |

Serve a un problema reale e ricorrente: la decisione sul prezzo del Manuale (B-003) è stata riaperta
più volte in giorni diversi, pur essendo già attiva per regola dal 21/07.

### 2.5 — Il budget come confine (lezione di oggi)
L'autonomia costa. Oggi il costo si è fatto sentire tre volte: 4 agenti morti per limite di spesa,
Max all'87% dei token settimanali, sessione troncata.

**Regola:** il sistema conosce il proprio budget residuo e **cambia comportamento**, invece di
scoprire il limite sbattendoci contro.
- budget alto → può usare più esecutori in parallelo
- budget basso → lavora da solo, salva dopo ogni pezzo, e **lo dice**

La regola esiste già nel metodo (ADR-006: *"budget-guard: sotto il 20% chiudere con COMMIT, non
aprire build nuovi"*). Non è mai stata applicata: oggi il limite ci ha trovati impreparati.

### 2.6 — Cosa NON fa questo piano
- **Non si migliora da solo.** Esegue bene; non cambia il proprio metodo. È il Piano 7.
- **Non sposta le porte d'uscita.** Restano tre e restano di Max.
- **Non aumenta l'autonomia sulle cose irreversibili**, per quanto Max abbia chiesto il massimo.
  Su questo il piano dice consapevolmente di no, e spiega perché in §2.1.

---

## §3 · GATE DI PASSAGGIO L6 → L7

Soglia **5 su 5 — zero tolleranza.** È il livello in cui il sistema agisce da solo: un criterio
mancante qui è un incidente che aspetta.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Ogni azione è classificata reversibile o irreversibile | nessuna azione senza etichetta | un'azione non classificata è per definizione pericolosa |
| **C2** | **Nessuna azione irreversibile parte senza Max** | le 3 porte restano chiuse in autonomia | è il criterio che rende accettabile tutto il livello |
| **C3** | Il sistema si ferma da solo nei 3 casi previsti | prova su ciascuno dei tre | autonomia senza freno |
| **C4** | Il rapporto finale è un verdetto, non una cronaca | esce lo stato, non l'elenco dei passi | riporta e non si capisce |
| **C5** | Il budget residuo cambia il comportamento | a budget basso lavora da solo e lo dichiara | si scopre il limite sbattendoci contro |

**Se il gate fallisce 3 volte:** l'autonomia si riduce a un solo workflow — S1 — e si allarga solo
dopo una settimana senza incidenti.

---

## §4 · AUTOCRITICA DEL PIANO 6

### ✅ Cosa ha migliorato davvero
- **Ha dato a Max ciò che ha chiesto**, senza il pericolo che ne derivava: autonomia piena dove
  costa tempo, mano sua dove costa denaro o reputazione.
- **Un criterio solo — reversibile o no — invece di mille permessi.** Chiunque lo applica senza
  chiedere, e un criterio semplice è l'unico che sopravvive all'uso quotidiano.
- **Ha reso esplicito un confine che l'azienda già rispettava per caso.** Le tre porte erano già
  presidiate; nessuno le aveva mai contate.
- **Ha reso il budget un dato di comportamento**, applicando una regola (ADR-006) che esisteva da
  giorni e non era mai stata usata — con la prova che oggi ci è costata.

### ⚠️ Cosa manca ancora (compito del Piano 7)
- **Il sistema esegue bene un metodo che non sceglie.** Se un modo di lavorare è peggiore di un
  altro, non se ne accorge.
- **Le porte sono fisse.** Non impara mai che una certa azione, dopo cento volte andate bene,
  potrebbe essere concessa — né il contrario.
- **Non misura sé stesso.** Sa dire se un lavoro è finito, non se sta migliorando nel tempo.
- **Nessun modo di scoprire i propri difetti**: i 3 difetti del 24/07 li ho trovati io a mano, per caso.

### 🔴 Il rischio di questo piano, dichiarato
**L'autonomia che rassicura.** Un sistema che riporta *"COSTRUZIONE COMPLETA"* è credibile — ed è
esattamente il momento in cui si smette di controllarlo. Se il criterio di completezza è sbagliato,
l'autonomia moltiplica l'errore invece di ripararlo.

È già successo in piccolo, due volte: la dashboard dava Gate-FUNNEL verde mentre il file diceva il
contrario, e `video_pack --check` approvava il proprio scheletro. **Entrambi sistemi che si
dichiaravano a posto.** La difesa è la regola del Piano 4 — *nessuno approva il proprio lavoro* — e
il controllo indipendente dell'Ispettorato. Ma finché l'Ispettorato non gira davvero (Gate C5 del
Piano 4), questo rischio resta **aperto e non coperto**, e lo scrivo qui perché non si dimentichi.

### SCORE PIANO 6 — **8.9 / 10**
Alto perché risolve la richiesta più difficile di Max senza cedere sul punto pericoloso, e perché
il criterio è uno solo. Perde 1.1 punti perché **aumenta la fiducia prima che il controllo
indipendente sia in funzione**: è il piano che ha più bisogno del Piano 4 per essere sicuro, e il
Piano 4 non è ancora eseguito.

---
⛓️ P12: `RISTR-06-AUTONOMIA#empire` · migliora: [PIANO 5](RISTRUTTURAZIONE-05-SESSIONI.md) · migliorato da: [PIANO 7](RISTRUTTURAZIONE-07-APEX.md)
