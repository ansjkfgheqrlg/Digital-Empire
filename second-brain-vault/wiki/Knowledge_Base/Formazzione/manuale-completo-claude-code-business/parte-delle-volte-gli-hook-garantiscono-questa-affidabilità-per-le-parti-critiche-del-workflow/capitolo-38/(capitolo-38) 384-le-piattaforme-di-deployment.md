# 38.4 — Le Piattaforme di Deployment
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow > capitolo-38]]

## Content

Definizione del Concetto 
Esistono diverse piattaforme su cui potete fare deployment dei vostri progetti. La guida menziona 
specificamente Modal, Vercel e GitHub Actions come le tre opzioni principali. 
Confronto delle Piattaforme 
Piattaforma 
Ideale Per 
Caratteristiche Chiave 
Modal 
Cloud functions, skill, API, 
workflow 
Serverless, pay-per-use, deployment di script Python 
Vercel 
Frontend, siti web, web app 
Ottimo per Next.js, deploy automatico da GitHub, hosting 
web 
GitHub 
Actions 
CI/CD, automazioni, test 
Esegue workflow automatici su push/merge, gratuito per 
repo pubbliche 
Quando Usare Quale 
 
ALBERO DECISIONALE PER LA PIATTAFORMA 
═════════════════════════════════════ 
 
Cosa state deployando? 

--- PAGE 196 ---
│ 
├── Una SKILL o un'API → MODAL 
│   └── Es: LinkedIn Post Generator come servizio 
│   └── Es: Scraper come servizio 
│   └── Es: Qualsiasi workflow backend 
│ 
├── Un SITO WEB o una WEB APP → VERCEL 
│   └── Es: Il sito aziendale 
│   └── Es: L'app Trello clone con frontend 
│   └── Es: Landing page con pagamento integrato 
│ 
└── Un'AUTOMAZIONE che parte a evento → GITHUB ACTIONS 
    └── Es: Test automatici quando il codice cambia 
    └── Es: Deploy automatico quando fate merge 
    └── Es: Report automatici giornalieri 
Modal nel Dettaglio 
L'autore mostra familiarità specifica con Modal e ne illustra i vantaggi: 
1.​ Serverless: non dovete gestire server. Il codice gira solo quando viene chiamato e 
pagate solo per il tempo di esecuzione. 
2.​ Facilità di deployment: un singolo prompt a Claude Code è sufficiente per fare 
deployment di una skill su Modal. 
3.​ URL pubblico automatico: Modal genera automaticamente un URL accessibile a 
chiunque. 
4.​ Dashboard di monitoraggio: potete vedere ogni chiamata, il tempo di esecuzione e i log. 
5.​ Costi contenuti: per la maggior parte dei casi d'uso, i costi sono nell'ordine di centesimi 
per chiamata. 
Vercel nel Dettaglio 
L'autore menziona Vercel come piattaforma per il deployment del suo sito web: 
"Andiamo a Vercel, che è anche il posto in cui alcune di queste cose verranno pubblicate." 
Vercel è ideale quando avete: 
●​
Un frontend web (React, Next.js, etc.) 
●​
Bisogno di un hosting continuo (non solo a chiamata) 
●​
Integrazione con GitHub per deploy automatici 
L'autore ha il suo sito ("Gentes") deployato su Vercel, e quando fa merge di una worktree, il 
deploy su Vercel è automatico.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
