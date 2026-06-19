# K07-skill-system
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Agente Max > knowledge]]

## Content

# MODULO KNOWLEDGE BASE

**K07-skill-system.md** — Capitoli 27-30 | Architettura skill, creare skill, marketplace, qualità dati riferimento

## Riferimenti Correlati
- K06-sub-agenti.md (skill vs agent teams: confronto ROI)
- K08-mcp.md (MCP vs skill: scegliere cosa usare)

---

**PARTE 8 — IL SISTEMA DELLE SKILL**  
---

*"Le skill di Cloud sono la funzione più sottovalutata del momento. Chi le usa è 10x più veloce di chi non le conosce."*  
*— Dalla guida originale (esempio di LinkedIn Post generato dal sistema)*

---

## **Introduzione alla Parte 8**

Se i sub-agenti e gli Agent Teams rappresentano la vostra capacità di delegare e parallelizzare, le skill rappresentano la vostra capacità di codificare l'eccellenza in processi ripetibili. Una skill ben costruita trasforma un processo che richiederebbe 20 minuti di prompt, riflessione e iterazione in un singolo comando che produce risultati consistenti ogni volta.

Questa è probabilmente la Parte più direttamente collegata alla monetizzazione di Claude Code. Le skill sono ciò che vi permette di creare asset riutilizzabili, vendibili e scalabili. Un'agenzia di social media che costruisce le proprie skill ha un vantaggio competitivo enorme rispetto a chi usa Claude Code come un chatbot avanzato.

Questa Parte è composta da quattro capitoli:

| Capitolo | Titolo | Focus Principale |
| ----- | ----- | ----- |
| 27 | Architettura delle Skill | Come sono strutturate internamente |
| 28 | Creare Skill Personalizzate | Il processo completo di creazione |
| 29 | Il Marketplace delle Skill | Dove trovare e importare skill esterne |
| 30 | La Qualità dei Dati di Riferimento | Perché il reference data è tutto |

---

# **CAPITOLO 27**

## **Architettura delle Skill**

---

### **27.1 — Cosa Sono le Skill**

#### **Definizione del Concetto**

Una skill in Claude Code è un processo codificato e ripetibile che insegna a Claude come eseguire una task specifica seguendo una procedura predefinita. Potete pensare a una skill come a una ricetta dettagliata che uno chef (Claude) segue per preparare un piatto specifico ogni volta con lo stesso livello di qualità.

#### **Spiegazione Approfondita**

L'analogia della ricetta, introdotta nella guida originale, è illuminante:

*"Claude possiamo vederlo come uno chef a cui diamo un sacco di ricette. Una ricetta serve per cucinare la pasta, una per la pizza, una per fare un buon caffè. E gli diciamo quali sono gli ingredienti, quali sono gli strumenti che deve usare e tutte quelle cose lì."*

Questa analogia cattura perfettamente l'essenza delle skill. Senza skill, Claude è uno chef talentuoso ma senza ricette: può cucinare qualcosa, ma il risultato varierà ogni volta e dipenderà dalla vostra capacità di descrivere cosa volete. Con le skill, Claude è uno chef con un ricettario completo: sa esattamente cosa fare, in quale ordine e con quali ingredienti.

#### **Dove Vivono le Skill**

Le skill possono esistere a diversi livelli dell'architettura Claude Code, esattamente come le regole e i sub-agenti:

text

LIVELLI DI POSIZIONAMENTO DELLE SKILL  
══════════════════════════════════════

LIVELLO LOCAL (dentro il progetto corrente):  
progetto/  
└── .claude/  
    └── skills/  
        ├── linkedin-post/  
        │   ├── skill.md  
        │   └── scripts/  
        │       └── generate\_post.py  
        ├── publish/  
        │   ├── skill.md  
        │   └── scripts/  
        │       ├── build\_schedule.py  
        │       ├── check\_meta.py  
        │       ├── check\_youtube.py  
        │       └── upload\_youtube.py  
        └── audit/  
            ├── skill.md  
            └── scripts/  
                └── run\_audit.py

LIVELLO GLOBAL (disponibile per tutti i progetti):  
\~/.claude/  
└── skills/  
    ├── \[stesse strutture di sopra\]  
    └── \[accessibili da qualsiasi progetto\]

LIVELLO LEGACY:  
\[Formato precedente, meno strutturato, 

 che la guida menziona ma non approfondisce\]

La scelta di dove posizionare una skill dipende dal suo ambito di utilizzo:

| Posizione | Quando usarla | Esempio |
| ----- | ----- | ----- |
| Local | Skill specifica per un progetto | Skill di deploy per un'app specifica |
| Global | Skill riutilizzabile in tutti i progetti | Skill di generazione LinkedIn post |

#### **L'Impatto delle Skill sul Contesto**

Un dato fondamentale emerso dalla guida è l'efficienza delle skill in termini di consumo di contesto:

text

CONFRONTO CONSUMO CONTESTO  
═══════════════════════════

Skill del progetto:        \~0,3% del contesto  
MCP leggero (Dev Tool):    \~0,1% del contesto  
MCP pesante (ClickUp):     \~27% del contesto  
System Prompt (Anthropic):  \~10% del contesto

CONCLUSIONE: Le skill sono 90 volte più efficienti 

di un MCP pesante per fornire funzionalità a Claude.

Questo dato da solo giustifica l'investimento nella creazione di skill personalizzate: sono il modo più efficiente per dare capacità a Claude senza saturare il contesto.

---

### **27.2 — La Struttura Interna di una Skill**

#### **Definizione del Concetto**

Ogni skill è composta da due componenti fondamentali contenuti in una cartella dedicata:

1. Il file skill.md — l'orchestratore (la checklist)  
2. La cartella scripts/ — il codice eseguibile

Questi due componenti lavorano insieme ma hanno ruoli molto diversi.

#### **Spiegazione Approfondita — Il File skill.md (L'Orchestratore)**

L'autore della guida usa una metafora potente per spiegare il ruolo del file skill.md:

*"Dovete pensare a questa skill.md come un orchestrator. Immaginatevi un'orchestra: c'è il direttore d'orchestra — il tizio con le bacchette — e poi ci sono quelli che suonano l'orchestra."*

