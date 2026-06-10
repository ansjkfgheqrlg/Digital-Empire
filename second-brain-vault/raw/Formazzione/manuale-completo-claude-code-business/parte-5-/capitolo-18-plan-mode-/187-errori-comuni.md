# 18.7 — Errori Comuni

Errore 1: Approvare il piano troppo velocemente​
La tentazione di premere "Approva" per passare subito all'esecuzione è forte. Ma ogni minuto speso a revisionare il 
piano risparmia potenzialmente ore di debugging e ricostruzione. L'autore è chiaro: "Questa è la parte su cui ci 
focalizziamo di più." 
Errore 2: Non dare feedback specifico durante la revisione​
Dire "non mi piace" non è feedback utile. Dire "il punto 4 non mi piace perché dovremmo usare PostgreSQL anziché 
SQLite, e il punto 5 manca di error handling" è feedback che Claude Code può utilizzare per migliorare il piano. 
Errore 3: Saltare il Plan Mode per task "semplici"​
Molte task che sembrano semplici si rivelano complesse durante l'esecuzione. L'autore raccomanda il Plan Mode per 
qualsiasi task che coinvolga più di un file o più di una funzionalità. 
Errore 4: Non fare Plan Mode prima di Bypass Permission​
Fare Bypass Permission senza un piano approvato è la ricetta per il disastro. L'autore lo raccomanda esplicitamente 
come workflow sequenziale: prima Plan Mode per creare e approvare il piano, poi Bypass Permission per eseguirlo. 
Errore 5: Confondere Plan Mode con una modalità di esecuzione lenta​
Plan Mode non è "fare le cose lentamente". È investire tempo nella direzione prima di investire tempo nell'esecuzione. Il 
tempo totale è quasi sempre inferiore rispetto all'esecuzione diretta senza piano.

