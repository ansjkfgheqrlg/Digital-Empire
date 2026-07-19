# 🖥️ 17 — EMPIRE DESK: l'app .exe di TUTTO (direttiva Max 2026-07-19)

> **Ordine di Max:** "Gael deve costruire l'app .exe di tutto. Alla fine una piattaforma fatta bene,
> precisa, semplice da usare, che abbia dentro TUTTO: ogni singola automazione, ogni singola cosa.
> Tutto passo per passo, non tutto subito, pezzettino per pezzettino. La v0.1 pronta ENTRO OGGI. Ci pensa Gael."

---

## 0. Missione + DONE WHEN

**Missione:** un solo `.exe` Windows = la plancia di comando di Digital Empire. Ogni automazione
esistente si lancia da lì con un click. Semplice per Max, premium nell'aspetto, onesta nel funzionamento.

**DONE WHEN v0.1 (OGGI):**
1. Finestra desktop premium (stile empire) con **≥6 tile automazioni** che lanciano runtime REALI.
2. Pannello log live (output del processo lanciato, colorato).
3. `EmpireDesk.exe` buildato con PyInstaller e TESTATO (doppio click → funziona).
4. Selftest: ogni tile lancia il suo processo e mostra exit code. **ZERO bottoni finti** (Mandato Art.2:
   un bottone che non fa nulla è una promessa falsa).

---

## 1. STACK VINCOLATO (pattern già provato 2 volte — NON si sperimenta)

Identico a PreventivoForge GUI (CP-20260703-001) e Prof Autocad (CP-20260702-002):
- **pywebview + WebView2** (fallback Tkinter) — `app.py` con bridge JS↔Python.
- **UI HTML/CSS empire-premium-style**: slate scuro + argento + orange #fb4604, font premium,
  card/tile con hover, log colorato. Riusa i pattern di `Clienti/.../ui/index.html`.
- **PyInstaller** — riusa lo schema `build_exe.bat` + spec di PreventivoForge.
- **Lancio automazioni = `subprocess`** che apre i runtime ESISTENTI (ADR-003: l'app è un
  LAUNCHER/WRAPPER — mai riscrivere i motori, mai copiare la loro logica dentro l'app).

---

## 2. MODULI v0.1 — le tile (ognuna = subprocess a runtime reale)

| # | Tile | Cosa lancia (già esistente) |
|---|---|---|
| 1 | 📧 Outreach Email | flusso `/avvia-email` (CMD run email completa) |
| 2 | 📸 Outreach Instagram | flusso `/avvia-ig` |
| 3 | 💼 LinkedIn | flusso `/avvia-linkedin` |
| 4 | 🔎 Scraper Lead | `/avvia-scraper` (scrape_only.py) |
| 5 | 🚗 PreventivoForge | app preventivi (run/GUI cliente) |
| 6 | 🎨 Caroselli | batch carousel-factory (brand selezionabile) |
| 7 | 🎬 Empire Studio | ingest video (input URL → pipeline) |
| 8 | 📊 STATO Empire | render di `company/Memory/STATO-EMPIRE.md` (sola lettura) |

Ogni tile: nome, stato (idle/running/done/error), bottone Avvia, output nel pannello log, exit code visibile.

---

## 3. STEP-BY-STEP (pezzettino per pezzettino — ordine vincolante)

- ✅ **P1 (oggi, ore 1-2):** shell finestra + UI tile statiche + pannello log. — FATTO (Gael, sync 15:06).
- ✅ **P2 (oggi, ore 2-4):** bridge subprocess: le 4 tile outreach lanciano i .bat/py reali, log live streaming. — FATTO.
- ✅ **P3 (oggi, ore 4-5):** tile 5-8 (PreventivoForge, caroselli, Studio con input URL, STATO render). — FATTO
  (residuo: tile Caroselli rossa al selftest, vedi §5 task B0).
- 🔴 **P4 (oggi, ora 6):** selftest 8/8 tile → build `EmpireDesk.exe` (PyInstaller) → test doppio click → CP + push.
  — DA CHIUDERE (task B0, Gael). Selftest attuale: **7/8** (Caroselli FAIL, dettagli chirurgici in §5).
- **P5 (domani+):** scheduler run programmate · metriche settimana (dossier 16 §4) in dashboard ·
  checklist task board Max/Gael live · notifiche fine-run. → **diviso metà/metà in §5 (ordine Max 2026-07-19).**
- **P6 (dopo):** gestione licenze concessionari (gestione-licenze.py wrap) · pannello revenue (incassi,
  pipeline S1) · config multi-tenant · tile Fliki WF-YT quando S5 pronto. → **diviso metà/metà in §5.**

**Regola: ogni P chiuso = commit. Mai saltare avanti se il P corrente non è verde.**

## 4. GATE (bloccanti)

1. Ogni tile v0.1 lancia un processo REALE e mostra l'exit code — selftest documentato nel CP.
2. Niente logica di business nell'app: SOLO launcher (ADR-003). Se una tile "richiede" di riscrivere
   un motore → si wrappa il .bat esistente, punto.
3. Zero secrets nell'app o nel repo: path a `.env` locali, mai chiavi hardcoded.
4. Path robusti: l'exe gira da qualsiasi cartella (base dir risolta, no path relativi fragili).
5. UI: se WebView2 manca → fallback Tkinter funzionante (pattern già fatto).

## 5. DIVISIONE METÀ/METÀ MAX ↔ GAEL (ordine Max 2026-07-19 pomeriggio — FOCUS TOTALE APP)

> **Ordine di Max:** da ora lavoro sull'app diviso a metà precisa tra Max e Gael. Massimo impegno,
> attenzione a ogni dettaglio, coinvolgimento dei migliori reparti. L'app è il lavoro più importante.

### 5.0 Stato verificato al momento della divisione (2026-07-19 ~15:20)
- `EmpireDesk/` esiste: `app.py` (461 righe, 3 motori GUI, TileManager, bridge HTTP), `ui/index.html`
  (217 righe, bridge dual-mode), `build_exe.bat`, `empiredesk.spec`, README, REGISTRO-ERRORI.
- Selftest: **7/8**. Unica FAIL = tile Caroselli, con **2 difetti** (entrambi verificati sul codice):
  1. `app.py` riga ~101: `"script": "scripts/generate.js"` — risolto da `REPO_ROOT` → punta a
     `<repo>/scripts/generate.js` che NON esiste. Path vero:
     `Workfolw crea caroselli à/carousel-factory/scripts/generate.js` (verificato su disco).
  2. `generate.js` **esige un argomento** (`process.argv[2]` = file JSON carosello; senza → usage + exit 1).
     In `input/` non c'è nessun JSON pronto (solo `images/`). → la tile DEVE avere `"input"` (campo
     path JSON, come la tile Studio ha l'URL) o sarebbe un bottone che fallisce sempre = bottone finto (Gate 1).
- `dist/` assente: exe mai buildato. P4 aperto.

### 5.1 GAEL — Half B «Core & Runtime» (owner: `app.py` · `ui/index.html` · `build_exe.bat` · `empiredesk.spec`)
- **B0 — CHIUDI v0.1 (OGGI, per primo):**
  1) fix tile Caroselli: path completo + campo `input` per il JSON carosello (2 difetti sopra);
  2) selftest **8/8**;
  3) `build_exe.bat` → `dist/EmpireDesk/EmpireDesk.exe` → test DOPPIO CLICK reale;
  4) CP + STATO + push. **v0.1 CHIUSA.**
