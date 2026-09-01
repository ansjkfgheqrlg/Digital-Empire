# REF_15 — Post-Launch Review Templates
## Sistema di Review Post-Lancio per Prodotti e Feature

Questi template permettono di chiudere il ciclo PRD → Sviluppo → Lancio → Apprendimento. Ogni PRD eccellente prevede già QUANDO e COME si farà la review post-lancio. Questi template vanno inclusi nella sezione "Post-Launch" del PRD o allegati come appendice.

---

## Filosofia della Post-Launch Review

Un PRD senza review post-lancio è un documento a senso unico. La review è il momento in cui:
1. Verifichi se il problema che hai risolto era quello reale
2. Misuri se le metriche che avevi previsto si sono materializzate
3. Documenti cosa hai imparato (non solo cosa ha funzionato)
4. Decidi il prossimo passo: iterate, expand, kill, or accept

---

## TEMPLATE A — 2-Week Pulse Review

### Quando usarlo
Entro 14 giorni dal lancio. Focus su: stabilità tecnica, errori critici, feedback immediato degli early adopters.

```markdown
# Post-Launch Pulse Review — [Nome Feature/Prodotto]
**Data lancio**: [Data]
**Data review**: [Data + 14 giorni]
**Autore review**: [Nome PM]
**Partecipanti**: [PM, Lead Eng, Designer, Data Analyst]

---

## 1. Stato di Salute Tecnica

### Uptime & Performance
| Metrica | Target (dal PRD) | Attuale | Status |
|---------|-----------------|---------|--------|
| Uptime | 99.9% | [X]% | 🟢/🟡/🔴 |
| API P95 latency | <500ms | [X]ms | 🟢/🟡/🔴 |
| Error rate | <0.1% | [X]% | 🟢/🟡/🔴 |
| Page load P95 | <2s | [X]s | 🟢/🟡/🔴 |

### Bug Report Summary
| Severity | Count aperto | Count chiuso | P0 risolti in <24h? |
|----------|-------------|-------------|---------------------|
| P0 (critico) | [N] | [N] | Sì/No |
| P1 (major) | [N] | [N] | - |
| P2 (minor) | [N] | [N] | - |

**Incidenti rilevanti**:
- [Incidente 1]: [data, durata, impatto utenti, risoluzione]
- [Incidente 2]: [...]

---

## 2. Adoption Iniziale

### Funnel di Adoption (prime 2 settimane)
| Step | Utenti coinvolti | Conversion |
|------|-----------------|------------|
| Feature released (base utenti) | [N totale] | - |
| Utenti che hanno visto la feature | [N] | [X]% |
| Utenti che l'hanno provata | [N] | [X]% |
| Utenti che l'hanno usata 2+ volte | [N] | [X]% |

**Commento**: [trend rispetto alle aspettative del PRD]

---

## 3. Feedback Qualitativo Immediato

### Canali monitorati
- [ ] Support tickets: [N ticket su questa feature] — sentiment: positivo/neutro/negativo
- [ ] NPS survey: [N rispondenti] — score medio: [X]
- [ ] Social media mentions: [N] — sentiment predominante
- [ ] Intercom / chat: [N conversazioni] — temi ricorrenti

### Top 3 Feedback Positivi
1. "[Quote reale utente]" — [fonte, data]
2. "[Quote reale utente]"
3. "[Quote reale utente]"

### Top 3 Feedback Negativi / Confusioni
1. "[Quote reale utente]" — [fonte, data] → **Azione**: [cosa farete]
2. "[Quote reale utente]" → **Azione**: [...]
3. "[Quote reale utente]" → **Azione**: [...]

---

## 4. Decisioni Immediate

| Decisione | Opzioni | Scelta | Motivazione | Owner | Deadline |
|-----------|---------|--------|-------------|-------|----------|
| [Es: gestire edge case X] | Fix ora / Accetta / Schedula | [scelta] | [motivazione] | [nome] | [data] |

---

## 5. Go/No-Go per Full Rollout (se in staged rollout)

**Attuale rollout**: [X]% utenti
**Prossimo step**: [Y]% o 100%

Checklist Go:
- [ ] Zero P0 bug aperti
- [ ] Error rate < target
- [ ] Nessun feedback critico blocca la UX principale
- [ ] Support team ha documentazione aggiornata

**Decisione**: 🟢 GO — 🟡 GO con fix urgenti — 🔴 ROLLBACK

**Motivazione**: [testo]
```

