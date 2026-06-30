---
Type: KPI
Status: Active
Tags: #kpi #content-factory #CF-R8 #apprendimento #ottimizzazione #pattern #improvement #post-produzione
Created: 2026-06-30
Last updated: 2026-06-30
---

# KPI — CF-R8 Apprendimento & Ottimizzazione

> **Reparto:** CF-R8 Apprendimento & Ottimizzazione · **Area:** Post-Produzione
> **Owner:** CF-R8-COORD · **Reporting:** L1-POST + CF-Director (report mensile)
> **[DM]** = Da Misurare: baseline non ancora disponibile; rilevare le prime 4 settimane di produzione reale.

---

## KPI primari (da monitorare ogni ciclo mensile)

| KPI | Definizione | Owner | Come si misura | Baseline |
|---|---|---|---|---|
| **Pattern validati/mese** | N. entry in `cf/patterns` con `ts_validazione` nel periodo; include hook, engine, failures distillati | CF-R8-QA | Conta entry con status "VALIDATO" create nel periodo | [DM] |
| **Fix proposti vs approvati vs implementati** | Ratio fix_proposti / fix_approvati / fix_implementati per ciclo mensile | CF-R8-COORD | Da `cf/improvements`: conta per stato nel periodo | [DM] |
| **Miglioramento first-pass rate nel tempo** | Delta first-pass rate CF-R6 mese M vs mese M-3 correlato con improvement implementati nello stesso periodo | CF-R8-COORD | Delta (first_pass_rate_M - first_pass_rate_M-3); solo se improvement chiuso con status RISOLTO | [DM] |
| **Pattern hook/angle aggiornati in CF-R1** | N. formule libreria CF-R1 aggiornate per mese a seguito di proposta CF-R8-HOOK | CF-R8-HOOK | Da log proposte CF-R1-LEARN accettate nel periodo | [DM] |
| **Latenza pattern→improvement implementato** | Giorni da `ts_validazione` del pattern a `ts_implementazione` dell'improvement corrispondente | CF-R8-COORD | Media (ts_implementazione - ts_validazione) per improvement chiusi nel periodo | [DM] |

---

## KPI secondari (monitorare per trend trimestrale)

| KPI | Definizione | Owner | Come si misura | Note |
|---|---|---|---|---|
| **Pattern scartati per n < 3 / ciclo** | N. candidati respinti dal Gate-N3 per ciclo; segnala maturità dei dati in ingresso | CF-R8-QA | Conta candidati con esito Gate-N3 FAIL nel periodo | Monitorare: alto scarto = volume produzione ancora basso; normale nelle prime fasi |
| **Improvement RECIDIVA** | N. improvement chiusi con verdetto RECIDIVA; segnala fix non efficaci | CF-R8-COORD | Conta entry `cf/improvements` con verdetto_finale "RECIDIVA" nel periodo | Deve tendere a 0 |
| **Pattern RISOLTI (no recidiva 90gg)** | N. pattern in `cf/failures` che non si ripresentano da ≥ 3 mesi dopo il fix | CF-R8-REASONING | Da revisione `cf/failures` trimestrale: conta status "RISOLTO" con ultima_occorrenza > 90gg fa | [DM] |
| **ADR bozze presentate al Board** | N. ADR bozze generate da pattern architetturali e presentate al Board | CF-R8-COORD | Da `company/Memory/decisions/ADR-bozza-*.md` con owner CF-R8 nel periodo | Non un obiettivo in sé; segnale di attività strutturale |
| **Feedback loop latency** | Giorni da pubblicazione contenuto a pattern distillato in `cf/patterns` per quel contenuto | CF-R8-COORD | Media (ts_validazione_pattern - ts_pubblicazione_ordine) per pattern hook del periodo | [DM]; obiettivo: ≤14gg (1 ciclo settimanale + buffer) |
| **Pattern engine validati/mese** | N. pattern engine in `cf/patterns` per ciclo mensile; segnala maturità comparazione engine | CF-R8-ENGINE | Conta entry tipo "engine" con ts nel periodo | [DM]; atteso 0 nelle prime fasi di produzione |
| **Sessioni neural_train completate** | N. sessioni CF-R8-NEURAL completate senza errori per trimestre | CF-R8-NEURAL | Da `neural-feed-report.json` nel periodo | [DM]; dipende dal volume di pattern validati |

---

## Come leggere i KPI (guida interpretazione)

**Pattern validati/mese:**
- Nelle prime 4 settimane: rilevare senza giudizio; il volume dipende dal volume di produzione CF-DE.
- Un valore basso non è un problema di CF-R8: è un segnale di volume produzione ancora basso.
- Un valore 0 per 2 cicli consecutivi → CF-R8-COORD verifica che CF-R6 stia alimentando `cf/failures`
  e che CF-R7 stia producendo feedback entries; se sì → dati ancora insufficienti per n ≥ 3.

**Fix proposti vs approvati vs implementati:**
- Un gap alto tra proposti e approvati → CF-Director sta rifiutando molte proposte;
  CF-R8-REASONING rivede la qualità delle proposte (evidenza insufficiente?).
- Un gap alto tra approvati e implementati → il reparto destinatario ha problemi di capacità;
  segnalare a L1-POST.

**Miglioramento first-pass rate nel tempo:**
- Questo è il KPI "sentinel" di CF-R8: se il first-pass rate CF-R6 non migliora nel tempo
  nonostante gli improvement implementati, qualcosa nel ciclo di apprendimento non funziona.
- Nota metodologica: il delta va attribuito con cautela — altri fattori (volume produzione,
  nuovi brand, nuovi formati) possono influenzare il first-pass rate indipendentemente dagli
  improvement. CF-R8-COORD segnala sempre il contesto quando riporta questo KPI.

**Latenza pattern→improvement implementato:**
- Obiettivo operativo: ≤30 giorni per fix puntuali; ≤60 giorni per fix strutturali.
- Una latenza alta segnala collo di bottiglia nel processo: o CF-Director approva lentamente,
  o il reparto destinatario non ha capacità di implementazione.

**Pattern scartati per n < 3:**
- Un alto tasso di scarto all'inizio è normale (volume produzione basso).
- Se dopo 3 mesi di produzione regolare il tasso di scarto è ancora > 70% → possibile che
  i brand attivi producano troppa varietà di format per accumulare n ≥ 3 sullo stesso hook_type;
  segnale per CF-R8-COORD di valutare focus su formati/brand principali.

---

## Reporting

| Cadenza | Report | Destinatario | Formato |
|---|---|---|---|
| Ogni ciclo settimanale (hook) | N. pattern hook candidati, validati, scartati | CF-R8-COORD (interno) | Log in `cf/improvements` con flag "ciclo_settimanale" |
| Ogni ciclo mensile | KPI primari completi + improvement status | L1-POST + CF-Director | `cf/improvements/report-YYYY-MM.json` |
| Trimestrale | KPI secondari + pattern RISOLTI + trend first-pass rate | CF-Director + 07-FORGE (se richieste aperte) | Sezione del report mensile di fine trimestre |

---

## Connessioni

- [[cf-r8-coord]] · `agenti/cf-r8-coord.md` — produce e consolida i KPI ogni ciclo; riporta a L1-POST
- [[WF-IMPROVEMENT-CYCLE]] · `workflow/WF-IMPROVEMENT-CYCLE.md` — il workflow che usa i KPI per misurare l'effetto dei fix
- [[CF-R6-QA-Gate/kpi/KPI]] · `../CF-R6-QA-Gate/kpi/KPI.md` — first-pass rate CF-R6 è il KPI sentinel di CF-R8
