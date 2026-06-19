# 23.2 — Il Primacy Bias (Bias di Primato)
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-23]]

## Content

Definizione del Concetto 
Il Primacy Bias è la tendenza degli LLM a dare maggiore peso e attenzione alle informazioni che appaiono all'inizio del 
contesto. Proprio come gli esseri umani tendono a ricordare meglio le prime informazioni ricevute (il "primo impatto"), gli 
LLM processano le istruzioni iniziali con maggiore fedeltà. 
Spiegazione Approfondita 
Questo bias ha implicazioni enormi per come strutturate il vostro CLAUDE.md e i vostri prompt. Le istruzioni posizionate 
all'inizio del contesto: 
●​
Vengono seguite con maggiore coerenza 
●​
Vengono rispettate anche quando il contesto si riempie 
●​
Hanno un effetto più duraturo sulla sessione di lavoro 
●​
Resistono meglio alla "diluizione" causata da messaggi successivi 
Applicazione Pratica Diretta 
Regola d'oro del Primacy Bias: 
Mettete le regole più importanti PER PRIME nel CLAUDE.md. 
Esempi concreti: 
in Markdown 
# CLAUDE.md — Struttura Ottimizzata per Primacy Bias 
 
## REGOLE CRITICHE (INIZIO = massima attenzione) 
- NON cancellare MAI il file .env 
- NON rimuovere MAI le API key dal codice 
- NON modificare MAI il database di produzione 
- Chiedi SEMPRE conferma prima di eliminare file 
 
## Regole Operative (mezzo = attenzione moderata) 
- Usa TypeScript per tutti i nuovi file 
- Segui le convenzioni ESLint del progetto 
- Scrivi commenti in italiano 
 
## Preferenze Stilistiche (fine = attenzione elevata grazie al Recency) 
- Preferisci componenti funzionali a classi 

--- PAGE 94 ---
- Usa Tailwind CSS per lo styling 
Notate come le regole critiche per la sicurezza sono posizionate all'inizio, dove il Primacy Bias garantisce la massima 
attenzione. Le regole operative sono nel mezzo (dove saranno meno "ricordate" ma non sono critiche se 
occasionalmente ignorate). Le preferenze stilistiche sono alla fine, dove il Recency Bias le mantiene presenti. 
L'Analogia della Lista della Spesa 
L'autore della guida usa un'analogia perfetta. Dice di avere "una memoria personale di un pesce rosso" e racconta: 
Immaginate che qualcuno vi dica: "Per favore vai al supermercato alle 6 e compra: biscotti, latte, pane, uova, burro, 
farina, zucchero, sale, olio, aceto." 
La maggior parte delle persone ricorderà: 
●​
Biscotti (primo elemento — Primacy Bias) ✅ 
●​
Aceto (ultimo elemento — Recency Bias) ✅ 
●​
Pochi o nessuno degli elementi nel mezzo ❌ 
Lo stesso identico pattern si applica agli LLM. 
Errori Comuni 
1.​
Mettere regole critiche nel mezzo del CLAUDE.md: è il peggior posto possibile. Saranno le prime a essere 
"dimenticate" quando il contesto si riempie. 
2.​
Mettere disclaimer o introduzioni lunghe all'inizio: se iniziate il CLAUDE.md con tre paragrafi di spiegazione 
generale del progetto, state "sprecando" la posizione più pregiata (l'inizio) per informazioni a basso impatto. 
3.​
Non ordinare le regole per importanza: molti utenti scrivono le regole nell'ordine in cui le pensano, non 
nell'ordine di importanza. Ristrutturate il CLAUDE.md mettendo le regole più critiche prima.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - General|General Area]]
