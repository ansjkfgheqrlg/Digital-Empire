# 35.1 — Cosa Sono gli Hooks

Definizione del Concetto 
Un hook è uno script personalizzato che si avvia automaticamente prima o dopo ogni chiamata 
di strumenti da parte di Claude. In parole semplici, un hook è un'azione automatica che scatta 
ogni volta che un certo evento si verifica nel vostro workflow di Claude Code. Immaginate un 
hook come una trappola a molla: ogni volta che qualcosa passa sopra (l'evento), la molla scatta 
(lo script si esegue). 
Spiegazione Approfondita 
La guida originale introduce gli hook con una definizione precisa: 
"Che cosa sono gli hook? Ossia gli script personalizzati che si avviano automaticamente prima o 
dopo ogni chiamata di strumenti da parte di Claude. Immaginatevi come: nel momento in cui voi 
premiate Enter, qualsiasi cosa succede e verrà staccata dall'LLM." 
Questa definizione contiene tre concetti chiave che meritano espansione: 
1. "Script personalizzati": gli hook sono codice vero e proprio, non prompt LLM. Sono programmi 
che voi (o Claude) scrivete e che vengono eseguiti dal sistema operativo, non dal modello di 
linguaggio. Questo è fondamentale perché significa che gli hook sono deterministici — 
producono sempre lo stesso risultato dato lo stesso evento. 
2. "Si avviano automaticamente": non dovete fare nulla per attivare un hook. Una volta 
configurato, si esegue da solo ogni volta che l'evento associato si verifica. Non c'è bisogno di 
ricordarsi di attivarlo, di premere un tasto o di dare un prompt. 
3. "Prima o dopo ogni chiamata di strumenti": gli hook possono scattare in due momenti: 
●​
Pre-hook: prima che Claude esegua un'azione (ad esempio, prima di modificare un file) 
●​
Post-hook: dopo che Claude ha completato un'azione (ad esempio, dopo aver finito una 
task) 
text 
MECCANISMO DEGLI HOOKS 
══════════════════════ 
 

--- PAGE 171 ---
SENZA HOOKS: 
    Utente → Prompt → Claude lavora → Risultato → [silenzio] 
     
    L'utente non sa che Claude ha finito. 
    Potrebbe passare mezz'ora prima di accorgersene. 
 
CON HOOKS: 
    Utente → Prompt → Claude lavora → Risultato → 🔔 HOOK SCATTA! 
     
    L'utente viene notificato immediatamente. 
    Zero tempo perso. 
La Differenza Fondamentale: Hooks vs LLM 
Un punto che la guida sottolinea con forza è che gli hook sono distaccati dal funzionamento 
dell'LLM: 
"Queste automazioni sono automatiche, cosa vuol dire? Che sono distaccate dal funzionamento 
dell'LLM. Sostanzialmente significa: non sono più legate alla token consumption di Claude o 
Sonnet, il modello che stiamo utilizzando, ma sostanzialmente partono ad evento. E sono codice, 
quindi non sono qualcosa di non deterministico e non misurabile." 
Questo è un concetto architetturale importante. Confrontiamo: 
Caratteristica 
Prompt LLM 
Hook 
Consumo token 
Sì, ogni esecuzione costa token 
No, zero consumo token 
Determinismo 
Non deterministico (output può variare) 
Deterministico (output sempre uguale) 
Velocità 
Dipende dalla complessità del prompt 
Istantaneo (è codice compilato) 

--- PAGE 172 ---
Affidabilità 
Può "allucinare" o sbagliare 
Fa esattamente quello che è programmato a 
fare 
Attivazione 
Richiede un prompt umano 
Automatica, basata su eventi 
Costo 
Contribuisce al consumo del piano 
Gratuito (è codice locale) 
Dove Vengono Configurati gli Hooks 
Gli hook vengono configurati nel file settings.json all'interno della cartella .claude/: 
text 
progetto/ 
└── .claude/ 
    └── settings.json    ← Qui si configurano gli hooks 
Il file settings.json contiene sia i permessi del sistema che le definizioni degli hook. 
Perché gli Hooks Sono Importanti 
Gli hook risolvono un problema pratico che l'autore della guida descrive dalla propria esperienza: 
"Io ho, quando uso Claude Code, per sapere quando un workflow o un prompt eseguire e 
richiede un mio input, ho un suono. Questo suono succede ogni volta che Claude finisce. Questo 
è un hook. Sono delle cose automatiche che succedono ogni volta che un evento si manifesta." 
"Questo è molto utile per evitare che magari voi ve ne andiate dal computer e poi il workflow 
abbia finito e magari state mezz'ora via. E realisticamente avreste potuto recuperare questa 
mezz'ora." 
In un contesto aziendale dove il tempo è denaro, recuperare mezz'ora per ogni ciclo di lavoro è 
un risparmio enorme su base giornaliera. 
 

--- PAGE 173 ---

