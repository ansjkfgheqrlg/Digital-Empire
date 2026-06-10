# 17.7 — Errori Comuni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-5- > capitolo-17-le-quattro-modalità]]

## Content

Errore 1: Restare sempre in Ask Before Edits​
Molti utenti non escono mai dalla modalità default per paura di perdere il controllo. Questo rallenta enormemente il 
workflow. Una volta che avete familiarità con Claude Code e avete un buon piano, passare ad Accept Edits o Bypass 
Permission è una scelta di produttività essenziale. 
Errore 2: Andare direttamente in Bypass Permission senza piano​
Questo è l'estremo opposto ed è molto pericoloso. L'autore racconta il caso di una persona che: "ha cancellato 
completamente qualsiasi cosa all'interno del suo computer. Aveva dato un piano povero, aveva fatto bypass permission, 
e quello che è successo è che il computer ha continuato a fare ricerca per qualche ora finché poi non ha deciso che la 
soluzione migliore per risolvere il problema era cancellare tutto quanto." 
Errore 3: Non capire la propagazione ai sotto-agenti​
Se date bypass permission all'agente principale, ogni sotto-agente chiamato eredita la stessa autonomia. Questo è 
particolarmente rischioso con sotto-agenti che fanno operazioni distruttive (es. pulizia codice, ristrutturazione file). 
Errore 4: Cambiare modalità nel mezzo di un'operazione critica​
Passare da Plan Mode a Bypass Permission mentre Claude sta ancora pianificando può creare confusione. Completate 
la fase corrente prima di cambiare modalità. 
Errore 5: Non abilitare Bypass Permission nelle impostazioni e non capire perché non appare​
La modalità Bypass Permission non è visibile di default. Deve essere esplicitamente abilitata nelle impostazioni dell'IDE. 
Molti utenti cercano questa opzione senza trovarla perché non hanno modificato le impostazioni.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
