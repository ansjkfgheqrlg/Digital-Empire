# KPI — Chief-Forge

> Indicatori di performance della figura Chief-Forge.
> Fonte: [[BP-Chief-Forge]] §KPI · [[principi/PRINCIPI.md]] P8 ("prove non promesse")
> Stato: tutti i valori "da misurare" fino a dati storici reali disponibili.

---

## Come si leggono questi KPI

Ogni KPI ha: definizione precisa, formula di calcolo, frequenza di misurazione, owner della
misurazione, fonte del dato. I target sono indicati come "da misurare" quando non esiste ancora
uno storico su cui basare un target credibile (P8: nessun numero senza fonte).

---

## KPI 1 — Tempo Richiesta → Consegna Artefatto

**Definizione:** giorni lavorativi tra la ricezione della richiesta in `board/chief-forge/intake`
e la notifica di consegna all'ecosistema richiedente.

**Formula:** `data_notifica_consegna - data_ricezione_richiesta` (in giorni lavorativi)

**Segmentato per urgenza:**
- CRITICAL: target da misurare (baseline attesa: ≤3gg)
- HIGH: da misurare
- NORMAL: da misurare
- LOW: da misurare (senza SLA — entra in backlog)

**Frequenza misurazione:** per ogni richiesta chiusa

**Owner misurazione:** `cf-memoria`

**Fonte dato:** log `board/chief-forge/intake` (timestamp ricezione) + log `board/chief-forge/registro` (timestamp consegna)

---

## KPI 2 — Eval Score Nuove Skill (Pass Rate)

**Definizione:** percentuale di artefatti che superano il gate eval al PRIMO ciclo con pass_rate ≥85%.

**Formula:** `(artefatti_PASS_ciclo_1 / totale_artefatti_valutati) × 100`

**Target:** da misurare. La soglia gate è ≥85% per singolo artefatto; questo KPI misura
quanti artefatti arrivano a gate già pronti senza iterazione.

**Frequenza misurazione:** mensile

**Owner misurazione:** `cf-eval-warden`

**Fonte dato:** log `board/chief-forge/eval` — campo `ciclo_attuale` al momento del PASS

---

## KPI 3 — Copertura Identity-HR

**Definizione:** percentuale di agenti attivi in EMPIRE OS che sono registrati in Identity-HR
con record completo (nessun campo critico nullo).

**Formula:** `(agenti_registrati_con_record_completo / agenti_esistenti_in_company) × 100`

**Target:** 100% — questo è l'unico KPI con target assoluto fisso (P5: copertura 100% è non negoziabile)

**Frequenza misurazione:** settimanale (audit WF-HR-REGISTRY)

**Owner misurazione:** `cf-agent-registry`

**Fonte dato:** output di `registry-audit.sh` — campo `copertura_percent`

---

## KPI 4 — Skill Orfane o Duplicate nel Catalogo

**Definizione:** numero di skill nel portfolio con `ecosistema_owner = null` (orfane) OR
`duplicato_di != null` (duplicate non risolte).

**Formula:** `COUNT(skill dove ecosistema_owner = null OR duplicato_di != null)`

**Target:** 0 — target assoluto (P6)

**Frequenza misurazione:** settimanale (audit `cf-skill-portfolio`)

**Owner misurazione:** `cf-skill-portfolio`

**Fonte dato:** snapshot `board/chief-forge/portfolio` — campi `ecosistema_owner` e `duplicato_di`

---

## KPI 5 — Cicli Eval Medi per Artefatto

**Definizione:** numero medio di cicli eval necessari per portare un artefatto a PASS.
Un ciclo = un invio a FORGE per iterate + re-eval.

**Formula:** `SUM(cicli_per_artefatto) / COUNT(artefatti_valutati)`

**Target:** da misurare. Il target ideale è 1 (pass al primo ciclo); il limite massimo per
definizione è 2 (dopo il secondo FAIL → escalation, non ulteriore iterate).

**Frequenza misurazione:** mensile

**Owner misurazione:** `cf-eval-warden`

**Fonte dato:** log `board/chief-forge/eval` — campo `ciclo_attuale` al momento del gate

---

## KPI 6 — Proposte Ecosistema con Analisi Completa

**Definizione:** percentuale di proposte ecosistema consegnate al CEO che includono tutti i
campi obbligatori (missione, org chart preview, costo build stimato, costo mensile stimato,
rischi, dipendenze, raccomandazione motivata).

**Formula:** `(proposte_complete / totale_proposte_consegnate) × 100`

**Target:** 100%

**Frequenza misurazione:** ad ogni proposta (evento-driven)

**Owner misurazione:** `cf-ecosystem-builder`

**Fonte dato:** checklist interna CF-PROP

---

## KPI 7 — Decisioni Intake con Motivazione Esplicita

**Definizione:** percentuale di decisioni conductor (BUILD/REUSE/EXTEND/REJECT/DEFER) con
campo `motivo` valorizzato nel log.

**Formula:** `(decisioni_con_motivo / totale_decisioni) × 100`

**Target:** 100% — ogni decisione senza motivazione è un pattern perso per `cf-memoria`

**Frequenza misurazione:** mensile

**Owner misurazione:** `cf-memoria`

**Fonte dato:** log `board/chief-forge/intake` — campo `motivazione_raccomandazione` e decisioni conductor

---

## Dashboard KPI (schema)

| KPI | Valore Attuale | Target | Trend | Owner |
|---|---|---|---|---|
| Tempo richiesta→consegna (CRITICAL) | da misurare | ≤3gg | — | cf-memoria |
| Tempo richiesta→consegna (NORMAL) | da misurare | da misurare | — | cf-memoria |
| Eval PASS ciclo 1 (%) | da misurare | da misurare | — | cf-eval-warden |
| Copertura Identity-HR (%) | da misurare | 100% | — | cf-agent-registry |
| Skill orfane/duplicate | da misurare | 0 | — | cf-skill-portfolio |
| Cicli eval medi | da misurare | da misurare | — | cf-eval-warden |
| Proposte eco complete (%) | da misurare | 100% | — | cf-ecosystem-builder |
| Decisioni intake motivate (%) | da misurare | 100% | — | cf-memoria |

*La dashboard viene alimentata da dati reali dopo le prime forgiature completate.*
