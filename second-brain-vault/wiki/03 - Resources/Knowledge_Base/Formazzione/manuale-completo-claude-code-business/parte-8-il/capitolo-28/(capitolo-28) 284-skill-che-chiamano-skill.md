# 28.4 — Skill che Chiamano Skill
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-8-il > capitolo-28]]

## Content

Definizione del Concetto 
Le skill possono essere composte — una skill può chiamare altre skill come parte del suo processo. Questo permette di 
creare catene complesse di operazioni a partire da un singolo comando. 
Spiegazione Approfondita 
Nell'esempio del Social Media Manager, la skill "publish" potrebbe internamente: 
1.​
Chiamare la skill "linkedin-post" per generare il contenuto 
2.​
Chiamare la skill "meta-push" per pubblicare su Facebook 
3.​
Chiamare la skill "shorts" per creare una versione short del contenuto 
Tutto questo da un singolo comando: "Pubblica il mio ultimo contenuto su tutte le piattaforme." 
text 
COMPOSIZIONE DI SKILL 
═════════════════════ 
 
Comando utente: "Pubblica su tutto" 
         │ 
         ▼ 
    ┌──────────┐ 
    │ publish  │ (skill principale) 
    │ skill.md │ 
    └────┬─────┘ 
         │ 
    ┌────┼────────────────┐ 
    │    │                │ 
    ▼    ▼                ▼ 
┌──────┐ ┌──────────┐ ┌────────┐ 

--- PAGE 141 ---
│linke-│ │ meta-    │ │shorts  │ 
│din-  │ │ push     │ │skill   │ 
│post  │ │ skill    │ │        │ 
│skill │ │          │ │        │ 
└──┬───┘ └────┬─────┘ └───┬────┘ 
   │          │            │ 
   ▼          ▼            ▼ 
LinkedIn   Facebook     YouTube 
  post      post        Shorts 
Ogni skill ha i suoi script, le sue verifiche e il suo self-healing. La skill principale coordina tutto, gestisce gli errori 
propagati e produce un report finale consolidato.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
