---
Type: KPI
Status: Active
Tags: #kpi #content-factory #CF-R2 #brand-kit #metriche #registry
Created: 2026-06-19
Last updated: 2026-06-19
---

# KPI — CF-R2 Brand-Kit & Tenant Registry

> Tutte le metriche con baseline [DM] sono da misurare sul campo e non vengono inventate.
> Owner primario: `cf-r2-coord` · Report: settimanale a L1-PRE.

---

## Metriche operative

### 1. Tenant attivi nel registry

| Campo | Valore |
|---|---|
| **Definizione** | N. brand con stato "approvato" nel namespace `cf/brand-kits` |
| **Come si misura** | Count di entry in `cf/brand-kits` con `stato: "approvato"` |
| **Frequenza** | Snapshot settimanale + delta rispetto alla settimana precedente |
| **Owner** | CF-R2-COORD |
| **Baseline** | 4 (i 4 brand seed carousel-factory dopo onboarding CF-grade) |
| **Target** | [DM] — stabilito dal CF-Director in base agli ordini attivi |

---

### 2. Brand_kit completi vs incompleti

| Campo | Valore |
|---|---|
| **Definizione** | N. brand_kit con gate CF-R2-QA PASS / N. totale brand nel registry (inclusi in_onboarding) |
| **Come si misura** | Count `gate_qa: "PASS"` in `state.json` per ogni brand / count totale entry `cf/brand-kits` |
| **Frequenza** | Misurata a ogni onboarding completato o tentato |
| **Owner** | CF-R2-QA (rileva il dato), CF-R2-COORD (riporta) |
| **Target** | 100% dei brand approvati con gate PASS (invariante — non ha senso avere brand approvato senza gate) |
| **Soglia attenzione** | Brand in stato "in_onboarding" da >72h → escalation a L1-PRE |

---

### 3. Drift alerts per ciclo

| Campo | Valore |
|---|---|
| **Definizione** | N. alert emessi da CF-R2-DRIFT nel ciclo di produzione / N. brand approvati campionati |
| **Come si misura** | Count alert in `drift-reports/` per ciclo / N. brand con campionamento eseguito |
| **Frequenza** | Per ogni ciclo di produzione (cadenza definita da CF-Director) |
| **Owner** | CF-R2-DRIFT (rileva), CF-R2-COORD (riporta) |
| **Baseline** | [DM] — da rilevare nei primi 3 cicli di produzione |
| **Target** | Trend decrescente ciclo su ciclo (il drift diminuisce man mano che i processi si stabilizzano) |
| **Soglia critica** | Alert su stesso brand per 2 cicli consecutivi → WF-BRAND-MAINTENANCE obbligatorio |

---

### 4. Latenza onboarding

| Campo | Valore |
|---|---|
| **Definizione** | Ore da ricezione richiesta onboarding a brand con stato "approvato" in registry |
| **Come si misura** | `timestamp_approvazione` - `timestamp_richiesta_onboarding` (da state.json) |
| **Frequenza** | Per ogni onboarding completato |
| **Owner** | CF-R2-COORD |
| **Baseline** | [DM] — da rilevare sui primi 4 onboarding (i 4 brand seed) |
| **Target** | [DM] — stabilito dopo prima baseline (dipende da complessità brief e disponibilità committente) |
| **Nota** | La latenza include il tempo di attesa per risposte committente (domande ICP, logo, font) — distinguere latenza interna CF-R2 vs latenza esterna committente |

---

### 5. % brand_kit PASS al primo gate

| Campo | Valore |
|---|---|
| **Definizione** | N. brand_kit che superano gate CF-R2-QA senza rework / N. tot brand_kit sottoposti a gate nel periodo |
| **Come si misura** | Count `gate_pass_primo_tentativo: true` in `state.json` / N. onboarding nel periodo |
| **Frequenza** | Mensile |
| **Owner** | CF-R2-QA (rileva), CF-R2-COORD (riporta) |
| **Baseline** | [DM] |
| **Target** | [DM] — un tasso basso indica che il brief onboarding ha lacune sistematiche → segnale per 07-FORGE |

---

### 6. Latenza WF-BRAND-MAINTENANCE

| Campo | Valore |
|---|---|
| **Definizione** | Ore da alert drift a brand_kit patchato con gate PASS |
| **Come si misura** | `timestamp_gate_pass_patch` - `timestamp_alert_drift` (da state.json) |
| **Frequenza** | Per ogni manutenzione completata |
| **Owner** | CF-R2-COORD |
| **Baseline** | [DM] |
| **Target** | [DM] — priorità alta per drift ricorrente (impatta produzione in corso) |

---

## Report a L1-PRE (formato settimanale)

CF-R2-COORD produce ogni settimana un report strutturato per il capo area Pre-Produzione:

```json
{
  "settimana": "YYYY-WNN",
  "tenant_attivi": 4,
  "brand_kit_completi": 4,
  "brand_in_onboarding": 1,
  "drift_alerts_ciclo": 0,
  "brand_con_drift_ricorrente": 0,
  "onboarding_completati": 1,
  "latenza_media_onboarding_ore": "[DM]",
  "manutenzioni_eseguite": 0,
  "note": "onboarding vendi-la-skill completato; nessun alert drift; 4 brand seed carousel-factory onboardati"
}
```

---

## Connessioni

- [[cf-r2-coord]] · `agenti/cf-r2-coord.md` — owner primario KPI e report L1-PRE
- [[cf-r2-drift]] · `agenti/cf-r2-drift.md` — fonte dati drift alerts
- [[cf-r2-qa]] · `agenti/cf-r2-qa.md` — fonte dati gate completi/incompleti
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R2 KPI`
