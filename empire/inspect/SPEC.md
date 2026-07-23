---
Owner: Max
Controllore: Claude
Origine: FORGE
Governo: MANDATO-EMPIRE.md (ADR-008)
Status: ATTIVO
---

# SPEC — Formule Scorecard 5D e Assunzioni

Questo documento definisce formalmente le metriche e le regole di calcolo deterministico per la valutazione delle performance (T2 ANALYZE) all'interno dell'Ispettorato Generale.

---

## 1. Asse ① correctness/debug

### Formula
$$Score = 5 - \min(4, errori + (retry \times 0.5) + (escalation \times 2))$$

### Assunzioni
- `errori`, `retry` ed `escalation` sono numeri interi non negativi.
- Il punteggio risultante è un numero decimale/intero compreso nell'intervallo $[1.0, 5.0]$.
- Le escalation pesano significativamente sulla correttezza poiché indicano l'incapacità dell'agente o del verificatore primario di risolvere il blocco senza intervento di terzi.

### Esempio svolto a mano
- **Input:** `errori = 1`, `retry = 2`, `escalation = 0`
- **Calcolo:**
  1. Calcolo del termine di penalità: $Penalità = 1 + (2 \times 0.5) + (0 \times 2) = 1 + 1.0 + 0 = 2.0$
  2. Applicazione del tetto massimo di penalità: $\min(4, 2.0) = 2.0$
  3. Calcolo finale: $5 - 2.0 = 3.0$
- **Punteggio Asse 1:** **3.0**

---

## 2. Asse ② qualità soluzione

### Regola
Il punteggio viene assegnato in base alle modalità con cui la soluzione è confluita nel monorepo:
1. `regressione == True` $\rightarrow$ **1**
2. `post_consegna == True` (presenza di fix successivi alla consegna) $\rightarrow$ **2**
3. `revisions >= 2` $\rightarrow$ **3**
4. `revisions == 1` o `first_pass == False` $\rightarrow$ **4**
5. `first_pass == True` (e nessun'altra penalità) $\rightarrow$ **5**

### Assunzioni
- I flag di regressione e post-consegna annullano i voti più alti poiché indicano codici rotti finiti in produzione.
- Se nessuna informazione è disponibile, il comportamento di default è considerare il lavoro come `first_pass == True` (punteggio 5).

### Esempio svolto a mano
- **Input:** `revisions = 1`, `first_pass = False`, `regression = False`, `post_consegna = False`
- **Risoluzione:** L'agente ha dovuto eseguire una revisione prima dell'accettazione. Il flag `regression` è False.
- **Punteggio Asse 2:** **4**

---

## 3. Asse ③ struttura output

### Regola
Valutazione della conformità degli artefatti prodotti (elencati in `output_ref`):
1. Per ciascun file in `output_ref`, calcoliamo un punteggio di conformità individuale:
   - Il file non esiste sul disco $\rightarrow$ **1**
   - Il file esiste ma non è conforme (manca intestazione ADR-008 o il path non è all'interno del monorepo) $\rightarrow$ **3**
   - Il file esiste, è all'interno del monorepo ed ha intestazione ADR-008 completa $\rightarrow$ **5**
2. Il punteggio finale dell'asse è la media aritmetica dei punteggi dei singoli file. Se `output_ref` è vuoto, il punteggio di default è **5** (nessun file errato prodotto).

### Assunzioni
- La conformità dell'intestazione ADR-008 è verificata tramite l'importazione di `empire.loader` (campi `owner`, `controller`, `origin`, `governance` tutti valorizzati).

### Esempio svolto a mano
- **Input:** 2 file in `output_ref`
  - File A: Esiste sul disco, è dentro il monorepo, ha intestazione completa (`owner`, `controller`, `origin`, `governance` valorizzati) $\rightarrow$ **5**
  - File B: Esiste sul disco ma manca il campo `governance` nell'intestazione $\rightarrow$ **3**
- **Calcolo:**
  $$Score = \frac{5 + 3}{2} = 4.0$$
- **Punteggio Asse 3:** **4.0**

---

## 4. Asse ④ scope-fit

### Formula
$$Score = 1 + 4 \times \left(\frac{dods\_verified}{dods\_total}\right)$$

Se `dods_total == 0` o non è specificato, il punteggio di default è **5**.

### Assunzioni
- `dods_total` rappresenta le Definition of Done dichiarate nel brief.
- `dods_verified` represents le DoD effettivamente spuntate e verificate con test/comandi.

### Esempio svolto a mano
- **Input:** `dods_total = 10`, `dods_verified = 8`
- **Calcolo:**
  1. Rapporto DoD superate: $\frac{8}{10} = 0.8$
  2. Calcolo finale: $1 + 4 \times 0.8 = 1 + 3.2 = 4.2$
- **Punteggio Asse 4:** **4.2**

---

## 5. Asse ⑤ efficiency

### Regola
Confronto tra la durata reale della run (`ttd_h` in ore) e il benchmark definito in `benchmarks.py` per quella specifica famiglia-task/ruolo:
- $ttd\_h \le 0.8 \times benchmark \rightarrow$ **5**
- $ttd\_h \le 1.2 \times benchmark \rightarrow$ **4**
- $ttd\_h \le 2.0 \times benchmark \rightarrow$ **3**
- $ttd\_h \le 3.0 \times benchmark \rightarrow$ **2**
- Altrimenti $\rightarrow$ **1**

### Assunzioni
- La durata è calcolata tramite la differenza tra fine run e inizio run.
- Se non è specificato alcun benchmark per la famiglia del task, il default è **4.0 ore**.

### Esempio svolto a mano
- **Input:** `ttd_h = 2.5 ore`, benchmark = `2.0 ore`
- **Calcolo:**
  1. Calcolo del rapporto: $\frac{2.5}{2.0} = 1.25$
  2. Valutazione delle soglie:
     - $1.25 > 0.8$ (no 5)
     - $1.25 > 1.2$ (no 4)
     - $1.25 \le 2.0$ $\rightarrow$ **3**
- **Punteggio Asse 5:** **3**

---

## 6. Gate Traceability

### Regola
Un checkpoint atomico (kind `"checkpoint"`) deve esistere in memoria centrale e referenziare lo stesso `task` associato alla performance.
- Esiste $\rightarrow$ **True** (🟢)
- Non esiste $\rightarrow$ **False** (🔴)

Se il gate è **False**, viene sollevata una segnalazione di violazione ADR-002 e il task non è considerabile come formalmente completato o valutato positivamente, a prescindere dai punteggi della scorecard.
