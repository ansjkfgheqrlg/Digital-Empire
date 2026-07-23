# SPEC — Motore Dashboard & Metriche (GEM-05)

Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md Art.8 pilastro 6

Questo documento definisce la specifica dei KPI tracciati dal cruscotto dell'azienda, le loro fonti dati e i vincoli visivi.

---

## 1. Tassonomia dei KPI e Fonti Dati

Ogni metrica visualizzata deve provenire da una fonte eseguibile verificabile. Se il modulo di provenienza non è presente o la fonte dati è assente, lo stato viene visualizzato come `n/d` (non disponibile) con spiegazione del motivo.

### 1.1. Salute dell'Azienda (Company Health)

| ID | Nome KPI | Fonte Eseguibile / Calcolo | Tipo Dato |
|---|---|---|---|
| `agenti_progettati` | Agenti Progettati | `len(empire.loader.load_agents())` | Intero |
| `agenti_cf_grade` | Agenti CF-Grade | `len([a for a in loader.load_agents() if a.cf_grade])` | Intero |
| `ecosistemi_completi` | Ecosistemi Completi | `len([e for e in loader.load_ecosystems() if e.has_backbone and e.has_ecosistema_md])` (Target: 10) | Intero |
| `artefatti_adr008` | Conformi ADR-008 | Conteggio dei file completi di provenienza estratti da `empire/.data/census.json` | Intero |
| `link_rotti` | Link Rotti | Numero di link bloccanti estratti dal motore `registry links` o `links.py` | Intero |
| `workflow_conformi` | Workflow Art. 8 | Numero di workflow che soddisfano la presenza dei 6 pilastri organizzativi | Intero |
| `spazio_sprecato` | Spazio Duplicato | Somma di `wasted_bytes` estratta da `empire/.data/duplicates.json` | MegaByte (MB) |

### 1.2. Performance dell'Automazione (Telemetry - n/d in attesa di GEM-03)

| ID | Nome KPI | Fonte Eseguibile / Calcolo | Tipo Dato |
|---|---|---|---|
| `runs_giornalieri` | Esecuzioni/gg | `telemetry/runs/*.json` (Modulo `inspect` assente -> `n/d`) | Intero |
| `scorecard_5d` | Scorecard 5D | Scorecard generata (Modulo `inspect` assente -> `n/d`) | Decimale |
| `first_pass_rate` | First-pass Rate | `verification.first_pass` (Modulo `inspect` assente -> `n/d`) | Percentuale |
| `ttd_medio` | TTD Medio vs Bench | `benchmarks.py` (Modulo `inspect` assente -> `n/d`) | Durata |
| `tip_aperti` | TIP Aperti / Recurred | Atomi di feedback (Modulo `inspect` assente -> `n/d`) | Intero |
| `traceability_rate` | Checkpoint Coverage | Rapporto task con checkpoint/totale task (Modulo `inspect` assente -> `n/d`) | Percentuale |

### 1.3. Commerciale, Revenue e Gate Estate

| ID | Nome KPI | Fonte Eseguibile / Calcolo | Tipo Dato |
|---|---|---|---|
| `gates_settimanali` | 6 Gate Settimanali | Tabella parsed da `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-MASTER.md` + stato da `gates_status.json` | Tabella Stati |
| `lead_concessionari` | Stato 7 Lead | Caricato dal CSV `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/lead.csv` | Tabella Dati |
| `anticipi_incassati` | Anticipi Chiusi | Count di concessionari in stato `incassato` in `lead.csv` o `revenue.json` | Intero |
| `decisioni_attive` | Veto Scaduto | Atomi decision (Modulo `memory` assente -> `n/d`) | Intero |

---

## 2. Design Visuale e Palette di Colori

A causa dell'assenza della skill globale `dataviz`, viene applicata la palette neutra a 6 colori documentata conforme alle linee guida di accessibilità (contrasto AA):

### 2.1. Palette Colori Standard
- **Accent (Digital Empire Orange):** `#fb4604` (Orange brillante per pulsanti primari, brand ed evidenziazioni critiche)
- **Ink (Dark Theme Background/Card):** `#1e293b` (Slate scuro neutro per layout scuro)
- **Paper (Light Theme Background/Card):** `#f8fafc` (Grigio chiarissimo per layout chiaro)
- **Border/Muted:** `#64748b` o `#e2e8f0` (Grigio per bordi e testi di servizio)
- **Success (Green):** `#10b981` (Per indicatori verdi e gate superati)
- **Danger (Red/Alert):** `#ef4444` (Per indicatori rossi e gate falliti)

### 2.2. Distinzione Visiva dei Metadati
La dashboard deve mostrare visivamente lo stato della fonte:
- **Misurato (Pieno):** Indicatori e celle con bordi solidi e colore pieno (rappresenta un dato reale estratto programmaticamente).
- **Inserito a mano (Tratteggiato):** Indicatori circondati da un bordo tratteggiato (`border-style: dashed`) per i dati manuali (es. `lead.csv`).
- **Non Disponibile (Grigio):** Visualizzato in grigio opaco con icona informativa o tooltip esplicativo sul motivo (es. modulo mancante).
