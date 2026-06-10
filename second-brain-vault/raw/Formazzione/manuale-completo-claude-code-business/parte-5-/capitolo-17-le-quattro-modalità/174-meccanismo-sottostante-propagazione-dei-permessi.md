# 17.4 — Meccanismo Sottostante: Propagazione dei Permessi

L'autore introduce un concetto critico che molti ignorano: i permessi si propagano a tutti i sotto-agenti. 
"Quando diamo una permission all'agente principale, tutte queste permission si replicano anche a tutti i sottoagenti o a 
qualsiasi cosa concateniamo dopo." 
text 
PROPAGAZIONE DEI PERMESSI: 
 
Agente Principale (Bypass Permission) 
     ↓ eredita 
Sub-agente Researcher (Bypass Permission) 
     ↓ eredita 
Sub-agente Reviewer (Bypass Permission) 
     ↓ eredita 
Sub-agente QA (Bypass Permission) 
 

--- PAGE 59 ---
IMPLICAZIONE: Se l'agente principale ha Bypass Permission, 
TUTTI i sotto-agenti avranno Bypass Permission. 
Non è possibile dare Bypass Permission al principale 
e Ask Before Edits a un sotto-agente. 
Questo ha implicazioni di sicurezza significative: se date bypass permission all'agente principale e uno dei sotto-agenti 
commette un errore, quell'errore viene eseguito senza alcuna richiesta di conferma.

