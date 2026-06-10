# 24.6 — Parallelizzazione dei Sub-agenti

Definizione del Concetto 
La parallelizzazione dei sub-agenti consiste nell'eseguire più sub-agenti contemporaneamente in terminal separati, in 
modo che lavorino in parallelo su task diverse anziché in sequenza. 
Spiegazione Approfondita 
Nella guida originale, l'autore mostra come parallelizzare i sub-agenti aprendo più istanze di Claude Code: 
text 
TERMINAL 1 (Agente Principale) 
┌─────────────────────────────────┐ 
│ $ claude --dangerously-skip-    │ 
│   permissions                    │ 
│                                  │ 
│ > "Per favore chiama il         │ 
│    reviewer sub-agent..."       │ 
└─────────────────────────────────┘ 
 

--- PAGE 113 ---
TERMINAL 2 (Parallelo) 
┌─────────────────────────────────┐ 
│ $ claude --dangerously-skip-    │ 
│   permissions                    │ 
│                                  │ 
│ > "Per favore chiama il         │ 
│    QA sub-agent..."             │ 
└─────────────────────────────────┘ 
 
TERMINAL 3 (Parallelo) 
┌─────────────────────────────────┐ 
│ $ claude --dangerously-skip-    │ 
│   permissions                    │ 
│                                  │ 
│ > "Per favore fai una ricerca   │ 
│    sulla pasta con il           │ 
│    researcher sub-agent..."     │ 
└─────────────────────────────────┘ 
Ogni istanza ha il proprio contesto indipendente. Non si influenzano a vicenda. Tutte hanno accesso allo stesso file 
system (stessa cartella del progetto), quindi le modifiche fatte da un sub-agente sono visibili agli altri. 
L'Importanza del Flusso Monodirezionale 
Un punto critico sottolineato nella guida è che con i sub-agenti tradizionali, il flusso di informazioni è monodirezionale: 
dai sub-agenti all'agente principale. 
text 
FLUSSO MONODIREZIONALE DEI SUB-AGENTI 
═══════════════════════════════════════ 
 
     Sub-agente 1 ──────────► 
                              \ 
     Sub-agente 2 ────────────►  Agente Principale 
                              / 
     Sub-agente 3 ──────────► 
 
OGNI FRECCIA = solo risultato (2K token circa) 
NESSUNA COMUNICAZIONE TRA SUB-AGENTI 
I sub-agenti non si parlano tra loro. Sub-agente 1 non sa cosa sta facendo Sub-agente 2, e viceversa. Questo è un 
vantaggio per il context management (nessun overhead di comunicazione) ma un limite per task che richiedono 
collaborazione. Per superare questo limite, Anthropic ha introdotto gli Agent Teams, che vedremo nel capitolo 
successivo.

