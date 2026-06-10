# 34.4 — Il Pattern Strategico Completo per gli MCP
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-9-mcp > capitolo-34]]

## Content

Riepilogo della Strategia Ottimale 
Combinando tutti i concetti appresi in questa Parte, ecco la strategia completa per la gestione degli MCP: 
 
STRATEGIA COMPLETA DI GESTIONE MCP 
═══════════════════════════════════ 
 
LIVELLO BASE (per tutti): 
───────────────────────── 
✅ Installate Chrome Dev Tool MCP → tenetelo SEMPRE 
✅ Non installate nient'altro a meno che non serva 
✅ Consumo contesto base: ~0,1% 
 
QUANDO SERVE UN SERVIZIO ESTERNO: 
───────────────────────────────── 
1. Installate l'MCP del servizio 
2. Verificate il consumo con /context 
3. Usate l'MCP per capire COME funziona il servizio 
4. Identificate le 2-3 funzionalità che vi servono 
5. Chiedete a Claude di creare skill per quelle funzionalità 
6. Testate le skill indipendentemente 
7. Rimuovete l'MCP 
8. Verificate con /context che il contesto sia libero 
 
ECCEZIONI (mantenete l'MCP): 
──────────────────────────── 
• MCP con consumo < 1% del contesto 
• MCP che usate quotidianamente con molte funzionalità 
• MCP in fase di esplorazione attiva 
 
MAI: 
──── 
• Non installate più di 2-3 MCP contemporaneamente 
• Non lasciate MCP installati che non state usando 
• Non ignorate l'impatto sul contesto 
• Non assumete che "più MCP = migliore" 

--- PAGE 168 ---
 
Riepilogo della Parte 9 
In questa Parte avete appreso: 
1.​
Cos'è un MCP: un protocollo che collega servizi esterni a Claude Code, come una "chiavetta USB universale" 
che eredita tutte le funzionalità del servizio 
2.​
Le tipologie di MCP: leggeri vs pesanti, built-in vs terze parti, always-on vs on-demand 
3.​
Il formato JSON di configurazione: struttura con key-value che definisce come Claude comunica con il servizio 
4.​
Come installare un MCP: tramite prompt, tramite Dev Tool MCP o tramite comando specifico 
5.​
L'impatto devastante degli MCP pesanti sul contesto: ClickUp occupa il 27% del contesto, 270 volte più del 
Chrome Dev Tool 
6.​
La strategia MCP → Skill Conversion: usare l'MCP per prototipare, poi convertire in skill e rimuovere l'MCP 
7.​
Il collegamento con il Lost in the Middle: gli MCP pesanti spingono le vostre informazioni nella zona cieca del 
contesto 
8.​
Il Chrome Dev Tool MCP: l'unico MCP raccomandato, con 0,1% di consumo e funzionalità universali 
9.​
La regola del 5%: se un MCP occupa più del 5% del contesto, valutate la conversione in skill 
10.​ La strategia completa: Chrome Dev Tool sempre, tutto il resto temporaneo e convertito in skill 
​

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
