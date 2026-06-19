# 20.2 — Cosa Sono i Token
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-20]]

## Content

Definizione del Concetto 
Un token è l'unità fondamentale con cui gli LLM misurano e processano il testo. In termini semplificati — come 
suggerisce la guida originale — potete pensare a un token come una parola. In realtà tecnicamente un token 
corrisponde a circa 3-4 lettere, ma per finalità pratiche e per questo corso, l'approssimazione "un token ≈ una parola" è 
sufficiente. 
Spiegazione Approfondita 
Quando voi scrivete un messaggio a Claude, quel messaggio viene scomposto in token prima di essere processato. Ad 
esempio: 
●​
La frase "Ciao come stai" potrebbe essere scomposta in 3-4 token 
●​
La frase "Per favore analizza il codice del mio progetto e trova i bug" potrebbe essere 10-12 token 
●​
Un intero file di codice di 500 righe potrebbe essere migliaia di token 
Il modello Claude ha un limite massimo di token per il contesto. A seconda del modello utilizzato, questo limite può 
essere: 
●​
200.000 token (200K) per le configurazioni standard 
●​
1.000.000 token (1M) per configurazioni specifiche 
Questo numero rappresenta il totale di tutto ciò che può stare nella "scrivania" del modello: input vostro, output di 
Claude, istruzioni di sistema, MCP, skill, memoria — tutto insieme. 
Il Meccanismo Sottostante 
I token non corrispondono esattamente alle parole perché il sistema di tokenizzazione (il processo con cui il testo viene 
convertito in token) funziona diversamente dalla divisione per parole che facciamo noi umani: 
 
Esempio di tokenizzazione approssimativa: 
 
Testo: "Costruiamo un'applicazione web" 
Token: ["Costru", "iamo", " un", "'", "applic", "azione", " web"] 
Risultato: ~7 token per 3 parole 
 

--- PAGE 74 ---
Testo: "Hello world" 
Token: ["Hello", " world"] 
Risultato: ~2 token per 2 parole 
Notate come le parole italiane tendono a consumare più token rispetto a quelle inglesi. Questo accade perché i modelli 
LLM sono stati addestrati prevalentemente su testo inglese, quindi il tokenizzatore è più "efficiente" con l'inglese. 
Perché i Token Contano 
I token sono la valuta di Claude Code. Ogni azione ha un costo in token: 
Azione 
Consumo Token Approssimativo 
Un messaggio breve dell'utente 
50-200 token 
Una risposta breve di Claude 
200-500 token 
Lettura di un file di codice medio 
1.000-5.000 token 
System prompt di Anthropic 
~10.000-20.000 token 
Un MCP leggero (Chrome Dev Tool) 
~200 token (0,1% del contesto) 
Un MCP pesante (ClickUp) 
~54.000 token (27% del contesto) 
Le skill del progetto 
~600 token (0,3% del contesto) 

--- PAGE 75 ---
Interpretazione Pratica 
Nella barra di stato di Claude Code (quella che avete configurato seguendo le istruzioni nella Parte 2 del manuale), 
vedrete due informazioni relative ai token: 
1.​
Percentuale di contesto utilizzato: ad esempio "14% used" — questo indica quanto della finestra totale è 
occupato 
2.​
Token totali disponibili: ad esempio "200K" — questo è il limite massimo 
3.​
Costo API equivalente: se usaste il piano API al posto dell'abbonamento, questo sarebbe il costo effettivo 
della chiamata 
Queste informazioni sono fondamentali per prendere decisioni in tempo reale durante il lavoro. 
Nota Importante sui Piani 
Se utilizzate il piano Pro ($17/mese) o il piano Max ($100/mese o superiore), il costo dei token è incluso 
nell'abbonamento. Il costo visualizzato nella barra di stato è puramente informativo — vi mostra quanto avreste speso 
se foste sul piano API. Tuttavia, anche con un piano in abbonamento, la gestione del contesto resta fondamentale 
perché la qualità delle risposte dipende da quanto efficientemente usate il contesto disponibile, non solo da quanto ne 
avete. 
Errori Comuni 
1.​
Pensare che "tanto ho token illimitati con l'abbonamento": l'abbonamento vi dà accesso illimitato alle 
chiamate, ma ogni singola sessione ha un limite di contesto fisso. Se lo riempite, le prestazioni degradano 
indipendentemente dal piano. 
2.​
Non distinguere tra token di input e token di output: i token che voi scrivete (input) e quelli che Claude produce 
(output) occupano entrambi spazio nel contesto. Una risposta molto lunga di Claude consuma contesto 
esattamente come un prompt lungo vostro. 
3.​
Ignorare il consumo "invisibile": prima ancora che voi scriviate il primo messaggio, una percentuale 
significativa del contesto è già occupata dal system prompt di Anthropic, dagli MCP e dalle configurazioni del 
progetto. 
Insight Avanzato 
Esiste una relazione diretta tra il numero di token nel contesto e la latenza (tempo di risposta) di Claude. Più token ci 
sono nel contesto, più tempo impiega Claude per elaborare una risposta, perché deve "leggere" e "considerare" tutto 
ciò che è presente. Questo significa che un contesto snello non solo produce risposte migliori, ma anche risposte più 
veloci. L'ottimizzazione del contesto è quindi un'ottimizzazione sia qualitativa che temporale.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