---

## TEMPLATE B — 30-Day Product Review

### Quando usarlo
30 giorni dopo il lancio. Focus su: metriche vs target del PRD, pattern di utilizzo reale vs aspettative, priorità di iterazione.

```markdown
# 30-Day Product Review — [Nome Feature/Prodotto]
**Data lancio**: [Data]
**Data review**: [Data + 30 giorni]
**PRD originale**: [link o versione]
**Autore review**: [Nome PM]

---

## 1. Scorecard Metriche (vs PRD)

### North Star Metric
| | Target PRD | Attuale Day 30 | Gap | Trend |
|--|-----------|----------------|-----|-------|
| [North Star Metric] | [X] | [Y] | [±Z%] | ↑↓→ |

**Interpretazione**: [In linea / Sotto target — perché / Sopra target — perché]

### Primary Metrics
| Metrica | Target PRD | Attuale | Status | Driver principale |
|---------|-----------|---------|--------|------------------|
| [Metrica 1] | [X] | [Y] | 🟢/🟡/🔴 | [cosa sta guidando questo numero] |
| [Metrica 2] | [X] | [Y] | 🟢/🟡/🔴 | [driver] |
| [Metrica 3] | [X] | [Y] | 🟢/🟡/🔴 | [driver] |

### Guardrail Metrics (non devono peggiorare)
| Metrica guardrail | Baseline pre-lancio | Attuale | Impatto |
|------------------|---------------------|---------|---------|
| [Metrica 1] | [X] | [Y] | Nessuno / Positivo / ⚠️ Negativo |
| [Metrica 2] | [X] | [Y] | |

---

## 2. Utilizzo Reale vs PRD

### Feature Usage Breakdown
| Feature/Componente | Utilizzo atteso | Utilizzo reale | Delta | Insight |
|-------------------|----------------|----------------|-------|---------|
| [Feature A] | [X%] utenti | [Y%] utenti | [±Z] | [spiegazione] |
| [Feature B] | [X%] utenti | [Y%] utenti | [±Z] | [spiegazione] |
| [Feature C — "nice to have"] | [X%] | [Y%] | [±Z] | [spiegazione] |

### Pattern Inattesi Rilevati
1. **[Pattern 1]**: [descrizione comportamento utenti non previsto nel PRD]
   - Implicazione: [cosa significa per il prodotto]
   - Azione: [cosa fare]

2. **[Pattern 2]**: [descrizione]
   - Implicazione: [...]
   - Azione: [...]

---

## 3. User Research Quick Hits

### Interviste utenti (target: 5-8 interviste in 30 giorni)
- Interviste condotte: [N]
- Profili intervistati: [tipo 1 N, tipo 2 N]

**Tema ricorrente 1 — [Nome tema]**
*Evidence*: [N]/[N] utenti l'hanno menzionato
*Quote rappresentativa*: "[...]"
*Insight*: [cosa significa]
*Azione consigliata*: [...]

**Tema ricorrente 2 — [Nome tema]**
[...]

---

## 4. Hypothesis Validation

Per ogni ipotesi dichiarata nel PRD originale:

| Ipotesi PRD | Validata? | Evidenza | Confidenza |
|------------|-----------|---------|------------|
| "Gli utenti useranno X per Y" | ✅ Confermata | [dato] | Alta |
| "Il problema Z è la frustrazione principale" | ❌ Smentita | [dato contrario] | Media |
| "La feature A riduce il churn" | ⏳ Non ancora misurabile | - | - |

**Ipotesi più sorprendente smentita**: [nome] — [cosa significa per il prodotto]

---

## 5. Segmentazione Performance

### Performance per segmento utente
| Segmento | Adoption rate | Engagement | Retention D30 | Note |
|----------|--------------|-----------|---------------|------|
| [Segmento A — es: Free plan] | [X%] | [Y] | [Z%] | [insight] |
| [Segmento B — es: Pro plan] | [X%] | [Y] | [Z%] | [insight] |
| [Segmento C — es: Mobile] | [X%] | [Y] | [Z%] | [insight] |

**Segmento con performance migliore**: [nome] — perché?
**Segmento con gap maggiore**: [nome] — piano di intervento?

---

## 6. Backlog Prioritizzato Post-Launch

Basato su dati 30 giorni, lista ordinata di prossimi passi:

### P0 — Fix obbligatori (entro 2 settimane)
1. [Fix critico] — impatto: [N] utenti — effort: [S/M/L]

### P1 — Iterazioni ad alto valore (prossimo sprint)
1. [Improvement 1] — evidence: [dato] — effort: [S/M/L]
2. [Improvement 2] — evidence: [dato] — effort: [S/M/L]

### P2 — Idee da validare (backlog)
1. [Idea 1] — hypothesis: [cosa si aspetta]
2. [Idea 2]

### Kill list (da rimuovere o non iterare)
1. [Feature/componente] — utilizzo: [X%] — decisione: depreca perché [motivazione]

---

## 7. Verdict: La Feature ha Raggiunto il Suo Obiettivo?

**Score complessivo**: [X/10]

| Dimensione | Score | Note |
|-----------|-------|------|
| Problema risolto? | [1-10] | [evidenza] |
| Metriche raggiunte? | [1-10] | [evidenza] |
| UX quality? | [1-10] | [evidenza] |
| Business impact? | [1-10] | [evidenza] |

**Decisione strategica**:
- 🚀 EXPAND: la feature funziona, investire di più
- 🔄 ITERATE: basi solide, serve ottimizzazione
- 🔬 EXPERIMENT: risultati misti, testare approcci alternativi
- ⏸️ PAUSE: deprioritizzare, risorse su altro
- ☠️ KILL: non ha raggiunto nessun obiettivo, rimuovere

**Motivazione**: [testo]
```