text

ANATOMIA DEL FILE SKILL.MD  
═══════════════════════════

┌─────────────────────────────────────────────────────┐  
│                    SKILL.MD                          │  
│              (Il Direttore d'Orchestra)              │  
│                                                      │  
│  ┌───────────────────────────────────────────────┐  │  
│  │ DESCRIZIONE DELLA SKILL                       │  │  
│  │ "Pubblica Real Short Video e posta su          │  │  
│  │  YouTube, Instagram o Facebook in maniera      │  │  
│  │  automatica"                                   │  │  
│  └───────────────────────────────────────────────┘  │  
│                                                      │  
│  ┌───────────────────────────────────────────────┐  │  
│  │ PIATTAFORME E STRUMENTI                       │  │  
│  │ • YouTube: Python API                         │  │  
│  │ • Instagram: tramite Chrome Dev Tool MCP      │  │  
│  │ • Facebook: tramite Chrome Dev Tool MCP       │  │  
│  └───────────────────────────────────────────────┘  │  
│                                                      │  
│  ┌───────────────────────────────────────────────┐  │  
│  │ CHECKLIST DI VALIDAZIONE INPUT                │  │  
│  │ □ Gather input: which platform?               │  │  
│  │ □ Gather input: which content?                │  │  
│  │ □ If valid → procedi                          │  │  
│  │ □ If invalid → richiedi correzione            │  │  
│  └───────────────────────────────────────────────┘  │  
│                                                      │  
│  ┌───────────────────────────────────────────────┐  │  
│  │ SEQUENZA DI ESECUZIONE                        │  │  
│  │ 1\. Chiama build\_schedule.py                   │  │  
│  │ 2\. Chiama check\_meta.py                       │  │  
│  │ 3\. Chiama check\_youtube.py                    │  │  
│  │ 4\. Chiama upload\_youtube.py                   │  │  
│  └───────────────────────────────────────────────┘  │  
│                                                      │  
│  ┌───────────────────────────────────────────────┐  │  
│  │ GESTIONE ERRORI                               │  │  
│  │ • Se uno step fallisce → log errore           │  │  
│  │ • Tenta auto-correzione                       │  │  
│  │ • Se non risolvibile → notifica utente        │  │  
│  └───────────────────────────────────────────────┘  │  
│                                                      │

└─────────────────────────────────────────────────────┘

Il file skill.md è essenzialmente la mappa di navigazione della skill. Dice a Claude:

* Che cosa deve fare questa skill  
* Quali input raccogliere dall'utente  
* Come validare gli input  
* In quale ordine eseguire le operazioni  
* Quali script chiamare  
* Come gestire gli errori

#### **La Cartella scripts/ (I Musicisti dell'Orchestra)**

Se il file skill.md è il direttore d'orchestra, gli script sono i musicisti. Sono loro che effettivamente "suonano" — eseguono il codice reale che compie le operazioni.

text

ANATOMIA DELLA CARTELLA SCRIPTS/  
════════════════════════════════

scripts/  
├── build\_schedule.py  
│   └── Costruisce la mappatura di quando pubblicare  
│       Input: preferenze utente (giorno, ora, piattaforma)  
│       Output: schedule strutturato  
│  
├── check\_meta.py  
│   └── Verifica se su Meta (Facebook/Instagram)   
│       c'è già un post programmato  
│       Input: schedule, credenziali Meta  
│       Output: stato (libero/occupato)  
│  
├── check\_youtube.py  
│   └── Verifica lo stato del canale YouTube  
│       Input: credenziali YouTube API  
│       Output: stato canale, video recenti  
│  
└── upload\_youtube.py  
    └── Carica il video su YouTube  
        Input: file video, titolo, descrizione, tag

        Output: URL del video pubblicato

Gli script sono codice deterministico — non sono prompt LLM. Sono programmi Python (o altro linguaggio) che eseguono operazioni specifiche e prevedibili. Questo è un punto cruciale che vedremo in dettaglio.

#### **La Relazione tra skill.md e scripts/**

La guida originale chiarisce un malinteso molto comune:

*"Molte persone fanno una skill.md dicendo che è semplicemente un markdown, ma questo è un po' forviante."*

La skill non è il file markdown. La skill è l'insieme di skill.md \+ scripts/. Il markdown è il direttore d'orchestra, ma senza i musicisti (gli script) non c'è concerto.

text

INTERAZIONE TRA SKILL.MD E SCRIPTS  
═══════════════════════════════════

    L'utente dice: "Pubblica il mio video su YouTube"  
                │  
                ▼  
    ┌──────────────────────────┐  
    │      SKILL.MD            │  
    │   (Direttore)            │  
    │                          │  
    │   "OK, devo:             │  
    │    1\. Validare l'input   │  
    │    2\. Chiamare gli       │  
    │       script giusti      │  
    │    3\. Verificare i       │  
    │       risultati"         │  
    └────────────┬─────────────┘  
                 │  
    ┌────────────┼────────────────────┐  
    │            │                    │  
    ▼            ▼                    ▼  
┌─────────┐ ┌─────────────┐ ┌──────────────┐  
│ build\_  │ │ check\_      │ │ upload\_      │  
│schedule │ │ youtube     │ │ youtube      │  
│  .py    │ │  .py        │ │  .py         │  
│         │ │             │ │              │  
│ \[CODICE\]│ │ \[CODICE\]    │ │ \[CODICE\]     │  
│ \[DETER- │ │ \[DETER-     │ │ \[DETER-      │  
│ MINISTI-│ │ MINISTICO\]  │ │ MINISTICO\]   │  
│ CO\]     │ │             │ │              │  
└────┬────┘ └──────┬──────┘ └──────┬───────┘  
     │             │               │  
     └─────────────┼───────────────┘  
                   │  
                   ▼  
    ┌──────────────────────────┐  
    │      SKILL.MD            │  
    │   (Verifica risultati)   │  
    │                          │  
    │   "Tutto OK? → Report    │  
    │    Errore? → Self-heal"  │

    └──────────────────────────┘

---

### **27.3 — Il Processo di Self-Healing**

#### **Definizione del Concetto**

Il self-healing (auto-guarigione) è il processo attraverso il quale una skill è in grado di auto-correggersi quando qualcosa va storto durante l'esecuzione. Questo processo è reso possibile dalla combinazione del file skill.md (che contiene le istruzioni per la gestione degli errori) e del CLAUDE.md (che contiene le regole generali del progetto).

#### **Spiegazione Approfondita**

Quando uno script all'interno di una skill fallisce o produce un risultato non conforme, il processo di self-healing si attiva:

text

PROCESSO DI SELF-HEALING  
════════════════════════

ESECUZIONE NORMALE:  
    skill.md → script\_1.py → script\_2.py → script\_3.py → OUTPUT ✅  
                                                            
QUANDO QUALCOSA VA STORTO:  
    skill.md → script\_1.py → script\_2.py ← ERRORE\! ❌  
                                │  
                                ▼  
                    ┌───────────────────────┐  
                    │ SELF-HEALING ATTIVATO │  
                    │                       │  
                    │ 1\. Claude legge il    │  
                    │    CLAUDE.md per      │  
                    │    capire cosa fare   │  
                    │                       │  
                    │ 2\. Identifica         │  
                    │    l'errore           │  
                    │                       │  
                    │ 3\. Applica la         │  
                    │    correzione         │  
                    │                       │  
                    │ 4\. Aggiorna la        │  
                    │    skill.md           │  
                    │    (la checklist)     │  
                    │                       │  
                    │ 5\. Ri-esegue lo      │  
                    │    script corretto    │  
                    └───────────┬───────────┘  
                                │  
                                ▼

                    script\_2.py (corretto) → script\_3.py → OUTPUT ✅

L'aspetto più importante del self-healing è il Passo 4: Claude aggiorna la checklist (skill.md) per includere la correzione. Questo significa che la prossima volta che la skill viene eseguita, l'errore non si ripresenterà perché la checklist è stata migliorata.

Questo crea un ciclo virtuoso di miglioramento continuo:

text

CICLO DI MIGLIORAMENTO DELLA SKILL  
═══════════════════════════════════

    Esecuzione 1 → Errore A → Fix A → Skill aggiornata  
                                          │  
    Esecuzione 2 → Errore B → Fix B → Skill aggiornata  
                                          │  
    Esecuzione 3 → Nessun errore → Output perfetto  
                                          │  
    Esecuzione 4 → Nessun errore → Output perfetto  
                                          │

    ...la skill diventa sempre più robusta nel tempo

#### **Perché il Self-Healing è Fondamentale**

Senza self-healing, ogni errore richiederebbe l'intervento umano. Con il self-healing:

1. Riduzione dell'intervento umano: la skill si ripara da sola nella maggior parte dei casi  
2. Miglioramento continuo: ogni errore rende la skill più robusta  
3. Scalabilità: potete lanciare skill e andare a fare altro, sapendo che si auto-correggeranno  
4. Documentazione automatica: le correzioni vengono codificate nella checklist, creando documentazione vivente

#### **Il Ruolo del CLAUDE.md nel Self-Healing**

*"Quand'è che il file skill.md entra in funzione? Quando qualcosa va storto. Molti confondono perché molti dicono 'La skill è il file markdown' — la skill non è il file markdown."*

Il CLAUDE.md fornisce il contesto generale che Claude usa per capire come reagire agli errori. La skill.md fornisce la procedura specifica per la skill corrente. Insieme, danno a Claude abbastanza informazioni per:

* Diagnosticare cosa è andato storto  
* Decidere la strategia di correzione  
* Applicare il fix  
* Verificare che il fix funzioni  
* Aggiornare la documentazione per prevenire recidive

---

### **27.4 — Skill vs Script: La Natura Deterministica**

#### **Definizione del Concetto**

Gli script all'interno di una skill sono deterministici — producono sempre lo stesso output dato lo stesso input. Questo è in contrasto con le risposte dell'LLM, che sono non deterministiche (possono variare anche con lo stesso prompt). Comprendere questa distinzione è fondamentale per costruire skill affidabili.

#### **Spiegazione Approfondita**

La guida originale introduce questo concetto quando parla degli hook e lo rafforza parlando delle skill:

*"Questi hook possono essere anche il momento in cui attiviamo un sub-workflow. Sono distaccati dal funzionamento dell'LLM. Non sono più legati alla token consumption. Partono ad evento e sono codice, quindi non sono qualcosa di non deterministico."*

Lo stesso principio si applica agli script delle skill. Quando Claude esegue uno script Python per caricare un video su YouTube, quel codice:

* Non "interpreta" cosa fare — segue istruzioni precise  
* Non "allucinà" — esegue operazioni definite  
* Non "varia" il risultato — dato lo stesso input, produce lo stesso output  
* Non consuma token dell'LLM — è codice tradizionale

Questo è il motivo per cui le skill sono così potenti: combinano la flessibilità dell'LLM (per capire cosa l'utente vuole e orchestrare il processo) con la affidabilità del codice tradizionale (per eseguire le operazioni effettive).

