# 28.3 — L'Esempio del Social Media Manager
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-8-il > capitolo-28]]

## Content

Definizione del Concetto 
L'autore della guida mostra il suo Social Media Manager come esempio completo di un progetto basato interamente su 
skill. Questo progetto controlla tutte le sue piattaforme social (YouTube italiano, YouTube inglese, LinkedIn e altri) 
tramite un insieme di skill coordinate. 
Struttura Reale del Progetto 

--- PAGE 139 ---
Dalla guida, la struttura del Social Media Manager dell'autore include le seguenti skill: 
text 
social-media-manager/ 
├── CLAUDE.md                    ← Conciso, essenziale 
└── .claude/ 
    ├── agents/ 
    │   ├── researcher.md 
    │   ├── reviewer.md 
    │   └── qa.md 
    ├── rules/ 
    │   └── [regole modulari] 
    └── skills/ 
        ├── linkedin-post/       ← Generatore LinkedIn post 
        │   ├── skill.md 
        │   ├── scripts/ 
        │   └── references/      ← 50+ post scritti manualmente 
        ├── publish/             ← Pubblicazione su piattaforme 
        │   ├── skill.md 
        │   └── scripts/ 
        │       ├── build_schedule.py 
        │       ├── check_meta.py 
        │       ├── check_youtube.py 
        │       └── upload_youtube.py 
        ├── audit/               ← Lancia i 3 sub-agenti automaticamente 
        │   ├── skill.md 
        │   └── scripts/ 
        ├── meta-push/           ← Pubblicazione su Meta 
        │   ├── skill.md 
        │   └── scripts/ 
        └── shorts/              ← Creazione contenuti short 
            ├── skill.md 
            └── scripts/ 
L'Interazione tra Skill e Sub-agenti 
Un dettaglio particolarmente potente emerso dalla guida è la skill Audit: 
"Quando gli chiedo 'fammi un audit', devi chiamarmi tre agenti che sono esattamente quelli che vi ho presentato." 
Questo significa che la skill Audit è un orchestratore di sub-agenti. Quando l'utente dice "fammi un audit", la skill: 
1.​
Chiama automaticamente il Researcher sub-agent 
2.​
Chiama automaticamente il Reviewer sub-agent 
3.​
Chiama automaticamente il QA sub-agent 
4.​
Raccoglie i risultati 
5.​
Produce un report consolidato 
L'utente non deve sapere che ci sono tre sub-agenti coinvolti. Dice solo "audit" e riceve un report completo. Questa è 
l'astrazione: la complessità è nascosta dietro un'interfaccia semplice. 
Il Tempo di Creazione 
L'autore condivide un dato importante sul tempo necessario per creare il suo Social Media Manager: 
"C'ho messo 2 ore e mezza a fare planning e dopo ci ha messo 3 ore a costruirlo. Era un one-shot." 
Quindi: 

--- PAGE 140 ---
●​
2,5 ore di planning mode (creazione del piano dettagliato) 
●​
3 ore di esecuzione in bypass permission (costruzione automatica) 
●​
Totale: 5,5 ore per un sistema completo di gestione social media 
Questo sistema, una volta costruito, viene usato ogni giorno per generare contenuti, pubblicarli e gestire le piattaforme. 
Il ROI è enorme: 5,5 ore di investimento per un sistema che risparmia ore ogni giorno. 
L'Interfaccia UI Personalizzata 
L'autore menziona brevemente un dettaglio avanzato: 
"Questo mio ha poi un'interfaccia UI dove se premo un tasto e non mi piace, il feedback che do va, torna dentro Claude, 
migliora pian pianino anche la generazione di post." 
Questo significa che l'autore ha costruito un'interfaccia grafica personalizzata che: 
1.​
Mostra il post generato 
2.​
Permette di dare feedback con un singolo tasto 
3.​
Il feedback viene inviato a Claude Code 
4.​
Claude migliora la skill basandosi sul feedback 
5.​
Le generazioni successive sono progressivamente migliori 
Questo è il livello esperto dell'uso delle skill: un sistema che non solo funziona, ma migliora autonomamente con l'uso.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - Formazzione|Formazzione Area]]
