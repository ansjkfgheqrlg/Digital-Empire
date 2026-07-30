# FASE 0 — Tecnica di studio e analisi (7 miglioramenti stile APEX-7)

> Task: `company/Memory/tasks/TASK-GAEL-20260730-STREAM-S7-NFT-METODO.md`, sezione 2.
> Gate: 7/7 devono essere PASS prima di passare a Ondata 1. Ogni riga cita la fonte reale
> usata per verificarla (comando eseguito, non dichiarazione).

| # | Criterio | Verdetto | Evidenza |
|---|---|---|---|
| 1 | Domanda misurabile | **PASS** | Vedi §1 |
| 2 | Fonte dati dichiarata | **PASS** | Vedi §2 |
| 3 | Unità di misura coerente | **PASS** | Vedi §3 |
| 4 | Casistiche enumerate | **PASS** | Vedi §4 |
| 5 | Percentuali con intervallo | **PASS** (regola dichiarata, applicata in Ondata 1/3) | Vedi §5 |
| 6 | Confronto con baseline noto | **PASS** | Vedi §6 |
| 7 | Criterio di stop dichiarato | **PASS** | Vedi §7 |

**Verdetto FASE 0: 7/7 PASS.** Si procede a Ondata 1.

---

## §1. Domanda misurabile

> "Qual è l'**expectancy netta per trade** (in % del capitale allocato per trade), per una
> strategia di 'floor–rarity mismatch sniping' su Magic Eden (Solana), calcolata al netto di
> fee marketplace, royalty creator, gas/priority fee, e probabilità di illiquidità, su almeno
> 3 collection reali con dati storici verificabili via API pubblica?"

Non generica: ha un'unità (% capitale), un edge dichiarato (mismatch floor/rarity, non lo
stesso edge memecoin già coperto da `analysis_engine.py`), un netto di costi espliciti, e un
campione minimo dichiarato (≥3 collection).

## §2. Fonte dei dati dichiarata

Ogni fonte verificata **oggi, in questa sessione**, con comando reale (non assunta dalla
documentazione):

| Dato | Fonte | Comando/prova | Esito reale |
|---|---|---|---|
| Floor price, volume, listed count | `GET api-mainnet.magiceden.dev/v2/collections/{symbol}/stats` | `urllib.request` diretto | 200 OK — `mad_lads`: floor 7.389 SOL, listedCount 242, volume7d ≈ 51 937.7 SOL |
| Listing correnti (prezzo + rarity rank) | `GET .../v2/collections/{symbol}/listings` | idem | 200 OK — 5 listing reali, rank 6858–8812, prezzo 7.389–7.55 SOL |
| Storico attività (bid/sale/cancelBid) | `GET .../v2/collections/{symbol}/activities` | idem | 200 OK — eventi reali con `blockTime` Unix |
| Rate limit reale dell'API | burst 20 richieste concorrenti + uso cumulato | `ThreadPoolExecutor(20)` su `/stats`, poi ~10 chiamate cumulate su `/v2/collections/{symbol}` | **20/20 concorrenti OK** (0 × 429); ma dopo uso cumulato nella stessa sessione: `HTTPError 429 "You have exceeded the requests in 1 min limit! Please try again soon."` — limite reale esiste, per-minuto, non per-burst-istantaneo. Molto più permissivo dell'RPC Solana pubblico (429 dopo 2 chiamate, CP-20260728-006), ma non infinito |
| Priority fee reale rete Solana | `getRecentPrioritizationFees` RPC pubblico, targettizzato sul program ID Magic Eden (`M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K`) | chiamata RPC diretta | 150/150 campioni = **0 lamports** in questo momento (nessuna guerra di priority fee in corso su ME) |
| Base fee protocollo Solana | costante di protocollo pubblica (non per-query) | — | 5000 lamports/firma (costante nota, non stimata) |
| Tasso SOL/EUR-USD | CoinGecko public API | `GET api.coingecko.com/api/v3/simple/price` | 200 OK — SOL/USD 73.37, SOL/EUR 64.15 (istantaneo, timestamp di questa sessione) |
| Fee marketplace Magic Eden (%) | endpoint `/v2/collections/{symbol}` (info generale) e pagina fee ufficiale | **FALLITO**: 404 sulla pagina doc tentata, poi **429** sull'endpoint API prima di poter leggere il campo — non confermato oggi con fonte primaria propria | Segnalato come numero **non verificato in questa sessione**, non inventato: nel modello di costo (Ondata 1, blocco 5) uso 2% come parametro dichiarato pubblicamente noto di Magic Eden, marcato esplicitamente `fonte: non riverificata oggi, DA CONFERMARE` finché una chiamata non va a buon fine |

