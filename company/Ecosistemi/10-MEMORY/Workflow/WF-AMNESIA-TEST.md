# WF-AMNESIA-TEST
## Test di ripresa a freddo — verifica che MEMORY sia sufficiente

## Scopo
Verificare che una sessione nuova (agente o operatore che non ha visto NIENTE del lavoro
precedente) riesca a ricostruire lo stato completo della holding SOLO leggendo
`company/Memory/`. Nessun contesto extra, nessuna memoria di sessione, nessun briefing
verbale. Solo i file in Memory.

Questo test è il gate finale per ogni fase roadmap: una fase non è "completata" finché
il test amnesia non è superato.

---

## Trigger
- Fine di ogni fase roadmap (obbligatorio prima di avanzare alla fase successiva)
- Richiesta esplicita: "esegui amnesia test"
- Su richiesta di ME-A10 (Integrity Auditor) durante audit settimanale

---

## Input
- Nessun input esterno — questo è il punto: l'agente tester parte da zero
- L'unica fonte consentita: `company/Memory/` (tutti i file)
- VIETATO durante il test: wiki, PIANO-MAESTRO, Ecosistemi/, secondo cervello, conversazioni precedenti

---

## Passi

```
FASE 0: SETUP TEST
  ├── Definire il "tester": può essere un agente fresh, un operatore che fa finta,
  │   o ME-Conductor stesso con reset contesto
  ├── Registrare timestamp inizio test
  └── Annotare la fase roadmap sotto test (es. "F1 — post ME-5")

FASE 1: CARICAMENTO MEMORY (il tester esegue questi passi)
  ├── Legge company/Memory/INDEX.md → si orienta
  ├── Legge company/Memory/STATO-EMPIRE.md → capisce dove siamo
  ├── Legge l'ultima sessione in sessions/ → recupera "RIPRESA DA:"
  └── Legge il piano corrente in plans/ → capisce cosa si sta costruendo

FASE 2: DOMANDE TEST (devono avere risposta da Memory)
  Il tester deve rispondere SOLO con ciò che legge in Memory:

  D1: "In che fase siamo?"
  Risposta attesa: F[N], desunta da STATO-EMPIRE.md o state.json

  D2: "Quali ecosistemi sono completati?"
  Risposta attesa: lista desunta da state.json

  D3: "Qual era il task dell'ultima sessione? Come è andata?"
  Risposta attesa: ultima sessione + ultimo CP (desunto da sessions/ e checkpoints/)

  D4: "Quali decisioni architetturali sono attive?"
  Risposta attesa: lista ADR con stato=attivo da decisions/

  D5: "Cosa devo fare adesso per continuare il lavoro?"
  Risposta attesa: "prossima_azione" da state.json o "RIPRESA DA:" da sessione

  D6: "C'è qualche blocco aperto?"
  Risposta attesa: desunta da STATO-EMPIRE.md sezione "Blocchi"

  D7: "Quale task si era sospeso e perché?"
  Risposta attesa: da sessions/ campo "task_sospesi" o CP con esito=parziale

FASE 3: SCORING
  ├── 7/7 risposte corrette da Memory → SUPERATO (Gate verde)
  ├── 5-6/7 → WARNING (gate giallo): identificare quale campo Memory mancava
  └── < 5/7 → FALLITO (gate rosso): Memory incompleta, non si avanza di fase

FASE 4: REMEDIATION (se fallito o warning)
  ├── Identificare quali file Memory erano assenti o incompleti
  ├── Completare/aggiornare quei file
  └── Rieseguire il test (max 3 tentativi per fase)

FASE 5: REPORT
  └── Scrivere CP del test: "WF-AMNESIA-TEST eseguito — esito: SUPERATO/FALLITO"
  └── Aggiornare STATO-EMPIRE.md con risultato test
  └── Se SUPERATO: conferma avanzamento fase
```

---

## Gate

- **Obbligatorio** prima di avanzare a ogni nuova fase roadmap
- **3 tentativi** per fase: se fallisce 3 volte → blocco avanzamento + escalation Board
- **Indipendenza tester:** il tester NON può essere l'agente che ha scritto i file testati

---

## Output

```json
{
  "test_id": "AMNESIA-YYYYMMDD-F[N]",
  "fase_testata": "F1 | F2 | ...",
  "esito": "SUPERATO | WARNING | FALLITO",
  "punteggio": "7/7 | 6/7 | ...",
  "domande_fallite": ["D3", "D7"],
  "file_memory_incompleti": ["STATO-EMPIRE.md sezione X mancante"],
  "azioni_remediation": ["aggiornare STATO-EMPIRE.md"],
  "timestamp": "ISO8601"
}
```

---

## Valore del test

Il test amnesia misura l'efficacia reale di MEMORY, non la sua completezza formale.
Un INDEX.md con 100 voci che non risponde alla domanda "cosa faccio adesso?" è un
Memory che non funziona. Il test forza a scrivere Memory per il prossimo che non sa nulla —
il livello di chiarezza più alto.

---

## Note operative

- Frequenza raccomandata: ogni fine fase + spot check mensile
- Il tester ideale: Gael che testa il lavoro di Max (o viceversa) — contesto zero garantito
- Se gli agenti fanno il test: ME-Conductor con reset context o agente fresh

---

## Connessioni
- [[09-ECOSISTEMA-MEMORY]] — §11 fase ME-5: "Test amnesia: sessione pulita ricostruisce lo stato solo da MEMORY"
- [[STATO-EMPIRE]] — documento principale verificato nel test
- [[INDEX]] — mappa che il tester carica per prima
- [[ME-A10-memory-sentinel]] — può richiedere il test come parte dell'audit
- [[M1-RECALL-PRETASK]] — il pre-task gate usa la stessa logica di caricamento del test
- [[WF-PRE-TASK-GATE]] — se WF-PRE-TASK-GATE funziona bene, il test amnesia tende a essere superato
