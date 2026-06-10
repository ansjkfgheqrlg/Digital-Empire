# 26.3 — Strategia di Utilizzo Pragmatica

Definizione del Concetto 
L'approccio pragmatico all'utilizzo di Agent Teams e sub-agenti si basa sul principio del ROI consapevole: ogni 
decisione di spesa deve essere giustificata da un ritorno misurabile. 
Il Framework ROI per la Decisione 
Prima di lanciare un Agent Team, fatevi queste domande: 
text 
CHECKLIST PRE-LANCIO AGENT TEAM 
═══════════════════════════════ 
 
□ 1. VALORE: Quanto vale il risultato di questa task? 
     → Se la task produce un asset che genera ricavo: PROCEDERE 
     → Se la task è esplorativa o personale: USARE SUB-AGENTI 
 
□ 2. ALTERNATIVA UMANA: Quanto costerebbe farlo manualmente? 
     → Se il team umano costerebbe 10x+ il costo dell'Agent Team: PROCEDERE 
     → Se il costo è comparabile: VALUTARE caso per caso 
 
□ 3. TEMPO: Quanto tempo risparmiamo? 
     → Se risparmiamo giorni/settimane: PROCEDERE 
     → Se risparmiamo minuti: NON GIUSTIFICATO 
 
□ 4. QUALITÀ: L'Agent Team produce risultati migliori? 
     → Se la parallelizzazione migliora la qualità: PROCEDERE 
     → Se la qualità è equivalente ai sub-agenti: USARE SUB-AGENTI 
 
□ 5. BUDGET: Posso permettermi il costo? 
     → Se €10-80 per sessione sono sostenibili: PROCEDERE 
     → Se ogni euro conta: USARE SUB-AGENTI 
Esempi di ROI dal Mondo Reale (dalla Guida) 
Esempio 1: Analisi Repository per un Cliente 
text 
Costo Agent Team:  €20 (una sessione di ~15 minuti) 
Costo alternativo: 3 developer × 2 settimane = €6.000+ 
Valore deliverable: Report completo con priorità di intervento 
ROI: Estremo (300x) 
Verdetto: USARE AGENT TEAMS ✅ 
Esempio 2: Creazione Ads per Campagna 
text 
Costo Agent Team:  €500 (sessione intensiva di 1 ora) 
Costo alternativo: Team creativo × 2 settimane = €5.000-10.000 
Valore deliverable: 50-60 ads targetizzate 
ROI: 10-20x 
Verdetto: USARE AGENT TEAMS ✅ 

--- PAGE 125 ---
Esempio 3: Rinominare file e fare piccole modifiche 
text 
Costo Agent Team:  €10 
Costo alternativo: 5 minuti di lavoro manuale = €0 
Valore deliverable: File rinominati (valore quasi nullo) 
ROI: Negativo 
Verdetto: NON USARE AGENT TEAMS ❌ (usare singolo agente) 
Il Pubblico Target per gli Agent Teams 
L'autore è molto chiaro su chi dovrebbe usare gli Agent Teams: 
●​
Business con budget per AI: aziende che hanno allocato budget per strumenti AI e possono assorbire costi di 
€100-500 per sessione 
●​
Consulenti AI che vendono servizi: il costo dell'Agent Team viene ribaltato sul cliente con markup 
●​
Progetti ad alto valore: dove il risultato dell'Agent Team vale migliaia di euro 
Chi NON dovrebbe usare gli Agent Teams: 
●​
Hobbisti e curiosi: il costo è troppo alto per l'esplorazione 
●​
Progetti personali a basso budget: i sub-agenti fanno il 90% del lavoro a una frazione del costo 
●​
Task semplici: sprecare €20 per qualcosa che un singolo agente può fare in 2 minuti 
Insight Avanzato — Il Pattern "Agent Team come MVP → Skill" 
Un pattern avanzato che emerge dalla guida è usare gli Agent Teams come strumento di prototipazione rapida per poi 
convertire il risultato in skill riutilizzabili: 
text 
PATTERN: AGENT TEAM → SKILL CONVERSION 
═══════════════════════════════════════ 
 
FASE 1: Usa un Agent Team per fare qualcosa di complesso 
        (costo: €50) 
 
FASE 2: Analizza come i teammate hanno lavorato 
 
FASE 3: Estrai i pattern e le procedure usate 
 
FASE 4: Converti queste procedure in SKILL 
 
FASE 5: D'ora in poi, usa le SKILL invece dell'Agent Team 
        (costo: ~€0.01 per chiamata) 
 
RISULTATO: Investimento una tantum → risparmio perpetuo 
Questo è simile al pattern MCP → Skill discusso nella guida: usate lo strumento costoso (Agent Team/MCP) per capire 
COME fare qualcosa, poi codificate quel "come" in una skill che costa quasi nulla da eseguire. 
 
Riepilogo della Parte 7 
In questa Parte avete appreso: 

--- PAGE 126 ---
1.​
Cosa sono i sub-agenti: istanze separate di Claude con contesto indipendente che restituiscono solo il 
risultato all'agente principale 
2.​ Come creare sub-agenti: file Markdown nella cartella .claude/agents/ con frontmatter (modello, limiti) e 
istruzioni in linguaggio naturale 
3.​
I tre sub-agenti raccomandati: 
●​
Researcher: ricerca informazioni, restituisce sintesi (100K → 2K token) 
●​
Reviewer: revisione a zero contesto, ristruttura codice e CLAUDE.md 
●​
QA: test funzionali, di regressione e di integrazione con fix automatici 
4.​
La comunicazione monodirezionale: i sub-agenti non si parlano tra loro, tutto passa attraverso l'agente 
principale 
5.​
Gli Agent Teams: team collaborativi con comunicazione bidirezionale tra tutti i teammate 
6.​
Come abilitare e usare gli Agent Teams: solo via terminal, con Team Leader che spawna teammate 
7.​
I costi reali: Agent Teams costano 3-5x più dei sub-agenti, €10-80+ per sessione 
8.​
Quando usare cosa: sub-agenti per task indipendenti, Agent Teams per task che richiedono collaborazione 
9.​
La strategia ROI: ogni decisione di utilizzo deve essere giustificata da un ritorno misurabile 
10.​ Il pattern di conversione: usare strumenti costosi (Agent Teams) per prototipare, poi convertire in skill 
economiche 
​

