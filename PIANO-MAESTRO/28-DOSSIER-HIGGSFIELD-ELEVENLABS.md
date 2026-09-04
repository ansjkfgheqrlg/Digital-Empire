---
Type: SOURCE
Status: Active
Tags: #tool #video #voce #acquisto #higgsfield #elevenlabs #outreach
Created: 2026-09-04
Last updated: 2026-09-04
Autore: Emperator (per Max)
---

# Dossier 28 — Higgsfield + ElevenLabs: studio a fondo e piano d'acquisto

> Studio condotto entrando sui siti veri (Playwright, DOM renderizzato) piu' ricerca
> incrociata sul web. Le pagine prezzi di entrambi sono SPA: il fetch semplice le vede
> vuote, per questo i listini qui sotto vengono dal DOM reale, non da articoli di terzi.
> Dove il numero viene da una fonte terza, e' scritto.

---

## 0. VERDETTO IN CINQUE RIGHE

1. **Higgsfield va comprato.** Ma non per il motivo che pensi tu: **non sostituisce Fliki** sui video YouTube lunghi (fa clip da massimo 15 secondi). E' una fabbrica di video promo e di immagini, ed e' fortissima li'.
2. **Il problema dei video YouTube non e' Fliki.** Nei log dell'ultimo lotto ci sono **21 fallimenti dello stesso identico tipo**, e non vengono dai server di Fliki: vengono da un nostro gate, `quality_gate.py:93`. Stiamo dando la colpa a un fornitore per un blocco che ci siamo messi in casa da soli.
3. **ElevenLabs va comprato**, piano Creator. Voci ottime, clonazione professionale, licenza commerciale.
4. **Le chiamate a freddo automatiche in Italia, come le hai descritte, oggi non si possono fare.** Legge 49/2026 (opt-in dal 19 giugno) piu' AI Act art. 50 operativo dal 2 agosto. Il flusso si costruisce lo stesso, ma su chi ci ha gia' risposto, non a freddo. Dettaglio al paragrafo 3.4.
5. **Sui caroselli ti do' torto, con i numeri**: un carosello da 10 slide su Higgsfield costa **€0,78**. Continuare a combattere con Arena gratis costa piu' di 78 centesimi di tempo tuo e mio.

---

# PARTE 1 — HIGGSFIELD

## 1.1 Cos'e' davvero

Non e' un modello: e' un **negozio con oltre 30 modelli sotto un solo abbonamento e un solo
sistema di crediti**. Dentro ci sono Sora 2, Veo 3.1, Kling 3.0, Seedance 2.0 e 2.5, Wan 3.0,
Minimax Hailuo, Nano Banana Pro, FLUX.2, GPT Image. Fondata da ex Google Brain.

