# 5.7 — Insight Avanzato
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-2-installazione-e > capitolo-5-installazione-di]]

## Content

Quando interagite con Claude Code nel Terminal, noterete diversi elementi visivi: 
Indicatori di pensiero: Quando Claude sta elaborando una risposta, vedrete parole come "harmonizing", "thinking", 
"cogitating", "looping", "noodling". Queste sono etichette casuali (e personalizzabili) che indicano semplicemente che il 
modello sta processando la richiesta. Non hanno significato specifico — servono solo a comunicare "sto pensando, 
attendi". 
Distinzione input/output: Il vostro input (ciò che scrivete) è preceduto da un rettangolino/indicatore visivo. La risposta di 
Claude non ha questo indicatore. Questo vi permette di distinguere immediatamente chi ha scritto cosa nella 
conversazione. 

--- PAGE 16 ---
Informazioni di sessione nella barra inferiore (Status Line): 
┌─────────────────────────────────────────────────────┐ 
│ Context: 14% used │ Cost: $0.03 │ Tokens: 28K/200K │ Session: 5m │ 
└─────────────────────────────────────────────────────┘ 
●​
Context % used: La percentuale di contesto totale utilizzata. Questa è una delle metriche più importanti da 
monitorare (approfondita nel Capitolo 20-22) 
●​
Cost: Il costo stimato dell'interazione se si fosse sul piano API. Per chi usa un piano subscription, è solo 
informativo 
●​
Tokens: Il totale di token utilizzati rispetto al massimo disponibile 
●​
Session duration: Da quanto tempo è attiva la sessione corrente 
Nota importante dell'autore: Il numero di token totali e il contesto utilizzato non sono la stessa cosa. La ragione sarà 
spiegata nei capitoli dedicati al context management, ma per ora è sufficiente sapere che sono due metriche correlate 
ma distinte.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
