---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/PIANO-COMPLETAMENTO-L2.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# PIANO COMPLETAMENTO WORKFLOW-ESTATE — **LIVELLO 3** (piano eseguibile)
> 2026-07-23 · Claude · **Migliora L2** risolvendo i suoi 4 limiti. Questo è il piano che si esegue.
> Architettura: [ARCHITETTURA-COMPLETAMENTO.md](ARCHITETTURA-COMPLETAMENTO.md)

## 0. Le 4 correzioni che L3 applica a L2

| Limite di L2 | Correzione L3 |
|---|---|
| Nessun disegno di swarm → rischio collisione | **6 lotti con perimetro di file disgiunto e dichiarato**. Un agente che tocca fuori perimetro è un difetto, non una svista |
| Nessun comando unico di "finito" | **`python -m empire estate`** — un solo comando, exit 0 = Workflow Estate finito |
| Nessun pre-mortem | **§4 pre-mortem**: 7 modi di fallire, con contromisura scritta *prima* |
| Nessun protocollo di collisione | **§3 regole di swarm**: file condivisi hanno un solo proprietario; gli altri consegnano dati, non modifiche |

## 1. I 6 LOTTI — perimetri disgiunti

> Regola sovrana: **un file ha esattamente un lotto proprietario.** Se il lotto B ha bisogno di un file del lotto A, aspetta A o consegna un dato che A integra. Mai due scritture sullo stesso file.

### LOTTO 1 — `MISURA` (abilita tutto il resto, parte per primo)
**Perimetro:** `empire/inspect/**` (nuovo), `empire/tests/test_inspect.py` (nuovo), **`empire/dash/kpi.py` limitatamente alla sostituzione dei placeholder `n/d (modulo inspect...)` con chiamate reali** — il punto di innesto ha un solo proprietario, ed è chi costruisce il modulo.
**Vietato:** il resto di `empire/dash/**`, `empire/flow/**`, `empire/cli.py` (file congelato — si usa il loop di plugin).
**Lavori:** A1 (modulo inspect: telemetry/scorecard/first_pass/ttd/feedback/traceability).
**DoD:** `python -m empire inspect status` esce 0 · i 6 KPI di telemetria hanno un valore reale o un "non applicabile" motivato, mai `n/d (non implementato)`.

