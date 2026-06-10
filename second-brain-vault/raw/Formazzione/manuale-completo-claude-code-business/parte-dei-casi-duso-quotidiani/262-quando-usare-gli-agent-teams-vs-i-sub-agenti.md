# 26.2 — Quando Usare gli Agent Teams vs i Sub-agenti

Definizione del Concetto 
La scelta tra Agent Teams e sub-agenti non è una questione di "quale è migliore" ma di quale è appropriato per la task 
specifica, considerando il rapporto costo-beneficio. 
Framework Decisionale Completo 
text 
ALBERO DECISIONALE: AGENT TEAMS vs SUB-AGENTI 
══════════════════════════════════════════════ 
 
La task richiede COLLABORAZIONE tra agenti? 
│ 
├── NO → Usa SUB-AGENTI 
│   │ 
│   ├── Task indipendenti (ricerca, review, test) 
│   ├── Risultato di un agente non dipende dagli altri 
│   └── Costo: BASSO 
│ 
└── SÌ → La task genera un ROI significativo? 
    │ 
    ├── NO → Usa SUB-AGENTI in sequenza 
    │   │ 
    │   ├── Fai prima il Researcher 
    │   ├── Poi il Reviewer 
    │   ├── Poi il QA 
    │   └── Comunica i risultati manualmente 
    │ 
    └── SÌ → Usa AGENT TEAMS 
        │ 
        ├── Analisi complesse multi-dimensionali 
        ├── Creazione massiva di contenuti 
        ├── Task che richiedono coordinamento 
        └── Budget disponibile per il costo 
Tabella Comparativa Dettagliata 
Caratteristica 
Sub-agenti 
Agent Teams 
Comunicazione 
Mono-direzionale (→ principale) 
Bidirezionale (tutti ↔ tutti) 
Costo 
Basso (1x) 
Alto (3-5x) 
Velocità 
Veloce per task singole 
Velocissimo per task parallele 

--- PAGE 123 ---
Coordinamento 
Manuale (tramite utente) 
Automatico (tramite Team Leader) 
Context overhead 
Minimo 
Significativo 
Ideale per 
Task indipendenti e specializzate 
Task complesse che richiedono collaborazione 
Disponibilità 
GUI e Terminal 
Solo Terminal 
Rischio di costo 
Basso e prevedibile 
Alto e potenzialmente imprevedibile 
Esempi ideali 
Ricerca, review, test 
Analisi repository, creazione ads, audit 
Gli Use Case Ideali per Ciascuno 
Sub-agenti — Use Case Ideali: 
1.​
Ricerca di best practice (Researcher) 
2.​
Revisione del codice dopo una fase di sviluppo (Reviewer) 
3.​
Test e quality assurance (QA) 
4.​
Qualsiasi task che un singolo specialista può fare indipendentemente 
Agent Teams — Use Case Ideali: 
1.​
Analisi completa di repository grandi (multi-prospettiva) 
2.​
Creazione massiva di contenuti con variazioni (ads, post, email) 
3.​
Refactoring completo di un'applicazione (serve coordinamento tra frontend, backend, test) 
4.​
Audit aziendale completo (sicurezza + codice + architettura + documentazione) 
5.​
Qualsiasi task che in un'azienda richiederebbe un team di persone che si parlano 
La Regola Pratica 
Se la task può essere fatta da una singola persona competente → Sub-agente​
Se la task richiede un team di persone che collaborano → Agent Team 
 

--- PAGE 124 ---

