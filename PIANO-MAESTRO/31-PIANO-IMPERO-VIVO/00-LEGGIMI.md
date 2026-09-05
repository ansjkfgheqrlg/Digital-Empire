# 🜂 PIANO IMPERO VIVO — leggimi per primo

> **Aperto:** 2026-09-06 · **Committente:** Max · **Esecutore:** EMPERATOR
> **Assetto:** GOD EMPEROR DOOM · **Ripresa:** EMP-MCC4
> **Stato:** V1 in costruzione

---

## 1. L'ORDINE, NELLE PAROLE DI MAX

> *«L'obiettivo è finire la costruzione di tutta l'azienda Digital Empire e poi rendere quel
> 18% vivo. Quel 18% deve diventare 100%. Senza eliminare niente, senza togliere niente. Se
> c'è qualcosa che non si rende vivo facilmente, risolviamo, facciamo problem solving. Ma la
> cosa più importante, oltre a far diventare tutto vivo al 100%, è che tutto sia collegato,
> perché è un'azienda dove tutto è collegato: reparti, controlli, comunicazioni tra i vari
> reparti, tra i vari ecosistemi, tra i vari flussi. Tutte le comunicazioni interne ci devono
> essere, un collegamento di informazioni, tutto. Dobbiamo procedere con calma, con cautela,
> alla massima performance, nel modo più chirurgico e attento possibile.»*

E sul metodo:

> *«Il piano è tutto. Un piano talmente perfetto, migliorato anche 20 volte, anche 40, per
> avere un risultato one shot: un risultato buono, valido, performante subito. Non dobbiamo
> fermarci a pianificare l'idea. Devi fare un piano generale specifico nel minimo dettaglio,
> poi analizzarlo completamente, criticarlo — avrà migliaia di problemi, è normale — e rifarlo
> più grande e più ampio. Poi criticare di nuovo. Poi espandere ogni minimo dettaglio.»*

---

## 2. LE SETTE LEGGI DEL PIANO (valgono per ogni versione)

Queste non si negoziano, non si votano, non si aggirano. Ogni riga di ogni versione del piano
deve poter essere messa contro queste sette leggi e passare.

**L1 — NIENTE SI SCARTA.**
Nessun agente si cancella perché «documentale». Nessun ecosistema si declassa perché «è solo
carta». Nessun workflow si chiude perché «non è mai partito». L'unica rimozione ammessa è il
**duplicato accidentale**, e anche lì si **fonde**, non si butta: il pezzo più vecchio diventa
archivio d'origine, non spazzatura.
> *Perché è la prima legge:* il 5 settembre stavo per «fondere una cartella vuota» che vuota
> non era — conteneva l'archivio originale del bot Solana. L'audit del 31 agosto la dichiarava
> vuota e io citavo l'audit invece di aprirla. **Si apre sempre, prima di scriverne il destino.**

**L2 — VIVO SIGNIFICA UNA COSA SOLA, E SI MISURA.**
Un artefatto è vivo quando: (a) si può **invocare** con un comando dichiarato; (b) produce
un'**uscita conforme a un contratto scritto**; (c) quell'uscita **finisce in un posto stabilito**;
(d) esiste un **test che lo prova** e che si può rilanciare. Meno di quattro su quattro: non è
vivo, è descritto.

**L3 — COLLEGATO È PARTE DI VIVO, NON UN EXTRA.**
Un artefatto che gira ma non riceve da nessuno e non consegna a nessuno **non conta come
chiuso**. Ogni nodo dell'Impero deve avere almeno un ingresso dichiarato e almeno un'uscita
dichiarata, con il contratto che li descrive e la traccia che li registra.

**L4 — SI AVVOLGE, NON SI RISCRIVE (ADR-003).**
I motori che già funzionano restano dove sono, com'erano. Il lavoro è dare loro un punto
d'ingresso e un contratto, mai rifarli. Un sistema attivo non si tocca finché il sostituto non
è validato.

**L5 — NESSUN GATE SI DICHIARA, SI ESEGUE.**
Ogni pezzo di piano finisce con un comando che si può lanciare e un output atteso. «Fatto»
senza comando non esiste. Se un gate non passa si dice **perché** — non si sposta il gate.

**L6 — OGNI COSA HA UN PROPRIETARIO, UN CONTROLLORE E UN POSTO NELL'ANAGRAFE (ADR-008).**
Nessun artefatto orfano. Chi lo possiede, chi lo giudica, da dove viene, quale articolo del
Mandato lo governa. Un pezzo che nessun registro conosce è un pezzo di azienda che non
esiste.

**L7 — SI SCRIVE CIÒ CHE SI È MISURATO.**
Ogni numero del piano nasce da un comando lanciato o da un file aperto, e porta la sua fonte.
Dove c'è un giudizio e non una misura, va scritto che è un giudizio. **Un piano costruito su
un audit non verificato è il modo esatto in cui questo Impero ha già sbagliato.**

