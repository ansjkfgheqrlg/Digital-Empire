# 33.3 — Il Collegamento con il Lost in the Middle

Definizione del Concetto 
L'impatto degli MCP sul contesto non è solo quantitativo (occupano spazio) ma anche qualitativo: gli MCP pesanti 
spostano le vostre informazioni utili nella zona "Lost in the Middle", degradando la qualità delle risposte. 
Spiegazione Approfondita 
La guida collega esplicitamente l'impatto degli MCP al fenomeno del Lost in the Middle: 
"Vi ricordate il Lost in the Middle di cui abbiamo discusso all'inizio? Vuol dire che noi siamo arrivati già qua. Abbiamo 
fatto una cosa orribile per caricare queste tipologie di MCP." 
Ecco cosa succede visivamente: 
IMPATTO MCP SUL LOST IN THE MIDDLE 
═══════════════════════════════════ 

--- PAGE 164 ---
 
SENZA MCP PESANTI: 
┌────────────────────────────────────────────┐ 
│ System Prompt [INIZIO - alta attenzione]   │ 10% 
│ CLAUDE.md     [INIZIO - alta attenzione]   │ 5% 
│ ───────────────────────────────────────    │ 
│ Messaggi      [MEZZO → FINE]               │ 20% 
│ ───────────────────────────────────────    │ 
│ Ultimo prompt [FINE - alta attenzione]     │ 1% 
│ SPAZIO LIBERO                              │ 64% 
└────────────────────────────────────────────┘ 
→ Le vostre informazioni sono nelle zone di ALTA attenzione 
→ Risultato: risposte eccellenti 
 
CON MCP PESANTI (27% occupato): 
┌────────────────────────────────────────────┐ 
│ System Prompt [INIZIO - alta attenzione]   │ 10% 
│ MCP PESANTE   [INIZIO→MEZZO]              │ 27% 
│ ───────────────────────────────────────    │ 
│ CLAUDE.md     [MEZZO - BASSA attenzione]   │ 5%  ← PROBLEMA! 
│ Messaggi      [MEZZO - BASSA attenzione]   │ 20% ← PROBLEMA! 
│ ───────────────────────────────────────    │ 
│ Ultimo prompt [FINE - alta attenzione]     │ 1% 
│ SPAZIO LIBERO                              │ 37% 
└────────────────────────────────────────────┘ 
→ Il CLAUDE.md e i messaggi sono nella zona di BASSA attenzione 
→ Risultato: Claude "dimentica" le vostre regole e istruzioni 
→ Risposte degradate significativamente 
L'MCP pesante non solo occupa spazio, ma spinge le vostre informazioni importanti (CLAUDE.md, regole, messaggi) 
nella zona cieca del Lost in the Middle. Questo è il doppio danno degli MCP pesanti. 
La Regola Pratica 
"Quello che noi vogliamo fare è andare a costruire qualcosa che ci permetta di essere efficienti. Ci permetta di agire 
nelle fasi qui [inizio e fine] con le cose più importanti. Non vogliamo mai che il nostro prompt iniziale sia nell'intervallo in 
cui sostanzialmente l'LLM perde qualsiasi cosa." 
Tradotto in regola pratica: 
Se un MCP occupa più del 5% del contesto, valutate seriamente la conversione in skill. 
Sopra il 5%, l'MCP inizia a spingere le vostre informazioni nella zona Lost in the Middle. Sopra il 15%, l'impatto è 
significativo. Sopra il 25%, è devastante.