text

CONFRONTO: APPROCCIO LLM-ONLY vs SKILL  
═══════════════════════════════════════

APPROCCIO LLM-ONLY (senza skill):  
┌────────────────────────────────────────────┐  
│ Utente: "Pubblica questo video su YouTube" │  
│                                            │  
│ Claude LLM:                                │  
│ → Interpreta la richiesta (non determin.)  │  
│ → Cerca di capire come fare (non determin.)│  
│ → Prova a scrivere codice (non determin.)  │  
│ → Esegue il codice (deterministico)        │  
│ → Verifica il risultato (non determin.)    │  
│                                            │  
│ Risultato: VARIABILE ogni volta            │  
│ Token consumati: MOLTI                     │  
│ Tempo: LUNGO                               │  
└────────────────────────────────────────────┘

APPROCCIO CON SKILL:  
┌────────────────────────────────────────────┐  
│ Utente: "Usa la skill publish per YouTube" │  
│                                            │  
│ Claude \+ Skill:                            │  
│ → Legge skill.md (checklist fissa)         │  
│ → Valida gli input (checklist fissa)       │  
│ → Esegue upload\_youtube.py (determin.)     │  
│ → Verifica il risultato (checklist fissa)  │  
│                                            │  
│ Risultato: CONSISTENTE ogni volta          │  
│ Token consumati: POCHI                     │  
│ Tempo: BREVE                               │

