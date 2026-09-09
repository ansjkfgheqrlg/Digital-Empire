---
Type: SOURCE
Status: Active
Tags: #trading-bot #crypto #binance #claude-code #agentic-workflow #risk-management #algorithmic-trading #giovanni-beggiato #max18
Created: 2026-09-09
Last updated: 2026-09-09
---

# Source: Giovanni Beggiato — "Ho Creato un Bot Crypto che Fa Trading 24/7 con Claude Code"

## Overview

Video di 23m37s (canale Giovanni Beggiato, run `max18-v05-RnNSRF4s9nk`) in cui l'autore costruisce
dal vivo, con Claude Code dentro l'IDE "Antigravity", un **bot di trading Bitcoin su Binance
Testnet**, dichiarando fin dal primo secondo che l'obiettivo reale non è insegnare ad arricchirsi
col trading ma mostrare un **framework replicabile in tre fasi — Comprensione del problema, Design
del sistema, Implementazione — per affrontare con l'AI qualsiasi problema concreto di cui non si è
esperti**. Il bot che ne esce è un motore **ensemble/voting a 5 indicatori tecnici non correlati**
(EMA, RSI, OBV, Bollinger Bands, ADX) con formula di risk management (2% di rischio per trade,
stop-loss 1,5×ATR, trailing stop 2×ATR), progettato con ricerca parallela di agenti ("agent
polling"), validato con un flowchart Excalidraw generato da una skill personalizzata, poi
implementato da Claude Code in **plan mode** e mandato "live" su Binance Testnet (soldi finti) con
una dashboard locale che mostra saldo, indicatori e storico trade in tempo reale. Chiude ribadendo
la tesi di apertura e con un pitch per un corso a pagamento su come scrivere prompt efficaci con
Claude Code e Codex.

## Non è un video di trading: la tesi dichiarata in apertura e ripresa in chiusura

Apertura letterale, primo secondo di parlato: *"Ho costruito un bot che fa trading di Bitcoin con
Cloudcode ed in questo video lo andremo a ricostruire insieme."* — RnNSRF4s9nk#0:00 (KA-001).
Segue immediatamente la precisazione che rovescia le aspettative: *"Però questo video non è un
video su come si diventa ricchi facendo trading di Bitcoin, non sarei qui, eh, però è piuttosto un
video su come possiamo utilizzare l'AI per affrontare qualsiasi problema concreto."* —
RnNSRF4s9nk#0:06 (KA-002). Terza frase, l'obiettivo pedagogico esplicito: *"Quindi andremo a vedere
qual è un framework che possiamo utilizzare per affrontare questo problema e come possiamo farci
guidare da questi strumenti nel caso in cui noi non siamo degli esperti nel settore."* —
RnNSRF4s9nk#0:18-0:24 (KA-003).

La stessa tesi chiude il video, con un arco esplicito codificato nel grafo (relazione dichiarata
KA-002→KA-069, "la stessa tesi apre qui e viene ripresa identica nelle considerazioni conclusive"):
*"qual è il miglior modo di costruire un bot di trading, ma quanto per capire [...] come potete
affrontare qualsiasi problema con l'AI"* — RnNSRF4s9nk#23:00-23:12 (KA-069).

## Fase 1 — Comprensione del problema: i building blocks del bot

Mappa in tre parti, disegnata su Excalidraw e usata come indice dell'intero video — tre riquadri
collegati da frecce: "COMPRENSIONE DEL PROBLEMA" (icona lampadina, "Capire cosa si vuole
risolvere"), "DESIGN DEL SISTEMA" (icona foglio da progetto, "Progettare la soluzione"),
"IMPLEMENTAZIONE" ("</>", "Costruire il sistema"): *"Questo video si dividerà in tre parti
principali. Andremo inizialmente a comprendere il problema che dobbiamo analizzare [...] Andremo
poi a definire come facciamo un design del sistema ed alla fine procederemo
all'implementazione."* — RnNSRF4s9nk#0:30-0:54 (KA-004).

Presentazione personale, prima di entrare nel merito: *"...artificiale con la quale facciamo
consulenza business che vanno dai €10.000 al mese fino ai 50 milioni di euro all'anno ed ho una
community... privata nella quale insegno a freelancer ed imprenditori come applicare l'AI in
qualsiasi business e come vendere questi servizi."* — RnNSRF4s9nk#1:00-1:18 (KA-005).

Lo schema completo a tre livelli "TRADING BOT BITCOIN SU BINANCE" — LIVELLO 1 (viola)
Monitoraggio e Alert: supervisione costante, notifiche in tempo reale, dashboard di controllo;
LIVELLO 2 (verde) Il Bot: Lettura Dati → Decisione e Gestione del Rischio → Esecuzione Ordini;
LIVELLO 3 (arancione) Fondamenta: Piattaforma Binance + Connessione API, chiuso dalla graffa
"SI CONFIGURA UNA VOLTA POI FUNZIONA IN AUTOMATICO" — RnNSRF4s9nk#1:18 e #12:54 (KA-006). Sulla
scelta di Binance, dichiarazione di trasparenza non richiesta: *"...caso useremo Binance. Non ho
alcuna associazione, non c'è uno sponsored link, faccio il video solo perché qualcuno di voi me
l'ha chiesto."* — RnNSRF4s9nk#1:30-1:42 (KA-007). Sul perché la connessione API sta nelle
Fondamenta: *"...chiavi che permettono a Cloud di accedere a o a Codex di accedere in maniera
automatica, noi non possiamo fare questa cosa qui."* — RnNSRF4s9nk#2:00-2:06 (KA-008).

Due principi guida prima ancora di aprire l'IDE. Il primo, sulla vaghezza degli ordini dati
all'AI: *"Perché dire a Claud e per favore vai e conquista il mondo non è sufficiente per Claud
conquistare questo mondo, cioè con il carro armato, con le spade o con le pistole d'acqua. Quindi
dobbiamo definire quella che è la strategia..."* — RnNSRF4s9nk#3:18-3:30 (KA-009). Il secondo,
su dove sta davvero la proprietà intellettuale: *"...Non tanti sapranno qual è la miglior
strategia per fare trading, quindi la gran parte della vostra ricerca dovrebbe essere nel decidere
qual è la strategia migliore prima ancora di capire come costruire il sistema."* —
RnNSRF4s9nk#3:48-4:00 (KA-010). L'ordine di lavoro fissato per qualsiasi problema, illustrato da
una grande freccia verde verticale sul diagramma: *"...quindi partiamo sempre da possiamo farlo,
dopo andiamo al ok, cosa facciamo e dopo è come lo monitoriamo."* — RnNSRF4s9nk#4:36-4:54
(KA-011): Fondamenta → Bot → Monitoraggio, sempre in quest'ordine.

## Come Claude decompone qualsiasi problema: la skill /diagram-generator

Obiezione anticipata dall'autore, poi risolta indicando lo strumento: *"Hey Jo, però non è sempre
chiaro qual è il problema che sto affrontando [...] non ho sempre chiaro come farlo." Bene, per
risolvere questo problema vi consiglio sempre di utilizzare uno strumento come cloud.* —
RnNSRF4s9nk#4:54-5:06 (KA-012). L'ambiente di lavoro è "Antigravity IDE" (fork di VS Code,
etichetta "Antigravity IDE - Offline" in barra di stato — RnNSRF4s9nk#5:12, KA-013), progetto
radice preesistente "Social Media Manager" dentro cui nasce la sottocartella "btc-trading-bot".

Prompt reale usato per generare lo schema a blocchi con la skill `/diagram-generator`: *"I am
trying to build a trading bot for a YouTube video. It should analyze Bitcoin candles on Binance
and figure out the best strategy to implement for trading. I would like you to draw me a diagram
showing the skills you have, targeted at non-technical people (entrepreneurs and others who do not
understand much about finance and so on)."* — RnNSRF4s9nk#5:12-5:30 (KA-014). `/diagram-generator`
è definita come skill personale dell'autore che *"genera diagrammi ad alto livello a partire da una
descrizione testuale del sistema da costruire, pensati per un pubblico non tecnico"* —
RnNSRF4s9nk#5:12 (KA-015), con un meccanismo dichiarato esplicitamente: *"...semplicemente questa è
una skill nella quale io ho detto al bot, 'Hei, quando ti do un richiesta per farmi un diagramma',
stai ad alto livello, cerca di decomporre il task in micro sezioni e dopo"* —
RnNSRF4s9nk#7:00-7:12 (KA-016) — disegna il diagramma solo alla fine.

## Fase 2 — Design del sistema: dal blocco core alla strategia ensemble a 5 segnali

Apertura letterale del secondo capitolo, scritta a mano sulla stessa lavagna: *"parte numero due è
fare il design del sistema. Allora, da dove si parte però per fare il design del sistema?"* —
RnNSRF4s9nk#7:48-7:54 (KA-017). Risposta, cerchiando in blu il riquadro "Decisione e Gestione del
Rischio": *"dal blocco che io considero il blocco core. Quindi, partiamo sempre da la nostra
strategia."* — RnNSRF4s9nk#8:00-8:06 e #11:12-11:24 (KA-018). L'autore generalizza subito il
principio oltre il trading, con due esempi concreti (marketing automation e proposal generation):
*"andiamo a fare una proposal generation, quindi che mandiamo proposte automatiche ai nostri
clienti. Gran parte del successo del sistema viene da quanto bene analizziamo i transcript e da
quanto questi possono essere convertiti in pain per il nostro cliente"* — RnNSRF4s9nk#11:12-11:54
(KA-019).

Per generare la strategia vera e propria, prompt con lo slash command `/prompt-contracts`: *"I am
building a bot on Claude Code that should trade Bitcoin on a daily basis, doing daily trades. [...]
please come up with a strategy I can use to create this bot successfully. Please know that this is
a demo and it will be run in a sandbox with fake money [...] I need you to use agent polling to
scrape and find each individual strategy my bot could use"* — RnNSRF4s9nk#8:06-8:36 (KA-020).
"Agent polling" è definita come la tecnica per cui Claude lancia più agenti di ricerca in parallelo,
ciascuno specializzato su una categoria diversa: *"I'll research trading strategies using multiple
agents in parallel, then build a prompt contract for the bot."* — con tre agenti reali lanciati,
"Research trend-following strategies", "Research mean-reversion + momentum strategies", "Research
advanced + composite strategies" — RnNSRF4s9nk#8:06 e #9:36-10:42 (KA-021).

Documento di strategia generato da Claude, "Bitcoin Daily Trading Bot -- Strategy": *"Approach:
Ensemble/Voting (5 indicators, majority rules). [...] Evaluate 5 uncorrelated signals on each daily
BTC/USDT candle. Only trade when 3+ agree on direction. Skip when signals are mixed."* —
RnNSRF4s9nk#8:06 (KA-022). I 5 segnali per intero, con soglie: *"1. EMA 50/200 Crossover --
trend direction. [...] 2. RSI(14) above/below 50 -- momentum. [...] 3. OBV slope (14-day) --
volume confirmation. [...] 4. Bollinger Band position (20, 2 std dev) -- price above middle band =
bullish, below = bearish. 5. ADX(14) > 25 -- trend strength filter. Below 25 = no trade at all (no
clear trend)."* — RnNSRF4s9nk#8:06 e #12:00 (KA-023). Motivazione della scelta, tabella
comparativa "Signal | Dimension | Fails when": *"Each covers a different dimension of market
behavior. They are uncorrelated -- when one fails, others compensate"* — EMA/Trend/mercati
laterali; RSI/Momentum/trend estesi; OBV/Volume/fakeout a basso volume; Bollinger/Volatilità/cambi
di regime improvvisi; ADX/Forza del trend/filtro di sicurezza — RnNSRF4s9nk#12:00 (KA-024).

Risk Management per intero: *"Signals flip (3+ switch direction) OR trailing stop hit (2x ATR(14)
from highest point since entry). Stop-loss: 1.5x ATR(14) below entry price. Position size: risk max
2% of capital per trade. Formula: position_size = (capital * 0.02) / (1.5 * ATR). Trailing stop: 2x
ATR(14), adjusted"* — RnNSRF4s9nk#12:06-12:36 (KA-025). Performance attese: *"Win rate: 55-60%. Risk/
reward ratio: 1:1.5. Trade frequency: low (only on strong consensus). Works across: trending,
ranging, and volatile conditions."* — RnNSRF4s9nk#12:06 (KA-026). Motivazione contro l'uso di un
singolo indicatore, sezione "Why This Over 20 Other Strategies": *"RSI alone: 52-58% win rate but
only in ranging markets, destroyed in trends"* [...] *"EMA crossover alone: 35-42% win rate, great
R:R but constant whipsaws in ranges"* [...] *"ranges, mean reversion signals (RSI, Bollinger)
dominate. No regime detection needed — the voting handles it."* — RnNSRF4s9nk#12:06-13:18
(KA-027). Stack tecnico dichiarato: *"ccxt -- Binance Testnet API (testnet.binance.vision).
pandas + pandas-ta -- indicator calculations. python-dotenv -- API keys from environment. Both
backtest mode (historical candles) and live mode (daily polling)."* — RnNSRF4s9nk#13:06-13:30
(KA-028).

## Visualizzare l'architettura: la skill Excalidraw e la validazione del flowchart

Per generare il flowchart, Claude Code legge prima la skill Excalidraw ("Let me read the excalidraw
skill first"), crea `.tmp/btc_daily_trading_bot.excalidraw`, poi applica colori pastello con
`python3 .claude/skills/excalidraw-flowchart/colorize.py` — file risultante da **126.738 byte
(~127KB)** — RnNSRF4s9nk#13:30-14:00 (KA-029). Riepilogo testuale dei 7 step dell'intero ciclo,
generato da Claude Code: *"1. Start -- Daily Candle Close (trigger). 2. Fetch + Calculate [...] 3.
Voting [...] 4. Decision [...] 5. Risk Management [...] 6. Monitor [...] 7. Exit -- close position
e torna a Wait Next Candle, che riporta al Daily Candle Close."* — RnNSRF4s9nk#14:00-14:30
(KA-030). Il file `.excalidraw` è JSON puro e leggibile: *"'type': 'excalidraw', 'version': 2,
'source': 'https://github.com/swiftlysingh/excalidraw-...' 'elements': [ { 'id': '7YVt5tEnTQ',
'type': 'ellipse',"* — RnNSRF4s9nk#14:30-14:36 (KA-031).

Verifica visiva del flowchart su excalidraw.com, percorso completo: dall'ellisse verde "Wait Next
Candle" → "Daily Candle Close" → "Fetch BTC/USDT Daily Candle" → "Calculate Indicators" —
RnNSRF4s9nk#14:42-15:12 (KA-032) — poi i cinque box degli indicatori affiancati ("EMA 50/200
Crossover", "RSI 14", "OBV Slope 14d", "Bollinger Band 20,2", "ADX 14") confluenti in "Collect
Votes" — RnNSRF4s9nk#15:06-15:18 (KA-033) — primo rombo di decisione: *"E ora ci chiediamo se
questo è sopra a 25, che sarà molto probabilmente il nostro eh livello di thold sopra il quale
magari compriamo o sotto vendiamo."* — RnNSRF4s9nk#15:42-15:54 (KA-034) — routing su "3+ Bullish?"
/"3+ Bearish?" verso OPEN LONG / OPEN SHORT / HOLD — RnNSRF4s9nk#16:12-16:24 (KA-035) — chiusura
del ciclo su "Signals Flipped?"/"Trailing Stop Hit?" → Close Position o Update Trailing Stop → Wait
Next Candle, che torna a Daily Candle Close — RnNSRF4s9nk#16:42-16:54 (KA-036). Il senso di
percorrere l'intero diagramma, dichiarato esplicitamente: *"questa è la fase di validazione
dell'architettura e questo è quello che vogliamo fare, no? Perché noi vogliamo assicurarci che la
nostra architettura sia corretta."* — RnNSRF4s9nk#16:42-17:00 (KA-037).

## Dal design al piano: sintetizzare tutto in un prompt per il plan mode

Una volta validata l'architettura: *"perfetto, sintetizzami tutto in un prompt e includi anche
tutta la strategia che ti ho incollato, in modo tale che io possa andare ora in una nuova sessione
di Claude Code e incollartela in plan mode ed assicurarmi che Claude poi vada ad implementare il
mio sistema"* — RnNSRF4s9nk#17:00-17:24 (KA-038). Menu "Slash Commands" della toolkit personale
dell'autore, lista completa: `/pre-mortem` (selezionato), `/prompt-contracts`, `/loop`,
`/reverse-prompting`, `/step-back-prompting`, `/fewer-permission-prompts`, `/skool-video-upload`,
`/audit`, `/deploy-check`, `/contract` — RnNSRF4s9nk#17:24-17:36 (KA-039).

Sezione "## Implementation Order" del prompt sintetizzato, lista numerata completa: *"1. config.py
+ data.py [...] 2. indicators.py [...] 3. strategy.py [...] 4. risk.py [...] 5. backtest.py +
report.py [...] 6. executor.py [...] 7. bot.py [...] 8. monitor.py [...] 9. End-to-end test -- run
on testnet for several days, verify orders execute correctly."* — RnNSRF4s9nk#17:36 (KA-040).
Sezione "## Constraints", non negoziabile: *"Python 3.9+ compatible [...] All API keys from .env,
never hardcoded. Testnet only — never connect to production Binance without explicit confirmation.
Each module must be independently testable. Backtest must run before any live trading."* —
RnNSRF4s9nk#17:36 (KA-041). Istruzione d'uso allegata: *"Copia-incolla tutto in una nuova sessione
di Claude Code in plan mode. Claude ti proporrà il piano di implementazione step-by-step, tu approvi
e lui costruisce."* — RnNSRF4s9nk#17:36 (KA-042). Prima dell'invio, in coda al prompt vengono
aggiunti a mano due segnaposto ancora vuoti: *"Credenziali Binance: - API: - Link per vedere
candele:"* — con l'etichetta "Plan mode" attiva accanto al pulsante d'invio — RnNSRF4s9nk#18:12-19:06
(KA-043).

## Fase 3 — Connessione API a Binance: come si crea (e si protegge) una chiave

Apertura del capitolo, lasciando l'IDE per il sito reale: *"Quindi come facciamo ad autenticarci
nella piattaforma Binance e quindi da qui poi vedremo come come si fa e dove andiamo a prendere i
dati delle candele."* — RnNSRF4s9nk#18:12-18:18 (KA-044). Percorso seguito: *"API management sotto
la sezione account e qui abbiamo create API system generated e quindi label API YouTube bot."* —
RnNSRF4s9nk#18:12-18:48 (KA-045). Binance blocca la creazione finché non sono completate 2
verifiche di sicurezza su 2: *"Security verification requirements. You need to complete. Ok, va
bene. Ora mi autenticherò."* — RnNSRF4s9nk#18:48-18:54 (KA-046).

Regola centrale sulla chiave reale creata: ha **solo il permesso "Enable Reading" attivo**, tutti
gli altri (Universal Transfer, Spot & Margin Trading, Withdrawals, Margin Loan/Repay & Transfer,
Prediction Trading, Symbol Whitelist) restano disattivati, accesso IP "Unrestricted (Less Secure)"
— RnNSRF4s9nk#18:54-19:00 (KA-047). Avviso di sicurezza mostrato in rosso da Binance stessa: *"This
API Key allows access from any IP address. This is not recommended."* e *"To protect the safety of
your funds, if the IP is unrestricted and any permission other than Reading is enabled, this API
key will be deleted."* — Binance cancellerebbe automaticamente la chiave se, con IP non ristretto,
venisse attivato un permesso diverso dalla sola lettura — RnNSRF4s9nk#18:54-19:06 (KA-048). Per
trovare la documentazione delle candele: *"...potete o chiedere a Cloud di andare e ed esplorare
l'universo, oppure potete andare in questo link qui [...] developerinance.com [...] Come l'ho
trovata? Ovviamente l'ho trovata utilizzando Cloud"* — RnNSRF4s9nk#19:18-19:36 (KA-049).

Blocco finale completato e inviato dentro il prompt di plan mode (chiavi mascherate come nella
fonte, mai riportate per intero in questo documento): API `F4q6…tqJi`, Secret `bfwU…M9cD`, link
`https://developers.binance.com/docs/binance-spot-api-docs`, chiuso dal promemoria esplicito di
sicurezza: *"Per favore ricordati che, per questo bot, vorrei farlo funzionare utilizzando soldi
falsi e quindi in sandbox, ok?"* — RnNSRF4s9nk#19:30-20:12 (KA-050).

## Go live: il bug delle chiavi rifiutate e il bot in esecuzione su Testnet

Prova tangibile che l'implementazione è partita: la cartella "btc-trading-bot" appare nel Finder
macOS, *"la cosa che possiamo fare è ora premere plan mode e aspettare che tutto questo venga
implementato."* — RnNSRF4s9nk#20:12-20:30 (KA-051). Struttura di progetto Python generata:
`__pycache__`, `.claude`, `.pytest_cache`, `.tmp`, `.venv`, `data`, `src`, `tests`, `.env`,
`.gitignore`, `CLAUDE.md` — RnNSRF4s9nk#20:12-20:30 (KA-052).

Secondo `/prompt-contracts`, per chiarire cosa significa "andare live": *"please put this bot live.
What does that mean? I should be able to see the trades in my Binance account. [...] If you don't
know how to do it, use agent polling"* con l'annotazione manoscritta *"always fake money ofc"* —
RnNSRF4s9nk#20:12-20:30 (KA-053). Claude propone un "Contract" formale prima di eseguire: *"Got it
-- fake money only, always. Here's the contract: [...] GOAL: Bot is running live on Binance Testnet
(fake money), executing real trades visible in the testnet account. Gio can see balances, orders,
and trade history at testnet.binance.vision."* — RnNSRF4s9nk#20:12-20:30 (KA-054) — i percorsi file
a schermo rivelano il nome utente reale dell'autore, "giovannibeggiato", e Claude lo chiama "Gio"
(KA-055).

Sulla lavagna Excalidraw compare la terza voce, "3. Implementazione": *"il bot perché fino ad ora
che cosa abbiamo fatto? Abbiamo semplicemente creato la nostra infrastruttura [...] Però una volta
finita l'implementazione [...] abbiamo la parte di go live."* — RnNSRF4s9nk#20:30-20:42 (KA-056).
Prima di eseguire "put this bot live", Claude Code fa domande di chiarimento invece di agire alla
cieca: *"quick questions: 1. Is the bot live? 2. Is it connected and already taking things live, or
do I need to deploy it? [...] Want to tweak the strategy parameters before starting the live bot,
or are you good with running it as-is on testnet?"* — RnNSRF4s9nk#20:42-21:12 (KA-057).

Al primo avvio, bug reale: *"Good news: the connection to testnet.binance.vision is working
(correct URL). Bad news: the API keys are rejected -- 'Invalid API-key, IP, or permissions for
action.' [...] This usually means the testnet keys expired or were regenerated. You need to get
fresh ones"* — RnNSRF4s9nk#21:00-21:30 (KA-058). La chiave Spot creata su binance.com (KA-047)
risulta insufficiente: serve una chiave distinta generata direttamente su testnet.binance.vision.
Lista completa fornita da Claude: *"1. Go to https://testnet.binance.vision. 2. Log in with GitHub.
3. Click 'Generate HMAC_SHA256 Key'. 4. Copy the new API Key and Secret Key. 5. Give them to me and
I'll update the .env and start the bot."* — RnNSRF4s9nk#21:12-21:36 (KA-059). Alla richiesta di
Claude di recuperare da solo le chiavi, l'autore prima chiede *"you cando all alone right?"* poi
decide di farlo lui stesso davanti al pubblico invece di lasciare che sia l'AI a operare il browser
in autonomia — RnNSRF4s9nk#21:30-22:06 (KA-060).

Sul sito testnet.binance.vision, nome "YouTube bot" con i tre permessi di default lasciati spuntati:
*"TRADE — Can place/cancel orders. USER_DATA — Can view account information and query trades/orders
of the user. USER_STREAM — Can subscribe to the User Data Stream"* — RnNSRF4s9nk#21:36-21:54
(KA-061). Conferma: *"HMAC-SHA-256 Key registered"* con l'avviso *"Save these values right now.
They won't be shown again!"* — chiavi Testnet, denaro finto, ma comunque mai trascritte carattere
per carattere in questo documento (KA-062). L'autore incolla lui stesso le chiavi nel box di Claude
Code e preme il pulsante rosso "Bypass permissions" per proseguire senza altre conferme manuali —
RnNSRF4s9nk#22:06-22:24 (KA-063).

Header della dashboard locale del bot (`localhost:8501`): "₿ BTC Trading Bot", "BINANCE SPOT
TESTNET", indicatore verde "LIVE"; quattro metriche — USDT BALANCE **$10.000,00**, BTC HOLDINGS
**1,0000 BTC**, BTC/USDT **$77.440,79**, TOTAL PORTFOLIO **$87.440,79** (coerente:
10.000 + 1×77.440,79) — RnNSRF4s9nk#22:24-22:36 (KA-064). Sezione "Bot Status & Signals": badge
"Waiting for signal (ADX too low)", Signal "HOLD", griglia indicatori live (EMA FAST 76.767,29 /
EMA SLOW 84.707,42, RSI 47,04 / OBV SLOPE -53290,37, BB MID 79.058,66 / ADX 19,87, ATR 2.034,08),
confermata dal log: *"STATUS | capital=10000.00 | position=1.000000 | signal=HOLD | [...] |
adx=19.87 | atr=2034.08"* e *"Sleeping 46718s until next daily candle..."* — RnNSRF4s9nk#22:24-22:36
(KA-065). Tabella "Trade History", 6 transazioni simulate su 3 taglie (0,0010 / 0,0020 / 0,0030 BTC)
in coppie BUY/SELL consecutive attorno a $77.446 — RnNSRF4s9nk#22:24-22:36 (KA-066).

Chiarimento finale sulla differenza fra demo e realtà: *"[il testnet] dashboard visiva, ma se invece
poi voi andrete ad utilizzare la dashboard di Binance con soldi veri, allora potrete entrare
nell'interfaccia principale e vedere proprio le vostre trade, come se stesse facendo trading voi in
prima persona."* — RnNSRF4s9nk#22:36-23:00 (KA-067). Nota di trasparenza sul dato: il nome
descrittivo pronunciato a voce ("YouTube bot") non coincide col nome effettivamente registrato in
piattaforma ("Youtube_Bot_2"), probabile normalizzazione automatica o numerazione di un tentativo
precedente — RnNSRF4s9nk#22:42 (KA-068).

## Chiusura: la tesi ripresa, il metodo in tre step, il pitch finale

Chiusura in webcam a schermo intero, tesi ribadita: *"qual è il miglior modo di costruire un bot di
trading, ma quanto per capire [...] come potete affrontare qualsiasi problema con l'AI"* —
RnNSRF4s9nk#23:00-23:12 (KA-069). Riepilogo esplicito del metodo generale: *"chiarificando il
problema che andrete a fare, zoomando indietro, avendo una visione di alto livello, poi andando
[...] dentro e definendo più o meno una struttura architetturale e solo a quel punto procedere con
l'implementazione."* — RnNSRF4s9nk#23:12-23:24 (KA-070) — gli stessi tre step di KA-011
(Fondamenta→Bot→Monitoraggio), ricondensati. Ponte verso il pitch: *"Questi tre step però non sono
[...] sufficienti se non sapete come scrivere prompt [efficaci] con cloud"* — RnNSRF4s9nk#23:24-23:30
(KA-071). Chiusura commerciale: *"fatto un corso completo che vi lascio qua sopra nel quale vi porto
da beginner [...] a completi esperti in come scrivere prompt di successo con Cloud Code e con
Codex. Yeah."* — nessun prezzo o URL pronunciato, richiamo puramente visivo — RnNSRF4s9nk#23:30-23:36
(KA-072).

## Cosa ne ricava Digital Empire

Sezione mia, dichiarata come tale: nessuna patch applicata, nessuno script toccato — perimetro
`EMP-W4K7`, Fase 1 resta solo studio. Confronto fatto leggendo file veri, con Grep, non a memoria.

**Scoperta principale — DE ha già un ecosistema che costruisce bot di trading con Claude Code, ma
su un dominio diverso**: `company/Ecosistemi/12-STREAM-S7-BOT/` (Stream S7, di Gael) esiste da
prima di questo studio e non è materiale nuovo per l'Impero. Da `company/Memory/STATO-EMPIRE.md`
(righe verificate con Grep): *"Ordine diretto di Max: metodo logico-matematico per trading
NFT/token su marketplace stile 'Magic Eden' (Solana)"* (riga 4611), con due motori di strategia già
chiusi — *"oggi 2 esistono già, memecoin e NFT, entrambe architetturalmente solide ma bocciate per
l'uso con capitale vero"* (riga 4016) — e una disciplina di sicurezza esplicita e ripetuta più
volte: *"Resta paper trading: nessuna chiave privata vera, nessuna modalità LIVE senza PASS del
gate L5"* (riga 4621), classificazione *"R&D speculativo/0€ revenue [...] finché
`report-studio.md` non viene aggiornato con expectancy positiva verificata"* (righe 4622-4624). Il
video di questo studio (`v05`) è già citato per nome nello stesso file (riga 368: *"v05 (bot crypto
trading) studiato per intero 98/98 = 100%"*) — la ripresa `EMP-W4K7.md` conferma lo stesso.

**Confronto architetturale, non solo di dominio**: [[Tool_APEX7_Core_Motore_Condiviso]] (wiki DE,
ADR-010/011) documenta perché `12-STREAM-S7-BOT` **non** è stato fuso nel motore condiviso
`11-APEX-7-CORE`: *"l'implementazione APEX-7 di `12-STREAM-S7-BOT` è più matura del motore
condiviso su assi reali — 6 gate a rubrica con 33 criteri misurabili [...], Event Bus con priorità
P0-P3/DLQ/replay [...], memory interface con lock/checkpoint/restore, gate L6→L7 self-giudicante."*
Rispetto a questo, il bot di Beggiato è una demo di 23 minuti senza gate formali: nessun "Contract"
di sicurezza verificato da un self-giudizio, nessun event bus con priorità/DLQ, un solo test
manuale (guardare la dashboard). **Su architettura e disciplina di produzione, DE non ha nulla da
imparare da questo video** — il proprio sistema, sullo stesso genere di problema, è già più
rigoroso.

**Cosa il video aggiunge davvero, verificato assente in DE**: due comandi slash dell'autore,
`/diagram-generator` e `/prompt-contracts` (KA-014, KA-020, KA-038-043), non esistono come skill
proprie di Digital Empire — verificato con Grep su `.claude/skills/*/SKILL.md` (172 skill
censite): nessun file `diagram-generator` o `prompt-contracts`, i soli riscontri dei due termini
nel repo sono dentro archivi di conoscenza già ingeriti di **altri** video dello stesso autore
(`.claude/skills/empire-studio/runs/run-20260609T213405/`, `.claude/skills/memory-empire/knowledge/
B4i1qV0LiMw/`), mai come skill DE. Il meccanismo di `/diagram-generator` — *"stai ad alto livello,
cerca di decomporre il task in micro sezioni e dopo"* disegna il diagramma (KA-016) — è un pattern
concreto e piccolo che manca dove DE ne avrebbe uso immediato: [[Tool_Nerve_Solve_Orchestration_Layer]]
(NERVE-SOLVE) codifica un metodo di problem-solving assai più ricco (fasi P-1→P12, depth-router
D0-D3) ma non produce un diagramma visivo per interlocutori non tecnici — un gap piccolo, dichiarato
qui, non chiuso.

Il pattern `/prompt-contracts` — un "Contract" testuale con GOAL/CONSTRAINTS/FORMAT che Claude
propone e l'utente approva prima di un'azione rischiosa (KA-054, *"Got it -- fake money only,
always. Here's the contract"*) — è concettualmente vicino ma non identico al gate L5 di Stream S7
(un controllo automatico, non una conferma testuale in linguaggio naturale): un'ibridazione fra i
due (contract leggibile + gate automatico) è un'idea non ancora scritta in nessun documento DE
verificato.

**Cosa DE ha già, in sostanza indipendente**: la disciplina "chiave API con solo permesso di
lettura, mai scrivere credenziali reali nel prompt" (KA-047, KA-050) è lo stesso principio del
"nessuna chiave privata vera" di Stream S7 (riga 4621 STATO-EMPIRE.md) — conferma indipendente,
non un gap. Il reparto **Tesoreria** (`.claude/skills/tesoreria/SKILL.md`,
`.claude/agents/tesoreria-conductor.md` + `-entrate/-spese/-report/-previsione.md`, verificato con
Glob) esiste ma governa i conti reali dell'azienda, non il trading: tema adiacente (finanza + AI +
Claude Code) ma dominio non sovrapposto — nessun collegamento operativo da fare, solo la stessa
famiglia di argomento già coperta con più profondità dal video gemello
[[sources/Source_Giovanni_Beggiato_CFO_AI_Claude]] (stesso autore, stesso principio "il codice fa i
conti, l'AI li interpreta").

**Cosa non ho verificato**: se le formule di risk management di questo video (2% di rischio per
trade, stop-loss 1,5×ATR, trailing stop 2×ATR — KA-025) siano già presenti nel codice
`risk_manager.py` di `12-STREAM-S7-BOT` in forma equivalente o diversa — il file esiste (verificato
con Glob) ma non l'ho aperto: il dominio NFT/token non usa candele OHLC con ATR nello stesso modo
di uno spot-trading su Binance, quindi la formula potrebbe non essere applicabile as-is. Domanda
aperta, non chiusa qui, coerente col perimetro Fase 1 = solo studio.

## Connessioni

- [[tools/Tool_APEX7_Core_Motore_Condiviso]] — il motore di orchestrazione condiviso di DE
  (ADR-010/011) che documenta perché il bot di trading reale dell'Impero (`12-STREAM-S7-BOT`, Gael,
  NFT/token su Solana) è **più rigoroso** architetturalmente della demo di questo video: 6 gate a
  rubrica, Event Bus con DLQ/replay, gate L6→L7 self-giudicante — il confronto diretto più urgente
  di questa pagina.
- [[tools/Tool_Nerve_Solve_Orchestration_Layer]] — il sistema DE di problem-solving generico
  (fasi P-1→P12), il corrispettivo strutturalmente più ricco del framework a 3 fasi (Comprensione →
  Design → Implementazione) che questo video insegna in miniatura; manca però l'equivalente di
  `/diagram-generator` per output visivi non tecnici, gap dichiarato sopra.
- [[sources/Source_Giovanni_Beggiato_CFO_AI_Claude]] — stesso autore, stesso batch tematico
  "AI + soldi + Claude Code" (batch `max17`): il CFO AI applica la stessa disciplina di questo
  video (separare calcolo deterministico da interpretazione AI, cancello anti-invenzione) al
  dominio delle finanze aziendali invece del trading — utili lette insieme per vedere lo stesso
  autore applicare lo stesso rigore a due problemi diversi.
- [[sources/Source_Giovanni_Beggiato_Second_Brain_Obsidian_Claude]] — stesso autore, stesso lotto
  `max18`: quel video insegna a costruire una company brain da zero, questo un bot di trading;
  nessuna sovrapposizione di contenuto, ma la stessa metodologia di fondo (dare a Claude Code
  struttura e vincoli espliciti prima di lasciarlo costruire).

