# 35.3 — Hooks Avanzati — Oltre il Suono
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-10- > capitolo-35]]

## Content

Definizione del Concetto 
Gli hook non sono limitati a suoni di notifica. Possono attivare qualsiasi azione programmabile, 
inclusi workflow completi, invio di comunicazioni e attivazione di sistemi esterni. 
Spiegazione Approfondita 

--- PAGE 175 ---
L'autore della guida espande il concetto degli hook con un esempio aziendale concreto: 
"Ipotizziamo di stare lavorando all'interno di un'azienda. Ipotizziamo che abbiamo creato un 
CRM, ossia un sistema che ci aiuta a gestire i clienti. E ipotizziamo che nel momento in cui il 
sales team fa l'onboarding di qualcuno, vorremmo che questo cliente ricevesse in automatico 
un'onboarding email." 
Questo esempio illustra un hook molto più sofisticato del semplice suono: 
text 
HOOK AZIENDALE — ONBOARDING AUTOMATICO 
═══════════════════════════════════════ 
 
EVENTO: Un nuovo lead viene inserito nel CRM 
        (Claude completa l'inserimento del lead) 
         
HOOK SCATTA: 
    │ 
    ▼ 
┌──────────────────────────────────────────────┐ 
│ SCRIPT DI ONBOARDING                         │ 
│                                               │ 
│ 1. Legge i dati del lead dal CRM:            │ 
│    - Nome: "Ciccio"                           │ 
│    - Email: "ciccio@email.com"                │ 
│    - Piano: "Pro"                             │ 
│                                               │ 
│ 2. Compone l'email di onboarding:             │ 
│    - Template predefinito                     │ 
│    - Variabile dinamica: nome del cliente     │ 
│    - Link al materiale di onboarding          │ 
│                                               │ 
│ 3. Invia l'email:                             │ 
│    "Ciao Ciccio, benvenuto in azienda!        │ 
│     Sarai chiamato a breve.                   │ 
│     Ecco il link con l'onboarding material."  │ 
│                                               │ 
│ 4. Logga l'invio nel CRM                      │ 
└──────────────────────────────────────────────┘ 
 
RISULTATO:  
• Il lead riceve l'email ISTANTANEAMENTE 
• Nessun intervento umano necessario 
• Nessun consumo di token LLM 
• Processo 100% deterministico 
• Zero possibilità di dimenticarsi 
La Differenza Concettuale con il Workflow LLM 
L'autore sottolinea una distinzione fondamentale tra hook e workflow LLM: 

--- PAGE 176 ---
"A livello concettuale sono due cose che sono simili se non identiche. A livello pratico questo non 
lo è. Perché in questo caso stiamo letteralmente staccando l'inizio di un workflow dalla fine di un 
altro. Lo stiamo facendo in automatico." 
Confronto dettagliato: 
text 
APPROCCIO LLM (senza hook): 
──────────────────────────── 
Task 1: Claude inserisce il lead nel CRM 
    ↓ 
Claude deve "capire" che deve mandare un'email 
    ↓ 
Claude genera il testo dell'email (non deterministico) 
    ↓ 
Claude invia l'email (potrebbe sbagliare) 
    ↓ 
Task 2: continua il lavoro 
 
PROBLEMI: 
• Claude potrebbe dimenticarsi di inviare l'email 
• Il testo dell'email varia ogni volta 
• Consuma token 
• Richiede contesto per sapere come fare 
• Se il contesto è saturo, potrebbe fallire 
 
 
APPROCCIO HOOK (con hook): 
────────────────────────── 
Task 1: Claude inserisce il lead nel CRM 
    ↓ 
[FINE TASK 1 → HOOK SCATTA AUTOMATICAMENTE] 
    ↓ 
Script deterministico invia l'email (sempre identica) 
    ↓ 
Task 2: continua il lavoro (separatamente) 
 
VANTAGGI: 
• L'email viene SEMPRE inviata (garantito) 
• Il testo è sempre lo stesso (deterministico) 
• Zero token consumati 
• Non serve contesto 
• Funziona anche se il contesto è saturo 
Casi d'Uso Aziendali per gli Hooks 
Basandosi sul principio illustrato nella guida, ecco una mappa di casi d'uso aziendali: 
text 
MAPPA CASI D'USO HOOKS IN AMBITO BUSINESS 
══════════════════════════════════════════ 
 

--- PAGE 177 ---
VENDITE: 
├── Lead entra nel CRM → Email di benvenuto automatica 
├── Lead completa onboarding → Notifica al sales team 
├── Deal chiuso → Fattura automatica generata 
└── Follow-up scaduto → Reminder automatico 
 
SVILUPPO: 
├── Claude modifica un file → Backup automatico 
├── Build completata → Notifica Slack al team 
├── Test fallito → Report automatico via email 
└── Deploy completato → Screenshot automatico della pagina 
 
CONTENUTI: 
├── Post generato → Salvato automaticamente in draft folder 
├── Pubblicazione completata → Log in foglio di tracciamento 
├── Errore nella pubblicazione → Notifica al social media manager 
└── Engagement check → Report giornaliero automatico 
 
OPERAZIONI: 
├── Task completata → Aggiornamento status nel project manager 
├── Bug trovato → Ticket automatico nel sistema di tracking 
├── Sessione di lavoro terminata → Log automatico delle attività 
└── Costo sessione supera soglia → Alert automatico 
La Scalabilità degli Hooks attraverso i Livelli 
Gli hook possono essere configurati sia a livello local che global: 
text 
HOOKS A LIVELLO LOCAL: 
progetto/ 
└── .claude/ 
    └── settings.json    ← Hooks specifici per QUESTO progetto 
                            Es: "Dopo ogni modifica CSS,  
                            fai screenshot e confronta" 
 
HOOKS A LIVELLO GLOBAL: 
~/.claude/ 
└── settings.json        ← Hooks per TUTTI i progetti 
                            Es: "Suono di notifica alla  
                            fine di ogni task" 
                            Es: "Log automatico di ogni sessione" 
L'autore menziona specificamente che il suo hook di notifica sonora è configurato a livello 
globale: 
"Una volta che l'ho impostato in uno, lo voglio in tutti. Questo hook qui andrà nei miei settings 
globali." 

--- PAGE 178 ---
Questo è un esempio perfetto di come i livelli local/global/enterprise si applicano anche agli 
hook.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
