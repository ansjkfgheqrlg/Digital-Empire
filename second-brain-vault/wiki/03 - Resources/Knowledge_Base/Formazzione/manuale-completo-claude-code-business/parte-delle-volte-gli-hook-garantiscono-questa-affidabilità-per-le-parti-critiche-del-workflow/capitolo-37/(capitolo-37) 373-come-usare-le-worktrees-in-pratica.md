# 37.3 — Come Usare le Worktrees in Pratica
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow > capitolo-37]]

## Content

Procedura Pratica dalla Guida 
L'autore dimostra il processo completo con il suo sito web: 
text 
PROCEDURA COMPLETA WORKTREE 
════════════════════════════ 
 
PASSO 1: Definire cosa volete sperimentare 
────────────────────────────────────────── 
"Voglio aggiungere una dark mode al mio sito,  
 ma non sono sicuro che funzioni bene." 
 
PASSO 2: Chiedere a Claude di creare la worktree 
───────────────────────────────────────────────── 
"Per favore, utilizzando le git worktrees,  
 creami un progetto tale per cui io possa testare  
 una dark mode function all'interno del mio sito.  
 Dammi un local URL per vedere come va questa  
 funzionalità. Se funziona, e solo a quel punto,  
 allora decideremo cosa fare o se utilizzarla  
 all'interno della main branch oppure no." 
 
PASSO 3: Claude crea la worktree 
───────────────────────────────── 
• Crea un branch separato 
• Crea una directory fisica separata 
• Implementa la dark mode nella worktree 
• Fornisce un URL locale per il test 
 
PASSO 4: Test e Decisione 
───────────────────────── 
OPZIONE A — Funziona e mi piace: 
  "Perfetto, fai il processo di merge.  
   Fondi la mia worktree con il contesto  
   principale della mia repository GitHub  
   e poi pubblica su Vercel." 
 
OPZIONE B — Non funziona o non mi piace: 
  "Non mi piace. Cancella tutto, questa  
   branch non la utilizziamo." 

--- PAGE 188 ---
Cosa Succede Quando Cancellate una Worktree 
L'autore mostra che la cancellazione è pulita e completa: 
"Questa è una dot tree, quindi è una cartella nascosta. Ora la sta cancellando e l'ha cancellata. 
Ma qua dentro c'erano tutte le cose che avevamo fatto." 
La cancellazione di una worktree: 
1.​ Rimuove la directory fisica separata 
2.​ Rimuove il branch associato (se richiesto) 
3.​ Non tocca assolutamente il progetto principale 
4.​ Non influenza il branch main 
5.​ È come se l'esperimento non fosse mai avvenuto 
La Regola nelle Impostazioni dell'Autore 
L'autore rivela che ha regole specifiche nel suo CLAUDE.md per gestire le worktrees: 
"Ho già specificato nelle regole come queste git worktrees dovrebbero funzionare." 
E mostra l'inizio della regola: 
"Questo progetto usa una git worktree per lavorare in parallelo. Una worktree è una modalità 
isolata, una directory isolata che condivide la stessa git main repository." 
Questo significa che quando Claude lavora nel progetto dell'autore, sa già come comportarsi con 
le worktrees perché le regole sono codificate nel CLAUDE.md. Non serve spiegarglielo ogni 
volta. 
Combinazione con Agent Teams 
L'autore menziona un uso avanzato delle worktrees con gli Agent Teams: 
"Se gli avessi dato la possibilità di andare con Agent Teams, avrebbe sicuramente utilizzato 
Agent Teams perché è dentro il mio prompt. Perché semplicemente è molto più veloce e 
potremmo lavorare con più teammates in parallelo." 
L'idea è: 
1.​ Create una worktree per una nuova feature 
2.​ Lanciate un Agent Team nella worktree 

--- PAGE 189 ---
3.​ I teammate lavorano in parallelo (uno sul toggle UI, uno sul backend, uno sui test) 
4.​ Risultato: la feature viene sviluppata e testata in parallelo nella worktree 
5.​ Se tutto funziona, merge con il main 
Oppure, il pattern di varianti multiple: 
 
WORKTREES + AGENT TEAMS PER VARIANTI 
═════════════════════════════════════ 
 
"Fammi tre diversi design del bottone dark mode" 
 
    Worktree 1          Worktree 2          Worktree 3 
    ┌──────────┐       ┌──────────┐       ┌──────────┐ 
    │ Design A │       │ Design B │       │ Design C │ 
    │ (Toggle) │       │ (Slider) │       │ (Menu)   │ 
    └────┬─────┘       └────┬─────┘       └────┬─────┘ 
         │                  │                   │ 
         └──────────────────┼───────────────────┘ 
                            │ 
                      Scegliete il migliore 
                            │ 
                            ▼ 
                      Merge con main 
Ogni worktree è isolata, ogni Agent Team lavora indipendentemente, e voi scegliete il risultato 
migliore senza rischio. 
Errori Comuni con le Worktrees 
1.​ Non usare le worktrees per esperimenti rischiosi: se state per fare qualcosa di cui non 
siete sicuri, createne una. Il costo è zero, il beneficio è enorme. 
2.​ Dimenticare di cancellare le worktrees inutilizzate: le worktrees occupano spazio su 
disco. Cancellate quelle che non vi servono più. 
3.​ Fare merge senza testare: prima di fare merge con il main, testate SEMPRE la worktree. 
Un merge di codice rotto nel main è esattamente il problema che le worktrees 
dovrebbero prevenire. 
4.​ Non avere regole per le worktrees nel CLAUDE.md: se usate regolarmente le worktrees, 
codificate le regole nel CLAUDE.md così Claude sa come comportarsi. 
 
 
 

--- PAGE 190 ---

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
