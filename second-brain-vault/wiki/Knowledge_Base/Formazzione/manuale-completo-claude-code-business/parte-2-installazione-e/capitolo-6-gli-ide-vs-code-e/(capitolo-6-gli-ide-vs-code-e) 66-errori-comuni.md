# 6.6 — Errori Comuni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-2-installazione-e > capitolo-6-gli-ide-vs-code-e]]

## Content

Errore 1: Non accettare le modifiche proposte da Claude Code​
Quando Claude Code propone una modifica a un file, questa viene mostrata come una "diff" (differenza tra la versione 
originale e quella proposta). Se salvate il file senza accettare esplicitamente le modifiche, il file viene duplicato anziché 
modificato. L'autore ha mostrato questo accidentalmente durante il corso: "Se poi io ora lo salvassi senza accettare 
questi cambiamenti, vedete che me l'ha semplicemente duplicato." 
La regola è: sempre accettare o rifiutare esplicitamente le modifiche proposte prima di procedere. 
Errore 2: Non configurare il Dangerously Skip Permission​
La modalità bypass permission (che verrà approfondita nel Capitolo 19) non è attiva di default. Per abilitarla: 
In VS Code: 
1.​
Premere l'icona ingranaggio (⚙️) 
2.​
Selezionare "Settings" 
3.​
Cercare "Claude" 

--- PAGE 20 ---
4.​
Abilitare "Allow Dangerously Skip Permission" 
In Antigravity: 
1.​
Premere la rotellina/ingranaggio in alto a destra (posizione diversa da VS Code) 
2.​
Selezionare "Settings" 
3.​
Cercare "Claude Code" 
4.​
Abilitare "Dangerously Skip Permission" 
Nota: la posizione dell'ingranaggio è diversa nei due IDE. In VS Code è nella barra laterale, in Antigravity è in alto a 
destra. 
Errore 3: Confondere le modalità di interazione​
In entrambi gli IDE, Claude Code offre diverse modalità nella parte superiore del pannello: 
Modalità 
Comportamento 
Ask before edits 
Claude propone le modifiche e chiede approvazione prima di applicarle 
Edit automatically 
Claude applica le modifiche automaticamente (tranne creazione/cancellazione file) 
Plan mode 
Claude crea un piano strutturato e chiede approvazione prima di eseguirlo 
Bypass permission 
Claude fa tutto in autonomia: crea, modifica, cancella file senza chiedere 
La confusione tra queste modalità è molto comune e può portare a risultati inattesi (Claude che modifica file senza il 
vostro consenso, o al contrario Claude che si ferma continuamente a chiedere permessi rallentando il workflow).

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