└────────────────────────────────────────────┘

#### **L'Implicazione per la Costruzione di Skill**

Questa comprensione della dualità LLM/codice ha implicazioni dirette per come costruite le vostre skill:

* Tutto ciò che può essere codificato come script, DEVE essere codificato come script: upload di file, chiamate API, trasformazioni di dati, manipolazione di file — tutto questo deve essere codice deterministico  
* Solo ciò che richiede ragionamento resta nell'LLM: interpretazione dell'input utente, decisioni creative, gestione degli errori imprevisti, personalizzazione del tono di voce  
* La skill.md fa da ponte: coordina quando usare l'LLM e quando usare gli script

---

# **CAPITOLO 28**

## **Creare Skill Personalizzate**

---

### **28.1 — Perché Creare Skill Personalizzate**

#### **Definizione del Concetto**

Le skill personalizzate sono skill create da voi specificamente per i vostri processi, il vostro stile e le vostre esigenze. Sono l'opposto delle skill generiche importate da marketplace. L'autore della guida è categorico: le skill personalizzate sono la cosa a maggiore ROI che potete fare con Claude Code.

#### **Spiegazione Approfondita**

L'autore dimostra la differenza tra skill personalizzate e generiche con un esperimento diretto: genera un LinkedIn Post con la sua skill personalizzata e con una skill importata dal marketplace, usando lo stesso identico input.

Risultato con skill personalizzata:

* Post con la sua formattazione specifica  
* Emoji posizionate secondo il suo stile  
* Call to action personalizzata per il suo business  
* Tono di voce che rispecchia la sua personalità  
* Struttura di skimmability (leggibilità rapida) coerente con i suoi post precedenti  
* Riferimenti alla sua community e ai suoi programmi

Risultato con skill importata:

* Post generico con M-dashes ("—") tipici dell'AI  
* Struttura standard senza personalità  
* Nessun riferimento al brand personale  
* Tono "robotico" immediatamente riconoscibile come AI  
* Formattazione diversa da qualsiasi post precedente dell'autore

*"Stesso input, output estremamente diverso."*

La differenza non sta nella qualità del codice o nella struttura della skill. La differenza sta nel reference data — i dati di riferimento che alimentano la skill. Ma di questo parleremo in dettaglio nel Capitolo 30\.

#### **Il Processo Mentale per Identificare Skill da Creare**

Prima di costruire una skill, dovete identificare quali processi nel vostro lavoro sono:

text

CHECKLIST PER IDENTIFICARE SKILL UTILI  
═══════════════════════════════════════

□ RIPETITIVO: Faccio questa cosa più di 1 volta a settimana?  
  → SÌ: Candidata ideale per una skill

□ STRUTTURATO: Il processo segue sempre gli stessi passi?  
  → SÌ: Facile da codificare in una checklist

□ MISURABILE: Posso definire cosa è un "buon risultato"?  
  → SÌ: Posso creare verifiche nella skill

□ DELEGABILE: Potrei spiegare il processo a qualcuno?  
  → SÌ: Posso spiegarlo anche a Claude

□ TIME-CONSUMING: Mi prende più di 10 minuti ogni volta?  
  → SÌ: Il risparmio di tempo giustifica la creazione

Se rispondete SÌ a 3 o più domande, quella task 

dovrebbe diventare una skill.

Esempi concreti di skill che l'autore ha creato:

* LinkedIn Post Generator: genera post nello stile personale dell'autore  
* Audit Skill: lancia automaticamente i tre sub-agenti (Researcher, Reviewer, QA)  
* Publish Skill: pubblica contenuti su YouTube, Instagram e Facebook  
* Meta Push: gestisce la pubblicazione su piattaforme Meta  
* Shorts Creator: crea contenuti short-form per social media

---

### **28.2 — Il Processo di Creazione Passo per Passo**

#### **Definizione del Concetto**

La creazione di una skill personalizzata è un processo in quattro fasi: definire, strutturare, codificare e testare. Non è necessario essere programmatori per iniziare — Claude Code può assistere in ogni fase.

#### **Fase 1: Definire la Skill**

Il primo passo è definire chiaramente cosa deve fare la skill. Questo significa rispondere a tre domande:

1. COSA: Quale risultato deve produrre?  
2. COME: Quali passi deve seguire per arrivarci?  
3. QUANDO: In quali circostanze viene chiamata?

Esempio (LinkedIn Post Generator):

text

COSA: Generare un post LinkedIn nel mio stile personale  
COME:   
  1\. Ricevere un topic o un'idea dall'utente  
  2\. Analizzare i reference post per estrarre stile e tono  
  3\. Generare una bozza del post  
  4\. Formattare secondo le convenzioni personali  
  5\. Aggiungere CTA appropriata  
  6\. Presentare il risultato per approvazione

QUANDO: Ogni volta che voglio creare un nuovo post LinkedIn

#### **Fase 2: Strutturare la Skill**

Questa fase consiste nel creare la struttura della cartella e del file skill.md:

text

STRUTTURA DA CREARE  
═══════════════════

.claude/skills/  
└── linkedin-post/  
    ├── skill.md          ← La checklist/orchestratore  
    ├── scripts/          ← Gli script eseguibili  
    │   └── generate.py  
    └── references/       ← I dati di riferimento

        └── my\_posts.md   ← Post precedenti come esempio

Il file skill.md dovrebbe seguire questa struttura:

Markdown

**\# LinkedIn Post Generator**

Generate a LinkedIn post matching your writing style.

**\#\# Input Validation**  
\- Topic or idea: REQUIRED  
\- Target audience: OPTIONAL (default: entrepreneurs)  
\- Post style: OPTIONAL (default: storytelling)  
\- Include CTA: OPTIONAL (default: yes)

