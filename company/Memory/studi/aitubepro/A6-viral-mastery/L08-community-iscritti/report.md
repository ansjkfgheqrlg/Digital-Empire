# Report — A6/L08 «Fai crescere la Community e gli iscritti» (10:34)

- **Durata:** 10:34 · ~1.477 parole · **profondità ORO**
- **Letta:** parlato integrale + 9/38 frame unici (tutorial a schermo condiviso)
- **Materiale grezzo:** appunti.md nella stessa cartella · frame scelti: frame-scelti.md

---

## 1. Cosa insegna

Uso della scheda Community di YouTube Studio come canale distinto dai video: post-video con
call-to-action, sondaggi visivi/testuali per generare interazione, distribuzione dei post anche a
non iscritti in base all'interesse tematico (leva di scoperta), cross-promotion fra canali propri
specializzati per nicchia, e una regola operativa ripetuta con forza — rispondere a **tutti** i
commenti, sia sui post Community sia sui video, con un copione specifico (ringraziare, invitare a
iscriversi con campanella attiva) — più un canale Telegram esterno come leva di notifica
aggiuntiva.

## 2. Cosa facciamo oggi nella fabbrica

Verificato con grep su 02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py: zero occorrenze
di "community". Coerente con quanto gia registrato da A6-RC-01 (ripasso costruttivo del
2026-09-10), che aveva gia trovato playlist, schede, schermata finale e sottotitoli mai
automatizzati dall'uploader — ma A6-RC-01 non nominava esplicitamente la scheda Community, che è
un canale di pubblicazione a se stante, non solo un'opzione del wizard di upload. Nessuno script
pubblica post Community, sondaggi, o gestisce risposte ai commenti. Nessun canale Telegram di
notifica collegato alla pubblicazione.

## 3. Delta

Il delta e totale e concreto su quattro fronti, nessuno dei quali richiede giudizio: sono
funzionalita che oggi non esistono affatto nella fabbrica.

1. **Scheda Community non pubblicata mai**: ogni video prodotto potrebbe generare un post
   Community di annuncio (con like/commento fissato) e la fabbrica non lo fa. Il docente lo
   segnala come leva di scoperta oltre gli iscritti (parlato @ 02:50-03:00), non solo di
   engagement — quindi rilevante anche per CTR/visualizzazioni, non solo per fidelizzazione.
2. **Nessuna gestione strutturata delle risposte ai commenti**: la regola piu ripetuta della
   lezione ("rispondere a tutti i commenti [...] che io faccio su tutti i canali") non ha
   equivalente nella fabbrica — non esiste ne un agente ne uno script che presidi i commenti sui
   video pubblicati.
3. **Nessuna cross-promotion fra canali propri**: la fabbrica gestisce piu canali (vedi CANALI in
   apex7_orchestrator.py) ma non ha nessun meccanismo che usi un canale per promuoverne un altro
   via Community, come mostrato dal vivo nella lezione (frame-200.png).
4. **Nessun canale Telegram collegato**: la lezione lo presenta come leva concreta di notifica
   esterna, assente dalla catena di pubblicazione.

## 4. Conflitti

Nessuno. Il gap è di costruzione mancante, non di scelta contraria: la fabbrica non ha mai
affrontato la scheda Community come oggetto separato dal video stesso.

## 5. Regole estratte

Quattro regole, tutte costruttive (coerenti col mandato del 2026-09-10: qui non c'e un bug da
correggere, c'e un intero canale di crescita non ancora costruito). Dettaglio con prova in
regole/A6-viral-mastery/L08_community_iscritti.py.

| id | tipo | regola in una riga | azione | tocca |
|---|---|---|---|---|
| A6-L08-01 | flusso | pubblicare un post Community di annuncio per ogni video, con like e commento fissato, non solo il video stesso | costruisci | 02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py |
| A6-L08-02 | agente | manca un agente/operatore che presidi i commenti (video + community) e risponda secondo il copione del corso (ringraziare, invitare a iscriversi) | costruisci | 03-AGENTI-E-RUOLI/operatori/ (nuovo comment-responder) |
| A6-L08-03 | funzione | manca una funzione di cross-promotion Community fra i canali propri della fabbrica, usando la lista CANALI gia esistente | costruisci | 02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py |
| A6-L08-04 | strumento | canale Telegram di notifica esterno, oggi non collegato alla pubblicazione | costruisci | 04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md |

## 6. Applicabilità

Alta su tutti e quattro i punti: sono funzionalità concrete, dimostrate dal vivo nella lezione con
numeri reali (647 like, 269 commenti, 2.500 voti su un canale di due settimane), e la fabbrica ha
già l'infrastruttura di base (uploader Playwright, lista CANALI multi-canale) su cui innestarle —
non servono nuovi strumenti esterni salvo Telegram (bot gratuito, API pubblica nota). Il rischio
maggiore è A6-L08-02 (risposta commenti): tocca la voce pubblica dell'azienda verso il pubblico,
va imbrigliato con un copione fisso, non lasciato a generazione libera.
