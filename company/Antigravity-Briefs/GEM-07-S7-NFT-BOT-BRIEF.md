# GEM-07 — BRIEF S7: Bot Trading NFT/Memecoin (PAPER-TRADING FIRST)

> Delega di Max/Claude a Gemini/Antigravity, 2026-07-23. Decisione D-EST-007 (dossier 24 §A).
> Esecuzione 100% Gemini: Claude e Gael NON toccano questo stream (isolamento da S1/S2).
> Owner: Gemini. Cartella target: `company/Ecosistemi/08-TRADING-BOT/`.

## REGOLA ZERO (non negoziabile)
1. **PAPER-TRADING PRIMA.** Nessun capitale reale finché la simulazione non dimostra *expectancy positiva*
   su ≥3-4 settimane di dati reali. Il primo deliverable è un **verdetto onesto**, non un bot che spende.
2. **Nessuna chiave privata** nel repo/zip/log. Solo `.env.example`. Wallet/chiavi → variabili d'ambiente su VPS.
3. **Chain a fee basse** (Solana o Polygon) per i test. Mai Ethereum mainnet in fase test.
4. **Se la strategia non regge, DILLO.** Onestà ingegneristica > compiacere. Il paper-trading serve a
   scoprire GRATIS se abbiamo un edge contro gli MEV bot istituzionali (probabilmente no).

## COSA COSTRUIRE (4 layer, dal report S7)
- **A. Data Manager** — ingestione real-time: RPC WebSocket (Alchemy/Infura) su mempool Solana/Polygon.
  NO scraping OpenSea (bloccato Cloudflare). Registra eventi grezzi in un dataset locale per la simulazione.
- **B. Analysis Engine** — logica decisionale: rarity sniping (NFT sotto-floor vs rarità tratti) +
  trend/volume spike detection (memecoin). Stack `pandas`/`numpy`. Opz.: sentiment Twitter/Discord.
- **C. Execution Engine** — in **modalità SIMULAZIONE**: `web3.py`/`ethers.js` che *firmerebbe* le tx ma le
  registra in un log paper-trade invece di inviarle. Calcolo gas fee dinamico simulato (per contare i costi
  reali che avrebbe avuto). Solo dopo il gate → modalità reale dietro flag esplicito.
- **D. Risk & Treasury** — limiti posizione (max 5% wallet/trade), stop-loss/take-profit automatici,
  kill-switch manuale, log di ogni operazione simulata.

## CONSEGNA (zip auto-contenuto)
1. `report-studio.md` — verdetto onesto: la strategia ha un edge? qual è l'expectancy simulata? costi reali
   (gas, fee, slippage)? probabilità di perdita capitale? Se è un modo per vendere corsi, scrivilo.
2. Codice bot in **modalità simulazione** + `requirements.txt` + `.env.example` (mai chiavi vere).
3. Log di performance simulata su dati storici/live registrati (le metriche che decidono il gate).
4. `LEGGIMI.md` — come si passerebbe a soldi veri, QUALI rischi si accettano, come si arma il kill-switch.

## GATE PRIMA DI SOLDI VERI (Max decide)
Simulazione con expectancy positiva netta di costi su ≥3-4 settimane → SOLO allora Max valuta capitale reale
(che può perdere). Senza questo, S7 resta simulazione. **S7 = €0 nelle proiezioni revenue estate.**

## IMPORT AL RIENTRO (protocollo ADR-008)
Zip → Claude fa audit secrets/bloat, censisce in `REGISTRO-IMPRESA.md` + `skills-map.yaml`, checkpoint memoria.
