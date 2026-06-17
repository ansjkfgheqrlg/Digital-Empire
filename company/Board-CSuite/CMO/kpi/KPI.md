---
Type: CONCEPT
Status: Active
Tags: #cmo #kpi #metriche #apsoc #campagna #performance
Created: 2026-06-17
Last updated: 2026-06-17
---

# KPI — CMO (Chief Marketing Officer)

> KPI del team CMO. Fonte: Blueprint `BP-CMO.md` + Mandato Art.4.2.
> Convenzione: [DM] = "Da Misurare" → metrica reale richiede storico campagna o setup tracking.
> KPI senza [DM] hanno metodo di misura determinabile oggi. Nessun target inventato.

---

## KPI di Gate (non negoziabili)

Questi KPI non hanno target "aspirazionali": sono binari o sogliati. Un valore fuori soglia
è un blocco operativo, non un segnale di miglioramento.

| KPI | Target | Metodo di misura | Owner |
|---|---|---|---|
| Gate APSOC bypassati | **0** | n. output in produzione senza `gate_pass: true` in brand-gate-log | cmo-brand-voice-warden |
| Output con CPB violato in pubblicazione | **0** | n. output pubblicati con claim senza proof rilevato post-gate | cmo-brand-voice-warden |
| Lancio senza prezzo approvato | **0** | n. lanci avviati con WF-LANCIO-COORD senza `prezzo_approvato: true` | cmo-launch-coordinator |
| Campagne con spesa senza dry-run | **0** | n. spese attivate senza `dry_run_approvato: true` in lancio-log | cmo-conductor |

---

## KPI di Qualità Copy

| KPI | Target | Metodo di misura | Owner | Note |
|---|---|---|---|---|
| Score APSOC medio output standard | **≥ 80/100** | media da `brand-gate-log/aggregate-stats.json` | cmo-brand-voice-warden | calcolato per ciclo/trimestre |
| Score APSOC medio sales page | **≥ 85/100** | media filtrata per formato `sales_page` in brand-gate-log | cmo-brand-voice-warden | |
| First-pass rate gate brand (standard) | **> 70%** | n. output PASS primo check / tot output sottomessi | cmo-brand-voice-warden | fonte: v1 `CMO.md` |
| Output senza brand_kit dichiarato rimandati | **100%** | n. brief rimandati per brand_kit mancante / tot brief mancanti | cmo-marketing-liaison, cmo-content-liaison | deve essere 100%: ogni mancanza viene rimandato |

---

## KPI di Performance Campagna

| KPI | Target | Metodo di misura | Owner | Note |
|---|---|---|---|---|
| Reply rate cold email | **≥ 5%** | n. risposte / n. email inviate (per campagna) | cmo-performance-analyst | fonte: v1 `CMO.md`; misurabile da tool email |
| CTR per canale e variante | [DM] | click / impression per campagna e variante (da analytics canale) | cmo-performance-analyst | da settare tracking per ogni canale attivo |
| CVR sales page | [DM] | acquisti / visitatori (da analytics landing) | cmo-performance-analyst | richiede setup pixel/analytics |
| CPA (costo per acquisizione) | [DM] | spesa campagna / n. lead qualificati (o acquisti) | cmo-performance-analyst | calcolabile dopo prime campagne con budget |
| Lead qualificati per campagna | [DM] per campagna | n. lead con criteri ICP rispettati (qualifica da CRO/AGENCY) | cmo-performance-analyst | target si definisce per campagna, non globale |

---

## KPI di Intelligence e Pattern

| KPI | Target | Metodo di misura | Owner |
|---|---|---|---|
| Pattern ICP consolidati in cmo-memoria | **crescita YoY** | n. pattern con `validato: true` a fine anno vs inizio anno | cmo-memoria |
| Profili ICP aggiornati ≤90gg | **100% dei profili attivi** | n. profili con `data_aggiornamento` ≤90gg / tot profili attivi | cmo-audience-intel |
| Alert ICP drift emessi e azioni intraprese | [DM] | n. alert / n. campagne che hanno cambiato target dopo alert | cmo-audience-intel | misura efficacia intelligence |

---

## KPI Operativi del Team

| KPI | Target | Metodo di misura | Owner |
|---|---|---|---|
| Report performance per campagna chiusa | **100%** | n. report prodotti / n. campagne concluse | cmo-performance-analyst |
| Monitoraggio 72h completato per lancio | **100%** | n. report 72h / n. lanci eseguiti | cmo-launch-coordinator |
| Brief rifiutati per campi mancanti (iterazioni) | **tendere a 0** | n. brief rimandati per pre-condizioni incomplete / tot brief | cmo-conductor |

---

## Cadenza di review

- **Ogni campagna:** KPI di performance specifici alla campagna (report a chiusura).
- **Settimanale:** score APSOC medio + first-pass rate (da brand-gate-log aggregato).
- **Trimestrale:** tutti i KPI con trend, retrospettiva, aggiornamento target [DM] con valori reali.
- **Annuale:** KPI YoY, crescita pattern ICP in cmo-memoria, review soglie APSOC (invarianti dal Mandato).

---

## Connessioni

- [[BP-CMO]] · `company/Board-CSuite/_BLUEPRINT/BP-CMO.md` — fonte KPI
- [[cmo-performance-analyst]] · `agenti/cmo-performance-analyst.md`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[cmo-memoria]] · `agenti/cmo-memoria.md`
- [[state/README.md]] — dove vivono i dati che alimentano questi KPI
- [[MANDATO-EMPIRE]] Art.4.2 (soglie APSOC) + Art.4.1 (gate non bypassabili = KPI 0)
