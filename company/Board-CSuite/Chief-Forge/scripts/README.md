# SCRIPTS — Chief-Forge

> Script previsti per la figura Chief-Forge. Descrizione funzionale, I/O, stato.
> Questi script non esistono ancora: vanno forgiati via WF-CAPABILITY-INTAKE.
> Fonte: [[BP-Chief-Forge]] · [[skills/SKILLS.md]] · [[07-FORGE/ECOSISTEMA.md]]

---

## Script 1: `intake-validate.sh`

**Scopo:** validazione rapida del formato di una richiesta capability in ingresso.
Usato da `cf-intake-router` come pre-check prima dell'analisi completa.

**Input:**
```bash
intake-validate.sh --request '{"ecosistema_richiedente":"XX","gap_descritto":"...","tipo_richiesta":"skill","urgenza":"NORMAL"}'
```

**Output (stdout):**
```json
{
  "valid": true,
  "campi_mancanti": [],
  "warnings": ["budget_disponibile non specificato — default: non specificato"]
}
```

**Logica:** controlla presenza campi obbligatori (`ecosistema_richiedente`, `gap_descritto`,
`tipo_richiesta`, `urgenza`), valida l'enum dei valori (tipo deve essere in `[skill, agente, team, workflow, ecosistema]`,
urgenza in `[CRITICAL, HIGH, NORMAL, LOW]`), genera warning per campi opzionali assenti.

**Exit codes:** 0 = valido; 1 = campi mancanti critici; 2 = enum non valido

**Stato:** da forgiare | Path previsto: `company/Board-CSuite/Chief-Forge/scripts/intake-validate.sh`

---

## Script 2: `registry-audit.sh`

**Scopo:** audit automatico del registro Identity-HR. Scansiona `company/` alla ricerca di
schede agente e confronta con il namespace `board/chief-forge/registry`. Produce report
anomalie in JSON.

**Input:**
```bash
registry-audit.sh --company-root /path/to/company --registry-namespace board/chief-forge/registry
```

**Output (file JSON + stdout summary):**
```json
{
  "audit_date": "YYYY-MM-DD",
  "agenti_trovati_in_company": 0,
  "agenti_nel_registro": 0,
  "copertura_percent": 0,
  "anomalie": {
    "fantasmi": ["agente-senza-scheda"],
    "non_registrati": ["scheda-trovata-senza-record"],
    "orfani": ["agente-senza-ecosistema-owner"],
    "degradati": ["agente-con-eval-score-sotto-70"]
  }
}
```

**Logica:** trova tutti i file `*.md` nelle cartelle `Agenti/` di `company/`; estrae l'ID agente
dal frontmatter o dall'intestazione; confronta con il registro; classifica le discrepanze;
calcola la copertura percentuale.

**Trigger:** eseguito dal workflow WF-HR-REGISTRY ogni lunedì; eseguibile on-demand da conductor.

**Stato:** da forgiare | Path previsto: `company/Board-CSuite/Chief-Forge/scripts/registry-audit.sh`

---

## Script 3: `eval-gate-check.sh`

**Scopo:** verifica rapida se un artefatto supera la soglia eval. Usato da `cf-eval-warden`
come sanity check immediato sull'eval_report grezzo di FORGE.

**Input:**
```bash
eval-gate-check.sh --eval-report path/to/eval_report.json --threshold 85
```

**Output:**
```json
{
  "pass": true,
  "pass_rate": 91,
  "threshold": 85,
  "test_count": 11,
  "failures": [],
  "gate_decision": "PASS"
}
```

**Logica:** legge il JSON dell'eval_report, estrae `pass_rate`, confronta con la soglia,
lista i failures se presenti, emette `gate_decision` PASS/FAIL con motivazione.

**Exit codes:** 0 = PASS; 1 = FAIL; 2 = eval_report malformato

**Stato:** da forgiare | Path previsto: `company/Board-CSuite/Chief-Forge/scripts/eval-gate-check.sh`

---

## Script 4: `capability-gap-scan.sh`

**Scopo:** scansione rapida del portfolio skill e del registro agenti per identificare gap
evidenti (skill richieste da ecosistemi ma non presenti, agenti con dipendenze non soddisfatte).

**Input:**
```bash
capability-gap-scan.sh --scope holding --roadmap path/to/roadmap.json
```

**Output:**
```json
{
  "scan_date": "YYYY-MM-DD",
  "gap_count": 0,
  "gap": [
    {
      "tipo": "skill_mancante | agente_mancante",
      "nome": "...",
      "richiesto_da": ["XX-ECO"],
      "impatto": "CRITICO | ALTO | BASSO"
    }
  ],
  "raccomandazioni": ["avvia WF-CAPABILITY-INTAKE per: ..."]
}
```

**Logica:** legge `board/chief-forge/portfolio` (skill) e `board/chief-forge/registry` (agenti),
confronta con le dipendenze dichiarate nella roadmap e nelle schede agente, identifica gap
per priorità impatto. Output usato da `capability-gap-radar` come fonte dati principale.

**Stato:** da forgiare | Path previsto: `company/Board-CSuite/Chief-Forge/scripts/capability-gap-scan.sh`

---

## Note generali

Tutti gli script sono **descritti funzionalmente** qui. Il codice reale viene forgiato da FORGE
(via WF-CAPABILITY-INTAKE, tipo `skill` o `workflow`) quando la skill `forge-intake` è operativa.

Lo stack previsto: Bash (compatibile con il monorepo su Windows/Bash, usando Git Bash).
Nessuno script ha dipendenze esterne non disponibili nel monorepo.
