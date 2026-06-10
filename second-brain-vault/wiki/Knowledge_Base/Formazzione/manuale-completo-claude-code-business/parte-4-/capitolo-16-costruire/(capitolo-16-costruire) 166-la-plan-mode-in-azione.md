# 16.6 — La Plan Mode in Azione
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-16-costruire]]

## Content

Dopo aver inviato il prompt, Claude Code in Plan Mode produce un piano strutturato: 
text 
PIANO GENERATO DA CLAUDE CODE: 
 
Fase 1: Tech Stack Setup 
├── Inizializzare il progetto (Next.js o simile) 
└── Installare le dipendenze 
 
Fase 2: Database 
├── Creare lo schema SQL per Supabase 
└── Tabelle: utenti, board, card, pagamenti 

--- PAGE 49 ---
 
Fase 3: Autenticazione 
├── Form di login con email + nome 
└── Login diretto senza verifica email 
 
Fase 4: Pagine e Routing 
├── Pagina di login 
├── Pagina principale (board) 
└── Pagina di pagamento 
 
Fase 5: Componenti UI 
├── Board Trello-like 
├── Colonne draggabili 
├── Card con labels 
└── Commenti 
 
Fase 6: Server & Autenticazione 
├── Middleware di autenticazione 
└── Protezione delle rotte 
 
Fase 7: Stripe 
├── Integrazione pagamenti 
├── Webhook 
└── Gestione abbonamenti 
 
Ordine di implementazione: Sequenziale (1→7) 
Verifica: Test alla fine di ogni fase 
Interazione Intelligente del Piano 
Durante il planning, Claude Code pone domande strategiche all'utente: 
Domanda 1: "Quale metodo di autenticazione preferisci? Magic Link (l'utente riceve un'email e si autentica da lì) o Login 
diretto?"​
→ L'autore sceglie: Login diretto 
Domanda 2: "La chiave Stripe che hai condiviso è una chiave live di produzione. Vuoi usare chiavi test per lo sviluppo?"​
→ L'autore sceglie: Usare le chiavi fornite, consapevole del rischio 

--- PAGE 50 ---
Queste domande dimostrano che Claude Code in Plan Mode non è un esecutore cieco: è un collaboratore che 
identifica potenziali problemi e chiede chiarimenti prima di procedere.

## Collegamenti Correlati
- [[Map - Bho|Bho Area]]
- [[Map - Formazzione|Formazzione Area]]
