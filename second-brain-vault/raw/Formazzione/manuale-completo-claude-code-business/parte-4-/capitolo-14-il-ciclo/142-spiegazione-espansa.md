# 14.2 — Spiegazione Espansa

L'autore introduce questo concetto contrapponendo due modalità di utilizzo di Claude Code: 
Modalità Comune (Inefficace): Task → Do 
text 
FLUSSO SENZA VERIFICA: 
 
Utente: "Fai X" 
Claude: [fa X] 
Utente: [verifica] → "Questo non va bene, correggi Y" 
Claude: [corregge Y] 
Utente: [verifica] → "Ora Z non funziona" 
Claude: [corregge Z] 
... loop lungo e frustrante ... 
L'autore la descrive così: "Molte persone utilizzano un'AI per dire 'fai qualcosa', danno una task, l'AI la fa, poi danno un 
feedback, e via dicendo. In realtà questo è utilizzare Claude Code non al meglio dei modi, perché manca una parte 
importante." 
Modalità Corretta (Efficace): Task → Do → Verify → Fix → Loop 
text 

--- PAGE 37 ---
FLUSSO CON VERIFICA: 
 
Utente: "Fai X" 
Claude: [fa X] 
Claude: [verifica il risultato] 
Claude: [identifica problemi] 
Claude: [corregge autonomamente] 
Claude: [verifica di nuovo] 
Claude: [se ok → presenta risultato finale] 
Claude: [se non ok → corregge di nuovo → loop] 
... 
Utente: [riceve un risultato già verificato e corretto] 
La differenza fondamentale è che Claude Code diventa responsabile della verifica, non l'utente. L'utente riceve un 
output che è già stato iterato e migliorato internamente.