**\#\# Process**  
1\. Read reference posts from references/my\_posts.md  
2\. Analyze writing patterns:  
   \- Sentence length  
   \- Emoji usage  
   \- Line spacing  
   \- Hook structure  
   \- CTA format  
3\. Generate draft post  
4\. Format according to patterns  
5\. Add appropriate CTA  
6\. Present to user

**\#\# Output Format**  
\- Present the post in a code block  
\- Show character count  
\- Indicate target platform format compliance

**\#\# Error Handling**  
\- If reference file not found → warn user, generate generic  
\- If topic too vague → ask for clarification  
\- If post exceeds LinkedIn character limit → offer to shorten

**\#\# Self-Healing**  
\- If output doesn't match reference style → re-analyze   
  references and regenerate  
\- If CTA is missing → add default CTA

\- Log any corrections for future improvement

#### **Fase 3: Codificare gli Script**

Gli script trasformano la parte ripetitiva e deterministica del processo in codice eseguibile. Per il LinkedIn Post Generator, lo script potrebbe gestire:

* Lettura e parsing dei file di riferimento  
* Analisi statistica del tono (lunghezza frasi, frequenza emoji, etc.)  
* Formattazione del post secondo regole predefinite  
* Conteggio caratteri e validazione limiti piattaforma

L'aspetto fondamentale è che non dovete necessariamente scrivere questi script voi stessi. Potete chiedere a Claude:

text

"Per favore, guarda la skill.md che ho creato nella   
cartella linkedin-post e crea gli script necessari   
per implementare il processo descritto. Segui le 

best practice della documentazione ufficiale Claude."

Claude creerà gli script basandosi sulla checklist nel skill.md.

#### **Fase 4: Testare e Iterare**

Una volta creata la skill, testatela con diversi input:

text

Test 1: "Usa la skill LinkedIn Post per creare un   
        post sull'importanza delle skill in Claude Code"

Test 2: "Usa la skill LinkedIn Post per creare un   
        post su come l'AI sta cambiando il business"

Test 3: "Usa la skill LinkedIn Post per creare un 

        post controverso sull'overuse degli Agent Teams"

Per ogni test, valutate:

* Il risultato rispecchia il vostro stile? Se no, migliorate i reference data  
* Il processo ha avuto errori? Se sì, migliorate la checklist  
* Il formato è corretto? Se no, aggiornate le regole di formattazione  
* Il self-healing ha funzionato? Se no, migliorate la sezione Error Handling

#### **Il Prompt Completo per Chiedere a Claude di Creare una Skill**

Basandosi sull'approccio mostrato nella guida, ecco un template di prompt efficace:

text

"Per favore, crea una skill completa per \[DESCRIZIONE\].

La skill deve:  
1\. Essere posizionata in .claude/skills/\[NOME\]/  
2\. Avere un file skill.md con checklist completa  
3\. Avere una cartella scripts/ con gli script necessari  
4\. Seguire le best practice della documentazione ufficiale Claude  
5\. Includere gestione errori e self-healing  
6\. Includere validazione degli input

Per il file skill.md, segui la struttura:  
\- Descrizione  
\- Input Validation  
\- Process (step by step)  
\- Output Format  
\- Error Handling  
\- Self-Healing

Per gli script, usa Python e assicurati che siano   
deterministici e ben documentati.

Se hai bisogno di reference data, chiedimi e te li fornirò."

---

### **28.3 — L'Esempio del Social Media Manager**

#### **Definizione del Concetto**

L'autore della guida mostra il suo Social Media Manager come esempio completo di un progetto basato interamente su skill. Questo progetto controlla tutte le sue piattaforme social (YouTube italiano, YouTube inglese, LinkedIn e altri) tramite un insieme di skill coordinate.

#### **Struttura Reale del Progetto**

Dalla guida, la struttura del Social Media Manager dell'autore include le seguenti skill:

text

social-media-manager/  
├── CLAUDE.md                    ← Conciso, essenziale  
└── .claude/  
    ├── agents/  
    │   ├── researcher.md  
    │   ├── reviewer.md  
    │   └── qa.md  
    ├── rules/  
    │   └── \[regole modulari\]  
    └── skills/  
        ├── linkedin-post/       ← Generatore LinkedIn post  
        │   ├── skill.md  
        │   ├── scripts/  
        │   └── references/      ← 50+ post scritti manualmente  
        ├── publish/             ← Pubblicazione su piattaforme  
        │   ├── skill.md  
        │   └── scripts/  
        │       ├── build\_schedule.py  
        │       ├── check\_meta.py  
        │       ├── check\_youtube.py  
        │       └── upload\_youtube.py  
        ├── audit/               ← Lancia i 3 sub-agenti automaticamente  
        │   ├── skill.md  
        │   └── scripts/  
        ├── meta-push/           ← Pubblicazione su Meta  
        │   ├── skill.md  
        │   └── scripts/  
        └── shorts/              ← Creazione contenuti short  
            ├── skill.md

            └── scripts/

#### **L'Interazione tra Skill e Sub-agenti**

Un dettaglio particolarmente potente emerso dalla guida è la skill Audit:

*"Quando gli chiedo 'fammi un audit', devi chiamarmi tre agenti che sono esattamente quelli che vi ho presentato."*

Questo significa che la skill Audit è un orchestratore di sub-agenti. Quando l'utente dice "fammi un audit", la skill:

1. Chiama automaticamente il Researcher sub-agent  
2. Chiama automaticamente il Reviewer sub-agent  
3. Chiama automaticamente il QA sub-agent  
4. Raccoglie i risultati  
5. Produce un report consolidato

L'utente non deve sapere che ci sono tre sub-agenti coinvolti. Dice solo "audit" e riceve un report completo. Questa è l'astrazione: la complessità è nascosta dietro un'interfaccia semplice.

#### **Il Tempo di Creazione**

L'autore condivide un dato importante sul tempo necessario per creare il suo Social Media Manager:

*"C'ho messo 2 ore e mezza a fare planning e dopo ci ha messo 3 ore a costruirlo. Era un one-shot."*

Quindi:

* 2,5 ore di planning mode (creazione del piano dettagliato)  
* 3 ore di esecuzione in bypass permission (costruzione automatica)  
* Totale: 5,5 ore per un sistema completo di gestione social media