Nessun numero in questo documento o nei blocchi successivi è "a sensazione": ogni tabella nel
codice porta un commento con la fonte, comprese le voci non confermate (marcate come tali,
mai spacciate per misurate).

## §3. Unità di misura coerente

- Prezzi/volumi NFT: sempre **SOL** (Magic Eden restituisce lamports; conversione
  `/ 1_000_000_000` esplicita in ogni funzione, stesso pattern di `analysis_engine.py`
  `LAMPORTS_PER_SOL`).
- Conversione a € solo per il report finale a Max, con tasso dichiarato e timestampato
  (SOL/EUR 64.15 rilevato oggi) — mai mischiato con i calcoli in SOL.
- Percentuali sempre "in % del capitale allocato per trade", mai "in % del bankroll totale"
  senza dirlo esplicitamente (sono numeri diversi).
- Tempo: secondi Unix (`blockTime`/`timestamp`) per i dati Magic Eden, `time.time()` per il
  codice — stessa convenzione di `position_monitor.py`.

## §4. Casistiche enumerate

| Scenario | Descrizione |
|---|---|
| **Successo** | Compra un listing sotto il fair-value stimato dal rank di rarità, rivende sopra il fair-value entro la finestra di liquidità attesa |
| **Fallimento — illiquidità** | Nessun acquirente entro la finestra attesa: capitale bloccato ("bagholding"), stesso rischio già descritto in `LOGICA-COMPLETA-S7.md` §Rischi punto 4 |
| **Fallimento — wash trading** | Il volume/attività usati per calibrare fair-value o liquidità sono gonfiati da vendite fittizie tra wallet collusi |
| **Fallimento — scam/rug collection** | Il floor crolla per abbandono del progetto o rug pull del creator, indipendentemente dal mismatch di rarità |
| **Fallimento — costi netti** | Il mismatch lordo esiste ma fee (2%) + royalty + gas lo annullano o lo rendono negativo |
| **Fallimento — latenza/concorrenza** | Un altro bot/umano compra il listing sottoprezzato prima (stesso principio del rischio #1 in `report-studio.md`, ma su scala di secondi/minuti, non millisecondi) |

Non solo il caso positivo: 5 scenari di fallimento espliciti su 1 di successo.

## §5. Percentuali con intervallo, non solo media

Regola dichiarata qui, **applicata concretamente** in Ondata 1 blocco 8 (Monte Carlo → media +
intervallo di confidenza, non un singolo numero) e verificata di nuovo in Ondata 3 blocco 3
(intervallo di confidenza esplicito sul report finale). Nessuna stima di expectancy in questo
task viene presentata come singolo numero puntuale.

## §6. Confronto con un baseline noto

Baseline dichiarato: **`report-studio.md`** (mandato GEM-07) — expectancy netta **negativa**,
probabilità di perdere l'intero capitale di rischio **>85% nel primo mese**, per 3 motivi
strutturali (latenza 300-800ms contro MEV bot istituzionali, RPC pubblico che rate-limita dopo
2 chiamate `getTransaction`, rug pull su Pump.fun/Raydium). Più i 3 bug reali già trovati e
corretti su questo stesso ecosistema (`CP-20260728-006`: parser che leggeva un mondo finto,
limite posizioni che non scattava, spam di segnali duplicati) — evidenza che la logica ha già
dimostrato di avere buchi non ovvi anche dopo revisione. Ogni nuova stima in questo task si
confronta esplicitamente con questi numeri (Ondata 4, Controllo Chirurgico #2), non riparte da
zero come se non esistesse storia.

## §7. Criterio di stop dichiarato

Il metodo NFT **viene scartato per l'uso live** (resta R&D/paper trading) se, alla fine di
Ondata 3 (backtest + intervallo di confidenza), **una qualsiasi** di queste condizioni è vera:

1. Il limite superiore dell'intervallo di confidenza al 95% dell'expectancy netta per trade è
   **≤ 0%** (nessuna evidenza statistica di edge positivo, non solo "media negativa").
2. La probabilità simulata di perdere **>50%** del capitale allocato al lane NFT entro
   l'orizzonte di backtest supera **50%** (stesso ordine di rigore del bar già usato da
   `report-studio.md`, che parla di >85% probabilità di rovina totale).
3. Il Controllo Chirurgico #2 (Ondata 4) non riesce a spiegare **con numeri**, non a parole,
   quale problema strutturale di `report-studio.md` risolve.

Questo criterio è scritto **prima** di costruire il metodo (non a posteriori), esattamente
come richiesto dal criterio 7 stesso — evita di aggiustare la soglia per far tornare un
risultato positivo.
