# 2.7 — Insight Avanzato

Nella barra di stato di Claude Code (che vedremo come configurare nel Capitolo 8), viene mostrato un costo per ogni 
interazione. Questo costo rappresenta quanto avreste pagato se foste sul piano API. È un dato puramente informativo 
per chi usa un piano subscription, ma diventa critico per chi usa il piano API. 
L'autore mostra che una singola interazione ("Ciao, come stai?") ha un costo API di pochi centesimi, ma operazioni 
complesse come l'analisi di una repository con Agent Teams possono costare decine di euro in pochi minuti. 
La formula decisionale per la scelta del piano è: 
SE utilizzo_giornaliero > 2_ore → Piano Max 
SE utilizzo_giornaliero tra 30_min e 2_ore → Piano Pro 
SE utilizzo_occasionale < 30_min/giorno → Piano Pro (comunque, per il prezzo) 
SE team > 3_persone → Piano Enterprise 
SE esperienza_tecnica = alta E controllo_costi = necessario → Piano API (con cautela)

