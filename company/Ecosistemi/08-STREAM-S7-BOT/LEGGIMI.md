# LEGGIMI - Istruzioni Macchina Automatica S7

Questo ecosistema implementa un simulatore (Paper-Trader) per analizzare il Mempool di Solana e identificare opportunità di arbitraggio su NFT/Memecoin.

## Come eseguire la simulazione
1. Entrare nella cartella: `cd company/Ecosistemi/08-STREAM-S7-BOT`
2. Installare le dipendenze: `pip install -r requirements.txt`
3. Eseguire il bot: `python main.py`

Il bot inizierà a generare eventi crudi mock (o reali se configuri `SOLANA_WSS_URL` nel file `.env`), li analizzerà e scriverà l'esito dei trade simulati nel file `paper_trade_log.csv`.

## Come passare alla modalità "Soldi Veri" (LIVE)
> [!CAUTION]
> **PERICOLO DI PERDITA CAPITALE**
> Prima di passare alla modalità Live, assicurati che `report-studio.md` dimostri un'expectancy positiva su almeno 30 giorni di simulazione.

Se il Gate viene superato, questi sono i passaggi tecnici:
1. Copiare `.env.example` in `.env`.
2. Compilare `WALLET_PUBLIC_KEY` e `WALLET_PRIVATE_KEY` con un "Hot Wallet" usa e getta (non il vault principale).
3. Modificare `TRADE_MODE=SIMULATION` in `TRADE_MODE=LIVE`.
4. Nel file `execution_engine.py`, sostituire la funzione `_simulate_transaction` con la libreria crittografica di `solana-py` (`solders.keypair`) per firmare e inviare il payload RPC.
5. Finanziare l'Hot Wallet con il quantitativo indicato in `BASE_BANKROLL_SOL`.

## Funzionamento del Kill-Switch
Il `RiskManager` possiede una funzione `activate_kill_switch()`.
Se la volatilità del mercato esplode, se le gas fees decuplicano, o se il log rileva 3 trade in perdita consecutivi a causa di latenza, il Kill-Switch bloccherà l'allocazione del capitale, mettendo in pausa il layer di esecuzione all'istante senza chiudere le connessioni WebSocket.