### LOTTO 2 — `GATE` (verità dei gate)
**Perimetro:** `empire/flow/gate.py`, `empire/flow/state.py`, `empire/flow/cli.py`, `empire/tests/test_flow.py`, `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/workflows.yaml`.
**Vietato:** `empire/inspect/**`, `empire/dash/**`.
**Lavori:** A2 (default-plus-veto automatico: veto scaduto senza opposizione → decisione ATTIVA + fatto scritto, ADR-EST-006), A3 (Gate-CONTATTI legge l'evidenza da `lead.csv`, resta `human` ma con evidenza calcolata).
**DoD:** `python -m empire flow gates` → Gate-DEC 🟢 · Gate-CONTATTI mostra `contattati=N/7` contato dal CSV vero.

### LOTTO 3 — `CASSA` (il lotto con più €/h)
**Perimetro:** `Crea siti/Siti CCM/manuale.html`, `Crea siti/Siti CCM/thank-you.html`, `Crea siti/Siti CCM/checkout.config.json` (nuovo), `Crea siti/Siti CCM/pagamento.html` (nuovo), `empire/tools/checkout.py` (nuovo).
**Vietato:** tutto ciò che sta fuori da `Crea siti/Siti CCM/` e dal file tool.
**Lavori:** A4 (ladder checkout completa).
**DoD:** `grep -r YOUR_STRIPE "Crea siti/"` → 0 · `python empire/tools/checkout.py --check` → 0 placeholder · esiste un modo di pagare attivo **oggi** senza Stripe.

### LOTTO 4 — `PROVA` (sblocca S6 e l'outreach)
**Perimetro:** `Clienti/Prof Autocad/preventa-launch-kit/**` (nuovi file), `Crea siti/Preventa/**` (nuovo).
**Vietato:** `agency-empire/**` (già toccato da un'altra sessione — ADR-003, non si tocca).
**Lavori:** A5 (case study Novacar in HTML+PDF con numeri veri), A6 (landing Preventa standalone dal copy già scritto in `01_LANDING_COPY_ONE_PAGE.md`).
**DoD:** i file esistono, si aprono, contengono i numeri reali dei checkpoint Novacar (CP-20260702-003, CP-20260703-001), zero lorem.

### LOTTO 5 — `VIDEO` (S5, ladder obbligata)
**Perimetro:** `WORKFLOW-ESTATE/07-VIDEO-RUN/**` (nuovo), `empire/tools/video_pack.py` (nuovo).
**Vietato:** `.env` (mai scritto), `04-SKILLS-E-REFERENCE/**` (sola lettura).
**Lavori:** A7 (1 video E2E via ladder — Fliki è morta, chiave vuota).
**DoD:** o il file video esiste, o esiste il pacchetto-render completo (script a scene + TTS text + shot list + SEO pack) **e** l'errore è registrato onestamente. Mai dichiarare un video che non c'è.

### LOTTO 6 — `CHIUSURA` (memoria, igiene, anagrafe)
**Perimetro:** `empire/flow/eod.py` (nuovo), `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/**`, `empire/empire.toml` (sezione `[legacy_files]`), `company/REGISTRO-IMPRESA.md`, `skills-map.yaml`.
**Vietato:** i perimetri di 1-5.
**Lavori:** A9 (EOD/RETRO eseguibili), A10 (13 link riparati + registrazione ADR-008 degli artefatti nuovi).
**DoD:** `python -m empire conform WORKFLOW-ESTATE` → 0 block 0 warn · ogni artefatto nuovo dei lotti 1-5 è registrato.
**Vincolo:** parte **per ultimo** — deve registrare ciò che gli altri hanno prodotto.

### Ordine di esecuzione
```
ONDA 1 (parallela):  LOTTO 1 · LOTTO 3 · LOTTO 4 · LOTTO 5     ← nessuna dipendenza reciproca
ONDA 2 (parallela):  LOTTO 2                                    ← legge i fatti prodotti da onda 1
ONDA 3 (sequenziale): LOTTO 6                                   ← registra tutto il prodotto
```
LOTTO 2 è in onda 2 perché il Gate-FUNNEL va rivalutato **dopo** che il lotto 3 ha toccato le pagine: valutare prima significherebbe misurare un mondo che sta cambiando.

## 2. IL COMANDO UNICO — `python -m empire estate`
Il difetto peggiore di L2: dieci DoD sparse che nessuno rieseguirà mai tutte. L3 le fonde.

```
python -m empire estate          # verdetto complessivo, exit 0 = finito
python -m empire estate --json   # per la dashboard
```
Controlla in sequenza e stampa una riga per voce:
1. i 6 gate (`flow gates`)
2. zero placeholder di pagamento nelle pagine di vendita
3. esistenza reale degli artefatti promessi (case study, landing, pacchetto video)
4. `conform` a 0 block
5. i KPI di telemetria non sono `n/d (non implementato)`
6. suite test verde

**Exit code:** 0 solo se tutto è verde **o** rosso-con-azione-applicata-e-registrata. Un ⏳ vale rosso: *"nessun gate quasi verde"* (WF-MASTER §3).

## 3. REGOLE DI SWARM (il protocollo di collisione che mancava a L2)
1. **Un file, un proprietario.** Il perimetro di §1 è vincolante. Toccare fuori perimetro = difetto da correggere, anche se il codice funziona.
2. **File condivisi = consegna di dato, non modifica.** Chi ha bisogno che la dashboard mostri X non modifica la dashboard: scrive il fatto e il lotto 6 lo rende.
3. **Prompt idempotenti.** Ogni agente deve poter essere rilanciato: prima controlla se il lavoro c'è già, e in tal caso lo verifica invece di rifarlo (regola ADR-006).
4. **File congelati, mai toccati da nessuno:** `empire/cli.py`, `empire/paths.py`, `empire/config.py`, `empire/schema.py`, `empire/conform.py`. Le estensioni entrano dal loop di plugin già previsto.
5. **ADR-003 wrap:** i motori vivi (`empire_auto_v3.py`, carousel-factory, PreventivoForge) si avvolgono, non si riscrivono.
6. **Onestà di stato:** un agente che non riesce lo dichiara. Un lavoro dichiarato fatto e non fatto è il difetto più costoso del sistema — la dashboard che dava Gate-FUNNEL 🟢 mentre il file diceva `YOUR_STRIPE` è già costata una settimana.

## 4. PRE-MORTEM — 7 modi di fallire, contromisure decise ora

| # | Come fallisce | Contromisura (decisa PRIMA) |
|---|---|---|
| 1 | Due agenti scrivono lo stesso file → conflitto | perimetri disgiunti §1 + un solo proprietario per file |
| 2 | Un agente "chiude" un gate scrivendo un fatto falso | i gate `human` restano human: nessun agente può auto-confermarli, può solo **preparare l'evidenza** |
| 3 | Il video non si renderizza (no ffmpeg / no chiave) | ladder L-VIDEO: si consegna il pacchetto-render e si registra l'errore. Mai fingere |
| 4 | Il checkout "funziona" ma nessuno può pagare davvero | DoD richiede un metodo di pagamento **attivo oggi**, non un link vuoto in attesa di Stripe |
| 5 | Si costruisce il lotto 6 su artefatti non ancora esistenti | il lotto 6 è in onda 3, dopo tutti |
| 6 | Sessione finisce a metà → stato ambiguo | ogni lotto scrive il proprio checkpoint appena chiude, non alla fine di tutto |
| 7 | Si finisce l'infrastruttura e non la cassa | ordine di valore L2 §2 rispettato: LOTTO 3 (cassa) e LOTTO 4 (prova) sono in onda 1, non in coda |

## 5. Cosa resta GATED a Max dopo che ho finito
Alla fine di questo piano il Workflow Estate è completo **tranne** 4 azioni che sono sue e solo sue:
1. **2 Payment Link Stripe** → incolla in `checkout.config.json`, un comando riallinea tutto il sito.
2. **Canale YouTube + credenziali** (M-EST-8) → il video/pacchetto è già pronto da caricare.
3. **Ok all'invio outreach** (G-A4) → coda e messaggi già generati e verificati in dry-run.
4. **Conferma umana** di Gate-CONTATTI / S4 / S5 → l'evidenza è già calcolata, serve il suo "sì".

Queste 4 stanno in un unico file operativo: `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/AZIONI-MAX.md` (prodotto dal lotto 6).

---
⛓️ P12: `PIANO-COMPL-L3#estate-2026` · migliora: L2 · esegue: 6 lotti in 3 onde · verdetto: `python -m empire estate`
