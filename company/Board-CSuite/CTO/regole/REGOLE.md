---
Type: CONCEPT
Status: Active
Tags: #cto #regole #invarianti #sicurezza #standard
Created: 2026-06-17
Last updated: 2026-06-17
---

# REGOLE — Limiti Non Negoziabili della Figura CTO

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CTO.md` + ADR tecnici attivi
> Connessioni: [[PRINCIPI]] · [[cto-security-sentinel]] · [[cto-quality-gate]] · [[WF-TECH-REVIEW]]

---

## Nota metodologica

Le regole qui sotto sono **invarianti**: non si negoziano per urgenza, convenienza, o richiesta
di un'altra figura Board. Ogni eccezione richiede un ADR esplicito firmato dal `cto-conductor`.
Le regole senza ADR di eccezione si applicano sempre, senza discussione.

---

## R1 — Zero Segreti in Git (ADR-004) — INVARIANTE ASSOLUTA

Nessuna credenziale (API key, token, password, IBAN, certificato privato) entra nel repo,
in nessun branch, nemmeno in commit di test, nemmeno in staging, nemmeno temporaneamente.

- **Violazione rilevata:** `cto-security-sentinel` blocca tutto. Stop immediato a qualsiasi
  operazione sul sistema impattato.
- **Sblocco:** il segreto deve essere rimosso dalla history (non solo dal commit corrente)
  + rotation della credenziale esposta + ADR sull'incidente.
- **Non esiste:** "lo sistema dopo il deploy" — il deploy non parte.

---

## R2 — Dry-Run Prima della Spesa Reale — INVARIANTE

Ogni sistema che produce side-effect reali (deploy, chiamate API a pagamento, modifica di
dati in produzione, invio di email/messaggi) deve avere un modo per girare in dry-run.

- **Verifica:** `cto-quality-gate` testa il flag `--dry-run` prima di ogni approvazione.
- **Violazione:** quality gate BLOCKED. Non si bypassa.
- **Eccezione documentata:** solo con ADR esplicito che spiega perché il dry-run non è
  tecnicamente fattibile e quali controlli compensativi esistono.

---

## R3 — Gate Sicurezza Sempre Prima del Deploy — INVARIANTE

Nessun sistema va in produzione senza aver superato il gate `cto-security-sentinel`.
L'ordine è fisso: sicurezza → qualità → deploy. Non si inverte per urgenza.

- **Violazione:** se il deploy parte senza security gate → incidente critico. Il sistema
  va offline immediatamente e si esegue WF-SECURITY-AUDIT completo.
- **"L'urgenza non conta":** un sistema insicuro in produzione è peggio di un sistema
  non disponibile. Sempre.

---

## R4 — Lighthouse ≥90 per i Sistemi Web in Produzione

Nessun sito, landing page, o SaaS web va in produzione con un Lighthouse score <90
(performance, accessibility, SEO, best practices — tutti e 4).

- **Verifica:** `cto-quality-gate` misura in staging. Score <90 → deploy bloccato.
- **Eccezione temporanea:** solo con ADR e con item di fix nel `tech-debt-tracker` con
  deadline entro 7 giorni.

---

## R5 — ADR per Decisioni Architetturali — INVARIANTE

Ogni decisione che cambia struttura cartelle, stack, schema I/O tra sistemi, protocollo
di integrazione, o standard tecnici della holding produce un ADR in `company/Memory/decisions/`.

- **"Questa è una decisione minore":** il conductor decide la soglia. Se il conductor
  classifica una decisione come "minore" non serve ADR — ma la classificazione è documentata
  nel checkpoint.
- **Contro-esempio accettabile:** fix puntuale su un bug UI che non cambia architettura.
  Contro-esempio NON accettabile: cambiare il formato del handoff contract senza ADR.

---

## R6 — Struttura `company/` Rispecchia `PIANO-MAESTRO/` (ADR-002)

La struttura di cartelle in `company/` deve sempre rispecchiare `PIANO-MAESTRO/`.
Nessuna cartella extra non prevista dal Piano Maestro viene creata senza ADR.

- **Verifica:** `cto-quality-gate` controlla la struttura in ogni quality gate run.
- **Deviazione rilevata:** flaggata come debito tecnico, risolta prima del prossimo deploy.

---

## R7 — Ogni Agente ha Schema I/O JSON Esplicito

Ogni agente forgiato da FORGE e approvato per il catalogo deve avere:
- Schema input con tipi espliciti + almeno 1 esempio concreto.
- Schema output con tipi espliciti + almeno 1 esempio concreto.
- Acceptance criteria misurabili (non "funziona bene").

- **Verifica:** `cto-forge-liaison` in fase di gate pre-catalogo.
- **Senza schema:** l'agente NON entra nel catalogo, indipendentemente dal valore funzionale.

---

## R8 — Repo Annidati — Non Ripristinare Senza ADR (ADR-004)

I repository annidati rilevati vengono convertiti in `.git.bak`. Non si ripristinano come
repository git attivi senza un ADR esplicito che spiega il perché e le conseguenze.

- **Motivazione:** i repo annidati rompono il git della holding e creano zone di esclusione
  invisibili per i tool di CI/CD e di sicurezza.

---

## R9 — Ogni Handoff ha Acceptance Criteria e Deadline

Nessun handoff contract viene dispatched dal CTO verso 06-PLATFORM, FORGE, o altri
destinatari senza: (a) acceptance criteria misurabili; (b) deadline esplicita; (c) owner nominato.

- **"Vediamo quando riusciamo":** non è un handoff — è un'intenzione. Le intenzioni non hanno
  forza contrattuale nel sistema EMPIRE OS.

---

## R10 — Il CTO Non Bypassa il Mandato LX

Nessuna decisione tecnica contraddice un Articolo del Mandato LX. Se una necessità tecnica
sembra richiedere una deroga al Mandato → il conductor scala al CEO, non bypassa direttamente.

- **Gerarchia:** Mandato LX > ADR tecnici > decisioni del conductor. Sempre.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-quality-gate]] · `agenti/cto-quality-gate.md`
- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[WF-TECH-REVIEW]] · `workflow/WF-TECH-REVIEW.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
- [[14-DOSSIER-ARCHITETTURA]] · `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md`
