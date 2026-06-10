# 36.2 — Uso Strategico della Memoria
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow > capitolo-36]]

## Content

Definizione del Concetto 
La memoria non è solo per ricordare fatti curiosi. È uno strumento strategico fondamentale per la 
gestione del contesto e la continuità dei progetti complessi. 
Il Pattern "Salva e Continua" 

--- PAGE 182 ---
La guida mostra un pattern fondamentale che l'autore usa quotidianamente. Quando il contesto 
raggiunge il 60-70% e c'è ancora lavoro da fare, il processo è: 
 
PATTERN "SALVA E CONTINUA" 
══════════════════════════ 
 
SESSIONE CORRENTE (contesto al 66%): 
───────────────────────────────────── 
Utente: "Sei al 66% del contesto. Quello che mi  
         sarebbe utile che tu facessi è salvare le  
         cose in memoria di modo tale che io nel nuovo  
         contesto possa continuare a sviluppare l'app,  
         perché quello che manca è l'integrazione con  
         Stripe. Possiamo procedere?" 
 
Claude: "Assolutamente, sì. Salvo tutto in memoria." 
 
         [Claude scrive nel memory.md:] 
         • Stato del progetto: app Trello clone completa 
         • Backend: Supabase configurato e funzionante 
         • Auth: login con email funzionante 
         • Mancante: integrazione Stripe 
         • API keys: già nel file .env 
         • Database: schema già predisposto per Stripe 
         • Prossimo passo: integrazione pagamenti 
 
Claude: "Tutto salvato. Nella prossima conversazione  
         puoi dirmi: 'Continua con integrazione Stripe'" 
 
NUOVA SESSIONE (contesto fresco): 
────────────────────────────────── 
Utente: "Continua con integrazione Stripe" 
 
Claude: [Legge memory.md → sa tutto quello che serve] 
         "Ho recuperato il contesto dalla memoria.  
          Procedo con l'integrazione Stripe..." 
Questo pattern è cruciale perché: 
1.​ Preserva le informazioni critiche: tutto ciò che serve per continuare viene salvato 
esplicitamente 
2.​ Libera il contesto: la nuova sessione parte con il contesto fresco 
3.​ Fornisce un prompt di continuazione: Claude stesso vi dice cosa scrivere per riprendere 
4.​ Mantiene la continuità: nonostante il cambio di sessione, il lavoro procede senza 
interruzioni 
Cosa Salvare in Memoria 
Non tutto merita di essere salvato in memoria. Ecco una guida pratica: 
 

--- PAGE 183 ---
COSA SALVARE IN MEMORIA 
════════════════════════ 
 
✅ SALVARE: 
├── Stato corrente del progetto 
├── Decisioni architetturali prese 
├── API key e credenziali (se in .env) 
├── Problemi noti e come sono stati risolti 
├── Preferenze di lavoro dell'utente 
├── Prossimi passi pianificati 
├── Errori ricorrenti e relative soluzioni 
└── Informazioni critiche per la continuità 
 
❌ NON SALVARE: 
├── Dettagli di implementazione (sono nel codice) 
├── Conversazioni verbose (occupano spazio) 
├── Informazioni temporanee 
├── Cose che sono già nel CLAUDE.md 
├── Ragionamenti intermedi di Claude 
└── Dati che cambieranno alla prossima sessione 
L'Impatto della Memoria sul Contesto 
Come visto nella Parte 6, i file di memoria occupano una porzione del contesto: 
"Memory Files occupano circa il 4-5% del contesto." 
Questo significa che troppa memoria può diventare controproducente. Se salvate troppe 
informazioni nel memory.md, il file cresce e inizia a consumare contesto significativo all'inizio di 
ogni sessione. La soluzione è: 
●​
Periodicamente rivedere il memory.md e rimuovere informazioni obsolete 
●​
Essere selettivi su cosa salvare 
●​
Preferire informazioni sintetiche a descrizioni verbose 
Errori Comuni con la Memoria 
1.​ Non usare mai la memoria: continuare sessioni enormi fino a saturare il contesto, 
perdendo qualità. Usate il pattern "Salva e Continua". 
2.​ Salvare troppo: trasformare il memory.md in un romanzo. Deve essere conciso e 
azionabile. 
3.​ Non pulire mai la memoria: informazioni di progetti vecchi che restano nel memory.md e 
consumano contesto in progetti nuovi. 
4.​ Aspettarsi che la memoria sia perfetta: la memoria non cattura sfumature e contesto 
complesso. Per informazioni critiche, codificatele nel CLAUDE.md, non nel memory.md. 
5.​ Confondere memoria con CLAUDE.md: il CLAUDE.md contiene regole e istruzioni 
permanenti del progetto. La memoria contiene informazioni di stato e preferenze che 
possono cambiare. 
 

--- PAGE 184 ---

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
