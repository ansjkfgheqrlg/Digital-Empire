# 8.5 — Meccanismo Sottostante: La Funzione Rewind/Checkpoint
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-2-installazione-e > capitolo-8-configurazione]]

## Content

Il Rewind/Checkpoint è una funzionalità che salva automaticamente "istantanee" del progetto durante il lavoro. L'autore 
la spiega così: 
"Rewind checkpoint vuol dire che ipotizziamo che eravamo contenti con una roba che abbiamo fatto ma ci siamo fregati 
e abbiamo scritto una cosa che ha mandato a monte tutto il resto. Per tornare indietro semplicemente diciamo: 'Ehi 
torna alla versione precedente.' Se fosse OFF non potremmo farlo." 

--- PAGE 27 ---
Questa funzionalità è particolarmente importante quando si lavora in bypass permission, dove Claude Code ha la libertà 
di creare e cancellare file autonomamente. Senza checkpoint, un errore potrebbe essere irreversibile (o almeno molto 
costoso da recuperare). 
ESEMPIO DI FLUSSO CON CHECKPOINT: 
 
Checkpoint 1: Progetto funzionante ✅ 
     ↓ 
Modifica A: Aggiunta feature X → tutto ok 
     ↓ 
Checkpoint 2: Progetto con feature X ✅ 
     ↓ 
Modifica B: Tentativo feature Y → ERRORE! Progetto rotto 💥 
     ↓ 
"Ehi, torna alla versione precedente" 
     ↓ 
Ripristinato Checkpoint 2: Progetto con feature X ✅

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
