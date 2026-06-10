# 20.4 — La Relazione tra Contesto e Prestazioni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-6-context > capitolo-20]]

## Content

Definizione del Concetto 
Esiste una relazione inversamente proporzionale tra la quantità di contesto occupato e la qualità delle prestazioni di 
Claude. Questa relazione non è lineare: le prestazioni non degradano in modo uniforme, ma seguono un pattern 
specifico legato ai bias cognitivi del modello. 
Spiegazione Approfondita 
La guida originale introduce un grafico concettuale che possiamo rappresentare così: 
 
Qualità delle Prestazioni 
        │ 
   100% ┤ ████ 
        │ ████████ 
    75% ┤ ████████████ 
        │ ████████████████ 
    50% ┤ ████████████████████ 
        │ ████████████████████████ 
    25% ┤ ████████████████████████████ 
        │ ████████████████████████████████ 
     0% ┤───────────────────────────────────── 
        0%   20%   40%   60%   80%   100% 
                 Contesto Utilizzato 
Le prestazioni diminuiscono man mano che il contesto si riempie, e la diminuzione accelera nella seconda metà. 
Questo significa che: 
●​
Da 0% a 30% di contesto: prestazioni eccellenti 
●​
Da 30% a 60% di contesto: prestazioni buone, leggero calo 
●​
Da 60% a 80% di contesto: prestazioni in calo visibile 
●​
Da 80% a 100% di contesto: prestazioni significativamente degradate 
Implicazione Pratica Diretta 
Quando nella guida l'autore vede che il contesto è al 66%, dice immediatamente a Claude: "Sei al 66% del contesto, 
cosa che significa che comincerai a perdermi a livello di performance." E chiede di salvare le informazioni importanti in 
memoria per poter iniziare una nuova sessione pulita. 
Questa è la strategia corretta: non aspettare che il contesto sia al 90% per reagire. Già al 60-70% è il momento di: 

--- PAGE 80 ---
1.​ Compattare il contesto (/compact) 
2.​
Salvare informazioni critiche nella memoria 
3.​
Considerare di iniziare una nuova sessione 
4.​
Fornire a Claude un prompt di continuazione per la sessione successiva 
Perché le Prestazioni Degradano 
Le prestazioni degradano per diverse ragioni tecniche che è utile comprendere almeno a livello intuitivo: 
1.​
Dispersione dell'attenzione: il modello deve distribuire la sua "attenzione computazionale" su tutti i token 
presenti. Più token ci sono, meno attenzione viene data a ciascuno. 
2.​
Conflitto di istruzioni: con più contesto, aumenta la probabilità che ci siano istruzioni contraddittorie o ambigue, 
causando incertezza nel modello. 
3.​
Allucinazioni: quando il contesto è saturo, il modello è più propenso a "inventare" informazioni anziché 
ammettere di non sapere, perché ha troppi pattern tra cui scegliere. 
4.​
Perdita di focus: le istruzioni iniziali (il CLAUDE.md, le regole) vengono "diluite" dalla massa di conversazione 
successiva.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