Il valore non e' la qualita' del singolo modello (quella e' di Google, ByteDance, OpenAI):
e' **non dover pagare sei abbonamenti separati**, piu' uno strato di controllo registico
(oltre 70 preset di camera: crash zoom, dolly, crane, FPV, bullet time) e di consistenza del
personaggio (Soul ID: definisci un volto da una reference e resta lo stesso attraverso luci,
angoli e stile).

Moduli: Image, Video, Audio, Edit, **Cinema Studio 4.0**, **Marketing Studio**, Viral Presets,
**MCP e CLI**, **Supercomputer**, Canvas, Plugins.

## 1.2 Listino reale (verificato sul sito, 2026-09-04, in EURO)

Promo attiva adesso: **30% di sconto sull'annuale**.

| Piano | Mensile | Annuale | Crediti/mese | Costo per credito | Job paralleli |
|---|---|---|---|---|---|
| Free | €0 | — | limitato (150/mese, fonte terza) | — | 1 video / 1 img |
| **Starter** | €19 | €19 (nessuno sconto) | **270** fissi | €0,070 | 2 video / 4 img |
| **Plus** | €59 | **€47** (risparmi €144/anno) | **1.200** fissi | €0,039 | 6 video / 8 img |
| **Ultra** | €129 | **€99** (risparmi €360/anno) | **3.000** (scalabile a 6.000 e 9.000) | €0,033 | 8 video / 8 img |

Prezzi IVA esclusa. Crediti extra a pacchetto: circa 20 crediti per 1 dollaro (**$0,05 al
credito**), cioe' **piu' cari dell'abbonamento** — i pacchetti servono per l'emergenza, non per
la produzione. Da fonte terza: i crediti top-up **scadono dopo 90 giorni**.

### Sbarramento importante
**Starter NON accede a Seedance 2.0 e 2.5.** Nessun accesso, non "meno crediti". Se vuoi la
qualita' cinematografica seria, il piano minimo e' **Plus**.

## 1.3 Tabella crediti — quanto costa davvero una generazione

Estratta dal comparatore del sito. Riporto solo cio' che ci serve.

**VIDEO (per clip)**

| Modello | Costo | Note |
|---|---|---|
| Kling 3.0 720p | 7 cr / 5s | il cavallo da lavoro |
| **Kling 3.0 1080p** | **8 cr / 5s** | **miglior rapporto qualita'-prezzo di tutto il listino** |
| Kling 3.0 4K | 30 cr / 5s | |
| Kling Omni 3 Image Reference 1080p | 7 cr / 5s | parte da una tua immagine |
| Seedance 2.0 1080p | 45 cr / 5s | top di gamma realismo |
| Seedance 2.0 4K | 110 cr / 5s | |
| Seedance 2.0 Fast 720p | 17 cr / 5s | |
| Seedance 1.5 1080p | 7 cr / 5s | economico e decente |
| Google Veo 3.1 1080p | 29 cr / 4s | |
| Google Veo 3.1 Fast 1080p | 11 cr / 4s | |
| Sora 2 720p | 10 cr / 4s | |
| Sora 2 Pro 1080p | 50 cr / 4s | |
| Wan 3.0 1080p | 27,5 cr / 5s | |
| Minimax Hailuo 2.3 1080p | 10 cr / 6s | |

**IMMAGINI (per immagine)**

| Modello | Costo | A cosa serve |
|---|---|---|
| **Higgsfield Soul 2.0** | **0,12 cr** | fotorealismo persone — praticamente gratis |
| Higgsfield Soul | 0,25 cr | |
| Reve | 0,25 cr | |
| Wan 2.2 | 0,5 cr | |
| Nano Banana / Seedream / GPT Image / FLUX.2 Pro | 1 cr | |
| **Nano Banana Pro** | **2 cr** | **il migliore per il testo dentro l'immagine, quindi caroselli** |
| Nano Banana Pro 4K | 4 cr | |
| Multi Reference | 1,5 cr | piu' immagini di riferimento insieme |
| Face Swap / Character Swap | 2 cr | |

**LIPSYNC E PARLATO**

| Modello | Costo |
|---|---|
| Higgsfield Speak 2.0 720p | 14 cr / 5s |
| Kling Speak 720p | 2 cr / 2s |
| Wan 2.5 Speak 720p | 12 cr / 5s |
| Infinite Talk 720p | 12 cr / 2s |
| Sync Lipsync 3 4K 30FPS | 18 cr / 2s |

## 1.4 Come funziona "Unlimited" — la parte che quasi nessuno legge

Non e' "generi quanto vuoi su tutto". E':

- Ogni piano sblocca un **numero di modelli in modalita' unlimited**: Starter 3, Plus 7, Ultra 7 (con i modelli di punta migliori).
- Ogni modello ha una **finestra temporale**: la maggior parte 365 giorni, i modelli di punta appena usciti (Kling 3.0, Nano Banana 2, Nano Banana Pro) **7 giorni**.
- **Starter non ha unlimited su Kling 3.0, Nano Banana 2 e Nano Banana Pro.** Plus li ha; Ultra aggiunge Nano Banana Pro a 2K.
- L'unlimited gira su **coda rilassata**: 1 immagine, 1 video e 1 audio alla volta, e la velocita' **cala nelle ore di punta**. I crediti invece vanno sempre in **coda prioritaria**.
- **L'unlimited esiste SOLO su higgsfield.ai.** Non funziona su MCP, CLI, Canvas o Supercomputer. Li' si pagano crediti, sempre.
- **I Termini vietano l'automazione sull'unlimited**: possono limitare, sospendere, rallentare o mettere in coda lenta l'uso "automated or materially exceeds typical individual use". L'unlimited e' riservato all'uso personale umano; scripting, condivisione credenziali e rivendita sono fuori. Le soglie numeriche non le pubblicano.

**Conseguenza operativa, e va rispettata:** l'unlimited si usa **a mano, io o tu davanti al
browser**, in sprint. L'automazione vera passa da MCP, CLI o API **a crediti**, che e'
pienamente legittimo. Non si scripta l'unlimited: e' il modo piu' veloce per farsi chiudere
l'account.

## 1.5 MCP e CLI — questo cambia il gioco per noi

Higgsfield espone un server MCP ufficiale. Installazione su Claude Code:

```
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

Autenticazione OAuth dal browser, nessuna chiave da gestire. Da quel momento **io genero
immagini e video direttamente da qui**, dentro il flusso di lavoro, senza che tu apra un sito.
Supporta: immagini fino a 4K, video fino a 15 secondi, training del personaggio, prompt da
testo o da immagine, accesso allo storico. Esiste anche una CLI per Claude Code e Codex.

Limiti da sapere: **niente unlimited via MCP** (solo crediti) e **nessun tetto di spesa nativo**
— il freno lo mette l'istruzione all'agente. Regola nostra: mai una generazione sopra i 50
crediti senza tuo via libera esplicito.

## 1.6 API Cloud (cloud.higgsfield.ai)

Canale separato dall'abbonamento, per l'automazione industriale. Autenticazione Bearer token,
asincrona (invio, request ID, poi polling o webhook), SDK Python e TypeScript. Modalita':
Text-to-Video, Image-to-Video, Soul Mode.
**Attenzione:** i file di output restano scaricabili **almeno 7 giorni** — vanno portati subito
in casa nostra. Tariffa indicativa da fonte terza: circa $0,10 per secondo di video generato.

## 1.7 Supercomputer e Canvas

- **Supercomputer**: un agente che gira Higgsfield da capo a fondo dentro una chat, con job in parallelo. Accessibile da Starter in su. Una lavorazione completa costa circa 200 crediti (circa €8 su Plus).
- **Canvas**: pipeline visuali salvabili come template riutilizzabili tra campagne. E' li' che si costruisce una volta lo stampo "video promo Digital Empire" e poi lo si ricicla.

## 1.8 Cosa Higgsfield NON fa — leggi questo prima di comprare

- **Non fa video lunghi.** Il tetto e' circa 15 secondi per clip. Un video YouTube da 10 minuti andrebbe assemblato da 40-120 clip: costo e tempo fuori scala. **Non e' un sostituto di Fliki.**
- **Non fa montaggio narrativo lungo.** Fa il girato, non il film.
- **L'unlimited non e' automatizzabile** (paragrafo 1.4).
- **Non ha tetto di spesa nativo** su MCP e CLI.

---

# PARTE 2 — ELEVENLABS

## 2.1 Listino reale (verificato sul sito, 2026-09-04, in DOLLARI)

Annuale uguale a **2 mesi gratis (circa 17%)** su tutti i piani a pagamento.

| Piano | Mensile | Annuale (equiv.) | Crediti/mese | Minuti TTS | Clonazione | Licenza commerciale | Richieste concorrenti |
|---|---|---|---|---|---|---|---|
| Free | $0 | — | 10.000 | ~10 | Instant (2 slot) | **NO** | 2 |
| Starter | $6 | $5 | 30.000 | ~30 | Instant (2 slot) | SI | 3 |
| **Creator** | **$22** (1° mese $11) | **$18,33** | **121.000** | **~121** | **Professional (1)** | SI | 5 |
| Pro | $99 | $82,50 | 600.000 | ~600 | Professional (1) | SI | 10 |
| Scale | $299 | $249 | 1.800.000 | ~1.800 | Professional (3), 3 postazioni | SI | 15 |
| Business | $990 | $825 | 6.000.000 | ~6.000 | Professional (10), 10 postazioni | SI | 25 |

74 lingue su tutti i piani. Qualita' audio: 128 kbps da Free e Starter, **192 kbps piu'
WAV/PCM 44,1 kHz da Pro in su**. Il minuto extra costa circa $0,18 su Creator e $0,17 su Pro.

**La licenza commerciale parte dal piano Starter.** Sul Free non si puo' pubblicare nulla.

## 2.2 Quanto consuma ogni prodotto (fonte: help center e documentazione)

| Prodotto | Consumo |
|---|---|
| Text to Speech | **1 credito per carattere** (circa 1.000 caratteri = 1 minuto parlato) |
| **Voice Changer (speech-to-speech)** | **1.000 crediti al minuto** |
| Voice Isolator | 1.000 crediti al minuto |
| Speech to Text | 330 crediti al minuto |
| Eleven Music | 900 crediti al minuto |
| Sound Effects | 200 crediti a generazione |
| Doppiaggio automatico | 2.000/min con watermark, 3.000 senza |
| Dubbing Studio | 5.000/min con watermark, 10.000 senza |

**Il link che mi hai mandato e' Speech-to-Speech, cioe' Voice Changer**: prende una tua
registrazione e la rifa' con un'altra voce **mantenendo la tua recitazione** — pause, enfasi,
ritmo. E' la cosa piu' vicina a dirigere un attore. Modello consigliato
`eleven_multilingual_sts_v2`, 29 lingue, **massimo 5 minuti per file** (sopra va spezzato),
rimozione del rumore di fondo integrata.

Per noi vale una cosa sola ma pesante: **tu reciti lo script come lo vuoi, la macchina ci mette
la voce definitiva.** Fine della voce sintetica piatta.

## 2.3 ElevenAgents — le chiamate vocali

Listino separato, verificato sul sito:

| Piano | Minuti chiamata inclusi | Chiamate concorrenti | Minuto extra | Burst |
|---|---|---|---|---|
| Free | 15 | 4 | $0,080 | $0,160 |
| Starter $6 | 75 | 6 | $0,080 | $0,160 |
| **Creator $22** | **275** | **10** | $0,080 | $0,160 |
| Pro $99 | 1.238 | 20 | $0,080 | $0,160 |
| Scale $299 | 3.738 | 30 | $0,080 | $0,160 |
| Business $990 | 12.375 | 40 | $0,080 | $0,160 |

Messaggi di testo: $0,003 l'uno. **LLM e telefonia si pagano a parte, a costo.**
LLM disponibili: Gemini 2.5 Flash ($0,0012 al minuto, irrisorio), Claude Haiku, Sonnet e Opus,
GPT-5.x. Telefonia via SIP, Twilio, Genesys e oltre 200 provider.

**Costo reale di una chiamata da 2 minuti:**
voce $0,16 + telefonia Italia circa $0,06 + LLM circa $0,002 = **circa €0,21 a chiamata**.
500 chiamate al mese da 2 minuti fanno 1.000 minuti, quindi serve **Pro ($99)**: totale
**circa €120 al mese**, cioe' **€0,24 a chiamata**. Per confronto, un teleoperatore in Italia
costa €4-8 l'ora e ne fa 15-20. Il rapporto e' circa 1 a 15.

## 2.4 Programma Startup Grants
ElevenLabs regala **12 mesi gratuiti piu' 33 milioni di caratteri** a startup che integrano gli
agenti conversazionali in un prodotto. Digital Empire, con PreventivoForge ed Empire Desk, ha
un profilo candidabile. **Vale la candidatura prima di pagare.**

---

# PARTE 3 — I QUATTRO FRONTI, UNO PER UNO

## 3.1 Video YouTube — Higgsfield NON risolve, e il problema non e' Fliki

Tu hai detto: "i video come li stiamo facendo ora non sta andando bene, problemi di server con
Fliki". Sono andato a guardare i log invece di crederti sulla parola, ed e' giusto che tu sappia
cosa c'e' dentro.

Nella memoria di produzione ci sono **21 fallimenti identici**, e dicono questo:

```
Sezioni obbligatorie dello script mancanti: HOOK, CORPO, CTA
Lo script e' troppo corto (minimo 5...)
```

Quella stringa vive in `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/quality_gate.py:93`.
**E' un nostro gate, non un server di Fliki.** Lo scrittore produce script in un formato, il gate
ne pretende un altro, e la produzione si ferma prima ancora di chiamare Fliki.

Comprare Higgsfield non toglie di mezzo questo. **Va sistemato il gate**, ed e' lavoro di
mezz'ora, non di budget. Se dopo quella mezz'ora i video ancora non escono, allora il colpevole
e' Fliki davvero e ne riparliamo con le prove in mano.

**Dove Higgsfield entra sui video YouTube:** non come motore, come **strato visivo**. Hook dei
primi 5 secondi, B-roll cinematografico al posto dello stock, stacchi tra i capitoli, intro.
Sono clip da 5 secondi, esattamente il formato in cui Higgsfield e' il migliore. Costo: 5 hook
da 5 secondi in Kling 3.0 1080p fanno 40 crediti, cioe' **€1,57**.

## 3.2 Video promo dei prodotti — QUI Higgsfield vale ogni euro

E' il caso d'uso forte. Numeri veri, su piano Plus (€0,039 al credito):

| Cosa | Modello | Crediti | Costo |
|---|---|---|---|
| Promo 30s (6 clip da 5s), primo giro | Kling 3.0 1080p | 48 | **€1,88** |
| Promo 30s con 3 tentativi per clip (realistico) | Kling 3.0 1080p | 144 | **€5,65** |
| Promo 30s premium, 3 tentativi | Seedance 2.0 1080p | 810 | €31,75 |
| Promo 30s premium, 3 tentativi | Veo 3.1 1080p | 696 | €27,30 |

**Piano Plus (1.200 crediti) = 8 video promo da 30 secondi al mese in Kling 3.0 con retake veri.**
**Piano Ultra (3.000 crediti) = 20.**

E sopra ci sono i **7 giorni di Kling 3.0 unlimited**: una settimana all'inizio del mese in cui si
produce a mano tutto il girato del mese **senza toccare un credito**, lasciando i 1.200 crediti
interi per i modelli premium dove servono davvero. E' il modo giusto di usare questo abbonamento,
e quasi nessuno lo fa.

Piu' **Soul ID**: il volto o il personaggio di Digital Empire resta identico attraverso tutte le
campagne. E' quella la differenza tra "video fatti con l'AI" e un brand.

## 3.3 Caroselli e post — qui ti do' torto, con i numeri

La tua posizione: Arena e' gratis, non sprechiamo crediti.
Il conto vero, su Plus:

| Cosa | Su Higgsfield | Costo |
|---|---|---|
| 1 carosello da 10 slide | Nano Banana Pro, 2 cr a immagine | **€0,78** |
| 30 caroselli al mese | 600 crediti | **€23,50** |
| 1 immagine fotorealistica | Soul 2.0, 0,12 cr | **€0,005** |
| 10.000 immagini Soul 2.0 | 1.200 crediti | €47 |

E il piano Plus regala in piu' **5.000 generazioni Soul 2.0 gratuite**.

Dall'altra parte Arena: gratis in denaro, ma abbiamo gia' pagato. In `caroselli - agency` ci
sono **oltre 40 script di debug e 60 screenshot** di tentativi. Captcha, modali "Terms of Use",
bottoni che cambiano, sessioni che scadono. E il risultato, parole tue: "per ora i post caroselli
fatti con l'arena non vanno bene".

**Non e' che Arena sia sbagliata. E' che stiamo pagando in tempo — la valuta piu' cara che
abbiamo — qualcosa che costa 78 centesimi.**

E sulla cosa che hai detto tu, quella che nessun flusso capisce mai: **le reference**. Hai ragione
al 100%, senza immagini allegate il carosello non viene. Higgsfield ha `Multi Reference` (1,5 cr)
e Kling Omni 3 Image Reference: li' le reference sono **un parametro dell'API**, non un upload da
fare a mano con un click che a volte non funziona. Sono deterministiche.

**La mia proposta:** Arena resta viva per l'esplorazione e per i test gratuiti — non la buttiamo,
e va comunque riparata perche' ci serve. Ma la **produzione** dei caroselli passa su Nano Banana
Pro via MCP, con le reference come parametro. Se sbaglio, l'errore ci e' costato €23 in un mese
e torniamo indietro.

## 3.4 Chiamate a freddo automatiche — leggi con attenzione

Qui devo fermarti, e ti spiego esattamente perche'.

**Cosa e' cambiato in Italia quest'anno:**

1. **Legge 49/2026, in vigore dal 19 giugno 2026.** Modifica l'articolo 51 del Codice del Consumo e introduce l'**opt-in obbligatorio**: chiamata commerciale solo con consenso preventivo, esplicito e tracciabile. Nasce sul settore energia; le fonti divergono su quanto sia trasversale agli altri settori, e questo va verificato con un legale **prima** di partire, non dopo.
2. **Registro Pubblico delle Opposizioni: copre anche le utenze aziendali.** La revoca vale sia per l'operatore umano sia per le chiamate automatiche.
3. **Il 68% dei numeri "aziendali" nelle liste e' intestato a persone fisiche** (ditte individuali, professionisti). Su quelli si applica il GDPR pieno: consenso esplicito, punto.
4. **AI Act articolo 50, operativo dal 2 agosto 2026.** Chi riceve la chiamata deve sapere **al primo contatto e dentro la conversazione** che sta parlando con un'AI e per conto di chi. Scriverlo nella privacy policy non basta.
5. **Sanzioni fino a €20 milioni o il 4% del fatturato mondiale.** E la responsabilita' e' **in solido tra mandante e contact center**: non ci si copre appaltando.

**Traduzione:** un agente vocale AI che chiama a freddo concessionari italiani presi da una
lista, senza consenso e senza dichiararsi, oggi mette a rischio l'azienda per un ritorno che non
vale la cifra. Non e' prudenza mia, e' aritmetica.

**Cosa invece si puo' fare, ed e' meglio di quello che avevi in mente.**

In Preventa abbiamo gia' una catena di consenso: WhatsApp, il concessionario risponde, e **quello
e' un contatto che ha manifestato interesse**. L'agente vocale entra li':

- **Richiamo del lead caldo** — ha risposto su WhatsApp, l'agente chiama entro 5 minuti e fissa l'appuntamento. Consenso tracciabile: c'e'.
- **Qualifica in entrata** — chi chiama noi. Zero problemi normativi.
- **Conferma e recupero appuntamenti** — rapporto contrattuale in essere.
- **Riattivazione dormienti** — contratti cessati da meno di 30 giorni, o con consenso raccolto.
- **Post-vendita e raccolta recensioni.**

Con la dichiarazione AI nei primi tre secondi ("Sono un assistente virtuale di Digital Empire") e
un opt-out immediato, questi flussi sono **in regola**. E convertono di piu' del freddo, perche'
chiami gente che ti ha gia' risposto.

**Volume realistico:** 500 richiami al mese da 2 minuti fanno **circa €120 al mese** tutto
compreso, contro circa €2.000 di un teleoperatore.

---

# PARTE 4 — COSA COMPRARE

## Raccomandazione

| Tool | Piano | Prezzo | Perche' |
|---|---|---|---|
| **Higgsfield** | **Plus, MENSILE il primo mese** | **€59** | Sotto Plus non hai Seedance. Mensile il primo mese perche' €564 bloccati su un tool mai provato sui nostri asset veri sono un rischio che non serve correre |
| **ElevenLabs** | **Creator, mensile** | **$22** (primo mese $11) | Sblocca Professional Voice Cloning, licenza commerciale e 275 minuti di agente per prototipare le chiamate |

**Mese 1: €59 piu' $11, circa €69.**
**A regime, se supera la prova: Higgsfield Plus annuale €47 al mese piu' ElevenLabs Creator
annuale $18,33 al mese, circa €64 al mese, circa €770 all'anno.**

### Il compromesso, dichiarato
C'e' **il 30% di sconto sull'annuale Higgsfield adesso**. Prendendo il mensile lo perdi. Lo
consiglio lo stesso: sconti cosi' vengono rimessi ogni due mesi da tutte queste aziende, mentre
€564 bloccati su uno strumento che potrebbe non reggere la prova sui nostri asset non tornano
indietro. **Trenta giorni di prova valgono piu' del 30%.** Se dopo il primo mese regge — e credo
che reggera' — si passa ad annuale su entrambi.

### Cosa NON comprare adesso
- **Higgsfield Ultra (€99)**: solo quando finiamo i 1.200 crediti due mesi di fila. Ultra ha senso da 20 promo al mese in su, e non ci siamo ancora.
- **Higgsfield Starter (€19)**: niente Seedance. Falso risparmio.
- **ElevenLabs Pro ($99)**: serve solo quando le chiamate superano i 275 minuti al mese. Non prima.
- **Pacchetti crediti extra**: $0,05 al credito contro €0,039 dell'abbonamento. Solo emergenze.

### Da fare prima di pagare
**Candidare Digital Empire allo Startup Grant ElevenLabs** (12 mesi gratis piu' 33 milioni di
caratteri). Se passa, ElevenLabs costa zero per un anno. Costo della candidatura: mezz'ora.

---

# PARTE 5 — IL PIANO

## Fase 0 — Prima di spendere un euro (io, oggi)
- [ ] Riparare `quality_gate.py:93`: allineare il formato che lo scrittore produce a quello che il gate pretende. **21 fallimenti aspettano questo, non un abbonamento.**
- [ ] Candidatura Startup Grant ElevenLabs.
- [ ] Preparare il test di accettazione: 3 prompt su asset veri Digital Empire, gia' scritti, pronti a partire il minuto dopo l'acquisto.

## Fase 1 — Acquisto e collegamento (tu piu' io, giorno 1)
- [ ] Tu: Higgsfield **Plus mensile** e ElevenLabs **Creator**.
- [ ] Io: `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`, tu autorizzi dal browser.
- [ ] Io: chiave ElevenLabs in `.env`, mai nel repository.
- [ ] **Regola di spesa scritta nel codice: nessuna generazione sopra i 50 crediti senza tuo via libera.**

## Fase 2 — La prova dei 30 giorni (giorni 1-30)
Tre prove. Se ne falliscono due, si disdice e non si rinnova.
1. **Promo prodotto**: un video da 30 secondi per il Manuale Claude Code, Kling 3.0 1080p. Metro: si puo' pubblicare senza scuse?
2. **Carosello**: uno da 10 slide, Nano Banana Pro **con reference allegate**. Metro: batte quello che esce da Arena?
3. **Voce**: uno script YouTube inciso da te e ripassato in Speech-to-Speech. Metro: sembra una persona?

## Fase 3 — Lo sprint unlimited (giorni 1-7 di ogni mese)
I 7 giorni di Kling 3.0 e Nano Banana 2 unlimited si usano **a mano**, in sprint, per produrre
tutto il girato e tutte le immagini del mese. **A mano, mai con script** (paragrafo 1.4). I 1.200
crediti restano interi per i modelli premium.

## Fase 4 — Costruzione (settimane 2-6)
- [ ] Template Canvas "Promo Digital Empire": lo stampo si costruisce una volta.
- [ ] Soul ID del personaggio di brand.
- [ ] Skill `promo-video`: brief, prompt, MCP, clip, montaggio, cartella VIDEO-PRONTI.
- [ ] Carosello Nano Banana Pro innestato nella skill `carousel-empire` esistente, **con le reference come parametro**.
- [ ] Riparazione del ramo Arena (resta vivo per l'esplorazione gratuita, non e' buttato).

## Fase 5 — L'agente vocale (settimane 4-8)
- [ ] **Prima: parere legale** su Legge 49/2026 e perimetro B2B. Non si costruisce niente prima di quella risposta.
- [ ] Agente "richiamo lead caldo" agganciato a Preventa: risposta WhatsApp, poi chiamata entro 5 minuti.
- [ ] Dichiarazione AI nei primi 3 secondi piu' opt-out immediato (AI Act articolo 50).
- [ ] Voce clonata professionale.
- [ ] Registro dei consensi tracciabile e a prova di ispezione.
- [ ] Test su 20 lead, poi si decide se salire.

---

## Connessioni
- [[Digital_Empire_YouTube_Automation_Factory]]
- [[Preventa_Outreach_Automation]]
- [[Tool_Arena_Workflow_Caroselli]]
- `PIANO-MAESTRO/27-ARENA-WORKFLOW-COMPLETO-METODO.md`
- `PIANO-MAESTRO/21-ARENA-PROMPTS-MASTER-PACK.md`

## Fonti
Siti ufficiali letti direttamente il 2026-09-04: higgsfield.ai/pricing, higgsfield.ai/mcp,
docs.higgsfield.ai, elevenlabs.io/pricing, elevenlabs.io/pricing/agents,
elevenlabs.io/docs/capabilities/voice-changer, Terms of Use Higgsfield.
Normativa: Garante Privacy (telemarketing), Legge 49/2026, AI Act articolo 50 (linee guida
della Commissione Europea, operative dal 2026-08-02).
