# 25.1 — Cosa Sono gli Agent Teams
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-7-sub-agenti > capitolo-25]]

## Content

Definizione del Concetto 
Gli Agent Teams sono una funzionalità relativamente recente introdotta da Anthropic che permette di creare un team di 
agenti collaborativi che possono comunicare tra loro in modo bidirezionale. A differenza dei sub-agenti tradizionali (dove 
la comunicazione è solo dal sub-agente verso l'agente principale), negli Agent Teams ogni agente può parlare con ogni 
altro agente del team. 
Spiegazione Approfondita 
La differenza fondamentale tra sub-agenti e Agent Teams si capisce meglio con un diagramma comparativo: 
SUB-AGENTI (comunicazione monodirezionale): 
text 
    Researcher ──────►  
                         \ 
     Reviewer  ──────────► Main Agent 
                         / 
     QA ────────────────► 
 
• Ogni sub-agente lavora isolato 
• Nessuna comunicazione tra sub-agenti 
• Solo il risultato va all'agente principale 
• Costo: BASE (1x) 
AGENT TEAMS (comunicazione bidirezionale): 
text 
    Code Quality ◄────────► Security 
          │    \              /    │ 
          │     \            /     │ 
          │      ▼          ▼      │ 
          │     Team Leader        │ 
          │      ▲          ▲      │ 
          │     /            \     │ 
          │    /              \    │ 
     Architect ◄──────────► Content 
 
• Ogni agente può parlare con ogni altro agente 
• Condivisione di informazioni reciproca 
• Coordinamento automatico dei lavori 
• Costo: ELEVATO (3-5x rispetto ai sub-agenti) 
Il Meccanismo della Comunicazione Bidirezionale 
Negli Agent Teams, quando un agente scopre qualcosa di rilevante per un altro agente, può comunicarglielo 
direttamente. Questo elimina il collo di bottiglia dell'agente principale come unico punto di comunicazione. 
Esempio pratico dalla guida: 
L'autore analizza una repository GitHub con un Agent Team di 4 teammate: 
●​
Code Quality: analizza la qualità del codice 
●​
Security: analizza la sicurezza 

--- PAGE 115 ---
●​
Architect: analizza l'architettura 
●​
Content: analizza la documentazione 
Durante l'analisi, il teammate Security potrebbe trovare una vulnerabilità che impatta l'architettura. In un sistema con 
sub-agenti tradizionali, dovrebbe: 
1.​
Comunicare il problema all'agente principale 
2.​
L'agente principale dovrebbe poi comunicarlo al sub-agente Architect 
3.​
L'Architect dovrebbe poi proporre una soluzione 
4.​
La soluzione tornerebbe all'agente principale 
Con un Agent Team, il processo è diretto: 
1.​
Security comunica direttamente ad Architect: "Ho trovato una vulnerabilità nella struttura X. Devi ristrutturare 
Y." 
2.​
Architect modifica l'architettura 
3.​
Entrambi aggiornano il Team Leader 
Questo è molto più veloce e produce risultati più coerenti. 
La Struttura del Team 
text 
STRUTTURA DI UN AGENT TEAM 
═══════════════════════════ 
 
                ┌──────────────────┐ 
                │   TEAM LEADER    │ 
                │   (Main Agent)   │ 
                │                  │ 
                │ Responsabilità:  │ 
                │ • Coordinamento  │ 
                │ • Assegnazione   │ 
                │   task           │ 
                │ • Raccolta       │ 
                │   risultati      │ 
                │ • Decisioni      │ 
                │   finali         │ 
                └────────┬─────────┘ 
                         │ 
            ┌────────────┼────────────┐ 
            │            │            │ 
    ┌───────┴──────┐ ┌───┴───┐ ┌─────┴────────┐ 
    │  Teammate 1  │ │ T. 2  │ │  Teammate 3  │ 
    │  (es. Code   │ │(Sec.) │ │  (es. Arch.) │ 
    │   Quality)   │ │       │ │              │ 
    └──────┬───────┘ └───┬───┘ └──────┬───────┘ 
           │             │            │ 
           └─────────────┼────────────┘ 
                         │ 
              Comunicazione bidirezionale 
              tra tutti i teammate 
Come il Team Leader "Spawna" i Teammate 
Quando date un comando per creare un Agent Team, il Team Leader (l'agente principale) analizza la task e decide: 
1.​
Quanti teammate servono (potete specificarlo voi o lasciarlo decidere a lui) 
2.​
Quali ruoli assegnare a ciascun teammate 
3.​
Quali responsabilità specifiche dare a ciascuno 
4.​
Come suddividere il lavoro per evitare duplicazioni 
Nell'esempio della guida, l'autore chiede: 

--- PAGE 116 ---
"Crea un agent team con un massimo di quattro compagni di squadra per analizzare questa repository." 
Il Team Leader decide autonomamente di creare: 
●​
Code Quality teammate 
●​
Security teammate 
●​
Architect teammate 
●​
Content teammate 
Ciascuno con responsabilità specifiche e complementari. 
L'Interfaccia di Monitoraggio 
La guida mostra che è possibile monitorare i teammate in tempo reale. Premendo Shift + freccia giù nel terminal, si 
accede a una visualizzazione live che mostra: 
text 
VISUALIZZAZIONE LIVE AGENT TEAMS 
════════════════════════════════ 
 
┌─── Main (Team Leader) ──────────────────────────┐ 
│ Contesto: 45.000/200.000 tokens                 │ 
│ Tools chiamati: 12                               │ 
│ Stato: coordinamento                             │ 
└─────────────────────────────────────────────────┘ 
 
┌─── Code Quality ────────────────────────────────┐ 
│ Contesto: 171.000/200.000 tokens                │ ← QUASI PIENO 
│ Tools chiamati: 47                               │ 
│ Stato: analisi in corso                          │ 
└─────────────────────────────────────────────────┘ 
 
┌─── Security ────────────────────────────────────┐ 
│ Contesto: 89.000/200.000 tokens                 │ 
│ Tools chiamati: 63                               │ 
│ Stato: scan vulnerabilità                        │ 
└─────────────────────────────────────────────────┘ 
 
┌─── Architect ───────────────────────────────────┐ 
│ Contesto: 120.000/200.000 tokens                │ 
│ Tools chiamati: 35                               │ 
│ Stato: revisione struttura                       │ 
└─────────────────────────────────────────────────┘ 
Dalla guida emerge un dato importante: il teammate Code Quality ha raggiunto i 171.000 token nel suo contesto. 
Successivamente fa un reset del context e scende a 59.000, dimostrando che anche i teammate hanno la capacità di 
fare context management automatico. 
Le Shared Task — Coordinamento Automatico 
Una caratteristica specifica degli Agent Teams è la gestione delle shared task (task condivise). Anthropic ha 
implementato un meccanismo che impedisce a due agenti di lavorare sulla stessa identica cosa: 
"Loro sanno in automatico che cosa uno sta facendo e quindi Anthropic in automatico ha fatto sì che noi non avessimo 
mai il problema di avere due agent che lavorano sulla stessa identica cosa." 

--- PAGE 117 ---
Questo significa che se il teammate Code Quality sta analizzando il file auth.js, il teammate Security sa che quel file è 
"occupato" e analizzerà prima altri file, per poi tornare su auth.js quando sarà libero (con eventuali note del teammate 
precedente).

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
