# 23.1 — Introduzione ai Bias Cognitivi degli LLM
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-23]]

## Content

Definizione del Concetto 
I bias cognitivi degli LLM sono pattern sistematici nel modo in cui i modelli di linguaggio processano e "ricordano" le 
informazioni all'interno del contesto. Esattamente come gli esseri umani hanno bias cognitivi che influenzano la 
memoria e il giudizio, anche gli LLM presentano pattern prevedibili che dobbiamo conoscere e sfruttare. 
Spiegazione Approfondita 
La guida originale introduce tre concetti fondamentali che rappresentano il cuore del Context Management avanzato: 
1.​
Primacy Bias (Bias di Primato): il modello ricorda molto bene le informazioni posizionate all'inizio del contesto 
2.​
Recency Bias (Bias di Recenza): il modello ricorda molto bene le informazioni posizionate alla fine del 
contesto 
3.​
Lost in the Middle (Perso nel Mezzo): il modello ha difficoltà significative a ricordare e utilizzare le informazioni 
posizionate nel mezzo del contesto 
Questi tre fenomeni insieme creano una curva di "attenzione" del modello che ha una forma caratteristica a U: 
Performance / Capacità di Ricordo 
        │ 
   Alta ┤ ████                              ████ 
        │ ████████                      ████████ 

--- PAGE 93 ---
        │ ████████████            ████████████ 
        │ ████████████████  ████████████████ 
  Bassa ┤ ████████████████████████████████████ 
        │ 
        └────────────────────────────────────── 
          INIZIO       MEZZO          FINE 
                del contesto 
           
          ◄─────►                   ◄─────► 
          Primacy                   Recency 
           Bias                     Bias 
           
                    ◄───────► 
                   Lost in the 
                     Middle

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
