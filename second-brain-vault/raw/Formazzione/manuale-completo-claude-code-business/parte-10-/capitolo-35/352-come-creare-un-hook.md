# 35.2 — Come Creare un Hook

Definizione del Concetto 
La creazione di un hook richiede di definire quale evento deve attivarlo e quale azione deve 
eseguire. Il processo è semplice e può essere fatto tramite un prompt a Claude Code. 
Esempio Pratico dalla Guida — L'Hook Sonoro 
L'autore crea un hook in tempo reale durante la guida: 
text 
"Ehi, mi farebbe piacere che tu ora creassi un hook.  
Sostanzialmente quello che voglio sentire è un suono,  
tipo un chime, ogni volta che Claude finisce di fare  
un'attività. Questo mi servirebbe perché quello che  
succede è che io tendo a perdere un po' di tempo  
perché non mi accorgo che Claude finisce di fare una  
task. Quindi vorrei avere una clue uditiva." 
Claude: 
1.​ Comprende la richiesta 
2.​ Crea lo script che produce il suono 
3.​ Configura l'hook nel settings.json 
4.​ L'hook è immediatamente operativo 
Il risultato è che da quel momento in poi, ogni volta che Claude completa una task, si sente un 
suono "glass" (un tintinnio). L'autore lo testa con un semplice prompt ("Come stai?") e conferma 
che il suono si attiva correttamente alla fine della risposta. 
La Struttura Tecnica di un Hook 
Sebbene l'autore crei l'hook tramite prompt (senza scrivere codice manualmente), è utile capire 
cosa succede dietro le quinte: 
text 
STRUTTURA DI UN HOOK 
════════════════════ 
 
1. EVENTO TRIGGER (cosa lo attiva): 
   └── "Quando Claude finisce un'azione" 
   └── Oppure: "Quando Claude sta per modificare un file" 
   └── Oppure: "Quando una sessione inizia" 
   └── Oppure: "Quando un tool viene chiamato" 
 
2. SCRIPT (cosa esegue): 
   └── Un file script (bash, Python, etc.) 

--- PAGE 174 ---
   └── Es: script che riproduce un suono 
   └── Es: script che invia un'email 
   └── Es: script che avvia un altro workflow 
 
3. CONFIGURAZIONE (dove è definito): 
   └── Nel file .claude/settings.json 
   └── Associa l'evento allo script 
Tipologie di Hook per Evento 
Tipo di Evento 
Quando Scatta 
Esempio di Uso 
Post-tool 
Dopo che Claude usa un tool 
Suono di notifica 
Pre-tool 
Prima che Claude usi un tool 
Validazione di sicurezza 
Post-session 
Alla fine di una sessione 
Salvataggio automatico del log 
Post-edit 
Dopo una modifica a un file 
Backup automatico del file 
Custom event 
Quando un'azione specifica avviene 
Invio email, avvio workflow