Questo sistema, una volta costruito, viene usato ogni giorno per generare contenuti, pubblicarli e gestire le piattaforme. Il ROI è enorme: 5,5 ore di investimento per un sistema che risparmia ore ogni giorno.

#### **L'Interfaccia UI Personalizzata**

L'autore menziona brevemente un dettaglio avanzato:

*"Questo mio ha poi un'interfaccia UI dove se premo un tasto e non mi piace, il feedback che do va, torna dentro Claude, migliora pian pianino anche la generazione di post."*

Questo significa che l'autore ha costruito un'interfaccia grafica personalizzata che:

1. Mostra il post generato  
2. Permette di dare feedback con un singolo tasto  
3. Il feedback viene inviato a Claude Code  
4. Claude migliora la skill basandosi sul feedback  
5. Le generazioni successive sono progressivamente migliori

Questo è il livello esperto dell'uso delle skill: un sistema che non solo funziona, ma migliora autonomamente con l'uso.

---

### **28.4 — Skill che Chiamano Skill**

#### **Definizione del Concetto**

Le skill possono essere composte — una skill può chiamare altre skill come parte del suo processo. Questo permette di creare catene complesse di operazioni a partire da un singolo comando.

#### **Spiegazione Approfondita**

Nell'esempio del Social Media Manager, la skill "publish" potrebbe internamente:

1. Chiamare la skill "linkedin-post" per generare il contenuto  
2. Chiamare la skill "meta-push" per pubblicare su Facebook  
3. Chiamare la skill "shorts" per creare una versione short del contenuto

Tutto questo da un singolo comando: *"Pubblica il mio ultimo contenuto su tutte le piattaforme."*

text

COMPOSIZIONE DI SKILL  
═════════════════════

Comando utente: "Pubblica su tutto"  
         │  
         ▼  
    ┌──────────┐  
    │ publish  │ (skill principale)  
    │ skill.md │  
    └────┬─────┘  
         │  
    ┌────┼────────────────┐  
    │    │                │  
    ▼    ▼                ▼  
┌──────┐ ┌──────────┐ ┌────────┐  
│linke-│ │ meta-    │ │shorts  │  
│din-  │ │ push     │ │skill   │  
│post  │ │ skill    │ │        │  
│skill │ │          │ │        │  
└──┬───┘ └────┬─────┘ └───┬────┘  
   │          │            │  
   ▼          ▼            ▼  
LinkedIn   Facebook     YouTube

  post      post        Shorts

Ogni skill ha i suoi script, le sue verifiche e il suo self-healing. La skill principale coordina tutto, gestisce gli errori propagati e produce un report finale consolidato.

---

# **CAPITOLO 29**

## **Il Marketplace delle Skill**

---

### **29.1 — Dove Trovare Skill Esterne**

#### **Definizione del Concetto**

Il marketplace delle skill è un ecosistema di skill create dalla community che possono essere importate e utilizzate nei propri progetti. La guida menziona specificamente SkillM come marketplace principale.

#### **Spiegazione Approfondita**

L'autore fornisce informazioni concrete sul marketplace:

*"SkillM è uno che è fenomenale. Ci sono 351.349 skill."*

Il marketplace è organizzato per categorie:

text

CATEGORIE DEL MARKETPLACE SKILLM  
═════════════════════════════════

├── Tool Development  
├── Business  
├── Data  
├── AI  
├── Content  
├── Social Media  
├── Documentation

└── \[altre categorie\]

#### **Come Trovare Skill nel Marketplace**

La procedura pratica mostrata nella guida:

1. Andate su skillm.com (o il sito del marketplace)  
2. Navigate per categoria o cercate per keyword  
3. Trovate una skill che vi interessa  
4. Premete il pulsante "Copy" per copiare il comando di installazione  
5. Incollate il comando in Claude Code  
6. La skill viene importata nel vostro progetto

#### **Come Importare una Skill**

L'importazione è semplice come un prompt:

text

"Per favore importa questa skill: \[incolla comando copiato   
dal marketplace\] e creami un post di LinkedIn sull'argomento 

\[topic\]"

Claude scarica la skill, la posiziona nella cartella corretta e la esegue immediatamente se richiesto.

#### **L'Avvertimento sulla Sicurezza**

La guida menziona un punto importante sulla sicurezza:

*"Dovrete stare semplicemente attenti perché qui abbiamo MCP e strumenti sviluppati da terzi che possono contenere malware."*

Lo stesso principio si applica alle skill importate dal marketplace:

| Rischio | Come mitigarlo |
| ----- | ----- |
| Skill con codice malevolo | Leggete il codice degli script prima di eseguirli |
| Skill che accedono a dati sensibili | Verificate quali permessi richiede |
| Skill di bassa qualità | Controllate le valutazioni e i download |
| Skill obsolete | Verificate la data di ultimo aggiornamento |

---

### **29.2 — Quando Importare vs Quando Creare**

#### **Definizione del Concetto**

Non tutte le skill devono essere create da zero. Alcune volte è più efficiente importare una skill esistente e personalizzarla. Altre volte è indispensabile crearla da zero. La scelta dipende dalla specificità della vostra esigenza.

#### **Framework Decisionale**

text

ALBERO DECISIONALE: IMPORTARE O CREARE?  
════════════════════════════════════════

La skill richiede il MIO tono di voce personale?  
│  
├── SÌ → CREA da zero  
│   (Nessuna skill esterna avrà il vostro stile)  
│  
└── NO → La skill è tecnica/procedurale?  
    │  
    ├── SÌ → IMPORTA dal marketplace  
    │   │  
    │   ├── Skill di deploy  
    │   ├── Skill di formattazione codice  
    │   ├── Skill di design/CSS  
    │   └── Skill di test automatici  
    │  
    └── NO → La skill richiede dati proprietari?  
        │  
        ├── SÌ → CREA da zero con i tuoi dati  
        │  
        └── NO → IMPORTA e personalizza

#### **Perché le Skill di Design Funzionano Meglio come Import**

La guida contiene un'osservazione sottile ma cruciale:

