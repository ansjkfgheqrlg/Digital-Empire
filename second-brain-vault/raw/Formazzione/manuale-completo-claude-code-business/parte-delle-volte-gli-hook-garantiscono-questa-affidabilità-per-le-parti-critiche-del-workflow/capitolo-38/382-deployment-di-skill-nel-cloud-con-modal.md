# 38.2 — Deployment di Skill nel Cloud con Modal

Definizione del Concetto 
Modal è la piattaforma di deployment che l'autore della guida preferisce e utilizza per portare le 
proprie skill nel cloud. Modal permette di creare cloud functions — funzioni che girano su server 
remoti e sono accessibili tramite URL pubblici. 
Spiegazione Approfondita 
La guida mostra il processo completo di deployment di una skill (il LinkedIn Post Generator) su 
Modal: 
text 
PROCESSO DI DEPLOYMENT SU MODAL 
════════════════════════════════ 
 
PASSO 1: Creare un Account Modal 
───────────────────────────────── 
• Andate su modal.com 
• Sign in con Google 
• Completate la registrazione 
• Riceverete due righe di autenticazione da copiare 
 
PASSO 2: Collegare Modal a Claude Code 
─────────────────────────────────────── 
• Copiate le due righe di autenticazione 
• Incollatele in Claude Code 
• "Connettimi a Modal" 
• Claude configura la connessione 
 
PASSO 3: Creare un Token API 
───────────────────────────── 
• Nella dashboard Modal → Token 
• "New API Token" 
• Dategli un nome descrittivo 
• Copiate il token 
 

--- PAGE 192 ---
PASSO 4: Chiedere a Claude di Fare il Deployment 
───────────────────────────────────────────────── 
"Ho una skill nella cartella .claude/skills che mi  
 permette di creare dei post LinkedIn. Vorrei creare  
 una mia API, quindi avere un mio URL che posso  
 premere e avere questa skill accessibile nel web. 
 Vorrei che questo fosse accessibile non solo a me  
 ma a tutti. Per farlo, vorrei utilizzare Modal. 
 L'URL al mio Modal è [link]. 
 Per favore entraci e creami una cloud function. 
 Una volta che hai fatto, fammi vedere l'URL." 
 
PASSO 5: Claude Esegue il Deployment 
───────────────────────────────────── 
• Claude crea la cloud function su Modal 
• Configura l'interfaccia web 
• Pubblica il servizio 
• Restituisce l'URL pubblico 
 
RISULTATO: 
────────── 
URL: https://giovanni-beggiato--linkedin-post-generator.modal.run 
Accessibile da: chiunque con il link 
Funzionalità: generare LinkedIn post nel vostro stile 
L'Interfaccia Web Risultante 
L'autore mostra l'interfaccia web generata dal deployment: 
 
INTERFACCIA WEB DEL LINKEDIN POST GENERATOR 
════════════════════════════════════════════ 
 
┌─────────────────────────────────────────────┐ 
│ Giovanni's LinkedIn Post Generator          │ 
│                                             │ 
│ Topic: [                                  ] │ 
│ "Quanto importante è utilizzare Claude Code │ 
│  nel futuro"                                │ 
│                                             │ 
│ Paste from another author: [              ] │ 
│ (opzionale)                                 │ 
│                                             │ 
│ Style: [Storytelling ▼]                     │ 
│                                             │ 
│ Include CTA: [No ▼]                         │ 
│                                             │ 
│ [    GENERATE POST    ]                     │ 
│                                             │ 
└─────────────────────────────────────────────┘ 
L'utente compila i campi, preme "Generate Post" e riceve un LinkedIn post generato nel stile 
dell'autore. Tutto avviene nel cloud, senza bisogno che il computer dell'autore sia acceso. 

--- PAGE 193 ---
Verifica del Deployment su Modal 
Dopo il deployment, l'autore verifica nella dashboard di Modal: 
"Vediamo che qui abbiamo fatto una chiamata adesso, che è l'ultima che abbiamo fatto. 
Mezzanotte, 9 secondi. Quindi vediamo che è stata chiamata." 
La dashboard mostra: 
●​
Ogni chiamata effettuata al servizio 
●​
Il tempo di esecuzione (9 secondi) 
●​
Le chiamate di inizializzazione 
●​
I log per il debugging

