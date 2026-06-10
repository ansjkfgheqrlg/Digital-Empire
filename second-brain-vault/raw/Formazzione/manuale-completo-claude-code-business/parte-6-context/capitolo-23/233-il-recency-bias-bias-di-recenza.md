# 23.3 — Il Recency Bias (Bias di Recenza)

Definizione del Concetto 
Il Recency Bias è la tendenza degli LLM a dare maggiore peso alle informazioni che appaiono alla fine del contesto — 
cioè le informazioni più recenti nella conversazione. L'ultimo messaggio che inviate, le ultime istruzioni che date, le 
ultime informazioni che condividete avranno un impatto sproporzionatamente elevato sulla risposta di Claude. 
Spiegazione Approfondita 
Il Recency Bias funziona a vostro vantaggio in diversi modi: 
1.​
Correzioni immediate funzionano bene: se Claude fa un errore e lo correggete immediatamente, la correzione 
(essendo l'informazione più recente) viene rispettata con alta fedeltà. 
2.​
L'ultimo prompt è il più influente: se dovete dare un'istruzione critica, fatelo nell'ultimo messaggio prima che 
Claude inizi a lavorare. 
3.​
Le decisioni recenti prevalgono: se all'inizio della conversazione avete detto "usa il colore blu" e alla fine dite 
"usa il colore rosso", Claude userà il rosso (Recency Bias) a meno che la regola del blu non sia nel 
CLAUDE.md (Primacy Bias del system prompt). 
Applicazione Pratica 
Potete sfruttare il Recency Bias in modo strategico: 

--- PAGE 95 ---
Strategia "Rinforzo Finale":​
Prima di dare un comando complesso a Claude, ripetete le istruzioni più importanti nell'ultimo messaggio: 
Utente: "Costruisci il componente di autenticazione.  
RICORDA:  
- usa Supabase come backend 
- email + password, NO magic link 
- salva nome e email nel database 
Procedi." 
Le tre istruzioni dopo "RICORDA" sono posizionate alla fine del prompt (Recency Bias), quindi Claude le seguirà con 
maggiore fedeltà. 
Strategia "Prompt di Continuazione":​
Quando salvate informazioni in memoria per continuare in una nuova sessione, l'autore della guida mostra che Claude 
produce un "prompt di continuazione" — un messaggio predefinito da usare nella sessione successiva. Questo prompt, 
essendo il primo messaggio della nuova sessione, beneficerà del Primacy Bias nella nuova sessione E del Recency 
Bias (perché è l'ultimo contesto significativo salvato).

