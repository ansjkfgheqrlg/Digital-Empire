# 23.5 — Strategia Integrata di Context Management

Definizione del Concetto 
La Strategia Integrata di Context Management è l'applicazione combinata di tutti i principi discussi in questa Parte del 
manuale per massimizzare l'efficienza e la qualità del lavoro con Claude Code. 
Il Framework Completo 
Combinando tutti i concetti appresi, ecco il framework completo per la gestione del contesto: 
FRAMEWORK DI CONTEXT MANAGEMENT 
════════════════════════════════ 
 
FASE 1: PRIMA DI INIZIARE 
───────────────────────── 
□ Verificare gli MCP installati → rimuovere quelli non necessari 
□ Verificare che il CLAUDE.md sia conciso e ben strutturato 
□ Verificare che le regole siano spezzate in file modulari 
□ Eseguire /context per vedere lo stato iniziale 
□ Obiettivo: tenere il contesto pre-occupato sotto il 20% 
 
FASE 2: STRUTTURA DEL CLAUDE.MD 
──────────────────────────────── 
□ Regole critiche (sicurezza, vincoli) → INIZIO 
□ Dettagli operativi → MEZZO 
□ Standard di qualità e formato → FINE 
□ Tutto il resto → file modulari in .claude/rules/ 
 
FASE 3: DURANTE IL LAVORO 
───────────────────────── 
□ Scrivere prompt concisi ad alta densità informativa 
□ Monitorare il contesto con /context ogni 15-20 messaggi 
□ Compattare con /compact quando si supera il 60% 
□ Ripetere istruzioni importanti prima dei comandi critici 
□ Non caricare documenti enormi → usare sub-agenti 
 
FASE 4: GESTIONE DELLE TRANSIZIONI 
─────────────────────────────────── 
□ Al 65-70% di contesto → salvare in memoria 
□ Chiedere a Claude il prompt di continuazione 
□ Iniziare nuova sessione con contesto fresco 
□ Nella nuova sessione: "Continua con [task]" 
 
FASE 5: OTTIMIZZAZIONE CONTINUA 
──────────────────────────────── 
□ Errori ricorrenti → codificarli nel CLAUDE.md 
□ MCP pesanti usati una volta → convertire in skill 
□ Regole obsolete → rimuovere dal CLAUDE.md 
□ Raccogliere nuove best practice mensilmente 
Riepilogo delle Metriche Chiave 

--- PAGE 98 ---
Metrica 
Soglia Verde 
Soglia Gialla 
Soglia Rossa 
Contesto pre-occupato 
< 20% 
20-35% 
> 35% 
Contesto durante il lavoro 
< 50% 
50-70% 
> 70% 
Skill nel contesto 
< 1% 
1-3% 
> 3% 
MCP nel contesto 
< 5% 
5-15% 
> 15% 
Messaggi nel contesto 
< 40% 
40-60% 
> 60% 
Il Principio Fondamentale 
Se dovessimo riassumere l'intero Context Management in una singola frase, sarebbe questa: 
Ogni token nel contesto deve guadagnarsi il suo posto. Se un'informazione non contribuisce direttamente alla qualità 
del risultato, non dovrebbe essere nel contesto. 
Questo principio guida ogni decisione: cosa installare, cosa scrivere nel CLAUDE.md, come strutturare i prompt, 
quando compattare, quando iniziare una nuova sessione. È il metro con cui misurare ogni azione che impatta il 
contesto. 
 
Riepilogo della Parte 6 
In questa Parte avete appreso: 
1.​
Cosa sono i token e come funzionano come unità di misura del contesto 
2.​
Come è composto il contesto in Claude Code (system prompt, tools, MCP, memoria, skill, messaggi, buffer) 
3.​ Come monitorare il contesto con /context, /config e la Status Line 

--- PAGE 99 ---
4.​ Come funziona l'Autocompact e come usare /compact manualmente 
5.​
Il concetto di densità informativa e come scrivere prompt efficienti 
6.​
Il Primacy Bias e perché le regole importanti vanno all'inizio 
7.​
Il Recency Bias e come sfruttare la posizione finale per istruzioni critiche 
8.​
Il Lost in the Middle e perché le informazioni nel mezzo del contesto vengono "dimenticate" 
9.​
La strategia integrata che combina tutti questi principi in un framework operativo 
Questa conoscenza è la base su cui si costruisce l'uso professionale di Claude Code. Senza Context Management, 
state usando Claude Code come un chatbot. Con il Context Management, lo state usando come uno strumento di 
produttività professionale.

