---
Type: CONCEPT
Status: Active
Tags: #cto #kpi #sicurezza #qualita #stack #debito
Created: 2026-06-17
Last updated: 2026-06-17
---

# KPI — Indicatori Presidiati dalla Figura CTO

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CTO.md` §KPI
> Principio: KPI "da misurare" — nessun numero inventato. Tag [DM] dove i dati non esistono ancora.
> Connessioni: [[cto-tech-debt-tracker]] · [[cto-quality-gate]] · [[cto-security-sentinel]] · [[WF-SECURITY-AUDIT]]

---

## Nota metodologica

I KPI elencati qui sono quelli che la figura CTO è responsabile di presidiare. I valori target
sono dichiarati come target o "da misurare" (DM) in base alla disponibilità di dati reali.
Tag [DM]: la misurazione deve essere attivata prima di assegnare un target numerico.
La fonte del dato (dove si legge lo stato) è indicata per ogni KPI.

---

## KPI 1 — Segreti in Git (security sentinel — post-commit)

**Cosa misura:** il numero di segreti (API key, token, password) trovati nel repo dopo il commit,
ovvero che hanno superato il pre-commit check (se attivo) o che erano presenti prima della
sua attivazione.

**Come si misura:** output di `security_scan_report.py` su tutto il repo. Conteggio finding
con `tipo: "segreto"` e stato "non-risolto". Fonte: `state/security-audit-log.json`.

**Target:** 0 — zero tolerance assoluta. Un solo finding attivo è un incidente.

**Frequenza:** settimanale (WF-SECURITY-AUDIT); on-demand dopo ogni deploy.

---

## KPI 2 — First-Pass QA Rate (gate qualità)

**Cosa misura:** la percentuale di sistemi che superano il quality gate di `cto-quality-gate`
al primo tentativo (senza rework intermedio). Un first-pass rate alto indica che i sistemi
arrivano al gate già maturi; un rate basso indica che la qualità è trasferita al gate invece
di essere costruita nel processo.

**Come si misura:** n. QG con esito PASS alla prima run / n. totale QG eseguiti nel periodo.
Fonte: `state/quality-gate-log.json` (campo `attempt_number`).

**Target:** ≥80% (dal BP-CTO). [DM] — target da calibrare dopo prime 20 quality gate run.

**Frequenza:** settimanale; in ogni WF-REVIEW-TRIMESTRALE.

---

## KPI 3 — Lighthouse Score Medio in Produzione

**Cosa misura:** il Lighthouse score medio dei sistemi web della holding in produzione (media
sui 4 domini: performance, accessibility, SEO, best practices) e il numero di sistemi sotto
la soglia minima ≥90.

**Come si misura:** output di `lighthouse_batch.sh` su tutti gli URL in `state/platform-status.json`
(sistemi in stato "produzione"). Aggregato: media e count <90.

**Target:** 0 sistemi in produzione con score <90. Media holding: [DM] — target a regime.

**Frequenza:** settimanale (nel ciclo WF-SECURITY-AUDIT); post-deploy di ogni sistema web.

---

## KPI 4 — Debito Tecnico Totale (trend)

**Cosa misura:** il numero totale di item di debito tecnico aperti in `state/tech-debt-register.json`
e il trend settimanale (in calo / stabile / in crescita). Non è il numero assoluto a essere
il KPI principale: è il trend. Il debito deve essere "in calo" nel tempo.

**Come si misura:** conteggio item con stato "aperto" in `state/tech-debt-register.json`.
Confronto con la settimana precedente. Fonte: report di `cto-tech-debt-tracker`.

**Target:** trend "in calo" — il numero assoluto dipende dalla fase della holding [DM].
Alert se trend è "in crescita" per 2 settimane consecutive.

**Frequenza:** settimanale (report `cto-tech-debt-tracker`); in ogni WF-REVIEW-TRIMESTRALE.

---

## KPI 5 — 100% Repo Censiti in Architecture-Registry

**Cosa misura:** la percentuale di sistemi attivi della holding che sono censiti nel registro
architetturale (`state/architecture-registry.json`) con versione, blueprint di riferimento,
e ADR di architettura. Un sistema non censito è un sistema non governato.

**Come si misura:** n. sistemi in `state/architecture-registry.json` / n. sistemi identificati
come attivi in `state/platform-status.json`. [DM] — da attivare al primo ciclo di censimento.

**Target:** 100% — ogni sistema attivo deve essere censito.

**Frequenza:** mensile; ogni volta che un nuovo sistema viene deployato in produzione.

---

## KPI 6 — 0 Incidenti Security Post-Deploy

**Cosa misura:** il numero di incidenti di sicurezza rilevati in produzione (non in staging,
non in review) in un dato periodo. Un incidente di sicurezza post-deploy indica che uno dei
gate (security o quality) non ha rilevato il problema in pre-deploy.

**Come si misura:** conteggio record in `state/security-audit-log.json` con
`trigger: "post_deploy"` e gravità `critica | alta`. Fonte: log incidenti `cto-security-sentinel`.

**Target:** 0 incidenti critici post-deploy. Incidenti medi o bassi: [DM] target da definire.

**Frequenza:** per ogni deploy; cumulativo mensile.

---

## KPI 7 — ADR Tecnici Scritti per Decisioni Architetturali

**Cosa misura:** la percentuale di decisioni classificate come "architetturali" (cambiano
struttura, stack, contratti I/O, standard) che hanno prodotto un ADR in `company/Memory/decisions/`.

**Come si misura:** n. ADR con tag `#cto` in `state/adr-index.json` / n. decisioni architetturali
nel log sessioni CTO. Richiede che il conductor classifichi le decisioni in ogni checkpoint.

**Target:** 100% — ogni decisione architetturale produce un ADR. Non negoziabile (ADR-002).

**Frequenza:** per decisione; report aggregato in WF-REVIEW-TRIMESTRALE.

---

## KPI 8 — Sistemi in Produzione con Dry-Run Mode

**Cosa misura:** la percentuale di sistemi deployati in produzione che hanno un dry-run mode
funzionante e verificato. Un sistema senza dry-run è un sistema che non può essere testato
in sicurezza (invariante tecnico R2).

**Come si misura:** n. sistemi in `state/platform-status.json` con `dry_run_verified: true`
/ n. totale sistemi in produzione. Verificato dal `cto-quality-gate` in ogni gate run.

**Target:** 100% — tutti i sistemi in produzione devono avere dry-run mode verificato.

**Frequenza:** per ogni deploy; audit mensile.

---

## Connessioni

- [[cto-tech-debt-tracker]] · `agenti/cto-tech-debt-tracker.md`
- [[cto-quality-gate]] · `agenti/cto-quality-gate.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[WF-SECURITY-AUDIT]] · `workflow/WF-SECURITY-AUDIT.md`
- [[STATE]] · `state/README.md`
- [[SCRIPTS]] · `scripts/README.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