---

## 3. IL METODO — QUATTRO VERSIONI, TRE CRITICHE

Ordine di Max: il risultato deve essere **one shot**. Si paga in pianificazione ciò che non si
vuole pagare in rifacimenti.

```
   CENSIMENTI (4 doom bot, in parallelo)
        │   cosa deve diventare vivo · i collegamenti · le forze · i motori reali
        ▼
   ┌──────────────┐
   │  V1 GENERALE │  tutto ciò che va fatto, specifico, con l'architettura della soluzione
   └──────┬───────┘
          ▼
   ✂ CRITICA 1 — revisori indipendenti, modello diverso dal mio (ADR-017)
          │        cercano: ciò che non ho considerato, ciò che ho dato per vero senza provarlo,
          │        ciò che si romperebbe al primo contatto con la realtà
          ▼
   ┌──────────────┐
   │  V2 AMPLIATA │  più grande e più profonda: architettura di ogni pezzo, organizzazione
   └──────┬───────┘   delle forze, regolamento, addestramento, direzione
          ▼
   ✂ CRITICA 2 — più dura della prima, sulle scelte architetturali, non sulle sviste
          ▼
   ┌──────────────┐
   │  V3 BASE     │  il piano assestato: ultra-architettato, ultra-specifico, ma ancora base
   └──────┬───────┘
          ▼
   ✂ CRITICA 3 (opzionale, se V3 regge si salta)
          ▼
   ┌──────────────────────┐
   │  V4 ESECUTIVO        │  l'espansione: ogni dettaglio, ogni file, ogni comando, ogni gate,
   │  (più documenti)     │  ogni prompt di ingaggio. Da qui si costruisce senza più pensare.
   └──────────────────────┘
```

**Regola delle critiche:** chi critica **non** è chi ha scritto. Modello diverso dove possibile
(ADR-017). Il critico non propone lo stile: cerca il **difetto che costerebbe caro**, e per ogni
rilievo deve dire *dove* il piano si romperebbe e *con quale conseguenza*.

**Regola delle versioni:** una versione non sovrascrive la precedente. `V1` resta leggibile
accanto a `V2`. Le critiche restano in `_critica-vN/`. Si deve poter sempre rispondere alla
domanda «perché il piano dice questo e non quello».

---

## 4. COSA CONTIENE QUESTA CARTELLA

| Percorso | Cosa è | Stato |
|---|---|---|
| `00-LEGGIMI.md` | questo file: ordine, leggi, metodo, avanzamento | ✅ |
| `dati/censimento-01-vivo.md` | cosa deve diventare vivo, nodo per nodo | 🔄 in corso |
| `dati/censimento-02-collegamenti.md` | chi parla con chi oggi, chi dovrebbe | 🔄 in corso |
| `dati/censimento-03-forze.md` | popolazione agenti, contratto C4, regolamento delle forze | 🔄 in corso |
| `dati/censimento-04-motori.md` | tutto ciò che già gira fuori da `company/` | 🔄 in corso |
| `V1-PIANO-GENERALE.md` | prima versione | ⬜ |
| `_critica-v1/` | i rapporti dei revisori su V1 | ⬜ |
| `V2-PIANO-AMPLIATO.md` | seconda versione | ⬜ |
| `_critica-v2/` | i rapporti su V2 | ⬜ |
| `V3-PIANO-ASSESTATO.md` | terza versione | ⬜ |
| `V4-ESECUTIVO/` | il piano esecutivo espanso, in più documenti | ⬜ |

---

## 5. RAPPORTO CON I PIANI CHE ESISTONO GIÀ

Questo piano **non cancella niente** (L1) e non riparte da zero:

- **[Dossier 30](../30-PIANO-COMPLETAMENTO-IMPERO.md)** — la misura del 5 settembre (92% carta /
  18% vivo) e i sette scaglioni S1..S7. **Resta valido come misura**; i suoi scaglioni verranno
  assorbiti e riordinati dentro V1, non buttati. La sua lacuna dichiarata — copre «vivo», non
  copre «collegato» — è la ragione per cui questo piano esiste.
- **[TASK-MAX-20260831-IMPERO-OPERATIVO](../../company/Memory/tasks/TASK-MAX-20260831-IMPERO-OPERATIVO.md)**
  — la task madre, blocchi B0..B8. Resta la fonte dei blocchi. **Ma va riverificata riga per
  riga:** ha già mentito una volta (la «cartella vuota» che non era vuota).
- **[Dossier 08 — Roadmap F1..F12](../08-ROADMAP-FASI.md)** — la roadmap originale. F1-F3 sono
  la carta (fatta), F4-F12 sono la vita (da fare). Questo piano è il modo di attraversare F4-F12.
