# 7.6 — Approfondimento: La Status Line
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-2-installazione-e > capitolo-7-il-terminal-come]]

## Content

La Status Line è la barra informativa che appare nella parte inferiore del Terminal quando Claude Code è attivo. 
L'autore la considera essenziale e mostra come attivarla. 
Come attivare la Status Line: 
Metodo 1: Comando diretto​
Nel prompt di Claude Code, digitare il comando specifico per la status line (disponibile nella configurazione) e premere 
Enter. 
Metodo 2: Chiedere a Claude Code​
Se non riuscite a configurarla manualmente, l'autore suggerisce un approccio pragmatico e potente: fare uno 
screenshot della Status Line come appare nel video/tutorial, incollarlo nel Terminal, e chiedere a Claude: "Ehi, per 
favore fa sì che io abbia sotto al terminal queste cose qui." Claude Code configurerà tutto automaticamente. 
Questa è una perla filosofica dell'autore: "D'ora in poi la vostra vita sarà sempre alla distanza di un buon prompt da 
risolvere gran parte dei vostri problemi." 
Cosa mostra la Status Line: 
┌────────────────────────────────────────────────────────────────┐ 
│ 📊 14% used │ 💰 $0.03 │ 🔢 28,000/200,000 tokens │ ⏱ 5m 32s   
└────────────────────────────────────────────────────────────────┘ 
 
📊 Contesto utilizzato (%) 
   → La metrica più importante da monitorare 
   → Quando si avvicina al 100%, le performance degradano 
   → L'autocompact interviene automaticamente prima del 100% 
 
💰 Costo stimato (API pricing) 
   → Quanto costerebbe l'interazione nel piano API 
   → Solo informativo per utenti con piano subscription 
   → Utile per capire il "peso" di ogni operazione 
 
🔢 Token utilizzati / Token totali 
   → Quanti token sono stati consumati nella sessione 
   → Il totale dipende dal modello (es. 200K per alcuni, 1M per altri) 
 
⏱ Durata sessione 
   → Da quanto tempo la sessione è attiva 
   → Utile per gestire il tempo e pianificare i compact

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
