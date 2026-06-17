---
Type: CONCEPT
Status: Active
Tags: #cto #skills #empire-verify #tech-adr #security-preflight
Created: 2026-06-17
Last updated: 2026-06-17
---

# SKILLS — Skill Proprie della Figura CTO

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CTO.md` §Skill
> Connessioni: [[cto-quality-gate]] · [[cto-security-sentinel]] · [[cto-memoria]] · [[FORGE]]

---

## Nota metodologica

Le skill elencate qui sono le skill **proprie** della figura CTO: forgiate da FORGE per uso
specifico di questa figura o dei suoi agenti. Non sono skill generiche del catalogo FORGE:
sono specializzate sul dominio tecnico della holding. Ogni skill ha uno status:
- `attiva`: disponibile per l'uso
- `da-forgiare`: specifica progettata, build ancora da eseguire in FORGE
- `in-beta`: forgiata ma in fase di validazione

---

## SK1 — `empire-verify`

**Status:** da-forgiare
**Usata da:** `cto-quality-gate` (primario), `cto-conductor` (on-demand)
**Tier consigliato:** Sonnet (ha bisogno di analizzare output di tool)

**Scopo:** Esegue la suite completa di verifica tecnica su un sistema della holding:
lint (TypeScript/ESLint) → build (Next.js) → test E2E (playwright) → Lighthouse →
brand gate (conformità `empire-style`) → struttura cartelle → dry-run mode check.
Produce un report strutturato con esito globale (PASS/BLOCKED/WARNING) e lista dettagliata
di ogni check con esito, errori, e fix azionabili.

**Input:**
```json
{
  "path": "company/path/al/sistema",
  "checks": ["lint", "build", "playwright", "lighthouse", "brand", "struttura", "dry_run"],
  "lighthouse_target": 90,
  "ambiente": "local | staging"
}
```

**Output:**
```json
{
  "esito": "PASS | BLOCKED | WARNING",
  "check_results": {"lint": "pass|fail", "build": "pass|fail", "playwright": "pass|fail",
    "lighthouse": {"esito": "pass|fail", "score": 0}, "brand": "pass|fail",
    "struttura": "pass|fail", "dry_run": "pass|fail"},
  "problemi": [{"check": "string", "descrizione": "string", "fix": "string"}]
}
```

**Acceptance criteria per la build:**
- Gira senza errori su un repo conforme al template empire.
- Ritorna BLOCKED se anche solo un check bloccante fallisce.
- Ritorna WARNING (non BLOCKED) per problemi non bloccanti.
- Produce problemi con fix azionabili (non generici).

---

## SK2 — `tech-adr`

**Status:** da-forgiare
**Usata da:** `cto-memoria` (primario)
**Tier consigliato:** Haiku (scrittura strutturata, non analisi)

**Scopo:** Redige un ADR tecnico a partire da una decisione strutturata. Verifica che l'ID
sia progressivo e non in conflitto con ADR esistenti. Verifica che il nuovo ADR non contraddica
ADR attivi prima di produrre il draft. Salva il file in `company/Memory/decisions/` con il
naming convention standard (`ADR-NNN-titolo-kebab.md`).

**Input:**
```json
{
  "titolo": "Aggiornamento Next.js 14→15",
  "contesto": "Descrizione del problema che la decisione risolve",
  "decisione": "Testo della decisione presa",
  "conseguenze": ["conseguenza 1", "conseguenza 2"],
  "sostituisce": "ADR-NNN | null",
  "firma": "cto-conductor — YYYY-MM-DD",
  "tag": ["#cto", "#stack", "#nextjs"]
}
```

**Output:**
```json
{
  "adr_id": "ADR-NNN",
  "path": "company/Memory/decisions/ADR-NNN-aggiornamento-nextjs-14-15.md",
  "contraddizioni_trovate": [],
  "scritto": true
}
```

**Acceptance criteria per la build:**
- ID progressivo corretto (no conflitti).
- File scritto nel formato standard con tutti i campi obbligatori.
- Contraddiction check eseguito e risultato incluso nell'output.

---

## SK3 — `security-preflight`

**Status:** da-forgiare
**Usata da:** `cto-security-sentinel` (primario), `cto-forge-liaison` (gate pre-catalogo)
**Tier consigliato:** Sonnet

**Scopo:** Esegue un preflight di sicurezza rapido (più veloce di un audit completo) su
un target specifico: segreti hardcoded, PII in output, CVE critiche nelle dipendenze dichiarate,
pattern injection in prompt di agenti. Progettata per essere eseguita in automatico come
parte di ogni WF-TECH-REVIEW senza richiedere una sessione separata di audit.

**Input:**
```json
{
  "target_path": "company/path/o/file",
  "check_types": ["segreti", "pii", "cve", "injection"],
  "dipendenze_file": "package.json | null",
  "modalita": "fast | thorough"
}
```

**Output:**
```json
{
  "esito": "PASS | BLOCKED | WARNING",
  "findings": [
    {
      "tipo": "segreto | pii | cve | injection",
      "gravita": "critica | alta | media | bassa",
      "posizione": "file:linea",
      "fix": "string"
    }
  ],
  "blocco_attivo": false
}
```

**Acceptance criteria per la build:**
- Rileva pattern di segreti comuni (API key `sk_`, token `Bearer`, password in variabili).
- Usa `aidefence_has_pii` MCP se disponibile per il check PII.
- Produce findings con posizione esatta (file + linea), non solo il tipo di problema.
- Modalità `fast` completa in <30 secondi su repo standard.

---

## Note per FORGE

Queste 3 skill sono da forgiare nella prossima sessione FORGE disponibile.
Priorità: (1) `empire-verify` — è il gate di qualità principale; (2) `security-preflight` —
è il gate di sicurezza rapido; (3) `tech-adr` — è il writer degli ADR.

Brief completo per FORGE: inviare via `cto-forge-liaison` con schema I/O sopra come specifica.

---

## Connessioni

- [[cto-quality-gate]] · `agenti/cto-quality-gate.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[cto-forge-liaison]] · `agenti/cto-forge-liaison.md`
- [[WF-TECH-REVIEW]] · `workflow/WF-TECH-REVIEW.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
