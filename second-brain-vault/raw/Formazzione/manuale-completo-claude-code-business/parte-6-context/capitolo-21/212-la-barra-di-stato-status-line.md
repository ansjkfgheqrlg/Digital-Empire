# 21.2 — La Barra di Stato (Status Line)

Definizione del Concetto 

--- PAGE 82 ---
La Status Line è una barra informativa posizionata nella parte inferiore del terminal di Claude Code che mostra in tempo 
reale informazioni chiave sulla sessione corrente: percentuale di contesto utilizzato, costo equivalente API, token totali 
disponibili e durata della sessione. 
Spiegazione Approfondita 
La Status Line mostra le seguenti informazioni: 
Elemento 
Significato 
Esempio 
% used 
Percentuale del contesto utilizzata 
14% used 
Cost 
Costo equivalente se si usasse il piano API 
$0.03 
Token totali 
Dimensione totale della finestra di contesto 
200K 
Durata sessione 
Da quanto tempo è attiva la sessione 
5m 
Come Configurare la Status Line 
Per ottenere la Status Line, esistono due metodi: 
Metodo 1 — Comando diretto: 
 
/status line 
Premete Enter e la barra verrà configurata automaticamente. 
Metodo 2 — Prompt a Claude Code:​
Nel caso in cui il Metodo 1 non funzionasse, l'autore della guida suggerisce un approccio ingegnoso: 
1.​
Fate uno screenshot della barra di stato che volete replicare (ad esempio dalla guida o da un video) 
2.​
Incollatelo nel terminal 
3.​
Dite a Claude: "Per favore fai sì che io abbia sotto al terminal queste cose qui" 
4.​
Claude configurerà automaticamente la Status Line 

--- PAGE 83 ---
Questa è un'applicazione pratica di un principio fondamentale: la vostra vita con Claude Code sarà sempre alla distanza 
di un buon prompt dal risolvere i vostri problemi. 
Interpretazione Pratica 
La Status Line è il vostro indicatore di carburante durante la guida. Non è precisa come il comando /context (che è il 
vostro cruscotto diagnostico completo), ma è sempre visibile e vi dà un'indicazione rapida di dove siete. 
Abitudini corrette con la Status Line: 
●​
Guardarla dopo ogni scambio significativo con Claude 
●​
Preoccuparvi quando supera il 50-60%: è il momento di iniziare a pensare alla gestione del contesto 
●​
Non ignorarla mai quando supera il 70%: a questo punto le azioni di gestione del contesto diventano urgenti 
La Discrepanza tra Percentuale e Token 
La guida originale nota che la percentuale mostrata nella Status Line e il numero di token "non sono uguali". Questo 
avviene perché: 
●​
La percentuale è calcolata sul contesto totale disponibile 
●​
Il numero di token potrebbe riferirsi al totale di token processati (input + output cumulativi), che può superare il 
contesto disponibile grazie alla compattazione 
●​
La durata della sessione influenza questa discrepanza perché la compattazione ridistribuisce i token 
La regola pratica è: fidatevi della percentuale per le decisioni operative. Se dice 60%, agite di conseguenza, 
indipendentemente dal numero assoluto di token mostrato.

