# parte delle volte". Gli hook garantiscono questa affidabilità per le parti critiche del workflow.
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-delle-volte-gli-hook-garantiscono-questa-affidabilità-per-le-parti-critiche-del-workflow]]

## Content

Errori Comuni con gli Hooks 
1.​ Non usare hook quando servirebbero: molti utenti chiedono a Claude di "ricordarsi" di 
fare qualcosa alla fine di una task. Questo consuma contesto e non è garantito. Un hook 
lo farebbe gratuitamente e con certezza. 

--- PAGE 179 ---
2.​ Creare hook troppo complessi: un hook dovrebbe fare UNA cosa. Se avete bisogno di un 
workflow complesso, create più hook in sequenza o usate un hook che avvia uno script 
multi-step. 
3.​ Non testare gli hook: dopo aver creato un hook, testatelo sempre con un prompt 
semplice per verificare che si attivi correttamente. 
4.​ Dimenticare che gli hook sono globali se messi nei settings globali: un hook di test 
messo nei settings globali si attiverà in TUTTI i vostri progetti. Assicuratevi che sia 
intenzionale.

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
