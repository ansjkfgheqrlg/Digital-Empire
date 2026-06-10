# 16.4 — Il Prompt Iniziale e la Plan Mode

L'autore costruisce un prompt strutturato che copre tutti gli aspetti dell'applicazione. Analizzandolo nel dettaglio: 
text 
STRUTTURA DEL PROMPT: 
 
1. CONTESTO VISIVO: 
   "Interfaccia simile a Trello come nell'image.png" 
   → Immagine di riferimento scaricata da Google 
 
2. FUNZIONALITÀ RICHIESTE: 
   • Card draggabili con cambio di status 
   • Ricerca online su cos'è Trello (per le funzionalità) 
 
3. AUTENTICAZIONE: 
   • Form di login con email e nome 
   • Dati salvati su Supabase 
 
4. BACKEND: 
   • Supabase come database 
   • Tracking utenti attivi/inattivi 
   • Storico pagamenti 
 

--- PAGE 47 ---
5. PAGAMENTI: 
   • Integrazione Stripe (da predisporre ma non implementare subito) 
   • Database predisposto per tracking pagamenti 
 
6. SICUREZZA: 
   • File .env per le chiavi API 
   • Chiavi salvate in locale 
   • Non condividere le chiavi quando si condivide il progetto 
 
7. API KEYS: 
   • Chiave Stripe (fornita direttamente nel prompt) 
   • Chiave Supabase (fornita direttamente nel prompt) 
Osservazione dell'autore sulla qualità del prompt:​
"A livello teorico, uno dovrebbe mettersi lì e fare un prompt un po' migliore. Ma già con questo riusciremo ad ottenere un 
prodotto che è sufficiente per essere venduto ad un'azienda." 
Questa osservazione è importante: il prompt non è perfetto, ma è sufficiente per ottenere un risultato funzionante. La 
perfezione del prompt non è necessaria quando si ha una buona architettura di progetto (CLAUDE.md, rules, ciclo di 
verifica).