- **B1 — SEAM MODULI (subito dopo B0 — sblocca Max):** loader `EmpireDesk/modules/` (contratto §5.3)
  + switcher pannelli nella UI. Dopo B1: `app.py`/`index.html` **FREEZE** — si estendono SOLO via modules/.
- **B2 — `modules/scheduler.py`:** run programmate per tile (orari, persistenza in `EmpireDesk/state/`,
  riusa il lock "un processo per tile", mai run concorrenti).
- **B3 — `modules/notify.py`:** notifica Windows a fine run con exit code (toast; zero dipendenze pesanti).
- **B4 — `modules/taskboard.py`:** task board Max/Gael live (fonte `EmpireDesk/state/taskboard.json`,
  seed dai task del dossier 16).

### 5.2 MAX — Half A «Dati & Business» (owner: i 4 moduli qui sotto — file NUOVI, zero collisione)
- **A1 — `modules/metrics.py`:** dashboard metriche settimana (dossier 16 §4) da dati REALI
  (report outreach, output caroselli, storico preventivi). Dato assente → il pannello dice
  «nessun dato», MAI numeri inventati.
- **A2 — `modules/revenue.py`:** pannello revenue — pipeline S1 (7 concessionari: stato
  contatto/demo/incasso), fonte `EmpireDesk/state/revenue.json` compilato da Max.
- **A3 — `modules/licenze.py`:** wrap di `gestione-licenze.py` (stato/sospendi/attiva concessionari
  da Empire Desk). Kill-switch già ownership Max. Zero secrets nell'app (usa gh/config locali).
- **A4 — `modules/fliki.py`:** tile WF-YT Fliki (parte quando S5 è pronto; API key SOLO da `.env`
  locale gitignorato).
- Max può scrivere A1-A4 **da subito** a contratto (§5.3) in parallelo; l'integrazione si accende
  quando Gael pusha B1. Unica dipendenza = B1.

### 5.3 Contratto modulo (vincolante — così i due half non si toccano MAI)
Ogni modulo = un file `EmpireDesk/modules/<nome>.py` che espone:
```python
MODULE = {
    "id": "metrics",                    # univoco
    "tile": {...} | None,               # opzionale: tile aggiuntiva nel grid (schema TILES)
    "routes": {"metrics/summary": fn},  # fn(payload: dict) -> dict, montate su POST /api/<route>
    "panel_html": "<div>…</div>",       # opzionale: pannello nello switcher UI
}

def selftest() -> tuple[bool, str]: ...  # entra nel selftest globale (verifica path/config, MAI lanci reali)
```
Il loader (B1, Gael) scandisce `modules/*.py`, importa, monta routes/tile/panel e estende il selftest.

### 5.4 Regole anti-collisione (lezione PreventivoForge — 2 collisioni reali, mai più)
1. **MAI toccare i file dell'altro.** Gael: core + moduli B. Max: moduli A. Punto.
2. `REGISTRO-ERRORI.md`: append-only per entrambi (mai riscrivere righe altrui).
3. Ogni task chiuso = commit + push + blocco STATO aggiornato. Un solo swarm Opus per volta.
4. Gate per OGNI modulo: zero bottoni finti · dati reali o «nessun dato» esplicito · zero secrets ·
   selftest modulo verde · ADR-003 (wrappa, mai riscrivere motori).
5. Sequenza: **B0 (oggi) → B1 (oggi/domani) → parallelo pieno** (A1-A4 ∥ B2-B4).

## 6. Connessioni
- [[16-PIANO-ESTATE-REVENUE]] — l'app serve l'esecuzione della settimana revenue
- [[CP-20260703-001]] — GUI premium PreventivoForge (pattern sorgente)
- [[ADR-003]] — wrap, mai riscrittura
- `company/skills-map.yaml` — mappa automazioni disponibili
