# 27.1 — Cosa Sono le Skill
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-8-il > capitolo-27]]

## Content

Definizione del Concetto 
Una skill in Claude Code è un processo codificato e ripetibile che insegna a Claude come eseguire una task specifica 
seguendo una procedura predefinita. Potete pensare a una skill come a una ricetta dettagliata che uno chef (Claude) 
segue per preparare un piatto specifico ogni volta con lo stesso livello di qualità. 
Spiegazione Approfondita 
L'analogia della ricetta, introdotta nella guida originale, è illuminante: 

--- PAGE 128 ---
"Claude possiamo vederlo come uno chef a cui diamo un sacco di ricette. Una ricetta serve per cucinare la pasta, una 
per la pizza, una per fare un buon caffè. E gli diciamo quali sono gli ingredienti, quali sono gli strumenti che deve usare 
e tutte quelle cose lì." 
Questa analogia cattura perfettamente l'essenza delle skill. Senza skill, Claude è uno chef talentuoso ma senza ricette: 
può cucinare qualcosa, ma il risultato varierà ogni volta e dipenderà dalla vostra capacità di descrivere cosa volete. Con 
le skill, Claude è uno chef con un ricettario completo: sa esattamente cosa fare, in quale ordine e con quali ingredienti. 
Dove Vivono le Skill 
Le skill possono esistere a diversi livelli dell'architettura Claude Code, esattamente come le regole e i sub-agenti: 
text 
LIVELLI DI POSIZIONAMENTO DELLE SKILL 
══════════════════════════════════════ 
 
LIVELLO LOCAL (dentro il progetto corrente): 
progetto/ 
└── .claude/ 
    └── skills/ 
        ├── linkedin-post/ 
        │   ├── skill.md 
        │   └── scripts/ 
        │       └── generate_post.py 
        ├── publish/ 
        │   ├── skill.md 
        │   └── scripts/ 
        │       ├── build_schedule.py 
        │       ├── check_meta.py 
        │       ├── check_youtube.py 
        │       └── upload_youtube.py 
        └── audit/ 
            ├── skill.md 
            └── scripts/ 
                └── run_audit.py 
 
LIVELLO GLOBAL (disponibile per tutti i progetti): 
~/.claude/ 
└── skills/ 
    ├── [stesse strutture di sopra] 
    └── [accessibili da qualsiasi progetto] 
 
LIVELLO LEGACY: 
[Formato precedente, meno strutturato,  
 che la guida menziona ma non approfondisce] 
La scelta di dove posizionare una skill dipende dal suo ambito di utilizzo: 
Posizione 
Quando usarla 
Esempio 
Local 
Skill specifica per un progetto 
Skill di deploy per un'app specifica 

--- PAGE 129 ---
Global 
Skill riutilizzabile in tutti i progetti 
Skill di generazione LinkedIn post 
L'Impatto delle Skill sul Contesto 
Un dato fondamentale emerso dalla guida è l'efficienza delle skill in termini di consumo di contesto: 
text 
CONFRONTO CONSUMO CONTESTO 
═══════════════════════════ 
 
Skill del progetto:        ~0,3% del contesto 
MCP leggero (Dev Tool):    ~0,1% del contesto 
MCP pesante (ClickUp):     ~27% del contesto 
System Prompt (Anthropic):  ~10% del contesto 
 
CONCLUSIONE: Le skill sono 90 volte più efficienti  
di un MCP pesante per fornire funzionalità a Claude. 
Questo dato da solo giustifica l'investimento nella creazione di skill personalizzate: sono il modo più efficiente per dare 
capacità a Claude senza saturare il contesto.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
