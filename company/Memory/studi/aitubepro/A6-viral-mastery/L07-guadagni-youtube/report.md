# Report — A6/L07 «Come Aumentare i GUADAGNI su YouTube» (14:34)

- **Durata:** 14:34 · ~2.017 parole · **profondità ORO**
- **Letta:** parlato integrale + 13/69 frame unici (campione motivato, vedi `frame-scelti.md`)
- **Rapporto grezzo:** [`appunti.md`](appunti.md) · frame: [`frame-scelti.md`](frame-scelti.md)

---

## 1. Cosa insegna

Cinque leve di guadagno YouTube oltre le view pubblicitarie automatiche: (1) mid-roll — video
sopra 8 minuti sbloccano interruzioni pubblicitarie posizionabili manualmente, strategia "ogni 2
minuti" per intercettare anche chi salta avanti nel video; (2) Shorts monetizzabili ma marginali
salvo scala enorme; (3) Super Chat/Stickers/Grazie e Abbonamenti canale (fino a 3-4 livelli a
pagamento, consigliati 3 livelli come "risultato migliore"); (4) Shopping/merchandising collegato
al canale, soglia consigliata 10.000 iscritti; (5) email business nella sezione Informazioni del
canale come canale di collaborazioni sponsorizzate; (6) affiliazioni dentro descrizione/commento
fissato — esempio dal vivo su un canale crypto con link Ledger, guadagno dichiarato "prettamente
da affiliazioni, non dalle visualizzazioni".

## 2. Cosa facciamo oggi

`youtube_uploader_playwright.py` attiva l'interruttore generale "Watch Page ads" dopo l'upload
(`ads_on_after_upload()`, righe 225-258) — necessario perché Google lo lascia spento di default,
verificato dal codice e dal suo stesso commento sorgente. Non tocca mai il pannello "Interruzioni
pubblicitarie" (mid-roll) mostrato in `frame-057.png`: grep mirato, zero occorrenze di "midroll",
"ad break", "interruzione". `scripts/tesoreria.py:57` ha già `"youtube"` come motore di business
valido nel ledger dei ricavi, ma — confermato dalla memoria dell'azienda — nessun ricavo YouTube
è mai stato registrato: nessuno script legge le "Entrate stimate" di YouTube Studio né un ricavo
da affiliazione. `regolatori.py:270 DURATA_MINIMA_S = 480` (8 minuti esatti) è già in vigore come
soglia minima di durata.

## 3. Delta

**Conferma più che delta sul punto più importante**: la soglia 8 minuti del corso coincide
esattamente con `DURATA_MINIMA_S = 480` già nel nostro codice — chiude, con un numero motivato
dal corso stesso, l'ambiguità segnalata dal piano di studio §2 fra questa soglia e
`PAROLE_MINIME_SCRIPT` (target 12 minuti in `apex7_orchestrator.py:164`): non sono in
contraddizione, sono due soglie per due scopi (8 min = minimo tecnico per i mid-roll, 12 min =
target di retention scelto sopra il minimo).

Il delta vero è nella catena "monetizzazione oltre le view", che oggi si ferma al primo gradino
(ads generiche on/off) e non prosegue sui quattro successivi insegnati dalla lezione: nessun
posizionamento mid-roll ottimizzato, nessun campo email business nel setup canale (verificato
assente in `ytl-channel-architect`, `ytl-brand-designer`, `ytl-channel-seo`), nessuno slot per
link di affiliazione nella generazione descrizione (`apex7_orchestrator.py`, righe ~1495-1520),
e — il più grave dei quattro perché tocca direttamente Tesoreria — nessun pull di "Entrate
stimate" da YouTube Studio verso `scripts/tesoreria.py`, benché il motore "youtube" esista già
nel ledger. Lo stesso accesso Studio richiesto da questo punto è **identico** a quello del
lettore Analytics proposto in `A6-L04-01` (login persistente già collaudato in
`youtube_uploader_playwright.py`): le due regole condividono la stessa porta d'accesso.

## 4. Conflitti

Nessuno. Anzi, un conflitto apparente dal piano di studio (§2, soglie di durata) viene qui
risolto a favore di entrambe le soglie esistenti: 8 minuti (mid-roll) e 12 minuti (target
retention) coesistono senza contraddirsi.

## 5. Regole estratte

Sei: due **costruttive** (pull ricavi Studio→Tesoreria, priorità alta; email business nel setup
canale), una **conferma** che chiude l'ambiguità sulle soglie, tre parametriche/procedurali.

| id | regola in una riga | tipo | tocca |
|---|---|---|---|
| `A6-L07-01` | Costruire un pull delle "Entrate stimate" da YouTube Studio (Panoramica video/canale) verso `scripts/tesoreria.py`, motore `youtube` già esistente nel ledger ma mai popolato da dati reali | **script** — costruisci | `02-AUTOMAZIONI-E-SCRIPTS/youtube_studio_analytics_playwright.py` (condiviso con `A6-L04-01`) → `scripts/tesoreria.py` |
| `A6-L07-02` | La soglia di durata 480s (8 minuti) in `regolatori.py` è confermata come il minimo tecnico reale per sbloccare i mid-roll: non va alzata, resta distinta dal target 12 minuti di `apex7_orchestrator.py` che serve la retention, non la monetizzazione | vincolo | `02-AUTOMAZIONI-E-SCRIPTS/regolatori.py` (conferma, nessuna modifica) |
| `A6-L07-03` | Aggiungere il campo email business nel checklist di lancio canale (sezione Informazioni di base), oggi assente in tutti e tre gli agenti di setup canale | funzione | `03-AGENTI-E-RUOLI/operatori/ytl-channel-architect.md` |
| `A6-L07-04` | Il posizionamento mid-roll non è mai configurato dal nostro uploader (solo l'interruttore generale ads on/off): valutare se automatizzare una cadenza (es. ogni 2 minuti) per video sopra 480s | flusso | `02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py` |
| `A6-L07-05` | Shorts monetizzano poco salvo scala enorme: non deviare risorse di produzione dal formato lungo già scelto dalla fabbrica per inseguire gli Shorts | euristica | `03-AGENTI-E-RUOLI/` (capo-strategia) |
| `A6-L07-06` | Affiliazioni in descrizione/commento fissato sono una fonte di ricavo indipendente dalle view: nessuno slot esiste oggi nella generazione descrizione | funzione | `02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py` (generazione descrizione) |

## 6. Applicabilità

**Alta su `A6-L07-01`**: chiude un buco già a registro nella memoria aziendale (zero ricavi
YouTube mai registrati) e condivide l'infrastruttura di accesso con `A6-L04-01` — costruirli
insieme è più efficiente che separatamente. **Alta su `A6-L07-02`**: chiude un'ambiguità aperta
nel piano di studio con un numero verificato, zero rischio (nessuna modifica al codice, solo
conferma). **Media su `A6-L07-03`/`06`**: passi concreti e a basso rischio ma dipendono da una
decisione di prodotto (vogliamo fare affiliate marketing? in quali nicchie?), non solo da un
gap tecnico. **Bassa-media su `A6-L07-04`**: automatizzare il mid-roll richiede test A/B contro
il posizionamento automatico di YouTube, che potrebbe già essere sufficiente. **Bassa su
`A6-L07-05`**: conferma di una scelta già presa, non un'azione nuova.
