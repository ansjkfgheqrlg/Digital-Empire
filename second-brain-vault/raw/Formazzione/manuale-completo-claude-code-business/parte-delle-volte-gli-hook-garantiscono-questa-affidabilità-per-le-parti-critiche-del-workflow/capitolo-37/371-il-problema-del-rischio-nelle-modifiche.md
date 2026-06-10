# 37.1 — Il Problema del Rischio nelle Modifiche

Definizione del Concetto 
Quando lavorate su un progetto con Claude Code, ogni modifica al codice è potenzialmente 
irreversibile se non avete un sistema di version control. Il version control (controllo delle versioni) 
è il sistema che vi permette di salvare "istantanee" del vostro codice nel tempo, così da poter 
tornare a una versione precedente se qualcosa va storto. 
Spiegazione Approfondita 
L'autore introduce il concetto con un esempio pratico: 
"Fino ad ora noi abbiamo sempre operato in tutti i progetti in un solo folder. Se qualcosa andava 
storto, non avevamo mai la possibilità di salvare la versione precedente. O meglio, Claude Code 
lo fa in automatico, ma non siamo mai stati consapevoli e non l'abbiamo mai fatto 
volontariamente." 
Il rischio è reale. L'autore racconta un caso specifico: 
"È successo che una persona, un paio di mesi fa, abbia cancellato completamente qualsiasi 
cosa all'interno del suo computer. Aveva dato un piano povero, aveva fatto bypass permission, e 
quello che è successo è che il computer ha continuato a fare ricerca per qualche ora finché poi 
non ha deciso che la soluzione migliore per risolvere il problema era cancellare tutto quanto." 
Questo caso estremo illustra perché il version control non è un "nice to have" — è una necessità 
assoluta. 
Cos'è GitHub 
La guida introduce GitHub come la piattaforma di version control: 

--- PAGE 185 ---
"GitHub è una piattaforma che permette di fare la cosiddetta version control, quindi il controllo 
delle versioni di un determinato codice, che in parole povere è semplicemente un posto nel quale 
possiamo mettere il nostro codice e avere ogni versione che abbiamo committato. Se noi 
sbagliamo il codice una volta e il nostro progetto si distrugge, possiamo andare a prendere una 
versione precedente e ripristinare il codice." 
Pensate a GitHub come un Time Machine per il codice: potete viaggiare indietro nel tempo e 
recuperare qualsiasi versione precedente del vostro progetto. 
 
VERSION CONTROL COME TIME MACHINE 
═════════════════════════════════ 
 
SENZA VERSION CONTROL: 
Versione 1 → Versione 2 → Versione 3 → BUG! → 😱 
                                         │ 
                                         └── Non potete tornare indietro. 
                                             Tutto è perso. 
 
CON VERSION CONTROL (GitHub): 
Versione 1 → Versione 2 → Versione 3 → BUG! → 😊 
    💾           💾           💾           │ 
    Salvata      Salvata      Salvata      └── Tornate alla Versione 2. 
                                               Problema risolto.

