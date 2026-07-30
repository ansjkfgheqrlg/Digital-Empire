# Failure Modes — Layer NFT Stream S7 (P09 First-Class, da `master-build-architecture`)

> FASE 2 del task: pattern applicato dal repo clonato
> `gh repo clone ansjkfgheqrlg/master-build-architecture` (vedi checkpoint per il dettaglio di
> cosa e' stato clonato/applicato e cosa no). Principio P09 ("Failure Modes as First-Class",
> `references/knowledge-pack/01-principles/P09-...`): ogni componente ha una tabella
> Failure | Symptom | Prevention | Detection | Recovery — non generica, con i guasti REALMENTE
> trovati in Fase 0-4, non ipotetici.

| # | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| 1 | Collection senza dati di rarity | `FairValueModel.fit()` non ha su cosa regredire | `best_rarity_rank()` verifica 3 provider prima di arrendersi | `ValueError` esplicito ("trovati 0"), mai un fit finto — visto reale su y00ts (0/98) | Escludi la collection dal backtest, segnalalo nel report (Ondata 3, non nascosto) |
| 2 | Campo stats mancante nella risposta reale (es. `volume7d` assente) | `scam_collection_filter` rifiuta una collection legittima (visto reale: degods) | `.get(campo, 0)` esplicito, mai un KeyError silenzioso | Log/report dichiara ESATTAMENTE quale check ha fallito e perche' (non solo "rifiutata") | Non forzare il pass: segnalare come limite della fonte dati, non della collection, e riprovare piu' tardi con un fetch diverso |
| 3 | Rate limit reale Magic Eden (429 su uso cumulato) | `MagicEdenClient._get` riceve HTTPError 429 | Pacing prudenziale (`MIN_INTERVAL_S=1.2`) sotto la soglia osservata in Fase 0 | `calls_429` contatore + log esplicito per tentativo | Backoff esponenziale (2^tentativo), fino a `MAX_RETRIES_429`; oltre, `MagicEdenRateLimited` esplicita (mai un retry infinito silenzioso) |
| 4 | Marketplace irraggiungibile (DNS/rete giu') | `client.get_stats()` lancia un'eccezione di rete | Nessuna soppressione dell'eccezione nel client | Ondata 3, Controllo Chirurgico stress test: `URLError` reale verificato pulito | Il chiamante (motore NFT) deve trattare come segnale mancante, non come "0 mismatch trovati" — differenza critica non ancora cablata in produzione, solo verificata a livello di client |
| 5 | Fit fair-value debole E instabile (R² basso, IC95%% ampio) | L'expectancy sembra positiva ma il modello potrebbe essere rumore | Bootstrap R² (Ondata 3) invece di fidarsi del punto singolo | IC95%% che include valori vicini a zero (visto reale: fino a 0.257 su degods, punto 0.026) | Non promuovere a live: serve piu' campione storico (backtest Ondata 3 nota esplicitamente questo limite) |
| 6 | Campione di segnali reali minuscolo (n=3 su 1 sola collection) | Monte Carlo/expectancy stimati su pochissimi trade reali | `backtest_across_collections` testa TUTTE le collection, non nasconde le 2/3 senza segnale | `n_eligible_real_listings_used` riportato esplicitamente in ogni risultato MC | Non generalizzare oltre il campione; il verdetto finale (Ondata 4) lo dichiara esplicitamente come limite, non lo ignora |
| 7 | Evento di uscita assunto (buyNow) raro nel mercato reale | Liquidity model stimato su k=1 evento reale (400 attivita' fetchate) | Poisson esatto (non gaussiano) proprio perche' k e' piccolo | IC95%% enorme dichiarato esplicitamente ([4.0, 880.3] giorni) — non nascosto dietro il punto (22.3gg) | Non usare il punto stimato da solo per decisioni di capitale; servono piu' finestre storiche (Ondata 3, item aperto) |
| 8 | Doppia esecuzione dello stesso segnale su bus condiviso | Se RiskManager/ExecutionEngine memecoin E NFT girassero sullo STESSO processo con lo stesso `global_bus`, ogni segnale approvato verrebbe eseguito due volte | Il layer NFT riusa le stesse CLASSI ma non e' MAI wired insieme al motore memecoin nello stesso processo di produzione in questo task | Non ancora osservato in produzione (solo in test, sempre isolati); rischio dichiarato qui prima che accada | Prima di un eventuale main.py unificato: instradare per `asset_class`/`strategy` (richiede una modifica a `execution_engine.py`, oggi frozen — decisione da prendere esplicitamente con Max, non silenziosa) |
| 9 | Wash-trading/concentrazione venditore ignorati | Il motore comprerebbe da un venditore che genera la maggioranza dell'attivita' recente senza saperlo | `seller_concentration()` + `is_wash_trading_suspect()` (Ondata 2) | Percentuale reale calcolata per collection (visto: fino al 43.9%% su y00ts) | Segnale scartato/marcato, non eseguito automaticamente (verificato nei test, non ancora cablato come blocco automatico nello scan — nota per un futuro miglioramento) |
| 10 | Royalty/fee non confermate dalla fonte primaria | Il modello di costo usa 2%% fee dichiarato pubblicamente noto, non riverificato oggi (429 sull'endpoint) | Costante marcata esplicitamente "DA CONFERMARE" nel codice e in Fase 0 §2, mai spacciata per misurata | Chiunque legga `nft_analysis_engine.py` vede il commento inline | Riprovare l'endpoint `/v2/collections/{symbol}` quando il rate limit si libera, aggiornare la costante con fonte reale |

## Traceability (P12, applicato)

Ogni numero usato in questo file e nei moduli `nft_*.py` ha una fonte dichiarata: API Magic Eden
pubblica (stats/listings/activities, fetchati e cachati in `memory/nft_cache/`), RPC Solana
pubblico (getRecentPrioritizationFees), CoinGecko (SOL/EUR), oppure calcolo derivato da questi
con la formula visibile nel codice. Nessun numero di questo file e' inventato — dove un dato
reale manca (royalty, tasso storico di rug per collection blue-chip), e' dichiarato come tale,
non stimato a sensazione (Fase 0, criterio 2).
