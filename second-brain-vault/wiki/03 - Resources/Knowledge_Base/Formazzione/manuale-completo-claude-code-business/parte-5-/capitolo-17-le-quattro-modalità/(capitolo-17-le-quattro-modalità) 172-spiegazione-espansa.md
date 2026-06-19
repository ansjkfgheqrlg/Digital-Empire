# 17.2 — Spiegazione Espansa
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-5- > capitolo-17-le-quattro-modalità]]

## Content

--- PAGE 56 ---
Esistono quattro modalità di permesso, disposte in ordine crescente di autonomia: 
text 
SPETTRO DI AUTONOMIA: 
 
Controllo massimo ◄────────────────────────────► Autonomia massima 
dell'utente                                       di Claude Code 
 
[Ask Before Edits] → [Accept Edits] → [Plan Mode] → [Bypass Permission] 
    Modalità 1          Modalità 2      Modalità 3      Modalità 4 
Modalità 1: Ask Before Edits (Default) 
text 
COMPORTAMENTO: 
 
Utente: "Cambia il titolo del sito e scrivici Giovanni" 
     ↓ 
Claude Code: [analizza il file, trova il titolo] 
     ↓ 
Claude Code: [MOSTRA le modifiche proposte senza applicarle] 
     ↓ 
Schermata: "Vorrei fare queste modifiche. Vuoi procedere?" 
     ↓ 
Opzioni: 
├── [Sì] → Applica questa modifica specifica 
├── [Sì a tutto] → Applica tutte le modifiche in questa sessione 
├── [No] → Non applicare 
└── [Altro] → Opzione alternativa / modifica della richiesta 
Caratteristiche chiave: 
●​
È il comportamento di default quando si installa Claude Code 
●​
Claude Code propone le modifiche ma non le applica fino a conferma esplicita 
●​
L'utente vede esattamente cosa verrà modificato prima che succeda 
●​
Ogni modifica richiede un'approvazione separata (a meno che non si scelga "Sì a tutto") 
Quando usarla: 
●​
Quando state imparando Claude Code e volete capire cosa fa 
●​
Quando lavorate su file critici che non volete siano modificati per errore 
●​
Quando volete controllo granulare su ogni singola modifica 
●​
In ambienti di produzione dove ogni cambiamento deve essere approvato 
Limitazione:​
È la modalità più lenta perché richiede intervento umano per ogni modifica. Su progetti con decine o centinaia di 
modifiche, diventa impraticabile. 
Modalità 2: Accept Edits (Accettazione Automatica delle Modifiche) 
text 
COMPORTAMENTO: 
 
Utente: "Cambia il titolo del sito e scrivici Giovanni" 
     ↓ 
Claude Code: [analizza il file, trova il titolo] 
     ↓ 
Claude Code: [APPLICA le modifiche AUTOMATICAMENTE] 
     ↓ 
[Modifica completata senza chiedere conferma] 

--- PAGE 57 ---
     ↓ 
⚠️ ECCEZIONE: Chiede sempre conferma per: 
   • Creare nuovi file 
   • Cancellare file esistenti 
Caratteristiche chiave: 
●​
Le modifiche ai file esistenti vengono applicate automaticamente 
●​
La creazione e cancellazione di file richiede sempre conferma 
●​
È un buon compromesso tra velocità e sicurezza 
●​
Elimina la necessità di approvare ogni singolo edit 
Quando usarla: 
●​
Quando avete un'idea chiara di cosa volete e non serve revisionare ogni modifica 
●​
Per task di refactoring dove molti file devono essere modificati 
●​
Quando volete velocità ma mantenete la protezione contro creazione/cancellazione accidentale 
Limitazione importante notata dall'autore:​
Accept Edits non può creare o cancellare file autonomamente. Per queste operazioni, chiederà sempre il consenso. 
Questo è un limite di sicurezza intenzionale che protegge da cancellazioni accidentali. 
Modalità 3: Plan Mode (Pianificazione) 
Il Plan Mode è sufficientemente importante da meritare un capitolo dedicato (Capitolo 18). Qui ne forniamo la 
definizione sintetica nel contesto delle quattro modalità. 
text 
COMPORTAMENTO: 
 
Utente: "Costruiscimi un'app simile a Trello con autenticazione e pagamenti" 
     ↓ 
Claude Code: [ANALIZZA la richiesta] 
     ↓ 
Claude Code: [CREA UN PIANO strutturato con subtask] 
     ↓ 
Claude Code: [PRESENTA il piano all'utente] 
     ↓ 
Utente: [Revisiona il piano, approva/modifica] 
     ↓ 
Claude Code: [Esegue il piano approvato] 
Caratteristiche chiave: 
●​
Claude Code non esegue nulla immediatamente 
●​
Prima crea un piano strutturato e lo presenta per approvazione 
●​
L'utente può modificare, aggiungere o rimuovere elementi dal piano 
●​
Solo dopo l'approvazione, Claude Code procede all'esecuzione 
●​
Durante l'esecuzione, segue la checklist del piano approvato 
Modalità 4: Bypass Permission (Dangerously Skip Permissions) 
Anche questa modalità merita un capitolo dedicato (Capitolo 19). Definizione sintetica: 
text 
COMPORTAMENTO: 
 
Utente: "Costruiscimi un'app simile a Trello con autenticazione e pagamenti" 

--- PAGE 58 ---
     ↓ 
Claude Code: [ESEGUE TUTTO in completa autonomia] 
     ↓ 
[Crea file, modifica file, cancella file, esegue comandi] 
     ↓ 
[NESSUNA richiesta di conferma per nulla] 
     ↓ 
[Risultato finale presentato quando tutto è completato] 
Caratteristiche chiave: 
●​
Autonomia totale: Claude Code può fare qualsiasi cosa senza chiedere 
●​
Include la capacità di creare e cancellare file 
●​
È la modalità più veloce ma anche la più rischiosa 
●​
L'autore la usa frequentemente ma avverte dei rischi

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
