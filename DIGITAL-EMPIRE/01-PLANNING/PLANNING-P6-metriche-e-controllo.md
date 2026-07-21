# PLANNING-P6 — Metriche, Revenue Math & Controllo
> Livello 6 di 7 · migliora P5: sostituisce le promesse con numeri misurabili. Chiude anche A-03 ("certezza >95%" resa onesta) e G-11 (soglia revenue in €).

## 1. Revenue math onesto (al posto dello stipite ">95%")

**S1 — Formula della certezza condizionale:**
```
P(≥1 chiusura) = 1 − (1 − p)^n     con n = lead contattati davvero, p = close-rate per lead caldo
```
| Scenario | n | p | P(≥1) | Chiusure attese (n×p) |
|----------|---|---|-------|------------------------|
| Esecuzione perfetta | 7 | 0,40 | **97,2%** | 2,8 |
| Esecuzione buona | 7 | 0,30 | 91,8% | 2,1 |
| Contatti parziali | 4 | 0,30 | 76,0% | 1,2 |
| Solo 2 contatti | 2 | 0,40 | 64,0% | 0,8 |

**Verità chirurgica:** il ">95%" esiste SOLO se (a) tutti i 7 vengono contattati entro 23/07 h12:00 **e** (b) il close-rate su lead caldi con prodotto pronto è ≥35%. Quindi la metrica-gate non è "revenue sì/no", è **"7/7 contattati"** — quella è in nostro pieno controllo. (Gate-CONTATTI, P5.)

**S2 — atteso prudente:** lista calda outreach + push Max. Con EUR 67 e traffico realistico: 0-5 vendite settimana 1 (non garantite — lo dice il dossier, lo confermiamo).

**Soglia minima settimana (G-11 chiuso):** **1 setup concessionario incassato** = settimana vinta. Target: 2-3 anticipi + prime vendite Manuale.

## 2. Albero KPI

```
NORTH STAR: € incassati entro 26/07 h23:59
├── S1 anticipi: contatti 7/7 → risposte → chiusure → € setup/canoni
├── S2 vendite: funnel live → visite checkout → vendite → €
└── compounding (non revenue, solo leading): caroselli pubblicati, video YT, kit S6 pronto
```

## 3. Tracker EOD (h19:00, comando memoria)

| Metrica (nome per `metric --name`) | Tipo | Target cumulato 26/07 |
|---|---|---|
| `s1_lead_contattati` | leading | 7 |
| `s1_risposte` | leading | ≥4 |
| `s1_anticipi_chiusi` | lagging | ≥1 (target 2-3) |
| `s1_incasso_eur` | lagging | >0 |
| `s2_funnel_live` (0/1) | leading | 1 entro 22/07 |
| `s2_vendite_manuale` | lagging | ≥1 |
| `s2_incasso_eur` | lagging | >0 |
| `s3_caroselli_pubblicati` | leading | ≥3 |
| `s4_pipeline_e2e` (0/1) | gate | 1 entro 24/07 o STANDBY dichiarato |
| `s5_video_test` (0/1) | leading | 1 (o fallback dichiarato) |
| `s6_kit_pronto` (0/1) | leading | 1 entro 24/07 |

Comando: `python3 00-MEMORY/memory_manager.py metric --name s1_anticipi_chiusi --value 1 --unit EUR`

## 4. Regole anti-vanity (R-10)
1. Follower, like, reach **non** sono risultati: compaiono solo come diagnostica sotto i KPI.
2. Ogni pagina riattivata deve puntare a UN funnel e produrre UNA metrica di business (regola dossier n.5, confermata).
3. La dashboard riporta prima gli € e i lead, poi (sotto il fold) il resto.

## 5. Dashboard
File unico: `07-CONTROL/DASHBOARD-E-RETRO.md` — aggiornato EOD da Claude con i valori del tracker + stato gate (🟢🟡🔴). RETRO domenica 26/07 secondo `00-MEMORY/RETRO-PROTOCOLLO.md`.

---
⛓️ Trace P12: `PLANNING-P6#estate-2026` · input: P5 · chiude: A-03, G-11, R-10
