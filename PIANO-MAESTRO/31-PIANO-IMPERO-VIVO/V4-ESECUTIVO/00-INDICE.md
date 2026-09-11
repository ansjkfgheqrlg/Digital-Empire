# 🜂 V4 — PIANO ESECUTIVO: DA QUI SI COSTRUISCE SENZA PIÙ PENSARE

> **Versione:** 4 di 4 · **Aperta:** 2026-09-11 · **Autore:** EMPERATOR · **Committente:** Max
> **Base:** `V3-PIANO-ASSESTATO.md` (chiusa il 2026-09-10: 13 correzioni + Appendici B/C/D) sopra
> `V2-PIANO-AMPLIATO.md` (il corpo). V4 **non ridiscute niente**: espande. Ogni scaglione diventa un
> documento con comandi esatti, file esatti, gate eseguibili e prompt d'ingaggio già scritti.
> **Regola d'oro di V4:** se per eseguire un passo serve *pensare*, il passo è scritto male — si
> torna qui e lo si riscrive finché basta *leggere*.
> **Stato:** IN SCRITTURA. Il **divieto di modifiche costruttive resta in vigore** finché questo
> indice non segna tutti i documenti ✅ e Max non dice «via alla costruzione».

---

## 1. LE LEGGI CHE OGNI DOCUMENTO DI V4 DEVE RISPETTARE (non si ripetono nei documenti: si citano)

| Legge | Dove è scritta | Cosa impone a ogni scaglione |
|---|---|---|
| **L1–L7** | `00-LEGGIMI.md` §2 | niente si scarta · vivo = 4/4 · collegato è parte di vivo · si avvolge non si riscrive · un gate si esegue · ogni cosa ha proprietario/controllore/anagrafe · si scrive ciò che si è misurato |
| **L8–L10** | V2 §2 | ARCHIVIO è uno stato · un gate = comando+condizione+exit code · ogni cardinale porta i nomi |
| **LC-vivo / LC-portata** | V3 §1 | ogni funzione dichiara il consumatore quotidiano; le funzioni-flusso (F1, F2, F3) misurano la **portata** (fatti serviti nella finestra), non l'età del rapporto |
| **Contratto d'innesto** | V3 §4 | ogni innesto su un file vivo porta: politica di guasto (fail-open/closed), gate di regressione dell'ospite, piano di rientro, migrazione dei chiamanti con finestra warning→blocco |
| **Stato a due tempi** | V3 §5 | `NEW → SENDING → CONTACTED`; il lead in `SENDING` alla ripresa va a riconciliazione umana, mai risolto d'ufficio |
| **`fonte_di_verita` per coppia** | V3 §6 | ogni coppia scheda↔esecutore dichiara quale lato è la fonte; la guardia blocca l'edit del lato generato |
| **Tre esiti** | V3 §7 | `PASSA / NON PASSA / NON VALUTATO` — i NON VALUTATO non entrano né al numeratore né al denominatore, e ognuno ha la riga che dice perché |
| **HC-v2 a 13 campi** | V3 Appendice D | i 10 di V2 §12 + `due_at` (opzionale) + `costi` (obbligatorio per esecutori-agente) |
| **H13 — legge di nascita** | V3 §3 | ogni artefatto nuovo nelle classi censite nasce con `Consumatore quotidiano` + ingresso in anagrafe, o il pre-commit lo respinge |
| **ADR-028 — niente blocca tutto** | `CLAUDE.md` REGOLA DUE | un impedimento ferma solo ciò che dipende letteralmente da lui; ogni «bloccato» nel documento elenca anche cosa NON è bloccato |
| **INV-GAEL** | V3 §8 / §19 | **E5b è l'unico scaglione che aspetta Gael, e nessun altro scaglione dipende da E5b.** Nessun documento di V4 può introdurre una dipendenza nuova da Gael. Chi la trova, la scrive come violazione e la toglie |
| **Perimetro 16, non 15** | V3 Appendice B punto 6 | gli ecosistemi sul disco sono 16 e il numero 08 è doppio: `empire vivo --json` non nasce prima che `REGISTRO-NUMERI.md` sia sanato (passo di E0.5) |
| **Divieto costruttivo** | EMP-MCC4 §1 | fino al «via» di Max, V4 è carta: nessun documento contiene lavoro già eseguito, solo lavoro pronto da eseguire |

---

## 2. L'ORDINE DI ESECUZIONE — venti scaglioni, un documento ciascuno

L'ordine viene da V3 §10 con le tre inversioni corrette (E0b dopo E0.5; E0.9 prima di E1; F3 prima
di E3). **La colonna «Dipende da» è l'unica verità sull'ordine**: chi esegue segue questa tabella,
non la numerazione dei nomi.