*"Le skill che funzionano meglio sono generalmente quelle di design, dove abbiamo dei CSS o degli elementi all'interno dei website. Funzionano perché per fare design non abbiamo bisogno di un database molto ricco per allenare l'AI, perché non c'è il nostro tono di voce."*

Questo spiega perché certi tipi di skill si possono importare tranquillamente:

* Skill di design/CSS: il "tono di voce" non esiste nel design visivo. Un bottone è un bottone, un layout è un layout. Le skill generiche funzionano bene.  
* Skill di codice: il codice funzionale non ha "personalità". Una funzione di autenticazione è la stessa per tutti.  
* Skill di deploy: il processo di deployment è standardizzato e non richiede personalizzazione.

Mentre altri tipi di skill devono essere personalizzate:

* Skill di scrittura (post, email, copywriting): il tono di voce è tutto  
* Skill di comunicazione (cold outreach, onboarding email): la personalità fa la differenza  
* Skill di branding (contenuti brand-specific): ogni brand è unico

---

# **CAPITOLO 30**

## **La Qualità dei Dati di Riferimento**

---

### **30.1 — Perché i Reference Data Sono Tutto**

#### **Definizione del Concetto**

I reference data (dati di riferimento) sono gli esempi, i campioni e le informazioni che fornite a una skill per insegnarle il vostro stile, le vostre preferenze e i vostri standard di qualità. Sono il "materiale di addestramento" della skill.

#### **Spiegazione Approfondita**

Questo è forse il concetto più importante dell'intera sezione skill. L'autore della guida lo afferma con chiarezza:

*"Il motivo per cui quando fate cold outreach le email sembrano degli automi, quando scrivete LinkedIn Post fate 87 prompt perché non vi viene l'output che volete, è semplicemente perché il database che avete come riferimento non è sufficientemente ricco."*

La qualità del reference data determina la qualità dell'output. Non la skill, non il prompt, non il modello — i dati di riferimento.

#### **L'Esempio Concreto dalla Guida**

L'autore mostra il suo progetto di Social Media Manager e rivela:

*"Ho una serie infinita di post di LinkedIn che ho scritto manualmente perché lui capisse quali sono le mie idee, qual è la mia voce. Come vedete sono un mezzo cazziliardo di robe."*

*"Per il mio LinkedIn, la mia skill mette in pasto tutti quelli che vi ho già mostrato, che sono qualche migliaio di righe."*

Questo significa che la skill LinkedIn Post Generator dell'autore ha accesso a:

* Decine di post scritti manualmente dall'autore  
* Migliaia di righe di testo di riferimento  
* Pattern completi di formattazione, emoji, struttura, CTA

Confrontate questo con una skill importata dal marketplace che non ha NESSUN reference data personalizzato. La differenza di output è prevedibilmente abissale.

#### **La Catena della Qualità**

text

CATENA DELLA QUALITÀ DELLE SKILL  
════════════════════════════════

Reference Data di alta qualità  
    │  
    ▼  
Skill capisce il VOSTRO stile  
    │  
    ▼  
Output che sembra scritto da VOI  
    │  
    ▼  
Minimo editing manuale necessario  
    │  
    ▼  
Alta produttività, alto ROI

Reference Data scadente o assente  
    │  
    ▼  
Skill produce output GENERICO  
    │  
    ▼  
Output che sembra scritto da un robot  
    │  
    ▼  
Editing manuale estensivo necessario  
    │  
    ▼  
Bassa produttività, basso ROI

---

### **30.2 — Come Costruire Reference Data di Qualità**

#### **Definizione del Concetto**

La costruzione di reference data di qualità è un processo che richiede tempo e impegno iniziale, ma produce dividendi enormi nel lungo periodo. Non è un processo che potete delegare completamente all'AI — richiede la vostra partecipazione attiva.

#### **La Regola d'Oro**

*"La capacità di far scrivere l'AI in modo umano è strapagata ed è estremamente difficile."*

Questa frase dell'autore contiene un'intuizione business fondamentale: la capacità di produrre contenuti AI che suonano umani è un servizio di alto valore nel mercato attuale. E la chiave per arrivarci sono i reference data.

#### **Processo di Costruzione**

text

PROCESSO DI COSTRUZIONE DEI REFERENCE DATA  
═══════════════════════════════════════════

FASE 1: RACCOLTA (Settimana 1-2)  
───────────────────────────────  
□ Raccogliete tutto il contenuto che avete già prodotto  
  manualmente:  
  \- Post LinkedIn  
  \- Email inviate  
  \- Messaggi di vendita  
  \- Articoli scritti  
  \- Script video  
  \- Presentazioni  
    
□ Organizzate per tipologia e qualità  
□ Selezionate solo i migliori (top 20%)

FASE 2: CATEGORIZZAZIONE (Settimana 2-3)  
──────────────────────────────────────────  
□ Dividete per tipo di contenuto  
□ Identificate pattern ricorrenti:  
  \- Come iniziate (hook)  
  \- Come strutturate il corpo  
  \- Come chiudete (CTA)  
  \- Che emoji usate e dove  
  \- Che lunghezza hanno i paragrafi  
  \- Che tono usate (formale, informale, tecnico)

FASE 3: FORMATTAZIONE (Settimana 3\)  
────────────────────────────────────  
□ Convertite tutto in formato Markdown  
□ Aggiungete annotazioni dove utile:  
  "Questo post ha convertito molto bene perché..."  
  "Questo formato funziona per il pubblico X..."  
□ Salvate nella cartella references/ della skill

FASE 4: ITERAZIONE CONTINUA (Ongoing)  
──────────────────────────────────────  
□ Ogni volta che producete contenuto di qualità,  
  aggiungetelo ai reference data  
□ Ogni volta che un output AI è particolarmente buono,  
  aggiungetelo come esempio  
□ Rimuovete periodicamente esempi obsoleti o di bassa qualità

#### **Il Numero Minimo di Riferimenti**

Non c'è un numero magico, ma basandosi sull'esperienza dell'autore:

