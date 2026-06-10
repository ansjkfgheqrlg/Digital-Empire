# 28.2 — Il Processo di Creazione Passo per Passo
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-8-il > capitolo-28]]

## Content

Definizione del Concetto 
La creazione di una skill personalizzata è un processo in quattro fasi: definire, strutturare, codificare e testare. Non è 
necessario essere programmatori per iniziare — Claude Code può assistere in ogni fase. 
Fase 1: Definire la Skill 
Il primo passo è definire chiaramente cosa deve fare la skill. Questo significa rispondere a tre domande: 
1.​
COSA: Quale risultato deve produrre? 
2.​
COME: Quali passi deve seguire per arrivarci? 
3.​
QUANDO: In quali circostanze viene chiamata? 
Esempio (LinkedIn Post Generator): 
text 
COSA: Generare un post LinkedIn nel mio stile personale 
COME:  
  1. Ricevere un topic o un'idea dall'utente 
  2. Analizzare i reference post per estrarre stile e tono 
  3. Generare una bozza del post 
  4. Formattare secondo le convenzioni personali 
  5. Aggiungere CTA appropriata 
  6. Presentare il risultato per approvazione 
QUANDO: Ogni volta che voglio creare un nuovo post LinkedIn 
Fase 2: Strutturare la Skill 
Questa fase consiste nel creare la struttura della cartella e del file skill.md: 
text 
STRUTTURA DA CREARE 
═══════════════════ 
 
.claude/skills/ 
└── linkedin-post/ 
    ├── skill.md          ← La checklist/orchestratore 
    ├── scripts/          ← Gli script eseguibili 
    │   └── generate.py 
    └── references/       ← I dati di riferimento 
        └── my_posts.md   ← Post precedenti come esempio 

--- PAGE 137 ---
Il file skill.md dovrebbe seguire questa struttura: 
Markdown 
# LinkedIn Post Generator 
 
Generate a LinkedIn post matching your writing style. 
 
## Input Validation 
- Topic or idea: REQUIRED 
- Target audience: OPTIONAL (default: entrepreneurs) 
- Post style: OPTIONAL (default: storytelling) 
- Include CTA: OPTIONAL (default: yes) 
 
## Process 
1. Read reference posts from references/my_posts.md 
2. Analyze writing patterns: 
   - Sentence length 
   - Emoji usage 
   - Line spacing 
   - Hook structure 
   - CTA format 
3. Generate draft post 
4. Format according to patterns 
5. Add appropriate CTA 
6. Present to user 
 
## Output Format 
- Present the post in a code block 
- Show character count 
- Indicate target platform format compliance 
 
## Error Handling 
- If reference file not found → warn user, generate generic 
- If topic too vague → ask for clarification 
- If post exceeds LinkedIn character limit → offer to shorten 
 
## Self-Healing 
- If output doesn't match reference style → re-analyze  
  references and regenerate 
- If CTA is missing → add default CTA 
- Log any corrections for future improvement 
Fase 3: Codificare gli Script 
Gli script trasformano la parte ripetitiva e deterministica del processo in codice eseguibile. Per il LinkedIn Post 
Generator, lo script potrebbe gestire: 
●​
Lettura e parsing dei file di riferimento 
●​
Analisi statistica del tono (lunghezza frasi, frequenza emoji, etc.) 
●​
Formattazione del post secondo regole predefinite 
●​
Conteggio caratteri e validazione limiti piattaforma 
L'aspetto fondamentale è che non dovete necessariamente scrivere questi script voi stessi. Potete chiedere a Claude: 
text 
"Per favore, guarda la skill.md che ho creato nella  
cartella linkedin-post e crea gli script necessari  
per implementare il processo descritto. Segui le  
best practice della documentazione ufficiale Claude." 
Claude creerà gli script basandosi sulla checklist nel skill.md. 
Fase 4: Testare e Iterare 

--- PAGE 138 ---
Una volta creata la skill, testatela con diversi input: 
text 
Test 1: "Usa la skill LinkedIn Post per creare un  
        post sull'importanza delle skill in Claude Code" 
 
Test 2: "Usa la skill LinkedIn Post per creare un  
        post su come l'AI sta cambiando il business" 
 
Test 3: "Usa la skill LinkedIn Post per creare un  
        post controverso sull'overuse degli Agent Teams" 
Per ogni test, valutate: 
●​
Il risultato rispecchia il vostro stile? Se no, migliorate i reference data 
●​
Il processo ha avuto errori? Se sì, migliorate la checklist 
●​
Il formato è corretto? Se no, aggiornate le regole di formattazione 
●​
Il self-healing ha funzionato? Se no, migliorate la sezione Error Handling 
Il Prompt Completo per Chiedere a Claude di Creare una Skill 
Basandosi sull'approccio mostrato nella guida, ecco un template di prompt efficace: 
text 
"Per favore, crea una skill completa per [DESCRIZIONE]. 
 
La skill deve: 
1. Essere posizionata in .claude/skills/[NOME]/ 
2. Avere un file skill.md con checklist completa 
3. Avere una cartella scripts/ con gli script necessari 
4. Seguire le best practice della documentazione ufficiale Claude 
5. Includere gestione errori e self-healing 
6. Includere validazione degli input 
 
Per il file skill.md, segui la struttura: 
- Descrizione 
- Input Validation 
- Process (step by step) 
- Output Format 
- Error Handling 
- Self-Healing 
 
Per gli script, usa Python e assicurati che siano  
deterministici e ben documentati. 
 
Se hai bisogno di reference data, chiedimi e te li fornirò."

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - Prove|Prove Area]]
