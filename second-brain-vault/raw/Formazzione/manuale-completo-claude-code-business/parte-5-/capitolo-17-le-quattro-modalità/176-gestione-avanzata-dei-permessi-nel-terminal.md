# 17.6 — Gestione Avanzata dei Permessi nel Terminal

Nel Terminal, esiste un sistema di permessi più granulare accessibile tramite il comando permissions: 

--- PAGE 60 ---
text 
SISTEMA DI PERMESSI GRANULARE: 
 
Allow (Consenti): 
→ Il tool è sempre permesso senza chiedere 
→ Esempio: "Allow bash" = i comandi bash vengono eseguiti automaticamente 
 
Ask (Chiedi): 
→ Chiede sempre il permesso prima di usare il tool 
→ Esempio: "Ask write" = chiede conferma prima di ogni scrittura su file 
 
Deny (Nega): 
→ Il tool non viene mai usato, nemmeno se richiesto 
→ Esempio: "Deny delete" = impossibile cancellare file in qualsiasi circostanza 
 
Workspace: 
→ Permessi specifici per il workspace/progetto corrente 
→ Permette configurazioni diverse per progetti diversi 
Questo sistema è più granulare delle quattro modalità principali perché permette di controllare i singoli tool 
individualmente anziché applicare una politica uniforme a tutti i tool.

