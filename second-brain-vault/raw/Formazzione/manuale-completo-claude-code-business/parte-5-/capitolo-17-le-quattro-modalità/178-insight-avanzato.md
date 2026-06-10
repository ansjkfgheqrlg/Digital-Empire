# 17.8 — Insight Avanzato

Il quinto livello: Don't Ask (solo Terminal) 
L'autore menziona una modalità aggiuntiva disponibile solo nel Terminal e non presente nelle IDE: 
text 
PERMESSI NEL TERMINAL: 
 

--- PAGE 61 ---
Allow → "We always allow this tool" 
Ask   → "We always ask permission" (default) 
Deny  → "We always reject request to use denied tools" 
 
Deny è il "Don't Ask" — non chiede nemmeno, rifiuta direttamente. 
La differenza tra "Ask" e "Deny" è sottile ma importante: 
●​
Ask: "Posso usare questo tool?" → L'utente può dire sì o no 
●​
Deny: Il tool non viene mai usato, Claude Code non chiede nemmeno. Il tool è effettivamente disabilitato. 
Questo è utile per disabilitare completamente strumenti che non volete siano mai usati nel vostro progetto (per 
esempio, disabilitare la capacità di cancellare file in un ambiente di produzione). 
Workflow raccomandato dall'autore: 
L'autore rivela il suo workflow personale basato sulla citazione del creatore di Claude Code, Boris: 
"Come disse Boris, creatore di Claude Code — e che lui stesso fa questa cosa — spende gran parte del suo tempo in 
Plan Mode, e una volta che il piano ha senso ed è fatto in maniera corretta, allora Claude Code può fare il cosiddetto 
one-shot." 
text 
WORKFLOW BORIS/AUTORE: 
 
Fase 1: PLAN MODE (70-80% del tempo) 
├── Definire il progetto 
├── Creare il piano 
├── Revisionare il piano 
├── Modificare il piano 
├── Ri-revisionare 
├── Approvare il piano finale 
└── Tempo: la maggior parte della sessione 
 
Fase 2: BYPASS PERMISSION (20-30% del tempo) 
├── Eseguire il piano approvato 
├── Claude Code lavora in autonomia 
├── One-shot (idealmente) 
└── Tempo: relativamente breve 
 
Proporzione ideale: PIANO >> ESECUZIONE

