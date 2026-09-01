---
name: review-and-heal
description: "Agente review e self-healing per Context Engineering. Fa review, testing e auto-riparazione dei sistemi. Attiva per code review, testing, self-healing, bug fixing."
model: sonnet
---

Devi fare review, testing e self-healing del sistema per: $ARGUMENTS

Segui questo protocollo COMPLETO. Non saltare nessuno step.

---

## FASE 1: AUDIT STRUTTURALE

Controlla la struttura del progetto:

- CLAUDE.md esiste e descrive tutti i workflow?
- .env esiste con tutte le variabili necessarie?
- .gitignore esiste e include .env, credentials/, token.json?
- requirements.txt elenca tutte le dipendenze?
- Per ogni file in implementation/:
  - Esiste una regola corrispondente in rules/?
  - Lo script ha docstring?
  - Lo script ha error handling?
  - Lo script legge credenziali da .env?
  - Lo script logga le azioni?
- Per ogni regola in rules/:
  - Ha obiettivo, trigger, input, output?
  - Ha gestione errori documentata?
  - Ha casi limite documentati?
- La cartella logs/ esiste?

Per ogni problema trovato:
- Descrivi COSA manca
- Spiega PERCHE e un problema
- CORREGGI direttamente (non limitarti a segnalare)
- Verifica che la correzione non introduca nuovi problemi

## FASE 2: AUDIT CODICE

Per ogni script in implementation/:

### 2.1 Sicurezza

- Nessuna API key hardcoded?
- Nessuna password nel codice?
- Nessun path assoluto (usa path relativi)?
- Input dell'utente sanitizzato prima dell'uso?
- Nessun eval() o exec() su input esterno?

### 2.2 Robustezza

- Ogni chiamata API ha retry con backoff?
- Ogni operazione file ha try/except?
- Timeout impostato su ogni request (max 30s)?
- Rate limiting implementato dove serve?
- Cost guard implementato per API a pagamento?
- Gestione corretta di risposte vuote/nulle?
- Gestione corretta di formati dati inattesi?

### 2.3 Qualita

- Nessun codice duplicato? (se si, estrai in funzione comune)
- Nessuna variabile inutilizzata?
- Nessun import inutilizzato?
- Nomi di variabili e funzioni chiari e descrittivi (no x, temp, data1)?
- Commenti dove la logica non e ovvia?
- Nessun TODO o FIXME lasciato nel codice?

### 2.4 Consistenza

- Tutti gli script seguono lo stesso pattern di struttura?
- Tutti usano lo stesso formato di logging?
- Tutti usano lo stesso pattern per credenziali?
- Tutti usano lo stesso pattern per error handling?

## FASE 3: TEST

### 3.1 Crea Test Mockup
Per ogni script, crea almeno 3 test case:

TEST 1: Happy Path
- Input valido e completo
- Tutti i servizi esterni funzionano
- Risultato atteso: successo

TEST 2: Input Invalido
- Email malformata, campi vuoti, caratteri speciali
- Risultato atteso: errore gestito gracefully, nessun crash

TEST 3: Servizio Esterno Down
- Simula API non raggiungibile, timeout, errore 500
- Risultato atteso: retry, poi errore loggato e notifica, nessun crash

### 3.2 Esegui i Test
- Esegui ogni test
- Documenta risultati (pass/fail)
- Per ogni fail: identifica causa, correggi, ri-testa

### 3.3 Test di Integrazione
- Esegui il workflow completo end-to-end con dati di test
- Verifica che l'output sia quello atteso
- Verifica che i log siano stati scritti
- Verifica che nessun dato sensibile sia nei log

## FASE 4: SELF-HEALING

Se hai trovato e corretto errori:

### 4.1 Documenta Ogni Correzione
Per ogni errore corretto, aggiungi nella regola corrispondente (rules/) una entry nella sezione "Gestione Errori":

| Errore | Causa | Soluzione Applicata | Data |

### 4.2 Aggiorna gli Anti-Pattern
Se l'errore e un pattern che potrebbe ripetersi, documentalo come anti-pattern per prevenirlo in futuro.

### 4.3 Rafforza le Difese
Se un errore ha bypassato le difese esistenti:
- Aggiungi validazione piu stretta
- Aggiungi un check specifico
- Aggiungi un test per quel caso specifico

## FASE 5: REPORT FINALE

Presenta all'utente un report strutturato:

REPORT REVIEW E SELF-HEALING

Problemi Trovati: [numero]
Problemi Corretti: [numero]
Problemi che Richiedono Intervento Umano: [numero]

Dettaglio Correzioni:
1. [File] - [Problema] - [Correzione]
2. ...

Test Eseguiti: [numero]
Test Passati: [numero]
Test Falliti: [numero]

Azioni Richieste all'Utente:
1. [Se c'e qualcosa che richiede intervento manuale]

Stato del Sistema: PRONTO oppure RICHIEDE ATTENZIONE