- **[Dossier 29 — ECOSISTEMA LANCI](../29-ECOSISTEMA-LANCI/00-LEGGIMI.md)** — piano v4 pronto,
  in attesa di ADR-023. Non parte prima che un flusso vero abbia chiuso un ciclo.
- **ADR attivi** — nessuno viene contraddetto. Se il piano avesse bisogno di superarne uno, lo
  dichiara e propone l'ADR nuovo: mai in silenzio.

---

## 6. LE FORZE SCHIERATE SU QUESTO PIANO

Ogni attivazione è dichiarata per iscritto (ADR-015). Questa tabella si aggiorna a ogni schieramento.

| Data | Grado | Nome | Compito | Uscita | Esito |
|---|---|---|---|---|---|
| 2026-09-06 | DOOM BOT (opus) | CENSIMENTO-VIVO | cosa deve diventare vivo, nodo per nodo | `dati/censimento-01-vivo.md` | ❌ **CADUTO** (rete) — 12 righe salvate su ~500 |
| 2026-09-06 | DOOM BOT (opus) | CENSIMENTO-COLLEGAMENTI | chi parla con chi, oggi e in progetto | `dati/censimento-02-collegamenti.md` | 🔄 |
| 2026-09-06 | DOOM BOT (opus) | CENSIMENTO-FORZE | popolazione agenti, contratto C4, regolamento | `dati/censimento-03-forze.md` | ❌ **CADUTO** (ECONNRESET) — 3 righe salvate |
| 2026-09-06 | DOOM BOT (opus) | CENSIMENTO-MOTORI | tutto ciò che gira fuori da `company/` | `dati/censimento-04-motori.md` | 🔄 |
| 2026-09-06 | DOOM BOT (opus) | 01A-ECOSISTEMI | i 15 ecosistemi, scheda per scheda | `dati/censimento-01a-ecosistemi.md` | 🔄 |
| 2026-09-06 | DOOM BOT (opus) | 01B-ORGANI | Board, Guilds, Sentinelle, MAXIMILIAN, Mandato, Ispettorato | `dati/censimento-01b-organi.md` | 🔄 |
| 2026-09-06 | DOOM BOT (opus) | 03A-POPOLAZIONE | i due censimenti agenti, la specifica C1..C6, le ondate | `dati/censimento-03a-popolazione.md` | 🔄 |
| 2026-09-06 | DOOM BOT (opus) | 03B-REGOLAMENTO | cadute reali → regolamento, addestramento, modulo d'ingaggio | `dati/censimento-03b-regolamento-forze.md` | 🔄 |

### ⚠️ Prima lezione del piano, pagata sul campo (2026-09-06)

Due doom bot su quattro sono caduti per un guasto di rete (`server_error` e `ECONNRESET`)
**dopo aver raccolto tutti i dati e prima di averne scritto uno**. Il file di uscita c'era —
l'avevano creato come ordinato — ma conteneva solo l'intestazione: 12 righe su circa 500, e 3.
Tutto il lavoro perso.

**L'ordine era giusto e insufficiente.** Dicevo *«crea subito il file e riscrivilo a ogni
sezione completata»*: un agente che considera «una sezione» l'intero censimento la rispetta
alla lettera e muore con tutto in mano.

**Regola corretta, ora in vigore per ogni forza schierata:**
> **Non tenere mai in testa più di una scheda.** Finita una scheda — un ecosistema, un organo,
> una sezione — **si scrive su disco immediatamente**, poi si passa alla successiva. Se la
> forza cade alla settima, le sei precedenti devono essere già salvate.

E, insieme: **perimetri più piccoli.** I due caduti avevano un compito grande; sono stati
rischierati in quattro, ciascuno con meno terreno. Un doom bot con meno da tenere in mano cade
meno, e quando cade perde meno.


---

## 7. AVANZAMENTO

| Tappa | Stato | Data |
|---|---|---|
| Leggi e metodo fissati | ✅ | 2026-09-06 |
| Quattro censimenti | 🔄 in corso | 2026-09-06 |
| V1 — piano generale | ⬜ | |
| Critica 1 | ⬜ | |
| V2 — piano ampliato | ⬜ | |
| Critica 2 | ⬜ | |
| V3 — piano assestato | ⬜ | |
| V4 — piano esecutivo | ⬜ | |
| **Via alla costruzione** | ⬜ | **solo dopo V4, per ordine di Max** |

**Divieto in vigore fino a V4:** nessuna modifica costruttiva al repository. Ordine esplicito
di Max del 2026-09-06 — *«non puoi adesso iniziare a modificare, fare piccole cose, quando poi
nel complesso magari andranno a intralcio»*. Si scrive il piano. Si legge, si misura, si
progetta. **Non si tocca.**
