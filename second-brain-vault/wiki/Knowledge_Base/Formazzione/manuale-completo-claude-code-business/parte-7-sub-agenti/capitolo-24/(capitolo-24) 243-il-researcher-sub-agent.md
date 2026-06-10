# 24.3 — Il Researcher Sub-agent
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-7-sub-agenti > capitolo-24]]

## Content

Definizione del Concetto 

--- PAGE 106 ---
Il Researcher è un sub-agente specializzato nella ricerca di informazioni, best practice, documentazione e dati online. Il 
suo scopo è raccogliere grandi quantità di informazioni, processarle e restituire all'agente principale solo un riassunto 
sintetico e azionabile. 
Spiegazione Approfondita 
Il Researcher è il primo dei tre sub-agenti raccomandati dall'autore della guida, e il suo funzionamento illustra 
perfettamente il vantaggio dei sub-agenti per il context management. 
Il Problema che il Researcher Risolve: 
Quando chiedete a Claude di fare una ricerca (ad esempio: "Cerca le best practice per costruire un sito internet con 
Next.js"), il processo di ricerca genera una quantità enorme di dati: 
●​
Pagine web visitate e scrappate 
●​
Documentazione tecnica letta 
●​
Articoli analizzati 
●​
Codice di esempio trovato 
●​
Discussioni su forum consultate 
Tutto questo materiale può facilmente raggiungere i 100.000 token. Se questa ricerca avviene nel contesto principale, 
avete bruciato metà del vostro contesto solo per la fase di ricerca, prima ancora di iniziare a costruire qualcosa. 
Come il Researcher Risolve il Problema: 
 
FLUSSO DEL RESEARCHER SUB-AGENT 
════════════════════════════════ 
 
AGENTE PRINCIPALE                    RESEARCHER SUB-AGENT 
      │                                      │ 
      │  "Cerca le best practice             │ 
      │   per costruire un sito              │ 
      │   con Next.js"                       │ 
      │ ─────────────────────────────────►   │ 
      │                                      │ 
      │                              ┌───────┴───────┐ 
      │                              │ Naviga il web  │ 
      │                              │ Legge docs     │ 
      │                              │ Analizza codice│ 
      │                              │ Processa       │ 
      │                              │ 100K token     │ 
      │                              │ di materiale   │ 
      │                              └───────┬───────┘ 
      │                                      │ 
      │                              ┌───────┴───────┐ 
      │                              │ Sintetizza     │ 
      │                              │ tutto in un    │ 
      │                              │ riassunto di   │ 
      │                              │ 2K token       │ 
      │                              └───────┬───────┘ 
      │                                      │ 
      │  ◄───────────────────────────────────│ 
      │  Risultato: 2K token                 │ 
      │  "Le 10 best practice principali     │ 
      │   sono: 1) ... 2) ... 3) ..."        │ 
      │                                      │ 
      │  [Il contesto del Researcher         │ 
      │   viene distrutto]                   │ 
      │                                      │ 
Il risultato netto è che nel contesto principale entrano solo 2.000 token di risultato altamente raffinato, invece di 100.000 
token di materiale grezzo. Questo è un miglioramento del 98% nell'efficienza del contesto. 

--- PAGE 107 ---
Applicazione Pratica — Quando Usare il Researcher 
Scenario 
Usare il Researcher? 
Motivo 
Cercare best practice per un framework 
✅ Sì 
Produce molti dati da sintetizzare 
Analizzare documentazione di una libreria 
✅ Sì 
Documentazioni sono tipicamente enormi 
Confrontare diverse soluzioni tecniche 
✅ Sì 
Richiede lettura di multiple fonti 
Chiedere un parere su un errore specifico 
❌ No 
Task troppo piccola, non serve delegare 
Fare un semplice calcolo 
❌ No 
Non c'è ricerca da fare 
Esplorare un topic nuovo per il progetto 
✅ Sì 
Esplorazione = molti dati in input 
L'Esempio Pratico dalla Guida 
L'autore della guida fornisce un esempio concreto: prima di costruire un sito internet, invece di chiedere all'agente 
principale di cercare le best practice (inquinando il contesto), fa questa sequenza: 
1.​
Chiama il Researcher sub-agent: "Cerca le best practice per costruire un sito internet" 
2.​
Il Researcher fa la ricerca nel suo contesto separato 
3.​
Torna con un riassunto sintetico delle best practice 
4.​
L'agente principale usa queste best practice per costruire il sito 
Questo approccio produce risultati superiori perché: 
●​
Il contesto principale resta pulito per il lavoro di costruzione 
●​
Le best practice sono già sintetizzate e pronte all'uso 
●​
Non c'è rischio di "polluting the context" (inquinamento del contesto) 

--- PAGE 108 ---
Insight Avanzato — Il Concetto di "Polluting the Context" 
La guida introduce il termine "polluting the context" (inquinare il contesto) per descrivere ciò che accade quando si 
caricano nel contesto principale informazioni che non sono direttamente rilevanti per la task corrente. Ogni informazione 
irrilevante: 
●​
Occupa spazio prezioso 
●​
Aumenta il rischio di "Lost in the Middle" 
●​
Può confondere il modello durante il ragionamento 
●​
Degrada la qualità complessiva delle risposte 
Il Researcher sub-agent è la soluzione primaria a questo problema: tutta la "sporcizia" della ricerca resta nel suo 
contesto (che viene poi distrutto), e solo il "distillato" puro entra nel contesto principale.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
