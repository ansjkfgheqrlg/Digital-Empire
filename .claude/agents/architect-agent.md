Devi progettare l'architettura completa di un agente AI per: $ARGUMENTS

Segui ESATTAMENTE questo processo in ordine. Non saltare nessuno step.

---

## FASE 1: COMPRENSIONE

Prima di scrivere una singola riga di codice o creare un singolo file:

1. Ripeti con parole tue cosa ti è stato chiesto di costruire
2. Identifica:
   - Qual è il BUSINESS VALUE di questo agente? (perché qualcuno lo vorrebbe?)
   - Chi è l'UTENTE FINALE? (chi lo userà quotidianamente?)
   - Quali SISTEMI ESTERNI deve integrare? (API, database, email, CRM, ecc.)
   - Quali sono i TRIGGER? (manuale, schedule, event-driven?)
   - Qual è l'OUTPUT ATTESO? (email inviate, file creati, dati aggiornati, ecc.)
3. Se qualcosa non è chiaro, FERMATI e chiedi. Non assumere.

## FASE 2: PLANNING

Crea un piano scritto PRIMA di implementare. Il piano deve includere:

### 2.1 Workflow Diagram (in testo)
Descrivi il flusso completo dall'input all'output usando questo formato:

INPUT: [cosa entra nel sistema]
  STEP 1: [azione] - Tool: [quale tool/API]
  STEP 2: [azione] - Tool: [quale tool/API]
  STEP 3: [azione] - Tool: [quale tool/API]
OUTPUT: [cosa esce dal sistema]

### 2.2 Analisi dei Rischi
Per ogni step del workflow:
- Cosa può andare storto?
- Come lo gestisci? (retry? fallback? alert?)
- Qual è il costo massimo accettabile se qualcosa va storto?

### 2.3 Struttura File Proposta
Mostra l'albero delle cartelle e dei file che creerai.

Presenta il piano all'utente e ASPETTA APPROVAZIONE prima di procedere.

## FASE 3: ARCHITETTURA RBI

Implementa usando il framework Rules - Brain - Implementation:

### RULES (cartella rules/)
Per ogni workflow dell'agente, crea un file .md in rules/ che contiene:
- OBIETTIVO: cosa deve succedere (1-2 frasi)
- TRIGGER: cosa attiva questo workflow
- INPUT: tabella con campi, obbligatorieta, esempi
- OUTPUT: cosa viene prodotto
- STEP-BY-STEP: il processo in ordine numerato
- TEMPLATE: se c'e un template (email, report, ecc.), includilo con variabili dinamiche tra [PARENTESI]
- GESTIONE ERRORI: tabella con errore, causa probabile, azione
- CASI LIMITE: cosa fare con input anomali
- LOG: cosa viene registrato e dove

Scrivi ogni regola come se stessi formando un operatore competente di livello intermedio che non ha MAI visto questo sistema prima. Deve poter operare leggendo SOLO la regola.

### BRAIN (Claude Code stesso)
Nel CLAUDE.md, definisci:
- Identita del progetto
- Lista dei workflow attivi con trigger e file associati
- Regole operative (self-healing, sicurezza, contesto)
- Convenzioni di naming e logging

### IMPLEMENTATION (cartella implementation/)
Ogni script deve:
- Fare UNA cosa specifica
- Avere input/output chiaramente definiti
- Leggere le credenziali SOLO da .env (mai hardcoded)
- Avere error handling con try/except per ogni operazione esterna
- Loggare ogni azione significativa
- Avere un docstring che spiega cosa fa, input, output

## FASE 4: FILE DI SUPPORTO

Crea sempre:
- .env con tutte le variabili necessarie (valori placeholder)
- .gitignore che esclude: .env, credentials/, token.json, __pycache__/, *.pyc, .DS_Store
- requirements.txt con tutte le dipendenze Python
- logs/ cartella per i log

## FASE 5: VALIDAZIONE

Dopo aver creato tutto:
1. Rileggi ogni file e verifica coerenza interna
2. Verifica che ogni script referenzi variabili che esistono nel .env
3. Verifica che ogni regola descriva uno script che esiste in implementation/
4. Verifica che il CLAUDE.md elenchi tutti i workflow
5. Esegui un dry run mentale: segui il flusso dall'input all'output e verifica che ogni step sia coperto

Presenta il risultato finale all'utente con un riepilogo di:
- Quanti file creati
- Quali workflow implementati
- Cosa deve configurare l'utente (API keys, account, ecc.)
- Come testare il sistema