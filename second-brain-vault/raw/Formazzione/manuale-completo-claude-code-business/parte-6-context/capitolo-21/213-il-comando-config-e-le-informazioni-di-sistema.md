# 21.3 — Il Comando /config e le Informazioni di Sistema

Definizione del Concetto 
Il comando /config apre un pannello di configurazione completo che mostra tutte le impostazioni attive di Claude 
Code. Tra le informazioni disponibili in questo pannello, ci sono anche dati relativi alla gestione del contesto. 
Spiegazione Approfondita 
Quando digitate /config nel terminal, potete navigare tra diverse sezioni usando le frecce su/giù e il tasto Tab. Le 
sezioni principali sono: 
Sezione Config: 
●​
Autocompact: mostra se la compattazione automatica è attiva (on/off) 
●​
Thinking Mode: mostra se la modalità di pensiero estensivo è attiva 
●​
Rewind Checkpoint: mostra se i checkpoint di ripristino sono attivi 
●​
Tema e personalizzazione visiva 
●​
Teammate Mode e altre impostazioni avanzate 
Sezione Usage (raggiungibile premendo Tab): 
●​
Mostra quanto del modello è stato utilizzato nella sessione corrente 
●​
Nell'esempio della guida: "28% utilizzato al momento" 
Sezione Status (raggiungibile premendo Tab di nuovo): 
●​
Mostra un riepilogo delle informazioni della Status Line 

--- PAGE 84 ---
Autocompact nel Config 
L'impostazione più rilevante per il Context Management nel pannello /config è Autocompact. Quando questa è 
impostata su "on": 
●​
Claude compatta automaticamente il contesto quando raggiunge una certa soglia 
●​
Non dovete fare nulla manualmente per attivare la compattazione 
●​
Il sistema gestisce autonomamente la densità delle informazioni 
Quando è su "off": 
●​
Il contesto si riempie linearmente senza compressione 
●​
Dovete usare manualmente /compact per liberare spazio 
●​
Avete più controllo ma più responsabilità 
Raccomandazione: tenete Autocompact su on. La gestione automatica è generalmente superiore a quella manuale per 
la maggior parte degli utenti. Potrete sempre usare /compact manualmente in aggiunta quando necessario. 
Rewind Checkpoint nel Config 
Questa funzione è rilevante per il Context Management perché i checkpoint occupano spazio. Quando è su "on": 
●​
Claude salva dei punti di ripristino a cui potete tornare 
●​
Potete dire "torna alla versione precedente" e Claude lo farà 
●​
Questi checkpoint consumano una piccola quantità di contesto aggiuntiva 
Quando è su "off": 
●​
Non ci sono checkpoint 
●​
Non potete fare rollback delle azioni 
●​
Risparmiate una piccola quantità di contesto 
Raccomandazione: tenete i checkpoint su on. Lo spazio che consumano è minimo rispetto al vantaggio di poter tornare 
indietro in caso di errore. 
 
​

