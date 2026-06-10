# 37.2 — Cosa Sono le Git Worktrees

Definizione del Concetto 
Le Git Worktrees sono una funzionalità avanzata di Git che permette di avere multiple copie di 
lavoro dello stesso progetto contemporaneamente, ciascuna su un branch (ramo) diverso. In 
pratica, è come avere più "tavoli di lavoro" separati dove potete sperimentare senza rischiare di 
rovinare il progetto principale. 
Spiegazione Approfondita 
L'autore usa un'analogia di processo produttivo per spiegare il concetto: 
 
ANALOGIA DELLA CATENA DI PRODUZIONE 
════════════════════════════════════ 
 
PROCESSO PRINCIPALE (main branch): 
    Nodo 1 → Nodo 2 → Nodo 3 → Nodo 4 → Nodo 5 → Nodo 6 
                                   │ 
                                   │ "A Nodo 4 c'è qualcosa  
                                   │  che non sono sicuro. 

--- PAGE 186 ---
                                   │  Voglio sperimentare  
                                   │  senza rischiare." 
                                   │ 
                                   ▼ 
BRANCH SPERIMENTALE (worktree): 
                               Nodo 4' → Nodo 5' → Test 
                                                     │ 
                                    ┌────────────────┤ 
                                    │                │ 
                                    ▼                ▼ 
                              FUNZIONA?          NON FUNZIONA? 
                                    │                │ 
                                    ▼                ▼ 
                              Merge con         Cancella il 
                              il processo       branch e 
                              principale        torna al 
                                                principale 
Il vantaggio è chiaro: potete sperimentare liberamente sapendo che il progetto principale è al 
sicuro. Se l'esperimento funziona, lo integrate (merge). Se non funziona, lo cancellate senza 
conseguenze. 
Perché le Worktrees Sono Superiori ai Branch Tradizionali 
La differenza tra un branch tradizionale e una worktree è che la worktree crea una directory fisica 
separata sul vostro computer: 
text 
BRANCH TRADIZIONALE: 
progetto/ 
├── [tutto il codice]     ← Dovete "switchare" tra branch 
└── .git/                    Potete lavorare su un solo  
                             branch alla volta 
 
WORKTREE: 
progetto/                 ← Branch principale 
├── [tutto il codice]        (potete continuare a lavorare qui) 
└── .git/ 
 
progetto-dark-mode/       ← Worktree separata 
├── [copia del codice]       (lavorate qui in parallelo) 
└── [modifiche sperimentali] 
Con le worktrees, potete letteralmente avere due finestre di Claude Code aperte: una sul 
progetto principale e una sulla worktree sperimentale. Lavorate in parallelo senza interferenze. 
Il Motivo per Cui Sono Importanti nel Contesto 
L'autore spiega un problema specifico che le worktrees risolvono: 

--- PAGE 187 ---
"Non voglio fare quello che ho fatto prima con il mio social media manager dove ho messo 
dentro tutti gli MCP per poi accorgermi che non mi serve un ClickUp MCP dentro il mio social 
media manager. Quindi devo rimuoverlo. Ma voglio avere una modalità per lavorare in maniera 
parallela senza dover per forza andare a rovinare il mio contesto e/o il mio progetto." 
La worktree protegge sia il codice (nessuna modifica al progetto principale) che il contesto (le 
sperimentazioni avvengono in un contesto Claude separato).

