---
Type: CONCEPT
Status: Active
Tags: #kpi #advertising #metriche #performance #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — L2.2 Advertising

> Metriche di performance del reparto. Nessuna baseline storica esiste: si stabilisce in M4
> (primo run reale) secondo il principio "niente numeri inventati" del Mandato.
> Dove non c'è baseline → indicato come [DM] (Da Misurare).
> Confronto: variante vs variante — MAI vs benchmark di settore esterni.
> Standard: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §7.2`

---

## KPI di campagna (per ogni campagna lanciata)

| KPI | Definizione | Owner | Frequenza | Note |
|---|---|---|---|---|
| **CTR (Click-Through Rate)** | Click / Impressioni per creative | AD6 | Quotidiana (campagne attive) | Confronto: variante A vs variante B; [DM] baseline al primo run |
| **CPC (Cost Per Click)** | Spesa / Click | AD6 | Quotidiana | Per piattaforma e creative; [DM] |
| **CPA (Cost Per Acquisition)** | Spesa / Conversioni | AD3 / AD6 | Aggiornata ogni 48h (dopo learning period) | Metrica definitiva per verdetto winner; [DM] baseline dal primo run reale |
| **CPL (Cost Per Lead)** | Spesa / Lead generati | AD3 / AD6 | Aggiornata ogni 48h | Variante di CPA per obiettivi lead gen; [DM] |
| **ROAS (Return On Ad Spend)** | Revenue attribuita / Spesa ads | ADS-LEAD | Fine campagna | Solo quando pipeline vendita è tracciata da AN2 (L2.4); [DM] nelle prime campagne |
| **Frequency** | Impressioni / Reach (volte viste per utente) | AD6 | Quotidiana (monitoraggio fatigue) | Alert automatico se >3 su audience fredda (segnale ad fatigue) |
| **Completion rate (video)** | % video visti fino alla fine | AD6 | Per campagne video | Indicatore qualità hook visivo; rilevante per Reels/TikTok; [DM] |

---

## KPI di processo (qualità del reparto)

| KPI | Definizione | Owner | Frequenza | Obiettivo |
|---|---|---|---|---|
| **G3 PASS rate** | % creative che passano compliance AD4 al primo tentativo | AD4 | Per ciclo campagna | Crescente — più il processo di brief è rodato, più le creative passano al primo giro |
| **AD-QA PASS rate** | % campagne che passano QA senza rework | AD-QA | Per ciclo campagna | [DM] — baseline dal primo lancio |
| **Varianti per ciclo di test** | N creative testate in WF-CREATIVE-TEST per ciclo | AD2 | Per ciclo test | Indicatore di efficienza del processo (non troppe, non troppo poche) |
| **Cicli di iterazione prima del winner** | N cicli WF-CREATIVE-TEST prima di identificare winner stabile | ADS-LEAD | Per campagna | Meno cicli = matrice iniziale più efficace; [DM] |
| **Gate bypass rate** | N gate saltati / N gate totali | ADS-LEAD | Per campagna | Deve essere 0 assoluto — ogni bypass è un incidente |
| **Approvazioni Max rispettate** | % lanci con approvazione registrata in state.json | ADS-LEAD | Per campagna | 100% — non negoziabile |

---

## KPI di apprendimento (qualità del loop)

| KPI | Definizione | Owner | Frequenza |
|---|---|---|---|
| **Pattern ADS scritti in namespace** | N record validi in `marketing/ads/patterns/*` | AD6 | Per ciclo chiuso |
| **Anti-pattern identificati** | N varianti perdenti documentate in `marketing/ads/experiments` | AD6 | Per ciclo chiuso |
| **Rapporto winner / total varianti** | % varianti testate che diventano winner | ADS-LEAD | Per trimestre |

---

## Come si misura (fonte dati)

1. **AN2 (L2.4)** traccia CTR/CPC/CPA per `copy_id` e `creative_id` dalle piattaforme.
2. **AD6** legge i dati da AN2 e produce analisi creative-level.
3. **AN3 (L2.4)** valida dimensione campione prima di ogni verdetto.
4. **ADS-LEAD** consolida il report di KPI al termine di ogni campagna per il CMO.

**Regola anti-rumore (Piano V2 §4b):** nessun KPI viene dichiarato definitivo prima che
la dimensione campione minima (validata da AN3) sia raggiunta. Un CTR di una creative vista
da 100 persone non è un dato affidabile.

---

## KPI di controllo (presidio vincoli operativi)

| KPI | Definizione | Valore atteso | Note |
|---|---|---|---|
| **Budget spend vs approvato** | delta% tra budget approvato da Max e spend effettivo | < 5% deviazione | Monitorato da Cost-Sentinel |
| **Dry-run compliance** | % campagne con dry_run: true al momento della consegna ad ADS-LEAD | 100% | Non negoziabile (Art.4.3) |
| **Approvazione Max pre-lancio** | % lanci con approval_timestamp in state.json | 100% | Non negoziabile (Art.4.3) |

---

## Connessioni

- [[README]] · `README.md` — missione e roster del reparto
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §7.2`
- [[state/README]] · `state/README.md` — schema state.json per tracciamento
- [[WF-ADS-PERFORMANCE]] · `workflow/WF-ADS-PERFORMANCE.md`
