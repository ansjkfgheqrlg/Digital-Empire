# 22.3 — Strategie Pratiche per l'Efficienza del Contesto
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-22]]

## Content

La Lista delle Cose da Fare e Non Fare 
La guida originale fornisce un "80/20" delle best practice per il Context Management. Espandiamo ciascuna: 
✅ COSE DA FARE: 
1. Lanciare /init quando si inizia un nuovo progetto 
Il comando /init crea automaticamente un CLAUDE.md strutturato secondo le best practice. Questo assicura che il 
contesto iniziale sia organizzato in modo efficiente. Un CLAUDE.md ben strutturato consuma meno contesto di uno 
caotico per la stessa quantità di informazioni. 
2. Mettere le regole più importanti in cima al CLAUDE.md 
Questo è legato direttamente al fenomeno del Primacy Bias che tratteremo nel Capitolo 23. Le regole posizionate 
all'inizio del CLAUDE.md vengono "ricordate" meglio dall'LLM. Esempi di regole critiche da mettere in cima: 
●​
"Non cancellare mai il file X" 
●​
"Non rimuovere le API key" 
●​
"Non modificare il database di produzione" 
●​
"Chiedi sempre conferma prima di cancellare file" 
3. Tenere sotto controllo il file CLAUDE.md e sfoltirlo regolarmente 
Il CLAUDE.md tende a crescere nel tempo man mano che aggiungete regole e istruzioni. Periodicamente: 
●​
Rimuovete regole che non sono più rilevanti 
●​
Consolidate regole simili 
●​
Spostate regole specifiche nelle sotto-cartelle (rules/) 
●​
Verificate che non ci siano ripetizioni 
4. Spezzare il CLAUDE.md in regole modulari 
Come spiegato nelle Parti precedenti del manuale, invece di avere un unico CLAUDE.md monolitico, è molto più 
efficiente spezzare le regole in file separati nella cartella .claude/rules/: 
 
Prima (inefficiente): 
CLAUDE.md → un unico file enorme che viene caricato per intero 
 
Dopo (efficiente): 
CLAUDE.md → piccolo, solo regole essenziali 
.claude/rules/design-fidelity.md → regole di design 
.claude/rules/security.md → regole di sicurezza 
.claude/rules/screenshot-workflow.md → regole per gli screenshot 
Il vantaggio è che Claude carica solo le regole rilevanti per la task corrente, non tutte le regole di tutti gli aspetti del 
progetto. 

--- PAGE 91 ---
5. Inserire errori ricorrenti direttamente nel CLAUDE.md 
Quando Claude continua a fare lo stesso errore nonostante le vostre correzioni, la soluzione è codificarlo nel 
CLAUDE.md: 
"Se Claude te lo fa due-tre volte, inseriscilo nel CLAUDE.md. Lo fai hard code dentro e hai risolto i tuoi problemi." 
Questo trasforma un problema ricorrente (che consuma contesto ogni volta che dovete correggerlo) in una regola 
permanente (che previene il problema alla fonte). 
6. Raccogliere regolarmente le best practice aggiornate 
L'autore della guida condivide la sua strategia personale per rimanere aggiornato: 
●​
Va su X (Twitter) 
●​
Segue Boris (il fondatore di Claude Code) e altri power user 
●​
Usa Grok per sintetizzare le novità: "Per favore raccoglimi tutto quello che è successo nell'ultimo mese in 
termini di best practice di Claude e riassumile così che io possa inglobarle dentro al mio progetto" 
●​
Incorpora le nuove best practice nel proprio CLAUDE.md 
❌ COSE DA NON FARE: 
1. Non buttate dentro guide inutili o documentazioni API 
"Le API sono legate al vostro conto in banca." 
Caricare documentazioni API complete, guide di terze parti o blocchi enormi di testo nel contesto è uno spreco 
catastrofico. Questi documenti possono consumare decine di migliaia di token senza fornire valore proporzionale. Se 
avete bisogno di informazioni da una documentazione, chiedete a Claude di cercarle specificamente (usando il Dev 
Tool MCP o un sub-agente researcher) invece di caricare tutto il documento. 
2. Non scrivete regole vaghe o aspirazionali 
Regole come: 
●​
❌ "Non fare errori" — è inutile e vaga 
●​
❌ "Fammi diventare ricco" — non è un'istruzione operativa 
●​
❌ "Scrivi codice perfetto" — non definisce cosa significhi "perfetto" 
Regole efficaci sono: 
●​
✅ "Quando modifichi un file, crea sempre un backup prima" 
●​
✅ "Ogni funzione deve avere una documentazione inline" 
●​
✅ "Dopo ogni modifica CSS, fai uno screenshot e confronta con il design di riferimento" 
Le regole vaghe non solo non aiutano Claude, ma consumano contesto senza produrre valore. 
3. Non sprecate contesto con il ciclo di verifica umano quando potete automatizzarlo 
Il pattern inefficiente è: 
Utente: "Fai X" 
Claude: [fa X] 
Utente: "Hai fatto bene?" 
Claude: "Sì" 
Utente: "Sei sicuro?" 

--- PAGE 92 ---
Claude: "Sì, sono sicuro" 
Ogni messaggio "Hai fatto bene?" e "Sei sicuro?" è uno spreco di contesto. Invece, codificate la verifica nel 
CLAUDE.md: "Dopo ogni modifica, verifica automaticamente il risultato confrontandolo con il riferimento. Se ci sono 
differenze, correggi e ripeti."​
​
​
​
​
​
​
​
​

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
