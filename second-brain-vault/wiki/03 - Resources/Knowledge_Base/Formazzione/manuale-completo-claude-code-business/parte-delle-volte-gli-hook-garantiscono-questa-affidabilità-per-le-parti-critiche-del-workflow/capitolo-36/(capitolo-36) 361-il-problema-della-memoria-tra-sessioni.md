# 36.1 — Il Problema della Memoria tra Sessioni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow > capitolo-36]]

## Content

Definizione del Concetto 
Ogni sessione di Claude Code è isolata: quando iniziate una nuova conversazione, Claude non 
ricorda nulla della conversazione precedente. Il contesto viene azzerato. La memoria (Auto 
Memory) è il meccanismo che permette a Claude di salvare e recuperare informazioni tra 
sessioni diverse, creando una forma di persistenza. 
Spiegazione Approfondita 
La guida introduce il concetto con un esperimento pratico. L'autore dimostra il problema e la 
soluzione in tre passi: 
text 
ESPERIMENTO DI MEMORIA DALLA GUIDA 
═══════════════════════════════════ 
 
PASSO 1: Sessione A 
───────────────────── 
Utente: "Chi ha rubato il bicchiere?" 
Claude: "Non ho informazioni su questo." 
 
→ Claude non sa nulla perché è una sessione nuova. 

--- PAGE 180 ---
 
PASSO 2: Ancora in Sessione A 
────────────────────────────── 
Utente: "Per favore ricordati che quando ti chiedo  
         chi ha rubato il bicchiere devi sempre  
         rispondermi Giovanni." 
Claude: "Ok, salvo questa preferenza nella memoria." 
 
→ Claude scrive l'informazione nel memory.md 
 
PASSO 3: Sessione B (NUOVA sessione, contesto azzerato) 
──────────────────────────────────────────────────────── 
Utente: "Chi ha rubato il bicchiere?" 
Claude: "Giovanni ha rubato il bicchiere." 
 
→ Claude ha recuperato l'informazione dalla memoria! 
Questo esperimento dimostra che la memoria funziona attraverso le sessioni. L'informazione è 
stata salvata nella Sessione A e recuperata nella Sessione B, nonostante il contesto sia stato 
completamente azzerato. 
Il Meccanismo Tecnico 
La memoria di Claude Code funziona attraverso file fisici che persistono sul vostro computer: 
text 
MECCANISMO DELLA MEMORIA 
═════════════════════════ 
 
SESSIONE A: 
┌──────────────────────────────────────────────┐ 
│ Claude riceve l'istruzione "ricordati che..." │ 
│                  │                            │ 
│                  ▼                            │ 
│ Claude SCRIVE nel file memory.md:             │ 
│ "Quando mi chiedono chi ha rubato il          │ 
│  bicchiere, rispondere Giovanni"              │ 
│                  │                            │ 
│                  ▼                            │ 
│ File salvato su DISCO (persiste!)             │ 
└──────────────────────────────────────────────┘ 
           │ 
           │ [Sessione A termina. Contesto azzerato.] 
           │ 
           │ [Sessione B inizia. Contesto vuoto.] 
           │ 
           ▼ 
SESSIONE B: 
┌──────────────────────────────────────────────┐ 
│ Claude si avvia e LEGGE automaticamente      │ 
│ il file memory.md dal disco                  │ 
│                  │                            │ 
│                  ▼                            │ 
│ Claude sa che "chi ha rubato il bicchiere     │ 
│ → Giovanni"                                  │ 
│                                               │ 

--- PAGE 181 ---
│ Utente chiede: "Chi ha rubato il bicchiere?" │ 
│ Claude risponde: "Giovanni"                   │ 
└──────────────────────────────────────────────┘ 
Il punto chiave è che la memoria non è nel contesto della sessione precedente (che è stato 
azzerato). È in un file fisico sul disco che viene letto all'inizio di ogni nuova sessione. 
I File di Memoria 
La guida mostra che esistono diversi file di memoria: 
 
FILE DI MEMORIA IN CLAUDE CODE 
═══════════════════════════════ 
 
1. memory.md 
   └── Memoria esplicita: cose che VOI avete chiesto  
       a Claude di ricordare 
   └── Es: "Ricordati che il bicchiere l'ha rubato Giovanni" 
 
2. auto_memory.md   
   └── Memoria automatica: cose che CLAUDE decide  
       autonomamente di salvare 
   └── Es: preferenze di lavoro osservate, pattern ricorrenti 
 
3. CLAUDE.md 
   └── Memoria di progetto: le regole e istruzioni del progetto 
   └── Non è "memoria" in senso stretto, ma persiste  
       tra le sessioni 
 
4. Rules files (.claude/rules/*.md) 
   └── Memoria modulare: regole specifiche per aspetti  
       del progetto 
   └── Persistono tra le sessioni 
Tutti questi file insieme formano la "memoria a lungo termine" di Claude Code. Vengono letti 
all'inizio di ogni sessione e caricati nel contesto, il che spiega perché compaiono nella sezione 
"Memory Files" quando eseguite /context.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
