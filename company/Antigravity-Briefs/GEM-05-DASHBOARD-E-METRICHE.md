---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md Art.8 pilastro 6
Esecutore: GEMINI (Antigravity) · Priorità: P1 · Created: 2026-07-22
Dipendenze: GEM-01 + GEM-03 chiusi (consuma GEM-04) · Blocca: nessuno
---

# GEM-05 — DASHBOARD & METRICHE
## Il cruscotto: l'azienda deve vedersi, non raccontarsi

> **LEGGI PRIMA:** `GEM-00`, consegne `GEM-01`/`GEM-03`.

---

## 1. IL PROBLEMA MISURATO

L'ecosistema `09-OPERATIONS` ha progettato `ops-dashboard-builder`, `ops-cost-accountant`,
`ops-cost-sentinel`, `ops-watchdog`, `ops-scheduler` — 10 agenti, più i reparti
`MONITORING-DASHBOARD/`, `COST-GUARD/`, `RUNTIME/`, `SCHEDULING/`. Tutti in Markdown.

Sul disco, oggi:
- `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/` → **vuota** (viola Art.8, pilastro 6)
- `company/Ispettorato/telemetry/` → **vuota** finché GEM-03 non gira
- nessun file `.html`, `.json` o `.csv` di metriche in tutto `company/`
- l'unico posto dove si legge lo stato dell'azienda è `STATO-EMPIRE.md`: un file di prosa che
  cresce in testa, dove per sapere "a che punto siamo" si legge a occhio

Conseguenza concreta: la settimana estate ha **6 gate con deadline oraria**
(`WF-MASTER.md`: DEC 21/07 20:00 · FUNNEL 22/07 20:00 · CONTATTI 23/07 12:00 · S4 24/07 20:00 ·
S5 23/07 18:00 · REV 26/07). Nessuno di questi gate ha un posto dove diventare 🟢 o 🔴.
Un gate senza cruscotto è un buon proposito.

**GEM-05 costruisce il cruscotto reale: un HTML autocontenuto + JSON, generati dai dati.**

---

## 2. SKILL DA USARE (verifica prima — GEM-00 §2)