---

## TEMPLATE C — 90-Day Business Impact Review

### Quando usarlo
90 giorni dal lancio. Focus su: impatto business reale, ROI dello sviluppo, decisioni strategiche a lungo termine.

```markdown
# 90-Day Business Impact Review — [Nome Feature/Prodotto]
**Periodo analizzato**: [Data lancio] → [Data +90 giorni]
**PRD originale versione**: [v1.x]
**Executive Sponsor**: [Nome]

---

## 1. Executive Summary (1 pagina max)

**Headline**: [1 frase che riassume il verdict — es: "La feature X ha superato le aspettative di revenue del 40% ma non ha impattato la retention come previsto"]

**3 numeri chiave**:
1. [Metrica 1]: [valore attuale] vs [target PRD] — [+/-X%]
2. [Metrica 2]: [valore attuale] vs [target PRD] — [+/-X%]
3. [Metrica 3]: [valore attuale] vs [target PRD] — [+/-X%]

**Prossima decisione richiesta**: [una sola azione che il leadership deve approvare]

---

## 2. Business Impact Analysis

### Revenue Impact
| Metrica | Pre-lancio | Attuale | Delta | Attribuibile alla feature? |
|---------|-----------|---------|-------|--------------------------|
| MRR | €[X] | €[Y] | +€[Z] | Sì/Parzialmente/No — [motivazione] |
| ARPU | €[X] | €[Y] | +€[Z] | [attribuibilità] |
| Conversion rate trial→paid | [X]% | [Y]% | +[Z]pp | [attribuibilità] |
| Churn rate | [X]% | [Y]% | -[Z]pp | [attribuibilità] |

### Cost Impact
| Costo | Stimato nel PRD | Reale | Delta | Note |
|-------|----------------|-------|-------|------|
| Engineering (ore) | [N ore] | [N ore] | [±X%] | [causa variazione] |
| Infrastructure | €[X]/mese | €[Y]/mese | [±Z] | |
| Support (ticket aggiuntivi) | [N] | [N] | [±Z] | |

**ROI stimato**: [formula: (Revenue generata - Costo sviluppo) / Costo sviluppo × 100] = [X]%
**Payback period**: [N mesi]

---

## 3. Competitive Impact

### Positioned rispetto ai competitor?
| Competitor | Hanno questa feature? | La nostra è migliore/peggiore? | Win rate cambiato? |
|-----------|----------------------|-------------------------------|-------------------|
| [Competitor A] | Sì/No | [Meglio/Peggio/Parità] | [cambiamento] |
| [Competitor B] | Sì/No | [Meglio/Peggio/Parità] | [cambiamento] |

**Win/Loss analysis**: [dai deal persi negli ultimi 90 giorni, questa feature è stata menzionata come fattore in X% dei casi]

---

## 4. Long-Term Signals

### Retention cohort (utenti acquisiti dopo il lancio vs prima)
| Coorte | Day 7 retention | Day 30 retention | Day 90 retention |
|--------|----------------|-----------------|-----------------|
| Pre-lancio feature | [X]% | [Y]% | [Z]% |
| Post-lancio feature | [X]% | [Y]% | [Z]% |
| Delta | [±X]pp | [±Y]pp | [±Z]pp |

**Interpretazione**: [la feature ha migliorato la retention di lungo periodo?]

### NPS longitudinale
| Periodo | NPS score | Promotori % | Detrattori % |
|---------|-----------|------------|-------------|
| Pre-lancio | [X] | [Y]% | [Z]% |
| Post-lancio 30gg | [X] | [Y]% | [Z]% |
| Post-lancio 90gg | [X] | [Y]% | [Z]% |

---

## 5. Lessons Learned (OBBLIGATORIO)

### Cosa ha funzionato meglio del previsto
1. [Insight 1]: [evidenza] — perché è andato bene — cosa replicare
2. [Insight 2]: [evidenza] — [...]
3. [Insight 3]: [evidenza] — [...]

### Cosa non ha funzionato come previsto
1. [Problema 1]: [evidenza] — causa root — cosa cambiare nel processo
2. [Problema 2]: [evidenza] — [...]
3. [Problema 3]: [evidenza] — [...]

### Cosa non sapevamo e avremmo dovuto scoprire prima
1. [Discovery 1]: [come avremmo potuto scoprirlo in discovery] — cambierà il nostro processo PRD?
2. [Discovery 2]: [...]

### Ipotesi del PRD da aggiornare nel processo
| Ipotesi originale nel PRD | Realtà scoperta | Aggiornamento al processo |
|--------------------------|----------------|--------------------------|
| [Es: "gli utenti capiranno X da soli"] | [X% ha avuto bisogno di supporto] | Aggiungere onboarding tooltip per feature complesse |

---

## 6. Strategic Recommendation

### Opzione A — Double Down
**Cosa**: investire [X eng-weeks] per espandere la feature con [funzionalità aggiuntive]
**Perché**: [evidenza che giustifica l'investimento]
**Expected outcome**: [metrica] → [target] entro [data]
**Risk**: [rischio principale]

### Opzione B — Optimize
**Cosa**: iteration mirata su [2-3 punti deboli specifici]
**Perché**: [costi/benefici]
**Expected outcome**: [...]
**Risk**: [...]

### Opzione C — Deprioritize
**Cosa**: mettere in maintenance mode
**Perché**: [ROI insufficiente o opportunity cost]
**Risk**: [...]

**Raccomandazione PM**: [Opzione X] perché [2-3 righe di ragionamento]
**Decisione finale** (da compilare dopo review leadership): [Opzione Y] — [firma + data]
```

