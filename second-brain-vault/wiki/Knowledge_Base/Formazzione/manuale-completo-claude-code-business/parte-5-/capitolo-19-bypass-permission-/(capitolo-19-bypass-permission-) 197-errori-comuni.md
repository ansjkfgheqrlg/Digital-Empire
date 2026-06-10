# 19.7 — Errori Comuni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-5- > capitolo-19-bypass-permission-]]

## Content

Errore 1: Bypass Permission come modalità predefinita​
Alcuni utenti, dopo aver visto la velocità del Bypass Permission, lo usano per tutto. Questo è pericoloso perché non 
tutte le task meritano autonomia totale. Per task esplorative, debugging o modifiche a file critici, Ask Before Edits o 
Accept Edits sono più appropriate. 
Errore 2: Lasciare il computer incustodito per ore durante Bypass Permission​
Anche con un buon piano, Claude Code può incontrare situazioni impreviste e prendere decisioni autonome che non 
sono ottimali. Monitorare periodicamente (anche solo guardando lo schermo ogni 10-15 minuti) previene situazioni 
problematiche. 
Errore 3: Non avere checkpoint attivi​
Senza checkpoint, un'operazione distruttiva non è reversibile (almeno non facilmente). Verificare sempre che /config 
→ Rewind/Checkpoint: ON prima di usare Bypass Permission. 

--- PAGE 69 ---
Errore 4: Non definire vincoli negativi nel CLAUDE.md​
Senza vincoli espliciti su cosa NON fare, Claude Code in Bypass Permission potrebbe: 
●​
Cancellare file che considera obsoleti 
●​
Ristrutturare completamente l'architettura del progetto 
●​
Modificare configurazioni di sistema 
●​
Eliminare codice che considera ridondante 
Vincoli come "NON cancellare MAI i file nella cartella /config" o "NON modificare i file .env" sono essenziali. 
Errore 5: Avere paura irrazionale di Bypass Permission​
L'autore nota che "un po' di persone hanno diciamo paura" di questa modalità. Con le precauzioni appropriate (piano, 
checkpoint, vincoli), Bypass Permission è lo strumento più produttivo disponibile. La paura irrazionale porta a non 
usarlo mai, il che significa perdere il beneficio della produttività massima.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
