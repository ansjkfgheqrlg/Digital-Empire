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

- **P1 (oggi, ore 1-2):** shell finestra + UI tile statiche + pannello log. Nessuna logica.
- **P2 (oggi, ore 2-4):** bridge subprocess: le 4 tile outreach lanciano i .bat/py reali, log live streaming.
- **P3 (oggi, ore 4-5):** tile 5-8 (PreventivoForge, caroselli, Studio con input URL, STATO render).
- **P4 (oggi, ora 6):** selftest 8/8 tile → build `EmpireDesk.exe` (PyInstaller) → test doppio click → CP + push.
- **P5 (domani+):** scheduler run programmate · metriche settimana (dossier 16 §4) in dashboard ·
  checklist task board Max/Gael live · notifiche fine-run.
- **P6 (dopo):** gestione licenze concessionari (gestione-licenze.py wrap) · pannello revenue (incassi,
  pipeline S1) · config multi-tenant · tile Fliki WF-YT quando S5 pronto.

**Regola: ogni P chiuso = commit. Mai saltare avanti se il P corrente non è verde.**

## 4. GATE (bloccanti)

1. Ogni tile v0.1 lancia un processo REALE e mostra l'exit code — selftest documentato nel CP.
2. Niente logica di business nell'app: SOLO launcher (ADR-003). Se una tile "richiede" di riscrivere
   un motore → si wrappa il .bat esistente, punto.
3. Zero secrets nell'app o nel repo: path a `.env` locali, mai chiavi hardcoded.
4. Path robusti: l'exe gira da qualsiasi cartella (base dir risolta, no path relativi fragili).
5. UI: se WebView2 manca → fallback Tkinter funzionante (pattern già fatto).

## 5. Connessioni
- [[16-PIANO-ESTATE-REVENUE]] — l'app serve l'esecuzione della settimana revenue
- [[CP-20260703-001]] — GUI premium PreventivoForge (pattern sorgente)
- [[ADR-003]] — wrap, mai riscrittura
- `company/skills-map.yaml` — mappa automazioni disponibili
