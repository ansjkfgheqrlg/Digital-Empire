# 38.6 — Riepilogo Architetturale Completo

Il Disegno Completo 
La guida costruisce progressivamente un disegno architetturale che cresce capitolo dopo 
capitolo. Ecco la versione finale e completa: 
 
ARCHITETTURA COMPLETA DI UN PROGETTO CLAUDE CODE 
═════════════════════════════════════════════════ 
 
LIVELLO ENTERPRISE (opzionale, per aziende grandi) 
┌─────────────────────────────────────────────────────────┐ 
│ CLAUDE.md Enterprise                                    │ 
│ ├── Permessi a livello di sistema                       │ 
│ ├── Regole di sicurezza enterprise                      │ 
│ └── Override globale su tutto                           │ 
└─────────────────────────────────────────────────────────┘ 
            │ (override) 
            ▼ 
LIVELLO GLOBAL (~/.claude/) 
┌─────────────────────────────────────────────────────────┐ 
│ ├── CLAUDE.md Globale                                   │ 
│ │   ├── Permessi globali                                │ 
│ │   ├── Istruzioni di sicurezza globali                 │ 
│ │   └── Stile e brand globali                           │ 
│ ├── agents/ (sub-agenti globali)                         
│ │   ├── researcher.md                                   │ 
│ │   ├── reviewer.md                                     │ 
│ │   └── qa.md                                           │ 
│ ├── skills/ (skill globali)                             │ 
│ ├── rules/ (regole globali)                             │ 
│ ├── settings.json (hooks globali)                       │ 
│ └── .mcp.json (MCP globali, es: Chrome Dev Tool)        │ 
└─────────────────────────────────────────────────────────┘ 
            │ (si applica a tutti i progetti) 
            ▼ 
LIVELLO LOCAL (progetto/.claude/) 
┌─────────────────────────────────────────────────────────┐ 
│ ├── CLAUDE.md del Progetto                              │ 
│ │   └── Conciso: what, how, why, do, don't              │ 
│ ├── agents/ (sub-agenti del progetto)                   │ 

--- PAGE 200 ---
│ ├── skills/ (skill del progetto)                        │ 
│ │   └── [nome-skill]/                                   │ 
│ │       ├── skill.md (orchestratore)                    │ 
│ │       ├── scripts/ (codice deterministico)            │ 
│ │       └── references/ (dati di riferimento)           │ 
│ ├── rules/ (regole modulari)                            │ 
│ │   ├── design-fidelity.md                              │ 
│ │   ├── security.md                                     │ 
│ │   └── screenshot-workflow.md                          │ 
│ ├── settings.json (hooks + permessi locali)             │ 
│ ├── .local.json (istruzioni personali, non condivise)   │ 
│ └── .mcp.json (MCP del progetto)                        │ 
└─────────────────────────────────────────────────────────┘ 
            │ 
            ▼ 
COMPONENTI INIETTATI DA ANTHROPIC 
┌─────────────────────────────────────────────────────────┐ 
│ ├── System Prompt (~10% del contesto)                   │ 
│ ├── System Tools (bash, read, write, edit, etc.)        │ 
│ ├── Tool Calling                                        │ 
│ └── Auto Memory (memory.md, auto_memory.md)             │ 
└─────────────────────────────────────────────────────────┘ 
            │ 
            ▼ 
CONTESTO DELLA SESSIONE 
┌─────────────────────────────────────────────────────────┐ 
│ ├── Tutto quanto sopra viene caricato qui               │ 
│ ├── + i vostri messaggi                                 │ 
│ ├── + le risposte di Claude                             │ 
│ ├── + Autocompact Buffer (~33K token riservati)         │ 
│ └── = La vostra finestra di lavoro                      │ 
└─────────────────────────────────────────────────────────┘ 
            │ 
            ▼ 
DEPLOYMENT (rendere accessibile al mondo) 
┌─────────────────────────────────────────────────────────┐ 
│ ├── Modal: cloud functions, API, skill deployate        │ 
│ ├── Vercel: frontend, siti web, web app                 │ 
│ ├── GitHub: version control, collaborazione             │ 
│ ├── GitHub Actions: CI/CD, automazioni                  │ 
│ ├── Supabase: backend, database, autenticazione         │ 
│ └── Stripe: pagamenti, abbonamenti                      │ 
└─────────────────────────────────────────────────────────┘ 
Questo disegno rappresenta il quadro completo di come un progetto Claude Code professionale 
è strutturato, dalla configurazione di base fino al deployment e alla monetizzazione. 
 
Riepilogo della Parte 10 
In questa Parte finale avete appreso: 
1.​ Hooks: script deterministici che si attivano automaticamente a eventi specifici, senza 
consumo di token e con affidabilità garantita 

--- PAGE 201 ---
2.​ Hook sonoro: l'esempio base per essere notificati quando Claude finisce una task, 
risparmiando potenzialmente ore di attesa 
3.​ Hook aziendali: automazioni come l'invio automatico di email di onboarding quando un 
lead entra nel CRM 
4.​ La differenza fondamentale tra hook e workflow LLM: gli hook sono deterministici, 
gratuiti, istantanei e affidabili; i workflow LLM sono non deterministici, costosi, più lenti e 
potenzialmente inaffidabili 
5.​ Auto Memory: il meccanismo che permette a Claude di salvare e recuperare informazioni 
tra sessioni diverse attraverso file fisici (memory.md, auto_memory.md) 
6.​ Il pattern "Salva e Continua": salvare lo stato del progetto in memoria quando il contesto 
raggiunge il 60-70%, poi continuare in una nuova sessione con contesto fresco 
7.​ Git Worktrees: directory isolate che permettono di sperimentare in parallelo senza 
rischiare il progetto principale, con possibilità di merge se l'esperimento ha successo 
8.​ Deployment su Modal: il processo completo per portare una skill nel cloud e renderla 
accessibile tramite URL pubblico 
9.​ Il modello di monetizzazione end-to-end: frontend + autenticazione (Supabase) + 
pagamento (Stripe) + servizio (skill) + deployment (Modal/Vercel) 
10.​L'architettura completa: dal livello enterprise al deployment, passando per global, local, 
componenti Anthropic e gestione del contesto 
 
Riepilogo Generale del Manuale 
Avete completato il Manuale Completo di Claude Code per il Business. Ecco il percorso che 
avete fatto: 
Parte 
Contenuto 
Competenza Acquisita 
1 
Fondamenta e Panoramica 
Sapete cosa è Claude Code e come scegliere il piano 
2 
Installazione e Configurazione 
Sapete installare e configurare Claude Code 
3 
CLAUDE.md e Architettura 
Sapete strutturare un progetto professionale 

--- PAGE 202 ---
4 
Costruire Progetti 
Sapete costruire siti web e applicazioni complete 
5 
Modalità di Permesso 
Sapete quando usare Plan Mode vs Bypass Permission 
6 
Context Management 
Sapete gestire il contesto come un professionista 
7 
Sub-agenti e Agent Teams 
Sapete delegare e parallelizzare con team di agenti 
8 
Sistema delle Skill 
Sapete creare, importare e monetizzare skill 
9 
MCP 
Sapete installare, gestire e ottimizzare gli MCP 
10 
Funzionalità Avanzate e Deployment 
Sapete automatizzare, versionare e deployare 
Come dice l'autore della guida: 
"Alla fine sarete sicuramente nel top 10% delle persone che usano Claude Code." 
Con questo manuale, avete le basi per costruire qualsiasi cosa vogliate — e le competenze per 
trasformare quella costruzione in valore reale e monetizzabile.