| Skill | Path | Uso | Fallback |
|---|---|---|---|
| `dataviz` | skill di sistema (`dataviz`) | **leggila prima di scegliere un solo colore o tipo di grafico**: definisce la formula di colore, le mark spec, la leggibilità in light/dark | palette neutra a 6 colori documentata |
| `master-app-builder` | `.claude/skills/master-app-builder/` | la dashboard va poi montata come modulo di EmpireDesk: rispetta i suoi pattern | modulo standalone |
| `frontend-design` | `~/.claude/skills/frontend-design/` | qualità visiva | CSS minimale sobrio |
| `verification-quality` | `.claude/skills/verification-quality/` | gate: i numeri mostrati coincidono con la sorgente? | §6 |
| `empire-premium-style` | `~/.claude/skills/empire-premium-style/` | **solo se** Max chiede il look Empire (arancio #fb4604 / ink / silver, font Onest) | look sobrio di default |
| `hooks-automation` | `.claude/skills/hooks-automation/` | rigenerazione automatica a fine giornata | `.bat` schedulato documentato |

**Nota su EmpireDesk:** esiste già `EmpireDesk/modules/metrics.py` (modulo caricato, 7 moduli
attivi, selftest 16/16 PASS). **Non riscriverlo.** La dashboard deve poterlo alimentare o
essere consumata da lui. Leggi `EmpireDesk/app.py` e `modules/metrics.py` prima di progettare.
`EmpireDesk/platform/` è ownership Max: **non toccare**.

---

## 3. LE METRICHE — solo ciò che esiste davvero

Regola dura: **una metrica che non ha una sorgente misurabile non entra nella dashboard.**
Niente KPI aspirazionali. Se il dato non c'è, la cella dice `n/d` con il motivo.

### 3.1 Salute dell'azienda (da GEM-01 + GEM-04)
| Metrica | Sorgente | Oggi vale |
|---|---|---|
| Agenti progettati | `empire agents --json` | ~300+ |
| Agenti CF-grade (7 file) | `empire.schema.Agent.cf_grade` | da misurare |
| Ecosistemi con BACKBONE + ECOSISTEMA.md | census | 10/10 da verificare |
| Artefatti con intestazione ADR-008 | `registry orphans` | **basso** |
| Link rotti | `registry links` | **≥26** |
| Workflow conformi Art.8 (6/6 pilastri pieni) | `conform` | **0** prima di GEM-04 TASK 7 |
| MB duplicati | `registry dupes` | da misurare |

### 3.2 Performance (da GEM-03)
| Metrica | Sorgente |
|---|---|
| Run per giorno, per agente, per workflow | `telemetry/runs/*.json` |
| Media 5D per asse | scorecard |
| First-pass rate | `verification.first_pass` |
| TTD medio vs benchmark | `benchmarks.py` |
| TIP aperti / acked / confirmed / **recurred** | atomi `feedback` |
| Pattern ReasoningBank: DRAFT vs UFFICIALI | atomi `pattern` |
| **Traceability rate** = task con checkpoint / task totali | ADR-002 |

### 3.3 Revenue e gate estate (da 07-CONTROL + memoria)
| Metrica | Sorgente | Nota |
|---|---|---|
| 6 gate della settimana con stato 🟢/🔴/⏳ e deadline | `WF-MASTER.md` + atomi memoria | il cuore operativo |
| 7 lead concessionari: contattato / risposto / preventivo / incassato | `DIGITAL-EMPIRE/07-CONTROL/LISTA-7-LEAD.md` | **inserimento manuale**: prevedi un file `06-DASHBOARD-E-METRICHE/lead.csv` che Max aggiorna a mano |
| Anticipi incassati | `mem list --kind metric --name anticipi_chiusi` | KPI REV |
| Decisioni con veto scaduto → ATTIVE | atomi `decision` | enforcement automatico |

**Distingui sempre, visivamente, tre stati:** `misurato` (verde/pieno) · `inserito a mano`
(bordo tratteggiato) · `n/d` (grigio + motivo in tooltip). Un cruscotto che confonde un dato
reale con una stima è peggio di nessun cruscotto.

---

## 4. ARCHITETTURA RICHIESTA

```
empire/dash/
├── __init__.py
├── SPEC.md
├── collect.py      # interroga empire.index / inspect / registry → un solo dict
├── kpi.py          # definizione dichiarativa dei KPI: id, label, sorgente, soglie, formato
├── render_md.py    # → WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/DASHBOARD.md (leggibile a occhio)
├── render_html.py  # → empire/.data/dashboard.html (autocontenuto, zero CDN)
├── history.py      # snapshot giornalieri → trend
├── cli.py
└── tests/
```

### 4.1 `kpi.py` — dichiarativo, non hardcoded
```python
KPI(id="link_rotti", label="Link rotti", source="registry.links.dead_end",
    fmt="int", good="== 0", warn="<= 5", bad="> 5", owner="FORGE")
```
Aggiungere un KPI = aggiungere una riga. Nessun numero cablato nel renderer.

### 4.2 `render_html.py` — vincoli duri
- **File singolo, autocontenuto.** CSS e JS inline. **Zero richieste esterne** (no CDN, no font
  remoti, no immagini remote): deve aprirsi con doppio click, offline, e funzionare.
- Dati embeddati come `<script type="application/json">`, non fetch.
- **Tema chiaro e scuro** via `prefers-color-scheme` + override `[data-theme]`.
- Responsive: tabelle larghe dentro un contenitore `overflow-x:auto`; il body non scrolla mai
  in orizzontale.
- Grafici: **SVG inline generato da Python**. Niente librerie JS di charting.
- Applica `dataviz`: forma del grafico scelta in base al dato (trend → linea, confronto
  categorie → barre, quota → non usare torte con >5 fette), palette coerente, contrasto AA.

### 4.3 `render_md.py`
`WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/DASHBOARD.md` — versione testuale, perché Max e Gael
la leggono da GitHub e dal telefono. Tabelle Markdown, semafori con emoji, in testa il blocco
**"I 6 gate della settimana"** con deadline e stato. Data di generazione sempre in cima.

### 4.4 `history.py`
Snapshot giornaliero in `empire/.data/history/<YYYY-MM-DD>.json`. Append-only, mai sovrascritto.
Serve ai trend: "link rotti: 26 → 4 in 5 giorni" è il segnale che l'azienda sta migliorando —
esattamente ciò che oggi manca.

### 4.5 `cli.py`
```
python -m empire dash build            # md + html + snapshot
python -m empire dash show             # apre l'html nel browser di default
python -m empire dash kpi link_rotti   # un singolo KPI, per script
python -m empire dash trend --days 14
python -m empire dash gates            # solo i 6 gate estate, output compatto da terminale
```

---

## 5. SEQUENZA

**TASK 1 — Ricognizione.** Verifica skill. **Leggi `dataviz` per intero prima di scrivere una
riga di CSS.** Leggi `EmpireDesk/modules/metrics.py`, `EmpireDesk/app.py`,
`DIGITAL-EMPIRE/07-CONTROL/`, `WF-MASTER.md` (mappa gate).
Output `empire/dash/SPEC.md` con **la tabella completa dei KPI e la loro sorgente esatta**.
**Gate 1**: ogni KPI ha una sorgente eseguibile, o è marcato `manuale`. Zero KPI senza sorgente.

**TASK 2 — `collect.py` + `kpi.py`.** **Gate 2**: `dash kpi link_rotti` restituisce il numero
reale, coincidente con `registry links`. Incolla i due output.

**TASK 3 — `render_md.py`.** **Gate 3**: `06-DASHBOARD-E-METRICHE/DASHBOARD.md` esiste, è
popolato con dati veri, e `empire conform --workflow WORKFLOW-ESTATE` non segnala più il
pilastro 6 vuoto. Incolla il conform prima/dopo.

**TASK 4 — `render_html.py`.** **Gate 4**: apri l'HTML **offline** (disconnetti la rete o usa
un profilo browser senza cache) → si vede tutto, zero risorse mancanti. Incolla il conteggio
delle richieste esterne = 0 (dimostrabile con `grep -c "https\?://" dashboard.html` limitato
agli attributi `src`/`href`).