---

## Calendario Standard Post-Launch

Include sempre questo calendario nel PRD nella sezione Timeline:

```markdown
## Post-Launch Review Calendar

| Review | Timing | Owner | Partecipanti | Output atteso |
|--------|--------|-------|-------------|---------------|
| Pulse Review | T+14 giorni | PM | PM + Lead Eng | Go/No-Go staged rollout |
| 30-Day Review | T+30 giorni | PM | Full squad | Backlog prioritizzato |
| 90-Day Review | T+90 giorni | PM + VP Product | Leadership | Strategic decision |
| Annual Review | T+365 giorni | PM | Product Leadership | Kill/Expand/Maintain |

**Nota**: le review non sono opzionali. Se mancano i dati → investigare il tracking,
non posticipare la review.
```

---

## Red Flags da Monitorare (alert automatici)

Configura alert automatici per intervenire prima delle review formali:

```markdown
## Alert da Configurare Post-Launch

### Tecnici (Datadog / Sentry)
- Error rate > 1% → PagerDuty immediato
- API P95 > 2x baseline → alert slack engineering
- Uptime < 99.5% → incident response

### Business (PostHog / Amplitude)
- Feature adoption D7 < 10% target → review anticipata
- Support tickets feature-related > 50/settimana → UX review
- Churn rate aumento > 2pp rispetto baseline → escalation

### Revenue (Stripe / ChartMogul)
- MRR weekly drop > 5% → exec alert
- Failed payments spike → billing team + engineering
```