| Tipo di Contenuto | Minimo Consigliato | Ideale |
| ----- | ----- | ----- |
| Post LinkedIn | 20 post | 50+ post |
| Email commerciali | 15 email | 30+ email |
| Script video | 10 script | 20+ script |
| Articoli blog | 10 articoli | 25+ articoli |
| Messaggi cold outreach | 20 messaggi | 50+ messaggi |

Più reference data avete, più Claude capirà le sfumature del vostro stile. La differenza tra 10 e 50 riferimenti è enorme in termini di qualità dell'output.

---

### **30.3 — L'Errore degli M-Dashes e il Tono Robotico**

#### **Definizione del Concetto**

L'autore identifica specifici marker che rivelano quando un contenuto è stato generato da AI senza reference data adeguati. Questi marker includono l'uso eccessivo di M-dashes ("—"), strutture di frase ripetitive e un tono generalmente "robotico".

#### **Spiegazione Approfondita**

*"Avete M-dashes quindi trattini molto AI e via dicendo."*

Gli M-dashes sono il segnale più riconoscibile di testo generato da AI. Quando vedete frasi come:

* "L'intelligenza artificiale — strumento rivoluzionario del nostro tempo — sta trasformando..."  
* "Le skill — se utilizzate correttamente — possono..."  
* "Il business moderno — in continua evoluzione — richiede..."

Questi trattini lunghi sono usati dall'AI con una frequenza molto superiore a quella di un essere umano. Un lettore attento li riconosce immediatamente come "scritto da AI".

#### **Come Eliminare il Tono Robotico**

La soluzione è duplice:

1\. Reference Data Ricchi:  
Se la skill ha accesso a 50+ post scritti da voi manualmente e voi non usate mai M-dashes, Claude imparerà a non usarli.

2\. Regole Esplicite nella Skill:  
Potete aggiungere regole specifiche nella skill.md:

Markdown

**\#\# Regole di Stile**  
\- NON usare MAI M-dashes ("—")  
\- NON usare frasi che iniziano con "In un mondo..."  
\- NON usare "Immagina di..." come hook  
\- NON usare più di 2 emoji per paragrafo  
\- Usa frasi brevi (max 15 parole)

\- Vai a capo spesso (ogni 1-2 frasi)

La combinazione di reference data ricchi e regole esplicite produce output che sono indistinguibili da contenuto scritto manualmente.

---

### **30.4 — Il Valore Commerciale delle Skill Personalizzate**

#### **Definizione del Concetto**

Le skill personalizzate con reference data di alta qualità rappresentano un asset commerciale significativo. Possono essere vendute come servizio, utilizzate per fornire consulenza o implementate nelle aziende dei clienti.

#### **Spiegazione Approfondita**

L'autore della guida fa riferimento specifico alla monetizzazione:

*"Quando andrete a vendere questa tipologia di servizio per social media agency, content creation agencies, ecco è estremamente importante la qualità del reference data."*

E aggiunge:

*"La capacità di far scrivere l'AI in modo umano è strapagata."*

Questo posiziona le skill personalizzate come un servizio premium nel mercato dell'AI:

text

MODELLO DI BUSINESS BASATO SU SKILL  
════════════════════════════════════

SERVIZIO BASE (Basso valore):  
"Ti installo Claude Code e ti faccio vedere come usarlo"  
→ Prezzo: €200-500

SERVIZIO INTERMEDIO (Medio valore):  
"Ti creo un sistema con sub-agenti e skill generiche"  
→ Prezzo: €1.000-3.000

SERVIZIO PREMIUM (Alto valore):  
"Ti creo skill personalizzate con il TUO tono di voce,  
 i TUOI reference data, il TUO brand identity.  
 L'output è indistinguibile da quello che scrivi tu."  
→ Prezzo: €5.000-15.000+

SERVIZIO ENTERPRISE:  
"Implemento un sistema completo con skill personalizzate,  
 sub-agenti, agent teams, deployment e monitoring  
 per la tua azienda da 70 milioni di fatturato."

→ Prezzo: negoziato individualmente

#### **La Lezione Commerciale**

L'autore condivide un'intuizione importante per chi vuole monetizzare le skill:

*"Non basta solo il database, non basta solo sapere cos'è una skill. Servono una serie di piccole altre accortezze che vi permettono poi di rispecchiare il vostro tono di voce."*

Queste "piccole accortezze" — che si apprendono solo con l'esperienza pratica — sono ciò che distingue un'implementazione mediocre da una eccellente. Sono il motivo per cui l'autore può vendere servizi di consulenza ad alto prezzo: non vende la conoscenza di Claude Code (che è accessibile a tutti), ma vende l'esperienza di implementazione maturata in centinaia di progetti.

---

## **Riepilogo della Parte 8**

In questa Parte avete appreso:

1. Cosa sono le skill: processi codificati e ripetibili composti da skill.md (orchestratore) e scripts/ (codice eseguibile)  
2. L'architettura interna: il file skill.md è la checklist/direttore d'orchestra, gli script sono i musicisti che eseguono il lavoro deterministico  
3. Il processo di self-healing: quando qualcosa va storto, Claude usa il CLAUDE.md e la skill.md per auto-correggersi e aggiornare la checklist  
4. La differenza tra LLM e codice deterministico: gli script sono prevedibili e affidabili, l'LLM gestisce il ragionamento e l'orchestrazione  
5. Come creare skill personalizzate: definire, strutturare, codificare, testare — un processo in quattro fasi  
6. L'esempio del Social Media Manager: un sistema completo costruito in 5,5 ore che gestisce tutti i social dell'autore  
7. Il marketplace delle skill: SkillM con 351.349+ skill disponibili, organizzate per categoria  
8. Quando importare vs creare: skill tecniche → importa; skill con tono di voce → crea da zero  
9. L'importanza critica dei reference data: la qualità dell'output dipende dalla quantità e qualità dei dati di riferimento, non dalla skill stessa  
10. Il valore commerciale: le skill personalizzate con reference data di alta qualità sono un asset vendibile ad alto prezzo  
11. Il pattern di conversione MCP → Skill: usare MCP per prototipare, poi convertire in skill per risparmiare contesto

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - General|General Area]]
- [[Map - Outreach|Outreach Area]]
- [[Map - Prove|Prove Area]]
