# ADR-018 — Due decisioni portano il numero 012, e due motori sono canonici insieme

- **Stato:** ATTIVO (disambiguazione immediata) + **DECISIONE APERTA per Max** (§4)
- **Data:** 2026-09-03
- **Scoperto da:** lo scagnozzo incaricato di riempire le sentinelle, mentre travasava i 16 ADR
  dentro `sentinel-drift` — il guardiano che esiste proprio per impedire questo genere di deriva
- **Non risolve:** quale motore di orchestrazione sia quello buono. Vedi §4.

---

## 1. Il guasto

Nella cartella delle decisioni **due file portano il numero 012**:

| File | Data | Deciso da | Argomento |
|---|---|---|---|
| `ADR-012-ponte-memory-wiki.md` | **23 agosto 2026** | Max | il ponte fra `company/Memory/` e la wiki |
| `ADR-012-orchestration-layer-canonico.md` | **26 agosto 2026** | Neri, via Emperator Agent | un nuovo motore di orchestrazione |

**Quindici file citano "ADR-012" senza dire quale dei due.** Fra questi: `STATO-EMPIRE.md`,
`INDEX.md`, due checkpoint, il README di `11-APEX-7-CORE`, tre agenti del CTO, e — con una certa
ironia — `sentinel-drift` e `guild-quality`, cioè proprio i due che dovrebbero accorgersene.

---

## 2. Il guasto sotto il guasto — e questo è il grave

Il secondo dei due, quello del 26 agosto, **dichiara da sé di contraddire le decisioni
precedenti**. Testuale dal suo stesso testo:

> *«ADR-010/ADR-011 già impongono un solo motore di orchestrazione canonico,
> `company/Ecosistemi/11-APEX-7-CORE/`, e vietano nuove linee divergenti fuori da quella
> cartella (ADR-011 aveva già censito 6 linee parallele come problema…)»*

E il suo stato, sempre testuale: **«Fase 1 (innesto) completata, Fase 2 (migrazione consumatori)
NON iniziata»**.

Messo insieme, questo significa:

> **Digital Empire ha oggi due motori di orchestrazione entrambi dichiarati canonici, e la
> migrazione che avrebbe dovuto ridurli a uno non è mai partita.** Dura da **otto giorni**
> (26 agosto → 3 settembre) senza che nessuno se ne accorgesse.

ADR-011 aveva censito **sei** linee parallele di orchestrazione come un problema da chiudere.
La settima è entrata tre giorni dopo, con un ADR che lo dice apertamente nel proprio testo.

---

## 3. Cosa decido io, subito — la disambiguazione

**Fino a nuovo ordine, un riferimento a "ADR-012" senza altra indicazione significa
`ADR-012-ponte-memory-wiki` (23 agosto).** Motivo: è il primo per data, è di Max, ed è quello
citato dalla maggior parte dei quindici puntatori esistenti.

**L'altro si cita sempre per nome completo**: `ADR-012-orchestration-layer-canonico`.

**La rinumerazione dei file NON viene fatta ora.** Rinominare a macchina significa toccare
quindici puntatori senza sapere, per ciascuno, a quale dei due si riferisse: la probabilità di
lasciarne uno rotto è concreta, e un puntatore rotto è peggio di nessun puntatore perché manda a
sbattere invece di far cercare (regola puntatori, `CLAUDE.md`). Va fatta **a mano, un puntatore
alla volta**, quando Max avrà deciso il §4 — perché la decisione del §4 potrebbe rendere uno dei
due un ADR superato, e allora la rinumerazione sarebbe lavoro diverso.

Voce di backlog aperta: **B-046**, con l'elenco esatto dei quindici file.

---

## 4. ⚠️ LA DECISIONE CHE SPETTA A MAX — non la prendo io

**Quale motore di orchestrazione è quello canonico?**

Non la prendo io, e dico perché — perché rifiutare una delega va motivato:

1. **È lavoro di Neri.** L'ADR del 26 agosto nasce da un progetto che Neri ha portato e
   costruito. Cancellarlo o declassarlo senza di lui è una decisione sulla persona, non sul
   codice, e non è nel mio mandato.
2. **Tocca codice vivo.** `11-APEX-7-CORE` e `orchestration-layer` sono entrambi innestati.
   Scegliere significa migrare o buttare lavoro reale, non riscrivere un documento.
3. **Nessuna delle due parti è stata misurata.** Non esiste un confronto fra i due motori su
   dati veri: solo due ADR che si dichiarano canonici a vicenda. **Scegliere adesso sarebbe
   scegliere a caso con l'aria di decidere** — e questo è esattamente ciò che ADR-017 esiste
   per impedire.

**Le tre strade, con il loro costo:**

| Strada | Cosa comporta |
|---|---|
| **A — `11-APEX-7-CORE` resta il solo canonico** | Coerente con ADR-010/011. Il lavoro di Neri va assorbito o archiviato: va detto a Neri, e va detto bene. |
| **B — `orchestration-layer` diventa il canonico** | Va scritto un ADR che **supera esplicitamente** ADR-010 e ADR-011, e va fatta davvero la Fase 2 di migrazione, che oggi non è iniziata. |
| **C — Convivenza dichiarata** | Legittima solo se si scrive **chi fa cosa** e dove passa il confine. Oggi non c'è: due canoni senza confine non sono convivenza, sono confusione. |

**La mia raccomandazione, se la vuoi:** **A**, ma non prima di aver parlato con Neri, e non come
bocciatura del suo lavoro — l'ADR che ha scritto è documentato meglio di molti altri in questa
cartella, e la sua onestà nel dichiarare da sé la contraddizione è esattamente il comportamento
che vogliamo. Il problema non è la qualità di quel lavoro: è che è entrato senza che nessuno
chiudesse la porta di quello precedente.

---

## 5. La lezione, che vale oltre questo caso

**`sentinel-drift` esiste per impedire esattamente questo, e non l'ha impedito** — perché fino a
oggi era un file da 39 righe che non conteneva l'elenco degli ADR che doveva far rispettare. Un
guardiano che non conosce il regolamento non sorveglia niente: guarda passare tutto.

Il guasto è stato trovato solo il giorno in cui qualcuno ha travasato i 16 ADR dentro quel
guardiano. **Non è una coincidenza: è la dimostrazione che riempire i guardiani serviva davvero,**
e la prima cosa che ha trovato è un conflitto rimasto aperto otto giorni sotto gli occhi di tutti.

> **Un controllo vuoto non è un controllo debole: è un controllo che mente**, perché tutti
> credono che qualcuno stia guardando.

---

*Legami: [[ADR-010]] · [[ADR-011]] · `ADR-012-ponte-memory-wiki` · `ADR-012-orchestration-layer-canonico` ·
[[ADR-017]] (non scegliere senza misura) · `.claude/agents/sentinel-drift.md` ·
`company/Memory/BACKLOG.md` voce B-046*