**TASK 5 — `history.py` + trend.** **Gate 5**: 3 snapshot con dati diversi → il grafico di trend
mostra 3 punti corretti.

**TASK 6 — Integrazione EmpireDesk.** Esponi la dashboard come modulo: rispetta il contratto
esistente di `EmpireDesk/modules/*.py` (leggilo, non inventarlo) e registra una tile.
**Non toccare `platform/`.** Se il contratto non è chiaro, **fermati e documenta la domanda**
invece di indovinare: `app.py` è ownership Gael.
**Gate 6**: `python EmpireDesk/app.py --selftest` continua a passare (16/16 o superiore).
Incolla l'output. Se scende sotto 16, hai rotto qualcosa: torna indietro.

**TASK 7 — Automazione.** `.bat` + istruzione Task Scheduler per rigenerare ogni sera alle 19:00
(coerente con `WF-MEM-EOD` di `WF-MASTER.md`). **Documenta, non schedulare** senza approvazione.

**TASK 8 — Chiusura.** README, checkpoint via GEM-02, consegna GEM-00 §4.

---

## 6. DEFINITION OF DONE

- [ ] DoD-1 — `06-DASHBOARD-E-METRICHE/` **non è più vuota**, pilastro 6 conforme
- [ ] DoD-2 — HTML autocontenuto: **0 richieste esterne**, apribile offline (dimostrato)
- [ ] DoD-3 — funziona in tema chiaro E scuro (2 screenshot o descrizione del test)
- [ ] DoD-4 — ogni numero mostrato è ri-derivabile con un comando `empire *` (elenca la mappa)
- [ ] DoD-5 — i 3 stati (misurato / manuale / n/d) sono distinguibili a colpo d'occhio
- [ ] DoD-6 — i 6 gate estate compaiono con deadline e stato
- [ ] DoD-7 — trend su ≥3 snapshot funzionante
- [ ] DoD-8 — `EmpireDesk --selftest` ≥ 16/16 dopo l'integrazione
- [ ] DoD-9 — `EmpireDesk/platform/` non modificato (`git status` incollato)
- [ ] DoD-10 — nessun KPI inventato: SPEC dimostra la sorgente di ognuno
- [ ] DoD-11 — `dash build` idempotente: 2 run consecutivi → 1 solo snapshot per giorno
- [ ] DoD-12 — pytest ≥ 15 test verdi, zero crash Unicode

---

## 7. ANTI-PATTERN

| Anti-pattern | Perché rifiutato |
|---|---|
| KPI aspirazionali senza sorgente ("engagement", "brand health") | Numero finto = cruscotto inutile. |
| CDN, font remoti, Chart.js | Deve funzionare offline, con doppio click, per sempre. |
| Dato inserito a mano indistinguibile da dato misurato | È il modo più rapido per prendere decisioni sbagliate. |
| Toccare `EmpireDesk/platform/` | Ownership Max, ordine esplicito del 2026-07-21. |
| Riscrivere `modules/metrics.py` | ADR-003. Si legge il contratto e ci si aggancia. |
| Numeri cablati nel renderer | Il KPI si aggiunge in `kpi.py`, una riga. |
| Torta con 9 fette | `dataviz`. Serve una barra. |
| Schedulare il task automatico senza chiedere | Cambia il flusso quotidiano di due persone. |

---

## 8. HANDOFF

A Max: la dashboard rende visibile, per la prima volta, **il divario tra azienda progettata e
azienda funzionante** (agenti progettati vs agenti CF-grade vs agenti mai eseguiti). Quel numero
è la vera misura di completamento dell'impresa, e va guardato ogni giorno.

A Claude: i KPI marcati `manuale` sono candidati ad automazione futura — vanno in
`company/Memory/BACKLOG.md`, non lasciati impliciti.
</content>
