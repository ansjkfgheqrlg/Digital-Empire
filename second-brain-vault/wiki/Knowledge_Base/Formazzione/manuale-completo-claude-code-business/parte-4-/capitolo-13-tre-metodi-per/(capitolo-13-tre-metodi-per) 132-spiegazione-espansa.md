# 13.2 — Spiegazione Espansa
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-13-tre-metodi-per]]

## Content

Prima di descrivere i tre metodi, l'autore introduce due risorse fondamentali per trovare ispirazione e riferimenti visivi per 
i siti da costruire: 
Risorse per Riferimenti Visivi 

--- PAGE 29 ---
Risorsa 1: Godly Website (godly.website) 
●​
Contiene siti web che hanno vinto premi (award-winning websites) 
●​
Eccellenti a livello di design 
●​
L'autore nota: "Senza dubbio a livello di design sono belli. Poi sulla conversion, quella è un'altra roba." — 
Questo significa che un sito premiato per il design non è necessariamente ottimizzato per convertire visitatori 
in clienti 
●​
Utile per copiare/replicare siti di alta qualità estetica 
Risorsa 2: Dribbble (dribbble.com) 
●​
Contiene design di ogni tipo: animazioni, branding, UI/UX 
●​
Permette di trovare componenti specifici (bottoni, form, layout) 
●​
Fornisce codice e specifiche di design 
●​
Molto utile per trovare singoli elementi da integrare nei propri progetti 
Metodo 1: Prompt Dettato a Voce + Editing Manuale 
text 
FLUSSO DEL METODO 1: 
 
[Voce dell'utente] → [Speech-to-Text] → [Prompt scritto] → [Claude Code] → [Output] 
                                                                    ↓ 
                                                            [Editing manuale] 
                                                                    ↓ 
                                                            [Feedback vocale] 
                                                                    ↓ 
                                                              [Iterazione] 
Come funziona:​
L'utente detta il prompt a voce utilizzando uno strumento di Speech-to-Text (STT). Il testo trascritto viene inviato a 
Claude Code, che genera l'output. L'utente poi fornisce feedback vocale o effettua editing manuale. 
Perché è efficace:​
L'autore spiega il principio di throughput: "Se ci pensate, nel momento in cui una persona parla va molto più veloce a 
scrivere e a dettare parole a un throughput per hour molto maggiore di quando una persona scrive." 
Per quantificare: 
text 
VELOCITÀ DI OUTPUT PER MODALITÀ: 
 
Scrittura a tastiera:    ~40-60 parole/minuto (utente medio) 
Dettatura vocale:        ~130-180 parole/minuto (parlato naturale) 
Rapporto:                ~3x più veloce con la voce 
 

--- PAGE 30 ---
In termini di prompt: 
Un prompt di 200 parole: 
• Scritto: ~4 minuti 
• Dettato: ~1.5 minuti 
• Risparmio: ~2.5 minuti per prompt 
 
Su 20 prompt in una sessione: 
• Risparmio totale: ~50 minuti 
Quando è particolarmente utile: 
●​
Prompt lunghi e descrittivi 
●​
Sessioni di brainstorming con l'AI 
●​
Quando si vuole "pensare ad alta voce" e lasciare che Claude interpreti 
●​
Per utenti che scrivono lentamente a tastiera 
Strumenti di STT utilizzabili: 
●​
Su Mac: tasto Function (Fn) attiva la dettatura nativa 
●​
La trascrizione include punteggiatura, virgolette e formattazione 
●​
L'autore lo utilizza regolarmente nel suo workflow quotidiano 
Metodo 2: Utilizzo di Componenti Preconfezionati 
text 
FLUSSO DEL METODO 2: 
 
[Sito di componenti] → [Seleziona componente] → [Copy Prompt] → [Incolla in Claude Code] 
       ↓                                                                    ↓ 
[21st.dev]                                                         [Claude replica 
[altri siti]                                                        il componente 
                                                                    nel progetto] 
Come funziona:​
Esistono siti web che offrono componenti UI (bottoni, navbar, sezioni, animazioni, interfacce 3D) già pronti. L'utente 
seleziona il componente desiderato, copia il prompt associato, e lo incolla in Claude Code che lo replica nel progetto. 
Risorsa principale: 21st.dev​
L'autore presenta questo sito come una risorsa preziosa che "non molti conoscono". Caratteristiche: 
●​
Libreria di componenti visivi con il pulsante "Copy Prompt" 
●​
Include componenti interattivi e 3D (es. interfacce che seguono il mouse) 
●​
Ogni componente è sostanzialmente un insieme di HTML, CSS, JavaScript 
●​
Claude Code è "estremamente bravo quando si tratta di codice" — quindi la replica è fedele 
Perché funziona bene:​
I componenti web sono codice (HTML, CSS, JavaScript). Claude Code eccelle nel lavorare con il codice perché: 

--- PAGE 31 ---
●​
Il codice è strutturato e non ambiguo 
●​
Ogni componente ha una specifica tecnica chiara 
●​
La replica di codice è deterministica (a differenza della generazione creativa di testo) 
Quando è utile: 
●​
Quando volete un elemento specifico (un'animazione, un layout, un effetto) 
●​
Quando trovate un componente che vi piace e volete integrarlo nel vostro sito 
●​
Per assemblare rapidamente un sito combinando componenti diversi 
●​
Richiede registrazione sul sito dei componenti 
Metodo 3: Design di Riferimento + Screenshot Loop ⭐ (Raccomandato) 
text 
FLUSSO DEL METODO 3: 
 
[Screenshot sito riferimento] → [CLAUDE.md con regole] → [Claude Code costruisce] 
         ↓                                                        ↓ 
[Stili CSS copiati]                                     [Screenshot automatico] 
                                                                  ↓ 
                                                        [Confronto con riferimento] 
                                                                  ↓ 
                                                        [Identifica differenze] 
                                                                  ↓ 
                                                        [Corregge automaticamente] 
                                                                  ↓ 
                                                        [Nuovo screenshot] 
                                                                  ↓ 
                                                        [Ripete fino a convergenza] 
Questo è il metodo che l'autore "generalmente raccomanda" ed è il più sofisticato dei tre. La ragione della 
raccomandazione è legata a un concetto fondamentale che merita un capitolo dedicato: il ciclo Task-Do-Verify (Capitolo 
14).

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - General|General Area]]