| # | Scaglione | Documento | Chi | Ore (V3) | Tetto | Dipende da | Stato doc |
|---|---|---|---|---|---|---|---|
| 1 | **E0a — La merce** | `01-E0a-MERCE.md` | Max | 1-1,5 | 2,5 | — | ⬜ |
| 2 | **E0.5 — Gli agganci a costo zero** | `02-E0.5-AGGANCI.md` | EMPERATOR | 4-6 | 9 | — | ⬜ |
| 3 | **E0b — La rotazione** | `03-E0b-ROTAZIONE.md` | Max | 0,5-1 | 1,5 | E0.5 (gate_rotazione.py, INCASSO via HTTP) | ⬜ |
| 4 | **E0.9 — L'atto di vendita** | `04-E0.9-ATTO-DI-VENDITA.md` | Max decide, EMPERATOR esegue | 2-4 | 6 | E0a, E0.5 | ⬜ |
| 5 | **E0.6 — Le regole che si contraddicono** | `05-E0.6-REGOLE.md` | EMPERATOR + Max | 2-3 | 4,5 | — | ⬜ |
| 6 | **E0.7 — I tredici hook** | `06-E0.7-HOOK.md` | EMPERATOR | 6-10 | 15 | E0.6 | ⬜ |
| 7 | **E1 — Il perimetro pulito** | `07-E1-PERIMETRO.md` | EMPERATOR | 13-20 | 30 | E0.7 (H7, H11 attivi), decisione albero canonico | ⬜ |
| 8 | **E2 — La rinomina + 235 destinazioni** | `08-E2-RINOMINA.md` | EMPERATOR | 47-73 | 110 | E1 | ⬜ |
| 9 | **F3 — L'emettitore unico** (estratto da E4) | `09-F3-EMETTITORE.md` | EMPERATOR | 3-5 | 7,5 | E0.7 | ⬜ |
| 10 | **E3.0 — Riaccendere Preventa** | `10-E3.0-RIACCENSIONE.md` | Neri + EMPERATOR | 3-6 | 9 | — | ⬜ |
| 11 | **E3 — La fetta verticale** | `11-E3-FETTA-VERTICALE.md` | Neri + EMPERATOR | 12-18 | 27 | F3, E3.0 | ⬜ |
| 12 | **E4 — Le funzioni innestate (F4, F5, F2, F1)** | `12-E4-FUNZIONI.md` | EMPERATOR | 9-15 | 22,5 | F3, E0.5, E0.7 | ⬜ |
| 13 | **E5a — Il generatore** | `13-E5a-GENERATORE.md` | EMPERATOR | 8-15 | 22 | E1, E0.7 (H4) | ⬜ |
| 14 | **E5-bis — L'adozione dei 162** | `14-E5bis-ADOZIONE.md` | EMPERATOR | 20-40 | 60 | E5a | ⬜ |
| 15 | **E5b — I punti d'ingresso** | `15-E5b-INGRESSI.md` | EMPERATOR + Gael | 15-45 | 67 | **risposta di Gael** (default: non si costruisce) | ⬜ |
| 16 | **E5c — F1 popolata** | `16-E5c-F1-POPOLATA.md` | EMPERATOR | 10-20 | 30 | E4-F1, E5-bis | ⬜ |
| 17 | **E6 — Tre ecosistemi senza motore + APEX-7** | `17-E6-SENZA-MOTORE.md` | EMPERATOR | da stimare, tetto 30 | 30 | E4 | ⬜ |
| 18 | **E7 — Le ondate** | `18-E7-ONDATE.md` | EMPERATOR | 69-109 | 163 | E2, E5-bis (perimetro `fonte=scheda`) | ⬜ |
| 19 | **E8 — La consegna e gli orfani** | `19-E8-CONSEGNA.md` | Max + EMPERATOR | 10-20 | 30 | E0.9 (canale di vendita) | ⬜ |
| 20 | **E9 — L'auto-miglioramento** | `20-E9-AUTOMIGLIORAMENTO.md` | EMPERATOR | — | — | E3, E4, E5 | ⬜ |
| | **Totale** | | | **~230-395 h** | | **12-24 settimane** | |

**Cosa può correre in parallelo (ricognizione o proprietari diversi, percorsi disgiunti):** E0a‖E0.5‖E0.6
(giorno uno, tre proprietari) · E3.0 (Neri) ‖ E1 (EMPERATOR) · E5b non è mai sul cammino critico.
**Cosa è sequenziale per legge (§18):** tutto ciò che scrive in `company/**` (E1, E2, E5-bis, E7) —
un solo scrittore per volta, daemon di sync sospeso durante E1 ed E2.

---

## 3. IL TEMPLATE OBBLIGATORIO DI OGNI DOCUMENTO DI SCAGLIONE

Un documento che salta una sezione non è finito. Le sezioni, in quest'ordine:

```
# <numero> — <NOME SCAGLIONE>
> Chi · Ore V3 · Tetto · Dipende da · Percorsi in scrittura (elenco esatto) · Politica di guasto

## 0. Cosa NON è bloccato da questo scaglione (ADR-028)
   Elenco di cosa procede comunque se questo scaglione si ferma.

## 1. Prerequisiti — verificati con un comando, non dichiarati
   Per ogni prerequisito: <comando> → <output atteso> → <exit code>.

## 2. I passi — numerati, ognuno con il comando esatto
   Un passo = un'azione = un comando (o un edit con file:riga e testo esatto).
   Mai «configura X»: sempre il contenuto da scrivere.
   Per i passi che toccano un file vivo: il contratto d'innesto (V3 §4) compilato.

## 3. Il gate — comando, condizione di fallimento, exit code (L9)
   Blocco di comandi copiabile. Se il comando non esiste ancora, la sua specifica
   (nome, argomenti, condizione) è un passo di §2, non una promessa.

## 4. Politica di guasto e piano di rientro
   Cosa succede se un passo fallisce a metà: fail-open o fail-closed (motivato col
   danno peggiore), il comando di rientro, cosa si dichiara e dove.

## 5. Le forze — chi fa cosa, e il prompt d'ingaggio già scritto
   Se lo scaglione delega a scagnozzi/sentinelle/doom bot: il prompt COMPLETO, copiabile,
   con la regola di scrittura incrementale e i percorsi. Se lo fa EMPERATOR da solo: «nessuna».

## 6. Cosa si scrive in Memory alla chiusura
   Titolo del checkpoint, riga per STATO-EMPIRE, ADR se ne nasce una, i sei numeri del
   cruscotto (V2 §23) prima e dopo.
```

**Divieti di scrittura:** niente `~` davanti a un numero che decide un perimetro (L10) · niente
«bloccato» senza la lista di cosa non lo è (ADR-028) · niente gate «si verifica a mano e lo si
dichiara» (V3 §2, il caso E0 che ha generato E0b) · niente target di righe a una forza: si dà la
lista di cose da coprire (lezione EMP-8M9F, errore 2).

---

## 4. I GATE GLOBALI — quelli che non appartengono a un solo scaglione

| Gate | Comando | Quando |
|---|---|---|
| Il cruscotto quotidiano (V2 §23) | `python -m empire controllo` · `forge scan --json` · `trace stato --json` · `wc -c entrate.jsonl` · `ultimo_metro.py --json` · `empire vivo --json` | ogni giornata di lavoro sul piano, in coda a STATO-EMPIRE |
| Regola dei due giorni fermi | il numero dello scaglione aperto non si muove per 2 giornate → ci si ferma e si dichiara | continuo |
| Fusibile R5 (V3 §12) | dopo E3: pezzi fuori ≥ soglia **E** un canale di vendita apparecchiato | fine E3 |
| Gate F3 a data (V2 §25.3) | entro 4 settimane da E4: almeno una traccia `origine=hook` nata da lavoro reale | E4 + 4 settimane |
| Formula del 100% (V2 §3, V3 §3/§7) | `python -m empire vivo --json` → numeratore/denominatore su anagrafe dinamica, tre esiti | fine piano |

---

## 5. VIA ALLA COSTRUZIONE — la lista che Max spunta

V4 è chiusa quando **tutte** queste righe sono vere, e la costruzione parte solo dopo l'ordine di Max:

- [ ] I 20 documenti di scaglione esistono e rispettano il template §3 (verifica: `python
      PIANO-MAESTRO/scripts/verifica_v4.py` — da scrivere come ultimo passo di V4, stampa la
      sezione mancante per documento).
- [ ] Ogni gate di ogni documento è nella forma L9 (comando+condizione+exit code) o è la specifica
      di un comando che un passo di §2 costruisce.
- [ ] INV-GAEL verificata: `grep -l "Gael" V4-ESECUTIVO/*.md` restituisce **solo** `15-E5b-INGRESSI.md`
      e i documenti che lo citano come «non dipende da».
- [ ] Le decisioni di Max con default (V2 §26 + V3 §11, undici righe) sono riportate nel documento
      dello scaglione che le consuma, con il default scritto.
- [ ] Le tre credenziali esposte (B-020/021/023) hanno il loro passo in `03-E0b-ROTAZIONE.md` con i
      tre `.env` elencati per percorso.
- [ ] `REGISTRO-NUMERI.md` sanato (16 ecosistemi, numero 08 unico) è un passo di `02-E0.5-AGGANCI.md`.
- [ ] Il checkpoint di chiusura di V4 è coniato e `00-LEGGIMI.md` §7 segna V4 ✅.

---

## 6. AVANZAMENTO DI V4

| Documento | Stato | Chi lo ha scritto |
|---|---|---|
| `00-INDICE.md` | ✅ | EMPERATOR |
| `01`–`05` (E0a, E0.5, E0b, E0.9, E0.6) | 🔄 | sentinella opus A |
| `06`–`08` (E0.7, E1, E2) | 🔄 | sentinella opus B |
| `09`–`12` (F3, E3.0, E3, E4) | 🔄 | sentinella opus C |
| `13`–`20` (E5a, E5-bis, E5b, E5c, E6, E7, E8, E9) | 🔄 | sentinella opus D |
| `verifica_v4.py` | ⬜ | EMPERATOR (ultimo passo) |
| Chiusura + checkpoint | ⬜ | EMPERATOR |
