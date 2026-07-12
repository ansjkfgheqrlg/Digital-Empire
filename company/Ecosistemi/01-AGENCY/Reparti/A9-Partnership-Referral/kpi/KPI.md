---
Type: KPI
Status: Active
Tags: #kpi #partnership #referral #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# KPI — A9 Partnership & Referral

> Owner della misura: `AG-A9-INTEL`. Owner del report ad `AG-DIR`: `AG-A9-COORD`.
> **[DM] = da misurare.** Nessuna baseline è stimata: il reparto è greenfield v2, il primo mese
> live definisce i numeri. Un valore inventato è violazione R7 (bloccante).

---

## Tabella KPI

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| **Lead da referral / mese** | `AG-A9-INTEL` | N. lead entrati via partner o segnale A7 nel periodo, contati su `agency/a9/referrals` (solo post-PASS gate) | [DM] | [DM] dopo 1° mese; poi crescita mese/mese |
| **Tasso conversione referral vs outreach diretto** | `AG-A9-INTEL` | % deal chiusi su lead A9 (fonte `agency/a8/deals`) confrontata con % su lead A2 (`agency/a2/pipeline`) | [DM] | Referral ≥ outreach diretto (ipotesi da verificare) |
| **Commissioni maturate** | `AG-A9-MGMT` | Somma commissioni dovute su deal chiusi, **solo** con `contratto_firmato=true` e importo da catalogo | [DM] | 100% tracciate; 0 fuori catalogo |
| **Lead non-ICP con esito tracciato** | `AG-A9-QUALIFY` | % lead ricevuti da A1 con esito (`partner`/`nurture`/`archivio`) scritto in `agency/a9/nonicp` | [DM] | **100%** (Zero-Loss, non negoziabile) |
| **Gate AG-A9-QA PASS al primo tentativo** | `AG-A9-QA` | % referral che passano ICP + consenso senza rework, sul totale referral sottoposti al gate | [DM] | [DM]; trend crescente = briefing partner efficace |
| **Partner attivi** | `AG-A9-MGMT` | N. partner in stato `attivo` (accordo firmato + commissione catalogo + briefing datato) | [DM] | [DM] |
| **Referral respinti per consenso mancante** | `AG-A9-QA` | N. lead respinti al Consent Gate / totale referral | [DM] | Tendere a 0 (indicatore di qualità del briefing) |

---

## Misurazione

| Aspetto | Regola |
|---|---|
| **Fonte** | Ogni metrica cita il namespace di origine (`agency/a9/*`, `agency/a8/deals`, `agency/a2/pipeline`). Metrica senza fonte ⇒ non pubblicabile. |
| **Conteggio referral** | Un lead conta **una sola volta**, al PASS del gate. I FAIL non entrano nel numeratore ma restano tracciati per il PASS-rate. |
| **Conversione** | Numeratore = deal chiusi confermati da A8; denominatore = referral instradati (A8 + A2). Mai stime. |
| **Commissioni** | Solo `stato=maturata`. Le `hold` (senza contratto) si riportano separatamente, mai sommate. |
| **PII** | Tutti gli aggregati su `partner_id` / `lead_ref`. Nessun dato personale nei report. |
| **Blocco pubblicazione** | Se la copertura esiti non-ICP < 100%, `AG-A9-INTEL` **non pubblica** il periodo (Zero-Loss Gate). |

---

## Cadenza

| Report | Frequenza | Da → A |
|---|---|---|
| Snapshot KPI reparto | Mensile | `AG-A9-INTEL` → `AG-A9-COORD` → `AG-DIR` |
| Partner scorecard | Mensile | `AG-A9-INTEL` → `AG-A9-MGMT` |
| Copertura Zero-Loss (esiti non-ICP) | A ogni chiusura batch | `AG-A9-QUALIFY` → `AG-A9-INTEL` |
| Commissioni maturate | Mensile (+ evento a deal chiuso) | `AG-A9-MGMT` → `AG-DIR` |
| Alert recidiva partner (≥2 FAIL consenso) | Evento | `AG-A9-INTEL` → `AG-A9-MGMT` → `AG-A9-COORD` |

---

## Connessioni

- [[ag-a9-intel]] · `agenti/ag-a9-intel.md` — owner della misura
- [[REGOLE]] · `regole/REGOLE.md` — R7 (zero metriche inventate), R6 (commissioni)
- [[ARCHITETTURA]] · `ARCHITETTURA.md` §6 — gate che condizionano i KPI
