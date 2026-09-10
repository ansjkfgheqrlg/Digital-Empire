# Report — A6/L04 «Come aumentare il CTR vertiginosamente» (21:12)

- **Durata:** 21:12 · ~2.993 parole · **profondità ORO**
- **Letta:** parlato integrale + 12/54 frame unici (campione motivato, vedi `frame-scelti.md`)
- **Rapporto grezzo:** [`appunti.md`](appunti.md) · frame: [`frame-scelti.md`](frame-scelti.md)

---

## 1. Cosa insegna

Come leggere e usare i dati di YouTube Studio (non pubblici, dati da proprietario canale) per
alzare il CTR: la tab Copertura/Contenuti per leggere impressioni e percentuale di clic, la
regola "più view = CTR% più basso" (stesso volume assoluto su periodo più lungo diluisce la
percentuale), la soglia operativa **minimo 8% per un video/canale piccolo, 12-15% = copertina da
replicare, 5-7% accettabile solo su milioni di view**, la sezione Pubblico › cosa guarda il
pubblico come fonte diretta di idee per nuovi video/canali, e sei regole di produzione per il
CTR: niente intro nel primo minuto, keyword ripetuta e gancio in apertura, CTA mirate nei primi
minuti, copiare-non-clonare copertine competitor senza stravolgere un format che converte, mai
rivelare la risposta in copertina, titoli "forti" ma non clickbait (pena perdita di fiducia e
rischio demonetizzazione).

## 2. Cosa facciamo oggi

`channel-performance-analyst.md` §2 dichiara esplicitamente il limite: *"CTR, retention e ricavi
richiedono YouTube Studio, che è privato. Dal fetch pubblico si ricavano solo views ed età. Nei
log quei campi sono `null`, e `null` è la risposta giusta"*. Verificato nel codice, non solo
nella spec: `apex7_orchestrator.py:1678-1685` scrive sempre `"ctr": None, "retention_rate": None`
in ogni log di performance. A valle, `self_improve.py` (righe 68, 109-111, 130-132) e
`meta_agent.py` (righe 48-70) hanno **già pronte** soglie di apprendimento sul CTR (4,0% cattivo,
7,0-7,5% buono) — quasi identiche a quelle di questa lezione (8% in media, 12-15% da replicare) —
ma non ricevono mai un dato reale perché la fonte a monte è sempre vuota.

## 3. Delta

**Il delta è nella catena mancante, non nella soglia.** Il nostro motore di apprendimento
(`self_improve.py`, `meta_agent.py`) è già costruito per esattamente il metodo di questa
lezione — confrontare tag/keyword/hook per CTR medio e rinforzare quelli sopra soglia — ma è
**cieco** perché nessuno script legge mai i tab Analytics di YouTube Studio. Eppure la porta
d'accesso esiste già: `youtube_uploader_playwright.py` fa login persistente su
`studio.youtube.com` con un profilo Chrome salvato (righe 186-307) per il wizard di
pubblicazione — lo stesso identico accesso che servirebbe per leggere Panoramica, Copertura e
Pubblico. Non è un limite tecnico vero (i dati Studio sono privati ma noi **siamo** i proprietari
dei nostri canali, loggati) — è un pezzo di fabbrica che semplicemente non è mai stato scritto.
Questo chiude, con una causa precisa, il buco già registrato come `A4-RC-15` (CTR/retention
sempre `null`): non è "impossibile misurare", è "nessuno ha ancora scritto lo script che legge
Studio".

Un secondo delta minore: la sezione "Pubblico › cosa guarda il nostro pubblico" (12:05-13:04) è
una fonte diretta di idee-video/canale dichiarata da YouTube stesso — non automatizzata in nessun
punto della fabbrica (né `ytf-niche-scout` né `ytf-video-hunter` la citano). Applicabilità
media: richiederebbe lo stesso accesso Studio di cui sopra.

## 4. Conflitti

Nessuno. Le sei regole di produzione (niente intro, gancio in apertura, CTA mirate, copiare senza
clonare, copertina che non rivela, titoli forti non-clickbait) sono coerenti con quanto già
registrato in `A6-L01` (riscrittura titoli competitor) e non contraddicono nulla della fabbrica —
sono regole di scrittura copy/script che oggi il docente stesso applica manualmente, non un
processo automatizzato nostro da correggere.

## 5. Regole estratte

Cinque: una **costruttiva** (il buco vero, priorità alta — sblocca l'intero motore di
apprendimento già scritto), quattro documentali/procedurali sulle soglie e sulla produzione.

| id | regola in una riga | tipo | tocca |
|---|---|---|---|
| `A6-L04-01` | Costruire un lettore Playwright di YouTube Studio Analytics (Panoramica/Copertura/Pubblico) che riusa il login persistente già collaudato in `youtube_uploader_playwright.py`, per popolare `ctr`/`retention_rate` reali al posto di `None` | **agente/script** — costruisci | `02-AUTOMAZIONI-E-SCRIPTS/youtube_studio_analytics_playwright.py` (nuovo) |
| `A6-L04-02` | Soglia operativa di CTR: 8% = in media/accettabile per canale piccolo, 12-15% = copertina da replicare, sotto 4-6% = copertina/titolo da rivedere (ma solo dopo 10-20 video, non dal primo) | parametro | `04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md` |
| `A6-L04-03` | Il CTR% scende fisiologicamente quando le impressioni assolute crescono (stesso video, periodo più lungo): un calo percentuale non è di per sé un problema, va letto insieme al volume | euristica | `03-AGENTI-E-RUOLI/operatori/channel-performance-analyst.md` |
| `A6-L04-04` | Prima del primo minuto nessuna intro di canale; ripetere la keyword e creare un gancio nei primi secondi; CTA mirata (non generica) entro i primi minuti | procedura | `03-AGENTI-E-RUOLI/` (script-writer / hook) |
| `A6-L04-05` | La sezione Pubblico › "cosa guarda il nostro pubblico" di YouTube Studio è una fonte diretta di idee-canale/idee-video dichiarata da YouTube stesso | strumento | `03-AGENTI-E-RUOLI/operatori/` (niche-scout / video-hunter) |

## 6. Applicabilità

**Alta su `A6-L04-01`**: è il pezzo mancante che, una volta costruito, rende reale (non più
teorico) tutto il motore di apprendimento già scritto in `self_improve.py` e `meta_agent.py` —
non richiede di inventare nulla di nuovo lato logica, solo di dargli l'input che gli manca.
**Media** sulle soglie numeriche (`A6-L04-02`/`03`): utili come criteri di lettura una volta che
il dato esiste, oggi non applicabili perché il dato è `null`. **Media-bassa** sulle regole di
produzione copy (`A6-L04-04`): buone pratiche già in parte presenti nello stile dei nostri
script, da verificare puntualmente non da questa lezione sola. **Bassa** su `A6-L04-05`: idea
valida ma dipende dallo stesso accesso Studio di `A6-L04-01`.
